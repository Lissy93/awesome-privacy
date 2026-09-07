<script lang="ts">
  import { onMount } from 'svelte';

  import ServiceCard from './ServiceCard.svelte';
  import FontAwesome from '@components/form/FontAwesome.svelte';
  import { runSearch } from '@utils/do-searchy-searchy';
  import type { SearchItem } from '@utils/do-searchy-searchy';
  import { slugify } from '@utils/fetch-data';

  interface Props {
    searchTerm: string;
  }
  const { searchTerm }: Props = $props();

  type Sort = 'relevance' | 'category';
  const sorts: { key: Sort; label: string }[] = [
    { key: 'relevance', label: 'Relevance' },
    { key: 'category', label: 'Category' },
  ];

  const PAGE_SIZE = 50;

  let results: SearchItem[] = $state([]);
  let loading = $state(true);
  let sort: Sort = $state('relevance');
  let shown = $state(PAGE_SIZE);

  const visible = $derived(results.slice(0, shown));

  onMount(async () => {
    const wanted = new URLSearchParams(location.search).get('sort');
    if (wanted === 'category') sort = wanted;
    try {
      results = (await runSearch(searchTerm)).filter(
        (r) => r.type === 'Service',
      );
    } finally {
      loading = false;
    }
  });

  const setSort = (next: Sort) => {
    sort = next;
    const url = new URL(location.href);
    if (next === 'relevance') url.searchParams.delete('sort');
    else url.searchParams.set('sort', next);
    history.replaceState(null, '', url);
  };

  // Group into category > section, keeping the relevance order within each
  const grouped = $derived.by(() => {
    const categories: Record<string, Record<string, SearchItem[]>> = {};
    for (const item of visible) {
      const sections = (categories[item.category] ??= {});
      (sections[item.sectionName || ''] ??= []).push(item);
    }
    return Object.entries(categories).map(([name, sections]) => ({
      name,
      sections: Object.entries(sections).map(([sectionName, items]) => ({
        sectionName,
        items,
      })),
    }));
  });

  const onlySection = $derived(
    grouped.length === 1 && grouped[0].sections.length === 1
      ? { category: grouped[0].name, name: grouped[0].sections[0].sectionName }
      : null,
  );
  const canGroup = $derived(!onlySection && results.length > 0);
  const view = $derived(canGroup ? sort : 'relevance');
</script>

<section class="results-head">
  <div>
    <h3>Results</h3>
    <p>
      {#if loading}
        Searching for "{searchTerm}"...
      {:else if visible.length < results.length}
        Showing {visible.length} of {results.length} results for "{searchTerm}"
      {:else}
        {results.length}
        {results.length === 1 ? 'result' : 'results'} for "{searchTerm}"
      {/if}
    </p>
  </div>
  {#if onlySection}
    <a
      class="view-all"
      href={`/${slugify(onlySection.category)}/${slugify(onlySection.name)}/`}
    >
      View all {onlySection.name} &rarr;
    </a>
  {:else if canGroup}
    <div class="sort-by" role="group" aria-label="Sort results by">
      <span>Sort by:</span>
      {#each sorts as option (option.key)}
        <button
          type="button"
          class:active={sort === option.key}
          aria-pressed={sort === option.key}
          onclick={() => setSort(option.key)}
        >
          {option.label}
        </button>
      {/each}
    </div>
  {/if}
</section>

{#if !loading && !results.length}
  <section class="nothing-found">
    <p>Nothing matched "{searchTerm}"</p>
    <small>
      Try a tool's name, the product you're replacing, or a platform. Or browse
      <a href="/all/">all listings</a>.
    </small>
  </section>
{:else if view === 'relevance'}
  <section class="service-grid">
    {#each visible as item (item.path)}
      {#if item.service}
        <ServiceCard
          service={item.service}
          categoryName={item.category}
          sectionName={item.sectionName || ''}
        />
      {/if}
    {/each}
  </section>
{:else}
  <section class="by-category">
    {#each grouped as category (category.name)}
      <div class="category">
        <a class="category-title" href={`/${slugify(category.name)}/`}>
          <h3>{category.name}</h3>
          <FontAwesome iconName={slugify(category.name)} />
        </a>
        {#each category.sections as section (section.sectionName)}
          <h4>
            <a
              href={`/${slugify(category.name)}/${slugify(section.sectionName)}/`}
            >
              {section.sectionName}
            </a>
          </h4>
          <div class="service-grid">
            {#each section.items as item (item.path)}
              {#if item.service}
                <ServiceCard
                  service={item.service}
                  categoryName={item.category}
                  sectionName={item.sectionName || ''}
                />
              {/if}
            {/each}
          </div>
        {/each}
      </div>
    {/each}
  </section>
{/if}

{#if shown < results.length}
  <section class="load-more">
    <button type="button" onclick={() => (shown += PAGE_SIZE)}>
      Show {Math.min(PAGE_SIZE, results.length - shown)} more
    </button>
  </section>
{/if}

<style lang="scss">
  .results-head {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-md);
    align-items: end;
    justify-content: space-between;
    max-width: var(--width-container);
    width: calc(100% - 2rem);
    margin: var(--space-lg) auto var(--space-md) auto;

    h3 {
      margin: 0;
      color: var(--accent-3-text);
      font-size: var(--text-xl);
    }
    p {
      margin: 0;
      opacity: var(--opacity-muted);
    }
  }

  .load-more {
    display: flex;
    justify-content: center;

    button {
      cursor: pointer;
      font-family: inherit;
      font-size: var(--text-md);
      padding: var(--space-sm) var(--space-lg);
      color: var(--accent-3-text);
      background: var(--surface);
      border: var(--border-heavy);
      border-radius: var(--curve-sm);
      transition: var(--transition-normal);

      &:hover {
        box-shadow: var(--shadow-md);
      }
    }
  }

  .view-all {
    color: var(--accent-3-text);
    text-decoration: none;
    font-size: var(--text-sm);
    padding: var(--space-xs) var(--space-sm);
    border: var(--border-light);
    border-radius: var(--curve-sm);
    background: var(--surface);
    transition: var(--transition-normal);

    &:hover {
      border-color: var(--accent-3-text);
    }
  }

  .sort-by {
    display: flex;
    align-items: center;
    gap: var(--space-sm);

    span {
      opacity: var(--opacity-muted);
      font-size: var(--text-sm);
    }
    button {
      cursor: pointer;
      font-family: inherit;
      font-size: var(--text-sm);
      padding: var(--space-xs) var(--space-sm);
      color: var(--foreground);
      background: var(--surface);
      border: var(--border-light);
      border-radius: var(--curve-sm);
      transition: var(--transition-normal);

      &:hover {
        border-color: var(--accent-3-text);
      }
      &.active {
        color: var(--accent-3-text);
        border-color: var(--accent-3-text);
        font-weight: bold;
      }
    }
  }

  .service-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: var(--space-md);
  }

  .by-category,
  .service-grid,
  .nothing-found,
  .load-more {
    max-width: var(--width-container);
    width: calc(100% - 2rem);
    margin: 0 auto var(--space-lg) auto;
  }

  .by-category {
    display: flex;
    flex-direction: column;
    gap: var(--space-lg);

    .category-title {
      display: flex;
      align-items: center;
      gap: var(--space-sm);
      text-decoration: none;
      color: var(--foreground);

      h3 {
        margin: 0;
        font-family: var(--font-subtitle);
        font-size: var(--text-2xl);
      }
      :global(svg) {
        width: var(--text-xl);
        height: var(--text-xl);
        color: var(--accent-3-text);
        opacity: var(--opacity-dim);
      }
    }
    h4 {
      margin: var(--space-md) 0 var(--space-sm) 0;
      opacity: var(--opacity-muted);

      a {
        color: inherit;
        text-decoration: none;

        &:hover {
          color: var(--accent-3-text);
        }
      }
    }
  }

  .nothing-found {
    display: flex;
    flex-direction: column;
    gap: var(--space-sm);
    padding: var(--space-lg);
    text-align: center;
    background: var(--surface);
    border: var(--border-heavy);
    border-radius: var(--curve-sm);

    p {
      margin: 0;
      font-size: var(--text-lg);
    }
  }
</style>
