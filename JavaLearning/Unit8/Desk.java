public class Desk
{
    private boolean wobbles; //indicates whether desk is wobbly
    private String name; //first name of student at the desk
    public Desk(String n)
    {
        int x = (int)(Math.random()*100+1);
        if(x<=30) //The chance of a wobbly desk is 30%.
            wobbles = true;
        else
            wobbles=false;
        name = n;
    }

    public boolean getWobbles()
    {
        return wobbles;
    }

    public String getName()
    {
        return name;
    }

    public void setWobbles(boolean w)
    {
        wobbles=w;
    }

    public void setName(String n)
    {
        name=n;
    }

    /**
     * makeWobbly()-->private helper function
     * returns new String that makes every other letter uppercase, starting with 
     * first letter
     */
    private String makeWobbly(String s) 
    {
        String wob="";
        for(int i=0; i<s.length(); i++)
        {
            if(i%2==0)
                wob+=s.substring(i,i+1).toUpperCase();
            else
                wob+=s.substring(i,i+1);
        }
        return wob;
    }

    public String toString()
    {
        String s = "";        
        if(name.equals("") && !wobbles)
            s = "---"; //non-wobbly empty desk
        else if(name.equals("") && wobbles)
            s = "-^-"; //wobbly empty desk
        else if(wobbles)
            s=makeWobbly(name); //wobbly occupied desk
        else
            s = name; //non-wobbly occupied desk
        return s;
    }

}