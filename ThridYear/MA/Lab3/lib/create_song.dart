import "package:flutter/material.dart";
import 'package:lab3/song.dart';
import 'package:lab3/text_box.dart';

class CreateSong extends StatefulWidget {
  Song? _song;


  CreateSong([this._song]);

  @override
  State<StatefulWidget> createState() => _CreateSong();

}

class _CreateSong extends State<CreateSong> {
  late int id;
  late TextEditingController nameController;
  late TextEditingController durationController;
  late TextEditingController authorController;
  late TextEditingController genreController;
  late TextEditingController urlController;

  @override
  void initState() {
    id = (widget._song == null ? -1 : widget._song?.id)!;
    nameController = widget._song == null
        ? TextEditingController()
        : TextEditingController(text: widget._song?.name);
    durationController = widget._song == null
        ? TextEditingController()
        : TextEditingController(text: widget._song?.duration.toString());
    authorController = widget._song == null
        ? TextEditingController()
        : TextEditingController(text: widget._song?.author);
    genreController = widget._song == null
        ? TextEditingController()
        : TextEditingController(text: widget._song?.genre);
    urlController = widget._song == null
        ? TextEditingController()
        : TextEditingController(text: widget._song?.url);
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Song details"),
      ),
      body: ListView(
        children: [
          TextBox(nameController, "Name"),
          TextBox(durationController, "Duration"),
          TextBox(authorController, "Author"),
          TextBox(genreController, "Genre"),
          TextBox(urlController, "Url"),
          ElevatedButton(
              onPressed: () {
                String name = nameController.text;
                int duration = int.parse(durationController.text);
                String author = authorController.text;
                String genre = genreController.text;
                String url = urlController.text;

                Song newSong = Song(id, name, duration, author, genre, url);
                Navigator.pop(context, newSong);
              },
              child: Text("Save song"))
        ],
      ),
    );
  }

}