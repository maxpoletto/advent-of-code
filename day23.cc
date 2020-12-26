#include <iostream>
#include <string>
#include <vector>

class Game
{
public:
    Game(std::vector<int> cups, int maxval = -1)
    {
        if (maxval < static_cast<int>(cups.size())) {
            maxval = cups.size();
        }
        max = maxval;
        curr = cups[0];
        next = new int[max+1];
        int i = 0;
        for (; i < cups.size()-1; i++) {
            next[cups[i]] = cups[i+1];
        }
        if (max == cups.size()) {
            next[cups[i]] = curr;
            return;
        }
        next[cups[i]] = cups.size()+1;
        for (i = cups.size()+1; i < max; i++) {
            next[i] = i+1;
        }
        next[max] = curr;
    }
    ~Game() {
        delete[] next;
    }
    void play(int n) {
        for (int i = 0; i < n; i++) {
            int a = next[curr], b = next[a], c = next[b];
            int d = curr-1;
            if (d < 1) {
                d = max;
            }
            while (a == d || b == d || c == d) {
                d--;
                if (d < 1) {
                    d = max;
                }
            }
            next[curr] = next[c];
            curr = next[c];
            next[c] = next[d];
            next[d] = a;
        }
    }
    std::vector<int> after(int l, int n = -1) {
        if (n < 0)
            n = max-1;
        std::vector<int> res(n);
        for (int i = 0; i < n; i++) {
            l = next[l];
            res[i] = l;
        }
        return res;
    }

private:
    int max;
    int curr;
    int* next;
};

std::string part1()
{
    std::vector<int> v = { 6,5,3,4,2,7,9,1,8 };
    Game game(v);
    game.play(100);
    std::vector<int> res = game.after(1);
    std::string str;
    for (int i = 0; i < res.size(); i++) {
        str += std::to_string(res[i]);
    }
    return str;
}

int64_t part2()
{
    std::vector<int> v = { 6,5,3,4,2,7,9,1,8 };
    Game game(v, 1000*1000);
    game.play(10*1000*1000);
    std::vector<int> res = game.after(1,2);
    int64_t p = (int64_t)res[0] * res[1];
    return p;
}

int main()
{
    std::cout << part1() << std::endl;
    std::cout << part2() << std::endl;
    return 0;
}
