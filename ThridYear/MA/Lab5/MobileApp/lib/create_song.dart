import "package:flutter/material.dart";
import 'package:lab3/Domain/song.dart';
import 'package:lab3/text_box.dart';

class CreateSong extends StatefulWidget {
  Song? song;
  int? playlistId;


  CreateSong({required this.playlistId, required this.song });

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
    id = (widget.song == null ? -1 : widget.song?.id)!;
    nameController = widget.song == null
        ? TextEditingController()
        : TextEditingController(text: widget.song?.name);
    durationController = widget.song == null
        ? TextEditingController()
        : TextEditingController(text: widget.song?.duration.toString());
    authorController = widget.song == null
        ? TextEditingController()
        : TextEditingController(text: widget.song?.author);
    genreController = widget.song == null
        ? TextEditingController()
        : TextEditingController(text: widget.song?.genre);
    urlController = widget.song == null
        ? TextEditingController()
        : TextEditingController(text: widget.song?.url);
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

                Song newSong = Song(id, name, duration, author, genre, url, widget.playlistId!);
                Navigator.pop(context, newSong);
              },
              child: Text("Save song"))
        ],
      ),
    );
  }

}