/* 
=begin
# Ruby
n = gets.to_i
(0..n).each do |i|
  i.to_s(2).chars.each { |c| print "#{c}" }
end
=END
*/
#if 0
// Swift
import Foundation
let n = Int(readLine()!)!
for i in 0...n {
    let b = String(i, radix: 2)
    for ch in b { print(ch, terminator: "") }
}
#endif

#if 0
// Java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i = 0; i <= n; i++) {
            String b = Integer.toBinaryString(i);
            for (char c : b.toCharArray()) System.out.print(c);
        }
    }
}
#else
// C++
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n; cin >> n;
    for(int i=0;i<=n;i++){
        if(i == 0) {
            cout << 0;
        } else {
            string b = bitset<64>(i).to_string();
            b.erase(0, b.find('1'));
            cout << b;
        }
    }
}
#endif
