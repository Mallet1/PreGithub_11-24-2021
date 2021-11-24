
/**
 * ArrayLists are resizable lists.
 * They can only hold OBJECTS, not primitive types
 * Wrapper classes--classes that mimic primitive data types
 * Integer, Double, Character, Boolean
 * Remember, Strings are objects
 */
import java.util.ArrayList; //Must import this

public class ArrayListMethods
{
    public static void main(String args[])
    {
        
        
        ArrayList<String> words=new ArrayList<String>(); //size=0  capacity=10
        ArrayList<Double> decis=new ArrayList<Double>(30); //size=0  capacity=30
        ArrayList<Integer> ints=new ArrayList<Integer>();
        
        
        //add to words
        words.add("I"); //index=0
        words.add("want");//1
        words.add("winter");//2
        words.add("over");//3
        words.add("right");//4
        words.add("now");//5
        
        
        System.out.println(words); //actually prints the ArrayList!
        System.out.println("First element in the list: " + words.get(0));
        
        words.set(2,"boredom");//replaces "winter" with boredom
        words.add(1,"really"); //inserts "really" before "want", changes indices of all elements after it
        words.add(words.size(),"grrrr"); //adds "grrr" to the end
        words.remove(5); //removes "right", changes indices of all elements after it
        
        System.out.println(words + "\n");
        
        decis.add(new Double(3.4)); //0
        decis.add(2.6); //1 //Java "auto-boxes" the value to a Double object, no need to use constructor
        decis.add(1.5); //2
        decis.add(9.2); //3
        decis.add(1.0); //4 //cannot do decis.add(1)--thinks it's an Integer
        decis.add(6.3); //5
       
        
        System.out.println(decis);
        Double dec1=decis.get(decis.size()-1); //sets dec1 to last element 
        double dec2=decis.get(0); //sets dec2 to first element, auto-unboxes (converts Double to double)
        double dec3=decis.get(3).doubleValue(); //sets dec3 to the element at position 3, manually converts to double
        System.out.println(dec1 + " " + dec2 + " " + dec3 + "\n");
        
        
        
        ints.add(5); //0
        ints.add(9); //1
        ints.add(2); //2
        ints.add(10); //3
        ints.add(4); //4
        ints.add(-3); //5
        
        System.out.println(ints);
        System.out.println("Replaced element: " + ints.set(3,7)); //prints replaced element (10) and sets it to 7
        int in1=ints.set(0,12);  //replaces first element with 12 and sets in1 to replaced element (5) 
        System.out.println("Replaced element: " + in1);
        System.out.println(ints+"\n");
        
        System.out.println("Removed element: " + ints.remove(1)); //removes element at position 1 (9) and prints it
        //all elements after position 1 shift
        Integer in2=ints.remove(2);  //removes element at position 2 (7) and stores it in in2
        System.out.println("Removed element: " + in2);
        System.out.println(ints);
    }
}