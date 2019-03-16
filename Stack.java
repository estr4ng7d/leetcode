class Stack{
	static final int MAX=100;
	int top;
	int a[]=new int[MAX];

	Stack(){
		top = -1;
	}
	boolean push(int data){
		if(top>=(MAX-1)){
			System.out.println("Stack overflow");
			return false;
		}
		a[++top]=x;
		System.out.println(x+ "pushed on stack");
		return true;
	}

	int pop(){
		if(top<0){
			System.out.println("Stack underflow");
			return 0;
		}
		else{
			int x=a[top--];
			return x;
		}
	}

	public static void main(String[] args){
		Stack s=new Stack();
		s.push(10);
		s.push(20);
		s.push(30);

		s.pop();
	}
}