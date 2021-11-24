 /**
 * String Methods on the AP test:
 * The String constructor
 * length()
 * Both versions of substring()
 * indexOf()
 * equals()
 * compareTo()
 * 
 * But...Other methods are very useful too!!!
 * charAt()
 * trim()
 * equalsIgnoreCase()
 * compareToIgnoreCase()
 * toUpperCase()
 * toLowerCase()
 * replace()--can be useful, but you probably want to avoid it on the AP test.
 * concat()--not very useful, just use '+'
 * 
 */




import java.util.*;
public class StringMethods
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        
        //Length
        String name="Mrs. Frizzle"; //length=12
        System.out.println("The length of my name is " + name.length()+"\n"); //start counting at 1 for length
        
        //Concatenation
        String job="teacher";
        String title=name + ": " + job; //concatenation
        System.out.println(title);
        String awesome=title.concat("...she's awesome!"); //also does concatenation
        System.out.println(awesome+"\n");
        
        
        //UpperCase
        
        //title.toUpperCase(); 
        //This does nothing.  You must set it to a string
        //because strings are IMMUTABLE (methods can't change them)
        
        //The correct way to convert to uppercase is:
        title=title.toUpperCase(); //title="MRS. FRIZZLE: TEACHER"
        System.out.println("title = " + title+"\n");
        
        //Replacement
        String title2=title.replace('R','X'); //replace R with X
        System.out.println(title2+"\n"); //title2="MXS. FXIZZLE: TEACHEX"
        
        //indexOf
        int space=title.indexOf(' '); //returns index of first space in title, 4
        int u=title.indexOf('U'); //returns -1 because there is no 'U' in title
        int frizz=title.indexOf("FRIZZ");//returns the index where "FRIZZ" starts, 5
        
        System.out.println("Space: " + space + "\tU: " + u + "\tFRIZZ: " + frizz + "\n");
        
        //charAt
        char first=title.charAt(0); //returns character at index=0, 'M'
        char last=title.charAt(title.length()-1); //returns last character (index is always length-1)
        
        System.out.println("First letter: " + first + "\tLast letter: " + last + "\n");
        
        //substring
        /**
         * title="MRS. FRIZZLE: TEACHER"
         * Just print out the FRIZZLE part.
         */
        String frizzle=title.substring(5,12); //start at 5 and end at 11
        //12-5=7 which is the length of FRIZZLE
        /**
         * How about just TEACHER?
         */
        String teacher=title.substring(14); //starts at 14 and goes to the end of the String, Don't put a second number 
        //if you don't need to. 
        System.out.println(frizzle + "\n" + teacher);
        /**
         * Ask how many characters.
         */
        System.out.println("How many characters do you want? ");
        int chars=s.nextInt();
        System.out.println("Here they are: " + title.substring(0,chars) + "\n");
        
        s.nextLine(); //THIS CLEARS THE SCANNER. YOU NEED TO DO THIS WHENEVER YOU GO FROM ASKING FOR A PRIMITIVE TYPE
        //TO ASKING FOR A STRING WITH NEXTLINE
        
        //equals and compareTo
        //Let's compare Strings!  Don't use ==, <, >, !=
        //These will compare their addresses (in memory)
        String s1="apples";
        String s2="cherries";
        String s3="Apples";
        String s4="grapes";
        String s5="guavas";
        
        //compareTo() compares ASCII values, you can subtract to find the exact number, but pos/neg is really all that matters
        //In ASCII table: numbers < capital letters < lowercase letters
        System.out.println(s1.compareTo(s2)); //s1-s2 a-c=97-99=-2
        System.out.println(s1.compareTo(s3)); //s1-s3 a-A=97-65=pos    
        //OR assign Apples =1 and apples=2 because 'a' comes after 'A' in the ASCII table, then do 2-1=positive
        System.out.println(s1.compareToIgnoreCase(s3));//0
        System.out.println(s4.compareTo(s2)); //s4-s2=g-c=2-1=pos
        System.out.println(s4.compareTo(s5)); //s4-s5 r-u=1-2=neg (compares second char because first char is the same)
        
        System.out.println(s3.equals(s1)); //prints false, s3 and s1 don't hold the same value
        System.out.println(s1.equalsIgnoreCase(s3)); //prints true, s3 and s1 are the same if you ignore the case.

        if(s1.compareTo(s4)<0) 
        {
            System.out.println(s1 + " comes before " + s4);            
        }
        else if(s1.compareTo(s4)>0)
        {
            System.out.println(s4 + " comes before " + s1);  
        }
        else
        {
            System.out.println(s1 + " is the same as " + s4);  
        }
        System.out.println();
        
        
        //Method testing
        System.out.println("Enter an HTML tag: ");
        String html=s.nextLine();
        String convert=removeHTML(html);
        System.out.println("Converted from HTML: " + convert + "\n");
        
        System.out.println("Enter a string to split: ");
        String entry=s.nextLine();
        System.out.println("What character do you want to use to split it?");
        char x=s.nextLine().charAt(0); //gets first char of string entered, could also use next() instead of nextLine()
        String split=split(entry,x);
        System.out.println("Split string: " + split + "\n");
        
        
    }
    /**
     * removeHTML()--takes a String parameter that represents an HTML tag, removes the '<' and '>', converts it to all
     * lowercase letters, and returns the result.
     * Precondition: The parameter is a String in the form "<" + string + ">".
     * 
     * A precondition is an assumption you can make about the parameter(s).
     * 
     */
    //Strategy: Use a concrete example when figuring out a "rule" or "formula". This rule is also called an algorithm.
    //example: removeHTML("<MARQUEE>") would return "marquee"
    //length=9 and I want the positions to go from 1-7, the total length of my answer will be 7
    //So... s=s.substring(1,8) (starts at position 1, 8-1=7-->the length of result and 8 is one past 7)  
    //How do I get 8? length -1!
    //final formula: s=s.substring(1,s.length()-1)
    public static String removeHTML(String s) 
    {
        s=s.toLowerCase(); //converts s to lowercase (If it's already lowercase, it won't do anything.)
        return s.substring(1,s.length()-1);    
    }
    /**
     * split()--takes a String parameter and a char parameter, splits the string into two words, with the split occurring at the
     * char parameter, and returns a String made up of these two words.
     * Precondition: The char parameter appears exactly once in the String parameter.
     * 
     * 
     */
    //example: split("like/unlike",'/') would return "like unlike"; '/' is at position 4,
    //word1=substring(0,4), word2=substring(5)
    public static String split(String s, char ch)
    {
        int pos=s.indexOf(ch); //finds position of the character parameter
        String word1=s.substring(0,pos);
        String word2=s.substring(pos+1);
        return word1 + " " + word2;
    }
    public static String birthday(String b)
    {
        String month = b.substring(0,2);
        String day = b.substring(3,5);
        String year = b.substring(6);
        
        return day+month+year;
    }
}




