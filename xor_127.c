 #include <stdio.h>
 int main() {
 // Initialize the string
 char str[] = "Hello world";
 // Create copies of the original string for AND and XOR operations
 char and_result[sizeof(str)];
 char xor_result[sizeof(str)];
 // Perform AND and XOR operations with 127
 for (int i = 0; str[i] != '\0'; i++) {
 and_result[i] = str[i] & 127; // AND with 127
 xor_result[i] = str[i] ^ 127; // XOR with 127
 }
 // Null-terminate the result strings
 and_result[sizeof(str)- 1] = '\0';
 xor_result[sizeof(str)- 1] = '\0';
 // Display the results
 printf("Original string: %s\n", str);
 printf("Result after AND with 127: %s\n", and_result);
 printf("Result after XOR with 127: %s\n", xor_result);
 return 0;
 }