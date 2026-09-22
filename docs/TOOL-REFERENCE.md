<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->

# Tool Reference

Fast-scan index of all 69 MCP tools, grouped by category. This page is the
lookup; full behavioural detail, edge cases, and worked examples live in the
[README's Available Tools section](../README.md#available-tools) and
[`usage.md`](usage.md). For a tool's exact parameter names, types, and
required fields, call the tool's `inputSchema` through any connected MCP
client (`tools/list`); this page intentionally does not restate JSON
schemas, so it can never drift from what the server actually serves.

## Query & Model Inspection (6)

| Tool | Purpose |
|---|---|
| `get-model-info` | Model overview: name, purpose, properties, element/relationship/view counts by type and layer |
| `get-element` | Retrieve element(s) by ID, single or batch |
| `get-views` | List views, with optional viewpoint/name filtering |
| `get-view-contents` | Full view diagram contents: elements, relationships, positions, routing, styling |
| `get-relationships` | Traverse relationships with configurable depth or multi-hop chains |
| `find-concept-usage` | Reverse where-used lookup for an element or relationship across all views |

## Search & Discovery (4)

| Tool | Purpose |
|---|---|
| `search-elements` | Full-text search across element names, documentation, properties |
| `search-relationships` | Full-text search across relationships |
| `get-or-create-element` | Return an existing exact-match element, or create one |
| `search-and-create` | Combined search + conditional create, with duplicate candidates shown |

## Element & Relationship Creation (4)

| Tool | Purpose |
|---|---|
| `create-element` | Create an ArchiMate element with type validation and duplicate detection |
| `create-relationship` | Create a relationship with ArchiMate specification rule enforcement |
| `create-view` | Create a new diagram view |
| `clone-view` | Duplicate an existing view with all visual contents |

## Element, Relationship, View & Model Updates (4)

| Tool | Purpose |
|---|---|
| `update-element` | Update name, documentation, properties, or specialization |
| `update-relationship` | Update name, documentation, properties, or specialization |
| `update-view` | Update view name, viewpoint, documentation, properties |
| `update-model` | Update the loaded model's own name, purpose, and properties |

## ArchiMate Specializations (5)

| Tool | Purpose |
|---|---|
| `list-specializations` | List every specialization defined on the model |
| `create-specialization` | Define a specialization without creating any element |
| `update-specialization` | Rename a specialization and/or set its icon |
| `delete-specialization` | Delete a specialization (refuses if in use, unless forced) |
| `get-specialization-usage` | Audit every element/relationship referencing a specialization |

## View Composition (9)

| Tool | Purpose |
|---|---|
| `add-to-view` | Place a model element onto a view |
| `add-group-to-view` | Add a visual grouping rectangle (no model representation) |
| `add-note-to-view` | Add a text note annotation (no model representation) |
| `add-view-reference-to-view` | Embed another view as a clickable thumbnail |
| `add-image-to-view` | Add a standalone image as a first-class diagram node |
| `add-connection-to-view` | Add a visual connection for an existing model relationship |
| `update-view-object` | Update position, size, styling, image, or anchor of a visual element |
| `update-view-connection` | Replace bendpoints, styling, or label of a connection |
| `apply-positions` | Apply a complete visual layout atomically |

## View Cleanup (2)

| Tool | Purpose |
|---|---|
| `remove-from-view` | Remove a visual element/connection from a view (model object preserved) |
| `clear-view` | Remove all visuals from a view (model objects preserved) |

## Layout & Routing (11)

| Tool | Purpose |
|---|---|
| `auto-route-connections` | Orthogonal connection routing (visibility-graph A*, full or terminals-only mode) |
| `auto-layout-and-route` | ELK Layered auto-layout plus routing, in `auto` or `grouped` mode |
| `layout-within-group` | Arrange child elements inside a container (row/column/grid) |
| `layout-flat-view` | Automatic layout for flat (non-grouped) views |
| `arrange-groups` | Position top-level groups relative to each other |
| `optimize-group-order` | Reorder elements within groups to minimise edge crossings |
| `resize-elements-to-fit` | Resize elements to fit their labels |
| `adjust-view-spacing` | Inflate inter-element/inter-group spacing, then re-route |
| `apply-element-spacing-recommendations` | Automated control loop to inflate within-group spacing |
| `apply-group-spacing-recommendations` | Automated control loop to widen inter-group corridors |
| `apply-spacing-recommendations` | Composed element + group spacing control loop |

## Layout Assessment & Analysis (2)

| Tool | Purpose |
|---|---|
| `assess-layout` | Assess view layout/routing quality across a multi-metric severity-tiered rating |
| `detect-hub-elements` | Identify hub elements by visual connection count, with sizing suggestions |

## View Operations (1)

| Tool | Purpose |
|---|---|
| `auto-connect-view` | Create visual connections for every existing relationship between elements already on a view |

## Folder Management (5)

| Tool | Purpose |
|---|---|
| `get-folders` | List folders (root-level, or children of a folder) |
| `get-folder-tree` | Folder hierarchy as a nested tree |
| `create-folder` | Create a new subfolder |
| `update-folder` | Update folder name, documentation, or properties |
| `move-to-folder` | Move a model object to a different parent folder |

## Deletion (4)

| Tool | Purpose |
|---|---|
| `delete-element` | Delete an element, cascading relationships and view references |
| `delete-relationship` | Delete a relationship, cascading view connections |
| `delete-view` | Delete a view and its visuals (model elements preserved) |
| `delete-folder` | Delete a folder (requires `force: true` if non-empty) |

## Export (1)

| Tool | Purpose |
|---|---|
| `export-view` | Render a view as PNG, JPG, SVG, or PDF |

## Images (2)

| Tool | Purpose |
|---|---|
| `add-image-to-model` | Import an image into the model archive |
| `list-model-images` | List images stored in the model archive |

## Batch & Mutation Control (4)

| Tool | Purpose |
|---|---|
| `begin-batch` | Start batch mode: mutations queue instead of applying immediately |
| `end-batch` | Commit all queued mutations atomically, or roll back |
| `get-batch-status` | Check operational mode and queued operation count |
| `bulk-mutate` | Execute multiple mutations as a single compound command |

## Undo / Redo (2)

| Tool | Purpose |
|---|---|
| `undo` | Undo the agent's own most recent mutation(s), scoped so human edits are never crossed |
| `redo` | Redo previously undone operation(s), symmetric to `undo` |

## Approval Workflow (1)

| Tool | Purpose |
|---|---|
| `list-pending-approvals` | List mutation proposals awaiting the human's approval (read-only) |

## Session Management (2)

| Tool | Purpose |
|---|---|
| `set-session-filter` | Set persistent filters/field selection applied to subsequent queries |
| `get-session-filters` | Retrieve currently active session-scoped filters |
