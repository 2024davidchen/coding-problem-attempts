// Status: Complete
// https://open.kattis.com/problems/greetings2

using System;
class greetings2 {
  static void Main() {
    String inHey = Console.ReadLine();
    int numOfE = inHey.Length - 2;
    String outHey = "h";
    for (int i = 0; i < numOfE * 2; i++){
        outHey += "e";
    }
    outHey += "y";
    Console.WriteLine(outHey);
  }
}