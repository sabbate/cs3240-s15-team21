// Sarah Mohamed (smm8ec)
// 10-6-13
// TreeCalc.cpp:  CS 2150 Tree Calculator method implementations

#include "TreeCalc.h"
#include <iostream>
#include <string>
#include <stack>
#include <stdlib.h>

using namespace std;

//Constructor
TreeCalc::TreeCalc()
{
}

//Destructor- frees memory
TreeCalc::~TreeCalc()
{
  if (!(mystack.empty())) {
      cleanTree(mystack.top());
    }
}

//Deletes tree/frees memory
void TreeCalc::cleanTree(TreeNode* ptr)
{
  if (ptr->left == NULL ) {
    delete ptr;
  } else {
    cleanTree(ptr->left);
    cleanTree(ptr->right);
    delete ptr; 
  }
}

//Gets data from user
void TreeCalc::readInput()
{
    string response;
    cout << "Enter elements one by one in postfix notation" << endl
    << "Any non-numeric or non-operator character,"
    << " e.g. #, will terminate input" << endl;

    cout << "Enter first element: ";
    cin >> response;

    //while input is legal
    while (isdigit(response[0]) || response[0]=='/' || response[0]=='*'
            || response[0]=='-' || response[0]=='+' )
    {
        insert(response);
        cout << "Enter next element: ";
        cin >> response;
    }
}

//Puts value in tree stack
void TreeCalc::insert(const string& val)
{
  TreeNode* t = new TreeNode(val);
  if ( val == "+" || val == "-" || val == "*" || val == "/" ) {
    TreeNode * rght = mystack.top();
    mystack.pop();
    TreeNode * lft = mystack.top();
    mystack.pop();
    t->left = lft;
    t->right = rght;
    mystack.push(t);
  }
  else {
    mystack.push(t);
  }
    // insert a value into the tree
}

//Prints data in prefix form
void TreeCalc::printPrefix(TreeNode* ptr) const {
//	string s;
  if (! (ptr == NULL) ) {
    cout << ptr->value << " ";
    printPrefix(ptr->left);
    printPrefix(ptr->right);
  }   // print the tree in prefix format 
}

//Prints data in infix form
void TreeCalc::printInfix(TreeNode* ptr) const {
  if (! (ptr == NULL) ) {
    string val = ptr->value;
    if (val == "+" || val == "-" || val == "*" || val == "/") {
      cout << "(";
      printInfix(ptr->left);
      cout << " " << ptr->value << " ";
      printInfix(ptr->right);
      cout << ")";	
    }
    else {
      cout << ptr->value;
    }
  }
    // print tree in infix format with appropriate parentheses
}

//Prints data in postfix form
void TreeCalc::printPostfix(TreeNode* ptr) const {
  if (! (ptr == NULL) ) {
    string val = ptr->value;
    if (val == "+" || val == "-" || val == "*" || val == "/") {
      printPostfix(ptr->left);
      printPostfix(ptr->right);
      cout << " " << ptr->value << " ";
    }
    else {
      cout << ptr->value << " ";
    } 
  }
   // print the tree in postfix form
}

// Prints tree in all 3 (pre,in,post) forms

void TreeCalc::printOutput() const
{
    if (mystack.size()!=0 && mystack.top()!=NULL)
    {
        cout << "Expression tree in postfix expression: ";
	printPostfix(mystack.top());
        // call your implementation of printPostfix()
        cout << endl;

        cout << "Expression tree in infix expression: ";
	printInfix(mystack.top());
        // call your implementation of printInfix()
        cout << endl;

        cout << "Expression tree in prefix expression: ";
        // call your implementation of printPrefix()
	printPrefix(mystack.top());
        cout << endl;
    }
    else
        cout<< "Size is 0." << endl;
}

//Evaluates tree, returns value
// private calculate() method
int TreeCalc::calculate(TreeNode* ptr) const
{	
    // Traverse the tree and calculates the result
  if ( !(ptr->value == "+") && !(ptr->value == "-") && !(ptr->value == "*") && !(ptr->value == "/") ) {
    const char * cstr = (ptr->value).c_str();
    int num = atoi(cstr);
    return num;
  } else {
    if ( (ptr->value) == "+" ) {
      return calculate(ptr->left) + calculate(ptr->right);
    }
    if ( (ptr->value) == "-" ) {
      return calculate(ptr->left) - calculate(ptr->right);
    }
    if ( (ptr->value) == "*" ) {
      return calculate(ptr->left) * calculate(ptr->right);
    }
    if ( (ptr->value) == "/" ) {
      return calculate(ptr->left) / calculate(ptr->right);
    }
  }
}

//Calls calculate, sets the stack back to a blank stack
// public calculate() method. Hides private data from user
int TreeCalc::calculate()
{
  int i = calculate(mystack.top()); 
  cleanTree(mystack.top());
  mystack.pop();
  // call private calculate method here
  return i;
}
