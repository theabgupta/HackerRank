import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static int a;
    static int b;
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a0 = in.nextInt();
        int a1 = in.nextInt();
        int a2 = in.nextInt();
        int b0 = in.nextInt();
        int b1 = in.nextInt();
        int b2 = in.nextInt();
        test(a0,b0);
        test(a1,b1);
        test(a2,b2);
        System.out.print(a+" "+b);
    }
    static void test(int c , int d ){
        if(c>d){
            a+=1;
        }else if(d>c){
            b+=1;
        }
    }
}
