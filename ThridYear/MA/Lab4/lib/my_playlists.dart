import "package:flutter/material.dart";
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

  bool isLoading = false;

  @override void initState() {
    super.initState();
    refreshPlaylists();
  }

  @override void dispose() {
    PlaylistDatabase.instance.close();

    super.dispose();
  }

  void refreshPlaylists()  {
    PlaylistDatabase.instance.getPlaylists().then((value) => {
      setState(() {
        playlists = value;
      })
    });
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
                        onPressed: () async {
                          await PlaylistDatabase.instance.deletePlaylist(
                              playlists[index].id);
                          Navigator.of(context).pop();
                          setState(() {
                            playlists.removeAt(index);
                          });
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
                  "${playlists[index].name}\t\t\t-\t\t\t${playlists[index]
                      .createdBy}"),
              subtitle: Text("Duration: ${playlists[index].duration}"),
              trailing: TextButton(
                onPressed: () {
                  Navigator.push(
                      context, MaterialPageRoute(
                      builder: (_) => CreatePlaylist(playlists[index])))
                      .then((playlist) async =>
                  {
                    if (playlist != null) {
                      await PlaylistDatabase.instance.updatePlaylist(playlist),
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
                .then((playlist) async {
              if (playlist != null) {
                Playlist addedPlaylist = await PlaylistDatabase.instance
                    .createPlaylist(playlist);
                setState(() {
                  playlists.add(addedPlaylist);
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