import "package:flutter/material.dart";
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
                    if (song != null)
                      {
                        Song addedSong = await PlaylistDatabase.instance.addSongToPlaylist(song);
                        setState(() {
                          widget._playlist.songs.add(addedSong);
                        });
                      }
                  });
        },
        tooltip: "Add new song",
        child: const Icon(Icons.add),
      ),
    );
  }
}
