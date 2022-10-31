package com.example.playlistmanager

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import androidx.activity.result.ActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import com.google.android.material.textfield.TextInputEditText

class UpdatePlaylist : AppCompatActivity() {

    private lateinit var cancelButton: Button
    private lateinit var createButton: Button
    private lateinit var deleteButton: Button


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_update_playlist)


        cancelButton = findViewById(R.id.cancelButton)
        cancelButton.setOnClickListener() {
            setResult(Activity.RESULT_CANCELED)
            this.finish()
        }
        createButton = findViewById(R.id.createButton)
        createButton.setOnClickListener {
            val resultIntent = Intent()
            val playlist: Playlist = Playlist(
                findViewById<TextInputEditText>(R.id.textInputId).text.toString(),
                findViewById<TextInputEditText>(R.id.textInputName).text.toString(),
                findViewById<TextInputEditText>(R.id.textInputAuthor).text.toString(),
                findViewById<TextInputEditText>(R.id.textInputDuration).text.toString().toInt(),
                mutableListOf()
            )
            resultIntent.putExtra("playlist", playlist)
            setResult(Activity.RESULT_OK, resultIntent)
            this.finish()
        }

        var startForResult = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) {
                result: ActivityResult ->
            if (result.resultCode == Activity.RESULT_OK) {
                var intent = Intent()
                intent.putExtra("playlistId", findViewById<TextInputEditText>(R.id.textInputId).text.toString())
                setResult(Activity.RESULT_CANCELED, intent)
                finish()
            } else {
                setResult(Activity.RESULT_OK)
                finish()
            }
        }
        deleteButton = findViewById(R.id.deletePlaylistButton)
        deleteButton.setOnClickListener() {
            val resultIntent = Intent(this, DeleteSong::class.java)
            startForResult.launch(resultIntent)
        }
    }
}