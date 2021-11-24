import java.lang.*;
import java.util.*;
import java.text.*;
public class LineSegment
{
    private static DecimalFormat fmt=new DecimalFormat("#.000");
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);

        System.out.println("Enter the integer x and y coordinates of the first line segment.");
        System.out.print("X1:");
        int x1=s.nextInt();

        System.out.print("Y1:");
        int y1=s.nextInt();

        System.out.println("Enter the integer x and y coordinates of the second line segment.");
        System.out.print("X2:");
        int x2=s.nextInt();

        System.out.print("Y2:");
        int y2=s.nextInt();

        System.out.println("Information for the line segment with coordinates (" + x1 + ", " + y1 + ") and (" + x2 + ", " + y2 + "):");

        System.out.println("Length: " + fmt.format(getLength(x1,x2,y1,y2)));
        System.out.println("Midpoint: (" + getMidpointX(x1,x2,y1,y2) + ", " + getMidpointY(x1,x2,y1,y2) + ")");
        System.out.println("Slope: " + fmt.format(getSlope(x1,x2,y1,y2)));
        System.out.println("Y-Intercept: " + fmt.format(getIntercept(x1,y1,getSlope(x1,x2,y1,y2))));
        System.out.println("y = " + fmt.format(getSlope(x1,x2,y1,y2)) + "x + " + fmt.format(getIntercept(x1,y1,getSlope(x1,x2,y1,y2))));
    }

    public static double getLength(int x1, int x2, int y1, int y2)
    {
        double length = Math.sqrt(Math.pow((x2-x1),(2))+Math.pow((y2-y1),(2)));
        return length;
    }

    public static double getMidpointX(int x1, int x2, int y1, int y2)
    {
        double midPointX = (x1+x2)/2.0;
        return midPointX;
    }

    public static double getMidpointY(int x1, int x2, int y1, int y2)
    {
        double midPointY = (y1+y2)/2.0;
        return midPointY;
    }

    public static double getSlope(int x1, int x2, int y1, int y2)
    {
        double slope = ((double)y2-y1)/((double)x2-x1);
        return slope;
    }

    public static double getIntercept(int x1, int y1, double slope)
    {
        double intercept = y1-(slope*x1);
        return intercept;
    }
}
