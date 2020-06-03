#include<bits/stdc++.h>
using namespace std;

struct Point
{
	int x,y;

};

//following function simply calculates the slope of the line (orientation of the ordered triplet p,q and r).

int slope(Point p,Point q, Point r)
{
	int val = (q.y - p.y)*(r.x - q.x) - 
	          (q.x-p.x)*(r.x-q.y);

	if(val == 0) return 0; //if the points are colinears
	return (val > 0)? 1: 2; //ternary operator. 
}

//
void convexHull(Point points[], int n) 
{ 
    // works only if there are atleast 3 points. 
    if (n < 3) return; 
  
    // Initialize Result 
    vector<Point> hull; 
  
    // Find the leftmost point 
    int l = 0; 
    for (int i = 1; i < n; i++) 
        if (points[i].x < points[l].x) 
            l = i; 
  
    // Start from leftmost point, keep moving counterclockwise 
    // until reach the start point again.  This loop runs O(h) 
    // times where h is number of points in result or output. 
    int p = l, q; 
    do
    { 
        // Add current point to result 
        hull.push_back(points[p]); 
  
        // Search for a point 'q' such that orientation(p, x, 
        // q) is counterclockwise for all points 'x'. The idea 
        // is to keep track of last visited most counterclock- 
        // wise point in q. If any point 'i' is more counterclock- 
        // wise than q, then update q. 
        q = (p+1)%n; 
        for (int i = 0; i < n; i++) 
        { 
           // If i is more counterclockwise than current q, then 
           // update q 
           if (slope(points[p], points[i], points[q]) == 2) 
               q = i; 
        } 
  
        // Now q is the most counterclockwise with respect to p 
        // Set p as q for next iteration, so that q is added to 
        // result 'hull' 
        p = q; 
  
    } while (p != l);  // While we don't come to first point 
  
    // Print Result 
    for (int i = 0; i < hull.size(); i++) 
        cout << "(" << hull[i].x << ", "
              << hull[i].y << ")\n"; 
} 


// this main function run and tests all the functions.
int main() 
{ 
    Point points[] = {{0, 3}, {2, 2}, {1, 1}, {2, 1}, 
                      {3, 0}, {0, 0}, {3, 3}}; 
    int n = sizeof(points)/sizeof(points[0]); 
    convexHull(points, n); 
    return 0; 
} 
