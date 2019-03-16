class Node{
	int data;
	Node left,right;
	Node(int z){
		data=z;
		left=right=null;
	}
}

class BSTDelete{

	Node root;

	BSTDelete(){
		root=null;
	}

	void insertRec(Node root,int z){
		if (root == null){
			root = new Node(data);
			return root;
		}
		if(z<root.data)
			insertRec(root.left,z);
		else
			insertRec(root.right,z);
	}

	void insert(int z){
		insertRec(root,z);
	}

	void delete(int z){
		deleteRec(root,z);
	}

	Node deleteRec(Node root, int z){
		if(root==null) return false;
		else if(root.data<z){
			root.left=deleteRec(root.right,z);
		}else if(root.data>z){
			root.right=deleteRec(root.left,z);
		}

		else{
			if(root.left==null)
				return root.right;
			else if(root.right==null)
				return root.left;
		}

	}

	public static void main(String[] args){
		BSTDelete tree=new BSTDelete();

		tree.insert(50);
		tree.insert(30); 
		tree.insert(20); 
		tree.insert(40); 
		tree.insert(70); 
		tree.insert(60); 
		tree.insert(80); 

		tree.delete(20);


	}
}
