
/**
 * Child class of Occupation (extends Occupation)
 * Shows inheritance
 * A Programmer "IS-A" Occupation
 * A Programmer "IS-A" Object
 * All public methods/fields from the parent class are inherited.
 * Constructors are not inherited!
 * If no constructors are defined, then a default, no-args contructor will be automatically defined
 * which sets all fields from the child class to default values and calls the default constructor
 * from the parent class (if one exists).
 * (Defaults: ints/doubles=0, booleans=false, objects (including arrays and Strings)=null)
 */
import java.util.ArrayList;
public class Programmer extends Occupation //you can only extend one class
{
    private ArrayList<String> languages; //list of languages that the programmer knows
    private boolean isManager; //true if programmer manages a team
    
    public Programmer()
    {
        /**
         * super calls a method from the parent class.
         * It must come first if you use it in the constructor.
         * If you don't use super to call a constructor from the parent class, the default constructor
         * from the parent class will be called automatically.
         */
        super(80000,false,50,"Amanda"); //calls constructor with parameters
        //from Occupation
        languages=new ArrayList<String>();
        languages.add("BASIC");
        isManager=false;
        
    }
    public Programmer(double s, boolean d, int h, String n, String[] lang, boolean m)
    {
        super(s,d,h,n);
        languages=new ArrayList<String>();
        for(int i=0; i<lang.length; i++)
            languages.add(lang[i]);
        isManager=m;
    }
    //accessors/getters
    public boolean getManager()
    {
        return isManager;
    }
    public ArrayList<String> getLanguages()
    {
        return languages;
    }
    //modifiers/setters
    public void setManager(boolean m)
    {
        isManager=m;
    }
    /**
     * learnsLanguage(String lang)--adds lang to languages ArrayList
     * 
     */
    public void learnsLanguage(String lang)
    {
        languages.add(lang);       
    }
    
    /**
     * Inherited methods: toString(), philosophy(), 
     * aspirations()--override them
     * The method headers must match the parent class!
     */
    @Override
    public String toString()
    {
        String m= "no";
        if(isManager)
            m="yes";
        String lang="";
        for(int i=0; i<languages.size(); i++)
            lang+=languages.get(i)+"\n";
        //super.toString() will call toString() from Occupation
        return super.toString() + "Manager: " + m + "\nLanguages known:\n"
        + lang + "\n";
        
    }
    @Override
    public String philosophy()
    {
        return "Efficiency is everything.";
    }
    @Override
    public String aspirations()
    {
        return "I'm going to be a billionaire.";
    }
    
 
}
