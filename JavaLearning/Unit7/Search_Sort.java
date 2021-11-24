
/**
 * Shows an example of Selection Sort, Insertion Sort, and Sequential/Linear Search
 */
import java.util.ArrayList;
public class Search_Sort
{
    public static void main(String args[])
    {
        int arr1[]={4,5,0,2,6,3,10,9,1,2};
        int arr2[]={3,5,1,0,-2,7,35,9};
        int position=search(arr2,7);
        if(position>=0)
            System.out.println("7 found at position " + position);
        else
            System.out.println("7 is not in the list!");
        
        selection(arr1);
        print(arr1);
        insertion(arr2);
        print(arr2);
        
        ArrayList<Integer> aList=new ArrayList<Integer>();
        aList.add(5);
        aList.add(1);
        aList.add(3);
        aList.add(10);
        aList.add(7);
        aList.add(2);
        selection(aList);
        System.out.println(aList);
        
    }
    public static void print(int[] a)
    {
        for(int i=0; i<a.length; i++)
        {
            System.out.print(a[i] + " ");
        }
        System.out.println();       
    }
     /**
     * Linear search: return index of num in a, -1 if not found.
     * Best Case: num is at the beginning of a
     * Worst Case: num is at the end of a or not in a
     * Average Case: a.length/2
     */
    public static int search(int[] a, int num) 
    {
       for(int i=0; i<a.length; i++)
       {
           if(a[i]==num)
           {
                return i;
           }
       }      
       return -1;
    }
    /**
     * Selection sort
     * The number of comparisons is ALWAYS n(n-1)/2.
     */
    public static void selection(int[] a)
    {
         for(int n=0; n<a.length-1; n++)
         {
              int min=n;
              for(int i=n+1; i<a.length; i++)
              {
                  if(a[i]<a[min])
                  {
                      min=i;                     
                  }     
              }
              int temp=a[min]; 
              a[min]=a[n];
              a[n]=temp;      
         }
    }
    /**
     * Insertion sort:
     * Best Case: The list is already in order.
     * Worst Case: The list is in reverse order.
     */
    public static void insertion(int[] a)
    {
        for(int n=1; n<a.length; n++)
        {
            int temp=a[n];
            int i=n;
            while(i>0 && temp<a[i-1])
            {
                a[i]=a[i-1];
                i--;
            }
            a[i]=temp; 
        }
    }

    /**
     * Overloaded selection sort for ArrayList of Integers
     * We need to use ArrayList methods: size(), get(), set()
     */
        public static void selection(ArrayList<Integer> a)
    {
         for(int n=0; n<a.size()-1; n++) //replace length with size()
         {
              int min=n;
              for(int i=n+1; i<a.size(); i++) //replace length with size()
              {
                  if(a.get(i)<a.get(min))  //replace [] with get()
                  {
                      min=i;                     
                  }     
              }
              int temp=a.get(min); //replace [] with get(), temp holds the minimum value
              a.set(min,a.get(n)); //set the value at min to the element at n
              a.set(n,temp);     //set the value at n to temp
         }
    }
}
