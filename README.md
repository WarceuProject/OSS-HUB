# OSS HUB

Welcome to OSS HUB.

OSS HUB is a monorepo from the WarceuProject Community containing a collection of simple projects, experiments, and small open-source works.

⚠️ Note:  
This repository acts as the parent/base of all OSS HUB activities. Development in the root repository is limited. Most development happens inside each subproject directory.

---

## Languages Used

Projects inside OSS HUB may use:

- python  
- nodejs  
- perl  
- ruby  
- c / c++  
- java  
- php  
- javascript (ES)  
- flutter  

---

## Build Tools

Depending on the project:

- meson  
- cmake / GNU Make  

Each project must include its own build and run instructions inside its directory.

---

## Repository Structure

Each folder in the root directory represents a standalone project.

Example:

```
OSS-HUB/
├── project-a/
├── project-b/
└── your-feature/
```

`your-feature` = your standalone subrepository/project.

---

## Contribution Guidelines

1. Fork or clone this repository  
2. Create a new branch using **lowercase only**, no camelCase, no spaces, no special characters except `-`:

   ```
   feature/your-feature
   ```

   ❌ Examples of disallowed branch names:  
   - `Feature/MyFeature` (uppercase)  
   - `myFeature` (camelCase)  
   - `my feature` (space)  
   - `feature@123` (special characters)  

3. Create a new directory in the repository root named:

   ```
   your-feature
   ```

4. Put your project inside that directory  
5. Push your changes and open a Pull Request  
6. Wait for review  

Keep it simple. Include a README, and ensure your project builds and runs properly.

---

## Licensing

All projects submitted to OSS HUB **must use the GPL license**.  
Other licenses are not allowed.  

Include a proper `LICENSE` file in your project folder specifying the GPL version you are using.

---

## Engineering Philosophy

We prefer practical and maintainable code over unnecessary complexity.

- **YAGNI** — You Aren't Gonna Need It  
  Don’t build something until it’s actually needed.

- **DRY** — Don’t Repeat Yourself  
  Avoid duplicated logic and redundant code.

- **KISS** — Keep It Simple, Stupid  
  Simple solutions are usually better.

- **SOLID** — Basic object-oriented design principles  
  Write modular, extendable, and maintainable code.

Clean > Clever  
Readable > Smart-looking  
Working > Overengineered  

---

## Ethics & Commit Guidelines

OSS HUB is a community. We value clear, honest, and respectful contributions.

- **Commit Messages**  
  - Must be clear and descriptive.  
  - Include commit hash if referencing previous commits or issues.  
  - Commits with a joke or creative touch are appreciated 😄.  
  - Lazy or meaningless commits will be rejected.  
  - **Follow [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)** for consistency.

- **Behavior**  
  - Respect other contributors  
  - Do not spam or flood the repo  
  - Help others when possible  

- **Collaboration Mindset**  
  - Focus on learning, sharing, and improving together.  
  - Quality over quantity: better to submit one solid PR than five half-baked ones.

---

## Read More

For detailed guidelines and additional information, please read the full documentation:

👉 **[Read more](https://github.com/WarceuProject/OSS-HUB/blob/master/OSSHUB.md)**
