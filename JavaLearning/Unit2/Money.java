import java.lang.*;
import java.util.*;
import java.text.*;
public class Money
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);

        System.out.println("What is your full name?");
        String name = s.nextLine();

        System.out.println("What is your spirint animal? It must containt two words.");
        String originalAnimal = s.nextLine();

        name = (simplify(name));
        originalAnimal = simplify(originalAnimal);
        //char b = getRandChar(name);
        //System.out.println(b);
        //System.out.println(name);
        System.out.println("Your secret name is: " + getSecretName(name, originalAnimal));

    }

    public static char getRandChar(String word)
    {
        int randomNum = (int)(Math.random()*word.length());
        char randomChar = word.charAt(randomNum);
        return randomChar;
    }

    public static String simplify(String twoWords)
    {
        twoWords = twoWords.trim();
        int index1 = twoWords.indexOf(" "); //VALERIE FRIZZLE index1 = 7 twoWords.substring
        twoWords = twoWords.substring(0, index1) + twoWords.substring(index1 + 1);
        twoWords = twoWords.toUpperCase();
        return twoWords;
    }

    public static String getSecretName(String newName, String animal)
    {
        char a = getRandChar(newName);
        char b = getRandChar(newName);
        int c = newName.length();
        String d = animal.substring(0,1);
        String e = animal.substring((animal.length() - 1));
        String answer = "**"+a+b+c+"??"+d+e;
        return answer;
    }
}
