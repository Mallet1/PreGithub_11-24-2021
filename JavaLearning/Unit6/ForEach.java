
public class ForEach
{
    public static void main(String args[])
    {
        int[] arr={2, 3, 12, 7, 8, 9 , 2, 2, 11, 7};
        System.out.println(findAverage(arr));
        System.out.println(findMax(arr));
        System.out.println(findMode(arr));
    }

    /**
     * findAverage--takes an int array and returns the average 
     * (could be a decimal)
     * precondition -- a.length > 0
     */
    public static double findAverage(int a[])
    {
        //Finding the sum with an indexed for loop
        int sum=0; //you need to initialize to 0!!!
        for(int i=0; i<a.length; i++)
        {
            sum+=a[i];
        }

        /**
         * Enhanced for loop (for-each loop)-->i is each value in the array, not the index
         * Example: a={4,2,7,8} Regular for loop: i=0,1,2,3
         * For-each loop: i=4,2,7,8
         * You cannot change an array with a for-each loop!!!
         */
        sum = 0;
        for(int i : a) //first parameter must be of the same type as the array
        //second parameter is the name of the array
        {
            sum+=i;
        }
        return (double)sum/a.length;
    }

    //findMax--returns the maximum value in an int array
    //precondition -- arr.length>0
    public static int findMax(int arr[])
    {
        //Regular for loop approach:
        int max=arr[0]; //always set max/min to first element in the array
        for(int i=0; i<arr.length; i++) //could start at 1
        {
            if(arr[i]>max) //if finding min, this is the only part you would need to change (<)
                max=arr[i];
        }
        
        //For-each loop:
        max=arr[0];
        for(int val : arr)
        {
            if(val>max)
                max=val;
        }
        return max;        
    }
    //findMode-returns the mode of an int array (the value that occurs the most in the array)
    //precondition -- arr.length>0 and arr contains only one mode
    public static int findMode(int arr[])
    {
        //Regular for loop approach:
        int maxCount=0;
        int mode=0;
        for(int i=0; i<arr.length; i++)
        {
            int count=0;
            for(int j=0; j<arr.length; j++)
            {
                if(arr[i]==arr[j])
                {
                    count++;
                }
            }
            if(count>maxCount)
            {
                maxCount=count;
                mode=arr[i];
            }
        }
        
        //For-each loop:
        maxCount=0;
        mode=0;
        for(int val1 : arr)
        {
            int count=0;
            for(int val2 : arr)
            {
                if(val1==val2)
                {
                    count++;
                }
            }
            if(count>maxCount)
            {
                maxCount=count;
                mode=val1;
            }
        }
        return mode;       
    }
}
