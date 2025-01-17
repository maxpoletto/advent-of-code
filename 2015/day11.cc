#include <string>
#include <iostream>
#include <vector>

// "Increments" a letter string: xx, xy, xz, ya, yb, ...
void inc(std::string &s) {
    int carry = 1;
    for (int i = s.size() - 1; i >= 0; i--) {
        int c = s[i] - 'a' + carry;
        s[i] = 'a' + (c % 26);
        carry = (c == 26);
    }
    if (carry) {
        s = "a" + s;
    }
}

// Tests a password for validity.
bool good(const std::string &s) {
    // No invalid letters.
    uint32_t bad = 1 << ('i'-'a') | 1 << ('o'-'a') | 1 << ('l'-'a');
    for (int i = 0; i < s.size(); i++) {
        if (bad & (1 << s[i])) {
            return false;
        }
    }
    // Contain an increasing straight.
    bool ok = false;
    for (int i = 0; i < s.size() - 2; i++) {
        if (s[i]+1 == s[i+1] && s[i]+2 == s[i+2]) {
            ok = true;
            break;
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
    return pairs & (pairs-1); // 2 or more bits
}

// Given a password, return the next valid one.
std::string nextpass(const std::string &ss) {
    std::string s(ss);
    do {
        inc(s);
    } while (!good(s));
    return s;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: day11 <password>\n");
        return 1;
    }
    auto s = nextpass(argv[1]);
    std::cout << s << std::endl;
    s = nextpass(s);
    std::cout << s << std::endl;
    return 0;
}
