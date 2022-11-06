package com.example.playlistmanager

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView

class RecyclerViewAdapterSong(
    private var values: List<Song>,
    private var context: PlaylistActivity
    ): ListAdapter<Song, RecyclerViewAdapterSong.MyViewHolder>(SongDiffCallBackUtil) {
    private val onClickListener: View.OnClickListener = View.OnClickListener { v ->
        val item = v.tag as Song
        val intent = Intent(v.context, CreateSong::class.java)
        intent.putExtra("song", item)
        v.context.startActivity(intent)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.song_item, parent, false);
        return MyViewHolder(view);
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val item = values[position]
        holder.apply {
            songName.text = item.getName()
            author.text = item.getAuthor()
            duration.text = item.getDuration().toString()
            genre.text = item.getGenre()
            url.text = item.getUrl()
        }
        holder.itemView.setOnClickListener {
            val intent = Intent(holder.itemView.context, CreateSong::class.java)
            intent.putExtra("song", item)
            context.startForResult.launch(intent)
        }
    }

    override fun getItemCount(): Int {
        return values.size;
    }

    class MyViewHolder(view: View): RecyclerView.ViewHolder(view)
    {
        val songName: TextView = view.findViewById(R.id.textViewName)
        val author: TextView = view.findViewById(R.id.textViewAuthor)
        val duration: TextView = view.findViewById(R.id.textViewDuration)
        val genre: TextView = view.findViewById(R.id.textViewGenre)
        val url: TextView = view.findViewById(R.id.textViewURL)

    }

}
object SongDiffCallBackUtil : DiffUtil.ItemCallback<Song>() {
    override fun areItemsTheSame(oldItem: Song, newItem: Song): Boolean {
        return oldItem == newItem
    }

    override fun areContentsTheSame(oldItem: Song, newItem: Song): Boolean {
        return oldItem.getId() == newItem.getId()
    }
}
