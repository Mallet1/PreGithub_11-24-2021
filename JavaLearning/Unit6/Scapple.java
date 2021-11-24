import java.lang.*;
import java.util.*;
import java.text.*;
public class Scapple
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int again=1;

        System.out.println("Welcome to my Scapple game!");
        while(again==1)
        {
            System.out.println("Enter a word:");
            String newWord=s.nextLine();

            WordTiles w = new WordTiles(newWord);
            System.out.println(w.toString());
            System.out.println("That word is worth "+w.getWordScore()+" points.");

            System.out.println("Do you want to enter another word? (1=yes 2=no)");
            again=s.nextInt();
            while(again!=1&&again!=2)
            {
                System.out.println("Invalid response. Do you want to enter another word? (1=yes 2=no)");
                again=s.nextInt();
            }
            s.nextLine();
        }
    }
}
