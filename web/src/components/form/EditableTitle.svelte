<script>
  import { onMount, tick } from 'svelte';
  let title = 'Inventory'; // Default title
  let editing = false;

  // Function to save the title to local storage
  function saveTitle(newTitle) {
    localStorage.setItem('userTitle', newTitle);
    title = newTitle;
    editing = false;
  }

  onMount(async () => {
    const storedTitle = localStorage.getItem('userTitle');
    if (storedTitle) {
      title = storedTitle;
    }
    await tick(); // Ensures Svelte has completed initial DOM updates
  });

  // Function to handle key events
  function handleKeydown(event) {
    if (event.key === 'Enter') {
      event.preventDefault(); // Prevent form submission
      saveTitle(event.target.innerText);
      event.target.blur(); // Remove focus from the element
    }
    if (event.key === 'Escape') {
      editing = false;
      event.target.innerText = title; // Revert changes
      event.target.blur(); // Remove focus from the element
    }
  }

  // Click outside to stop editing
  function handleClickOutside(event) {
    if (editing) {
      saveTitle(event.target.innerText);
      editing = false;
    }
  }
</script>

<svelte:window on:click={handleClickOutside} />

<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
<div>
  <h2
    contenteditable={true}
    class:editable={editing}
    on:click={() => (editing = true)}
    on:keydown={handleKeydown}
    on:blur={() => saveTitle(title)}
    tabindex="0"
  >
    {title}
  </h2>

  <small>Click the title, to edit your inventory name</small>
</div>

<style>
  h2 {
    font-family: 'Lekton', sans-serif;
    font-weight: bold;
    font-size: 3rem;
    margin: 0;
    color: var(--accent-3);
    cursor: pointer;
    border-bottom: 2px solid transparent;
    outline: none;
    padding: 0.25rem;
  }
  .editable {
    border-bottom: 2px solid var(--accent-3); /* Visual cue to show editable state */
  }
  h2:focus {
    border-bottom: 2px solid var(--accent-3);
  }
  small {
    font-size: 0.8rem;
    opacity: 0.5;
  }
</style>
