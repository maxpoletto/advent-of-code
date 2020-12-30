#include <string>
#include <stdio.h>
#include <openssl/md5.h>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        printf("Usage: day04 <part> <keybase>\n");
        return 1;
    }
    int part;
    try {
        part = std::stoi(argv[1]);
    } catch (...) {
        part = 0;
    }
    if (part != 1 && part != 2) {
        printf("Part must be 1 or 2\n");
        return 1;
    }
    std::string keybase(argv[2]);
    int iter = 1;
    unsigned char buf[MD5_DIGEST_LENGTH];
    while (true) {
        std::string key = keybase + std::to_string(iter);
        MD5((unsigned char *)key.c_str(), key.size(), buf);
        if ((part == 1 && buf[0] + buf[1] + (buf[2]&0xF0) == 0)
            || (part == 2 && buf[0] + buf[1] + buf[2] == 0)) {
            break;
        }
        iter++;
    }
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++) {
        printf("%x", buf[i]);
    }
    printf("\n%d\n", iter);
    return 0;
}
