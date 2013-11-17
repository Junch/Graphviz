Graphviz 入门
===

把如下代码保存为hello.dot

```
digraph G {
	Hello -> World
}
```
输入命令：  
dot -T png hello.dot -o hello.png  
即可画出如下图片:  
![image](hello.png)


###例子1

```
graph graphname {
	a -- b -- c;
	b -- d
}
```
![image](g1.png)

###例子2
```
digraph graphname {
	a -> b -> c;
	b -> d;
}
```
![image](g2.png)

###例子3
```
//DOT语言中，可以对节点和边添加不同的属性。

digraph graphname {
    //节点的属性，节点的名称
    a [lable = "Foo"];

    //节点的属性，节点的形状
    b [shape = box];

    //边的属性，边的颜色
    a -> b -> c [color = blue];

    //边的属性，边的线状
    b -> d [style = dotted];
}
```
![image](g3.png)

###例子4
```
digraph G {
	//把图片的尺寸设为4inch * 4inch
	size = "4,4";
	main [shape = box];
	
	//边的重要程度，默认是1
	main->parse [weight = 8];
	parse->execute;
	
	//点状线
	main->init[style = dotted];
	main->cleanup;
	
	//连接了两条线
	execute->{make_string;printf}
	init->make_string;
	
	//把边的默认颜色设为red
	edge [color = red];
	main->printf [sytle=bold, label = "100times"];
	
	//节点的名称
	make_string [label = "make a\nstring"];
	
	//设置节点的默认属性
	node [shape=box,style =filled,color=lightgrey];
	execute->compare;
}
```
![image](g4.png)

###例子5
```
digraph G{
	a -> b -> c;
	b -> d;
	
	/* 形状为多边形，边数为5，外框为3条，颜色为淡蓝，样式为填充 */
	a [shape = polygon, sides = 5, peripheries = 3, color = lightblue, style = filled];
	
	/* 形状为多边形，边数为4，角的倾斜度为0.4，内容为hellow world*/
	c [shape = polygon, sides = 4, skew = 0.4, label = "hello world"];
	
	/* 形状为倒三角，整体旋转30度 */
	d [shape = invtriangle,orientation = 30];
	
	/* 形状为多边形，边数为4，扭曲度为0.7 */
	e [shape = polygon, sides = 4, distortion = 0.7];
}

```
![image](g5.png)

###例子6
```
digraph G {
	label = "Binary search tree";
	node [shape = record];

	A [label = "<f0>|<f1>A|<f2>"];
	B [label = "<f0>|<f1>B|<f2>"];
	C [label = "<f0>|<f1>C|<f2>"];
	D [label = "<f0>|<f1>D|<f2>"];
	E [label = "<f0>|<f1>E|<f2>"];
	F [label = "<f0>|<f1>F|<f2>"];
	G [label = "<f0>|<f1>G|<f2>"];

	A:f0 -> B:f1;
	A:f2 -> C:f1;
	B:f0 -> D:f1;
	B:f2 -> E:f1;
	C:f0 -> F:f1;
	C:f2 -> G:f1;
}
```
![image](g6.png)

###例子7
```
digraph G{
	nodesep = .05;
	rankdir = LR;
	
	node [shape = record,width = .1,height = .1];
	node0 [label = "<f0>|<f1>|<f2>|<f3>|<f4>|<f5>|<f6>|",height = 2.5];
	
	node [width = 1.5];
	node1 [label = "{<n>n14|719|<p>}"];
	node2 [label = "{<n>a1|805|<p>}"];
	node3 [label = "{<n>i9|718|<p>}"];
	node4 [label = "{<n>e5|989|<p>}"];
	node5 [label = "{<n>t20|959|<p>}"];
	node6 [label = "{<n>o15|794|<p>}"];
	node7 [label = "{<n>s19|659|<p>}"];
	
	node0:f0 -> node1:n;
	node0:f1 -> node2:n;
	node0:f2 -> node3:n;
	node0:f5 -> node4:n;
	node0:f6 -> node5:n;
	node2:p -> node6:n;
	node4:p -> node7:n;
}
```
![image](g7.png)

