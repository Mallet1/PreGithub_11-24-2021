public class TournamentDecks
{
    private Deck[] allDecks; //An array of Decks-->uninitialized
    public static final int NUMDECKS = 5;

    public TournamentDecks()
    {
        allDecks = new Deck[NUMDECKS];
        for(int i=0; i < NUMDECKS; i++)
            allDecks[i] = new Deck(); //must call constructor for each Deck
    }

    public void printDecks()
    {
        for(int i = 0; i < allDecks.length; i++)
            allDecks[i].printDeck();
        /**
         * Using for-each (from 6.3)
         * for(Deck d : allDecks)
         *      d.printDeck();
         */
    }

    public void shuffleAll()
    {
        for(int i = 0; i < allDecks.length; i++)
            allDecks[i].shuffle();         
        /**
         * Using for-each (from 6.3)
         * for(Deck d : allDecks)
         *      d.shuffle();
         */
    }
}
