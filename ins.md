# macOS Secret Hygiene and 1Password-Only Setup

Goal: remove local secrets from your Mac and ensure all credentials come from 1Password (CLI + SSH agent). Follow top-to-bottom; skip anything that doesn’t apply.

## Part A — Remove any local secrets from the Mac

- Keychain (UI)
  - Open “Keychain Access” and delete saved items for:
    - github.com, AWS, npm, Docker, gcloud, Azure, Heroku
    - any “git:https://…” entries
    - any personal access tokens (PATs) or API tokens

- Git credential helpers
  ```bash path=null start=null
  # Show configured credential helpers (if any)
  git config --global --get-all credential.helper

  # Remove all global helpers to avoid caching plaintext tokens
  git config --global --unset-all credential.helper || true
  ```

- AWS CLI
  ```bash path=null start=null
  # List configured profiles (sanity check)
  aws configure list-profiles 2>/dev/null || true

  # Delete static credentials from disk
  rm -f ~/.aws/credentials

  # Optional: back up config if it contains anything sensitive, then trim
  cp -n ~/.aws/config ~/.aws/config.bak 2>/dev/null || true
  ```

- GitHub CLI (gh)
  ```bash path=null start=null
  gh auth logout -h github.com --hostname github.com --all
  rm -f ~/.config/gh/hosts.yml
  ```

- npm
  ```bash path=null start=null
  npm logout 2>/dev/null || true
  rm -f ~/.npmrc
  ```

- Docker
  ```bash path=null start=null
  docker logout 2>/dev/null || true
  rm -f ~/.docker/config.json
  ```

- Google Cloud / Azure / Heroku (if used)
  ```bash path=null start=null
  gcloud auth revoke --all 2>/dev/null || true
  rm -rf ~/.config/gcloud

  az logout 2>/dev/null || true

  heroku auth:logout 2>/dev/null || true
  ```

- SSH private keys on disk
  1) Import your SSH keys into 1Password (Developer → SSH Keys).
  2) Then remove local copies you no longer want stored on disk.
  ```bash path=null start=null
  ls -la ~/.ssh
  # After import into 1Password:
  # rm -f ~/.ssh/id_ed25519 ~/.ssh/id_ed25519.pub
  # rm -f ~/.ssh/id_rsa ~/.ssh/id_rsa.pub
  ```

- Generic secret files
  ```bash path=null start=null
  # Find likely secret files under $HOME
  find ~ -type f \( -name ".env" -o -name ".env.*" -o -name "*.pem" -o -name "*.key" -o -name "*.p12" -o -name "*.pfx" -o -name "*.cer" -o -name "*.crt" -o -name ".pypirc" -o -name ".npmrc" \) 2>/dev/null

  # Review the list, then delete any that contain secrets.
  ```

- Shell/environment leakage
  ```bash path=null start=null
  # Search for exported secrets in shell config files
  grep -nEi 'AKIA|ASIA|ghp_|github_pat_|xox|AWS_(ACCESS|SECRET)_KEY|SECRET|TOKEN|PRIVATE_KEY' \
    ~/.zshrc ~/.zprofile ~/.zshenv ~/.bash_profile ~/.bashrc 2>/dev/null || true

  # Manually remove any lines that export secrets.
  ```

- Shell history (only if you pasted secrets into the terminal)
  ```bash path=null start=null
  cp -n ~/.zsh_history ~/.zsh_history.bak 2>/dev/null || true
  sed -i '' -E '/AKIA|ASIA|ghp_|github_pat_|xox|AWS_(ACCESS|SECRET)_KEY|SECRET|TOKEN|PRIVATE_KEY/d' ~/.zsh_history 2>/dev/null || true
  ```

## Part B — Ensure Git and SSH use 1Password only

- Enable 1Password integrations
  - 1Password → Settings → Developer:
    - Check “Integrate with 1Password CLI”
    - Check “Use SSH agent”

- Install the CLI
  ```bash path=null start=null
  brew install 1password/tap/1password-cli
  op --version
  ```

- Use 1Password SSH agent for GitHub
  ```bash path=null start=null
  # Prefer SSH remotes (no HTTPS passwords needed)
  git remote -v

  # If needed, switch to SSH:
  # git remote set-url origin git@github.com:<owner>/<repo>.git
  ```

- Optional: commit signing via SSH (no GPG keys on disk)
  ```bash path=null start=null
  git config --global gpg.format ssh
  # Use your public key that 1Password manages (path here is illustrative)
  git config --global user.signingkey ~/.ssh/id_ed25519.pub
  git config --global commit.gpgsign true
  ```

## Part C — Make CLIs pull credentials from 1Password

- SSH-only for GitHub/Git
  - Use the 1Password SSH agent; no tokens needed.

- AWS via environment on demand
  - In 1Password, create an item with fields:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_SESSION_TOKEN (if using sessions)
    - AWS_REGION
  - Inject for a single command:
    ```bash path=null start=null
    export AWS_ACCESS_KEY_ID="$(op read op://<Vault>/<Item>/AWS_ACCESS_KEY_ID)"
    export AWS_SECRET_ACCESS_KEY="$(op read op://<Vault>/<Item>/AWS_SECRET_ACCESS_KEY)"
    export AWS_SESSION_TOKEN="$(op read op://<Vault>/<Item>/AWS_SESSION_TOKEN)"  # if applicable
    export AWS_REGION="$(op read op://<Vault>/<Item>/AWS_REGION)"

    aws sts get-caller-identity
    ```
  - Or keep a dotenv file with op:// references and run through 1Password:
    ```bash path=null start=null
    # .env contains:
    # AWS_ACCESS_KEY_ID=op://<Vault>/<Item>/AWS_ACCESS_KEY_ID
    # AWS_SECRET_ACCESS_KEY=op://<Vault>/<Item>/AWS_SECRET_ACCESS_KEY
    # AWS_SESSION_TOKEN=op://<Vault>/<Item>/AWS_SESSION_TOKEN
    # AWS_REGION=op://<Vault>/<Item>/AWS_REGION

    op run --env-file .env -- aws s3 ls
    ```

- GitHub CLI (gh) using SSH
  ```bash path=null start=null
  gh auth login  # choose SSH; with 1Password SSH agent, no PAT is needed
  ```

- npm
  ```bash path=null start=null
  # Store your token in 1Password and export only when needed:
  export NPM_TOKEN="$(op read op://<Vault>/<Item>/NPM_TOKEN)"
  npm whoami --registry=https://registry.npmjs.org/
  # Avoid a persistent ~/.npmrc containing _auth tokens.
  ```

## Part D — Repo hygiene (prevent future leaks)

- .gitignore should include at least:
  ```text path=null start=null
  .env
  .env.*
  *.pem
  *.key
  *.p12
  *.pfx
  *.cer
  *.crt
  *.der
  .pypirc
  .npmrc
  .DS_Store
  ```

- Scan your repo locally (belt-and-suspenders)
  ```bash path=null start=null
  grep -RInE 'AKIA[0-9A-Z]{16}|ASIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,}|xox[baposrt]-[A-Za-z0-9-]{10,}|AIza[0-9A-Za-z_-]{20,}|AWS_(ACCESS|SECRET)_KEY|SECRET[_-]?KEY|PRIVATE KEY|BEGIN CERTIFICATE' .
  ```

## Optional help I can provide

- Generate exact op:// paths for your 1Password items and wire a `.env.example` for this repo.
- Switch any remaining HTTPS Git remotes to SSH and verify the 1Password SSH agent is authenticating and (optionally) signing commits.
- Run a focused scan on your Mac and produce a short list of files to delete or rotate.
