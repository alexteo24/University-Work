import 'dart:async';

import 'package:lab3/Domain/playlist.dart';
import 'package:lab3/Domain/song.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

class PlaylistDatabase {
  static final PlaylistDatabase instance = PlaylistDatabase._init();

  static Database? _database;

  PlaylistDatabase._init();

  Future<Database> get database async{
    if (_database != null) {
      return _database!;
    }
    _database = await _initDB('playlist.db');
    return _database!;
  }

  Future<Database> _initDB(String filepath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filepath);

    return await openDatabase(path, version: 1, onCreate: _createDB);
  }

  Future _createDB(Database db, int version) async {
    const idType = 'INTEGER PRIMARY KEY AUTOINCREMENT';
    const stringType = 'TEXT NOT NULL';
    const integerType = 'INTEGER NOT NULL';
    await db.execute('''
    CREATE TABLE $tablePlaylist (
      ${PlaylistFields.id} $idType,
      ${PlaylistFields.name} $stringType,
      ${PlaylistFields.duration} $integerType,
      ${PlaylistFields.createdBy} $stringType,
      ${PlaylistFields.coverPhoto} $stringType
    )
    ''');

    await db.execute('''
    CREATE TABLE $tableSong (
      ${SongFields.id} $idType,
      ${SongFields.name} $stringType,
      ${SongFields.duration} $integerType,
      ${SongFields.author} $stringType,
      ${SongFields.genre} $stringType,
      ${SongFields.url} $stringType,
      ${SongFields.playlistId} $integerType,
      FOREIGN KEY(${SongFields.playlistId}) REFERENCES playlists(${PlaylistFields.id})
      )
    ''');
  }

  Future<Playlist> createPlaylist(Playlist playlist) async {
    final db = await instance.database;

    final id = await db.insert(tablePlaylist, playlist.toMap());

    playlist.id = id;
    return playlist;
  }

  Future<Playlist> getPlaylistById(int id) async {
    final db = await instance.database;

    final playlists = await db.query(
      tablePlaylist,
      columns: PlaylistFields.values,
      where: '${PlaylistFields.id} = ?',
      whereArgs: [id]
    );

    if (playlists.isNotEmpty) {
      return Playlist.formMapObject(playlists.first);
    } else {
      throw Exception('ID $id was not found');
    }
  }

  Future<List<Playlist>> getPlaylists() async {
    final db = await instance.database;

    final playlists = await db.query(tablePlaylist);

    List<Playlist> result = [];
    playlists.map((json) async {
      Playlist playlist =  Playlist.formMapObject(json);
      List<Song> songs = await getSongsForPlaylist(playlist.id);
      playlist.songs = songs;
      return playlist;
    }).forEach((element) {element.then((value) => result.add(value));});
    return result;
  }

  Future<int> updatePlaylist(Playlist playlist) async {
    final db = await instance.database;

    return db.update(
    tablePlaylist,
    playlist.toMap(),
    where: '${PlaylistFields.id} = ?',
    whereArgs: [playlist.id]);
  }

  Future<int> deletePlaylist(int id) async {
    final db = await instance.database;

    return db.delete(
      tablePlaylist,
      where: '${PlaylistFields.id} = ?',
      whereArgs: [id]
    );
  }

  Future<List<Song>> getSongsForPlaylist(int playlistId) async {
    final db = await instance.database;
    final result = await db.query(
      tableSong,
      where: '${SongFields.playlistId} = ?',
      whereArgs: [playlistId]
    );
    return result.map((song) => Song.fromMap(song)).toList();
  }
  
  Future<Song> addSongToPlaylist(Song song) async {
    final db = await instance.database;
    final id = await db.insert(tableSong, song.toMap());
    song.id = id;
    return song;
  }

  Future<int> updateSong(Song song) async {
    final db = await instance.database;
    return db.update(
    tableSong,
    song.toMap(),
    where: '${SongFields.id} = ?',
    whereArgs: [song.id]
    );
  }

  Future<int> deleteSong(int id) async {
    final db = await instance.database;
    return db.delete(
      tableSong,
      where: '${SongFields.id} = ?',
      whereArgs: [id]
    );
  }

  Future close() async {
    final db = await instance.database;
    db.close();
  }
}