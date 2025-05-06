import 'package:easy_sidemenu/easy_sidemenu.dart';
import 'package:flutter/material.dart';
import 'package:rillaauth_frontend/widgets/layout/side_menu/side_menu_items.dart';
import 'package:themesplus/themesplus.dart';

class RillaSideMenu extends StatelessWidget {
  final SideMenuController sideMenuController;

  const RillaSideMenu({super.key, required this.sideMenuController});

  @override
  Widget build(BuildContext context) {
    return SideMenu(
      controller: sideMenuController,
      showToggle: false,
      collapseWidth: 1200,
      style: SideMenuStyle(
        // Background color of the side menu
        backgroundColor: Colors.transparent,

        // Selected item text and icon style
        selectedTitleTextStyle: TextStyle(color: AppTheme.data.colorScheme.primary, fontWeight: FontWeight.w600),
        selectedIconColor: AppTheme.colors!.primary,

        // Unselected item text and icon style
        unselectedIconColor: AppTheme.colors!.onSurface,
        unselectedTitleTextStyle: TextStyle(color: AppTheme.colors!.onSurface, fontWeight: FontWeight.w400),

        // Toggle button style
        arrowCollapse: AppTheme.colors!.onSurface,
        arrowOpen: AppTheme.colors!.onSurface,
        toggleColor: AppTheme.colors!.onSurface,

        unselectedIconColorExpandable: AppTheme.data.colorScheme.onSurface,

        // Hover color
        hoverColor: AppTheme.data.colorScheme.onSurface.withValues(alpha: 0.1),

        //Display mode
        displayMode: SideMenuDisplayMode.auto,

        // Outer padding of the side menu items
        itemOuterPadding: EdgeInsets.all(0),

        // Item border radius
        itemBorderRadius: BorderRadius.circular(0),

        // Width of the side menu when in compact mode
        compactSideMenuWidth: 65,

        selectedTitleTextStyleExpandable: TextStyle(color: AppTheme.colors!.onSurface),

        unselectedTitleTextStyleExpandable: TextStyle(color: AppTheme.colors!.onSurface),

        selectedIconColorExpandable: AppTheme.colors!.onSurface,

        expandedDividerColor: AppTheme.colors!.onSurface,

        // Disable tooltips
        showTooltip: false,
      ),
      onDisplayModeChanged: (value) {
        // Handle display mode changes if needed
        debugPrint('Display mode changed to: $value');
      },
      items: sideMenuItems,
    );
  }
}
