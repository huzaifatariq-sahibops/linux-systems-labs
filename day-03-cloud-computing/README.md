# Day 3 — Cloud Computing Models

## Objective

Distinguish common cloud service models and connect the responsibility boundaries to a small Bash program with success and failure paths.

## Learning-source scope

The concept diagnostic for this milestone was grounded in the official Miseacademy Day 3 portal questions for **Introduction to Cloud Computing**. The separate trainer video was blocked by YouTube's automated bot check, and the presentation required an authorized Google session. This page therefore does not claim full coverage of the trainer's video or slides.

## Key models

### On-premises

The organization directly manages the physical hardware, networking, operating system, runtime, applications, and data.

### Infrastructure as a Service (IaaS)

The provider supplies the underlying infrastructure. The customer normally manages the operating system, runtime, applications, and data.

**Memory line:** I manage from the OS upward.

### Platform as a Service (PaaS)

The provider manages the infrastructure, operating system, and runtime. The customer deploys application code and manages its data.

**Memory line:** I bring the code; the platform runs it.

### Software as a Service (SaaS)

The provider supplies the complete application platform. The customer uses and configures the application and remains responsible for appropriate users, access, and data handling.

**Memory line:** I use the finished software.

## Bash responsibility checker

The script accepts one model and prints the simplified provider/customer responsibility boundary:

```bash
./cloud-model-check.sh on-prem
./cloud-model-check.sh iaas
./cloud-model-check.sh paas
./cloud-model-check.sh saas
```

It normalizes its argument to lowercase, selects a branch with `case`, and rejects unsupported input:

```bash
./cloud-model-check.sh unknown
echo "Exit code: $?"
```

The invalid input produces usage guidance and exits with status `2`. A non-zero exit status allows a person or another program to detect that the command did not complete successfully.

## Syntax versus behavior

```bash
bash -n cloud-model-check.sh
```

`bash -n` parses the script without executing its commands. It can detect malformed Bash structure, such as unmatched quotes or a missing terminator, but it cannot prove that the definitions or program logic are correct. Running all four supported arguments and one unsupported argument tested the actual behavior.

**Memory line:** `bash -n` checks whether Bash can read it—not whether the script does the right thing.

## Verified result

- The script passed the Bash syntax check.
- All four supported models selected the expected branch.
- Unsupported input displayed usage guidance.
- The unsupported input path returned exit code `2`.
- A practical-understanding check confirmed the difference between valid syntax and correct logic.

See the [sanitized terminal evidence](evidence/terminal-output.txt).

## Scope and limitations

The displayed boundaries are a beginner-friendly model. Real cloud security remains a shared responsibility: customers still control areas such as identities, access, configuration, and their data even when the provider manages more of the technology stack.

This script is a learning artifact, not a cloud deployment or a claim of professional cloud-engineering experience.

## AI assistance disclosure

I created and ran the script in my Ubuntu/WSL environment and supplied the terminal output. SAHIB, my AI learning assistant, provided the guided exercise, checked my understanding through MCQs, helped sanitize the evidence, and structured this documentation.
