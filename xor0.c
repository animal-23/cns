 #include <stdio.h>
 int main() {
 // Initialize the string
 char str[] = "Hello world";
 // XOR each character in the string with 0
 for (int i = 0; str[i] != '\0'; i++) {
 str[i] ^= 0; // XOR with 0 (which has no effect on the character)
 }
 // Display the result
 printf("Resulting string: %s\n", str);
 return 0;
 }
