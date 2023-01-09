package com.example.MobileServer.Repository;

import com.example.MobileServer.Domain.Song;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface RepositorySong extends JpaRepository<Song, Long> {
}
