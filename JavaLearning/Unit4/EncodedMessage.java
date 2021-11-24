import java.lang.*;
import java.util.*;
import java.text.*;
public class EncodedMessage
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);

        System.out.println("Enter a phrase with a length greater than or equal to 10.");
        String message = s.nextLine();
        if(message.length()<=9){
            while(message.length()<=9){
                System.out.println("That is an invalid entry. Try again.");
                message = s.nextLine();
            }
        }

        System.out.println("Enter one code word with a length less than 7.");
        String codeWord = s.nextLine();
        if(codeWord.length()>7||codeWord.indexOf(" ")==1){
            while(codeWord.length()>7||codeWord.indexOf(" ")==1){
                System.out.println("That is an invalid entry. Try again.");
                codeWord = s.nextLine();
            }
        }
        codeWord=codeWord.toUpperCase();
        message=message.toUpperCase();
        System.out.println("Here is your encoded phrase: "+(encode(message, codeWord).toUpperCase()));
    }

    public static String getRandString(String codeWord)
    {
        int i = 0, k = 0;
        i = (int)(Math.random()*codeWord.length());
        k = (int)(Math.random()*codeWord.length())+1;

        while(i>=k){
            i = (int)(Math.random()*codeWord.length());//length-1-0+1
            k = (int)(Math.random()*codeWord.length())+1;}
        /*String newI=""+i +" "+ k;
        System.out.println(newI);*/

        String subCodeWord = codeWord.substring(i,k);
        System.out.println(subCodeWord);
        return subCodeWord;
    }

    public static String encode(String original, String codeWord)
    {
        String encodedWord="";
        boolean x=false;
        for(int i=0;i<original.length();i++)
        {
            for(int k=0;k<codeWord.length();k++)
            {
                if(original.substring(i,i+1).equalsIgnoreCase(codeWord.substring(k,k+1)))
                {
                    encodedWord+=getRandString(codeWord);
                    x=true;
                }
            }
            if(!x)
                encodedWord+=original.substring(i,i+1);
            x=false;
        }
        //System.out.println();
        return encodedWord;
    }
}
