import 'package:flutter/material.dart';

class TextBox extends StatelessWidget {
  final TextEditingController _controller;
  final String _label;
  TextBox(this._controller, this._label);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.all(15),
      child: TextField(
        controller: _controller,
        decoration: InputDecoration(
          filled: true,
          label: Text(_label),
          suffix: GestureDetector(
            child: Icon(Icons.close),
            onTap: () {
              _controller.clear();
            },
          )
        ),
      ),
    );
  }

}
