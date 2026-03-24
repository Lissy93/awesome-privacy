<script lang="ts">
  import { onMount } from 'svelte';
  import Fuse from 'fuse.js';
  import { slugify } from '@utils/fetch-data';
  import type { Category } from '../../types/Service';
  import { formatLink } from '@utils/parse-markdown';
  import { prepareSearchItems, searchOptions } from '@utils/do-searchy-searchy';
  import type { SearchItem } from '@utils/do-searchy-searchy';

  export let data: Category[];
  export let previousSearch: string | undefined = undefined;

  let fuse: Fuse<SearchItem>;
  let searchQuery = '';
  let results: SearchItem[];

  // Initialize Fuse.js
  onMount(() => {
    const items = prepareSearchItems(data);
    fuse = new Fuse(items, searchOptions);
  });

  const makeResultLink = (cat?: string, sec?: string, itm?: string) => {
    if (!cat) return '/';
    if (!sec) return `/${slugify(cat)}`;
    if (!itm) return `/${slugify(cat)}/${slugify(sec)}`;
    return `/${slugify(cat)}/${slugify(sec)}/${slugify(itm)}`;
  };

  const makeResultText = (cat?: string, sec?: string, itm?: string) => {
    if (itm) return itm;
    if (sec) return sec;
    if (cat) return cat;
    return '';
  };

  const makeLogoSrc = (logo: string, url: string) => {
    if (!logo && !url) return '/broken-image.png';
    return logo || `https://icon.horse/icon/${formatLink(url)}`;
  };

  const makeTitle = (typ: string, desc: string) => {
    if (desc && typ === 'Service') {
      return `${desc.slice(0, 60)}...`;
    }
    return '';
  };

  function handleKeyDown(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      event.preventDefault();
      if (window) {
        window.location.href = `/search/${encodeURIComponent(searchQuery)}`;
      }
    }
    if (event.key === 'Escape') {
      searchQuery = '';
    }
  }

  // Watch for changes in the search query and update results
  $: if (searchQuery) {
    results = fuse
      .search(searchQuery)
      .map((result) => result.item)
      .splice(0, 25);
  } else {
    results = [];
  }
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
    placeholder={previousSearch || 'Start typing...'}
    autocomplete="off"
    bind:value={searchQuery}
    on:keydown={handleKeyDown}
  />

  {#if searchQuery.length > 0}
    <div class="suggestions">
      <ul>
        {#each results as result (result.name + result.category + result.sectionName)}
          <li class="result-row">
            <a
              href={makeResultLink(
                result.category,
                result.sectionName,
                result.name,
              )}
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
    margin: 1rem auto;
    max-width: 900px;
    margin: 0 auto;
    width: 80vw;
    label {
      margin: 0.5rem 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      .enter-hint {
        font-size: 0.8rem;
        opacity: 0.7;
      }
    }

    input {
      padding: 0.5rem 1rem;
      font-size: 1.8rem;
      border: 2px solid var(--box-outline);
      border-radius: var(--curve-lg);
      box-shadow: 3px 3px 0 var(--box-outline);
      z-index: 4;
      background: var(--accent-fg);
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
        border: 2px solid var(--box-outline);
        border-radius: 0 0 var(--curve-lg) var(--curve-lg);
        box-shadow: 3px 3px 0 var(--box-outline);
        transform: translateY(-0.5rem);
        max-height: 500px;
        overflow-y: scroll;
        background: var(--background-form);
        li.result-row {
          padding: 0.5rem 1rem;
          margin: 0.5rem 0;
          a {
            color: var(--foreground);
            text-decoration: none;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            .name {
              display: flex;
              align-items: center;
              gap: 0.5rem;
              i {
                color: var(--accent);
                font-weight: bold;
                font-style: normal;
              }
              img {
                border-radius: var(--curve-md);
                width: 1.25rem;
                height: 1.25rem;
                font-size: 10px;
                color: var(--accent);
                overflow: hidden;
                background: #f453974d;
                padding: 1px;
              }
            }
            .path {
              font-size: 0.85rem;
              opacity: 0.7;
            }
          }
          &:hover {
            background: var(--accent);
            .name i {
              color: var(--accent-fg);
            }
          }
        }
      }
    }
  }
</style>
