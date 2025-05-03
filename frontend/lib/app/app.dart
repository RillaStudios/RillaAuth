import 'package:easy_sidemenu/easy_sidemenu.dart';
import 'package:flutter/material.dart';
import 'package:responsiveplus/responsive.dart';
import 'package:rillaauth_frontend/config/keys/app_keys.dart';
import 'package:rillaauth_frontend/screens/main_screen.dart';
import 'package:rillaauth_frontend/screens/users_screen.dart';
import 'package:rillaauth_frontend/widgets/layout/header.dart';
import 'package:rillaauth_frontend/widgets/layout/side_menu/side_menu.dart';
import 'package:themesplus/themesplus.dart';

class AuthApp extends StatefulWidget {
  const AuthApp({super.key});

  @override
  State<AuthApp> createState() => _AuthAppState();
}

class _AuthAppState extends State<AuthApp> {
  PageController pageController = PageController();
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
    return ResponsiveBuilder(
      builder: (context, constraints, orientation, screenType) {
        return ThemeListener(
          builder: (context, value, child) {
            return MaterialApp(
              theme: value.themeData,
              scaffoldMessengerKey: scaffoldMessengerKey,
              navigatorKey: navigatorKey,
              debugShowCheckedModeBanner: false,
              debugShowMaterialGrid: false,
              showSemanticsDebugger: false,
              showPerformanceOverlay: false,
              title: 'Rilla Auth',
              builder: (context, child) {
                return Scaffold(
                  appBar: Header(),
                  body: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Material(
                        elevation: 3,
                        shadowColor: AppTheme.colors!.shadow,
                        child: RillaSideMenu(sideMenuController: sideMenuController),
                      ),
                      Expanded(child: child!),
                    ],
                  ),
                );
              },
              home: PageView(controller: pageController, children: [UsersScreen(), MainScreen(), MainScreen()]),
            );
          },
        );
      },
    );
  }
}
