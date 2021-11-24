
/**
 * This program shows you how to work with nested loops, which are loops within loops.
 * We will draw a rectangle with a given base and height using the '#' character.
 * Then, we will make the program repeat so the user can try other values.
 */
import java.util.Scanner;

public class NestedLoops
{
    public static void main(String args[])
    {
        // Scanner scan=new Scanner(System.in);
        // int base, height;
        // char choice='y';  //will hold whether or not user wants to go again, assume yes to start
        // while(choice=='y' || choice=='Y')
        // {
            // System.out.println("Enter the base of a rectangle: ");
            // base=scan.nextInt();
            // System.out.println("Enter the height of a rectangle: ");
            // height=scan.nextInt();

            // //Example: base=3, height=5
            // /* ###       //outside loop-->height determines number of lines
             // * ###      //new line at end of each line
             // * ###      //inside loop-->base determines how many characters are printed
             // * ###
             // * ###
             // */
            // for(int i=0; i<height; i++)  
            // {
                // for(int j=0; j<base; j++)
                // {
                    // System.out.print("#");
                // }
                // System.out.println();

            // }
            // System.out.println("Do you want to do another one (y/n)?");
            // scan.nextLine(); //clear Scanner when going from nextInt() or nextDouble() to nextLine()
            // choice=scan.nextLine().charAt(0);  //gets first character of String
            // //there is no nextChar() method
            
            System.out.println("Mirror: " + mirrorEnds("abcdef", "cba"));
            System.out.println("Mirror: " + mirrorEnds("", "hey"));
            System.out.println("Mirror: " + mirrorEnds("redo", "mother"));
            System.out.println("Mirror: " + mirrorEnds("abcd", "xyz"));
            System.out.println("Mirror: " + mirrorEnds("x", "x"));
            System.out.println("Mirror: " + mirrorEnds("abc", "fedcba"));
        }
    

    /**Given 2 strings, look for a "mirror" string at the beginning of the first string that matches the end of
     * the second string, but in reverse. 
     *In other words, zero or more characters at the very begining of the first string, 
     *and at the very end of the second string in reverse order. 
     *For example,  in the strings "goodness" and "dog", the "go" in the first string matches the "og" in the second string
     *and returns "go".

     *mirrorEnds("abcdef", "cba") → "abc"
     *mirrorEnds("", "hey") → ""
     *mirrorEnds("redo", "mother") → "re"
     *mirrorEnds("abcd", "xyz") → ""
     *mirrorEnds("x","x") → "x"
     *mirrorEnds("abc", "fedcba") → "abc"
     */  
    public static String mirrorEnds(String s1, String s2) {
        String mirror=""; //will hold the "mirror" string
        String part1=""; //will hold beginning of s1
        String part2=""; //will hold end of s2
        int len1=s1.length();
        int len2=s2.length();
        //The loop can only go as far as the shorter string
        for(int i=1; i<=Math.min(len1,len2); i++) //Math.min() returns smaller number, also could have used an if statement
        {
            part1=s1.substring(0,i); //first i characters of s1
            part2=s2.substring(len2-i);//last i characters of s2
            String part2Rev=""; //will hold reverse of part2
            for(int j=part2.length()-1; j>=0; j--) //start at end of part2 and add each character to part2Rev
            {
                part2Rev+=part2.substring(j,j+1);
            }
            if(part1.equals(part2Rev)) //if they are equal set mirror to part 1
                mirror=part1;
            else
                break; //otherwise, stop the loop
        }
        return mirror;
    }
}
