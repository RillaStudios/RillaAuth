import 'dart:convert';

import 'package:http/http.dart' as http;

/// A class to handle database setup operations.
/// This class accesses the inner database to see
/// if the real database is set up or not. It acts
/// as a bootstrapper for the database setup process.
///
/// @author IFD
/// @since 2025-05-05
class SetupDb {
  /// The URL for the database setup API.
  static const String _dbUrl = 'http://localhost:9334/auth/db';

  /// Checks if the database setup is required.
  /// Returns true if setup is required, false otherwise.
  ///
  /// Throws an exception if the request fails.
  ///
  /// This method sends a GET request to the database URL to check if the setup is required.
  /// It expects a JSON response with a key 'is_setup' indicating the setup status.
  ///
  /// @author IFD
  /// @since 2025-05-05
  Future<bool> checkSetupRequired() async {
    final response = await http.get(Uri.parse('$_dbUrl/initialized'));

    if (response.statusCode == 200) {
      final json = jsonDecode(response.body);

      if (json['is_setup'] == true) {
        return false; // Setup is not required
      } else {
        return true; // Setup is required
      }
    } else {
      throw Exception('Failed to check setup status');
    }
  }
}
