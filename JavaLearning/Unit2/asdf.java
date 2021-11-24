import java.lang.*;
import java.util.*;
import java.text.*;
public class asdf
{
    public static void main(String args[])
    {
        System.out.println(bingo());
    }

    public static int bingo()
    {
        int randBingo = (int)(Math.random()*15)+61;
        return randBingo;
    }
}

