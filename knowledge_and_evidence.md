<style>

body {
    counter-reset: h2counter;
}

/* H1 - No numbering */
h1 {
    /* No counter reset or increment */
}

/* H2 - Level 1 numbering */
h2 {
    counter-reset: h3counter;
}

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}

/* H3 - Level 2 numbering */
h3 {
    counter-reset: h4counter;
}

h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) " ";
}

/* H4 - Level 3 numbering (optional) */
h4 {
    counter-reset: h5counter;
}

h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) " ";
}

</style>

# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## Required evidence

### Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![Local Execution (INSERT YOUR SCREENSHOT)](screenshots/CREATE_A_SCREENSHOT_OF_YOUR_local_setup.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name       | value          |
   | ----------              | ---------- | -------------- |
   | built-in primitive type | BLANK          |  (0,0,0)             |
   | built-in composite type | pixels         |  [(0, 0, 0), (255, 255, 0), ...]           |
   | user-defined type       | sense_hat      |  SenseHat()           |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type                    |
   | ------------             | ----------------------- |
   | self.pixels              | list                   |
   | A member of self.pixels  | tuple                  |
   | self                     | Smiley                 |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File       | First line                  | Line range  |
   | ------------ | ---------- | -----------                 | ----------- |
   |  sequence    | smiley.    | self.sense_hat = SenseHat() |12-18            | _           |
   |  selection   | sad.py     | if wide_open:               |21-25             |
   |  iteration   | happy.py   | for pixel in mouth:         |14-17                   |

   Sequence is just one line after another, like in a constructor
   selection is an if statement choosing between options
   Iterations is a for loop going through something (like pixels)

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used? | Example |
   | ----------------------- | ----- | --------|
   | int                     | yes     | 0, 255 used in rgb colors         |
   | float                   | yes     | 0.25 used in blink delay          |
   | str                     | yes     | "mock SenseHAT" in logging          |
   | bool                    | yes     | True, False (used for eyes)          |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> Your answer here
> Class variable would be 'YELLOW = (255, 255, 0)'
> Instance variable is self.pixels
Yellow is just defined outside of any method it’s a shared constant for the whole class (same for every object).
self.pixels is unique per object, each smiley you create gets its own version of pixels, so it’s an instance variable

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > Your answer here
   >The constructor __init__ is used to set up the object when it’s first made. In the Happy class, it sets up the face to look happy by drawing the mouth and eyes.

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > Your answer here
   >The `super().__init__()` call runs the constructor of the parent class (`Smiley`). That just means the LED grid and the smiley face structure get set up before we add the "happy" features on top of it

### Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:
   
> Your answer here
>The code mainly follows Pep8, which is the official python style guide. It uses clear indentation, lowercase with underscores for function names, and avoids long lines.

It’s probably not exactly the same as the real Sensehat code because
1. This code is simplified and written for teaching sensehat’s real codebase would be more complex and optimized.
2. SenseHat is maintained by pros at Raspberry pi and is more likely to include more rigorous documentation and testing


2. List three aspects of this convention you see applied in the code.

> Your answer here
>I saw snake case naming applied in the code, all function and variable names follow the python naming convention, like draw_mouth() and self.pixels
>Proper indentation is used within the code, all blocks of code are constantly indented with 4 spaces
>The 3rd aspect of this convention applied is clear method organization, methods are grouped logically by their purpose for example all drawing functions are placed together in each class

3. Give two examples of organizational documentation in the code.

> Your answer here
>Class and method docstrings are a good example, every class like smiley, happy and sad have a docstring describing what the class does.
>Inline comments are also an example of organizational documenation, you can see explanatory comments are used throughout the code, like in main.py where it says "Uncomment the lines below only if you have multi-processing issues"

### Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s) |
| ---------- | ------------- | ---------------- |
| Smiley     | Super         |   None    
|   Happy    | Sub           |   Smiley, Blinkable
   Sad       | Sub           |   Smiley
   Blinkable | Super         |   ABC         |      ...         |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Your answer here
Abstraction is about keeping things simple by hiding stuff you don’t need to see. In this project, the Smiley class is a good example. Classes like Happy don’t need to know how `set_pixels()` or the SenseHat works—they just call `show()` to display the face. It keeps the code clean and easy to use without showing all the behind-the-scenes stuff.


3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> Your answer here
>The process is called inheritance. It lets a class use methods and properties from a parent class without rewriting code. In this project, both happy and sad inherit from smiley, which means they automatically gain access to all the logic for pixel handling and screen display. This saves time and keeps the code consistent, It also lets each subclass add or override behavior, like how happy has a blink() method and a unique mouth shape, while still keeping the core display logic from smiley


### Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > Your answer here
   >The Happy class can blink, but the Sad class can’t. That’s because Happy uses another class called Blinkable, and Sad doesn’t.
2. What are the key similarities?
   > Your answer here
   >They both use the Smiley class and have similar functions like drawing the mouth and eyes.
3. What difference stands out the most to you and why?
   > Your answer here
   >The blinking. Happy looks more alive since it can blink, while Sad just stays still. It makes Happy feel more interactive.
4. How does this difference affect the functionality of these classes
   > Your answer here
   >Happy can do more since it has the blink method. Sad is limited and would need extra code if we want it to blink like Happy.

### Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > Your answer here
   >The Smiley class is the one that uses the SenseHat. It sets it up and controls what shows on the screen.
2. Which of these classes directly interact with the SenseHat functionalities?
   > Your answer here
   >Only the Smiley class talks directly to the SenseHat. The other classes like Happy and Sad just use Smiley’s functions to show stuff.
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > Your answer here
   >Encapsulation means hiding the complex stuff inside a class so other parts of the code dont need to deal with it. In this project, the SenseHat stuff is hidden inside the Smiley class. Other classes like Happy and Sad don’t have to know how it works. They just call methods like show() to display the smiley. This makes it easier to change how the Sensehat works later, without breaking the rest of the code. It also makes things neater and more organised because only one part of the code handles the hardware.


### Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> Your answer here
>No, not every smiley is meant to blink. Only the ones that use the Blinkable class are expected to blink, like the Happy smiley.


2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> Your answer here
>Yes, they should blink in a similar way. The blink method is the same across classes so the behavior is consistent, just with different expressions maybe

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Your answer here
>Polymorphism means different classes can have the same method name but do things in their own way. Like if both Happy and Sad had a blink() method, they could blink differently but still be called the same way.

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> Your answer here
>The blink method is added to the Happy class because it inherits from both `Smiley` and `Blinkable`. This lets it use `blink()` in its own way. That’s how polymorphism works—using the same method across different classes
1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![Sad Smiley Blinking](screenshots/sad_blinking.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > Your answer here

  ### If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     >Blinkable is an abstract class. It uses `ABC as its parent and has an abstract method called blink().


  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  >It’s called an interface. It’s a class that other classes are supposed to implement without giving full code.


  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  >This shows abstraction. The Blinkable class hides the actual code and just says what methods must exist, other classes can write their own version


  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > Because Python doesn’t need you to use an interface, all i did was i added the `blink()` method directly to sad and it still worked fine


  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > It’s called duck typing In Python, if something has a `blink()` method it doesn’t matter what class it’s from. In C# you need to follow strict rules and types


  ***

  ## Refactoring

  ### Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
    > The colors are defined in the `Smiley` class, these include white, green, red, yellow, and blank

     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
      > They are class variables (constants). The values are RGB tuples like (255, 255, 0) these values don’t change during the program because they’re just preset color definitions

     3. Add the color blue to the appropriate class using the appropriate format and values.

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
      > They are used in smiley, happy, and sad to draw the eyes and mouth using pixels with those colors


  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
   > Just change the YELLOW color to GREEN in the smiley class. That way everything that was yellow turns green without changing a bunch of code, but if you must change the code then just add YELLOW = (0, 255, 0) 


  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](screenshots/bulk_rename.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***
