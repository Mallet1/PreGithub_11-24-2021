import java.util.*;

public class ArrayListAlgorithms
{
    public static void main(String args[])
    {
        ArrayList<Integer> arr1=new ArrayList<Integer>();
        ArrayList<String> arr2=new ArrayList<String>();

        fill(arr1);
        System.out.println(arr1);
        int big=countBig(arr1);
        System.out.println("There are " + big + " numbers over 25.");
        removeEven(arr1);
        System.out.println(arr1+"\n");
        
        arr2.add("Pretty");
        arr2.add("pretty");
        arr2.add("please");
        arr2.add("let");
        arr2.add("summer");
        arr2.add("start");
        arr2.add("soon");

        toUpper(arr2);
        System.out.println(arr2);
        ArrayList<String> arr3=firstLets(arr2);
        System.out.println(arr3);
    }

    /**
     * Fill the Integer ArrayList a with a random number of values from 5-10.
     * Each value should be a random integer from 1-50
     * Precondition: a is an empty ArrayList
     * 
     */
    public static void fill(ArrayList<Integer> a)
    {
        int size=(int)(Math.random()*6+5); //Make list a random size from 5-10
        for(int i=0; i<size; i++)
        {
            int x=(int)(Math.random()*50+1); //random value from 1-50
            a.add(x); //add to end of ArrayList
        }
    }
    /**
     * Return the number of Integers in a greater than 25 
     */
    public static int countBig(ArrayList<Integer> a)
    {
        int count=0;
        for(Integer val : a) //for-each loop--you can also do int val because of auto-boxing
        {
            if(val>25)
                count++;
        }
        return count;
    }
    /**
     * Remove every even value from a
     * 
     * You should go backwards if using a for loop to remove items!
     * Example: a = {3, 5, 6, 8, 10, 1} remove the 6 at i = 2
     * a = {3, 5, 8, 10, 1} i++ makes i = 3, which is the 10
     * The 8 was skipped!
     */
    public static void removeEven(ArrayList<Integer> a)
    {
        for(int i=a.size()-1; i>=0; i--) //need to go backwards to preserve order of indices
        {
            if(a.get(i)%2==0)
                a.remove(i);
        }
    }
    /**
     * Converts a String ArrayList so that all elements are strictly uppercase letters
     * Precondition: w is an empty ArrayList
     */
    public static void toUpper(ArrayList<String> w)
    {
        for(int x=0; x<w.size(); x++)
            w.set(x, w.get(x).toUpperCase()); //replace every element with the previous element converted to uppercase     
    }
    /**
     * Converts a new ArrayList of Strings that holds the first letters of all of the Strings in s
     * Precondition: s is non-empty
     * Postcondition: s remains unchanged
     */
    public static ArrayList<String> firstLets(ArrayList<String> s)
    {
        ArrayList<String> w=new ArrayList<String>();
        for(int i=0; i<s.size(); i++)
            w.add(s.get(i).substring(0,1)); //add first letter of each element to w
        return w;
    }

}
