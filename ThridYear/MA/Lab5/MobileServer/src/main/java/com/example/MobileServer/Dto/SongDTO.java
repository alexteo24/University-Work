package com.example.MobileServer.Dto;

import com.example.MobileServer.Domain.Song;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.*;

@Builder
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class SongDTO {
    @JsonProperty("id")
    private Long id;
    @JsonProperty("name")
    private String name;
    @JsonProperty("duration")
    private Integer duration;
    @JsonProperty("author")
    private String author;
    @JsonProperty("genre")
    private String genre;
    @JsonProperty("url")
    private String url;
    @JsonProperty("playlistId")
    private Long playlistId;

    public Song convertToModel() {
        return Song.builder()
                .id(id)
                .name(name)
                .duration(duration)
                .author(author)
                .genre(genre)
                .url(url)
                .build();
    }
}
