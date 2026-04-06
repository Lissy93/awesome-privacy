<script lang="ts">
  import type {
    ChangelogEntry,
    ServiceChange,
    Rejection,
    ChangelogPr,
  } from '../../utils/fetch-changelog';
  import { slugify } from '@utils/fetch-data';

  export let entries: ChangelogEntry[] = [];
  export let rejections: Rejection[] = [];

  type Filter = 'added' | 'removed' | 'modified' | 'rejected';

  const filterDefs: { key: Filter; label: string; icon: string }[] = [
    { key: 'added', label: 'Additions', icon: '+' },
    { key: 'removed', label: 'Removals', icon: '−' },
    { key: 'modified', label: 'Amendments', icon: '✎' },
    { key: 'rejected', label: 'Rejections', icon: '✕' },
  ];

  let on: Record<Filter, boolean> = {
    added: true,
    removed: true,
    modified: true,
    rejected: true,
  };
  let searchQuery = '';

  function toggle(key: Filter) {
    on = { ...on, [key]: !on[key] };
  }

  type TimelineItem =
    | {
        kind: 'entry';
        date: string;
        sha: string;
        pr?: ChangelogPr | null;
        data: ChangelogEntry;
      }
    | {
        kind: 'rejection';
        date: string;
        sha: string;
        pr: ChangelogPr;
        data: Rejection;
      };

  const svc = (e: ChangelogEntry) => {
    const s = e.changes?.services;
    return {
      added: s?.added || [],
      removed: s?.removed || [],
      modified: s?.modified || [],
    };
  };
  const sec = (e: ChangelogEntry) => {
    const s = e.changes?.sections;
    return { added: s?.added || [], removed: s?.removed || [] };
  };
  const cat = (e: ChangelogEntry) => {
    const c = e.changes?.categories;
    return { added: c?.added || [], removed: c?.removed || [] };
  };

  function matchesFilters(
    item: TimelineItem,
    f: Record<Filter, boolean>,
  ): boolean {
    if (item.kind === 'rejection') return f.rejected;
    const s = svc(item.data),
      sc = sec(item.data),
      ct = cat(item.data);
    return (
      (f.added &&
        (s.added.length > 0 || sc.added.length > 0 || ct.added.length > 0)) ||
      (f.removed &&
        (s.removed.length > 0 ||
          sc.removed.length > 0 ||
          ct.removed.length > 0)) ||
      (f.modified && s.modified.length > 0)
    );
  }

  function matchesSearch(item: TimelineItem, query: string): boolean {
    if (!query) return true;
    const q = query.toLowerCase();
    if (item.kind === 'rejection') {
      return (
        item.data.title.toLowerCase().includes(q) ||
        (item.pr.author?.toLowerCase().includes(q) ?? false)
      );
    }
    const all = [
      ...svc(item.data).added,
      ...svc(item.data).removed,
      ...svc(item.data).modified,
    ];
    return (
      all.some(
        (c) =>
          c.name.toLowerCase().includes(q) ||
          `${c.category} ${c.section}`.toLowerCase().includes(q),
      ) ||
      (item.pr?.author?.toLowerCase().includes(q) ?? false)
    );
  }

  const pl = (n: number, word: string) => `${n} ${word}${n > 1 ? 's' : ''}`;

  function summarize(entry: ChangelogEntry): string {
    const s = svc(entry),
      sc = sec(entry);
    const parts: string[] = [];
    if (s.added.length) parts.push(pl(s.added.length, 'addition'));
    if (s.removed.length) parts.push(pl(s.removed.length, 'removal'));
    if (s.modified.length) parts.push(pl(s.modified.length, 'amendment'));
    if (sc.added.length) parts.push(pl(sc.added.length, 'new section'));
    if (sc.removed.length) parts.push(pl(sc.removed.length, 'section removal'));
    return parts.join(', ') || 'Changes';
  }

  function serviceLink(s: ServiceChange, isRemoval: boolean): string {
    const c = slugify(s.category),
      sc = slugify(s.section);
    return isRemoval ? `/${c}/${sc}` : `/${c}/${sc}/${slugify(s.name)}`;
  }

  type ChangeRow = {
    badge: string;
    cls: string;
    name: string;
    href: string;
    path: string;
    fields?: string[];
  };

  function changeRows(e: ChangelogEntry): ChangeRow[] {
    const s = svc(e),
      sc = sec(e),
      ct = cat(e);
    return [
      ...s.added.map((v) => ({
        badge: 'Added',
        cls: 'add',
        name: v.name,
        href: serviceLink(v, false),
        path: `into ${v.category} › ${v.section}`,
      })),
      ...s.removed.map((v) => ({
        badge: 'Removed',
        cls: 'rem',
        name: v.name,
        href: serviceLink(v, true),
        path: `from ${v.category} › ${v.section}`,
      })),
      ...s.modified.map((v) => ({
        badge: 'Amended',
        cls: 'mod',
        name: v.name,
        href: serviceLink(v, false),
        path: `in ${v.category} › ${v.section}`,
        fields: v.fields,
      })),
      ...sc.added.map((v) => ({
        badge: 'New Section',
        cls: 'add',
        name: v.name,
        href: `/${slugify(v.category)}/${slugify(v.name)}`,
      })),
      ...sc.removed.map((v) => ({
        badge: 'Section Removed',
        cls: 'rem',
        name: v.name,
        href: '',
      })),
      ...ct.added.map((v) => ({
        badge: 'New Category',
        cls: 'add',
        name: v,
        href: '',
      })),
      ...ct.removed.map((v) => ({
        badge: 'Category Removed',
        cls: 'rem',
        name: v,
        href: '',
      })),
    ];
  }

  $: allItems = [
    ...entries.map(
      (e): TimelineItem => ({
        kind: 'entry',
        date: e.date,
        sha: e.sha,
        pr: e.pr,
        data: e,
      }),
    ),
    ...rejections.map(
      (r): TimelineItem => ({
        kind: 'rejection',
        date: r.date,
        sha: `rej-${r.pr.number}`,
        pr: r.pr,
        data: r,
      }),
    ),
  ].sort((a, b) => b.date.localeCompare(a.date));

  $: filtered = allItems.filter(
    (item) => matchesFilters(item, on) && matchesSearch(item, searchQuery),
  );

  $: grouped = filtered.reduce<Record<string, TimelineItem[]>>((acc, item) => {
    const d = new Date(item.date + 'T00:00:00Z');
    const key = d.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      timeZone: 'UTC',
    });
    (acc[key] ??= []).push(item);
    return acc;
  }, {});

  function formatDate(dateStr: string): string {
    return new Date(dateStr + 'T00:00:00Z').toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      timeZone: 'UTC',
    });
  }
</script>

<details class="controls">
  <summary>Search &amp; Filter</summary>
  <div class="controls-body">
    <input
      class="search"
      type="text"
      placeholder="Search..."
      bind:value={searchQuery}
    />
    <div class="filters">
      {#each filterDefs as f (f.key)}
        <button
          class="pill {f.key}"
          class:active={on[f.key]}
          on:click={() => toggle(f.key)}
        >
          <span class="icon">{f.icon}</span>{f.label}
        </button>
      {/each}
    </div>
  </div>
</details>

{#if filtered.length === 0}
  <p class="empty">No matching changes found.</p>
{/if}

{#each Object.entries(grouped) as [month, monthItems] (month)}
  <h3 class="month-header">{month}</h3>
  {#each monthItems as item (item.sha)}
    <article class="entry">
      <time class="entry-date">{formatDate(item.date)}</time>
      <div class="entry-body">
        <div class="summary">
          {#if item.pr?.authorAvatar}
            <a
              href={`https://github.com/${item.pr.author}`}
              target="_blank"
              rel="noreferrer"
            >
              <img
                class="avatar"
                src={item.pr.authorAvatar}
                alt=""
                width="20"
                height="20"
                loading="lazy"
              />
            </a>
          {/if}
          {#if item.pr?.author}
            <span class="author"
              ><a
                href={`https://github.com/${item.pr.author}`}
                target="_blank"
                rel="noreferrer">@{item.pr.author}</a
              ></span
            >
          {/if}
          <span class="summary-text">
            {item.kind === 'rejection'
              ? 'Submission Reviewed'
              : summarize(item.data)}
          </span>
          {#if item.pr}
            <a
              class="pr-link"
              href={item.pr.url}
              target="_blank"
              rel="noreferrer">#{item.pr.number}</a
            >
          {/if}
        </div>

        <div class="changes">
          {#if item.kind === 'rejection'}
            <div class="change">
              <span class="badge rej">Rejected</span>
              <a
                class="svc-name"
                href={item.pr.url}
                target="_blank"
                rel="noreferrer">{item.data.title}</a
              >
              <span class="path">Not merged</span>
            </div>
          {:else}
            {#each changeRows(item.data) as row (`${row.cls}/${row.path}/${row.name}`)}
              <div class="change">
                <span class="badge {row.cls}">{row.badge}</span>
                {#if row.href}
                  <a
                    class="svc-name"
                    class:removed={row.cls === 'rem'}
                    href={row.href}>{row.name}</a
                  >
                {:else}
                  <strong>{row.name}</strong>
                {/if}
                {#if row.fields}<span class="fields"
                    >updated {row.fields.join(', ')}</span
                  >{/if}
                {#if row.path && !row.fields}<span class="path">{row.path}</span
                  >{/if}
              </div>
            {/each}
          {/if}
        </div>
      </div>
    </article>
  {/each}
{/each}

<style lang="scss">
  @use '../../styles/mixins' as *;
  .controls {
    margin-bottom: var(--space-md);

    summary {
      cursor: pointer;
      width: fit-content;
      font-family: var(--font-subtitle);
      opacity: var(--opacity-muted);
      &:hover {
        opacity: 1;
      }
    }

    .controls-body {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: var(--space-md);
      margin-top: var(--space-sm);
    }

    .search {
      width: 200px;
      padding: 0.35rem 0.75rem;
      border: var(--border-heavy);
      border-radius: var(--curve-lg);
      box-shadow: var(--shadow-xs);
      background: var(--accent-fg);
      color: var(--foreground);
      &:focus {
        outline: none;
        border-color: var(--accent);
        box-shadow: 2px 2px 0 var(--accent);
      }
      &::placeholder {
        opacity: var(--opacity-dim);
      }
    }

    .filters {
      display: flex;
      gap: 0.3rem;
      flex-wrap: wrap;
    }

    .pill {
      display: flex;
      align-items: center;
      gap: var(--space-xs);
      padding: 0.15rem var(--space-sm);
      border: 1px solid transparent;
      border-radius: var(--curve-md);
      background: var(--background);
      color: var(--foreground);
      cursor: pointer;
      font-family: var(--font-subtitle);
      font-size: var(--text-xs);
      opacity: var(--opacity-dim);
      transition: var(--transition-normal);

      .icon {
        font-size: var(--text-sm);
        line-height: 1;
      }
      &.active {
        opacity: 1;
        border-color: currentColor;
      }
      &.added {
        &.active {
          color: var(--changelog-add);
        }
        &:hover {
          background: color-mix(in srgb, var(--changelog-add) 10%, transparent);
        }
      }
      &.removed {
        &.active {
          color: var(--changelog-rem);
        }
        &:hover {
          background: color-mix(in srgb, var(--changelog-rem) 10%, transparent);
        }
      }
      &.modified {
        &.active {
          color: var(--changelog-mod);
        }
        &:hover {
          background: color-mix(in srgb, var(--changelog-mod) 10%, transparent);
        }
      }
      &.rejected {
        &.active {
          color: var(--changelog-rej);
        }
        &:hover {
          background: color-mix(in srgb, var(--changelog-rej) 10%, transparent);
        }
      }
    }
  }

  .empty {
    text-align: center;
    opacity: var(--opacity-muted);
    margin: var(--space-lg) 0;
  }

  .month-header {
    font-size: var(--text-lg);
    margin: 1.5rem 0 var(--space-sm) 0;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid var(--accent-3);
    color: var(--accent-3);
    font-family: var(--font-subtitle);
  }

  .entry {
    display: flex;
    gap: var(--space-md);
    padding: 0.6rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    &:last-child {
      border-bottom: none;
    }

    .entry-date {
      min-width: 7rem;
      opacity: 0.75;
      padding-top: 0.15rem;
      font-family: var(--font-subtitle);
    }

    .entry-body {
      flex: 1;
      min-width: 0;
    }
  }

  .summary {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex-wrap: wrap;
    margin-bottom: 0.3rem;
    font-size: var(--text-sm);
    opacity: var(--opacity-subtle);
    .author a {
      color: var(--foreground);
      &:hover {
        color: var(--accent);
      }
    }
    .avatar {
      border-radius: 50%;
    }
    .pr-link {
      padding: 0 0.4rem;
      border-radius: var(--curve-sm);
      background: var(--accent-3);
      color: var(--foreground);
      text-decoration: none;
      font-family: var(--font-subtitle);
      &:hover {
        opacity: 0.85;
      }
    }
  }

  .changes {
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
    .change {
      display: flex;
      align-items: baseline;
      gap: 0.4rem;
      flex-wrap: wrap;
    }
  }

  .badge {
    @include changelog-badge;
    &.add {
      background: color-mix(in srgb, var(--changelog-add) 33%, transparent);
      color: var(--changelog-add);
    }
    &.rem {
      background: color-mix(in srgb, var(--changelog-rem) 33%, transparent);
      color: var(--changelog-rem);
    }
    &.mod {
      background: color-mix(in srgb, var(--changelog-mod) 33%, transparent);
      color: var(--changelog-mod);
    }
    &.rej {
      background: color-mix(in srgb, var(--changelog-rej) 33%, transparent);
      color: var(--changelog-rej);
    }
  }

  .svc-name {
    font-weight: 500;
    color: var(--foreground);
    text-decoration: none;
  }
  a.svc-name:hover {
    color: var(--accent);
    text-decoration: underline;
  }

  .path,
  .fields {
    font-size: var(--text-sm);
    opacity: var(--opacity-muted);
  }
  .fields {
    font-style: italic;
  }

  @media (max-width: 768px) {
    .entry {
      flex-direction: column;
      gap: 0.2rem;
      .entry-date {
        min-width: unset;
      }
    }
  }
</style>
