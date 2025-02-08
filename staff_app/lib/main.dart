import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'screens/login_screen.dart';
import 'services/api_service.dart';

void main() {
  runApp(const StaffApp());
}

class StaffApp extends StatelessWidget {
  const StaffApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        Provider<ApiService>(create: (_) => ApiService()),
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'Staff Management',
        theme: ThemeData(primarySwatch: Colors.blue),
        home: const LoginScreen(),
      ),
    );
  }
}