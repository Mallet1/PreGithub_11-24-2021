
/**
 * This program calculates a letter grade based on a percentage grade.
 * It uses if statements and if...else if...else statements.
 */
import java.util.Scanner;
public class LetterGrades
{
    public static void main(String args[])
    {
        Scanner scan=new Scanner(System.in);
        System.out.println("Enter your grade as a percentage: ");
        double grade=scan.nextDouble();
        char letter=' '; //will hold letter grade
        //Logical Operators: &&--AND  ||--OR  !--NOT
        //Relational Operators: ==, <=, >=, <, >, !=
        // if(grade>=90)
        // {
           // letter='A'; 
            
        // }
        // if(grade<90 && grade>=80)
        // {
            
            // letter='B';
        // }
        // if(grade<80 && grade>=70)
        // {
            
            // letter='C';
        // }
        // if(grade<70 && grade>=60)
        // {
            
            // letter='D';
        // }
        // if(grade<60)
        // {
            // letter='F';
        // }
        if(grade>=0 && grade<=100)
        {
            if(grade>=90)
                letter='A';
            else if(grade>=80)
                letter='B';
            else if(grade>=70)
                letter='C';
            else if(grade>=60)
                letter='D';
            else
                letter='F';
                
            System.out.println("You have a(n) " + letter + ".");
       }
       else
       {
           System.out.println("That grade is not possible.");
           
       }
    }
}
