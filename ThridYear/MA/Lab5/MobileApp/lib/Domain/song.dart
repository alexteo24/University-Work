const String tableSong = 'songs';

class SongFields {
  static const List<String> values = [
    id, name, duration, author, genre, url, playlistId, local
  ];

  static const String local = '_local';
  static const String id = '_id';
  static const String name = '_name';
  static const String duration = '_duration';
  static const String author = '_author';
  static const String genre = '_genre';
  static const String url = '_url';
  static const String playlistId = 'playlistId';

}

class Song {
  int _id = 0;
  int _local = 0;
  String _name = "New song";
  int _duration = 30;
  String _author = "Best author";
  String _genre = "Genre";
  String _url = "www.google.com";
  int _playlistId = 0;

  Song(this._id, this._name, this._duration, this._author, this._genre, this._url, this._playlistId);

  Song.fromMap(Map<String, dynamic> map) {
    _local = map[SongFields.local];
    _id = map[SongFields.id];
    _name = map[SongFields.name];
    _duration = map[SongFields.duration];
    _author = map[SongFields.author];
    _genre = map[SongFields.genre];
    _url = map[SongFields.url];
    _playlistId = map[SongFields.playlistId];
  }

  Song.fromJsonObject(Map<String, dynamic> json) {
    _id = json["id"];
    _name = json["name"];
    _duration = json["duration"];
    _author = json["author"];
    _genre = json["genre"];
    _url = json["url"];
  }

  Map<String, dynamic> toMap() {
    var map = <String, dynamic>{};
    if (_local != -1) {
      map[SongFields.local] = _local;
    }
    map[SongFields.id] = _id;
    map[SongFields.name] = _name;
    map[SongFields.duration] = _duration;
    map[SongFields.author] = _author;
    map[SongFields.genre] = _genre;
    map[SongFields.url] = _url;
    map[SongFields.playlistId] = _playlistId;
    return map;
  }

  Map<String, dynamic> toJson() {
    var map = <String, dynamic>{};
    map['id'] = _id;
    map['name'] = _name;
    map['duration'] = _duration;
    map['author'] = _author;
    map['genre'] = _genre;
    map['url'] = _url;
    map['playlistId'] = _playlistId;
    return map;
  }


  int get id => _id;

  set id(int value) {
    _id = value;
  }

  String get url => _url;

  set url(String value) {
    _url = value;
  }

  String get genre => _genre;

  set genre(String value) {
    _genre = value;
  }

  String get author => _author;

  set author(String value) {
    _author = value;
  }

  int get duration => _duration;

  set duration(int value) {
    _duration = value;
  }

  String get name => _name;

  set name(String value) {
    _name = value;
  }

  int get playlistId => _playlistId;

  set playlistId(int value) {
    _playlistId = value;
  }

  int get localId => _local;

  set localId(int value) {
    _local = value;
  }


  @override
  String toString() {
    return 'Song{_name: $_name, _duration: $_duration, _author: $_author, _genre: $_genre, _url: $_url}';
  }

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Song && runtimeType == other.runtimeType && _id == other._id;

  @override
  int get hashCode => _id.hashCode;


}