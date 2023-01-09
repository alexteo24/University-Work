import 'dart:convert';

import 'song.dart';

const String tablePlaylist = 'playlists';

class PlaylistFields {
  static const List<String> values = [
    id, name, duration, createdBy, coverPhoto, local
  ];

  static const String local = '_local';
  static const String id = '_id';
  static const String name = '_name';
  static const String duration = '_duration';
  static const String createdBy = '_createdBy';
  static const String coverPhoto = '_coverPhoto';
}

class Playlist {
  int _id = 0;
  int _local = 0;
  String _name = 'New playlist';
  int _duration = 200;
  String _createdBy = 'Myself';
  String _coverPhoto = 'default';
  List<Song> _songs = [];

  Playlist.defaultPlaylist(this._id);

  Playlist(this._id, this._name, this._duration, this._createdBy,
      this._coverPhoto,
      this._songs);

  Playlist.formMapObject(Map<String, dynamic> map) {
    _local = map[PlaylistFields.local];
    _id = map[PlaylistFields.id];
    _name = map[PlaylistFields.name];
    _duration = map[PlaylistFields.duration];
    _createdBy = map[PlaylistFields.createdBy];
    _coverPhoto = map[PlaylistFields.coverPhoto];
  }

  Map<String, dynamic> toMap() {
    var map = <String, dynamic>{};
    if (local!= -1) {
      map[PlaylistFields.local] = local;
    }
    map[PlaylistFields.id] = _id;
    map[PlaylistFields.name] = _name;
    map[PlaylistFields.duration] = _duration;
    map[PlaylistFields.createdBy] = _createdBy;
    map[PlaylistFields.coverPhoto] = _coverPhoto;
    return map;
  }

  Playlist.fromJsonObject(Map<String, dynamic> json) {
    _id = json["id"];
    _name = json["name"];
    _duration = json["duration"];
    _createdBy = json["createdBy"];
    _coverPhoto = json["coverPhoto"];
    _songs = List<Song>.from(
        json["songs"].map((x) {
          Song song = Song.fromJsonObject(x);
          song.playlistId = _id;
          return song;
        })
    );
  }

  Map<String, dynamic> toJson() {
    var map = <String, dynamic>{};
    map['id'] = _id;
    map['name'] = _name;
    map['duration'] = _duration;
    map['createdBy'] = _createdBy;
    map['coverPhoto'] = _coverPhoto;
    map['songs'] = _songs;
    return map;
  }

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

  int get local => _local;

  set local(int value) {
    _local = value;
  }

  @override
  String toString() {
    return 'Playlist{_name: $_name, _duration: $_duration, _createdBy: $_createdBy, _coverPhoto: $_coverPhoto, _songs: $_songs}';
  }

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
          other is Playlist && runtimeType == other.runtimeType &&
              _id == other._id;

  @override
  int get hashCode => _id.hashCode;
}