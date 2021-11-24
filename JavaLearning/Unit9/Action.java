public class Action extends Movie
{
    private int deaths;
    
    public Action(String t, int s, String r, String[] a, int d)
    {
        super(t,s,r,a);
        deaths = d;
    }
    
    public int getDeaths()
    {
        return deaths;
    }
    
    public void getDeaths(int d)
    {
        deaths = d;
    }
    
    @Override
    public String toString()
    {
        return super.toString() + "Deaths: " + deaths;
    }
    
    public boolean changeRating()
    {
        if(deaths>=5)
        {
            super.setRating("R");
            return true;
        }
        return false;        
    }
}
