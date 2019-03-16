class GraphBFS{

	ArrayList<LinkedList<Integer>> adj_list;
	int v;

	GraphBFS(int z){
		adj_list=new ArrayList<LinkedList<Integer>>();
		v=z;
		for(int i=0;i<v;i++){
			adj_list.add(new LinkedList<Integer>());
		}

	}

	void add(int src, int dest){
		adj_list.get(src).add(dest);
		adj_list.get(dest).add(src);

	}

	public static void main(String[] args){

		GraphBFS graph=new GraphBFS(4);
		graph.add(0,1);
		graph.add(0,2);
		graph.add(1,2);
		graph.add(2,0);
		graph.add(2,3);
		graph.add(3,3);

		

	}
}