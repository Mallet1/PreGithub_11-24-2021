//client class

public class PlayCards
{
    public static void main(String [] args)
    {
		Deck d = new Deck();
		System.out.println("Single Deck before Shuffle: ");
		d.printDeck();
		d.shuffle();
		System.out.println("\nSingle Deck after Shuffle: ");
		d.printDeck();


		TournamentDecks tDecks = new TournamentDecks();
		System.out.println("\nTournament Decks before Shuffle: ");
		tDecks.printDecks();
		tDecks.shuffleAll();
		System.out.println("\nTournament Decks after Shuffle: ");
		tDecks.printDecks();
	}
}