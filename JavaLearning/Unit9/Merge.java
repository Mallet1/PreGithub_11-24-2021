public class Merge
{
    public static void main(String[] args)
    {
        int[] arr1 = {9, 1, 3, 5, 4};

int[] temp = new int[arr1.length];

mergeSortHelper(arr1, 0, arr1.length - 1, temp);


    }

public static void mergeSortHelper(int[] arr, int from, int to, int[] temp)

{

if (from < to)

{

int middle = (from + to) / 2;

mergeSortHelper(arr, from, middle, temp);

mergeSortHelper(arr, middle + 1, to, temp);

merge(arr, from, middle, to);

for(int each : arr)
    System.out.print(each + " ");
System.out.println();

}

}

    public static void merge(int arr[], int l, int m, int r)
    {
        // Find sizes of two subarrays to be merged
        int n1 = m - l + 1;
        int n2 = r - m;
  
        /* Create temp arrays */
        int L[] = new int [n1];
        int R[] = new int [n2];
  
        /*Copy data to temp arrays*/
        for (int i=0; i<n1; ++i)
            L[i] = arr[l + i];
        for (int j=0; j<n2; ++j)
            R[j] = arr[m + 1+ j];
  
  
        /* Merge the temp arrays */
  
        // Initial indexes of first and second subarrays
        int i = 0, j = 0;
  
        // Initial index of merged subarry array
        int k = l;
        while (i < n1 && j < n2)
        {
            if (L[i] <= R[j])
            {
                arr[k] = L[i];
                i++;
            }
            else
            {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
  
        /* Copy remaining elements of L[] if any */
        while (i < n1)
        {
            arr[k] = L[i];
            i++;
            k++;
        }
  
        /* Copy remaining elements of R[] if any */
        while (j < n2)
        {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
}
