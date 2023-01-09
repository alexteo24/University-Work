package com.example.MobileServer.Service;

import com.example.MobileServer.Domain.Playlist;
import com.example.MobileServer.Domain.Song;
import com.example.MobileServer.Repository.RepositoryPlaylist;
import com.example.MobileServer.Repository.RepositorySong;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class ServicePlaylistsImpl implements ServicePlaylist {

    @Autowired
    private RepositoryPlaylist repositoryPlaylist;

    @Autowired
    private RepositorySong repositorySong;

    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public List<Playlist> getAll() {
        return repositoryPlaylist.findAll();
    }

    @Override
    public Playlist addPlaylist(Playlist playlist) {
        return repositoryPlaylist.save(playlist);
    }

    @Override
    public void deletePlaylist(Long id) {
        repositoryPlaylist.findById(id).ifPresent(playlist -> repositoryPlaylist.delete(playlist));
    }

    @Override
    @Transactional
    public void updatePlaylist(Playlist playlist) {
        System.out.println("playlist = " + playlist);
        Playlist p = repositoryPlaylist.findById(playlist.getId()).orElseThrow();
        p.setName(playlist.getName());
        p.setCoverPhoto(playlist.getCoverPhoto());
        p.setDuration(playlist.getDuration());
        p.setCreatedBy(playlist.getCreatedBy());
    }

    @Override
    @Transactional
    public void updateSong(Song song) {
        repositorySong.findById(song.getId()).ifPresentOrElse((s) -> {
                    s.setName(song.getName());
                    s.setDuration(song.getDuration());
                    s.setAuthor(song.getAuthor());
                    s.setGenre(song.getGenre());
                    s.setUrl(song.getUrl());
                },
                () -> {});
    }

    @Override
    public void deleteSong(Long id) {
        repositorySong.deleteById(id);
    }

    @Override
    @Transactional
    public Song addSong(Song song, Long id) {
        Song added = repositorySong.save(song);
        entityManager.createNativeQuery("UPDATE songs set playlist_id=? where id=?")
                .setParameter(1, id)
                .setParameter(2, added.getId())
                .executeUpdate();
        return added;
    }
}
