package com.example.playlistmanager

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import com.google.android.material.textfield.TextInputEditText

class DeleteSong : AppCompatActivity() {
    private lateinit var yesButton: Button;
    private lateinit var noButton: Button;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_delete_song)
        yesButton = findViewById(R.id.yesButton)
        yesButton.setOnClickListener {
            setResult(Activity.RESULT_OK)
            this.finish()
        }
        noButton = findViewById(R.id.noButton)
        noButton.setOnClickListener {
            setResult(Activity.RESULT_CANCELED)
            this.finish()
        }
    }
}