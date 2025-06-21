#include <vector>

std::vector<int> FracDel(const int j) {
    std::vector<int> N;
    std::vector S = {3};
    for (int i = 0; i <= j; i++) {
        int G = 3;
        N.clear();
        N.reserve(S.size() * 2);
            for (int s : S) {
                N.push_back(s);
                N.push_back(s);
            }
        S = {3};
            for (int n : N) {
                G+=n;
                S.push_back(G%4);
            }
    }
    return S;
}

std::vector<int> Collatz(const int n) {
    if (n <= 0)
        return {};
    std::vector A = {n};
    while (A.back() != 1) {
        A.push_back((A.back()%2==0)?A.back()/2:(3*A.back()+1));
    }
        return A;
}

std::vector<int> Bin_Thue_Morse(int n) {
    std::vector<int> Thue = {0};
    for (int i = -1; i <= n; i++ ) {
        for (int k : Thue) {
            std::cout << Thue.back() << std::endl;
            Thue.push_back(k == 1 ? 0 : 1);
        }
    }
    return Thue;
}
