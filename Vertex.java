import java.io.*;
import java.util.*;
import java.awt.*;


public class Vertex
{
    private int valence;
    private int vertexNum;
    private int colour;
    private Color color;
    private ArrayList<Integer> relations;
    private int colourSatur;
    private int x;
    private int y;

  /*private Color[] colors = {Color.black,Color.red,Color.blue,Color.green,Color.gray,Color.cyan,Color.darkGray,Color.pink,Color.orange,Color.yellow,Color.lightGray,new Color(47,76,100),new Color(248,186,24),
        new Color(42,80,106),new Color(206,211,31),
        new Color(101,233,162),new Color(2,153,194),
        new Color(22,198,199),new Color(159,236,3),
        new Color(137,104,116),new Color(67,18,140),
        new Color(148,179,143),new Color(233,0,44),
        new Color(194,156,1),new Color(252,108,179),
        new Color(52,54,230),new Color(31,138,142)};*/

    public Vertex(int xVertexNum, int xValance, ArrayList<Integer> rel, int satur)
    {
        relations = rel ;
        vertexNum = xVertexNum;
        valence = xValance;
        colourSatur = satur;
    }

    public Vertex(int xVertexNum,int xValance)
    {
        vertexNum = xVertexNum;
        valence = xValance;
    }


    //Sets thecolour value
    public void setColour(int colourNum)
    {
        colour = colourNum;
    }


    // Returns the colour value
    public int getColour()
    {
        return colour;
    }

    public Color getColor()
    {
        return color;
    }

    public void setColor(Color xcolor)
    {
        color = xcolor;
    }

    public void updateColour()
    {
        colour++;
    /*if(color != colors[26])
      color = colors[colour-1];*/
    }


    //adds an element to the relations arraylist
    public void addRelation(int b)
    {
        this.relations.add(b);
    }

    public void setValence(int xValance)
    {
        valence = xValance;
    }

    public int getValence()
    {
        return valence;
    }

    // Returns the relations arraylist
    public ArrayList<Integer> getRelation()
    {
        return this.relations;
    }


    //Takes the index of relations arraylist and returns the index of a related vertex at
    public int getRelIndex(int index)
    {
        return relations.get(index);
    }


    //Sets the value of colour saturation
    public void setSatur(int satur)
    {
        colourSatur = satur;
    }


    // Gives the value of colour saturation
    public int getSatur()
    {
        return colourSatur;
    }

    public void setVertexNum(int x)
    {
        vertexNum = x;
    }

    public int getVertexNum()
    {
        return vertexNum;
    }

    public void setPos(int xX,int xY)
    {
        x = xX;
        y = xY;
    }

    public int getX()
    {
        return x;
    }

    public int getY()
    {
        return y;
    }
}
