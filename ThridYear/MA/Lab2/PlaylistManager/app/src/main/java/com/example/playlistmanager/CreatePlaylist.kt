    package com.example.playlistmanager

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import com.google.android.material.textfield.TextInputEditText

    class CreatePlaylist : AppCompatActivity() {
    private lateinit var cancelButton: Button
    private lateinit var createButton: Button;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_create_playlist)
        cancelButton = findViewById(R.id.cancelButton)
        cancelButton.setOnClickListener() {
            setResult(Activity.RESULT_CANCELED)
            this.finish()
        }
        createButton = findViewById(R.id.createButton)
        createButton.setOnClickListener() {
            val resultIntent = Intent()
            val playlist: Playlist = Playlist("-1",
                findViewById<TextInputEditText>(R.id.textInputName).text.toString(),
                findViewById<TextInputEditText>(R.id.textInputAuthor).text.toString(),
                findViewById<TextInputEditText>(R.id.textInputDuration).text.toString().toInt(),
                mutableListOf()
            )
            resultIntent.putExtra("playlist", playlist)
            setResult(Activity.RESULT_OK, resultIntent)
            this.finish()
        }
    }
}