// Task 1.
int addTwo(int num1, int num2) {
  return num1 + num2;
}

// Task 2
double subtractTwo(double num1, double num2) {
  return num1 - num2;
}

// Task 3.
double multiplyTwo(double num1, double num2) {
  return num1 * num2;
}

// Task 4.
double divideTwo(double num1, double num2) {
  if (num2 != 0) {
    return num1 / num2;
  } else {
    throw ArgumentError('Error: Cannot divide by zero!');
  }
}

// Task 5.
int stringLength(String text) {
  return text.length;
}

// Task 6.
dynamic getFirstElement(List<dynamic> list) {
  if (list.isNotEmpty) {
    return list[0];
  } else {
    print('Error: List is empty!');
    return null;
  }
}

void main() {
  // Testing the functions
  print('Task 1: ${addTwo(5, 3)}');
  print('Task 2: ${subtractTwo(10.5, 4.2)}');
  print('Task 3: ${multiplyTwo(2.5, 3)}');
  print('Task 4: ${divideTwo(8, 2)}');
  print('Task 5: ${stringLength("Hello")}');
  print('Task 6: ${getFirstElement([1, 2, 3])}');
}
