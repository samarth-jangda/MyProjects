size(500,500);
background(255);
float xLoc;
xLoc = width/5;
float yLoc = height/5;
strokeWeight(5);
fill(0,0,255);
//ellipse(250,250,100,100);

//strokeWeight(2);
//line(0,250,500,250);
xLoc = 143;
yLoc = 342;
ellipse(xLoc,yLoc,100,100);
line(xLoc,yLoc-50,xLoc,yLoc+50);
line(xLoc-50,yLoc,xLoc+50,yLoc);
