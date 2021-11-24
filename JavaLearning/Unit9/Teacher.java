
/**
 * Child class of SchoolEmployee (extends SchoolEmployee)
 * Shows inheritance
 * A Teacher "IS-A" SchoolEmployee
 * A Teacher "IS-A" Occupation
 * A Teacher "IS-A" Object
 * All public methods/fields from the parent class are inherited.
 * Constructors are not inherited!
 * If no constructors are defined, then a default, no-args contructor will be automatically defined
 * which sets all fields from the child class to default values and calls the default constructor
 * from the parent class (if one exists).
 * (Defaults: ints/doubles=0, booleans=false, objects (including arrays and Strings)=null)
 */
public class Teacher extends SchoolEmployee //you can only extend one class
{
    private String subject; //subject taught by teacher
    private boolean hasTenure; //true if teacher has tenure
    
    public Teacher()
    {
        /**
         * super calls a method from the parent class
         * it must come first if you use it in the constructor
         */
        //calls constructor from SchoolEmployee
        super(40000,true,35,"Carla","St. Louis Public School",true);
        subject="English";
        hasTenure=false;        
    }
    
    public Teacher(double s, int h, String n, String school, boolean p, String subj, boolean t)
    {
        super(s,true,h,n,school,p); //I plugged in true for degreeRequired
        //because all teachers need a degree
        subject=subj;
        hasTenure=t;
    }
    //accessors/getters
    public String getSubject()
    {
        return subject;
    }
    public boolean getTenure()
    {
        return hasTenure;
    }
    //modifiers/setters
    public void setTenure(boolean t)
    {
        hasTenure=t;
    }
    
    /**
     * getFired()--prints out that the teacher is fired if they 
     * don't have tenure.
     */
    public void getFired()
    {
        if(!hasTenure)
            System.out.println(this.getName() + " is fired.");
        else
            System.out.println(this.getName() + " cannot be fired.");
    }
    
    /**
     * Inherited methods: toString(), philosophy(), aspirations()
     * The method headers must match the parent class!
     */
    @Override
    public String toString()
    {
        String t="no";
        if(hasTenure)
            t="yes";
        //super.toString() will call toString() from SchoolEmployee
        return super.toString() + "Subject: " + subject + "\nTenure: "
        + t + "\n";
        
    }
    @Override
    public String philosophy()
    {
        return "To teach is to touch a life forever.";
    }
    @Override
    public String aspirations()
    {
        return "I want to retire early, but still get paid until I die.";
    }
    
}
