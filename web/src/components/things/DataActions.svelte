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
          {h.type === 'added' ? 'Added' : h.type === 'removed' ? 'Removed' : 'Amended'}
        </span>
        <time>{new Date(h.date + 'T00:00:00Z').toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric', timeZone: 'UTC' })}</time>
        {#if h.fields}<span class="history-fields">({h.fields.join(', ')})</span>{/if}
        {#if h.pr?.author}
          <span class="history-author">by
            <a href={`https://github.com/${h.pr.author}`} target="_blank" rel="noreferrer">@{h.pr.author}</a>
          </span>
        {/if}
        {#if h.pr}
          <a class="history-pr" href={h.pr.url} target="_blank" rel="noreferrer">#{h.pr.number}</a>
        {/if}
      </li>
    {/each}
  </ul>
{/if}

{#if lineNumbers}
  <h4>Edit {serviceName} Data</h4>
  <p>
    You can view or edit this {serviceName}'s entry in
    <a href={getGitHubSrcFile()}> this section </a>
    of <code>awesome-privacy.yml</code> in our GitHub repo.
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
  h4 {
    font-size: 1.4rem;
    margin-bottom: 0;
  }
  p {
    margin: 0.25rem 0 0.5rem 0;
  }

  .button-wrap {
    display: flex;
    gap: 1rem;
    justify-content: center;
    margin: 1rem auto;
    @media (max-width: 768px) {
      flex-direction: column;
    }
  }
  .button-link {
    background: var(--accent-3);
    border: 1px solid var(--box-outline);
    box-shadow: 3px 3px 0 var(--box-outline);
    color: var(--accent-fg);
    text-decoration: none;
    border-radius: 18px;
    padding: 0.5rem 1rem;
    font-weight: bold;
    min-width: 15rem;
    display: inline-block;
    text-align: center;
    font-family: 'Lekton', sans-serif;
    font-size: 1.2rem;
    :global(svg) {
      width: 1rem;
      height: 1rem;
    }
  }

  .history {
    list-style: none;
    padding: 0;
    margin: 0.5rem 0 1rem 0;
    li {
      display: flex;
      align-items: baseline;
      gap: 0.4rem;
      flex-wrap: wrap;
      padding: 0.3rem 0;
      font-size: 0.95rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      &:last-child { border-bottom: none; }
    }
    time { opacity: 0.6; font-family: 'Lekton', sans-serif; font-size: 0.85rem; }
  }
  .history-badge {
    font-size: 0.7rem;
    padding: 0.05rem 0.35rem;
    border-radius: var(--curve-sm);
    font-family: 'Lekton', sans-serif;
    text-transform: uppercase;
    font-weight: bold;
    &.added { background: color-mix(in srgb, var(--changelog-add) 33%, transparent); color: var(--changelog-add); }
    &.removed { background: color-mix(in srgb, var(--changelog-rem) 33%, transparent); color: var(--changelog-rem); }
    &.modified { background: color-mix(in srgb, var(--changelog-mod) 33%, transparent); color: var(--changelog-mod); }
  }
  .history-fields { font-size: 0.8rem; opacity: 0.5; font-style: italic; }
  .history-author {
    font-size: 0.85rem; opacity: 0.7;
    a { color: var(--foreground); &:hover { color: var(--accent); } }
  }
  .history-pr {
    font-size: 0.75rem;
    padding: 0.05rem 0.3rem;
    border-radius: var(--curve-sm);
    background: var(--accent-3);
    color: var(--accent-fg);
    text-decoration: none;
    font-family: 'Lekton', sans-serif;
    &:hover { opacity: 0.85; }
  }

  .yaml-embed {
    width: 100%;
    height: 370px;
    border: 1px solid var(--accent-3);
    border-radius: var(--curve-lg);
    padding: 0;
    margin: 1rem auto;
    box-shadow: 3px 3px 0 var(--accent-3);
  }
</style>
