public class RomCom extends Comedy
{
    private boolean happy;
    
    public RomCom(String t, int s, String r, String[] a, boolean h)
    {
        super(t,s,r,a);
        happy = h;
    }
    
    public boolean getHappy()
    {
        return happy;
    }
    
    public void setHappy(boolean h)
    {
        happy = h;
    }
    
    public String toString()
    {
        if(happy == true)
            return super.toString() + "\nHappy Ending? yes";
        return super.toString() + "\nHappy Ending? no";
    }
}
