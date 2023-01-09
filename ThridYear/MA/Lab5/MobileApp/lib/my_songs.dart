import 'dart:async';

import 'package:connectivity_plus/connectivity_plus.dart';
import "package:flutter/material.dart";
import 'package:lab3/Service/Service.dart';
import 'package:lab3/create_song.dart';
import 'package:lab3/Domain/playlist.dart';
import 'package:lab3/Repository/database.dart';

import 'Domain/song.dart';

class MySongs extends StatefulWidget {
  Playlist _playlist;

  MySongs(this._playlist, {super.key});

  @override
  State<StatefulWidget> createState() => _MySongs();
}

class _MySongs extends State<MySongs> {
  late List<Song> _songs;
  Service service = Service();
  late ConnectivityResult status;
  late StreamSubscription<ConnectivityResult> subscription;

  @override
  void initState() {
    _songs = widget._playlist.songs;
    subscription = Connectivity()
        .onConnectivityChanged
        .listen((ConnectivityResult result) {
      print("Internet connection changed! New connection: $result");
      status = result;
    });
    Connectivity().checkConnectivity().then((value) {
      setState(() {
        status = value;
      });
    });
    super.initState();
  }

  @override
  void dispose() {
    subscription.cancel();
    super.dispose();
  }

  bool checkIfConnected() {
    return status != ConnectivityResult.none &&
        status != ConnectivityResult.bluetooth;
  }

  void deleteSong(int index) async {
    int id = _songs[index].id;
    print("Deleting song with id $id");
    if (checkIfConnected()) {
      await service.deleteSong(id);
      setState(() {
        _songs.removeAt(index);
      });
      PlaylistDatabase.instance.deletePlaylist(id);
    } else {
      // await PlaylistDatabase.instance.deletePlaylist(id);
    }
    Navigator.of(context).pop();
  }

  void updateSong(Song? song) async {
    if (song != null) {
      print("Updating song to $song");
      if (checkIfConnected()) {
        await service.updateSong(song);
        PlaylistDatabase.instance.updateSong(song);
        setState(() {
          int index = _songs.indexOf(song);
          _songs[index] = song;
        });
      } else {
        // await PlaylistDatabase.instance.updateSong(song);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
        itemCount: _songs.length,
        itemBuilder: (context, index) {
          return ListTile(
            onTap: () {},
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
                        deleteSong(index);
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
            leading: Icon(Icons.music_note),
            title: Text(
                "${_songs[index].name}\t\t\t-\t\t\t${_songs[index].author}"),
            subtitle:
                Text("Duration: ${_songs[index].duration.toString()}\t\t\t"
                    "Genre: ${_songs[index].genre}"),
            trailing: TextButton(
              onPressed: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (_) => CreateSong(
                              playlistId: widget._playlist.id,
                              song: _songs[index],
                            ))).then((song) async => {
                              updateSong(song)
                });
              },
              child: Icon(Icons.edit),
            ),
          );
        });
  }
}
