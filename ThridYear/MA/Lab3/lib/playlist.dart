import 'song.dart';

class Playlist {
  int _id;
  String _name = "New playlist";
  int _duration = 200;
  String _createdBy = "Myself";
  String _coverPhoto = "default";
  List<Song> _songs = [Song.defaultSong(1),
    Song.defaultSong(2),
    Song.defaultSong(3),
    Song.defaultSong(4),
    Song.defaultSong(5),
  ];

  Playlist.defaultPlaylist(this._id);

  Playlist(this._id, this._name, this._duration, this._createdBy, this._coverPhoto,
      this._songs);


  int get id => _id;

  set id(int value) {
    _id = value;
  }

  List<Song> get songs => _songs;

  set songs(List<Song> value) {
    _songs = value;
  }

  String get coverPhoto => _coverPhoto;

  set coverPhoto(String value) {
    _coverPhoto = value;
  }

  String get createdBy => _createdBy;

  set createdBy(String value) {
    _createdBy = value;
  }

  int get duration => _duration;

  set duration(int value) {
    _duration = value;
  }

  String get name => _name;

  set name(String value) {
    _name = value;
  }

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Playlist && runtimeType == other.runtimeType && _id == other._id;

  @override
  int get hashCode => _id.hashCode;
}