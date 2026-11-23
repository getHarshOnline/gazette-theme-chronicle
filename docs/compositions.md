# Composing Chronicle pages

Personal accounts select `chronicle/about.html`, which inherits Base’s About composition. Section headings belong within its account and margin composition; length alone does not call for an article outline. `chronicle/article-services.html` adds the shared closing invitation to an explicitly selected reading page; the publication chooses it for the permitted content identity.

The [presentation package](../presentation.toml) declares exact components and resources. The workspace binds `shared/portrait.mjs` and `shared/portrait.css` for the selected portrait geometry and registration. Home passes its native page-resource list to Base’s continuous-portrait player so declared image renditions serve the same registered model in local and public builds.

## Encounter and pursuit directory

Authored `chronicle/home.html`, `chronicle/about.html` and `chronicle/projects.html` selectors provide a personal encounter, an account with marginal section headings, and a directory of pursuits. The directory uses Base’s `catalogue`, with `catalogue-entry` sections that carry `folder-art` and `folder-copy` slots. Native linked headings and complete descriptions remain in Content; Base owns the shared folder-card and carousel behaviour. The optional `pursuit-opening` remains available for an authored introduction. Projects use the interior colophon; writing indexes retain their quiet ending. Static components keep copy and portrait media in the authored source; they supply no identity, career facts or destinations.

Supporting encounter choices accept an optional decorative image in their Markdown body; the theme feathers it into the trailing edge beside complete copy and a native capsule link. Pointer inquiry lifts the card and brings the image inward; keyboard focus exposes the image immediately, while reduced motion changes the edge tone in place. At compact widths the portrait follows the introductory copy and the choices form a horizontally scrollable row below it, preserving complete copy without covering the face; print restores their complete text as plain linked groups.

The encounter's optional `room` treatment composes text over a supplied wide view and switches to its second, vertical image on handhelds. Its `detail` treatment places copy in the wide view's upper-left field and precedes the full image on handhelds. These treatments require art composed for those text regions; they do not animate or establish camera continuity.

The selected character encounter and interior pages share a masthead: identity and search on the left, destination pills and utilities on the right, recomposed as a native menu in hand. The controller-bound Home masthead stays fixed as the encounter scrolls; its existing portrait ground and shared film-ink support keep navigation readable. The no-controller navigation remains in ordinary flow. Scene material changes to stock or walnut when entering an account or reading page; navigation geometry and type roles remain connected.

About's continuous copy remains beside its heading on wide screens and follows it in source order on handhelds. Base owns all controls and reading apparatus.

The current encounter uses the source-owned portrait and registered underlying figure and world. [The world’s reasons](../WORLD.md#why-it-has-this-shape) explain its composition and relationship to the personal account.

## Collection bookmarks

Collection directories inherit Base’s bookmark composition (`docs/listings-and-cards.md`). This world supplies type, material and artwork; shared anatomy determines capacity and spacing.

## Generated editorial indexes

Generated article listings inherit Base's compact `reading-list`: each entry keeps its linked title, supplied author attribution and publication date, and summary in one reading track. Base owns the anatomy, measure and responsive spacing; this world supplies its existing type and material roles. Missing metadata stays absent. Authored collection and sequence contents retain their `publication-index` forms, while explicitly selected collection directories keep their bookmark composition.

## Canonical project and service selectors

`chronicle/product.html`, `chronicle/product-listing.html` and `chronicle/services.html` inherit Base's detail, directory and service compositions. The world selectors add the existing font declarations; Base owns their shared body roles and anatomy. Content owns introductions, demonstrations, status, destinations, questions and answers. The composing workspace selects the service composition only where actual offers are supplied; templates supply no copy or offers.

The product-listing selector retains the compact colophon of `chronicle/projects.html`; that older selector is a compatibility alias.

## Shared frame and focus ownership

The Home ground belongs to the source-owned encounter; interior pages use stock or walnut. Navigation, choice cards and keyboard indication inherit Base’s shared contracts. The world supplies warm role colours and contours. Decorative portrait response remains separate from a control’s keyboard indication.

The authored account uses its source headings while the native document title remains available to navigation and metadata.

Part of [gazette-theme-chronicle](../README.md).
