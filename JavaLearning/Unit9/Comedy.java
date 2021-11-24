public class Comedy extends Movie
{
    private int laughs;
    
    public Comedy(String t, int s, String r, String[] a)
    {
        super(t,s,r,a);
        laughs = 0;
    }
    
    public int getLaughs()
    {
        return laughs;
    }
    
    public void setLaughs(int l)
    {
        laughs = l;
    }
    
    @Override
    public String toString()
    {
        return super.toString() + "Laughs: " + laughs;
    }
    
    public void showMovie(int i)
    {
        laughs+=i;
        super.showMovie();
    }
}
