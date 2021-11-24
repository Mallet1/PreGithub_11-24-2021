import java.util.*;
public class Voters
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Welcome to the polls!");
        System.out.println("What is your first name?");
        String first=s.nextLine();
        System.out.println("What is your last name?");
        String last=s.nextLine();
        System.out.println("How old are you?");
        int age=s.nextInt();
        s.nextLine(); //clear Scanner
        boolean canVote=vote(age);
        if(canVote) //if(canVote==true)
        {
            System.out.println("Are you here with someone else today? (yes/no)");
            String companion=s.nextLine();
            if(companion.equalsIgnoreCase("yes")) //OPPOSITE if(!companion.equalsIgnoreCase("yes"))
            {
                System.out.println("What is your companion's first name?");
                String compFirst=s.nextLine();
                System.out.println("What is your companion's last name?");
                String compLast=s.nextLine();
                if(last.compareTo(compLast)<0) //your last name is first alphabetically
                { 
                    System.out.println("You will vote before your companion.");
                }
                else if(last.compareTo(compLast)>0) //your last name is last alphabetically
                {
                    System.out.println("You will vote after your companion.");
                }
                else  //same last name, now compare first name
                {
                    if(first.compareTo(compFirst)<0)
                    {
                        System.out.println("You will vote before your companion.");
                    }
                    else if(first.compareTo(compFirst)>0) 
                    {
                        System.out.println("You will vote after your companion.");
                    }
                    else
                    {
                        System.out.println("You have the same name as your companion? That's crazy!");
                    }
                }
            }
            System.out.println("Enjoy your voting experience, and please come again.");
        }
        else //if(!canVote) --> if(canVote==false)
        {
            System.out.println("Nice try, " + first + " " + last + ", but you are too young to vote!");        
        }
    }   

    /**
     * Write a method that takes the age as a 
     * parameter and returns true 
     * if the person can vote, false otherwise.
     */
    public static boolean vote(int age)
    {
        /*
         * if(age>=18)
         *      return true;
            else
                return false;  */

        /* boolean v;
        if(age>=18)
        v=true;
        else
        v=false;
        return v;  */

        /* boolean v;
        if(age>=18)
        v=true;
        if(age<18)
        v=false;
        return v; */ //incorrect, v could possibly not have a value

        /* if(age>=18)
        boolean v=true;
        else
        boolean v=false;
        return v; */ //incorrect, v must be declared outside of ifs

        /* if(age>=18)
        return true;
        else if(age<18)
        return false;
         */ //incorrect--may not return anything

        /* if(age>=18)
              return true;
           return false;  */ //CORRECT

        return (age>=18);
    }

}


