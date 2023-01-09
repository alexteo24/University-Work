import 'dart:async';

import 'package:connectivity_plus/connectivity_plus.dart';
import "package:flutter/material.dart";
import 'package:lab3/Service/Service.dart';
import 'package:lab3/create_playlist.dart';
import 'package:lab3/display_playlist.dart';
import 'package:lab3/Domain/playlist.dart';
import 'package:lab3/Repository/database.dart';
import 'package:loading_indicator/loading_indicator.dart';

class MyPlaylists extends StatefulWidget {
  final String _title;

  MyPlaylists(this._title);

  @override
  State<StatefulWidget> createState() => _MyPlaylists();
}

class _MyPlaylists extends State<MyPlaylists> {
  List<Playlist> playlists = [];
  Service service = Service();
  late ConnectivityResult status;
  late StreamSubscription<ConnectivityResult> subscription;

  bool isLoading = false;

  @override
  void initState() {
    super.initState();
    Connectivity().checkConnectivity().then((value) {
      setState(() {
        status = value;
      });
      initializePlaylists();
    });
    subscription = Connectivity()
        .onConnectivityChanged
        .listen((ConnectivityResult result) {
      print("Internet connection changed! New connection: $result");
      if (status == ConnectivityResult.none &&
          result != ConnectivityResult.none) {
        syncWithServer();
      }
      status = result;
    });
  }

  @override
  void dispose() {
    print("Cleaning up!");
    PlaylistDatabase.instance.close();
    subscription.cancel();
    super.dispose();
  }

  void syncWithServer() async {
    print("Syncing data with server...");
    service.getAllPlaylists().then((playlists) {
      playlists.forEach((element) {
        PlaylistDatabase.instance.getPlaylistById(element.local).then((value) async {
          if (value != null) {
            await PlaylistDatabase.instance.createPlaylist(value);
            value.songs.forEach((element) {
              PlaylistDatabase.instance.addSongToPlaylist(element);
            });
          }
        });
      });
    });
  }

  bool checkIfConnected() {
    return status != ConnectivityResult.none &&
        status != ConnectivityResult.bluetooth;
  }

  void initializePlaylists() {
    print("Initializing playlist data...");
    if (checkIfConnected()) {
      syncWithServer();
      service.getAllPlaylists().then((value) {
        print("Retrieving data from server");
        setState(() {
          playlists = value;
        });
      });
    } else {
      PlaylistDatabase.instance.getPlaylists().then((value) {
        print("Retrieving data from local db");
          setState(() {
              playlists = value;
            });
          });
    }
  }

  void deletePlaylist(int index) async {
    int id = playlists[index].id;
    print("Deleting playlist with id $id");
    if (checkIfConnected()) {
      await service.deletePlaylist(id);
      PlaylistDatabase.instance.deletePlaylist(id);
    } else {
      // await PlaylistDatabase.instance.deletePlaylist(id);
    }
    Navigator.of(context).pop();
    setState(() {
      playlists.removeAt(index);
    });
  }

  void addPlaylist(Playlist? playlist) async {
    print("Adding new playlist $playlist");
    if (playlist != null) {
      Playlist addedPlaylist;
      if (checkIfConnected()) {
        addedPlaylist = await service.addPlaylist(playlist);
        PlaylistDatabase.instance.createPlaylist(playlist);
        setState(() {
          playlists.add(addedPlaylist);
        });
      } else {
        // addedPlaylist =
        //     await PlaylistDatabase.instance.createPlaylist(playlist);
      }
    }
  }

  void updatePlaylist(Playlist? playlist) async {
    if (playlist != null) {
      print("Updating playlist to $playlist");
      if (checkIfConnected()) {
        await service.updatePlaylist(playlist);
        setState(() {
          int index = playlists.indexOf(playlist);
          playlists[index] = playlist;
        });
        PlaylistDatabase.instance.updatePlaylist(playlist);
      } else {
        // await PlaylistDatabase.instance.updatePlaylist(playlist);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget._title),
      ),
      body: ListView.builder(
          itemCount: playlists.length,
          itemBuilder: (context, index) {
            return ListTile(
              onTap: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (_) => DisplayPlaylist(
                              playlists[index],
                            )));
              },
              onLongPress: () {
                AlertDialog alert = AlertDialog(
                  title: Text("Notice"),
                  content: Text("Are you sure you want to delete the element?"),
                  actions: [
                    TextButton(
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                        child: Text("Cancel")),
                    TextButton(
                        onPressed: () async {
                          deletePlaylist(index);
                        },
                        child: Text("Continue"))
                  ],
                );
                showDialog(
                  context: context,
                  builder: (BuildContext context) {
                    return alert;
                  },
                );
              },
              title: Text(
                  "${playlists[index].name}\t\t\t-\t\t\t${playlists[index].createdBy}"),
              subtitle: Text("Duration: ${playlists[index].duration}"),
              trailing: TextButton(
                onPressed: () {
                  Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (_) => CreatePlaylist(playlists[index])))
                      .then((playlist) async => {updatePlaylist(playlist)});
                },
                child: Icon(Icons.edit),
              ),
            );
          }),
      floatingActionButton: FloatingActionButton(
          onPressed: () {
            Navigator.push(context,
                    MaterialPageRoute(builder: (_) => CreatePlaylist()))
                .then((playlist) async {
              addPlaylist(playlist);
            });
          },
          tooltip: "Add playlist",
          child: const Icon(Icons.add)),
    );
  }
}
