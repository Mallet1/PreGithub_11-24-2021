public class Classroom
{
    private Desk[][] roomDesks;
    
    /**
     * Precondition: names.length <= rows*desksPerRow
     */
    public Classroom(int rows, int desksPerRow, String names[])
    {
        int sum=0;
        roomDesks = new Desk[rows][desksPerRow];
        for(int i=0; i<roomDesks.length; i++)
        {
            for(int j=0; j<roomDesks[0].length; j++)
            {
                if((sum)<names.length)
                    roomDesks[i][j] = new Desk(names[sum]);
                else
                    roomDesks[i][j] = new Desk("");
                sum++;
            }
        }
    }
    
    public Desk getDesk(int row, int col)
    {
        return roomDesks[row][col];
    }
    
    public boolean fillDesk(Desk d, String name)
    {
        if(d.getName()=="")
        {
            d.setName(name);
            return true;
        }
        return false;
    }
    
    public Desk findEmptyDesk()
    {
        for(int i=0; i<roomDesks.length; i++)
        {
            for(int j=0; j<roomDesks[0].length; j++)
            {
                if(roomDesks[i][j].getName()=="")
                    return roomDesks[i][j];
            }
        }
        return null;
    }

    public void swapDesks(Desk d1, Desk d2)
    {
        String temp=d1.getName();
        d1.setName(d2.getName());
        d2.setName(temp);
    }
    //MUST USE A FOR-EACH LOOP FOR CREDIT
    public String toString()
    {
        String str="";
        for(Desk[] row : roomDesks)
        {
            for(Desk col : row)
            {
                str+=col.toString()+" ";
            }
            str+="\n";
        }
        return str;
    }
}
