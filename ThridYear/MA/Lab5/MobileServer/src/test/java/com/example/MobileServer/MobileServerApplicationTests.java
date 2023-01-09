package com.example.MobileServer;

import com.example.MobileServer.Domain.Playlist;
import com.example.MobileServer.Domain.Song;
import com.example.MobileServer.Repository.RepositoryPlaylist;
import com.example.MobileServer.Repository.RepositorySong;
import org.junit.jupiter.api.Test;

import java.util.HashSet;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class MobileServerApplicationTests {

	@Autowired
	private RepositorySong repositorySong;

	@Autowired
	private RepositoryPlaylist repositoryPlaylist;

	@Test
	void contextLoads() {
	}

	@Test
	void testDb() {
		Playlist playlist = Playlist.builder()
				.name("New playlist")
				.createdBy("Myself")
				.coverPhoto("Nema")
				.duration(100)
				.build();
		Song firstSong = Song.builder()
				.name("First song")
				.author("New author")
				.genre("New genre")
				.duration(50)
				.url("Some url")
				.build();
		Song secondSong = Song.builder()
				.name("Second song")
				.author("Some author")
				.genre("Some genre")
				.duration(50)
				.url("Old url")
				.build();
		HashSet<Song> songs = new HashSet<>();
		songs.add(firstSong);
		songs.add(secondSong);
		playlist.setSongs(songs);
		repositoryPlaylist.save(playlist);
	}

}
