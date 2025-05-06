import 'package:flutter/material.dart';
import 'package:responsiveplus/responsive.dart';
import 'package:rillaauth_frontend/app/app.dart';
import 'package:rillaauth_frontend/config/themes/dark_theme.dart';
import 'package:rillaauth_frontend/config/themes/default_theme.dart';
import 'package:themesplus/themesplus.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  ResponsiveUtil.init(enableOrientationChange: false);

  await ThemesUtil.init(themes: [defaultTheme, darkTheme]);

  runApp(const AuthApp());
}
