import java.util.*; //for ArrayList and Scanner
import java.text.*; //for NumberFormat
public class GroceryStore
{
    private static Scanner s=new Scanner(System.in);
    private static NumberFormat curr=NumberFormat.getCurrencyInstance();
    public static void main(String args[])
    {

        FoodList f=new FoodList(); //a new empty FoodList
        int choice=0;
        while(choice!=4) //program continues until check out
        {  
            System.out.println("Please enter your choice: ");
            System.out.println("1. Add more items to your list.\n2. Remove items from your list.\n"
                + "3. Print your list.\n4. Check out\n\n");
            choice=s.nextInt();
            while(choice<1 || choice>4)
            {
                System.out.println("Error.  Try again.");  
                choice=s.nextInt();
            }
            if(choice==1)
            {
                addItems(f);
            }
            else if(choice==2)
            {
                removeItems(f); 
            }
            else if(choice==3)
            {
                printList(f);
            }
            else
            {
                checkOut(f);
            }
        }
    }

    public static void printList(FoodList f)
    {
        System.out.println("Your grocery list in order of healthiness:\n"+f.toString());
    }

    public static void removeItems(FoodList f)
    {
        ArrayList<Integer> removed = new ArrayList<Integer>();
        System.out.println("Which item(s) would you like to remove (1-"+f.getFood().size()+")? Type a 0 to quit");
        int num=1;
        while(true)
        {
            num=s.nextInt();
            if(num>0&&num<=f.getFood().size())
                removed.add(num-1);
            else if(num==0)
                break;
            else 
                System.out.println("Invalid number. Try again.");
        }
        f.removeItems(removed);
    }
    
    public static void addItems(FoodList f)
    {
        System.out.println("How many foods would you like to enter?");
        int foods=s.nextInt();
        
        for(int i=0;i<foods;i++)
            f.addItem();
    }

    public static void checkOut(FoodList f)
    {
        printList(f);
        System.out.println("Total cost $"+f.totalCost()+". Thanks for shopping with us!");
    }
}
