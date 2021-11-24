
public class Unit8Exercise
{
     public static void main(String[] args)
    {
        String[] students={"Bobby", "Sam", "Carl", "Maya", "Ellen", "Javier", "Laura", "Amy", "Greg", "Liz", 
            "Mark", "Larry", "Zach", "Kate"}; //names of students in the classroom
        Classroom myClassroom = new Classroom(4,5,students); //4 rows with 5 desks per row

        // Calls toString in Classroom which, in turn, calls toString in Desk.
        System.out.println(myClassroom);
        
        //Tries to assign three more students to specific desks.
        boolean s1=myClassroom.fillDesk(myClassroom.getDesk(0,0),"Jill");
        boolean s2=myClassroom.fillDesk(myClassroom.getDesk(2,4), "Jack");
        boolean s3=myClassroom.fillDesk(myClassroom.getDesk(3,2), "Alice");
        if(s1)
            System.out.println("Jill was assigned to desk[0][0].");
        else
            System.out.println("Sorry, Jill. Go to a different school.");
        if(s2)
            System.out.println("Jack was assigned to desk[2][4].");
        else
            System.out.println("Sorry, Jack. Go to a different school.");
        if(s3)
            System.out.println("Alice was assigned to desk[3][2].");
        else
            System.out.println("Sorry, Alice. Go to a different school.");
            
        //print classroom again
        System.out.println("\n");
        System.out.println(myClassroom);
        
        //add more students
        String[] moreStudents={"Nathan", "Beth", "Scott", "Holly", "Joe", "Matt"};
        addMoreStudents(myClassroom, moreStudents);
        
        //print classroom
        System.out.println("\n");
        System.out.println(myClassroom);
        
        //swap seats
        switchSeats(myClassroom,0,0,1,2);
        switchSeats(myClassroom,1,3,3,4);
        
        //print classroom
        System.out.println("\n");
        System.out.println(myClassroom);
    }
    public static void addMoreStudents(Classroom c,String[] s)
    {
        for(int i=0;i<s.length;i++)
        {
            if(c.findEmptyDesk()!=null)
                c.findEmptyDesk().setName(s[i]);
            else
                System.out.println("There is no desk available for "+s[i]+".");
        }
    }
    public static void switchSeats(Classroom c,int row1, int col1, int row2, int col2)
    {
        c.swapDesks(c.getDesk(row1,col1),c.getDesk(row2,col2));
        System.out.println(c.getDesk(row1,col1).getName()+" swapped with "+c.getDesk(row2,col2).getName());
    }
}
