import java.lang.*;
import java.util.*;
import java.text.*;
public class Island
{
    private static Scanner s = new Scanner(System.in);
    public static void main(String args[])
    {
        String userOccupation;
        String friend1Occupation;
        String friend2Occupation;
        
        System.out.println("Please enter your first name and the first names of two of your friends, all on separate lines.");
        String user = s.nextLine();
        String friend1 = s.nextLine();
        String friend2 = s.nextLine();

        userOccupation = getRandJob();
        friend1Occupation = getRandJob();
        friend2Occupation = getRandJob();

        System.out.println("Oh no! you are stranded on a deserted island with two of your friends!");
        System.out.println(user + " the " + userOccupation);
        System.out.println(friend1 + " the " + friend1Occupation);
        System.out.println(friend2 + " the " + friend2Occupation);
        System.out.println("You must grow food and make a shelter!");

        if(userOccupation == "farmer" || friend1Occupation == "farmer" || friend2Occupation == "farmer")
            System.out.println("There is a farmer among you! You will have food to eat!");
        else
            System.out.println("There is no farmer among you! you will die from lack of food!");

        if(userOccupation == "carpenter" || friend1Occupation == "carpenter" || friend2Occupation == "carpenter")
            System.out.println("There is a carpenter among you! you will have shelter");

        else
            System.out.println("There is no carpenter among you! You will die from exposure to the elements!");

        if((userOccupation == "farmer" || friend1Occupation == "farmer" || friend2Occupation == "farmer") && (userOccupation == "carpenter" || friend1Occupation == "carpenter" || friend2Occupation == "carpenter")){
            System.out.println(user + " After months of surviving, you have found a magical cave.");
            System.out.println("Inside of the cave is a boat!");
            System.out.println("You must solve three puzzles to enter the cave.");
            System.out.println("Puzzle 1 is for " + user + ":");
            boolean first = puzzle1(user);
            if(first==true){
                System.out.println("Congrats! You made it to puzzle 3!");
                System.out.println("Puzzle 2 is for " + friend1 + ":");
                boolean second = puzzle2(friend1);
                if(second==true){
                    System.out.println("Congrats! You made it to puzzle 3!");
                    System.out.println("puzzle 3 is for " + friend2 + ":");
                    boolean third = puzzle3(friend2);
                    if(third==true){
                        System.out.println("You escaped! Hooray!");
                    }
                    else{
                        System.out.println("Sorry, you will not survive much longer. Better luck next time!");

                    }
                }
                else{
                    System.out.println("Sorry, you will not survive much longer. Better luck next time!");

                }
            }
            else{
                System.out.println("Sorry, you will not survive much longer. Better luck next time!");

            }
        }

        else{
            System.out.println("Sorry, you will not survive much longer. Better luck next time!");

        }
    }

    public static String getRandJob()
    {
        int randomNum=(int)(Math.random()*4)+1;
        if(randomNum==1)
            return "farmer";
        if(randomNum==2)
            return "carpenter";
        if(randomNum==3)
            return "dancer";
        return "comedian";
    }

    public static boolean puzzle1(String name)
    {
        System.out.println(name+", give me a word that starts and ends with the first letter of your name.");
        String attempt = s.nextLine();

        if(attempt.substring(0,1).equalsIgnoreCase(name.substring(0,1)) && attempt.substring(attempt.length()-1).equalsIgnoreCase(name.substring(0,1)))
            return true;
        return false;
    }

    public static boolean puzzle2(String name)
    {
        System.out.println(name+", I am thinking of an integer that is equal to the ones digit of the square of the length of your name.");
        System.out.println("What is the integer");
        int attempt = s.nextInt();

        int lengthSquared = (int)Math.pow(name.length(), 2);
        int onesDigit = lengthSquared%10;
        if(attempt==onesDigit)
            return true;
        return false;
    }

    public static boolean puzzle3(String name)
    {
        System.out.println(name+", if your first name contains an 'A', then enter the square root \nof twice the length of your first name rounded to the neares integer.");
        System.out.println("If your first name does not contain an 'A', then enter the cube root \nof twice the length of your first name rounded to the nearest integer");
        int attempt = s.nextInt();

        name=name.toLowerCase();

        int cubeRoot = (int)(Math.cbrt(name.length()*2)+0.5);
        int squareRoot = (int)(Math.sqrt(name.length()*2)+0.5);

        if(name.indexOf("a")>=0 && attempt==squareRoot)
            return true;
        if(name.indexOf("a")==-1 && attempt==cubeRoot)
            return true;
        return false;
    }
}
