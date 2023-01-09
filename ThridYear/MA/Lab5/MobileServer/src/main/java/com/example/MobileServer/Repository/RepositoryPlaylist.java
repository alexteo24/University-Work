package com.example.MobileServer.Repository;

import com.example.MobileServer.Domain.Playlist;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface RepositoryPlaylist extends JpaRepository<Playlist, Long> {
}
