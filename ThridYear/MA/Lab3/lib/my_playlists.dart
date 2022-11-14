import "package:flutter/material.dart";
import 'package:lab3/create_playlist.dart';
import 'package:lab3/display_playlist.dart';
import 'package:lab3/playlist.dart';

class MyPlaylists extends StatefulWidget {
  final String _title;
  MyPlaylists(this._title);

  @override
  State<StatefulWidget> createState() => _MyPlaylists();

}

class _MyPlaylists extends State<MyPlaylists> {
  List<Playlist> playlists = [Playlist.defaultPlaylist(1),
    Playlist.defaultPlaylist(2),
    Playlist.defaultPlaylist(3),
    Playlist.defaultPlaylist(4),
    Playlist.defaultPlaylist(5),
  ];

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
                  MaterialPageRoute(builder: (_) =>
                      DisplayPlaylist(playlists[index])));
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
                      child: Text("Cancel"))
                ,
                TextButton(
                    onPressed: () {
                      setState(() {
                        playlists.removeAt(index);
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
            title: Text("${playlists[index].name}\t\t\t-\t\t\t${playlists[index].createdBy}"),
            subtitle: Text("Duration: ${playlists[index].duration}\t\t\tNo songs: ${playlists[index].songs.length}"),
            trailing: TextButton(
              onPressed: () {
                Navigator.push(
                    context, MaterialPageRoute(builder: (_) => CreatePlaylist(playlists[index])))
                    .then((playlist) => {
                      if (playlist != null) {
                        setState(() {
                          int index = playlists.indexOf(playlist);
                          playlists[index] = playlist;
                        })
                      }
                });
              },
              child: Icon(Icons.edit),
            ),
          );
        }),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
              context, MaterialPageRoute(builder: (_) => CreatePlaylist()))
              .then((playlist) {
                if (playlist != null) {
                  setState(() {
                    playlist.id = playlists.last.id + 1;
                    playlists.add(playlist);
                  });
                }
          });
        },
        tooltip: "Add playlist",
        child: const Icon(Icons.add)
      ),
    );
  }

}