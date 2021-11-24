
/**
 * Client/Driver class--Uses the classes we made, main method
 * DO NOT USE EXTENDS
 * A Workforce "HAS-A" Occupation, Programmer, SchoolEmployee, Teacher, Principal because it uses those classes.
 */
public class Workforce
{
    public static void main(String args[])
    {
        Occupation employee=new Principal(99000,75,"Richard","Lafayette",true, 
        new String[]{"discipline","supervision","staff development"},true);
        System.out.println(employee.toString()); //calls toString() from Principal because of polymorphism
        System.out.println(employee.getName() + " is the new principal at "
            + ((SchoolEmployee)employee).getSchool() + "."); //type cast
        //employee to SchoolEmployee because getSchool() is not defined in Occupation
        Occupation occ[]=new Occupation[7]; //array of 7 Occupations
        setOccs(occ);
        printOccs(occ);
        philosophize(occ);
        dream(occ);
        unique(occ);
        
        //check if occupations are equal
        if(occ[0].equals(occ[5]))
            System.out.println(occ[0].getName() + " has the same salary and hours worked as " + occ[5].getName() + "!");
        if(occ[1].equals(occ[4]))
            System.out.println(occ[1].getName() + " has the same salary and hours worked as " + occ[4].getName() + "!");

    }

    public static void setOccs(Occupation arr[])
    {
        arr[0]=new Principal();
        arr[1]=new Teacher();
        arr[2]=new Programmer();
        arr[3]=new SchoolEmployee(5000,false,10,"Bob","Eureka",false);
        arr[4]=new Teacher(70000,35,"Seth","Marquette",true,
            "Computer Science",true);
        arr[5]=new Programmer(150000,true,80,"Kevin",new String[]{"C++","Java","C","Python"},true);
        arr[6]=new Occupation();

    }

    public static void printOccs(Occupation arr[])
    {
        /**
         * Polymorphism--Java automatically knows which method of a specific
         * class to call, even if it is "disguised" as a more generic class
         * Every object in arr is an Occupation reference, but the correct toString() is called for each object
         * at run-time
         * (Teacher objects call the Teacher toString(), Programmer objects call the Programmer toString())
         * This only works when the method is defined in the parent class (Occupation in this case).
         */
        for(int i=0; i<arr.length; i++)
        {
            System.out.println(arr[i]); //same as arr[i].toString()
        }
        System.out.println("\n");
    }
    /**
     * Another polymorphism example: correct philosophy method is called for each object
     */
    public static void philosophize(Occupation arr[])
    {
        for(int i=0; i<arr.length; i++)
        {
            System.out.println(arr[i].getName() + "'s philosophy: "
                + arr[i].philosophy());
        }
        System.out.println("\n");
    }
     /**
     * Another polymorphism example: correct aspirations method is called for each object
     */
    public static void dream(Occupation arr[])
    {
        for(int i=0; i<arr.length; i++)
        {
            System.out.println(arr[i].getName() + "'s dream: "
                + arr[i].aspirations());
        }
        System.out.println("\n");
    }
    
    /**
     * unique() is going to call methods that are unique to the different types of occupations.
     * instanceOf will determine if the occupations are of a certain type.
     * You CANNOT use polymorphism here because these methods were not defined in the parent class.
     * You must type cast each object or the program will not compile.
     */
    public static void unique(Occupation arr[])
    {
        for(int i=0; i<arr.length; i++)
        {
            if(arr[i] instanceof SchoolEmployee)
                ((SchoolEmployee)arr[i]).winsAward("Rose Award");
            if(arr[i] instanceof Programmer)
            {
                ((Programmer)arr[i]).learnsLanguage("C#");
                System.out.println(arr[i].getName() + ": languages learned: " + ((Programmer)arr[i]).getLanguages() + "\n");
            }
            if(arr[i] instanceof Teacher)
                ((Teacher)arr[i]).getFired();
            if(arr[i] instanceof Principal)
                ((Principal)arr[i]).disciplineStudent("Josh");
        }

    }

}
