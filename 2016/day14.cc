#include <string>
#include <stdio.h>
#include <openssl/md5.h>
#include <unordered_map>
#include <vector>

const int LOOK = 1000;
const int MD5_LEN = 2 * MD5_DIGEST_LENGTH;
unsigned char hexmap[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };
int part = 1;

void expand_hash(const unsigned char buf1[], unsigned char buf2[]) {
    for (int i = 0, j = 0; i < MD5_DIGEST_LENGTH; i++) {
        buf2[j] = hexmap[buf1[i]>>4];
        buf2[j+1] = hexmap[buf1[i]&0xF];
        j += 2;
    }
}

void compute_hash(const std::string& s, unsigned char buf[]) {
    unsigned char tmp[MD5_DIGEST_LENGTH];
    MD5((unsigned char *)s.c_str(), s.size(), tmp);
    expand_hash(tmp, buf);
    if (part == 2) {
        for (int i = 0; i < 2016; i++) {
            MD5(buf, MD5_LEN, tmp);
            expand_hash(tmp, buf);
        }
    }
}

unsigned char md5_run_of_any_three(const unsigned char buf[]) {
    for (int i = 0; i < MD5_LEN-2; i++) {
        if (buf[i] == buf[i+1] && buf[i] == buf[i+2]) {
            return buf[i];
        }
    }
    return 0;
}

bool md5_run_of_five(const unsigned char buf[], unsigned char c) {
    for (int i = 0; i < MD5_LEN-4; i++) {
        if (buf[i] == c && buf[i+1] == c && buf[i+2] == c && buf[i+3] == c && buf[i+4] == c) {
            return true;
        }
    }
    return false;
}

void populate_lookahead(std::unordered_map<unsigned char, std::vector<bool>>& v, const std::string& salt, int i) {
    std::string k = salt + std::to_string(i);
    unsigned char buf[MD5_LEN];
    compute_hash(k, buf);
    for (unsigned char j = 0; j < 16; j++) {
        unsigned char c = hexmap[j];
        v[c][(i-1)%LOOK] = md5_run_of_five(buf, c);
    }
}

bool in_lookahead(std::unordered_map<unsigned char, std::vector<bool>>& v, int n, unsigned char c) {
    for (int i = 0; i < LOOK; i++) {
        if (v[c][(n+i)%LOOK]) {
            return true;
        }
    }
    return false;
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        printf("Usage: %s <part> <input>\n", argv[0]);
        return 1;
    }
    try {
        part = std::stoi(argv[1]);
    } catch (...) {
        part = 0;
    }
    if (part != 1 && part != 2) {
        printf("Part must be 1 or 2\n");
        return 1;
    }
    std::string salt(argv[2]);
    std::unordered_map<unsigned char, std::vector<bool>> v;
    for (int i = 0; i < 16; i++) {
        auto c = hexmap[i];
        v[c] = std::vector<bool>(LOOK);
    }
    for (int i = 1; i <= LOOK; i++) {
        populate_lookahead(v, salt, i);
    }
    int npads = 0, i = 0;
    while (true) {
        std::string k = salt + std::to_string(i);
        unsigned char buf[MD5_LEN];
        compute_hash(k, buf);
        unsigned char c = md5_run_of_any_three(buf);
        if (c > 0) {
            if (in_lookahead(v, i, c)) {
                npads++;
                if (npads == 64) {
                    break;
                }
            }
        }
        i++;
        populate_lookahead(v, salt, i+LOOK);
    }
    printf("%d\n", i);
    return 0;
}
