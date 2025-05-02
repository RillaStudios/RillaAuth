import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppTheme.colors!.surface,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Current Theme: ${ThemesUtil.currentTheme!.value.themeName}'),
            const SizedBox(height: 20),
            FilledButton(
              onPressed: () {
                ThemesUtil.switchTheme();
                debugPrint(
                  'Switched Theme to ${ThemesUtil.currentTheme!.value.themeName}',
                );
              },
              child: const Text('Switch Theme'),
            ),
          ],
        ),
      ),
    );
  }
}
