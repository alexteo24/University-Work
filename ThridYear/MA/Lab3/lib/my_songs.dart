import "package:flutter/material.dart";
import 'package:lab3/create_song.dart';
import 'package:lab3/playlist.dart';

import 'song.dart';

class MySongs extends StatefulWidget {
  Playlist _playlist;

  MySongs(this._playlist, {super.key});

  @override
  State<StatefulWidget> createState() => _MySongs();
}

class _MySongs extends State<MySongs> {
  late List<Song> _songs;

  @override
  void initState() {
    _songs = widget._playlist.songs;
    super.initState();
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
                      child: Text("Cancel"))
                  ,
                  TextButton(
                      onPressed: () {
                        setState(() {
                          _songs.removeAt(index);
                        }) ;
                        Navigator.of(context).pop();
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
            title: Text("${_songs[index].name}\t\t\t-\t\t\t${_songs[index].author}"),
            subtitle: Text("Duration: ${_songs[index].duration.toString()}\t\t\t"
                "Genre: ${_songs[index].genre}"),
            trailing: TextButton(
              onPressed: () {
                Navigator.push(
                    context, MaterialPageRoute(builder: (_) => CreateSong(_songs[index])))
                    .then((song) => {
                  if (song != null) {
                    setState(() {
                      int index = _songs.indexOf(song);
                      _songs[index] = song;
                    })
                  }
                });
              },
              child: Icon(Icons.edit),
            ),
          );
        }
    );
  }
}
