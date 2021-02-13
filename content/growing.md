# Growing as a software engineer

I've recently taken on my first tech lead role, and I've been taking time to reflect on what that means.
I think a huge part of being a tech lead is growing your team, and recently I got the question, "How do I know what subject areas are available? What should I do in order to get promoted into more senior positions?"

My opinion is that a huge part of moving up in seniority is being able to deal with ambiguity.
It's also identifying these subject areas for one's self and then making sure they're addressed.
If I combined them, I think I'd summarize it like this:

> Asking questions about observed problems and proposing solutions is part of being an engineer.
> Becoming more senior means dealing with broader areas of ambiguity, adequately defining and breaking down the problems, then looking for solutions.

When you start as a programmer, your ambiguity is often down at the level of lines of code.
Someone will have outlined how the overall program will work, but it's your job to make the code fit that solution.
How do I write this loop efficiently?
What functions do I need to isolate the feature into understandable pieces?
How can I name my variables so they're understandable when I come back to this after a year of not touching it?
How do I write tests that I don't have to explain them to others in person?

As you move up to the middle of your career, you start looking at the program in larger components.
You may work with a tech lead or architect to decompose diagrams into discrete chunks.
What modules or packages should you organize the program into so that many functions or data structures that are related are grouped logically?
Can you avoid making a dumping ground module like `utils` or `helpers`?
How do you make the whole programmer faster? How do modules, packages, plugins, and external APIs interact together?

Some of this work starts to overlap with architecture.
You'll start diagramming multiple programs talking to each other, and focusing less on how each one works down to a single line.
Product managers and other leaders will start asking you for solutions to customer problems, which will require communicating with less technical audiences in a clear manner and translating their requests into a program that other programs can then implement.
Can you make that diagram easier to understand for the customer, and also ones that help the team understand the technical outcome?
What parts are you going to delegate and to whom?
Which people on your team have demonstrated the ability to break down segments of a problem, and who needs help getting there?

You'll notice here that the questions start to involve working with people rather than strictly code.
Drawing diagrams, writing design docs, and whitepapers.
Convincing others that your framing of the problem and the corresponding solution are the right one, as well as seeking out and integrating feedback.
This is intentional - a technical leader starts dealing less with the code directly and instead working with systems and how people interact with them.
The output in the end will likely be a program, sure but it's the job of a technical leader to ensure it's the *right* program, just as a junior developer would strive to make the right function.
It is *also* the technical leader's job to grow their team, along with the engineering manager.
Growing the team is good for the program itself, giving it different perspectives and injecting new ideas.
It's also good for the project as people's individual career goals change and they move between jobs or teams.
The knowledge is less isolated in one person, and the "bus factor" is reduced.
This is good for both community open source projects as well as businesses, which need continuity even as the entire original team is replaced.

---
You can also visual this process as a series of nested blocks.
At each level, you're filling in the unknowns of a slightly larger box.
At the highest levels, you begin defining whole new boxes by identifying gaps in current processes or tooling.
Things like Linux, Rails, Kubernetes, Rust, and pretty much any major codebase you've heard of has done this.
The authors saw some problem in the world, explored the domain, broke the problem down into smaller ones, and implemented binaries, libraries, or frameworks that provided an opinion on how the problem should be addressed.

---

This is my particular take on how to grow technically, reflecting on my own career path, as well as observing and talking to others.
For other people's thoughts and perspectives, I'd highly recommend [Lauri Apple's](https://twitter.com/Moinmoinapfel) [Awesome Leading and Managing list](https://github.com/LappleApple/awesome-leading-and-managing) for ideas from a lot of different folks.
I've also been recommended The Manager's Path by [Camille Fournier](https://twitter.com/skamille), though I've not yet read it.
When I asked for input on twitter, I was also pointed to Becoming a Technical Leader: An Organic Problem Solving Approach by Gerald M. Weinberg.
Finally, I'd like to thank Joe Beda for sharing some of his thoughts on technical leaders and their role with me.