public class WordTiles
{
    private Tile[] word;
    
    public WordTiles(String s)
    {
        word=new Tile[s.length()];
        for(int i=0;i<word.length;i++)
            word[i] = new Tile(s.substring(i,i+1));
    }
    
    public int getWordScore()
    {
        int total=0;
        for(int i=0;i<word.length;i++)
            total+=word[i].getValue();
        return total;
    }
    
    public String toString()
    {
        String print="";
        for(int i=0;i<word.length;i++)
            print+=word[i].toString()+" ";
        return print;
    }
}
