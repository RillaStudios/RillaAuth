import 'package:flutter/material.dart';
import 'package:responsiveplus/responsive.dart';
import 'package:rillaauth_frontend/api/service_router/service_router_endpoints.dart';
import 'package:rillaauth_frontend/config/keys/app_keys.dart';
import 'package:rillaauth_frontend/widgets/layout/header.dart';
import 'package:themesplus/themesplus.dart';

class AuthApp extends StatefulWidget {
  const AuthApp({super.key});

  @override
  State<AuthApp> createState() => _AuthAppState();
}

class _AuthAppState extends State<AuthApp> {
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
              home: SelectionArea(
                child: Scaffold(
                  appBar: Header(),
                  body: FutureBuilder<bool>(
                    future: AppRouterEndpoints().checkRunning(),
                    builder: (context, snapshot) {
                      if (snapshot.connectionState == ConnectionState.waiting) {
                        // This should be customized to show a loading screen
                        return Center(child: CircularProgressIndicator());
                      }

                      if (snapshot.hasError) {
                        // Improved error handling
                        return Center(
                          child: Padding(
                            padding: const EdgeInsets.all(20.0),
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(Icons.error_outline, color: Colors.red, size: 60),
                                SizedBox(height: 16),
                                Text('Connection Error', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
                                SizedBox(height: 8),
                                Text(
                                  'Unable to connect to the database service.',
                                  style: TextStyle(fontSize: 18),
                                  textAlign: TextAlign.center,
                                ),
                                SizedBox(height: 8),
                                Text(
                                  'Please ensure the backend server is running at http://127.0.0.1:9334',
                                  style: TextStyle(fontSize: 16),
                                  textAlign: TextAlign.center,
                                ),
                                SizedBox(height: 20),
                                ElevatedButton(
                                  onPressed: () {
                                    setState(() {}); // This will trigger the FutureBuilder again
                                  },
                                  child: Padding(
                                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                                    child: Text('Retry Connection', style: TextStyle(fontSize: 16)),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        );
                      }

                      if (snapshot.data!) {
                        return Center(
                          child: Padding(
                            padding: const EdgeInsets.all(20.0),
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(Icons.check_circle, color: Colors.green, size: 60),
                                SizedBox(height: 16),
                                Text(
                                  'Database Service Running',
                                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                                ),
                                SizedBox(height: 8),
                                Text(
                                  'The database service is running successfully.',
                                  style: TextStyle(fontSize: 18),
                                  textAlign: TextAlign.center,
                                ),
                              ],
                            ),
                          ),
                        );
                      } else {
                        return Center(
                          child: Padding(
                            padding: const EdgeInsets.all(20.0),
                            child: Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(Icons.error_outline, color: Colors.red, size: 60),
                                SizedBox(height: 16),
                                Text('Unknown Error', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
                                SizedBox(height: 8),
                                Text(
                                  'An unknown error occurred while checking the database service.',
                                  style: TextStyle(fontSize: 18),
                                  textAlign: TextAlign.center,
                                ),
                              ],
                            ),
                          ),
                        );
                      }
                    },
                  ),
                ),
              ),
            );
          },
        );
      },
    );
  }
}
