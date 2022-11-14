import "package:flutter/material.dart";
import 'package:lab3/create_playlist.dart';
import 'package:lab3/create_song.dart';
import 'package:lab3/playlist.dart';

import 'my_songs.dart';

class DisplayPlaylist extends StatefulWidget {
  Playlist _playlist;

  DisplayPlaylist(this._playlist);

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
      body: MySongs(widget._playlist),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
                  context, MaterialPageRoute(builder: (_) => CreateSong()))
              .then((song) => {
                    if (song != null)
                      {
                        setState(() {
                          song.id = widget._playlist.songs.isEmpty
                            ? 1
                            : widget._playlist.songs.last.id + 1;
                          widget._playlist.songs.add(song);
                        })
                      }
                  });
        },
        tooltip: "Add new song",
        child: const Icon(Icons.add),
      ),
    );
  }
}
