package com.example.playlistmanager

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import androidx.activity.result.ActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import com.google.android.material.textfield.TextInputEditText

class UpdateSong : AppCompatActivity() {
    private lateinit var cancelButton: Button
    private lateinit var saveButton: Button
    private lateinit var deleteButton: Button
    private lateinit var textInputID: TextInputEditText
    private lateinit var textInputSongName: TextInputEditText
    private lateinit var textInputAuthor: TextInputEditText
    private lateinit var textInputSongDuration: TextInputEditText
    private lateinit var textInputGenre: TextInputEditText
    private lateinit var textInputURL: TextInputEditText
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_update_song)

        textInputID = findViewById(R.id.textInputId)
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

        saveButton = findViewById(R.id.saveButton)
        saveButton.setOnClickListener() {
            val resultIntent = Intent()
            val song: Song = Song(textInputID.text.toString(),
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

        var startForResult = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) {
                result: ActivityResult ->
            if (result.resultCode == Activity.RESULT_OK) {
                var intent = Intent()
                intent.putExtra("songId", textInputID.text.toString())
                setResult(Activity.RESULT_CANCELED, intent)
                finish()
            } else {
                setResult(Activity.RESULT_OK)
                finish()
            }
        }
        deleteButton = findViewById(R.id.deleteButton)
        deleteButton.setOnClickListener() {
            val resultIntent = Intent(this, DeleteSong::class.java)
            startForResult.launch(resultIntent)
        }
    }
}