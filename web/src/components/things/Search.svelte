<script lang="ts">
  import { formatLink } from '@utils/parse-markdown';
  import { runSearch } from '@utils/do-searchy-searchy';
  import type { SearchItem } from '@utils/do-searchy-searchy';

  interface Props {
    previousSearch?: string | undefined;
  }
  const { previousSearch = undefined }: Props = $props();

  let searchQuery = $state(previousSearch ?? '');
  let results: SearchItem[] = $state([]);
  let isTyping = $state(false);

  // A section or category the query names is usually the intended destination,
  // unless the query is exactly a service's name
  const leadWithNamedGroup = (items: SearchItem[], query: string) => {
    const q = query.trim().toLowerCase();
    if (items.some((i) => i.type === 'Service' && i.name?.toLowerCase() === q))
      return items;
    const named = (i: SearchItem) =>
      i.type !== 'Service' &&
      ` ${i.sectionName ?? i.category}`.toLowerCase().includes(` ${q}`);
    return [...items.filter(named), ...items.filter((i) => !named(i))];
  };

  // Shares one index with the results island, so both rank identically
  $effect(() => {
    const query = searchQuery;
    runSearch(query).then((found) => {
      if (query === searchQuery)
        results = leadWithNamedGroup(found, query).slice(0, 25);
    });
  });

  const makeResultText = (cat?: string, sec?: string, itm?: string) => {
    if (itm) return itm;
    if (sec) return sec;
    if (cat) return cat;
    return '';
  };

  const makeLogoSrc = (logo?: string, url?: string) => {
    if (!logo && !url) return '/broken-image.png';
    return logo || `https://icon.horse/icon/${formatLink(url || '')}`;
  };

  const makeTitle = (typ?: string, desc?: string) => {
    if (desc && typ === 'Service') {
      return `${desc.slice(0, 60)}...`;
    }
    return '';
  };

  let activeIndex = $state(-1);

  function handleKeyDown(event: KeyboardEvent) {
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      event.preventDefault();
      const step = event.key === 'ArrowDown' ? 1 : -1;
      activeIndex = (activeIndex + step + results.length) % results.length;
      return;
    }
    if (event.key === 'Enter') {
      event.preventDefault();
      const active = results[activeIndex];
      window.location.href = active
        ? active.path
        : `/search/${encodeURIComponent(searchQuery)}/`;
    }
    if (event.key === 'Escape') {
      searchQuery = '';
      isTyping = false;
      activeIndex = -1;
    }
  }

  $effect(() => {
    searchQuery;
    activeIndex = -1;
  });
</script>

<div class="search-wrap">
  <label for="search">
    What are you looking for?
    {#if searchQuery.length > 0}
      <span class="enter-hint">Press enter to view all results</span>
    {/if}
  </label>
  <input
    id="search"
    placeholder="Start typing..."
    autocomplete="off"
    role="combobox"
    aria-expanded={isTyping && results.length > 0}
    aria-controls="search-results"
    aria-autocomplete="list"
    aria-activedescendant={activeIndex >= 0
      ? `search-result-${activeIndex}`
      : undefined}
    bind:value={searchQuery}
    oninput={() => (isTyping = true)}
    onkeydown={handleKeyDown}
  />

  {#if isTyping && results.length > 0}
    <div class="suggestions">
      <ul id="search-results" role="listbox" aria-label="Search results">
        {#each results as result, i (result.name + result.category + result.sectionName)}
          <li
            class="result-row"
            class:active={i === activeIndex}
            id={`search-result-${i}`}
            role="option"
            aria-selected={i === activeIndex}
          >
            <a
              href={result.path}
              title={makeTitle(result.type, result.description)}
            >
              <span class="name">
                {#if result.type === 'Service'}
                  <img
                    src={makeLogoSrc(result.logo, result.url)}
                    alt={result.name}
                    width="20"
                    height="20"
                    loading="lazy"
                  />
                {/if}

                {makeResultText(
                  result.category,
                  result.sectionName,
                  result.name,
                )}

                {#if result.itemCount}
                  <i>({result.itemCount})</i>
                {/if}
              </span>
              <span class="path">
                {result.category ? `${result.category}` : ''}
                {result.sectionName ? `➔ ${result.sectionName}` : ''}
                {result.name ? `➔ ${result.name}` : ''}
              </span>
            </a>
          </li>
        {/each}
      </ul>
    </div>
  {/if}
</div>

<style lang="scss">
  .search-wrap {
    display: flex;
    flex-direction: column;
    position: relative;
    max-width: 900px;
    margin: 0 auto;
    width: 100%;
    label {
      margin: var(--space-sm) 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      .enter-hint {
        font-size: var(--text-sm);
        opacity: var(--opacity-soft);
      }
    }

    input {
      padding: var(--space-sm) var(--space-md);
      font-size: var(--text-2xl);
      border: var(--border-heavy);
      box-shadow: var(--shadow-sm);
      z-index: 4;
      background: var(--background-form);
      color: var(--foreground);
      &:focus {
        outline: none;
        border-color: var(--accent);
        box-shadow: 3px 3px 0 var(--accent);
      }
    }

    .suggestions {
      ul {
        position: absolute;
        background: var(--background-form);
        z-index: 3;
        width: 100%;

        list-style: none;
        padding: 0;
        margin: 0;
        border: var(--border-heavy);
        border-radius: 0 0 var(--curve-lg) var(--curve-lg);
        box-shadow: var(--shadow-sm);
        transform: translateY(-0.5rem);
        max-height: 500px;
        overflow-y: auto;
        li.result-row {
          padding: var(--space-sm) var(--space-md);
          margin: var(--space-sm) 0;
          a {
            color: var(--foreground);
            text-decoration: none;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            .name {
              display: flex;
              align-items: center;
              gap: var(--space-sm);
              i {
                color: var(--accent-text);
                font-weight: bold;
                font-style: normal;
              }
              img {
                border-radius: var(--curve-md);
                width: 1.25rem;
                height: 1.25rem;
                object-fit: contain;
                font-size: 10px;
                color: var(--accent-text);
                overflow: hidden;
                background: var(--accent-translucent);
                padding: 1px;
              }
            }
            .path {
              font-size: var(--text-sm);
              opacity: var(--opacity-soft);
            }
          }
          &:hover,
          &.active {
            background: var(--accent);
            a,
            .name i,
            .path {
              color: var(--accent-fg);
            }
          }
        }
      }
    }
  }
</style>
