# Contributing to KilimoGuard Backend

This guide will help you understand our workflow and how you can contribute effectively.

## Branch Structure

### Main Branches
- **develop**: Default branch for development. All pull requests should be merged here.
- **main**: Production-ready code. Only thoroughly tested and reviewed code from `develop` gets merged here.

### Feature Branches
- Create a new branch for each feature or bug fix. Use the following naming conventions:
  - `feature/feature-name`
  - `bugfix/bug-description`

### Hotfix and Release Branches
- **Hotfix Branches:** For critical fixes in production, branch from `main`. Example: `hotfix/critical-issue`.
- **Release Branches:** For major releases, create a branch from `develop`. Example: `release/v1.0`.

## Workflow

1. **Starting a New Feature:**
   - Create a new branch from `develop`: `feature/your-feature-name`.
   - Make small, frequent commits with clear messages.

2. **Opening a Pull Request (PR):**
   - Push your branch to GitHub and open a PR to merge into `develop`.
   - Ensure your code is well-documented and tested.

3. **Code Reviews:**
   - At least one other team member must review the PR before merging.
   - Address any feedback and make necessary changes.

4. **Merging PRs:**
   - After approval, merge the PR into `develop`.

5. **Testing and Releases:**
   - Regularly test the `develop` branch.
   - For a new release, create a release branch: `release/v1.0` from `develop`.
   - Perform final testing and bug fixing on the release branch before merging into `main`.

6. **Hotfixes:**
   - For critical production issues, create a hotfix branch from `main`: `hotfix/critical-issue`.
   - Fix the issue, open a PR, and merge after review and testing.
   - Merge the hotfix branch into `develop` to include the fix in future development.

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


## Contribution Guidelines

- **Issues:** Use GitHub Issues to track tasks, bugs, and feature requests. Assign issues to team members and link them to PRs.
- **Commits:** Make small, frequent commits with clear messages. This helps in tracking changes and understanding the history.
- **Documentation:** Keep documentation up to date with changes in code. This includes README files, API documentation, and inline code comments.

## Collaboration Tools

- **GitHub Projects:** We use GitHub Projects to track progress with a Kanban board.
- **Continuous Integration (CI):** We have a CI pipeline set up with GitHub Actions to automatically run tests and checks on each PR.

By following this workflow, we can ensure a smooth and efficient development process. If you have any questions or suggestions, feel free to open an issue or contact a team member.

Thank you for contributing!
