import 'package:flutter/material.dart';
import 'package:lab3/my_playlists.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: MyPlaylists("Existing playlists")
    );
  }
}