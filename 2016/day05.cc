#include <string>
#include <stdio.h>
#include <openssl/md5.h>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        printf("Usage: %s <part> <input>\n", argv[0]);
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
    std::string door_id(argv[2]);
    char password[9], tmp[2];
    memset(password, 0, 9);
    int iter = 0;
    for (int i = 0; i < 8; i++) {
        unsigned char buf[MD5_DIGEST_LENGTH];
        while (true) {
            std::string key = door_id + std::to_string(iter);
            iter++;
            MD5((unsigned char *)key.c_str(), key.size(), buf);
            if (buf[0] + buf[1] + (buf[2]>>4) == 0) {
                if (part == 1) {
                    snprintf(tmp, 2, "%x", buf[2]&0xF);
                    password[i] = tmp[0];
                } else {
                    if (buf[2]&0x8) {
                        continue; // Invalid value.
                    }
                    int j = buf[2]&0x07;
                    if (password[j] != 0) {
                        continue;
                    }
                    snprintf(tmp, 2, "%x", buf[3]>>4);
                    password[j] = tmp[0];
                }
                break;
            }
        }
    }
    printf("%s\n", password);
    return 0;
}
