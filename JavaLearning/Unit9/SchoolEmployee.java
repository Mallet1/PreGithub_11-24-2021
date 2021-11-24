
/**
 * Child class of Occupation (extends Occupation)
 * Shows inheritance
 * A SchoolEmployee "IS-A" Occupation
 * A SchoolEmployee "IS-A" Object
 * All public methods/fields from the parent class are inherited.
 * Constructors are not inherited!
 * If no constructors are defined, then a default, no-args contructor will be automatically defined
 * which sets all fields from the child class to default values and calls the default constructor
 * from the parent class (if one exists).
 * (Defaults: ints/doubles=0, booleans=false, objects (including arrays and Strings)=null)
 */
public class SchoolEmployee extends Occupation //you can only extend one class
{
    private String schoolName; //name of employee's school
    private boolean publicSchool; //true if employee works at a public school
    
    public SchoolEmployee()
    {
        /**
         * super calls a method from the parent class
         * it must come first if you use it in the constructor
         */
        super(20000,false,40,"Frank"); //calls constructor with parameters from Occupation
        //If you don't use super to call a constructor from the parent class, the default constructor from the parent class
        //will be called automatically (if one exists). If no default constructor exists, there will be a compile error
        schoolName="St. Louis Public School";
        publicSchool=true;
    }
    public SchoolEmployee(double s, boolean d, int h, String n, String school, boolean p)
    {
        super(s,d,h,n);
        schoolName=school;
        publicSchool=p;
    }
    //accessors/getters
    public String getSchool()
    {
        return schoolName;
    }
    public boolean getPublic()
    {
        return publicSchool;
    }
    //modifiers/setters
    public void setSchool(String school)
    {
        schoolName=school;
    }
    public void setPublic(boolean p)
    {
        publicSchool=p;
    }
    /**
     * winsAward(String award)--prints out award that employee won.
     */
    public void winsAward(String award)
    {
        System.out.println(this.getName() + " has won the following award: " + award + ".");       
    }
    
    /**
     * Inherited methods: toString(), philosophy(), aspirations()
     * The method headers must match the parent class!
     */
    @Override //optional--checks to make sure your method header matches the parent class
    public String toString()
    {
        String p="no";
        if(publicSchool)
            p="yes";
        //super.toString will call toString from Occupation
        return super.toString() + "School Name: " + schoolName + "\nPublic School: "+p+"\n";
    }
    @Override
    public String philosophy()
    {
        return "A child's education influences them for the rest of their lives.";
    }
    @Override
    public String aspirations()
    {
        return "I want to save the world one child at a time.";
    }
    
}
