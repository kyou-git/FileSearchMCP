# File Search MCP Server

A basic Model Context Protocol (MCP) server that allows LLMs to safely browse,
search, and read local documents.

---

## Overview

This project is a simple MCP server implementation designed to demonstrate
a clear understanding of the core concepts of **Model Context Protocol (MCP)**.

By exposing local files as MCP resources and search functionality as MCP tools,
LLMs can interact with local documents in a structured and secure way.

---

## Features

- List all available files in a target directory
- Search documents by keyword
- Read file contents via MCP resources
- Safe access limited to a predefined directory

---

## Why I Built This

I built this project to:

- Learn and demonstrate the core design principles of MCP
- Understand the separation between **tools** and **resources**
- Create a portfolio-ready MCP implementation suitable for real-world use cases

This repository is intended to serve as a **foundational MCP example** that can
be extended to more advanced use cases such as API integrations or database access.

---

## Architecture

LLM Client (Claude / Cursor / etc.)
↓
Model Context Protocol (MCP)
↓
File Search MCP Server
↓
Local File System (documents/)