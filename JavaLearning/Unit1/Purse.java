
import java.text.*; //for NumberFormat

public class Purse
{
    //fields--property of a class
    //private--can only be used in the class they were defined in
    //public--can be used anywhere
    private int quarters;
    private int dimes;
    private int nickels;
    private int pennies;
    
    //will format with $ and two decimals
    private NumberFormat fmt=NumberFormat.getCurrencyInstance();
    
    //constants--usually in all caps and static
    //use final to denote a constant
    private static final double QVAL=.25;
    private static final double DVAL=.10;
    private static final double NVAL=.05;
    private static final double PVAL=.01;
    
    //Constructors
    /**
     * You can have as many constructors as you want as long as they
     * have different parameters.
     * If you have no constructors, a default no-args (no parameters)
     * constructor is automatically created that sets fields to default
     * values:
     * 
     * int or double: 0
     * boolean: false
     * objects: null
     */
    
    //default constructor--no parameters
    //Constructors have no return types!!!
    public Purse()
    {
        quarters=0;
        dimes=0;
        nickels=0;
        pennies=0;
        
    }
    
    //methods to add to our purse
    public void addQuarters(int count)
    {
        quarters+=count;
        
    }
    public void addDimes(int count)
    {
        dimes+=count;
        
    }
    public void addNickels(int count)
    {
        nickels+=count;
        
    }
    public void addPennies(int count)
    {
        pennies+=count;
        
    }
    
    public double getTotal()
    {
        double total=quarters*QVAL+dimes*DVAL+nickels*NVAL+pennies*PVAL;
        return total;       
    }
    
    /**
     * total is a LOCAL VARIABLE because it is declared inside of a method
     * The SCOPE of a variable is where the variable can be accessed.
     * The scope of a local variable is the method in which it is defined.
     * The scope of a private field (global variable)
     * is the class in which it is defined.
     * 
     * LOCAL VARIABLES HAVE NO DEFAULT VALUES
     * 
     */
    
    //change the number of coins so that the least number of coins is used
    public void simplifyCoins()
    {
        double total=getTotal();
        int cents=(int)(total*100+.5);
        quarters=cents/25;
        cents%=25; //cents=cents%25; cents left over after taking out quarters
        dimes=cents/10;
        cents%=10;
        nickels=cents/5;
        cents%=5;
        pennies=cents;
    }
    
    /**
     * toString() method
     * Every class has a toString() method--
     * It is from the Object class which every class inherits.
     * 
     * We are going to OVERRIDE (rewrite) the toString() method from Object.
     * The header of the method must be the same as Object.
     */
    public String toString()
    {
        return "***Purse Contents***\nQuarters: " + quarters
        + "\nDimes: " + dimes + "\nNickels: " + nickels + "\nPennies: "
        + pennies + "\nTotal: " + fmt.format(getTotal()) + "\n\n";
       
    }
}






