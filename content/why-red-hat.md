---
title: Why I Joined Red Hat
date: 2022-08-17
---

After getting laid off [LINK], I was on the job hunt.
Honestly, I wasn't sure what I was looking to do next.
Maybe something not directly related to Kubernetes, maybe some sort of SaaS.
I interviewed with a bunch of companies, got rejected by some, opted not to go very far with others, and ultimately had 3 offers to choose from.

My first was with a company that builds an open source "search engine database."
I know nothing about AI/machine learning, so while the thought of working on a database was cool, I couldn't really judge the merits of the core product.
Luckily, the position wasn't directly for the core database, but rather building up a SaaS offering for it.

What struck me about this company was that the CTO reached out with a very personal email that demonstrated he'd actually done some research on me beyond skimming my resume.
Often, people recruiting will say someone "looks like a great fit" by looking for some key words in their experience, only to reject the candidate for poor fit later; this happened to me with at least one company.
In light of that, getting a personal email was great.
Admittedly, the idea of running a SaaS on Kube to bundle up some open source project wasn't exactly what I had in mind for my next thing, but the whole team proved to be great.
Talking with all of them, they truly believed in open source, remote/asynchronous work, and autonomy within the team.
Still, I was left uneasy about not being able to evaluate the core product.
It did not help that most of the team was in Europe.
I'm totally fine with them living there, but the timezone difference meant that working asynchronously would be somewhat lonely for the foreseeable future.


My initial choice was actually a leading cybersecurity company.
They had some neat technology for detecting threats present on a system and ingested a _lot_ of data, something like a trillion points a day.
A friend reached in response to a twitter post, and told me about a new team he'd joined.
They were going to be using all that data to do proactive security, and it was all greenfield within the company.
Building brand new systems is like catnip for lots of programmers, and I'm no exception.
This was actually a super hard decision - I debated for days between this and Red Hat, before I even had a formal offer.
Working with so much data was a new thing to me in general, and it was kind of exciting to think about tackling a different domain.
That was also my fear, though - I didn't have direct past experience to leverage.
Sure, I've worked with Kubernetes projects that are distributed and did my best to run at scale, but I never ran them in production.
Such a large amount of data was also super intimidating.

The real deciding factor, though, was the chance to work on something open source again.

While the security company used open source software a lot, contributing wasn't really seen as core to the company.
If it fixed a problem they were having with Kafka or Zookeeper, awesome - go ahead and contribute.
Making a library or utility open source was largely up to the engineers to drive with legal, though.
And this all makes sense, I don't want to say that they're wrong.
But that friction was an itch that stayed in the back of my mind.

Red Hat, of course, is pretty famously built on open source.
They initially gave away the same product they charged for in Red Hat Linux, which was of course not a great long term strategy.
But how they chose to course correct was important.
They didn't just create a subscription-based offering in Red Hat Linux, they introduced the Fedora Project to drive innovation upstream.
Businesses could get the stability, testing, and longevity guarantees needed, and the open source community got to experiment with ideas and the latest packages.
They even let the CentOS team create a downstream, rebranded version of their flagship product without interfering for years.
The CentOS project was repurposed, but the original legacy lives on in Rocky Linux and _[FIND OTHER LINUX}_.
Finally, they're a big contributor to Linux device drivers.
Because they're looking to sell subscriptions for a long time, they need to be sure that the hardware RHEL runs on works well with Linux.
And most of those changes land directly in the kernel, letting everyone benefit.

Beyond a Linux distribution, Red Hat entered other spaces with JBoss, OpenStack, and Ansible.
They were amongst the first companies to start working with Kubernetes outside of Google.
And most projects they made outside of SaaS were open source first, with a subscription-based model on top.


That's the same approach with the KCP project [LINK].
KCP is an attempt to take the Kubernetes API server approach and apply it to managing Kubernetes clusters.
A KCP server/cluster will handle scheduling deployments and Custom Resource Definititions onto Kubernetes clusters much like Kubernetes abstracts scheduling an application to a specific server.
While the API is very similar, the number of built in types is fewer than Kubernetes to simplify the codebase.
Most types added are actually Custom Resource Definitions rather than built-ins.

A former coworker was on the KCP team, and they happened to be looking for a couple more team members.
At first I was reluctant, since it was More Kuberenetes.
However, the project is fairly new, and contributing a lot of improvements they're making back into upstream Kubernetes, such as API machinery work.
(Though they're _not_ contributing some things, like the code needed to make logical clusters/workspaces work.)
The fact that I could leverage the last few years of my work life was tempting, as it made me more confident in what I can deliver for the team.
Plus, I've tried to get into Red Hat multiple times.
I'd just never had someone on the inside who was close enough to my target team to help me get beyond the initial resume screening.

So that's largely it - Red Hat truly operates with open source as a priority to the company, and there was a good opening in a domain and community I'm already familiar with.
As it turns out, that was way more important to me than I even knew, but after spending a few months working primarily on closed source code, I'm excited to get back into the open.
