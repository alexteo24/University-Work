package com.example.MobileServer.Dto;

import com.example.MobileServer.Domain.Playlist;
import com.example.MobileServer.Domain.Song;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

import java.util.HashSet;
import java.util.stream.Collectors;

@Builder
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class PlaylistDTO {

    private Long id;

    private String name;

    private Integer duration;

    private String createdBy;

    private String coverPhoto;

    @JsonProperty("songs")
    private ListSongsDTO songs;

    public Playlist convertToModel() {
        return Playlist.builder()
                .id(id)
                .name(name)
                .duration(duration)
                .createdBy(createdBy)
                .coverPhoto(coverPhoto)
                .songs(new HashSet<>(songs.convertToModel()))
                .build();
    }
}
