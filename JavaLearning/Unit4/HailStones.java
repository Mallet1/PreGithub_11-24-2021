/**
 * What is a hailstone?
 * You start with any positive integer, and it will go to 1 if treated in the following fashion:
 * - If the number is even, it is divided by 2
 * - If the number is odd it is multiplied by 3 and incremented by 1.
 * This process continues until it reaches 1. Each time the integer is processed is called a hailstone.  
 * 
 * Sample Numbers: 17 has 12 hailstones, and 98 has 25 hailstones.
 * 1 is considered to have 0 hailstones.
 * The number with the most hailstones is 871 with 178 hailstones.

 */

import java.util.Scanner;

public class HailStones
{

    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);   

        System.out.print("Please enter a positive integer: ");
        int x=s.nextInt();
        int stone = stones(x); //stone will hold how many hailstones x has.

        System.out.println("\n"+x+ " has " + stone + " hailstones.");
        most(); //Void method, called all by itself

        printPerfect();
    }

    public static void most()
    {
        int number=1; //number with the most stones
        int most = 1; //number of stones that "number" has

        for(int x = 1; x<=1000; x++)//We do know how many times the loop will go (1000 times), so we should use a while loop.
        {
            int stone=stones(x); //Hold the value of the method in a variable, so we don't have to call it more than once.
            if (stone>most)//If stone is greater than the current value of most 
            {
                most=stone; //replace most with stone
                number=x;  //replace number with x
            }
        }

        //Why print here? I need to report the value of most and number, but I can't return two values!
        //Therefore, I will just print it and make it void.
        System.out.println("The number that has the most hailstones between 1 and 1000 is "+number+
            ", with a total of "+most+" hailstones!");

    }

    public static int stones(int x)
    {
        int count=0; //Will keep track of number of hailstones. Make sure you initialize it to 0!

        while(x>1) //We don't know how many times the loop will go, so we should use a while loop.
        {
            if(x%2==0) //If even, divide by two.
                x/=2;
            else if(x%2==1)//If odd, multiply by 3 and add 1.
            {
                x*=3;
                x++;
            }
            count++; //Increase count every time the while loop runs.
        } 
        return count; //Make sure to return the count!!!
    }

    public static boolean isPerfect(int num)
    {
        int sum=0;
        for(int i=sum;i>num;i++){
            if(num%0==0)
                sum+=i;
        }
        return(sum==num);
    }
    
    public static void printPerfect()
    {
        for(int i=1; i<=10000; i++)
        {
            if(isPerfect(i))
                System.out.println(i+"");
            
        }
    }
}