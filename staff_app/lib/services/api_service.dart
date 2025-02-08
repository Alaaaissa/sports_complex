import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  final String baseUrl = "http://127.0.0.1:8000"; // Change this to your Django server URL

  Future<Map<String, dynamic>?> login(String email, String phone) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/login/'),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"email": email, "phone": phone}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString('token', data['token']); // Store token locally
      return data;
    } else {
      return null;
    }
  }

  Future<void> logout() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('token');
  }
}