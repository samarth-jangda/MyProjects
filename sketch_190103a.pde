/* This is my first program for starting a game.
*  My name is Samarth preparing my first game.
*/

float xLoc;     // X Location (coordinate) of the centre of the ellipse.
float yLoc;     // Y Location (coordinate) of the centre of the ellipse
float diam;     // Diam of the ellipse.
// the setup of the program is always written is the starting. 
void setup()
{
  size(500,500);  //size of the ellipse
  background(255);  //background color of the screen
  
  xLoc = width/2; // x location of the ellipse
  yLoc = height/2; // y location of the elipse
  diam = 70;  // size of the diameter of the ellipse
}
// draw is the second syntax writtern in program
void draw()
{
  //xLoc = random(0,width);
  //yLoc = random(0,height);
  background(255);
  displayLogo();
  moveLogo();
}
void moveLogo()
{
 fill (0,255,0); // fill is use to fill the color in the ellipse
 xLoc = xLoc + random(-9,9);
 yLoc = yLoc + random(-9,9);
  
  
}  
void displayLogo() // it displays the ellipse
{
  float rad = diam * 0.5;  // radius of the ellipse is set to be half of the diameter
  strokeWeight(5);  // thickness of the ellipse
  ellipse(xLoc,yLoc,diam,diam); // location of the ellipse
  line(xLoc,yLoc-rad,xLoc,yLoc+rad); // size of the line 1
  line(xLoc-rad,yLoc,xLoc+rad,yLoc); // size of the line 2
  fill(0,0,255);
  ellipse(xLoc,yLoc,rad,rad);
} 
 
