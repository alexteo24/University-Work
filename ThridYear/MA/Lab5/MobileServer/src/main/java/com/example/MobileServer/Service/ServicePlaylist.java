package com.example.MobileServer.Service;

import com.example.MobileServer.Domain.Playlist;
import com.example.MobileServer.Domain.Song;

import java.util.List;

public interface ServicePlaylist {
    public List<Playlist> getAll();
    public Playlist addPlaylist(Playlist playlist);
    public void deletePlaylist(Long id);
    public void updatePlaylist(Playlist playlist);

    public void updateSong(Song song);
    public void deleteSong(Long id);
    public Song addSong(Song song, Long playlistId);
}
