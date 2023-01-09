package com.example.MobileServer.Domain;

import jakarta.persistence.*;
import lombok.*;

import java.util.Objects;

@Entity
@Table(name = "songs")
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
@Builder
@ToString
public class Song {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    private String name;

    private Integer duration;

    private String author;

    private String genre;

    private String url;

    public boolean check(Song other) {
        return Objects.equals(id, other.getId());
    }
//
//    @ManyToOne
//    @JoinColumn(name = "playlist_id", nullable = false)
//    @ToString.Exclude
//    private Playlist playlist;

}
