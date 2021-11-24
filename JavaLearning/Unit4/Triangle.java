import java.lang.*;
import java.util.*;
import java.text.*;
public class Triangle
{ 
    public static void main(String args[])
    {
        for(int i=1;i<=10000000;i*=10)
        {
                if(i==1)
                    System.out.println("Probability for 1 trial = " + calcProb(1));
                else
                    System.out.println("Probability for " + i + " trials = " + calcProb(i));
        }
    }

    public static double calcProb(int trials)
    {
        double success=0;
        double experimentalProbability=0;
        for(int i=1;i<=trials;i++)
        {
            double stick1=0, stick2=0, stick3=0;
            double a = 0, b = 0, c = 0;
            double num1=Math.random();
            double num2=Math.random();
            while(num1==0||num1==num2||num2==0)
            {
                num1=Math.random();
                num2=Math.random();
            }
            if(num1<num2){
                a=num1; b=num2;}
            else{
                b=num1; a=num2;}
            stick1=a;
            stick2=b-a;
            stick3=1-b;
            if(isTri(stick1,stick2,stick3))
                success+=1; 
        }
        experimentalProbability=success/trials;
        return experimentalProbability;
    }

    public static boolean isTri(double stick1,double stick2, double stick3)
    {
        if(stick1+stick2>stick3&&stick1+stick3>stick2&&stick2+stick3>stick1)
        {
            return true;
        }
        return false;
    }
}
