### A program for a very absurd Interview Question

This program is the answer to a random but very absurd question I saw on the web.

The question is - If you have a function called random() which returns a ramdom float value in range (0,1), what is the value of Pi (π)? <br>
The answer is in the following explaination - 
Consider a plane with x and y axis each of units 1 and let's assume that random() uses the parameters x and y to plot random points in the plane. Replicate this plane four times to make it a square in the 2D plane. Now we input a circle inside this square in which all the sides of the sqaure are tangent to the circle. We find out the total number of points inside the square and the total number of points inside the circle alone. If we connect one random point insde the circle to the center of the circle, we get the distance of the point from the origin. So we find the ratio of the number of points in the circle to the total number of points in the square and multiply it by 4. <br>`πr^2/(2r)^2`<br> Using the mentioned formula, we calculate the ratio which is nothing but the value of π 

![image]()
![image]()
