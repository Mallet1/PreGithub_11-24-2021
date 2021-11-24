import java.util.*; //for ArrayList and Scanner
import java.text.*; //for NumberFormat
public class Food
{

    private String myName; //name of Food
    private int myCals; //calories in Food
    private double cost; //cost of Food
    private static Scanner s=new Scanner(System.in);
    private static NumberFormat curr=NumberFormat.getCurrencyInstance();

    /**
     * default constructor that creates a Food item with fields set to default values
     * @param none
     **/
    public Food()
    {
        myName="";
        myCals=0;
        cost=0;
    }  

    /**
     * constructor that creates a Food item with fields set to the specified parameters
     * @param n     String for the food name
     * @param c     int for the number of calories per serving
     * @param cos   double for the cost of the Food
     **/
    public Food(String n,int c, double cos)
    {
        myName=n;
        myCals=c;
        cost=cos;
    } 

    /**
     * accessor method for the food name
     * @param      none
     * @return    returns a String that is the food name
     **/
    public String getName()
    {
        return myName;
    }

    /**
     * accessor method for the calories
     * @param      none
     * @return    returns an int number of calories per serving
     */
    public int getCals()
    {
        return myCals;
    }

    /**
     * accessor method for the cost
     * @param      none
     * @return    returns a double for cost
     */
    public double getCost()
    {
        return cost;        
    }

    /**
     * modifier method for the name of the food
     * @param      String n is what the name will become
     * @return    returns nothing
     */
    public void setName(String n)
    {
        myName=n;
    }

    /**
     * modifier method for the calories
     * @param     int c is what the calories will change to
     * @return    returns nothing
     */
    public void setCals(int c)
    {
        myCals=c;
    }

    /**
     * modifier method for the cost
     * @param     double c is what the cost will change to
     * @return    returns nothing
     */
    public void setCost(double c)
    {
        cost=c;        
    }

    /**
     * toString()--inherited from Object
     * @param     none
     * @return    a String is returned with all of the information for a Food
     */
    public String toString()
    {
        return "Name: "+myName+ "   Calories Per Serving: "+myCals +"   Cost: " + curr.format(cost)
        + "\n";
    }

    /**
     * getFoodInfo()--asks the user for name, calories, and cost of a Food and sets each field to these values
     * using modifiers
     * @param     none
     * @return    none
     */
    public void getFoodInfo()
    {
        System.out.print("Enter name of food: ");
        setName(s.nextLine()); //OR name=s.nextLine();
        System.out.print("Enter calories per serving: ");
        setCals(s.nextInt());
        System.out.print("Enter the cost: ");
        setCost(s.nextDouble());
        System.out.println();
        s.nextLine();  //clear out rest of the line after the number                 
    }
}


