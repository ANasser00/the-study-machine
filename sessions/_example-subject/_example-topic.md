# Session: Newton's Laws of Motion

**Subject:** Classical Mechanics
**Date:** 2026-03-10
**Source material:**
- [x] Transcript: `content/classical-mechanics/transcripts/lecture-03-newtons-laws.txt`
- [x] Slides: `content/classical-mechanics/slides/lecture-03.pdf`
- [x] Past exams: `content/classical-mechanics/pdfs/exam-2024.pdf`
- [ ] Notes:

**Status:**
- [x] Phase 1 — Understanding
- [x] Phase 2 — Exam Gold
- [x] Complete

---

## Phase 1 — Understanding

Worked through Newton's three laws with Claude. Started with the intuition before going formal.

**First Law (Inertia)** — The analogy that clicked: imagine a hockey puck on ice with no friction. Once sliding, it keeps sliding forever in a straight line because nothing is pushing it sideways or slowing it down. The "natural state" of an object is not rest — it is whatever it was already doing. Rest is just a special case where it was already at zero velocity. This reframing was important because my instinct had always been that objects "want" to stop.

**Second Law (F = ma)** — Force is what causes acceleration, not velocity. Pushing harder on a shopping cart accelerates it more. A heavier cart accelerates less for the same push. Worked through a quick exercise: if a 2 kg block has 10 N applied, acceleration = 10/2 = 5 m/s². Felt comfortable with this immediately.

**Third Law (Action-Reaction)** — The part that kept tripping me up: if every force has an equal and opposite reaction, why does anything move? Claude's clarification: the two forces act on *different objects*. When you push off a wall, the wall pushes back on *you* — those forces are on different bodies, so they don't cancel. The net force on *you* is the wall's push, so you accelerate away.

Also covered inertial vs. non-inertial reference frames briefly. Laws only hold cleanly in inertial frames. In a car accelerating forward you feel pushed back — that is a pseudo-force, not a real force.

Confirmed ready for Phase 2 after working through three practice problems from the 2024 exam paper.

---

## Phase 2 — Exam Gold

### Key Concepts

- **First Law**: An object at rest stays at rest; an object in motion stays in motion at constant velocity — unless a net external force acts on it. Inertia is the resistance to change in velocity.
- **Second Law**: Net force equals mass times acceleration: F_net = ma. Force and acceleration are vectors. Doubling force doubles acceleration. Doubling mass halves acceleration for the same force.
- **Third Law**: For every action force there is an equal and opposite reaction force, acting on a *different* object. Forces always occur in pairs; they never cancel each other because they act on different bodies.
- **Net force**: What matters is the *sum* of all forces on an object. If forces balance (net force = 0), acceleration = 0, meaning constant velocity (including rest).
- **Inertial reference frames**: Newton's laws hold exactly only in non-accelerating reference frames. In accelerating frames, fictitious (pseudo) forces appear (e.g. the feeling of being pushed back in an accelerating car).
- **Weight vs. mass**: Mass is a scalar measure of inertia (kg). Weight is the gravitational force on that mass: W = mg. They are not the same thing and change differently in different gravitational fields.
- **Free body diagrams**: Always isolate one object, draw all forces acting *on it*, and sum them vectorially to find net force before applying F = ma.

---

### Active Recall Questions

| # | Question | Difficulty | Last Reviewed | Next Review |
|---|----------|------------|---------------|-------------|
| 1 | State Newton's First Law and explain what "inertia" means in one sentence. | Medium | 2026-03-11 | 2026-03-14 |
| 2 | A 5 kg crate is pushed with 20 N on a frictionless surface. What is its acceleration? | Easy | 2026-03-11 | 2026-03-18 |
| 3 | Newton's Third Law says every action has an equal and opposite reaction. Why doesn't this mean nothing ever accelerates? | Hard | 2026-03-11 | 2026-03-12 |
| 4 | What is the difference between mass and weight? Give units for each. | Medium | 2026-03-11 | 2026-03-14 |
| 5 | An object moves at constant velocity. What can you conclude about the net force acting on it? | Easy | 2026-03-11 | 2026-03-18 |
| 6 | You are standing in an elevator that accelerates upward. You feel heavier. Explain this using Newton's laws without invoking "gravity got stronger." | Hard | 2026-03-11 | 2026-03-12 |
| 7 | Describe the steps for solving any Newton's Second Law problem. | Medium | 2026-03-11 | 2026-03-14 |

<details>
<summary>Answers</summary>

**Q1:** An object continues in its current state of motion (at rest or moving at constant velocity) unless a net external force acts on it. Inertia is an object's resistance to any change in its velocity.

**Q2:** F = ma, so a = F/m = 20/5 = 4 m/s².

**Q3:** The two forces act on *different objects*. When you push a wall, the wall pushes back on you — one force is on the wall, the other is on you. They act on separate bodies so they cannot cancel. The net force on *you* is the wall's push, which is why you accelerate away.

**Q4:** Mass is the measure of how much matter an object contains and is its resistance to acceleration. Unit: kilogram (kg). Weight is the gravitational force acting on that mass: W = mg. Unit: Newton (N). On the Moon, mass is unchanged but weight is about 1/6 of Earth weight because g is smaller.

**Q5:** If velocity is constant, acceleration is zero. By F = ma, net force = 0. All forces are balanced — this does not mean there are no forces, only that they sum to zero.

**Q6:** Your true weight (gravitational pull) acts downward. The elevator floor exerts a normal force upward. When the elevator accelerates upward, the net upward force must be positive, so the normal force must *exceed* your gravitational weight. It is that larger normal force from the floor that you feel as heaviness — not a change in gravity. Using F_net = ma: N - mg = ma, so N = m(g + a).

**Q7:** 1. Identify the object and draw a free body diagram showing all forces on it. 2. Set up a coordinate system. 3. Sum all force components along each axis. 4. Apply F_net = ma along each axis separately. 5. Solve for the unknown. 6. Check units and sign conventions.

</details>

---

### Weak Spots

- **Action-reaction pairs on different objects**: Keep confusing myself about why things still accelerate. Need to explicitly label which object each force acts on in every problem.
- **Non-inertial reference frames and pseudo-forces**: The elevator problem is manageable but I get confused as soon as rotation is involved (centrifugal force as a pseudo-force). Flag for the next session.
- **Free body diagrams under time pressure**: In the exam I skipped drawing them on easy problems and made sign errors. Must always draw the diagram, even if the problem looks simple.

---

## Session Notes

The 2024 exam had two multi-part problems on Newton's Laws. Both involved inclined planes with friction — that combination was not covered in this session. Schedule a follow-up session on friction and inclined planes before the midterm. Also worth connecting this to the momentum unit: F = ma can be rewritten as F = dp/dt, which is Newton's original formulation and comes up later in the course.
