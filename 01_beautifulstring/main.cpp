#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <algorithm>
#include <cctype>

using namespace std;
int main (int argc, const char* argv[]) {

  if (argc != 2) {
    return 1;
  }

  ifstream input(argv[1]);
  string ln;

  while (getline(input, ln)) {
    array<int, 26> cnt_chars{};

    for (auto i : ln) {
      if (isalpha(i)) {
        cnt_chars[tolower(i) - 'a']++;
      }
    }

    sort(cnt_chars.begin(), cnt_chars.end());

    int val = 1;
    int bval = 0;

    for (auto c : cnt_chars) {
      bval += c*val;
      val++;
    }

    cout << bval << endl;
  }

  return 0;
}
