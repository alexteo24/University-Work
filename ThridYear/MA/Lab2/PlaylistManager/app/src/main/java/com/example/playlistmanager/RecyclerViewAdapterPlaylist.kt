package com.example.playlistmanager

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
class RecyclerViewAdapterPlaylist(private var values: List<Playlist>): RecyclerView.Adapter<RecyclerViewAdapterPlaylist.MyViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.playlist_item, parent, false);
        return MyViewHolder(view);
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int) {
        val item = values[position]
        holder.playlistTitle.text = item.getName()
        holder.authorName.text = item.getAuthor()
        holder.duration.text = item.getDuration().toString()
        holder.itemView.setOnClickListener() {
            val intent = Intent(holder.itemView.context, PlaylistActivity::class.java)
            intent.putExtra("playlist", item)
            holder.itemView.context.startActivity(intent)
        }
    }

    override fun getItemCount(): Int {
        return values.size;
    }

    class MyViewHolder(view: View): RecyclerView.ViewHolder(view) {
        val playlistTitle: TextView = view.findViewById(R.id.playlist_title)
        val authorName: TextView = view.findViewById(R.id.createdBy)
        val duration: TextView = view.findViewById(R.id.duration)
    }

}