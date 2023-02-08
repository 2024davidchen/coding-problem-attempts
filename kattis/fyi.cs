// Status: Complete
// https://open.kattis.com/problems/fyi
using System;
class fyi{
    static void Main(){
        String inNum = Console.ReadLine();
        if (inNum.Substring(0,3) == "555"){
            Console.WriteLine("1");
        }
        else{
            Console.WriteLine("0");
        }
    }
}