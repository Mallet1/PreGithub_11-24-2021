import java.util.*;
public class asdf
{
    public static void main(String[] args)
    {
        double x = -3265.0;
        System.out.println(Math.pow(x, .5) == Math.sqrt(x));
System.out.println(replaceHi("hi hi dog hi Hi"));
System.out.println("wats up")
    }
    
public static String replaceHi(String str)

{
   if(str.length() < 2)
        return "";
   else if(str.length() <= 2)

      return str.substring(0,2);

   else if(str.substring(0,1).equals("hi"))

      return "bye" + replaceHi(str.substring(3));

   else

      return str.substring(0,2) + replaceHi(str.substring(3));

}
}
