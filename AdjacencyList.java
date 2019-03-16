import java.util.LinkedList;
import java.util.*;

class AdjacencyList{
	ArrayList<LinkedList<Integer>> adjList;
	int v;

	AdjacencyList(int z){
		v=z;
		adjList=new ArrayList<LinkedList<Integer>>();

		for(int i=0;i<v;i++){
			adjList.add(new LinkedList<Integer>());
		}
	}

	void add(int src, int dest){
		adjList.get(src).add(dest);
		adjList.get(dest).add(src);
//		System.out.println(adjList);
	}

	void printGraph(){
		for(int i=0;i<v;i++){
			System.out.print(i+" --> ");
			for(int z:adjList.get(i)){
				System.out.print(z+" ");				
			}
			System.out.println();
		}
	}

	public static void main(String[] args){
		AdjacencyList graph=new AdjacencyList(5);

		graph.add(0,1);
		graph.add(0,4);
		graph.add(1,2);
		graph.add(1,3);
		graph.add(1,4);
		graph.add(2,3);
		graph.add(3,4);
		
		graph.printGraph();

	}

}