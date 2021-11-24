import java.text.*;
import java.util.*;
public class Time
{
    private int hours, minutes, seconds;

    public Time(int inhours, int inminutes, int inseconds)
    {
        hours=inhours;
        minutes=inminutes;
        seconds=inseconds;
    }

    public Time(double totalSeconds)
    {
        int total=(int)(totalSeconds+0.5);
        hours = total/3600;
        total%=3600;
        minutes = total/60;
        seconds=total%60;
    }

    public int getSeconds()
    {
        int totalSeconds=(3600*hours)+(60*minutes)+seconds;
        return totalSeconds;
    }

    public String toString()
    {
        return hours + ":" + minutes + ":" + seconds;
    }
}
