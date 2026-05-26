# Security Baseline: content-generation-studio

## Purpose

Define the minimum security and privacy review baseline for the `content-generation-studio` software class.

## Required controls

- Identify data classes before choosing storage, auth, or integration boundaries.
- Use least-privilege access for users, services, automations, and tools.
- Validate all external input at trust boundaries.
- Log security-relevant events without exposing secrets or sensitive payloads.
- Document secrets handling, credential rotation, and local development safety.
- Define abuse cases and fallback behavior before implementation.

## Class-specific focus

This profile covers content production, review, versioning, and publishing workspace. The blueprint must map these controls to the actual raw request instead of assuming a market vertical.

## Quality gate

The Vertical Blueprint must state security assumptions, rejected unsafe defaults, and unresolved approval needs before plan and tasks.
