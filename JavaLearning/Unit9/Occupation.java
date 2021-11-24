/**
 * Parent class (superclass)--only extends Object (from lang package) class, 
 * which is the default parent class
 * An Occupation "IS-A" Object
 * An Occupation "HAS-A" String because it uses a String object.
 * An "IS-A" relationship shows inheritance.
 * A "HAS-A" relationship shows association.
 * If no constructors are defined, then a default, no-args contructor will be automatically defined
 * which sets all fields to default values.
 * (Defaults: ints/doubles=0, booleans=false, objects (including arrays and Strings)=null)
 *
 * Factoring out code--
 * Process of putting common methods/fields in a parent class
 */
import java.text.NumberFormat;

public class Occupation //extends Object
{
    private double salary;
    private boolean degreeRequired;
    private int hoursPerWeek;
    private String name;
    
    //default constructor
    public Occupation()
    {
        salary=0;
        degreeRequired=false;
        hoursPerWeek=0;
        name="Jack";
    }
    
    public Occupation(double s, boolean d, int h, String n)
    {
        this.salary=s;
        degreeRequired=d;
        hoursPerWeek=h;
        name=n;
    }
    //accessors/getters
    public double getSalary()
    {
        return salary;        
    }
    public boolean getDegreeReq()
    {
        return degreeRequired;
    }
    public int getHours()
    {
       return hoursPerWeek; 
    }
    public String getName()
    {
        return name;
    }
    
    //modifiers/setters
    public void setSalary(double s)
    {
        salary=s;
    }
    public void setHours(int h)
    {
        hoursPerWeek=h;
    }
       
    /**
     * toString() is inherited from the Object class (from lang package).
     * You must keep the same method header as the Object class.
     * When you rewrite a method from the parent class, 
     * this is called overriding the method.
     * If you don't override toString(), it will return the memory address.
     * getClass()--also from the Object class, returns the name of the class (not on AP exam)
     */
    @Override //optional--checks to make sure your method header matches the parent class
    public String toString()
    {
        String deg="no";
        if(degreeRequired)
            deg="yes";
        NumberFormat f = NumberFormat.getCurrencyInstance();
        return "\nName: " + name + "\nJob Type: " + getClass() + 
        "\nSalary: " + f.format(salary) + "\nHours Per Week: " + hoursPerWeek
        + "\nDegree Required: " + deg + "\n";
    }
    
    /**
     * equals() method is inherited from the Object class, 
     * must keep the same method header
     * We will consider two occupations equal if they have the 
     * same salary and same hours per week.
     */
    @Override //optional--checks to make sure your method header matches the parent class
    public boolean equals(Object other)
    {
        if(other!=null && other instanceof Occupation) //instanceof checks if the variable 
        //is a certain class type
        {
            return this.salary==((Occupation)other).salary && 
            this.hoursPerWeek==((Occupation)other).hoursPerWeek;
        }
        else
        {
            System.out.println("You can only compare two occupations.");
            return false;
        }       
    }
    
    //Other methods
    
    /**
     * philosophy--returns a String with the worker's philosophy about work
     */
    public String philosophy()
    {
        return "I hate work.";
        
    }
    /**
     * aspirations--returns a String with the worker's aspirations for the future
     */
    public String aspirations()
    {
        return "I want to live in my parents' basement forever.";       
    }
    
    
    
    
    
    
    
}
