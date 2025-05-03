import 'package:easy_sidemenu/easy_sidemenu.dart';
import 'package:flutter/material.dart';

List<SideMenuItem> sideMenuItems = [
  SideMenuItem(
    title: 'Users',
    icon: Icon(Icons.people),
    onTap: (index, sideMenuController) {
      print(index);
      sideMenuController.changePage(index);
    },
  ),
  SideMenuItem(
    title: 'Permissions',
    icon: Icon(Icons.lock),
    onTap: (index, sideMenuController) {
      print(index);
      sideMenuController.changePage(index);
    },
  ),
  SideMenuItem(
    title: 'Settings',
    icon: Icon(Icons.settings),
    onTap: (index, sideMenuController) {
      print(index);
      sideMenuController.changePage(index);
    },
  ),
];
