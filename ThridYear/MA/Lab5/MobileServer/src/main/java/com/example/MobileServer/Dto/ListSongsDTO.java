package com.example.MobileServer.Dto;

import com.example.MobileServer.Domain.Song;
import lombok.*;

import java.util.List;
import java.util.stream.Collectors;

@Builder
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class ListSongsDTO {
    private List<SongDTO> songs;

    public List<Song> convertToModel() {
        return songs.stream().map(SongDTO::convertToModel).collect(Collectors.toList());
    }
}
