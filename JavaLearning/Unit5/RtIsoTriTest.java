import java.lang.*;
import java.util.*;
import java.text.*;
public class RtIsoTriTest
{
    public static void main(String args[])
    {
        
        RightTri first = new RightTri();
        RightTri second = new RightTri(5.0);
        RightTri third = new RightTri(7.7);
        RightTri fourth = new RightTri(second);
        
        System.out.println(first.toString());
        System.out.println();
        first.setDrawChar('*');
        first.drawTri();
        System.out.println();
        System.out.println("The area is " + first.area());
        System.out.println();
        
        System.out.println(second.toString());
        System.out.println();
        second.setDrawChar('*');
        second.drawTri();
        System.out.println();
        System.out.println("The area is " + second.area());
        System.out.println();
        
        System.out.println(third.toString());
        System.out.println();
        third.setDrawChar('$');
        third.drawTri();
        System.out.println();
        System.out.println("The area is " + third.area());
        System.out.println();
        
        System.out.println(fourth.toString());
        System.out.println();
        fourth.setDrawChar('$');
        fourth.drawTri();
        System.out.println();
        System.out.println("The area is " + fourth.area());
        System.out.println();
        
        for(int i=0;i<=180;i+=15)
        {
            System.out.println("The tangent of "+i+" is "+first.tangent(i));
        }
    }
}
