# Project 2: MCP-Powered Dev Tools Server

## Overview
Build a custom MCP (Model Context Protocol) server that provides useful developer tools. Publish it to npm so anyone can use it in Cursor or Claude Desktop.

## What You'll Learn
- MCP protocol (servers, clients, tools, resources)
- TypeScript development
- Publishing npm packages
- Building tools that integrate with AI assistants

## Tools to Build

### Tool 1: `analyze_codebase`
Analyze a codebase and return a structured summary (file count, languages, structure, dependencies).

### Tool 2: `check_dependencies`
Check for outdated npm/pip dependencies and suggest updates.

### Tool 3: `generate_readme`
Auto-generate a README.md based on the project structure and code.

### Tool 4: `run_lighthouse`
Run a Lighthouse audit on a URL and return performance metrics.

### Tool 5: `search_docs`
Search documentation for a given library/framework.

### Resource: `project-context`
Expose project metadata as an MCP resource that AI can read.

## Setup

```bash
mkdir mcp-dev-tools && cd mcp-dev-tools
npm init -y
npm install @modelcontextprotocol/sdk zod
npm install -D typescript @types/node tsx
npx tsc --init
```

### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "declaration": true
  },
  "include": ["src/**/*"]
}
```

### package.json additions
```json
{
  "type": "module",
  "bin": {
    "mcp-dev-tools": "./dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsx src/index.ts",
    "prepublishOnly": "npm run build"
  }
}
```

## Step-by-Step Build Guide

### Step 1: Basic MCP server with one tool
Get the skeleton working with a single "hello world" tool.

### Step 2: Add analyze_codebase tool
Read file system, count files, detect languages, map structure.

### Step 3: Add check_dependencies tool
Parse package.json/requirements.txt, check for latest versions.

### Step 4: Add generate_readme tool
Analyze code structure and generate a markdown README.

### Step 5: Add resources
Expose project context as an MCP resource.

### Step 6: Test in Cursor
Add to `.cursor/mcp.json` and test each tool.

### Step 7: Publish to npm
`npm publish` -- make it available for anyone.

## Configuration for Cursor

`.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "dev-tools": {
      "command": "npx",
      "args": ["-y", "your-mcp-package-name"]
    }
  }
}
```

## What to Show in Your Portfolio
- npm package link
- Demo video of using it in Cursor
- Documentation of each tool
- Install instructions
- Download/usage stats (once published)
