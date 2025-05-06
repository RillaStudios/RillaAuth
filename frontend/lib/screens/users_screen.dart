import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

class UsersScreen extends StatelessWidget {
  const UsersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisAlignment: MainAxisAlignment.start,
      children: [
        Text('USERS Theme: ${ThemesUtil.currentTheme!.value.themeName}'),
        const SizedBox(height: 20),
        FilledButton(
          onPressed: () {
            ThemesUtil.switchTheme();
            debugPrint('Switched Theme to ${ThemesUtil.currentTheme!.value.themeName}');
          },
          child: const Text('Switch Theme'),
        ),
      ],
    );
  }
}
