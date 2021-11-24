public class Tile
{
    private String letter="";
    private int value=0;
    private static final int[] scores={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    private static final String alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    
    public Tile(String r)
    {
        letter=r;
        value=scores[alpha.indexOf(letter.toUpperCase())];
    }
    
    public String getLetter()
    {
        return letter;
    }
    
    public int getValue()
    {
        return value;
    }
    
    public String toString()
    {
        return letter+"("+value+")";
    }
}
