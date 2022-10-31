package com.example.playlistmanager

class Song(
    private var id: String,
    private val name: String,
    private val author: String,
    private val duration: Int,
    private val genre: String,
    private val url: String
): java.io.Serializable {

    fun getId(): String {
        return id;
    }

    fun setId(id: String) {
        this.id = id
    }

    fun getName(): String {
        return name
    }

    fun getAuthor(): String {
        return author
    }

    fun getDuration(): Int {
        return duration
    }

    fun getGenre(): String {
        return genre;
    }

    fun getUrl(): String {
        return url
    }
}