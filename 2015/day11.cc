#include <string>
#include <iostream>
#include <stdio.h>
#include <vector>

// "Increments" a letter string: xx, xy, xz, ya, yb, ...
void inc(std::string &s) {
    int carry = 1;
    for (int i = s.size() - 1; i >= 0; i--) {
        int c = s[i] - 'a' + carry;
        carry = (c == 26);
        s[i] = 'a' + (c % 26);
    }
    if (carry) {
        s = "a" + s;
    }
}

// Tests a password for validity.
bool good(const std::string &s) {
    // No invalid letters.
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'i' || s[i] == 'o' || s[i] == 'l') {
            return false;
        }
    }
    // Contain an increasing straight.
    bool ok = false;
    for (int i = 0; i < s.size() - 2 && !ok; i++) {
        ok = true;
        for (int j = 0; j < 3; j++) {
            if (s[i + j] != s[i] + j) {
                ok = false;
                break;
            }
        }
    }
    if (!ok) {
        return false;
    }
    // Contain two different non-overlapping pairs.
    uint32_t pairs = 0;
    for (int i = 0; i < s.size() - 1; i++) {
        if (s[i] == s[i + 1]) {
            pairs |= 1 << (s[i] - 'a');
            i++;
        }
    }
    uint32_t n = 0;
    while (pairs) { // Count 1-bits.
        pairs &= (pairs-1);
        n++;
    }
    return n > 1;
}

// Given a password, return the next valid one.
std::string nextpass(const std::string &ss) {
    std::string s(ss);
    do {
        inc(s);
    } while (!good(s));
    return s;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: day11 <password>\n");
        return 1;
    }
    auto s = nextpass(argv[1]);
    std::cout << s << std::endl;
    s = nextpass(s);
    std::cout << s << std::endl;
    return 0;
}
