import java.util.*;
public class FilmFestival
{
    public static void main(String args[])
    {
        ArrayList<Movie> movies = new ArrayList<Movie>();
        movies.add(new Action("Inception",80,"PG-13", new String[]{"Leonardo DiCaprio", "Joseph Gordon-Levitt", "Tom Berenger", "Ellen Page", "Tom Hardy"},4));
        movies.add(new Action("Inception",80,"PG-13", new String[]{"Leonardo DiCaprio", "Joseph Gordon-Levitt", "Tom Berenger", "Ellen Page", "Tom Hardy"},4));
        movies.add(new Action("Inception",80,"PG-13", new String[]{"Leonardo DiCaprio", "Joseph Gordon-Levitt", "Tom Berenger", "Ellen Page", "Tom Hardy"},4));
        movies.add(new RomCom("The Break-Up",68,"PG", new String[]{"Jennifer Aniston", "Vince Vaughn", "Jon Favreau"},false));
        movies.add(new Comedy("Ghostbusters",99,"PG-13", new String[]{"Bill Murray", "Dan Aykroyd", "Sigourney Weaver", "Harold Ramis"}));
        movies.add(new Movie("Good Will Hunting",89,"R", new String[]{"Robin Williams", "Matt Damon", "Ben Affleck", "Minnie Driver"}));
        movies.add(new Movie("The Lion King",95,"G", new String[]{"Matthew Broderick", "Jeremy Irons", "James Earl Jones", "Jonathan Taylor Tomas"}));
        movies.add(new RomCom("The Break-Up",68,"PG", new String[]{"Jennifer Aniston", "Vince Vaughn", "Jon Favreau"},false));
        movies.add(new Movie("The Lion King",82,"PG", new String[]{"Donald Glover", "Beyonce", "Seth Rogen"}));
        movies.add(new Action("The Matrix",89,"PG-13", new String[]{"Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"},25));
        movies.add(new Comedy("Toy Story",97,"G", new String[]{"Tom Hanks", "Tim Allen", }));
        movies.add(new RomCom("Sleepless in Seattle",75,"PG", new String[]{"Meg Ryan", "Tom Hanks"},true));
        movies.add(new Action("The Matrix",89,"PG-13", new String[]{"Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"},25));
        removeDups(movies);
        sortMovies(movies);
        violentMovies(movies);
        familyMovies(movies);
        tomMovies(movies);
        showMovies(movies);
        printMovies(movies);
    }

    /**
     * Remove duplicate Movies in arr--must use the equals method from Movie to determine if Movies are equal
     * Be careful--removing from an ArrayList shifts the indices
     * Decrease total movies using accessor and modifier of static variable totalMovies in Movie
     */    
    public static void removeDups(ArrayList<Movie> arr) // functional
    {
        for(int i=arr.size()-1;i>=0;i--)
        {
            //System.out.println(i);
            for(int k=arr.size()-1;k>=0;k--)
            {
                //System.out.println(k);
                if(i!=k && arr.get(i).equals(arr.get(k)))
                {
                    //System.out.println("Size "+arr.size());
                    Movie.setTotalMovies((Movie.getTotalMovies())-1);
                    arr.remove(i);
                    break;
                }
            }
            //System.out.println();
        }
    }

    /**
     * Print total movies using accessor of static variable totalMovies in Movie
     * Print Movies in arr by calling the toString() method (for-each loop suggested)
     */   
    public static void printMovies(ArrayList<Movie> arr)
    {
        System.out.println("There are "+Movie.getTotalMovies()+" movies in the film festival");
        for(Movie movie : arr)
        {
            System.out.println(movie.toString());
        }
    }

    /**
     * Sort arr using either Selection Sort or Insertion Sort
     * You must use the getBetter() method from Movie
     */  
    public static void sortMovies(ArrayList<Movie> arr) // functional
    {
         for(int n=0; n<arr.size()-1; n++) // selection sort
         {
              Movie min=arr.get(n);
              int minIndex = n;
              for(int i=n+1; i<arr.size(); i++)
              {
                  if(arr.get(i).getBetter(min) == min)
                  {
                      minIndex = i;
                      min = arr.get(i);
                  }
              }
              Movie temp=arr.get(minIndex);
              arr.set(minIndex,arr.get(n));
              arr.set(n,temp);
         }
         //for(Movie movie : arr)
         //     System.out.println("Score = " + movie.getScore());
    }

    /**
     * Call changeRating() for every Action movie in arr. (for-each loop suggested)
     * Print the TITLE of any movie that was changed.
     */
    public static void violentMovies(ArrayList<Movie> arr)
    {
        System.out.println("\nThe following action movies contain too many deaths and must be rated R:");
        for(Movie actionMovie : arr)
        {
            if(actionMovie instanceof Action)
            {
                if(((Action)actionMovie).changeRating() == true)
                    System.out.println(actionMovie.getTitle());
            }
        }
    }

    /**
     * print out TITLE of every Movie in arr with a G rating (for-each loop suggested)
     */
    public static void familyMovies(ArrayList<Movie> arr) // functional
    {
        System.out.println("\nThe following movies are suitable for children:");
        for(Movie familyMovie : arr)
        {
            if(familyMovie.getRating() == "G")
                System.out.println(familyMovie.getTitle());
        }
    }

    /**
     * print out the TITLE of every Movie in arr that stars an actor with a first name of Tom
     * Just check the first three letters of every actor to see if they are equal to Tom
     * Make sure every movie is printed ONCE (Inception has 2 Toms)
     * (Notice I spelled Jonathan Taylor Thomas' name incorrectly (Tomas) to make sure you check
     * the FIRST three letters.)
     * You must use SUBSTRING OR INDEXOF.
     */
    public static void tomMovies(ArrayList<Movie> arr) // functional
    {
        System.out.println("\nThe following movies star an actor named Tom:");
        for(Movie movie : arr)
        {
            for(int i=0;i<movie.getActors().length;i++)
            {
                String actor = movie.getActors()[i];
                if(actor.substring(0,3).equalsIgnoreCase("tom"))
                {
                    System.out.println(movie.getTitle());
                    break;
                }
            }
        }
    }

    /**
     * Increase the views for every Movie in arr by a random integer from 50-500
     * This means that you need a loop for every movie that goes "views" times.
     * If the movie is a Comedy, increase the laughs by a random number from 0-50 by calling the overloaded showMovie.
     * Call the showMovie method from Movie for every other type of movie.
     * (for-each loop suggested)
     */
    public static void showMovies(ArrayList<Movie> arr)
    {
        for(Movie movie : arr)
        {
            if(movie instanceof Comedy)
            {
                int views = (int)(Math.random()*451)+50;
                int laughs = (int)(Math.random()*51);
                for(int i=0;i<views;i++)
                    ((Comedy)movie).showMovie(laughs);
            }
            else
            {
                int views = (int)(Math.random()*451)+50;
                for(int i=0;i<views;i++)
                    movie.showMovie();
            }
        }
    }
}

