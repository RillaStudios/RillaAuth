import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

AppTheme lightTheme = AppTheme(
  id: 'light',
  icon: const Icon(Icons.light_mode),
  themeName: 'Light',
  themeData: ThemeData(
    colorScheme: ColorScheme.light(
      brightness: Brightness.light,

      // Brand colors (from logo)
      primary: Color(0xFFF15A24), // Vibrant orange
      onPrimary: Colors.white,
      primaryContainer: Color(0xFFFFE5D6),
      onPrimaryContainer: Color(0xFF3A1A00),

      secondary: Color(0xFFFFD700), // Strong yellow
      onSecondary: Colors.black,
      secondaryContainer: Color(0xFFFFFFE0),
      onSecondaryContainer: Color(0xFF3A2F00),

      tertiary: Color(0xFFED1C24), // Logo red
      onTertiary: Colors.white,
      tertiaryContainer: Color(0xFFFFD6D6),
      onTertiaryContainer: Color(0xFF3A0000),

      // Fixed colors (Material You support)
      primaryFixed: Color(0xFFFFA366),
      primaryFixedDim: Color(0xFFE65C00),
      onPrimaryFixed: Colors.black,
      onPrimaryFixedVariant: Color(0xFF692100),

      secondaryFixed: Color(0xFFFFF176),
      secondaryFixedDim: Color(0xFFE6C200),
      onSecondaryFixed: Colors.black,
      onSecondaryFixedVariant: Color(0xFF665B00),

      tertiaryFixed: Color(0xFFFF8A80),
      tertiaryFixedDim: Color(0xFFB71C1C),
      onTertiaryFixed: Colors.white,
      onTertiaryFixedVariant: Color(0xFF660003),

      // Surfaces and backgrounds
      surface: Color(0xFFFFFFFF),
      onSurface: Color(0xFF121212),
      surfaceDim: Color(0xFFF4F4F4),
      surfaceBright: Color(0xFFFFFFFF),
      surfaceContainerLowest: Color(0xFFFFFFFF),
      surfaceContainerLow: Color(0xFFF9F9F9),
      surfaceContainer: Color(0xFFF3F3F3),
      surfaceContainerHigh: Color(0xFFEDEDED),
      surfaceContainerHighest: Color(0xFFE7E7E7),

      // Error
      error: Color(0xFFED1C24),
      onError: Colors.white,
      errorContainer: Color(0xFFFFD6D6),
      onErrorContainer: Color(0xFF660003),

      // Inverse
      inverseSurface: Color(0xFF2C2C2C),
      onInverseSurface: Color(0xFFE6E1E5),
      inversePrimary: Color(0xFFF15A24),

      // Other
      outline: Color(0xFF8A746F),
      outlineVariant: Color(0xFFD8C2BA),
      shadow: Color(0xFF000000),
      scrim: Color(0xFF000000),
      surfaceTint: Color(0xFFF15A24),
    ),
  ),
);
