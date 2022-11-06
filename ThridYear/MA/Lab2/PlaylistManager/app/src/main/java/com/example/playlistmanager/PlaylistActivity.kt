package com.example.playlistmanager

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.result.ActivityResult
import androidx.activity.result.ActivityResultLauncher
import androidx.activity.result.contract.ActivityResultContracts
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class PlaylistActivity : AppCompatActivity() {
    private lateinit var recyclerViewSong: RecyclerView
    private lateinit var songs: MutableList<Song>
    private lateinit var backButton: Button
    private lateinit var addSongButton: Button
    private lateinit var modifySongButton: Button
    lateinit var startForResult: ActivityResultLauncher<Intent>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_playlist)
        recyclerViewSong = findViewById(R.id.recyclerViewSong)
        val layoutManager = LinearLayoutManager(applicationContext)
        recyclerViewSong.layoutManager = layoutManager
        songs = ArrayList()
        initializePlaylistData()

        val adapterSong = RecyclerViewAdapterSong(songs,this)
        recyclerViewSong.adapter = adapterSong

        backButton = findViewById(R.id.backButton)
        backButton.setOnClickListener {
            finish()
        }

        startForResult = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) {
                result: ActivityResult ->
            if (result.resultCode == Activity.RESULT_OK) {
                val intent = result.data
                if (intent != null) {
                    val song = intent.getSerializableExtra("song", Song::class.java)
                    if (song != null) {
                        var existing = false
                        for(i in songs.indices) {
                            if(songs[i].getId() == song.getId()) {
                                songs[i] = song
                                adapterSong.notifyItemChanged(i)
                                existing = true
                                break
                            }
                        }
                        if(!existing) {
                            song.setId((songs[songs.size - 1].getId().toInt() + 1).toString())
                            songs.add(song)
                            adapterSong.notifyItemInserted(songs.size)
                        }
                    }
                }
            } else if (result.resultCode == Activity.RESULT_CANCELED) {
                val intent = result.data
                if (intent != null) {
                    var songId = intent.getStringExtra("songId")
                    if(songId != null) {
                        for(i in songs.indices) {
                            if(songs[i].getId() == songId) {
                                songs.removeAt(i)
                                adapterSong.notifyItemRemoved(i)
                                break
                            }
                        }
                    }
                }
            }
        }
        addSongButton = findViewById(R.id.addSongButton)
        addSongButton.setOnClickListener {
            val intent = Intent(this, CreateSong::class.java)
            startForResult.launch(intent)
        }

        modifySongButton = findViewById(R.id.modifyButton)
        modifySongButton.setOnClickListener {
            val intent = Intent(this, UpdateSong::class.java)
            startForResult.launch(intent)
        }

    }
    private fun adapterOnClick(song: Song) {
        val intent = Intent(this, CreateSong::class.java)
        startForResult.launch(intent)
    }


    private fun initializePlaylistData() {
        val bundle = intent.extras
        if (bundle != null) {
            val playlist = bundle.getSerializable("playlist", Playlist::class.java)
            if (playlist != null) {
                findViewById<TextView>(R.id.playlist_title).text = playlist.getName()
                findViewById<TextView>(R.id.createdBy).text = playlist.getAuthor()
                findViewById<TextView>(R.id.duration).text = playlist.getDuration().toString()
                songs = playlist.getSongs()
            }
        }
    }
}