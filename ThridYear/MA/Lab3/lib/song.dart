class Song {
  int _id;
  String _name = "New song";
  int _duration = 30;
  String _author = "Best author";
  String _genre = "Genre";
  String _url = "www.google.com";

  Song.defaultSong(this._id);

  Song(this._id, this._name, this._duration, this._author, this._genre, this._url);


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

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is Song && runtimeType == other.runtimeType && _id == other._id;

  @override
  int get hashCode => _id.hashCode;
}