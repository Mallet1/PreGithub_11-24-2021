
/**
 * This program shows a simple while loop, a while loop that uses a Scanner inside,
 * and a while loop used for error trapping.
 */
import java.util.Scanner;

public class WhileLoops
{
    public static void main(String args[])
    {
        Scanner scan=new Scanner(System.in);
        int upperBound,count;
        System.out.println("Enter a positive number, and I will count up to it "
        + "starting at 1. ");
        upperBound=scan.nextInt();
        while(upperBound<1)  //will continuously ask user for number until a valid value is entered
        {
           System.out.println("Number must be positive.");
           System.out.println("Enter a positive number, and I will count up to it "
           + "starting at 1. ");
            upperBound=scan.nextInt();
            
        }
        //keep counting until count>upperBound
        //so, keep counting while count<=upperBound
        
        count=1; //give count a starting value
        while(count<=upperBound)
        {
            System.out.println(count);
            count++;      
        }
        
        
        int sum=0;  //give sum a starting value
        System.out.println("Enter a non-negative number to add to the sum (negative to quit)");
        int num=scan.nextInt();
        while(num>=0)
        {
              sum+=num;  //sum=sum+num;
              System.out.println("Enter a non-negative number to add to the sum (negative to quit)");
              num=scan.nextInt();
        }
        System.out.println("The sum is " + sum + ".");
     
    }
}
