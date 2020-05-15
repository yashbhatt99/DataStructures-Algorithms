
#include<iostream>
#include<bits/stdc++.h>

using namespace std;


// this class represents directed graph which uses adjacency list representation.
class Graph
{
	int V;  // No. of vertices in graph

	//Pointing array that contains adjacency list/

	list<int> *adj;


	//Recursive function of DFS
	//this function basically have two parameters passed inside it
	//first the vertex that we are visiting at that time ,
	//second is to check that the current vertex is in the visited array or not!

	void DFSrecursive(int v, bool visited[]);


public:

	Graph(int V); //Contructor

	//function to add new edge into the graph
	// v is the source and w is the destination.(remember this is directed graph)
	void addEdge(int v, int w);

	//DFS traversal of the vertices , source if v.

	void DFS(int v);
};

Graph::Graph(int V)
{
	this->V = V; // creating the intance of V
	adj = new list<int>[V];

}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);  //Add w to v's list.
}

void Graph::DFSrecursive(int v, bool visited[])
{
	//print the current node and mark it as visited.

	visited[v] = true;
	cout << v << " ";

	//do this for all the adjacent vertices of v.

	list<int>::iterator i;

	for (i = adj[v].begin(); i != adj[v].end(); ++i)
	{
		if (!visited[*i])
		{
			DFSrecursive(*i, visited);
		}
	}
}

//DFS traversal of the vertices reachable from the current node v.
//It uses recurcive DFSrecursive() Function.

void Graph::DFS(int v)
{
	//first mark all the vertices as not visited.

	bool *visited = new bool[V];

	for (int i = 0; i < V; i++)
	{
		visited[i] = false;

		//Call the recursive helper function to print DFS traversal.
		DFSrecursive(v, visited);


	}

}

//Driver code.

int main()
{

	// Create a graph given in the above diagram
	Graph g(4);
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEdge(1, 2);
	g.addEdge(2, 0);
	g.addEdge(2, 3);
	g.addEdge(3, 3);

	cout << "Following is Depth First Traversal"
	     " (starting from vertex 2) \n";
	g.DFS(2);

	return 0;
}
