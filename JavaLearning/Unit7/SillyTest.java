/**
 * This program makes an ArrayList of 6 SillyStrings, each with 5 words.  Each element is
 * filled with a random animal from a String array.  Each SillyString is printed.
 * Then, one random animal is removed from each SillyString.
 */
import java.util.*;

public class SillyTest
{
    private static Scanner s=new Scanner(System.in);
    public static void main(String args[])
    {

        //array of animals for filling up the SillyStrings
        String strArr[]={"dog", "CAT", "Lion", "elephanT", "parrot", "cow", "antelope", "PANDA", "dragon", "zebra"};

        ArrayList<SillyString> ss=new ArrayList<SillyString>(); //an empty ArrayList of SillyStrings

        for(int i=0; i<6; i++)  //loop for 6 SillyStrings
        {
            ss.add(new SillyString()); //adds new SillyString to list 
            for(int j=0; j<5; j++) //loop for adding 5 Strings to each SillyString
            {
                //Random: High=strArr.length-1, Low=0;
                //int r=(int)(Math.random()*(High-Low+1)+Low);
                //int r=(int)(Math.random()*(strArr.length-1-0+1)+0);
                int r=(int)(Math.random()*(strArr.length));
                String ranAnimal=strArr[r]; //finds random animal from strArr           
                ss.get(i).addString(ranAnimal);
            }

        }
        printList(ss); //prints list of Silly Strings
        for(int i=0; i<ss.size(); i++) //loop through all SillyStrings
        {
            //Random: High=strArr.length-1, Low=0;
            //int r=(int)(Math.random()*(High-Low+1)+Low);
            //int r=(int)(Math.random()*(strArr.length-1-0+1)+0);
            int r=(int)(Math.random()*(strArr.length));
            String ranAnimal=strArr[r]; //finds random animal from strArr
            System.out.println("Word to be removed: " + ranAnimal);
            ss.get(i).removeWord(ranAnimal); //gets one SillyString and removes the random animal from it
            System.out.println(ss.get(i)); //prints out one SillyString, calls ss.get(i).toString()

        }
        addSilly(ss);
        printList(ss); //The new animals will be printed out once at the end.

        addWords(ss);
        printList(ss); //The new animals will be in each list in alphabetical order
        System.out.println(ss.get(1));
    }

    //prints an ArrayList of SillyStrings
    public static void printList(ArrayList<SillyString> arr)
    {
        /**
         * You could just do System.out.println(arr) and it will show all of the lists.
         * However, the brackets and commas will show up because it is an ArrayList.
         */
        int count=1;
        for(SillyString str : arr)
        {
            System.out.print("#" + count + " ");
            count++;
            System.out.println(str); //calls str.toString() (default)
        } 
        System.out.println("--------------------------------------------");
    }

    //You complete the next two methods.

    /**
     * Ask the user for 3 animals and add these animals to a new SillyString.  (Use a loop for this part!)
     * Then, add the SillyString onto the end of arr.
     */
    public static void addSilly(ArrayList<SillyString> arr)
    {
        arr.add(new SillyString());
        for(int i=0;i<3;i++)
        {
            System.out.println("Name an animal:");
            arr.get(arr.size()-1).addString(s.nextLine());
        }
    }

    /**
     * Ask the user for 3 animals (using a loop).  Add these three animals onto every SillyString in arr.
     */
    public static void addWords(ArrayList<SillyString> arr)
    {
        for(int i=0;i<3;i++)
        {
            System.out.println("Name an animal:");
            String animal=s.nextLine();
            for(int k=0;k<arr.size();k++)
                arr.get(k).addString(animal);
        }
    }
}
