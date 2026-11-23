# World: chronicle

## For

Chronicle is getHarsh’s personal world. Its accepted opening pairs a centred portrait with a fine dither reveal of the registered figure and surrounding world; the portrait responds to attention while the introduction and translucent onward choices stay readable. Warm stock, a soft Fraunces display face and precise dates carry the quieter pages. The portrait and reveal are its loudest piece, with essays held to a quiet reading scale.

Envelope: Authored.

A personal authored publication: present questions, writing, work and an About account, with attributable evidence where it supports a claim. Dominant tasks: encounter the person and their inquiry, read their writing, and understand an experience in depth. Chronology serves an ordered career account; it is not the structure of every arrival. The world is authored and human, less institutional than its siblings.

## Character

**Organizing idea: authored attention with marginal evidence.** The person and their questions carry the account; attributable proof sits beside the claim it supports. A vertical spine and dated entries organise an ordered career account, without making chronology the structure of Home.

**Controlled contrast: human-scale warmth against technical precision.** The display voice is soft, personal and warm; dates, roles and marginal proof are set in the machine-oriented system voice with technical exactness. The record is authored, not a résumé template and not a sales page.

## The accepted opening

The personal opening holds a centred portrait, introduction and Projects, About and Thoughts in one continuous field. A fine dither reveal connects the portrait to its registered figure and world beneath. Translucent navigation and destination cards retain this world's type and material; the complete head, copy and choices remain usable at narrow widths.

The source owner supplies portrait geometry and registration. Base supplies attention response, reveal, typing and preference behaviour. Reduced motion and unavailable enhancement preserve a complete resting page. Interior pages retain their quieter stock and walnut surfaces and the shared navigation placement.

## Axes

The table distinguishes the current expression from the chronological motifs still to draw. A token value does not by itself implement a surface.

| Axis | Present expression | Values and remaining design |
| --- | --- | --- |
| Material character | Stock is intended to be warmer than Carrier’s; warm stock and walnut dark surfaces carry reading; sheet distinguishes Notes and supporting material. Painted texture belongs to imagery. | `world.*.paper`, `.sheet`, `.tint`, `.metal`, `world.material.emulsion`. |
| Raster and texture | Ordinary reading has no field texture. Fine dither belongs to the portrait and its reveal. | `world.material.raster.*` does not establish a notebook raster; a single hairline under each year, at rule-ink strength, remains part of the proposed chronological treatment. |
| Geometry | The encounter holds portrait, introduction and a horizontal choice rail. About places headings beside the continuing account on wide screens and above it on handhelds. | `world.*.strong-line`; the proposed entry nodes, vertical spine and node-edged proof plates are not current compositions. `world.geometry.plate-edge` is not a working plate control. |
| Display inflection | Soft, human-scale Fraunces at the intended medium weight contrasts with the proportional reading face and precise system labels for dates, roles and figures. | `world.type.display.family`, `.width`, `.weight`, `world.type.numeric.family`, `world.type.system.case`. |
| Figure rhythm | Figures keep their full contents, with world-supplied intervals and caption gaps. Attributable figures remain at body scale, attached to one entry and the claim they support. | `world.figure.interval`, `world.figure.caption.gap`; `world.figure.scale-step` has no current reader. A marginal proof plate remains to be drawn. |
| Emission hue and spectral light | Lamp-ember focus glow marks navigation and index links; an open Notes rule uses the signal color. Editorial currency stays in wording and position. | `world.illumination.emission`, `.emission-spread`; a lit position along the proposed spine is not implemented. Scene light follows its geography. |
| Crop behaviour | The opening preserves the complete head and the relation to the registered figure. Reading and supporting evidence remain contained. | `world.crop.bleed` records the permission for Home’s peak to bleed; it is not a current layout control. |
| Optical depth | Reading stays on a flat surface. The registered reveal connects person and wider world; translucent choices sit above it. A margin remains a column, not a floating layer. | `world.depth.*` describes intended depth; source geometry and the actual optical recipes determine the present composition. |
| Expressive motion curve | Base owns portrait response, reveal and typing. Choice imagery moves inward on pointer attention; keyboard and reduced-motion states retain immediate access. | `world.motion.expressive-easing`, `.expressive-scale`, `.decay` describe gentle opening in place, no latch or overshoot and quiet settling. The proposed chronological motion is not implemented. |

Accent is a warm amber with a derived darker ink for text where the pure accent fails contrast (`world.*.accent`, `world.*.focus`). With accent removed the world still reads through its registered portrait, warm material and soft display serif against the system voice. Entry nodes and marginal proof are further directions, not substitutes for the current encounter.

The scene's illumination and a person's movement belong to its geography and action. Lamp-ember interface state does not dictate every painted light source. A room, a folio or a notebook can serve an encounter without becoming a compulsory navigation system.

## Material and light

- **Registers:** stock carries the record; sheet carries marginal proof; anodised only for the command surface; emulsion carries authored imagery without texturing ordinary reading.
- **What emits and why:** current controls mark attention with lamp-ember light. A future chronological treatment would mark the focused entry and reader position, never the latest date as machine state. Editorial currency belongs in position and text, not telemetry.
- **Decay:** quiet, fading as focus moves on.

## States and contexts

Light uses warm stock; dark uses walnut, with reading on one plane and supporting columns distinguished by tone. Focus light gains presence on the darker ground while ordinary text stays ink. Painted lights retain their source geography rather than adopting the interface’s ember color.

Reduced motion keeps a complete portrait, introduction and choices at rest, without camera travel. Choice imagery and edge color retain the same destinations. If the chronological studies are drawn later, their nodes and proof must also be complete in place, with no travelling focus required to understand the account.

| Page mode | Web-native | Mobile-native |
| --- | --- | --- |
| Home | intimate setting and wider world: a broad field lets attention connect them while words hold their ground | complete gesture and context: in hand a closer view retains likeness before the wider relation is revealed |
| Sequence / journey | the authored progression beside the entry: at a desk the reader places this step in its wider inquiry | a persistent previous and next entry: in hand the account continues without returning to its index |

## Signature surfaces

Base’s `docs/page-families.md` governs component responsibilities and responsive continuity. Marginal evidence supports the particular claim while corpus orientation and local reading tools keep their separate positions. About may develop an ordered personal account; essays retain ordinary reading apparatus. A pursuit directory connects independent destinations without turning participation into ownership or every page into a chronology.

Baseline gives the least expression a page should show; Peak gives the most. These are design requirements, not automatic rendering controls.

| Page mode | Dominant use in this world | Baseline | Peak |
| --- | --- | --- | --- |
| Home (personal publication) | The person and their present inquiry, with entry points into the work and writing; human-scale warmth against precise marginal evidence. Peak at the authored encounter, where a change of attention or view opens the person's world. | 2 | 4 |
| Sequence / journey (entry) | An authored progression in depth, with preceding and following entries along the spine. Career accounts carry roles, dates and attributable proof; other inquiries use their supplied order. Peak at the evidence that changes the account. | 1 | 2 |
| Reading (writing) | Personal essays at the shared measure; quiet apparatus. | 1 | 1 |
| Index (writing or work) | Rows follow configured order, with dates where supplied and useful context beside each title. An authored pursuit directory may pair independent destinations with complete illustrative views; its peak is the selected relationship between description and image, not a cinematic scene. | 1 | 2 |
| Utility (contact, legal) | Complete and calm. Peak at the contact details, set on sheet in the margin like proof. | 0 | 1 |

About takes the task of its actual account. The authored `chronicle/about.html` selector maps it to Sequence, with section headings beside the continuing account. `chronicle/home.html` and `chronicle/projects.html` select Home and Index independently. Routes do not choose these forms; the author does. About's account does not acquire an article outline or reading rails because it is long. Its section headings belong within the account's composition. When Home includes pursuit choices, their anatomy matches the project index and belongs within the personal encounter. Omit that group when a direct onward action serves the encounter better. The fuller About account remains distinct.

Writing indexes retain Peak 1. Illustrated project catalogues use Base's Arc Carousel with shared Folder cards at Peak 2 when Content supplies distinct views and real destinations. Each entry carries its native landing link, artwork and complete description. Base owns selection, controls and the complete static rendition; the world supplies its warm material and human-scale type. The catalogue connects independent pursuits without implying ownership, and its artwork remains an illustration rather than evidence.

The selected `chronicle/collection-directory.html` uses Base’s bookmark anatomy and responsive behavior. This world supplies its material and typography; titles, premises and destinations remain complete. Ordinary article indexes retain Base’s compact reading rows.

## Crossing signature

`crossing.chronicle`: a small node on a short vertical stroke, a spine mark, bound to the last word. Amber may tint the mark.

## Must never become

- a disguised agency or services landing page;
- the latest period rendered as live telemetry, an emitting status light or an activity count;
- invented counts, credentials, awards or titles: the record is never padded;
- entries merged, generalized or reordered to flatter the arc;
- one record rendered twice;
- another world's type and stock with a new accent;
- decorative chronology or imagery that replaces the account or implies evidence it does not contain.
- unconsidered design choices covered by the catalogue in [the shared review instructions](AGENTS.md#shared-design-review).

## Not yet drawn

The accepted opening is the portrait and reveal. These chronological studies have not been implemented and belong only to an ordered account with real evidence; Home’s present inquiry does not call for them.

- **Spine:** entries as nodes laid down in order along the spine, the oldest lowest, the entry in focus lit.
- **Proof plate:** a marginal plate beside an entry in which the proofs are laid down in date order, the oldest lowest; only when the proof is real.

## Why it has this shape

**One registration preserves the person.** Source-owned geometry establishes likeness, framing and the relation to the revealed world. Base owns attention response and preferences, so shared interaction can change without silently recropping the person. A complete head, introduction and choices remain usable on narrow screens and at rest.

**Choices belong to the encounter.** The translucent horizontal rail connects the introduction to supplied destinations while preserving the portrait’s place. Complete copy and explicit links work without decorative imagery. One shared rail brings an edge choice into view; a second controller would compete with it. Keyboard and reduced-motion responses keep the same destinations available.

**Chronology serves an ordered account.** Dates, a spine and marginal evidence are useful when their order explains experience. Home introduces present inquiry, and an essay retains reading tools; length alone creates neither an article outline nor a career timeline. Dates and roles stay exact while the display voice stays human. A current period is editorial information; state light marks attention.

**Participation and ownership remain distinct.** A pursuit directory connects independent destinations. Its illustrative artwork is not evidence for the personal account, and taking part does not establish ownership.

**Shared controls keep the world continuous.** Navigation retains its place as the scene gives way to warm stock or walnut. Base’s anatomy supplies complete resting and print forms while Chronicle supplies its type and material. The [composition guide](docs/compositions.md) describes the available forms.
