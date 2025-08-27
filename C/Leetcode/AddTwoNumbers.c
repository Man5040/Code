
#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

void reverse(int arr[], int len) {
    for (int i = 0; i < len / 2; ++i) {
        int temp = arr[i];
        arr[i] = arr[len - i - 1];
        arr[len - i - 1] = temp;
    }
}

int main() {
    int a[] = {9, 9, 9};
    int b[] = {1};
    int lenA = sizeof(a) / sizeof(a[0]);
    int lenB = sizeof(b) / sizeof(b[0]);

    reverse(a, lenA);
    reverse(b, lenB);

    int maxLen = max(lenA, lenB);
    int* result = (int*)malloc((maxLen + 1) * sizeof(int)); // +1 for possible carry
    int carry = 0, sum, i;

    for (i = 0; i < maxLen; i++) {
        int digitA = (i < lenA) ? a[i] : 0;
        int digitB = (i < lenB) ? b[i] : 0;

        sum = digitA + digitB + carry;
        result[i] = sum % 10;
        carry = sum / 10;
    }

    if (carry) {
        result[i++] = carry;
    }

    // Print in reverse to show the correct number
    printf("Result: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", result[j]);
    }
    printf("\n");

    free(result);
    return 0;
}


