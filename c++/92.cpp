#include <iostream>
#include <string>

using namespace std;

struct Info{
  string country;

  struct Who{
    string name;
    string nickname;
  }who;
};

int main(){
  Info chuck = {"고려", {"장군 척준경", "소드마스터"}};
  Info anjang = {"고구려", "안장왕 고흥안", "한주 사랑"};

  cout << chuck.country << ", " << chuck.who.name << ", " << chuck.who.nickname << endl;
  cout << anjang.country << ", " << anjang.who.name << ", " << anjang.who.nickname << endl;

  return 0;
}