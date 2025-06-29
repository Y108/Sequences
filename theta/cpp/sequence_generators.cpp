#include <vector>

std::vector<int> FracDel(const int j) {
    std::vector<int> N;
    std::vector S = {3};
    for (int i = 0; i <= j; i++) {
        int G = 3;
        N.clear();
        for (int s : S) {
            N.push_back(s);
            N.push_back(s);
        }
        S.clear();
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
    while (0<=n){
        int size = Thue.size();
        for (int i = 0; i<size; i++) {
            Thue.push_back(!Thue[i]);
        }
        --n;
    }
    return Thue;
}

std::vector<int> Index(int n) {
    std::vector<int> Ind;
    for (int i = 1; i<=n; i++) {
        Ind.push_back(i);
    }
    return Ind;
}
