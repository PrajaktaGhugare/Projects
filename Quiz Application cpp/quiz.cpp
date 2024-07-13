#include <iostream>
#include <iomanip>
#include <cstdlib>  // For system("cls") on Windows, use "clear" for Linux/MacOS

using namespace std;

// Function to display quiz questions and get user answers
void runQuiz() {
    // Quiz questions and answers
    string questions[25] = {
        "1. What is encapsulation in C++?\n(a) Combining data members and functions into a single unit\n(b) Using inheritance to derive new classes\n(c) Allocating memory dynamically",
        "2. Which OOP principle describes the ability of objects to take multiple forms?\n(a) Inheritance\n(b) Encapsulation\n(c) Polymorphism",
        "3. What does inheritance facilitate in C++?\n(a) Code reusability\n(b) Data hiding\n(c) Dynamic memory allocation",
        "4. Which keyword is used to implement inheritance in C++?\n(a) derive\n(b) extends\n(c) class",
        "5. What is a virtual function in C++?\n(a) A function defined in a base class that can be overridden in derived classes\n(b) A function that is declared as private in a class\n(c) A function that takes no arguments",
        "6. Which access specifier allows members to be accessed from anywhere?\n(a) public\n(b) protected\n(c) private",
        "7. What is the purpose of the 'this' pointer in C++?\n(a) It refers to the current object\n(b) It refers to the base class\n(c) It refers to the derived class",
        "8. Which concept in OOP allows a class to inherit properties and behavior from another class?\n(a) Polymorphism\n(b) Inheritance\n(c) Encapsulation",
        "9. What is the default access specifier for members of a class in C++?\n(a) public\n(b) protected\n(c) private",
        "10. Which keyword is used to prevent inheritance of a class in C++?\n(a) break\n(b) final\n(c) stop",
        "11. What does the term 'abstraction' mean in the context of OOP?\n(a) Hiding the implementation details while showing the essential features\n(b) Using multiple inheritance to derive classes\n(c) Using inline functions to reduce function call overhead",
        "12. Which OOP concept allows a class to have more than one function with the same name but different parameters?\n(a) Polymorphism\n(b) Inheritance\n(c) Encapsulation",
        "13. What is operator overloading in C++?\n(a) Defining multiple operators for a class\n(b) Overriding standard operators for built-in types\n(c) Using operators with different precedence",
        "14. Which keyword is used to implement pure virtual functions in C++?\n(a) abstract\n(b) virtual\n(c) pure",
        "15. What is the purpose of constructors in C++ classes?\n(a) Initializing objects of a class\n(b) Destructing objects of a class\n(c) Calling base class methods",
        "16. Which operator is used to access members of a class using a pointer to an object?\n(a) ->\n(b) .\n(c) ::",
        "17. Which principle states that objects of different classes can be accessed through the same interface?\n(a) Encapsulation\n(b) Polymorphism\n(c) Inheritance",
        "18. What does the 'static' keyword mean when used with a class member in C++?\n(a) It makes the member accessible from any instance of the class\n(b) It prevents the member from being inherited by derived classes\n(c) It allocates memory only once for the member shared among all instances",
        "19. Which type of inheritance allows a class to inherit from multiple base classes?\n(a) Single inheritance\n(b) Multiple inheritance\n(c) Hierarchical inheritance",
        "20. What is the difference between 'struct' and 'class' in C++?\n(a) 'struct' members are private by default, while 'class' members are public by default\n(b) 'struct' members are public by default, while 'class' members are private by default\n(c) There is no difference between 'struct' and 'class' in C++",
        "21. What is dynamic polymorphism in C++?\n(a) Resolving function calls at compile time\n(b) Resolving function calls at runtime using virtual functions\n(c) Resolving function calls using function overloading",
        "22. Which OOP concept helps in achieving data hiding in C++?\n(a) Inheritance\n(b) Polymorphism\n(c) Encapsulation",
        "23. Which keyword is used to access base class members in a derived class in C++?\n(a) super\n(b) base\n(c) parent",
        "24. What is the destructor in C++?\n(a) A function that initializes objects of a class\n(b) A function that is automatically called when an object is destroyed\n(c) A function that copies one object to another",
        "25. Which OOP principle states that a child class can override methods of a parent class?\n(a) Polymorphism\n(b) Inheritance\n(c) Encapsulation"
    };
    char answers[25] = {'a', 'c', 'a', 'c', 'a', 'a', 'a', 'b', 'c', 'b',
                        'a', 'a', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'b',
                        'b', 'b', 'b', 'b', 'b'};
    
    char userAnswers[25];

    // Display questions and get user answers
    for (int i = 0; i < 25; ++i) {
        // Clear screen for better visibility (Windows)
        system("cls");
        cout << "*** Welcome to the Object-Oriented Programming Quiz ***\n\n";
        cout << "Question " << (i + 1) << ":\n" << questions[i] << "\n\n";

        char userAnswer;
        bool isValidAnswer = false;
        do {
            cout << "Select your answer (a, b, or c): ";
            cin >> userAnswer;

            // Convert user answer to lowercase for case insensitivity
            userAnswer = tolower(userAnswer);

            if (userAnswer != 'a' && userAnswer != 'b' && userAnswer != 'c') {
                cout << "Invalid option! Select options from (a), (b), or (c) only.\n";
            } else {
                isValidAnswer = true;
            }
        } while (!isValidAnswer);

        // Store user's answer
        userAnswers[i] = userAnswer;
    }

    // Clear screen again for displaying results
    system("cls");

    // Display quiz results and correct answers
    cout << "*** Quiz Results ***\n\n";
    int score = 0;
    for (int i = 0; i < 25; ++i) {
        cout << "Question " << (i + 1) << ":\n" << questions[i] << "\n";
        cout << "Your answer: " << userAnswers[i] << "\n";
        cout << "Correct answer: " << answers[i] << "\n\n";
        if (userAnswers[i] == answers[i]) {
            score++;
        }
    }

    // Display final score
    cout << "Total Score: " << score << "/25\n";
    if (score >= 15) {
        cout << "Congratulations! You passed the quiz.\n";
    } else {
        cout << "Sorry, you did not pass the quiz. Better luck next time!\n";
    }
}

int main() {
    runQuiz();
    return 0;
}
