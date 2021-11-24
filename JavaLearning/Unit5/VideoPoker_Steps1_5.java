


import java.util.*;
public class VideoPoker_Steps1_5
{
    static Scanner s=new Scanner(System.in);
    static Random r = new Random();
    static int money = 0;
    static int bet = 0;
    static String[] cardFV = new String[52];
    static int rand1;
    static int rand2;
    static int rand3;
    static int rand4;
    static int rand5;
    static int cardValue;
    static int swap1;
    static int swap2;
    static int swap3;
    static int swap4;
    static int swap5;

    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        Random r = new Random();

        System.out.print("How much money do you have? ");
        money = s.nextInt();

        cardFV[0] = "2♥";    
        cardFV[1] = "3♥";
        cardFV[2] = "4♥";
        cardFV[3] = "5♥";
        cardFV[4] = "6♥";
        cardFV[5] = "7♥";
        cardFV[6] = "8♥";
        cardFV[7] = "9♥";
        cardFV[8] = "T♥";
        cardFV[9] = "J♥";
        cardFV[10] = "Q♥";
        cardFV[11] = "K♥";
        cardFV[12] = "A♥";

        cardFV[13] = "2♦";
        cardFV[14] = "3♦";
        cardFV[15] = "4♦";
        cardFV[16] = "5♦";
        cardFV[17] = "6♦";
        cardFV[18] = "7♦";
        cardFV[19] = "8♦";
        cardFV[20] = "9♦";
        cardFV[21] = "T♦";
        cardFV[22] = "J♦";
        cardFV[23] = "Q♦";
        cardFV[24] = "K♦";
        cardFV[25] = "A♦";

        cardFV[26] = "2♠";    
        cardFV[27] = "3♠";
        cardFV[28] = "4♠";
        cardFV[29] = "5♠";
        cardFV[30] = "6♠";
        cardFV[31] = "7♠";
        cardFV[32] = "8♠";
        cardFV[33] = "9♠";
        cardFV[34] = "T♠";
        cardFV[35] = "J♠";
        cardFV[36] = "Q♠";
        cardFV[37] = "K♠";
        cardFV[38] = "A♠";

        cardFV[39] = "2♣";
        cardFV[40] = "3♣";
        cardFV[41] = "4♣";
        cardFV[42] = "5♣";
        cardFV[43] = "6♣";
        cardFV[44] = "7♣";
        cardFV[45] = "8♣";
        cardFV[46] = "9♣";
        cardFV[47] = "T♣";
        cardFV[48] = "J♣";
        cardFV[49] = "Q♣";
        cardFV[50] = "K♣";
        cardFV[51] = "A♣";

        rand1 = r.nextInt(52);
        rand2 = r.nextInt(52);
        rand3 = r.nextInt(52);
        rand4 = r.nextInt(52);
        rand5 = r.nextInt(52);

        bet1();
    }

    public static void bet1()
    {
        System.out.print("How much would you like to bet? ");
        bet = s.nextInt();

        if (bet > money || bet > 5)
        {
            System.out.println("NO!!");
            bet1();
        }

        deal();
    }

    public static void deal()
    {        
        System.out.print("    Card: " + cardFV[rand1]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand2]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand3]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand4]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand5]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        if (rand1 == rand2 || rand1 == rand3 || rand1 == rand4 || rand1 == rand5)
        {
            rand1 = r.nextInt(52);
            deal();
        }
        if (rand2 == rand1 || rand2 == rand3 || rand2 == rand4 || rand2 == rand5)
        {
            rand2 = r.nextInt(52);
            deal();
        }
        if (rand3 == rand2 || rand3 == rand1 || rand3 == rand4 || rand3 == rand5)
        {
            rand3 = r.nextInt(52);
            deal();
        }
        if (rand4 == rand2 || rand4 == rand3 || rand4 == rand1 || rand4 == rand5)
        {
            rand4 = r.nextInt(52);
            deal();
        }
        if (rand5 == rand1 || rand5 == rand3 || rand5 == rand4 || rand5 == rand1)
        {
            rand5 = r.nextInt(52);
            deal();
        }

        System.out.println("");

        System.out.print("Would you like to swap out card1? (1 = Yes, 2 = No)");
        swap1 = s.nextInt();

        if (swap1 == 1)
        {
            rand1 = r.nextInt(52);
        }

        System.out.print("Would you like to swap out card2? (1 = Yes, 2 = No)");
        swap2 = s.nextInt();

        if (swap2 == 1)
        {
            rand2 = r.nextInt(52);
        }

        System.out.print("Would you like to swap out card3? (1 = Yes, 2 = No)");
        swap3 = s.nextInt();

        if (swap3 == 1)
        {
            rand3 = r.nextInt(52);
        }

        System.out.print("Would you like to swap out card4? (1 = Yes, 2 = No)");
        swap4 = s.nextInt();

        if (swap4 == 1)
        {
            rand4 = r.nextInt(52);
        }

        System.out.print("Would you like to swap out card5? (1 = Yes, 2 = No)");
        swap5 = s.nextInt();

        if (swap5 == 1)
        {
            rand5 = r.nextInt(52);
        }

        deal1();
    }
    public static void deal1()
    {
		System.out.print("    Card: " + cardFV[rand1]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand2]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand3]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand4]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        System.out.print("    Card: " + cardFV[rand5]);
        try {Thread.sleep(2000);} 
        catch(InterruptedException e) {}

        if (rand1 == rand2 || rand1 == rand3 || rand1 == rand4 || rand1 == rand5)
        {
            rand1 = r.nextInt(52);
            deal();
        }
        if (rand2 == rand1 || rand2 == rand3 || rand2 == rand4 || rand2 == rand5)
        {
            rand2 = r.nextInt(52);
            deal();
        }
        if (rand3 == rand2 || rand3 == rand1 || rand3 == rand4 || rand3 == rand5)
        {
            rand3 = r.nextInt(52);
            deal();
        }
        if (rand4 == rand2 || rand4 == rand3 || rand4 == rand1 || rand4 == rand5)
        {
            rand4 = r.nextInt(52);
            deal();
        }
        if (rand5 == rand1 || rand5 == rand3 || rand5 == rand4 || rand5 == rand1)
        {
            rand5 = r.nextInt(52);
            deal();
        }

    }
}

