package ForTest;

import java.util.ArrayList;

public class Dsatur {

    public Dsatur(int[][] graph){
        dsatur(graph);
    }

    public void dsatur(int[][] graph){
    }

    //Compute the vertex with highest saturation.(If there are two vertex have same saturation, compare their valence)
    public Vertex checkSatur(Vertex[] v){
        int index = 0;
        for(int i = 0; i < v.length - 1; i++){
            if(v[i].getSatur() == v[i+1].getSatur()){
                if(v[i].getValence() >= v[i+1].getValence()) {
                    index = i;
                }else {
                    index = i+1;
                }
            }
            else if(v[i+1].getSatur() > v[i].getSatur()){
                index = i+1;
            }
        }
        return v[index];
    }

    //Add saturation for related vertices
    public void addSatur(Vertex vertex, Vertex[] v){
        for(int i = 0; i<vertex.getRelation().size(); i++){
            v[vertex.getRelation().get(i)].addSatur();
        }
    }

    //Update saturation for vertices
    public Vertex[] updateSatur(Vertex[] v){
        int satur = 0;
        for(int i = 0; i < v.length; i++){
            for(int j = 0; j < v[i].getRelation().size(); j++){
                if(v[v[i].getRelation().get(j)].getColour() != 0){
                    satur ++;
                }
            }
            v[i].setSatur(satur);
        }
        return v;
    }

    //Compute the vertex with highest valence
    public Vertex checkValence(Vertex[] v){
        int index = 0;
        for(int i = 0; i < v.length - 1; i++){
            if(v[i+1].getValence() > v[i].getValence()){
                index = i;
            }
        }
        return v[index];
    }

    //Make graph int[][] to vertex[]
    public Vertex[] arrayToVert(int[][] graph){
        Vertex[] v = new Vertex[graph.length];
        int valence = 0;
        for (int i = 0; i<graph.length; i++) {
            valence = 0;
            for (int j = 0; j<graph[i].length; j++) {
                valence += graph[i][j];
            }
            v[i] = new Vertex(i, valence, new ArrayList<Integer>(), 0);
        }
        return v;
    }

    //Computes the realtions between vertecies
    public Vertex[] addRelations(int[][] graph, Vertex[] v){
        for (int i = 0; i<graph.length; i++) {
            for (int j = 0; j<graph[i].length; j++) {
                if(graph[i][j] == 1){
                    v[i].addRelation(j);
                }
            }
        }
        return v;
    }

    //Check all vertices colored or not
    public boolean checkColored(Vertex[] v){
        boolean result = true;
        for(int i = 0; i<v.length; i++){
            if(v[i].getColour() == 0){
                result = false;
            }
        }
        return result;
    }
}
