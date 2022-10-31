package com.example.playlistmanager

import android.app.Activity
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class DeletePlaylist : AppCompatActivity() {
    private lateinit var yesButton: Button;
    private lateinit var noButton: Button;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_delete_playlist)

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