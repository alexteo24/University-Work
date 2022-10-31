package com.example.playlistmanager

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import androidx.activity.result.ActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {
    private lateinit var playlists: MutableList<Playlist>
    private lateinit var recyclerView: RecyclerView
    private lateinit var createPlaylistButton: Button
    private lateinit var modifyPlaylistButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        recyclerView = findViewById(R.id.recyclerViewPlaylist)
        val layoutManager = LinearLayoutManager(applicationContext)
        recyclerView.layoutManager = layoutManager
        initPlaylists()

        val adapter = RecyclerViewAdapterPlaylist(playlists)
        recyclerView.adapter = adapter;


        createPlaylistButton = findViewById(R.id.buttonCreatePlayList)
        val startForResult = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) {
                result: ActivityResult ->
            if (result.resultCode == Activity.RESULT_OK) {
                val intent = result.data
                if (intent != null) {
                    val playlist = intent.getSerializableExtra("playlist", Playlist::class.java)
                    if (playlist != null) {
                        var existing = false
                        for(i in playlists.indices) {
                            if(playlists[i].getId() == playlist.getId()) {
                                playlist.setSongs(playlists[i].getSongs())
                                playlists[i] = playlist
                                adapter.notifyItemChanged(i)
                                existing = true
                                break
                            }
                        }
                        if(!existing) {
                            playlist.setId((playlists[playlists.size - 1].getId().toInt() + 1).toString())
                            playlists.add(playlist)
                            adapter.notifyItemInserted(playlists.size)
                        }
                    }
                }
            } else if (result.resultCode == Activity.RESULT_CANCELED) {
                val intent = result.data
                if (intent != null) {
                    var playlistId = intent.getStringExtra("playlistId")
                    if(playlistId != null) {
                        for(i in playlists.indices) {
                            if(playlists[i].getId() == playlistId) {
                                playlists.removeAt(i)
                                adapter.notifyItemRemoved(i)
                                break
                            }
                        }
                    }
                }
            }
        }
        createPlaylistButton.setOnClickListener() {
            val intent = Intent(this, CreatePlaylist::class.java)
            startForResult.launch(intent)

        }

        modifyPlaylistButton = findViewById(R.id.modifyPlaylistButton)
        modifyPlaylistButton.setOnClickListener {
            val intent = Intent(this, UpdatePlaylist::class.java)
            startForResult.launch(intent)
        }
    }
    private fun initPlaylists() {
        playlists = ArrayList()
        playlists.add(Playlist("1", "Something", "Myself", 196,
            mutableListOf<Song>(
                Song("1", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("2", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("3", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("4", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("5", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("6", "New song", "New author", 10, "Pop", "www.google.com")
            )
        ))
        playlists.add(Playlist("2", "Something", "Myself", 196,
            mutableListOf<Song>(
                Song("1", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("2", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("3", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("4", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("5", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("6", "New song", "New author", 10, "Pop", "www.google.com")
            )))
        playlists.add(Playlist("3", "Something", "Myself", 196,
            mutableListOf<Song>(
                Song("1", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("2", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("3", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("4", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("5", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("6", "New song", "New author", 10, "Pop", "www.google.com")
            )))
        playlists.add(Playlist("4", "Something", "Myself", 196,
            mutableListOf<Song>(
                Song("1", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("2", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("3", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("4", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("5", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("6", "New song", "New author", 10, "Pop", "www.google.com")
            )))
        playlists.add(Playlist("5", "Something", "Myself", 196,
            mutableListOf<Song>(
                Song("1", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("2", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("3", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("4", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("5", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("6", "New song", "New author", 10, "Pop", "www.google.com")
            )))
        playlists.add(Playlist("6", "Something", "Myself", 196,
            mutableListOf<Song>(
                Song("1", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("2", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("3", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("4", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("5", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("6", "New song", "New author", 10, "Pop", "www.google.com")
            )))
        playlists.add(Playlist("7", "Something", "Myself", 196,
            mutableListOf<Song>(
                Song("1", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("2", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("3", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("4", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("5", "New song", "New author", 10, "Pop", "www.google.com"),
                Song("6", "New song", "New author", 10, "Pop", "www.google.com")
            )))
    }
}