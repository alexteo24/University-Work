package com.example.playlistmanager

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import com.google.android.material.textfield.TextInputEditText

class CreateSong : AppCompatActivity() {
    private lateinit var cancelButton: Button
    private lateinit var saveButton: Button
    private lateinit var textInputSongName: TextInputEditText
    private lateinit var textInputAuthor: TextInputEditText
    private lateinit var textInputSongDuration: TextInputEditText
    private lateinit var textInputGenre: TextInputEditText
    private lateinit var textInputURL: TextInputEditText
    private var songId: String = "-1"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_create_song)

        textInputSongName = findViewById(R.id.textInputSongName)
        textInputAuthor = findViewById(R.id.textInputAuthor)
        textInputSongDuration = findViewById(R.id.textInputSongDuration)
        textInputGenre = findViewById(R.id.textInputGenre)
        textInputURL = findViewById(R.id.textInputURL)

        cancelButton = findViewById(R.id.cancelSaveButton)
        cancelButton.setOnClickListener {
            setResult(Activity.RESULT_CANCELED)
            this.finish()
        }

        initializeSongData()

        saveButton = findViewById(R.id.saveButton)
        saveButton.setOnClickListener() {
            val resultIntent = Intent()
            val song: Song = Song(songId,
                textInputSongName.text.toString(),
                textInputAuthor.text.toString(),
                textInputSongDuration.text.toString().toInt(),
                textInputGenre.text.toString(),
                textInputURL.text.toString(),
            )
            resultIntent.apply {
                putExtra("song", song)
            }
            setResult(Activity.RESULT_OK, resultIntent)
            this.finish()
        }
    }

    private fun initializeSongData() {
        val bundle = intent.extras
        if (bundle != null) {
            val song = bundle.getSerializable("song", Song::class.java)
            if (song != null) {
                songId = song.getId()
                textInputSongName.setText( song.getName())
                textInputAuthor.setText( song.getAuthor())
                textInputSongDuration.setText( song.getDuration().toString())
                textInputGenre.setText( song.getGenre())
                textInputURL.setText( song.getUrl())
            }
        }
    }
}