
/**
 * This program shows how to tell if a number is divisible by another number using %.
 * It uses if statements and if...else if...else statements.
 * It also uses a boolean variable.
 * 
 * This program will determine if a year is a leap year using the following rules:
 * 
 * 1. Most years that can be divided evenly by 4 are leap years.
 * (For example, 2016 divided by 4 = 504: Leap year!)

 * 2. Exception: Century years are NOT leap years UNLESS they can be evenly divided by 400.
 * (For example, 1700, 1800, and 1900 were not leap years, but 1600 and 2000, 
 * which are divisible by 400, were.)
 */
import java.util.Scanner;
public class Leap
{
    public static void main(String args[])
    {
        Scanner scan=new Scanner(System.in);
        System.out.println("Enter a year: ");
        int year=scan.nextInt();
        boolean isLeapYear;  //will be true if a year is a leap year, false otherwise
        //The remainder will be 0 if a number is divisible by another number so use %
        if(year%4==0 && year%100==0 && year%400==0)
        {
            isLeapYear=true;
        }
        else if(year%4==0 && year%100==0 && year%400!=0)
        {
            isLeapYear=false;         
        }
        else if(year%4==0)
        {

            isLeapYear=true;
        }
        else
        {
            isLeapYear=false;
        }
        //OR I can shorten it:
        if(year%400==0 || year%4==0 && year%100!=0)
            isLeapYear=true;
        else
            isLeapYear=false;
            
        //OR I can shorten it more:
        isLeapYear=(year%400==0 || year%4==0 && year%100!=0); //This will set isLeapYear to the truth value of the conditional statement! No if statements needed!
            
            
            
        if(isLeapYear)  //also acceptable to do if(isLeapYear==true)
        {
            System.out.println("That is a leap year!");
        }
        else //OR if(!isLeapYear)
        {
            System.out.println("That is not a leap year!");
        }
        /**
         * De Morgan's Laws
         * !(p || q) == !p && !q
         * !(p && q) == !p || !q
         */
        System.out.println("Would you like to hear a joke about Leap Day? "
            + "\nIf not, press 'Q'. If you press any other key you will be subjected to my humor.");
        char quit=scan.next().charAt(0); //I did next(), because if I did nextLine() I would have to clear the Scanner.
        /**
         * The user could press Q with or without the shift key, so we should include 'q' or 'Q'.
         * 
         * INCORRECT if(quit!='q' || quit!='Q')...tell joke (it should be &&)
         * Why? If the user enters 'q' or 'Q' we do NOT want the user to go on.
         * This is equivalent to !(quit=='q' || quit=='Q').
         * Using De Morgan's Laws to simplify: quit!='q' && quit!='Q'
         */
        if(quit!='q' && quit!='Q')
        {
            System.out.println("What kind of music do you listen to on Leap Day?...hip hop!");             
        }
        
        /**
         * Short circuit evaluation: When the result of a logical expression using && or || can be determined 
         * by evaluating only the first Boolean operand, the second is not evaluated.
         * 
         * In a compound conditional using a logical and (&&), the evaluation will short circuit 
         * (not execute the second condition) if the first condition is false.
         * 
         * In a compound conditional using a logical or  ( || ) , the evaluation will short circuit 
         * (not execute the second condition) if the first condition is true.
         */
        System.out.println("Enter any string, and I'll tell you if it ends with \"leap\"!");
        scan.nextLine(); //Now I have to clear the Scanner
        String entry=scan.nextLine();
        int len=entry.length(); 
        /**
         * This will result in a runtime error if the string's length is less than 4.
        if(entry.substring(len-4).equals("leap"))
        {
            System.out.println("That string ends in leap!");           
        }
        **/
        
        /**
         * In this if statement, if len<4, the first condition is false, so the second condition will be ignored.
         * Be careful. If I switch the order, short circuit evaluation won't work.
         * if(entry.substring(len-4).equals("leap") && len>=4) -->The check for len>=4 comes too late, runtime error still occurs
         * 
         */
        if(len>=4 && entry.substring(len-4).equals("leap")) 
        {
            System.out.println("That string ends in leap!");            
        }
        else
        {
            System.out.println("That string doesn't end in leap!");
        }
    }  
}

