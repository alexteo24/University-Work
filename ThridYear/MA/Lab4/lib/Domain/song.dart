const String tableSong = 'songs';

class SongFields {
  static const List<String> values = [
    id, name, duration, author, genre, url, playlistId
  ];

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
  String _name = "New song";
  int _duration = 30;
  String _author = "Best author";
  String _genre = "Genre";
  String _url = "www.google.com";
  int _playlistId = 0;

  Song(this._id, this._name, this._duration, this._author, this._genre, this._url, this._playlistId);

  Song.fromMap(Map<String, dynamic> map) {
    _id = map[SongFields.id];
    _name = map[SongFields.name];
    _duration = map[SongFields.duration];
    _author = map[SongFields.author];
    _genre = map[SongFields.genre];
    _url = map[SongFields.url];
    _playlistId = map[SongFields.playlistId];
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

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Song && runtimeType == other.runtimeType && _id == other._id;

  @override
  int get hashCode => _id.hashCode;

  Map<String, dynamic> toMap() {
    var map = <String, dynamic>{};
    if (_id != -1) {
      map[SongFields.id] = _id;
    }
    map[SongFields.name] = _name;
    map[SongFields.duration] = _duration;
    map[SongFields.author] = _author;
    map[SongFields.genre] = _genre;
    map[SongFields.url] = _url;
    map[SongFields.playlistId] = _playlistId;
    return map;
  }
}