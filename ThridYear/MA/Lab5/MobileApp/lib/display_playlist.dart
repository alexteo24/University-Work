import 'dart:async';

import 'package:connectivity_plus/connectivity_plus.dart';
import "package:flutter/material.dart";
import 'package:lab3/Service/Service.dart';
import 'package:lab3/create_song.dart';
import 'package:lab3/Domain/playlist.dart';
import 'package:lab3/Repository/database.dart';
import 'package:lab3/Domain/song.dart';

import 'my_songs.dart';

class DisplayPlaylist extends StatefulWidget {
  final Playlist _playlist;

  const DisplayPlaylist(this._playlist, {super.key});

  @override
  State<StatefulWidget> createState() => _DisplayPlaylist();
}

class _DisplayPlaylist extends State<DisplayPlaylist> {
  Service service = Service();
  late ConnectivityResult status;
  late StreamSubscription<ConnectivityResult> subscription;

  @override
  void initState() {
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

  void addSong(Song? song) async {
    if (song != null)
    {
      print("Adding new song to current playlist $song");
      Song addedSong;
      if (checkIfConnected()) {
        addedSong = await service.addSong(song);
      } else {
        addedSong = await PlaylistDatabase.instance.addSongToPlaylist(song);
      }
        addedSong.playlistId = song.playlistId;
      setState(() {
        widget._playlist.songs.add(addedSong);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget._playlist.name),
      ),
      body:
      MySongs(widget._playlist),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
                  context, MaterialPageRoute(builder: (_) => CreateSong(playlistId: widget._playlist.id, song: null)))
              .then((song) async {
                    addSong(song);
                  });
        },
        tooltip: "Add new song",
        child: const Icon(Icons.add),
      ),
    );
  }
}
