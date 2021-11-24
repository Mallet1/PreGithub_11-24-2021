import java.lang.*;
import java.util.*;
import java.text.*;
public class RightTri
{
    private double leg=0;
    private static char drawChar;

    public RightTri()
    {
        leg=1.0;
    }

    public RightTri(double legLength)
    {
        leg=legLength;
    }
    
    public RightTri(RightTri RightTri)
    {
        this.leg=RightTri.leg;
    }

    private double hypotenuse()
    {
        double newHypotenuse=leg*Math.sqrt(2);
        return newHypotenuse;
    }

    public static double tangent(double angle)
    {
        double newTangent=Math.tan(Math.toRadians(angle));
        return newTangent;
    }

    public double area()
    {
        double newArea=Math.pow(leg,2)/2.0;
        return newArea;
    }

    public String toString()
    {
        return "LegLength = "+leg+" Hypotenuse = "+hypotenuse();
    }
    
    public void drawTri()
    {   
        for(int i=1;i<=Math.round(leg);i++)
        {
            for(int k=1;k<=i;k++)
            {
                System.out.print(drawChar);
            }
            System.out.println();
        }
    }   
    
    public static void setDrawChar(char letter)
    {
        drawChar=letter;
    }
}
