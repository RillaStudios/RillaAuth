import 'package:easy_sidemenu/easy_sidemenu.dart';
import 'package:flutter/material.dart';
import 'package:rillaauth_frontend/screens/analytics_screen.dart';
import 'package:rillaauth_frontend/screens/permission_screen.dart';
import 'package:rillaauth_frontend/screens/settings_screens/auth_setting_screen.dart';
import 'package:rillaauth_frontend/screens/settings_screens/db_setting_screen.dart';
import 'package:rillaauth_frontend/screens/settings_screens/layout_setting_screen.dart';
import 'package:rillaauth_frontend/screens/settings_screens/theme_setting_screen.dart';
import 'package:rillaauth_frontend/screens/users_screen.dart';
import 'package:rillaauth_frontend/widgets/layout/side_menu/side_menu.dart';
import 'package:themesplus/themesplus.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  PageController pageController = PageController(initialPage: 6);
  SideMenuController sideMenuController = SideMenuController();

  @override
  void initState() {
    // Connect SideMenuController and PageController together
    sideMenuController.addListener((index) {
      pageController.jumpToPage(index);
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Material(
          elevation: 3,
          shadowColor: AppTheme.colors!.shadow,
          child: RillaSideMenu(sideMenuController: sideMenuController),
        ),
        Expanded(
          child: PageView(
            controller: pageController,
            children: [
              UsersScreen(),
              PermissionScreen(),
              AnalyticsScreen(),
              AuthSettingScreen(),
              DbSettingScreen(),
              LayoutSettingScreen(),
              ThemeSettingScreen(),
            ],
          ),
        ),
      ],
    );
  }
}
