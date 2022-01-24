def conn(root):
	start = root	
	this=start
	while start.left:
		this.left.next = this.right
		if this.next:
			this.right.next = this.next.left
			this = this.next
		else:
			start=start.left
			this = start	

