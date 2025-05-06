import 'package:flutter/material.dart';

class ThemeSettingScreen extends StatelessWidget {
  const ThemeSettingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisAlignment: MainAxisAlignment.start,
      children: [
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Text('Select Theme', style: Theme.of(context).textTheme.headlineMedium),
              SizedBox(height: 20),
              ListView.builder(
                shrinkWrap: true,
                physics: AlwaysScrollableScrollPhysics(),
                itemBuilder: (context, index) {},
              ),
            ],
          ),
        ),
        SizedBox(width: 20),
        Expanded(
          child: Card(
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  Text('Create Theme', style: Theme.of(context).textTheme.headlineMedium),
                  SizedBox(height: 20),
                  ListView(
                    shrinkWrap: true,
                    physics: AlwaysScrollableScrollPhysics(),
                    children: [
                      Text('Theme Name'),
                      SizedBox(height: 10),
                      TextField(
                        decoration: InputDecoration(border: OutlineInputBorder(), hintText: 'Enter theme name'),
                      ),
                      SizedBox(height: 20),
                      Text('Theme Color'),
                      SizedBox(height: 10),
                      TextField(
                        decoration: InputDecoration(border: OutlineInputBorder(), hintText: 'Enter theme color'),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }
}
