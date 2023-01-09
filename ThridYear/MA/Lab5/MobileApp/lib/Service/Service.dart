import 'package:dio/dio.dart';
import 'package:lab3/Domain/playlist.dart';

import '../Domain/song.dart';

class Service {
  static const String _baseApi = "http://10.0.2.2:8080";
  final Dio _dio = Dio();

  Future<List<Playlist>> getAllPlaylists() async {
    final response = await _dio.get('$_baseApi/playlists');
    final json = response.data;
    var list = (json as List).map((e) => Playlist.fromJsonObject(e)).toList();
    return list;
  }

  deletePlaylist(int id) async {
    final response = await _dio.delete('$_baseApi/playlist/$id');
  }

  deleteSong(int id) async {
    final response = await _dio.delete('$_baseApi/song/$id');
  }

  Future<Playlist> addPlaylist(Playlist playlist) async {
    final response = await _dio.post('$_baseApi/playlist',
        data: {
          "id": playlist.id,
          "name": playlist.name,
          "duration": playlist.duration,
          "createdBy": playlist.createdBy,
          "coverPhoto": playlist.coverPhoto,
          "songs": {"songs": playlist.songs.toList()}
        });
    return Playlist.fromJsonObject(response.data);
    }

  updatePlaylist(Playlist playlist) async {
    final response = await _dio.put('$_baseApi/playlist',
        data: {
          "id": playlist.id,
          "name": playlist.name,
          "duration": playlist.duration,
          "createdBy": playlist.createdBy,
          "coverPhoto": playlist.coverPhoto,
          "songs": {"songs": playlist.songs.toList()}
        });
  }

  updateSong(Song song) async {
    final response = await _dio.put('$_baseApi/song',
        data: song.toJson());

  }

  addSong(Song song) async {
    final response = await _dio.post('$_baseApi/song',
        data: song.toJson());
    return Song.fromJsonObject(response.data);
  }
}

