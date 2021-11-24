
/**
 * A SillyString contains an ArrayList of Strings
 * It takes the reverse of each string and
 * it adds it to the list in alphabetical order, ignoring the case.
 * 
 * cat--> tac
 * DOG--> GOD, tac
 * dolphin--> GOD, nihplod, tac  //alphabetical order
 */
import java.util.*;

public class SillyString 
{
    //ArrayList field to hold list of Strings
    private ArrayList<String> s; //Declare the ArrayList, but don't initialize it yet

    public SillyString() //default constructor
    {
        s=new ArrayList<String>(); //initialize the ArrayList       
    }

    /**
     * private helper method to reverse the order of a String
     * I made it private because I don't want anyone to use it outside of this class.
     */
    private String reverse(String str)
    {
        String rev="";
        for(int i=str.length()-1; i>=0; i--) //goes through chars in the String backwards
        {       
            rev+=str.substring(i,i+1);
        }
        return rev;
    }

    public void addString(String str)
    {
        str=reverse(str); //reverse the String before adding it to the list
        /**
         * When adding to an ordered list, you need to think of three situations:
         * 1) What if the list is empty?  Then I just want to add to the end.
         * 2) What if the element I'm adding is greater than every item in the list?
         * Then, I also want to add to the end.
         * 3) What if neither of the previous two situations is true?  Then, I have to figure
         * out where I should put it by going through the list.
         */
        
        if(s.size()==0) //if the list is empty
        {
            s.add(str); //just add str to the end
        }
        else if(str.compareToIgnoreCase(s.get(s.size()-1))>=0) //if str is greater than the last element
        {
            s.add(str);   //just add str to the end         
        }
        else  //otherwise, str belongs at the beginning or in the middle of the list
        {
            //Example list: {"a", "c", "h", "m"}  What if I want to insert "e"?
            //"e">"a" keep going, "e">"c" keep going, "e"<"h" STOP!
            for(int i=0; i<s.size(); i++)
            {
                if(str.compareToIgnoreCase(s.get(i))<0) //if str is less than an element, 
                //this is where str should be inserted!
                {
                    s.add(i,str); //add str at position i
                    break; //stop the loop or you will keep adding str
                }
            }
        }
    }
    public String toString()
    {
        String output="Silly String: ";
        for(String str : s)
        {
            output+= str + " ";            
        }
        return output + "\n";
    }
    /**
     * This method takes a String parameter, word.  It will reverse the word, and then search
     * for it in the list.  It will remove the word from the list, and print out the word that
     * was removed.
     */
    public void removeWord(String word) 
    {
        word=reverse(word); //reverse word
        for(int i=s.size()-1; i>=0; i--) //loop backwards so the shifting indices don't mess us up
        {
            if(s.get(i).equalsIgnoreCase(word))
            {
               String rem=s.remove(i); //rem stores the value that was removed
               System.out.println("Removed from list: " + rem);
               /**I could also do: 
               System.out.println("Removed from list: " + s.remove(i));
               This would remove and print at the same time!*/
            }            
        }
        /**
         * Remember: The set method also returns a value: the element that was replaced
         * Example: Assume that the element with an index of three is "tac" (reverse of cat)
         * String rep=s.set(3,"mom");
         * rep="tac", s.get(3) would return "mom"        
         */   
    }

}



