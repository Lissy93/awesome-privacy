<script lang="ts">
  import { slugify } from '@utils/fetch-data';

  let linkId = '';
  let done = false;
  let error = false;

  const save = async () => {
    const savedServices = JSON.parse(
      localStorage.getItem('savedServices') || '[]',
    );
    const inventoryTitle =
      localStorage.getItem('userTitle') || "Anon's Inventory";
    const uniqueId = Math.random().toString(36).substring(2);
    const saveKey = `${uniqueId}_${slugify(inventoryTitle)}`;
    const url = 'https://awesome-privacy-share-api.as93.net';
    const data = { key: saveKey, services: savedServices };
    fetch(url, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        linkId = data.key;
        done = true;
        error = false;
        navigator.clipboard.writeText(
          `https://awesome-privacy.xyz/inventory/${linkId}`,
        );
      })
      .catch((error) => {
        error = true;
        console.error('Error:', error);
      });
  };
</script>

<div class="share-container">
  {#if !done}
    <button class="save-button" on:click={save}>Get Sharable Link</button>
  {/if}
  {#if done}
    <span class="success-msg">
      Done! Your share link has been copied to clipboard.
      <a href={`https://awesome-privacy.xyz/inventory/${linkId}`}>
        Visit Link
      </a>
    </span>
  {/if}
  {#if error}
    <span class="error-msg">Something unexpected happened</span>
  {/if}
</div>

<style lang="scss">
  .share-container {
    display: flex;
    flex-direction: column;
    max-width: 300px;
  }
  .save-button {
    background: var(--accent-3);
    border: 1px solid var(--box-outline);
    box-shadow: 3px 3px 0 var(--box-outline);
    padding: 0.25rem 0.5rem;
    border-radius: var(--curve-sm);
    color: var(--foreground);
    font-family: Lekton;
    font-size: 1.2rem;
    cursor: pointer;
  }
  .success-msg {
    font-size: 1rem;
    color: var(--success);
    a {
      color: var(--success);
    }
  }
  .error-msg {
    font-size: 1rem;
    color: var(--danger);
  }
</style>
