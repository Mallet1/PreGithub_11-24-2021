import java.text.*;
import java.util.*;
public class Race
{
    public static void main(String args[])
    {
        Scanner s = new Scanner(System.in);
        DecimalFormat   fmt=new   DecimalFormat("0.00000"); 
        int hours=0, minutes=0, seconds=0;

        System.out.println("Enter the time in hours, minutes, and seconds that it took you to run the marathon.");

        System.out.println("Hours: ");
        int newHours = s.nextInt();

        System.out.println("Minutes: ");
        int newMinutes = s.nextInt();

        System.out.println("Seconds: ");
        int newSeconds = s.nextInt();
        
        //Time sprint300 = new Time(double secs);

        System.out.println("Enter the number of seconds it took you to sprint 300 meters.");
        double sprint = s.nextDouble();
        
        
        /*
        seconds = (int)(sprint + .5);
        minutes = seconds/60;
        seconds%=60;
        hours = seconds/60;
        seconds%=60;
        */
        
        Time sprint300 = new Time(sprint);
        Time times = new Time(newHours,newMinutes,newSeconds);
        Time marathonRecord = new Time(2,1,39);
        Time record300 = new Time(30.81);
        
        

        System.out.println("Marathon time: " + times.toString());
        System.out.println("Sprint time: " + sprint300.toString());

        System.out.println("You ran the marathon " + Math.abs(marathonRecord.getSeconds() - times.getSeconds()) + " seconds slower than Eliud Kipchoge.");
        System.out.println("You sprinted 300 meters " + Math.abs(record300.getSeconds()-sprint300.getSeconds()) + " seconds slower that Wayde van Niekerk.");
        
        double secondsToNewYork = (times.getSeconds()/26.0)*(2789);
        double LAtoNewYork = secondsToNewYork/60/60/24;
        
        System.out.println("If you run at the same rate as your marathon, you would travel from LA to New York in " + fmt.format(LAtoNewYork) + " days");
    }
}
