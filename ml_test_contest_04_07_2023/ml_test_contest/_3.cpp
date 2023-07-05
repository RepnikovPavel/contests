#include <vector>
#include <fstream>
// #include <iostream>
using namespace std;

bool is_target(int a_i, int k) {
    return 1 <= a_i && a_i <= k;
}

void reset_dict(vector<int>& d) {
    for (size_t i = 0; i < d.size(); i++)
    {
        d[i] = 0;
    }
}

bool is_all_found(vector<int>& d, int k,int& current_found) {
    if (current_found<k)
    {
        return false;
    }
    
    current_found =0;
    for (size_t i = 0; i < d.size(); i++)
    {
        if (d[i]==1)
        {
            current_found +=1;
        }
        
    }
    if (current_found<k)
    {
        return false;
    }
    return true;
}


void search_next_seq(vector<int>& a_vec, int& start_pos, long long& min_s, int k, int n, vector<int>& have_y_seen_the_k) {
    long long current_s = 0;
    // |1| 2 1 4 2 1 |3| 7 8 9 11 1 2 3
    // 1 9 2 4 2 2 2 3 1 8 2 10 9
    int current_found = 0;
    for (int i = start_pos; i < n; ++i) {
        int a_i = a_vec[i];
        if (is_target(a_i, k)) {
            have_y_seen_the_k[a_i-1] = 1;
            current_found += 1;
        } else if (!is_target(a_i, k) && current_s == 0) {
            start_pos += 1;
            continue;
        }
        current_s += a_i;
        
        if (is_all_found(have_y_seen_the_k, k,current_found)) {
            min_s = min(min_s, current_s);
            reset_dict(have_y_seen_the_k);
            current_found=0;
            current_s = 0;
            for (int j = i; j > start_pos-1;--j)
            {
                // 6 2 3 1 2 3
                // 1 2 4 3 4 1 5 6
                // 1-4
                // 1 9 1 3 2 |4| 2 2 5 4 9 2 3 1 8 2 10 9
                // 1 9 1 3 2 4 2 2 5 4
                // 1 9 1 1 3 2 9 3
                
                int a_j = a_vec[j];
                if (is_target(a_j, k)) {
                    have_y_seen_the_k[a_j-1] = 1;
                    current_found += 1;
                }
                if (is_all_found(have_y_seen_the_k, k,current_found))
                {   
                    current_s += a_j;
                    min_s = min(min_s,current_s);
                    reset_dict(have_y_seen_the_k);
                    start_pos = j+1;
                    return;
                }
                current_s += a_j;                
            }
        }
    }
    start_pos = n;
}

int main() {
    ifstream ifstream("input.txt");
    ofstream ofstream("output.txt");
    int n, k;
    ifstream >> n >> k;
    if(k==1){
        ofstream << 1;
            ifstream.close();
            ofstream.close();
            return EXIT_SUCCESS; 
    }
    vector<int> a_vec(n);
    for (int i = 0; i < n; i++) {
        ifstream >> a_vec[i];
    }
    long long min_s = 125000750001;
    int start_pos = 0;
    vector<int> have_y_seen_the_k(k);
    while(true){
        search_next_seq(a_vec,start_pos,min_s,k,n, have_y_seen_the_k);
        if (start_pos > n-k){
            break;
        }
    }
    ofstream << min_s;
    ifstream.close();
    ofstream.close();
    return EXIT_SUCCESS; 
}
