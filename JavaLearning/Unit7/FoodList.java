import java.util.*;
public class FoodList
{
    private ArrayList<Food> f;
    private static Scanner s=new Scanner(System.in);

    public FoodList()
    {
        f=new ArrayList<Food>();
        System.out.println("How many foods would you like?");
        int foodNum=s.nextInt();
        for(int i=1;i<=foodNum;i++)
        {
            addItem();
        }
    }

    public ArrayList<Food> getFood()
    {
        return f;
    }

    public void addItem()
    {
        Food item = new Food();
        item.getFoodInfo();
        int calories = item.getCals();
        if(f.size()==0)
            f.add(item); 
        else if(calories>=f.get(f.size()-1).getCals()) //if str is greater than the last element
            f.add(item);
        else
        {
            for(int i=0; i<f.size(); i++)
            {
                if(calories<=f.get(i).getCals())
                {
                    f.add(i,item);
                    break;
                }
            }
        }
    }

    public String toString()
    {
        String str="";
        for(int i=0;i<f.size();i++)
        {
            str+=(i+1)+". "+f.get(i).toString()+"\n";
        }
        return str;
    }

    public void removeItems(ArrayList<Integer> nums)
    {
        for(int i=1;i<nums.size();i++)
        {
            int temp=nums.get(i);
            int possibleIndex=i;
            while(possibleIndex>0 && temp<nums.get(possibleIndex-1))
            {
                nums.set(possibleIndex,nums.get(possibleIndex-1));
                possibleIndex--;
            }
            nums.set(possibleIndex,temp);
        }
        
        for(int i=nums.size()-1;i>=0;i--)
        {
            //for(int k=f.size()-1;k>=0;k--)
            //{
                //if(k==nums.get(i))
            System.out.println(f.remove(nums.get(i).intValue()).getName()+" is removed");
            //}
        }
    }
    
    public double totalCost()
    {
        double sum=0;
        for(int i=0;i<f.size();i++)
        {
            sum+=f.get(i).getCost();
        }
        return sum;
    }
}

