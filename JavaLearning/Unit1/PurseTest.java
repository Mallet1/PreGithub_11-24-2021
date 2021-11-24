
/**
 * Driver/Client class--uses the Purse class
 */
public class PurseTest
{
    public static void main(String args[])
    {
        Purse coach = new Purse();
        System.out.println(coach.toString());
        coach.addQuarters(4);
        coach.addDimes(10);
        coach.addNickels(5);
        coach.addPennies(3);
        System.out.println(coach); //toString() is the default-->
        //you don't need it
        coach.simplifyCoins();
        System.out.println(coach);
        
    }
}
