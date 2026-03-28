<script lang="ts">
  import { onMount } from 'svelte';
  import FontAwesome from '@components/form/FontAwesome.svelte';
  import { slugify } from '@utils/fetch-data';

  export let categoryName: string;
  export let sectionName: string;
  export let serviceName: string;
  export let showLabel: boolean = false;

  const serviceRef = `${slugify(categoryName)}/${slugify(sectionName)}/${slugify(serviceName)}`;

  let isSaved = false;

  onMount(async () => {
    const stored = JSON.parse(localStorage.getItem('savedServices') || '[]');
    if (stored.includes(serviceRef)) {
      isSaved = true;
    }
  });

  function toggleSave() {
    const stored = JSON.parse(localStorage.getItem('savedServices') || '[]');
    const index = stored.indexOf(serviceRef);
    if (index === -1) {
      stored.push(serviceRef);
      isSaved = true;
    } else {
      stored.splice(index, 1);
      isSaved = false;
    }
    localStorage.setItem('savedServices', JSON.stringify(stored));
  }
</script>

<div class="wrapper-or-something">
  <button
    class={`save-container ${isSaved ? 'saved' : ''} ${showLabel ? 'label-button' : ''}`}
    title={`Save ${serviceName}`}
    on:click={toggleSave}
  >
    {#if showLabel}
      <span>
        {isSaved ? 'Saved' : 'Save'}
      </span>
    {/if}
    <FontAwesome iconName="saveListing" />
  </button>

  {#if showLabel && isSaved}
    <div class="done-msg">
      You can view all saved items in your <a href="/inventory">Inventory</a>
    </div>
  {/if}
</div>

<style lang="scss">
  .wrapper-or-something {
    display: flex;
    flex-direction: row-reverse;
    gap: var(--space-xs);
  }
  .save-container {
    cursor: pointer;
    background: none;
    border: none;
    display: flex;
    gap: var(--space-sm);
    align-items: center;
    transition: var(--transition-normal);
    span {
      font-size: var(--text-md);
      opacity: var(--opacity-subtle);
      color: var(--foreground);
      font-family: var(--font-subtitle);
    }
    :global(svg) {
      color: var(--foreground);
      width: 1.2rem;
      height: 1.2rem;
      opacity: var(--opacity-dim);
      transition: var(--transition-normal);
    }
    &:hover {
      :global(svg) {
        color: var(--accent-3);
        opacity: 1;
      }
    }
    &.saved {
      :global(svg) {
        color: var(--accent-2);
        opacity: 1;
      }
    }
    &.label-button {
      padding: 0.2rem 0.4rem;
      border-radius: var(--curve-sm);
      box-shadow: var(--shadow-sm);
      border: var(--border-light);
      background: var(--background-form);

      &:hover {
        box-shadow: var(--shadow-sm-hover);
      }
    }
  }

  .done-msg {
    max-width: 165px;
    font-size: var(--text-sm);
    opacity: var(--opacity-muted);
    @media (max-width: 768px) {
      display: none;
    }
  }
</style>
