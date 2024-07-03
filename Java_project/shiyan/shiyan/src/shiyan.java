class Point
{
    int[] x;
    static double min=-5.12;
    static double max=5.12;
    static int size=22;
    double fitness;

    public Point()
    {
        x=new int[size];
        for(int i=0;i<size;i++)
            if(Math.random()>0.5)
                x[i]=1;
            else
                x[i]=0;
    }

    public double decode()
    {
        double y=0;
        for(int i=0;i<size;i++)
        {
            y=y+x[i]*Math.pow(2,size-1-i);
        }
        y=min+y*(max-min)/(Math.pow(2,size)-1.0);
        return y;
    }

    public double getFitness()
    {
        double vx=decode();
        fitness=vx*vx;
        return fitness;
    }

}


class Tools
{

    public static void copy(Point a,Point b)
    {
        for(int i=0;i<a.x.length;i++)
        {
            b.x[i]=a.x[i];
        }
        b.fitness=a.fitness;
    }


    public static void swap(Point a,Point b)
    {
        Point temp=new Point();
        copy(a,temp);
        copy(b,a);
        copy(temp,b);
    }

    public static int findBest(Point[] arr)
    {
        int pos=0;
        double min=arr[pos].fitness;
        for(int i=1;i<arr.length;i++)
        {
            if(min>arr[i].fitness)
            {
                pos=i;
                min=arr[i].fitness;
            }
        }
        return pos;

    }

    public static void cross(Point a,Point b,Point ab,Point ba)
    {
        int pos=(int)(Math.random()*Point.size);
        for(int i=0;i<pos;i++)
        {
            ab.x[i]=a.x[i];
            ba.x[i]=b.x[i];
        }
        for(int i=pos;i<Point.size;i++)
        {
            ab.x[i]=b.x[i];
            ba.x[i]=a.x[i];
        }
    }


    public static void mutA(Point a)
    {
        Point temp=new Point();
        copy(a,temp);
        int pos=(int)(Math.random()*Point.size);
        a.x[pos]=(a.x[pos]+1)%2;
        if(a.getFitness()>temp.fitness)
            a.x[pos]=(a.x[pos]+1)%2;
    }
}


class GASet
{
    Point[][] obj;
    int row,col;

    public GASet(int r,int c)
    {
        row=r;
        col=c;
        obj=new Point[row][col];
        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
                obj[i][j]=new Point();
    }


    public void evolution()
    {

        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
                obj[i][j].getFitness();


        int best;
        for(int i=0;i<row;i++)
        {
            best=Tools.findBest(obj[i]);
            Tools.swap(obj[i][best],obj[i][i]);
        }


        for(int i=0;i<row;i++)
            for(int j=i+1;j<col;j++)
                Tools.cross(obj[i][i],obj[j][j],
                        obj[i][j],obj[j][i]);


        for(int i=0;i<row;i++)
            for(int j=0;j<col;j++)
                Tools.mutA(obj[i][j]);
    }
}

public class shiyan
{
    public static void main(String[] arg)
    {
        GASet s=new GASet(20,20);
        int n=0;
        while(n<100)
        {
            s.evolution();
            n++;
        }
        int allBest=findBest(s.obj);
        System.out.println("Min="+s.obj[allBest][allBest].getFitness());
    }

    public static int findBest(Point[][] arr)
    {
        int pos=0;
        double min=arr[pos][pos].fitness;
        for(int i=1;i<arr.length;i++)
        {
            if(min>arr[i][i].fitness)
            {
                pos=i;
                min=arr[i][i].fitness;
            }
        }
        return pos;

    }
}
