package com.example.MobileServer.Controller;

import com.example.MobileServer.Domain.Playlist;
import com.example.MobileServer.Domain.Song;
import com.example.MobileServer.Dto.PlaylistDTO;
import com.example.MobileServer.Dto.SongDTO;
import com.example.MobileServer.Service.ServicePlaylist;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class ControllerPlaylist {
    @Autowired
    private ServicePlaylist servicePlaylist;

    Logger logger = LoggerFactory.getLogger(ControllerPlaylist.class);

    @GetMapping("/playlists")
    public ResponseEntity<List<Playlist>> getAllPlaylists() {
        logger.info("Getting all playlists!");
        List<Playlist> playlists = servicePlaylist.getAll();
        return new ResponseEntity<>(playlists, HttpStatus.OK);
    }

    @PostMapping("/playlist")
    public ResponseEntity<Playlist> addPlaylist(@RequestBody PlaylistDTO playlist) {
        logger.info("Adding playlist " + playlist);
        Playlist added = servicePlaylist.addPlaylist(playlist.convertToModel());
        return new ResponseEntity<>(added, HttpStatus.CREATED);
    }

    @DeleteMapping("/playlist/{id}")
    public ResponseEntity<?> deletePlaylist(@PathVariable Long id) {
        logger.info(String.format("Deleting playlist with id %s", id));
        servicePlaylist.deletePlaylist(id);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @PutMapping("/playlist")
    public ResponseEntity<?> updatePlaylist(@RequestBody PlaylistDTO playlist) {
        logger.info(String.format("Updating playlist with id %d to " + playlist, playlist.getId()));
        servicePlaylist.updatePlaylist(playlist.convertToModel());
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @PutMapping("/song")
    public ResponseEntity<?> updateSong(@RequestBody SongDTO song) {
        logger.info(String.format("Updating song with id %d to " + song, song.getId()));
        servicePlaylist.updateSong(song.convertToModel());
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @DeleteMapping("/song/{id}")
    public ResponseEntity<?> deleteSong(@PathVariable Long id) {
        logger.info(String.format("Deleting song with id %s", id));
        servicePlaylist.deleteSong(id);
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }

    @PostMapping("/song")
    public ResponseEntity<Song> addSong(@RequestBody SongDTO songDTO) {
        logger.info("Adding song " + songDTO);
        Song added = servicePlaylist.addSong(songDTO.convertToModel(), songDTO.getPlaylistId());
        return new ResponseEntity<>(added, HttpStatus.CREATED);
    }

}
