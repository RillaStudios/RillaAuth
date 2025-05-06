import 'package:flutter/material.dart';
import 'package:themesplus/themesplus.dart';

class Header extends StatelessWidget implements PreferredSizeWidget {
  const Header({super.key});

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Image.asset('/images/rilla_auth_white.png', height: 40, fit: BoxFit.contain),
      centerTitle: false,
      backgroundColor: AppTheme.colors!.primary,
      actionsPadding: EdgeInsets.symmetric(horizontal: 10),
      actions: [
        const SizedBox(width: 10),
        IconButton(
          icon: Icon(Icons.logout, color: AppTheme.colors!.onPrimary),
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
