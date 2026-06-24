# PawPal+ Project Reflection

## 1. System Design

Core Actions:
- Add a pet
- See tasks and appointments for the day 
- Track a pet's diet

Classes:
- Pet class
    - Stores information about the pet
    - Ability to update the pet's weight, age, etc
- Scheduler class
    - Stores information about tasks and appointments
    - Ability to create, update, and delete tasks/appointments for a specific pet
- Diet tracker class
    - Stores information about the pet's diet over time
    - Ability to set and retrieve nutrition info (e.g. caloric)
- Recommendations class
    - Synthesizes the information to give recs and then gives an explanation for those recs
    - E.g. feed the dog or reminder for an appointment

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I included 5 classes: Task, Scheduler, Pet, Owner, and Recommendation. Owner and Pet are pure data classes, with an owner holding one or more pets. Task is also a data class holding the details of a scheduled activity, including its name, description, duration, priority, date range, and optional recurring days. Scheduler is a generic service class — rather than being tied to a specific pet, it takes a petId as a parameter on each method, allowing it to create, update, delete, and query tasks for any pet. Recommendation is a combined data and logic class that holds the result of a recommendation (text, explanation, category) and exposes a static generate() method that takes a pet and its tasks to produce relevant suggestions.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

Yes, 

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
