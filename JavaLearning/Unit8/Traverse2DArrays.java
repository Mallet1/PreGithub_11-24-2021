
public class Traverse2DArrays
{
    public static void main(String args[])
    {
        int arr[][]={
                {3, 7, 1, 8}, //arr2[0] //each row is a 1D array 
                {2, 9, -1, 0}, //arr2[1]
                {5, -3, 10, 12} //arr2[2]
            }; //3 rows and 4 columns
        
        print(arr);
            
        //print the sums of each row
        for(int i=0; i<arr.length; i++)
        {
            int rowSum=sumRow(arr,i);
            System.out.println("Sum of row with index of " + i + ": " + rowSum +"\n");            
        }
        //print the sums of each column
        for(int i=0; i<arr[0].length; i++)
        {
            int colSum=sumCol(arr,i);
            System.out.println("Sum of column with index of " + i + ": " + colSum +"\n");            
        }

        int countOver3=countOver(arr,3);
        System.out.println("The number of elements over 3 is " + countOver3 + ".\n");
        
        int[][] arrEvens = changeEvens(arr); //make a new array to hold changeEvens result
        print(arrEvens);
        print(arr); //make sure arr didn't change
       

    }

    //print 2D int array using for-each loop
    public static void print(int[][] arr)
    {
        for(int[] row : arr) //each row in arr is actually a 1D array
        {
            for(int col : row)//each column is an element of row[]
            {
                System.out.print(col + " ");
            }
            System.out.println(); //do a new line after each row
        }
        System.out.println(); //I added a new line after the array to make it look nicer
    }

    
    /**
     * returns sum of elements in row number rowNum
     * Precondition: 0<rowNum<arr.length
     *              arr contains at least one row and one column
     */
    public static int sumRow(int[][] arr, int rowNum)
    {
        int sum=0;
        for(int col=0; col<arr[0].length; col++) //loop through columns
        {
            sum+=arr[rowNum][col]; //row is always rowNum
        }
        return sum;
    }
    
     /**
     * returns sum of elements in column number colNum
     * Precondition: 0<colNum<arr[0].length
     *              arr contains at least one row and one column
     */
    public static int sumCol(int[][] arr, int colNum)
    {
        int sum=0;
        for(int row=0; row<arr.length; row++) //loop through rows
        {
            sum+=arr[row][colNum]; //column is always colNum
        }
        return sum;
    }
    
        
     /**
     * returns number of elements in arr that are greater than num using a for-each loop
     * Precondition: arr contains at least one row and one column
     */
    public static int countOver(int[][] arr, int num)
    {
        int count=0;
        for(int[] row : arr) 
        {
            for(int col : row)
            {
                if(col>num)
                    count++;
            }            
        }
        return count;
    }
     /**
     * returns a new 2D array that is a copy of arr except that all even values have been increased by 2
     * Precondition: arr contains at least one row and one column
     * Postcondion: arr should not be modified
     */
    public static int[][] changeEvens(int[][] arr)
    {
        int[][] arr2 = new int[arr.length][arr[0].length]; //make a new 2D array with the same rows/cols as arr
        //We cannot use a for-each here because we are modifying values
        for(int r=0; r<arr.length; r++) 
        {
            for(int c=0; c<arr[0].length; c++)
            {
                if(arr[r][c]%2!=0)
                    arr2[r][c]=arr[r][c]; //if original value is odd, just copy it
                else
                    arr2[r][c]=arr[r][c] + 2; //if original value is even, add 2 to original value and store in arr2
            }            
        }
        return arr2; //return new array
    }
}
