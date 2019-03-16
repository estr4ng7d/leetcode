class Node{
	int data;
	Node left,right;

	Node(int z){
		data=z;
		left=right=null;
	}
}

class TraversalBFS{
	Node root;
	TraversalBFS(){
		root=null;
	}

	void levelOrder(){
		int h=calculateHeight(root);
		System.out.println(h);

		for(int i=1;i<=h;i++)
			givenLevel(root,i);
	}

	int calculateHeight(Node root){
		if (root==null){
			return 0;
		}
		else{
			int lh=calculateHeight(root.left);
			int rh=calculateHeight(root.right);

			if(lh<rh){
				return rh+1;
			}else return lh+1;
		}
	}

	void givenLevel(Node root, int level){
		if(root==null)
			return;
		if(level==1)
			System.out.println(root.data+" ");
		else if(level>1){
			givenLevel(root.left, level-1);
			givenLevel(root.right, level-1);
		}
	}

	public static void main(String[] args){
		TraversalBFS tree=new TraversalBFS();
		tree.root=new Node(1);
		tree.root.left=new Node(2);
		tree.root.right=new Node(3);
		tree.root.left.left=new Node(4);
		tree.root.left.right=new Node(5);

		tree.levelOrder();

	}
}