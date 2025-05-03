import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

class MainScreen extends StatelessWidget {
  const MainScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Text('Current Theme: ${ThemesUtil.currentTheme!.value.themeName}'),
          const SizedBox(height: 20),
          FilledButton(
            onPressed: () {
              ThemesUtil.switchTheme();
              debugPrint('Switched Theme to ${ThemesUtil.currentTheme!.value.themeName}');
            },
            child: const Text('Switch Theme'),
          ),
        ],
      ),
    );
  }
}
