#include <bits/stdc++.h>
using namespace std;
int main() {
  int a,b;
  cin>>a>>b;
  for(int i=0;i<b;i++){
    if(a%10==0){
      a/=10;
    }else{
      a--;
    }
  }
  cout << a<<endl;
  return 0;
} 
//https://codeforces.com/contest/977/problem/A #Div_3
