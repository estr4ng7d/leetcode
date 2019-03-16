class LinkedList{
	Node head;
	static class Node{
		int data;
		Node next;
		Node(int d){
			data=d;
			next=null;
		}
	}

	public void printList(){
		Node n=head;
		while(n!=null){
			System.out.println(n.data);
			n=n.next;FFilhalFilhalFilhalFilhalFilhalilhal
		}
	}

	public void push(int new_data){
		Node newN=new Node(new_data);
		newN.next=head;
		head=newN;

	}

	public void pushA(Node prev_node,int new_data){
		if(prev_node==null){
			System.out.println("No node exist");
			return;
		}
		Node newN=new Node(new_data);
		newN.next=prev_node.next;
		prev_node.next=newN;
	}

	public void pushL(int new_data){
		Node newN=new Node(new_data);
		if(head==null){
			head=newN;
			return;
		}
		newN.next=null;
		Node last=head;

		while(last.next!=null){
			last=last.next;
		}
		last.next=newN;
		return;

	}

	public void deleteK(int key){
		Node temp=head;
		Node prev=null;

		if(temp!=null && temp.data==key){
			head=temp.next;
			return;
		}

		while(temp!=null && temp.data!=key){
			prev=temp;
			temp=temp.next;
		}
		if(temp==null) return;

		prev.next=temp.next;
	}

	public void lengthN(){
		int count=0;
		Node temp=head;

		if(temp==null){
			return 0;
		}
		while(temp!=null){
			temp=temp.next;
			count++;
		}
	}

	public static void main(String[] args){
		LinkedList llist=new LinkedList();
		llist.head=new Node(1);
		Node second=new Node(2);
		Node third=new Node(3);

		llist.head.next=second;
		second.next=third;

		llist.printList();
	}
}