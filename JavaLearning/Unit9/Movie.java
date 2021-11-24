import java.util.*;
public class Movie
{
    private String title; //title of movie
    private int score; //score on Rotting Potatoes
    private String rating; //G, PG, PG-13, or R
    private String actors[]; //list of main actors in the movie
    private int views; //number of times movie is viewed by an audience
    private static int totalMovies=0; //total movies in festival

    public Movie(String t, int s, String r, String a[])
    {
        title=t;
        score=s;
        rating=r;
        actors=a;
        views=0;
        totalMovies++;
    }
    //accessors
    public String getTitle()
    {
        return title;
    }

    public int getScore()
    {
        return score;
    }

    public String getRating()
    {
        return rating;        
    }

    public String[] getActors()
    {
        return actors;
    }

    public int getViews()
    {
        return views;
    }

    public static int getTotalMovies()
    {
        return totalMovies;
    }

    //modifiers
    public void setScore(int s)
    {
        score=s;
    }

    public void setRating(String r)
    {
        rating=r;
    }

    public static void setTotalMovies(int t)
    {
        totalMovies=t;
    }

    //other methods   
    public void showMovie() //increase views by one
    {
        views++;
    }

    @Override
    public String toString()
    {
        String s = "\nTitle: " + title + "\nScore: " + score + "\nRating: " + rating + "\nActors:\n";
        for(String a: actors)
        {
            s+=a+"\n";
        }
        s+="Views: " + getViews() + "\n";
        return s;     
    }

    /**
     * TO DO: EQUALS() METHOD
     * Override the equals method from Object.
     * It will return true when all of these conditions are met:
     *    the parameter is not null
     *    the parameter is a Movie
     *    the titles of the Movies are the same
     *    the scores of the Movies are the same
     * Otherwise, return false.
     */

    @Override
    public boolean equals(Object other)
    {
        return other != null && other instanceof Movie && ((Movie)other).title.equals(this.title) && ((Movie)other).score == this.score;
    }

    /**
     * TO DO: GETBETTER() METHOD
     * getBetter()
     * takes a Movie parameter (other)
     * returns the Movie that has the better score: this or other
     * either movie can be returned if they have the same score
     */

    public Movie getBetter(Movie other)
    {
        if(((Movie)other).score >= this.score)
            return other;
        return this;
    }

}
