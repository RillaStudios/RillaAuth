import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

AppTheme lightTheme = AppTheme(
  id: 'light',
  icon: const Icon(Icons.light_mode),
  themeName: 'Light',
  themeData: ThemeData(
    primarySwatch: Colors.blue,
    scaffoldBackgroundColor: Colors.white,
    appBarTheme: const AppBarTheme(
      backgroundColor: Colors.white,
      foregroundColor: Colors.black,
    ),
    colorScheme: ColorScheme.fromSwatch().copyWith(
      primary: Colors.blue,
      secondary: Colors.green,
      error: Colors.red,
      brightness: Brightness.light,
    ),
  ),
);
