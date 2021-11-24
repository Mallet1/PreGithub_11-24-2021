import java.lang.*;
import java.util.*;
import java.text.*;
public class QuizGrader
{
    public static void fill(int[] arr)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter your answers to the quiz: ");
        for(int i=0;i<arr.length;i++)
        {
            arr[i]=s.nextInt();
        }
    }

    public static void reverse(int[] arr)
    {
        int a=arr.length;
        int[] newArr=new int[arr.length];
        for(int i=0;i<arr.length;i++)
        {
            newArr[a-1]=arr[i];
            a--;
        }
        for(int i=0;i<arr.length;i++)
        {
            arr[i]=newArr[i];
            //System.out.println(arr[i]);
        }
    }

    public static void print(int[] arr)
    {
        for(int each:arr)
            System.out.print(each+" ");
        System.out.println();
    }

    public static void print(boolean[] arr)
    {
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]==true)
                System.out.print("O ");
            if(arr[i]==false)
                System.out.print("X ");
        }
        System.out.println();
    }

    public static boolean duplicates(int[] arr)
    {
        for(int i=0;i<arr.length;i++)
        {
            for(int k=0;k<arr.length;k++)
            {
                if(arr[i]==arr[k]&&i!=k)
                    return true;
            }
        }
        return false;
    }

    public static boolean isValid(int[] arr)
    {
        if(duplicates(arr)==true)
            return false;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]<1||arr[i]>arr.length)
                return false;
        }
        return true;
    }

    public static boolean[] grade(int[] arr,int[] arr1)
    {
        boolean[] newArr = new boolean[arr.length];
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]==arr1[i])
            {
                newArr[i]=true;
            }
        }
        return newArr;
    }

    public static int score(boolean[] arr)
    {
        int count=0;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]==true)
                count++;
        }
        return count;
    }

    public static void main(String args[])
    {
        int[] key = {7,8,1,4,5,6,3,2};
        int[] answers = new int[key.length];
        int rand=(int)(Math.random()*2)+1;

        if(rand==2)
        {
            reverse(key);
        }

        fill(answers);
        System.out.println("Answer key: ");
        print(key);
        System.out.println("Your answers: ");
        print(answers);

        if(isValid(answers))
        {
            boolean[] grade = new boolean[key.length];
            grade=grade(answers,key);
            print(grade);
            int score=score(grade);
            if(rand==1)
                System.out.println("You recieved test #1");
            else
                System.out.println("You recieved test #2");
            System.out.println("Your score is "+score+" out of "+key.length+".");
        }
        else
            System.out.println("At least one of those answers is invalid. You must retake the test!");
    }
}