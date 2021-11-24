import java.lang.*;
import java.util.*;
import java.text.*;
public class asdf
{
    public static void main(String[] args)
    {
            ArrayList<Double> nums = new ArrayList<Double>();

nums.add(5.0);

nums.add(2.0);

nums.add(6.0); 

nums.add(2.0);

nums.add(4.0);

nums.add(9.0);

nums.set(nums.size()-1, 5.7);

System.out.println(nums);

ArrayList<Double> arr = new ArrayList<Double>(20);

System.out.println(arr.size());
    }
}