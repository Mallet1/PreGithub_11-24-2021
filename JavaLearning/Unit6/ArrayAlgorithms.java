
public class ArrayAlgorithms
{
    public static void main(String args[])
    {
        int arr1[]={9, 2, 6, 1, 8, 3, 10};
        System.out.println("Has even? " + findEven(arr1));
        int arr2[]={2, 2, 2, 1, 8, 3, 3, 10, 10};
        System.out.println("Doubles: " + countDoubles(arr2));
        
        int arr3[]={1,2,3,4,5,6,7,8,9};
        rotate(arr3,4);
        print(arr3);
        rotate(arr3,-2);
        print(arr3);

    }
    /**
     * Algorithm: Determine if at least one element has a particular property. 
     * 
     * findEven()--return true if int array parameter has an even element, false otherwise
     * 
     * I used an indexed for loop. See if you can rewrite it using a for-each loop.
     * 
     */
    public static boolean findEven(int[] a)
    {
        for(int i=0; i<a.length; i++)
        {
            if(a[i]%2==0)
                return true;          
        }
        return false;
    }

    /**
     * Algorithm: Access all consecutive pairs of elements. 
     * 
     * countDoubles()--return the number of times two consecutive elements of an 
     * int array parameter are the same
     * (Note: {1,1,1} would return 2 because there are 2 consecutive pairs.)
     * 
     * Can you use a for-each loop for this?
     */
    public static int countDoubles(int a[])
    {
        int count=0;
        for(int i=0; i<a.length-1; i++) //do a.length-1 to avoid ArrayIndexOutOfBounds exception
        {
            if(a[i]==a[i+1])
            {
                count++;
            }
        }
        return count;
    }

    /**
     * Algorithm: Shift or rotate elements left or right (and wrap around). 
     * 
     * shiftLeft()--takes an int array and shifts every element one to the left
     * The first element will become the last element.
     * 
     * shiftRight()--takes an int array and shifts every element one to the right
     * The last element will become the first element.
     */

    public static void shiftLeft(int a[])
    {
        int temp=a[0]; //temporarily store first element
        for(int i=0; i<a.length-1; i++) //don't include a.length-1 to avoid out of bounds error
        {
            a[i]=a[i+1];           
        }
        a[a.length-1]=temp; //store first element in last element

    }

    public static void shiftRight(int a[])
    {
        int temp=a[a.length-1]; //temporarily store last element
        for(int i=a.length-1; i>0; i--) //need to go backwards, don't include 0 to avoid out of bounds error
        {
            a[i]=a[i-1];           
        }
        a[0]=temp; //store last element in first element
    }  

    /**
     * Test previous two methods
     * rotate()-has an int array parameter and int parameter, x.
     * If x>0, rotate x units right
     * If x<0, rotate -x units left
     * If x=0, do nothing
     */
    public static void rotate(int a[], int x)
    {
        if(x>0)
        {
            for(int i=0; i<x; i++)
                shiftRight(a);
        }
        if(x<0)
        {
            for(int i=0; i<Math.abs(x); i++) //Math.abs() so we don't need to work with a negative num
                shiftLeft(a);
        }
    }

    public static void print(int[] a)
    {
        for(int val: a)
            System.out.print(val + " ");
        System.out.println();
    }
}

