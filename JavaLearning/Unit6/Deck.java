/*
This program is modified from a version
in 8th edn of Barron's AP CS Guide
 */
public class Deck
{
    private int[] deck; //this is an array field-->it is declared, but not initialized-->
    //Its default value is NULL.
    private static final int NUMCARDS = 10; //Constant for number of cards in the deck.

    public Deck()
    {
        deck = new int[NUMCARDS]; //initialize deck

        // Assign ints to cards: 0 to NUMCARDS-1
        for(int i=0; i < NUMCARDS; i++)
            deck[i] = i;
    }

    public void printDeck()
    {
        for(int i=0; i<deck.length; i++)
            System.out.print(deck[i] + " ");
        System.out.println();
        
        /**
         * Using for-each (from 6.3)
         * for(int val : deck)
         *      System.out.println(val);
         */
    }

    private void swap(int i, int j) //private helper method--> only used to make shuffle() easier
    {
        //This code swaps two cards in a deck
        int temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }

    /*
    Loops backwards in the deck.
    Choose a random card from those remaining
    and swap it with the current card.
    */
    public void shuffle()
    {
        int index;
        for(int i = NUMCARDS -1; i > 0; i--)
        {
            // generate int from 0 to i
            index = (int)(Math.random() * (i + 1));
            swap(i, index);
        }
    }
}