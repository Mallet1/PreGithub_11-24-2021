
import java.util.*;
public class Methods
{
   
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        hello(); //void methods are always called all by themselves
        //System.out.println(hello()); not allowed
        //int x=hello(); not allowed
        System.out.println("What is your name? ");
        String name=s.nextLine();
        helloName(name); //name is an actual parameter
        String nickName=getNickname(name);
        System.out.println("What's up, " + nickName + "?");
        
        int r1=round(56.2);
        int r2=round(56.8);
        System.out.println(r1 + " " + r2);
        
        int a=average(4,5,8); //should be 6
        System.out.println("The average is " + a + ".");
        
        //Ask user for three integers and print out the average of those ints
        System.out.println("Enter three integers: ");
        int num1=s.nextInt();
        int num2=s.nextInt();
        int num3=s.nextInt();
        //int a2=average(num1,num2,num3); //You can make a separate variable or put it all in the print statement.
        System.out.println("The average is " + average(num1,num2,num3) + ".");
        
        //Test circArea() with radius=10
        
        //Test coneVolume() and coneSurfaceArea() with radius=10, height=5        
        
        
        
        
    }
    /**
     * All methods that you call in the main method must be static
     * because the main method is static.
     */
    /**
     * Void method--no return type, usually used when you want to print
     * something
     */
    //hello()-->prints out hello
    public static void hello()
    {
        System.out.println("Hello!");
        
    }
    //helloName()-->takes a String parameter (name) and prints "Hello, name!"
    public static void helloName(String name) //name is a formal parameter
    {
        System.out.println("Hello, " + name + "!");
        
    }
     
    //getNickName()--> returns a nickname for a String parameter-->adds dog to the end
    public static String getNickname(String name)
    {
        String nick=name + " dog";
        return nick;
        
        //OR--you could do this all in one line:
        //return name + " dog";
        
    }
    //round()-->takes a double and returns it rounded to the nearest integer
    public static int round(double x)
    {
        return (int)(x + 0.5);
        
    }
    
    //average()-->takes three integers and returns the average rounded to the nearest integer
    public static int average(int x, int y, int z)
    {
        double avg=(x+y+z)/3.0;
        return round(avg); //Use the method you made. Rewriting code when it is unnecessary is inefficent,
        //and you will lose points on the AP test!
    }
    
    
    /**
     * Write two methods. Test each one in the main method. Don't rewrite code!
     * 
     * circArea()-->Takes a radius as a double and returns area of circle.  
     * Use the Math class to find the value of pi.  
     * Test data: radius=10, area=314.2
     * 
     * coneVolume()-->Takes the radius of the base of a 
     * right circular cone and the height 
     * of the cone, both as doubles, and returns the volume of the cone.
     * Volume of cone=(1/3)*AreaofBase*height  
     * Test data: radius=10, height=5, vol=523.6
     * 
     * Challenge--Write a method that returns surface area of a cone 
     * given height and radius.
     * Surface Area of a cone = AreaofBase+LateralArea
     * Lateral Area = pi*radius*slantHeight  
     * Test data: radius=10, height=5, SA=665.4
     */
     
    
}









