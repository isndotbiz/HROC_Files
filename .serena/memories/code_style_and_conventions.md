# Code Style and Conventions

## HTML/CSS/JavaScript
- **HTML**: Semantic HTML5, WCAG 2.2 Level AA accessibility compliance
- **CSS**: Single `styles.css` file, mobile-responsive design
- **JavaScript**: Vanilla JS in `script.js`, no frameworks

## File Naming
- HTML files: lowercase with hyphens or underscores
- Images: descriptive names, `.webp` preferred for web images
- Scripts: snake_case for Python, kebab-case for shell scripts

## Git Conventions
- Branch: `main` is the primary branch
- Commits: Descriptive messages describing what changed
- Never commit sensitive credentials (AWS keys, etc.) - use environment variables or `.gitignore`

## Documentation
- Markdown files (`.md`) for documentation
- Status files indicate completion state (e.g., `DEPLOYMENT_COMPLETE.md`)

## Website Assets
- Images stored on S3 CDN, referenced by full URL
- PDFs stored in `pdfs/` directory or S3
- Generated images go to `Generated_Images/` (gitignored)

## Security
- AWS credentials should be in environment variables, not hardcoded
- Sensitive files listed in `.gitignore`
