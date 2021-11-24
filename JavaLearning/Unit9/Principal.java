
/**
 * Child class of SchoolEmployee (extends SchoolEmployee)
 * Shows inheritance
 * A Principal "IS-A" SchoolEmployee
 * A Principal "IS-A" Occupation
 * A Principal "IS-A" Object
 * All public methods/fields from the parent class are inherited.
 * Constructors are not inherited!
 * If no constructors are defined, then a default, no-args contructor will be automatically defined
 * which sets all fields from the child class to default values and calls the default constructor
 * from the parent class (if one exists).
 * (Defaults: ints/doubles=0, booleans=false, objects (including arrays and Strings)=null)
 */
public class Principal extends SchoolEmployee //you can only extend one class
{
    private String[] duties; //principal's duties
    private boolean isGradeLevel; //true if principal is a grade level principal
    
    public Principal()
    {
        /**
         * super calls a method from the parent class
         * it must come first if you use it in the constructor
         */
        super(150000,true,80,"Steve","St. Louis Public School",true); //calls constructor with parameters from SchoolEmployee
        //If you don't use super to call a constructor from the parent class, the default constructor
        //from the parent class will be called automatically.
        duties=new String[]{"discipline","supervision","budget"};
        isGradeLevel=false;
    }
    public Principal(double s, int h, String n, String school, boolean p, String[] dut, boolean g)
    {
        super(s,true,h,n,school,p); //I plugged in true for degreeRequired because all principals
        //need a degree
        duties=dut;
        isGradeLevel=g;
    }
    //accessors/getters
    public String[] getDuties()
    {
        return duties;
    }
    public boolean getGradeLevel()
    {
        return isGradeLevel;
    }
    //modifiers/setters--NONE
        
    /**
     * disciplineStudent(String student)--prints out that the principal is 
     * disciplining student
     */
    public void disciplineStudent(String student)
    {
            System.out.println(this.getName() + " is disciplining " + student + ".");
    }
    
    /**
     * Inherited methods: toString(), philosophy(), aspirations()
     * The method headers must match the parent class!
     */
    @Override
    public String toString()
    {
        String g="no";
        if(isGradeLevel)
            g="yes";
        String dut="";
        for(int i=0; i<duties.length; i++)
            dut+=duties[i]+"\n";
        //super.toString will call toString from SchoolEmployee
        return super.toString() + "Grade Level: " + g + "\nDuties:\n"+dut+"\n";
        
    }
    @Override
    public String philosophy()
    {
        return "Education is important, so I want to be in charge.";
    }
    @Override
    public String aspirations()
    {
        return "I want to retire early and go on a lot of vacations.";
    }
    
}
