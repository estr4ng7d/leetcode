class Node{
	int data;
	Node left,right;
	
	public Node(int v){
		data=v;
		left=right=null;
	}
}

class Traversal{

	Node root;
	public Traversal(int z){
		root=null;
	}

	public void inOrderTraversal(){
		if(root==null){
			return null;
		}
		inOrderTraversal(root.left);
		System.out.println(root.data);
		inOrderTraversal(root.right);
	}

	public static void main(String[] args){
		Traversal tree=new Traversal();
		tree.root=new Node(1);

		tree.root.left=new Node(2);
		tree.root.right=new Node(3);
		tree.root.left.left=new Node(4);
		tree.root.left.right=new Node(5);

		tree.inOrderTraversal();
	}
}