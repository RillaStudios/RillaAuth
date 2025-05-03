import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

AppTheme darkTheme = AppTheme(
  id: 'dark',
  icon: const Icon(Icons.dark_mode),
  themeName: 'Dark',
  themeData: ThemeData(
    colorScheme: ColorScheme(
      brightness: Brightness.dark,

      // Brand colors (from logo)
      primary: Color(0xFFF15A24), // Vibrant orange
      onPrimary: Colors.black,
      primaryContainer: Color(0xFF692100),
      onPrimaryContainer: Color(0xFFFFE5D6),

      secondary: Color(0xFFFFD700), // Strong yellow
      onSecondary: Colors.black,
      secondaryContainer: Color(0xFF665B00),
      onSecondaryContainer: Color(0xFFFFFFE0),

      tertiary: Color(0xFFED1C24), // Logo red
      onTertiary: Colors.white,
      tertiaryContainer: Color(0xFF660003),
      onTertiaryContainer: Color(0xFFFFD6D6),

      // Fixed colors (Material You support)
      primaryFixed: Color(0xFFFFA366),
      primaryFixedDim: Color(0xFFE65C00),
      onPrimaryFixed: Colors.black,
      onPrimaryFixedVariant: Color(0xFF3A1A00),

      secondaryFixed: Color(0xFFFFF176),
      secondaryFixedDim: Color(0xFFE6C200),
      onSecondaryFixed: Colors.black,
      onSecondaryFixedVariant: Color(0xFF3A2F00),

      tertiaryFixed: Color(0xFFFF8A80),
      tertiaryFixedDim: Color(0xFFB71C1C),
      onTertiaryFixed: Colors.white,
      onTertiaryFixedVariant: Color(0xFF3A0000),

      // Surfaces and backgrounds
      surface: Color(0xFF121212),
      onSurface: Colors.white,
      surfaceDim: Color(0xFF0D0D0D),
      surfaceBright: Color(0xFF1F1F1F),
      surfaceContainerLowest: Color(0xFF0C0C0C),
      surfaceContainerLow: Color(0xFF141414),
      surfaceContainer: Color(0xFF1C1C1C),
      surfaceContainerHigh: Color(0xFF242424),
      surfaceContainerHighest: Color(0xFF2C2C2C),

      // Error
      error: Color(0xFFED1C24),
      onError: Colors.black,
      errorContainer: Color(0xFF660003),
      onErrorContainer: Color(0xFFFFD6D6),

      // Inverse
      inverseSurface: Color(0xFFE6E1E5),
      onInverseSurface: Color(0xFF322F35),
      inversePrimary: Color(0xFFFFA366),

      // Other
      outline: Color(0xFFA08D87),
      outlineVariant: Color(0xFF53433F),
      shadow: Color(0xFFFFFFFF),
      scrim: Color(0xFF000000),
      surfaceTint: Color(0xFFF15A24),
    ),
  ),
);
