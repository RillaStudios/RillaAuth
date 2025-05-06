import 'package:easy_sidemenu/easy_sidemenu.dart';
import 'package:flutter/material.dart';

List sideMenuItems = [
  SideMenuItem(
    title: 'Users',
    icon: Icon(Icons.people_rounded),
    onTap: (index, sideMenuController) {
      print(index);
      sideMenuController.changePage(index);
    },
  ),
  SideMenuItem(
    title: 'Permissions',
    icon: Icon(Icons.lock_rounded),
    onTap: (index, sideMenuController) {
      print(index);
      sideMenuController.changePage(index);
    },
  ),
  SideMenuItem(
    title: 'Analytics',
    icon: Icon(Icons.analytics_rounded),
    onTap: (index, sideMenuController) {
      print(index);
      sideMenuController.changePage(index);
    },
  ),
  SideMenuExpansionItem(
    title: 'Settings',
    icon: Icon(Icons.settings_rounded),
    showDivider: true,
    dividerHeight: 1,
    dividerThickness: 1,
    children: [
      SideMenuItem(
        title: 'Auth',
        icon: Icon(Icons.security_rounded),
        onTap: (index, sideMenuController) {
          print(index);
          sideMenuController.changePage(index);
        },
      ),
      SideMenuItem(
        title: 'Database',
        icon: Icon(Icons.storage_rounded),
        onTap: (index, sideMenuController) {
          print(index);
          sideMenuController.changePage(index);
        },
      ),
      SideMenuItem(
        title: 'Layout',
        icon: Icon(Icons.view_comfy_rounded),
        onTap: (index, sideMenuController) {
          print(index);
          sideMenuController.changePage(index);
        },
      ),
      SideMenuItem(
        title: 'Theme',
        icon: Icon(Icons.color_lens),
        onTap: (index, sideMenuController) {
          print(index);
          sideMenuController.changePage(index);
        },
      ),
    ],
  ),
];
