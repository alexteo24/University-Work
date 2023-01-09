package com.example.MobileServer.Domain;

import jakarta.persistence.*;
import lombok.*;

import java.util.Set;

@Entity
@Table(name = "playlists")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
@ToString
public class Playlist {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "playlist_id")
    private Long id;

    private String name;

    private Integer duration;

    private String createdBy;

    private String coverPhoto;

    public void addSong(Song song) {
        songs.add(song);
    }

    public void deleteSong(Song song) {
        songs.remove(song);
    }

    @OneToMany(
//            mappedBy = "playlist",
            cascade = CascadeType.ALL,
            orphanRemoval = true)
    @JoinColumn(name = "playlist_id")
    private Set<Song> songs;

}
