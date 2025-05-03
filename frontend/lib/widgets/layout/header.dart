import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

class Header extends StatelessWidget implements PreferredSizeWidget {
  const Header({super.key});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: const Text('Rilla Auth'),
      centerTitle: true,
      backgroundColor: AppTheme.colors!.primary,
      actionsPadding: EdgeInsets.symmetric(horizontal: 10),
      actions: [
        IconButton(
          icon: const Icon(Icons.settings),
          onPressed: () {
            // Handle settings action
          },
        ),
        const SizedBox(width: 10),
        IconButton(
          icon: const Icon(Icons.logout),
          onPressed: () {
            // Handle logout action
          },
        ),
      ],
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}
