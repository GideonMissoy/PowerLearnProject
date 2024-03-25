// Task 1: Function to return the sum of two numbers:
int sum(int a, int b) {
  return a + b;
}

void main() {
  print(sum(5, 7));
}

// Task 2: Printing numbers from 1 to 10 using a for loop:
void main() {
  for (int i = 1; i <= 10; i++) {
    print(i);
  }
}

// Task 3: Using a switch statement to check string values:
void main() {
  String input = "apple";

  switch (input) {
    case "apple":
      print("It's a fruit.");
      break;
    case "banana":
      print("It's also a fruit.");
      break;
    default:
      print("Unknown");
  }
}

// Task 4: Printing numbers from 20 to 10 using a while loop:
void main() {
  int i = 20;
  while (i >= 10) {
    print(i);
    i--;
  }
}

// Task 5: Using an if-else statement to check if a number is even or odd:
void checkEvenOrOdd(int number) {
  if (number % 2 == 0) {
    print("$number is even.");
  } else {
    print("$number is odd.");
  }
}

void main() {
  checkEvenOrOdd(7);
}

// Task 6: Finding the largest number in a list:
int findLargest(List<int> numbers) {
  int largest = numbers[0];
  for (int number in numbers) {
    if (number > largest) {
      largest = number;
    }
  }
  return largest;
}

void main() {
  List<int> numbers = [10, 5, 20, 15, 8];
  print("Largest number: ${findLargest(numbers)}");
}

// Task 7: Using a try-catch block to catch an exception:
void main() {
  try {
    int result = 10 ~/ 0;
    print("Result: $result");
  } catch (e) {
    print("Error: $e");
  }
}
