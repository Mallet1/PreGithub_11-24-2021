public class FractionTest
{
    public static void main(String args[])
    {

        //test constructors
        Fraction f1=new Fraction(); //default constructor 0/1
        Fraction f2=new Fraction(7); // 7/1
        Fraction f3=new Fraction(45,-75); // -3/5
       
        System.out.println("f1: " + f1.toString());
        System.out.println("f2: " + f2); //toString() is the default method in a print statement
        //--it will automatically be called
        System.out.println("f3: " + f3 + " = " + f3.getValue() + "\n\n\n"); //Test getValue()
        
        
     

        //Using the copy constructor
         Fraction f4=new Fraction(f3); // f4 is -3/5, it is a copy of f3, a NEW reference is made to a NEW Fraction with 
         //a value of -3/5 **This is called a deep copy**
         System.out.println("f4: " + f4);  
         f3.setNum(7); // f3 is 7/5, but f4 is still -3/5
         System.out.println("f3: " + f3);  
         System.out.println("f4: " + f4 + "\n\n");  
         
         f4=f2;  //f4 is 7/1, it is a NEW reference to the SAME Fraction as f2, f4 and f2 are "aliases" because they both
         //reference the same object. **This is called a shallow copy**
         System.out.println("f4: " + f4); 
         
         f2.setDenom(-4); //Both f2 and f4 are changed to -7/4!
         System.out.println("f2: " + f2); 
         System.out.println("f4: " + f4); 
         


      
        
       

      
    }



}