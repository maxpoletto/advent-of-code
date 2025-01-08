#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

int read(const std::string& filename, std::vector<uint64_t>& v) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        return -1; // Return -1 if the file cannot be opened
    }
    uint number;
    while (file >> number) {
        v.push_back(number);
    }
    file.close();
    return v.size();
}

void part1(const std::vector<uint64_t>& v) {
    uint64_t sum = 0;
    for (int i = 0; i < v.size(); i++) {
        uint64_t n = v[i];
        for (int j = 0; j < 2000; j++) {
            n = ((n << 6) ^ n) & 0xFFFFFF;
            n = ((n >> 5) ^ n) & 0xFFFFFF;
            n = ((n << 11) ^ n) & 0xFFFFFF;
        }
        sum += n;
    }
    std::cout << sum << std::endl;
}

void part2(const std::vector<uint64_t>& v) {
    int best[19][19][19][19] = {};
    for (int b = 0; b < v.size(); b++) {
        int8_t seen[19][19][19][19] = {};
        int changes[4] = {};
        uint64_t n = v[b];
        int oldprice = v[b] % 10;
        for (int j = 0; j < 2000; j++) {
            n = ((n << 6) ^ n) & 0xFFFFFF;
            n = ((n >> 5) ^ n) & 0xFFFFFF;
            n = ((n << 11) ^ n) & 0xFFFFFF;
            int price = n % 10;
            int change = price - oldprice;
            oldprice = price;
            changes[j % 4] = change + 9;
            if (j < 3) {
                continue;
            }
            int x = changes[(j-3)%4], y = changes[(j-2)%4],
                z = changes[(j-1)%4], w = changes[j%4];
            if (seen[x][y][z][w]) {
                continue;
            }
            seen[x][y][z][w] = 1;
            best[x][y][z][w] += price;
        }
    }
    int bestsum = 0;
    for (int i = 0; i < 19; i++) {
        for (int j = 0; j < 19; j++) {
            for (int k = 0; k < 19; k++) {
                for (int l = 0; l < 19; l++) {
                    bestsum = std::max(bestsum, best[i][j][k][l]);
                }
            }
        }
    }
    std::cout << bestsum << std::endl;
}

int main() {
    std::vector<uint64_t> v;
    int n = read("input/i22.txt", v);
    if (n == -1) {
        std::cout << "Cannot open file" << std::endl;
        return 1; // Return 1 if the file cannot be opened
    }

    auto start = std::chrono::high_resolution_clock::now();
    part1(v);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << "part1 took " << elapsed.count() << std::endl;

    start = std::chrono::high_resolution_clock::now();
    part2(v);
    end = std::chrono::high_resolution_clock::now();
    elapsed = end - start;
    std::cout << "part2 took " << elapsed.count() << std::endl;
    return 0;
}
