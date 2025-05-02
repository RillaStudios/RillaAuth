import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

AppTheme darkTheme = AppTheme(
  id: 'dark',
  icon: const Icon(Icons.dark_mode),
  themeName: 'Dark',
  themeData: ThemeData(
    primarySwatch: Colors.blue,
    scaffoldBackgroundColor: Colors.black,
    appBarTheme: const AppBarTheme(
      backgroundColor: Colors.black,
      foregroundColor: Colors.white,
    ),
    colorScheme: ColorScheme.fromSwatch().copyWith(
      primary: Colors.blue,
      secondary: Colors.green,
      error: Colors.red,
      brightness: Brightness.dark,
    ),
  ),
);
