public class Fraction
{

    //----------------------FIELDS-----------------------------------
    //private fields for numerator and denominator-->Most fields are private!
    
    private int num;
    private int denom;

    //----------------------CONSTRUCTORS-----------------------------

    //Constructors - THEY INITIALIZE FIELDS
    /**if no constructors are written, a default is provided that initializes all fields to 0, booleans to false,  
     * object to null.  
     * This is not always good - in this instance, it would create a fraction where both numerator and denominator are zero! 
     * That fraction is undefined!  So providing your own default is sometimes a good idea.  
     * If you provide at least one constructor of your own, the default is not provided)*/

    //default constructor - creates default fraction 0/1
    public Fraction()
    {
        num=0;
        denom=1;

    }

    //constructor for a fraction that can be expressed as an integer 
    //- creates fraction n/1
    public Fraction(int n)
    {
        num=n;
        denom=1;
    }

    //constructor for any fraction with numerator n and denominator d 
    //- creates fraction n/d
    /*Precondition: d cannot = 0 */
    public Fraction(int n, int d)
    {
        if(d==0)
        {
            System.err.println("The denominator cannot be 0.");
            num=0;
            denom=1;          
        }
        else
        {
            num=n;
            denom=d;
            reduce();           
        }

    }

    //copy constructor - used to make a new Fraction object that is a copy of another
    public Fraction(Fraction f)
    {
        num=f.num; //sets numerator to the numerator of f
        denom=f.denom;        
    }

    //---------------------METHODS-------------------------------

    /**
     * Accessors (Getters)
     * give access to the fields
     */
    public int getNum()
    {
        return num;

    }

    public int getDenom()
    {
        return denom;
    }

    /**
     * Modifiers/Mutators (Setters)
     * modify a field
     */
    public void setNum(int n)
    {
        num=n;
        reduce();
    }

    public void setDenom(int d)
    {
        if(d==0)
        {
            System.err.println("The denominator cannot be 0.");
            num=0;
            denom=1;          
        }
        else
        {
            denom=d;
            reduce();           
        }
    }

    /**Public methods 
     * 
     * used by objects of the class that exist anywhere
     */
     
    
    /**method: getValue
    Precondition: accessed by a particular instance of the Fraction class
    Postcondition: returns the decimal value of the fraction as a double
     */
    public double getValue()
    {
        return (double)num/denom;

    }

    /**method: toString (from Object class--inherited by all classes)
    Precondition: accessed by a particular instance of the Fraction class
    Postcondition: returns the fraction as a string for output
     */
    public String toString()
    {
        return num + "/" + denom;

    }
    //**private method(can only be used within the class definition 
    //(this page!)***
    
        /**method: gcf  - This is a private "helper" method. Its only purpose is to "help" us reduce the Fraction.
     * Since we only need it inside of the class, we will make it private.

     * Precondition: two integer arguments passed in, x and y.  x>=0, y>0
     * Postcondition: returns the greatest common factor 
     * of two positive integers
     */
    private int gcf(int x, int y)
    {
        if(x<0 || y<=0)
        {
            System.err.println("gcf precondition failed.");
            return 1;
        }
        /**
         * start at either value (x or y)
         * count down to 1
         * if both x and y are divisible by any number in the countdown
         * return that number
         */
        for(int i=x; i>=1; i--)
        {
            if(x%i==0 && y%i==0)
            {
                return i;
            }     
        }
        return 1;
    }
    
    /**method: reduce--Fractions will automatically be reduced when cosntructed, so we don't need to provide access outside
     * of this class. Therefore, we will make it private.
     * Precondition: accessed by a particular method of the Fraction class,from within the class
     * Postcondition: converts the fraction to lowest terms.
     */
    private void reduce()
    {
        if(num==0)
        {
            denom=1;
            return; //stops the method (void, so just return)
        }
        if(denom<0) //if denom is negative, switch signs
        {
            num=-num;
            denom=-denom;
        }
        int g=gcf(Math.abs(num),denom);
        num/=g;
        denom/=g;        
    }
    
    

}