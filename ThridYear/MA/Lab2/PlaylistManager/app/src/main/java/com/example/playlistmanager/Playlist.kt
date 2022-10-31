package com.example.playlistmanager

class Playlist(
    private var id: String,
    private val name: String,
    private val author: String,
    private val duration: Int,
    private var songs: MutableList<Song>
    ): java.io.Serializable {

    fun getSongs(): MutableList<Song> {
        return songs
    }

    fun setSongs(songs: MutableList<Song>) {
        this.songs = songs
    }

    fun getId(): String {
        return id;
    }

    fun setId(id: String) {
        this.id = id;
    }

    fun getName(): String {
        return name;
    }

    fun getAuthor(): String {
        return author;
    }

    fun getDuration(): Int {
        return duration;
    }
}