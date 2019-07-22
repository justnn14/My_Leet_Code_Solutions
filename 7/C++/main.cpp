#include <cmath>

class Solution {
public:
    int reverse(int x) {
        long long rev = 0;
        int a = 0;
        while (x) {
            a = x % 10;
            rev = rev * 10 + a; 
            x = x / 10;
        }
        if (rev < INT_MIN || rev > INT_MAX) {
            return 0;
        }
        else {
            return rev;
        }
    }
};
