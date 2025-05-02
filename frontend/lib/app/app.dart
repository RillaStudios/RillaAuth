import 'package:flutter/material.dart';
import 'package:rillaauth_frontend/config/keys/app_keys.dart';
import 'package:rillaauth_frontend/screens/main_screen.dart';
import 'package:themesplus/themesplus.dart';

class AuthApp extends StatelessWidget {
  const AuthApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ThemeListener(
      builder: (context, value, child) {
        return MaterialApp(
          theme: AppTheme.data,
          scaffoldMessengerKey: scaffoldMessengerKey,
          navigatorKey: navigatorKey,
          debugShowCheckedModeBanner: false,
          debugShowMaterialGrid: false,
          showSemanticsDebugger: false,
          showPerformanceOverlay: false,
          title: 'Rilla Auth',
          home: const MainScreen(),
        );
      },
    );
  }
}
