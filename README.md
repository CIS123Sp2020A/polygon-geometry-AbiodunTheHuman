# More on Inheritance - Polygon Geometry 

## Instructions
- You will write a program that creates a base class Polygon with the following details:
   - class Polygon 
      - Parameterized constructor which takes num_of_sides as a parameter   
      - attributes: 
         - n(integer) refers to the number of sides for the polygon
         - sides(list) containing the lengths of each side of the polygon object
      
      - methods: 
         - findPerimeter
            - takes as input the sides of the polygon and outputs the polygon's perimeter
        - dispSide
            - displays the length for each side
            
   - 3 subclasses
      - appropriate methods for finding the area and perimeter
      - str method: prints properties of the polygon subclass
      
You should create an instance of your subclasses and print the details using your str class method. 
```Example: 
Enter the length of a side : 1
Enter the length of another side : 2
Side 1 is 1.0
Side 2 is 2.0
Side 3 is 1.0
Side 4 is 2.0
The area of the rectangle is 2.00
This rectangle has 4 sides and has 4 right angles.
This rectangle has sides with lengths [1.0, 2.0, 1.0, 2.0]

Enter the length of a side : 1
Side 1 is 1.0
Side 2 is 1.0
Side 3 is 1.0
Side 4 is 1.0
The area of the square is 1.00
This has 4 sides that are all of equal length and 4 right angles
This square has sides with lengths [1.0, 1.0, 1.0, 1.0] 

Enter the length of a side : 3
Side 1 is 3.0
Side 2 is 3.0
Side 3 is 3.0
Side 4 is 3.0
Side 5 is 3.0
Side 6 is 3.0
The area of the hexagon is 23.38
This regular hexagon has 6 sides.
This regular hexagon has sides with lengths [3.0, 3.0, 3.0, 3.0, 3.0, 3.0] 
```

### Helpful Resources if your math has slipped you :):

[How to Calculate the Area of a Polygon](https://www.wikihow.com/Calculate-the-Area-of-a-Polygon#targetText=To%20find%20the%20area%20of%20a%20regular%20polygon%2C%20all%20you,is%20perpendicular%20to%20that%20side)

[Finding the Perimeter and Area](https://www.montereyinstitute.org/courses/DevelopmentalMath/COURSE_TEXT2_RESOURCE/U07_L2_T2_text_final.html)
