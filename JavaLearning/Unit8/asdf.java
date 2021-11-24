import java.lang.*;
import java.util.*;
import java.text.*;
public class asdf
{
    public static void main(String[] args)
    {
        String[][] letters = {{"A","B","C","D"},
                {"E","F","G","H"},
                {"I","J","K","L"}};

        for(int col=1; col<letters[0].length; col++)
        {
            for(int row = 1; row<letters.length; row++)
                System.out.print(letters[row][col]+" ");
            System.out.println();
        }
                           
        /*
        for(int i=0; i<mat.length; i++) //loop through rows
        {
        for(int j=0; j<mat[0].length; j++)//loop through cols
        {
        System.out.print(mat[i][j] + " ");
        }
        System.out.println(); //do a new line after each row
        }
        System.out.println();*/
    }
}