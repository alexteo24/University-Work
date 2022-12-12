import 'package:flutter/material.dart';
import 'package:lab3/Domain/playlist.dart';
import 'package:lab3/Domain/song.dart';
import 'package:lab3/text_box.dart';

class CreatePlaylist extends StatefulWidget {
  Playlist? _playlist;

  CreatePlaylist([this._playlist]);

  @override
  State<StatefulWidget> createState() => _CreatePlaylist();

}

class _CreatePlaylist extends State<CreatePlaylist> {
  late int _id;
  late List<Song> _songs;
  late TextEditingController nameController;
  late TextEditingController durationController;
  late TextEditingController createdByController;

  @override
  void initState() {
    _songs = (widget._playlist == null ? [] : widget._playlist?.songs)!;
    _id = (widget._playlist == null ? -1 : widget._playlist?.id)!;
    nameController = widget._playlist == null
        ? TextEditingController()
        : TextEditingController(text: widget._playlist?.name);
    durationController = widget._playlist == null
        ? TextEditingController()
        : TextEditingController(text: widget._playlist?.duration.toString());
    createdByController = widget._playlist == null
        ? TextEditingController()
        : TextEditingController(text: widget._playlist?.createdBy);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Playlist details"),
      ),
      body: ListView(
        children: [
          TextBox(nameController, "Name"),
          TextBox(durationController, "Duration"),
          TextBox(createdByController, "Created by"),
          ElevatedButton(
              onPressed: () {
                String name = nameController.text;
                int duration = int.parse(durationController.text);
                String createdBy = createdByController.text;

                Playlist newPlaylist = Playlist(_id, name, duration, createdBy, "def", _songs);
                Navigator.pop(context, newPlaylist);
              },
              child: Text("Save playlist")
          )
        ],
      ),
    );
  }

}