# Contribution Guidelines

This guidelines are for team members only. Below are the guidelines to help you get started.

## Getting Started
1. **Clone the repository**: Clone your forked repository to your local machine using the following command:
   ```sh
   git clone https://github.com/KilimoGuard/kilimoGuard_Backend.git
   ```
3. **Create a branch**: Create a new branch for your feature or improvement or bugfix. Use a descriptive name for your branch.   
- Please use following branch name conventions:-
- When adding a new feature:-
   ```sh
   git checkout -b ft-your-feature-name
   ```
- When improving on existing code:-
   ```sh
   git checkout -b ch-your-feature-name
   ```
- When fixing a bug:-
   ```sh
   git checkout -b bg-your-feature-name
   ```

## Making Changes

1. **Install dependencies**: Install the necessary dependencies for the project. Ensure you are in the project directory.
   ```sh
   pip install -r requirements.txt
   ```
2. **Make your changes**: Implement your feature or fix the bug. Ensure your code follows the project's coding style and conventions.
4. **Commit your changes**: Write clear and concise commit messages.
   ```sh
   git add .
   git commit -m "Add feature/fix for ..."
   ```

## Pushing Changes

Before pushing any change to the repository:-
1. Please make sure you have no uncommited code.
2. Checkout to main branch and pull it to update it.
3. Once done, checkout to your branch and rebase it with main branch. Use the command below to rebase:-
   ```sh
   git rebase main   
   ```
4. Resolve any merge conflicts and then push your branch to the repository.
   ```sh
   git push origin bg-your-feature-name
   ```

## Submitting a Pull Request

1. **Create a pull request**: Go to the repository and click on the "Pull Request" button. Provide a clear and descriptive title for your pull request. In the description, explain what changes you have made and why. Make sure add a reviewer from the top right section.
2. **Review process**: The reviewer will review your pull request. They may ask for changes or provide feedback. Please be responsive to their comments.
3. **Merge**: Once your pull request is approved, it will be merged into the main branch.

## Questions?

If you have any questions or need further guidance, feel free to open an issue or reach out to the project maintainers.

Happy coding!

Peter Mirithu.