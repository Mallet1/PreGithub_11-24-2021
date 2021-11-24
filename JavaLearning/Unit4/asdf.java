import java.lang.*;
import java.util.*;
import java.text.*;
public class asdf
{
    public static void main(String args[])
    {
        for(int j=1;j<=5;j++)
        {
            for(int k=5;k>=j;k--)
            {

                System.out.print(j+" ");
            }
            System.out.println();
        }
    }

    public static int addOdds(int num)

    {
        int temp = 0;
        for(int i=1;i<=num;i+=2)
        {
            temp+=i;
        }
        return num;
    }


}
