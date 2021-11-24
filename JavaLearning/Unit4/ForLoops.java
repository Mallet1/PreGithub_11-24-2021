
/**
 * This program shows various uses of for loops.
 * Use a for loop when you know the start and stop values for your loop.
 * 
 * Format:
 * for(initialize; condition; update)
 * {
 *     //stuff to repeat
 * }
 */
import java.util.Scanner;

public class ForLoops
{
    public static void main(String args[])
    {
        Scanner scan=new Scanner(System.in);
        int count;
       
        //Forward loop
        //This for loop starts at 1 and counts up by 1.  It continues to run while count<=5.
        for(count=1; count<=5; count++)  
        {
           System.out.println(count);
            
        }
        
        //Backward loop
        //i is a common variable used in a for loop.  
        //The value that changes (i) is called an iterator.
        //This for loop starts at 5 and counts down by 1.  It continues to run while i>=1.
        for(int i=5; i>=1; i--)  //you can declare value of i inside of the loop
        {
           System.out.println(i);
            
        }
        
        //Since i was declared in the loop, I can use it again!
        //Write a loop that starts at 5 and counts up by 5's until it reaches 50
        for(int i=5; i<=50; i+=5)  //or i=i+5
        {
            System.out.println(i);
        }
        
        //The user will enter 5 integers.  Count how many even and odd numbers are entered.
        int odds=0, evens=0; //initialize variables
        int num;
        System.out.println("Enter 5 integers: ");
        for(int i=1; i<=5; i++) //OR for(int i=0; i<5; i++)
        {
            System.out.println("Enter number " + i + ": "); //counts the numbers, will have to change to (i+1) if you start at i=0
            num=scan.nextInt();
            if(num%2==0) //if num is divisible by 2 (even)
            {
                evens++;
            }
            else
            {
                odds++;                
            }            
        }
        System.out.println("You entered " + evens + " evens and " + odds + " odds.");
        
    }
}
