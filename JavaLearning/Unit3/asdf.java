import java.lang.*;
import java.util.*;
import java.text.*;
public class asdf
{
    public static void main(String args[])
    {
        int x = 1;
        boolean result = (x%2==0);
        System.out.println(result);
    }

    public static double findBalance(String account, double balance)
    {
        if(balance<50&&account.equals("S"))
            balance-=15;
        if(balance<50&&account.equals("c"))
            balance-=20;
        if(balance>=50&&account.equals("S")){
            balance = balance+(balance*.03);
        }
        if(balance>=50&&balance<300&&account.equals("C"))
            balance = balance+(balance*.02);
        if(balance>=300&&account.equals("C"))
            balance = balance+(balance*.04);
        return balance;
    }
}
