<script lang="ts">
  import { onMount } from 'svelte';
  import {
    fetchSrcData,
    makeRemovalRequest,
    makeEditRequest,
  } from '@utils/data-src-delete-n-edit';
  import FontAwesome from '@components/form/FontAwesome.svelte';

  export let categoryName: string;
  export let sectionName: string;
  export let serviceName: string;

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
