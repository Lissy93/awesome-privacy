<script lang="ts">
  import { onMount } from 'svelte';
  import {
    fetchSrcData,
    makeRemovalRequest,
    makeEditRequest,
  } from '@utils/data-src-delete-n-edit';
  import FontAwesome from '@components/form/FontAwesome.svelte';

  import type { ChangelogPr } from '../../utils/fetch-changelog';

  export let categoryName: string;
  export let sectionName: string;
  export let serviceName: string;
  export let history: Array<{
    date: string;
    type: 'added' | 'removed' | 'modified';
    fields?: string[];
    pr?: ChangelogPr | null;
  }> = [];

  let lineNumbers: { start: number; end: number } | null = null;
  let yamlContent = '';

  const getGitHubSrcFile = () => {
    if (lineNumbers) {
      const baseFile =
        'https://github.com/lissy93/awesome-privacy/blob/main/awesome-privacy.yml';
      return `${baseFile}#L${lineNumbers.start}-L${lineNumbers.end}`;
    }
    return '';
  };

  const getIframeSrc = () => {
    const host = 'https://github-embed.as93.net';
    const target = encodeURIComponent(getGitHubSrcFile());
    const opts =
      'style=felipec&type=code&showBorder=on&showLineNumbers=on&showFileMeta=on&showFullPath=on&showCopy=on';
    return `${host}/iframe.html?target=${target}&${opts}`;
  };

  onMount(async () => {
    const results = await fetchSrcData(categoryName, sectionName, serviceName);
    lineNumbers = results.lineNumbers;
    yamlContent = results.yamlContent;
  });
</script>

{#if history.length > 0}
  <h4>Change History</h4>
  <ul class="history">
    {#each history as h (h.date + h.type)}
      <li>
        <span class="history-badge {h.type}">
          {h.type === 'added'
            ? 'Added'
            : h.type === 'removed'
              ? 'Removed'
              : 'Amended'}
        </span>
        <time
          >{new Date(h.date + 'T00:00:00Z').toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            year: 'numeric',
            timeZone: 'UTC',
          })}</time
        >
        {#if h.fields}<span class="history-fields">({h.fields.join(', ')})</span
          >{/if}
        {#if h.pr?.author}
          <span class="history-author"
            >by
            <a
              href={`https://github.com/${h.pr.author}`}
              target="_blank"
              rel="noreferrer">@{h.pr.author}</a
            >
          </span>
        {/if}
        {#if h.pr}
          <a class="history-pr" href={h.pr.url} target="_blank" rel="noreferrer"
            >#{h.pr.number}</a
          >
        {/if}
      </li>
    {/each}
  </ul>
{/if}

{#if lineNumbers}
  <h4>Edit {serviceName} Data</h4>
  <p>
    You can edit {serviceName}'s entry in <a href={getGitHubSrcFile()}> this section </a> of <code>awesome-privacy.yml</code> by submitting a PR to our GitHub repo.<br>
    Note that some of the information shown above has been aggregated from external sources,
    a list of these can be found <a href="/about#our-data">data documentation</a>.
  </p>

  <h4>Origin Data</h4>
  <iframe
    frameborder="0"
    scrolling="no"
    class="yaml-embed"
    allow="clipboard-write"
    title="awesome-privacy.yml"
    src={getIframeSrc()}
  ></iframe>

  <h4>Modify Data</h4>
  <div class="button-wrap">
    <a
      class="button-link"
      target="_blank"
      href={makeRemovalRequest(
        categoryName,
        sectionName,
        serviceName,
        yamlContent,
      )}
    >
      <FontAwesome iconName="delete" /> Delete {serviceName}
    </a>
    <a
      class="button-link"
      target="_blank"
      href={makeEditRequest(
        categoryName,
        sectionName,
        serviceName,
        yamlContent,
      )}
    >
      <FontAwesome iconName="edit" /> Submit Edit to {serviceName}
    </a>
    <a class="button-link" href="/submit">
      <FontAwesome iconName="add" /> Add alternative
    </a>
  </div>
{/if}

<style lang="scss">
  @use '../../styles/mixins' as *;
  h4 {
    font-size: var(--text-lg);
    margin-bottom: 0;
  }
  p {
    margin: var(--space-xs) 0 var(--space-sm) 0;
  }

  .button-wrap {
    display: flex;
    gap: var(--space-md);
    justify-content: center;
    margin: var(--space-md) auto;
    @media (max-width: 768px) {
      flex-direction: column;
    }
  }
  .button-link {
    background: var(--accent-3);
    border: var(--border-light);
    box-shadow: var(--shadow-sm);
    color: var(--accent-fg);
    text-decoration: none;
    border-radius: var(--curve-pill);
    padding: var(--space-sm) var(--space-md);
    font-weight: bold;
    min-width: 15rem;
    display: inline-block;
    text-align: center;
    font-family: var(--font-subtitle);
    font-size: var(--text-md);
    :global(svg) {
      width: 1rem;
      height: 1rem;
    }
  }

  .history {
    list-style: none;
    padding: 0;
    margin: var(--space-sm) 0 var(--space-md) 0;
    li {
      display: flex;
      align-items: baseline;
      gap: 0.4rem;
      flex-wrap: wrap;
      padding: 0.3rem 0;
      font-size: 0.95rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      &:last-child {
        border-bottom: none;
      }
    }
    time {
      opacity: var(--opacity-muted);
      font-family: var(--font-subtitle);
      font-size: var(--text-sm);
    }
  }
  .history-badge {
    @include changelog-badge;
    font-size: var(--text-xs);
    &.added {
      background: color-mix(in srgb, var(--changelog-add) 33%, transparent);
      color: var(--changelog-add);
    }
    &.removed {
      background: color-mix(in srgb, var(--changelog-rem) 33%, transparent);
      color: var(--changelog-rem);
    }
    &.modified {
      background: color-mix(in srgb, var(--changelog-mod) 33%, transparent);
      color: var(--changelog-mod);
    }
  }
  .history-fields {
    font-size: var(--text-sm);
    opacity: var(--opacity-dim);
    font-style: italic;
  }
  .history-author {
    font-size: var(--text-sm);
    opacity: var(--opacity-soft);
    a {
      color: var(--foreground);
      &:hover {
        color: var(--accent);
      }
    }
  }
  .history-pr {
    font-size: var(--text-xs);
    padding: 0.05rem 0.3rem;
    border-radius: var(--curve-sm);
    background: var(--accent-3);
    color: var(--accent-fg);
    text-decoration: none;
    font-family: var(--font-subtitle);
    &:hover {
      opacity: 0.85;
    }
  }

  .yaml-embed {
    width: 100%;
    height: 370px;
    border: 1px solid var(--accent-3);
    border-radius: var(--curve-lg);
    padding: 0;
    margin: var(--space-md) auto;
    box-shadow: 3px 3px 0 var(--accent-3);
  }
</style>
