import 'dart:convert';

import 'package:http/http.dart' as http;

class AppRouterEndpoints {
  static const String baseUrl = 'http://localhost:9334/auth/service';

  Future<bool> checkRunning() async {
    final response = await http.get(Uri.parse('$baseUrl/system-check'));
    if (response.statusCode == 200) {
      final json = jsonDecode(response.body);
      print(response.body);
      return json['status'] == 'ok';
    } else {
      throw Exception('Failed to check running status');
    }
  }
}
