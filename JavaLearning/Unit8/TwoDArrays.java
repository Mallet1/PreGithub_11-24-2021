
public class TwoDArrays
{
    public static void main(String args[])
    {
        int arr1[][]=new int[5][3]; //5 rows and 3 columns of 0's
        int arr2[][]={
                {3, 7, 1, 8}, //arr2[0] //each row is a 1D array 
                {2, 9, -1, 0}, //arr2[1]
                {5, -3, 10, 12} //arr2[2]
            }; //3 rows and 4 columns
            
        print2D(arr1);
        print2D(arr2);
        
        arr1[3][2]=8; //sets 4th row, 3rd column to 8.
        print2D(arr1);
        
        print1D(arr2[0]); //prints first row of arr2, calls the print function for a 1D array
        System.out.println();
        
        print2Dv2(arr2);

    }

    //print 2D int array
    public static void print2D(int[][] arr)
    {
        for(int i=0; i<arr.length; i++) //loop through rows
        {
            for(int j=0; j<arr[0].length; j++)//loop through cols
            {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println(); //do a new line after each row
        }
        System.out.println(); //I added a new line after the array to make it look nicer
    }
    
    //print 1D int array
    public static void print1D(int[] arr)
    {
        for(int i=0; i<arr.length; i++) //loop through rows
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println(); //I added a new line after the array to make it look nicer
    }
    
    //alternate version of printing 2D array
    public static void print2Dv2(int[][] arr)
    {
        for(int i=0; i<arr.length; i++) //loop through rows
        {
            print1D(arr[i]); //prints each row of arr using 1D array print
        }
        System.out.println(); 
    }
}
