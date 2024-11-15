#include <iostream>
#include <array>

using namespace std;

void Print(const array<int, 3> &data){ //array 는 크기 고정
  cout << "== Print ==" << endl;

  for(auto iter = data.begin(); iter!=data.end(); ++iter){
    cout << *iter << ", ";
  }

  cout << endl;
}

int main(){
  array<int, 3>data1 {10,2,5};
  array<int, 3>data2;
  data2.fill(0);
  data2.at(1) = 200;

  Print(data2);

  copy(data1.begin(), data1.end(), data2.begin());

  Print(data1);
  Print(data2);

  return 0;
}