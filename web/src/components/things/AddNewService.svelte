<script lang="ts">
  import yaml from 'js-yaml';
  import { writable } from 'svelte/store';
  import { makeAdditionRequest } from '../../utils/data-src-delete-n-edit';

  // Defining writable stores for each form field
  const listingCategory = writable('');
  const serviceName = writable('');
  const serviceUrl = writable('');
  const serviceIcon = writable('');
  const serviceDescription = writable('');
  const serviceGithub = writable('');
  const serviceTosdrId = writable('');
  const serviceIosApp = writable('');
  const serviceAndroidApp = writable('');
  const serviceDiscordInvite = writable('');
  const serviceSubreddit = writable('');
  const serviceOpenSource = writable(false);
  const serviceSecurityAudited = writable(false);
  const serviceCrypto = writable(false);
  const additionalInfo = writable('');

  let codeBlock: any;
  let interactiveActivated = false;

  $: (yamlText, updateHighlighting());

  function updateHighlighting() {
    if (codeBlock) {
      codeBlock.textContent = yamlText;
      codeBlock.dataset.highlighted && delete codeBlock.dataset.highlighted;
      if (window && (window as any).hljs) {
        (window as any).hljs.highlightElement(codeBlock);
        interactiveActivated = true;
      }
    }
  }

  const filterEmptyValues = (obj: Record<string, any>) => {
    const filteredObj: Record<string, any> = {};
    Object.keys(obj).forEach((key) => {
      if (obj[key] || ['name', 'url', 'icon', 'description'].includes(key)) {
        filteredObj[key] = obj[key];
      }
    });
    return filteredObj;
  };

  $: yamlText = yaml.dump(
    [
      {
        name: $serviceName,
        url: $serviceUrl,
        icon: $serviceIcon,
        description: $serviceDescription,
        github: $serviceGithub,
        tosdrId: $serviceTosdrId,
        iosApp: $serviceIosApp,
        androidApp: $serviceAndroidApp,
        discordInvite: $serviceDiscordInvite,
        subreddit: $serviceSubreddit,
        openSource: $serviceOpenSource,
        securityAudited: $serviceSecurityAudited,
        acceptsCrypto: $serviceCrypto,
      },
    ].map((obj) => filterEmptyValues(obj)),
  );

  $: issueUrl = makeAdditionRequest(
    {
      listingCategory: $listingCategory,
      serviceName: $serviceName,
      serviceUrl: $serviceUrl,
      serviceIcon: $serviceIcon,
      serviceDescription: $serviceDescription,
      serviceGithub: $serviceGithub,
      serviceTosdrId: $serviceTosdrId,
      serviceIosApp: $serviceIosApp,
      serviceAndroidApp: $serviceAndroidApp,
      serviceDiscordInvite: $serviceDiscordInvite,
      serviceSubreddit: $serviceSubreddit,
      serviceOpenSource: $serviceOpenSource,
      serviceSecurityAudited: $serviceSecurityAudited,
      serviceCrypto: $serviceCrypto,
      additionalInfo: $additionalInfo,
    },
    yamlText,
  );

  // Form submission handler
  function handleSubmit() {
    window.open(issueUrl, '_blank');
  }
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/an-old-hope.min.css"
  />
  <script
    src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"
  ></script>
  <script
    src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/yaml.min.js"
  ></script>
</svelte:head>

<p>
  Before completing this form, you must ensure that the service you are adding
  aligns with the <a href="/about#creteria">Requirements</a> for Awesome
  Privacy.
  <br />
  You'll need a GitHub account in order to submit this form.
</p>

<form on:submit|preventDefault={handleSubmit}>
  <h3>Basics</h3>
  <p class="sub-title-description">All fields here are required.</p>

  <!-- Category Dropdown -->
  <div class="form-row">
    <label for="listing-category">Category</label>
    <select
      bind:value={$listingCategory}
      id="listing-category"
      required
      autocomplete="off"
    >
      <option value="">--Please choose an option--</option>
      <option value="Essentials">Essentials</option>
      <option value="Communication">Communication</option>
      <option value="Security Tools">Security Tools</option>
      <option value="Networking">Networking</option>
      <option value="Productivity">Productivity</option>
      <option value="Utilities">Utilities</option>
      <option value="Operating Systems">Operating Systems</option>
      <option value="Development">Development</option>
      <option value="Home and IoT">Home and IoT</option>
      <option value="Finance">Finance</option>
      <option value="Social">Social</option>
      <option value="Media">Media</option>
      <option value="Creativity">Creativity</option>
    </select>
    <p>
      Choose the top-level category, which should align with the <a
        href="/browse">one of these</a
      >.
    </p>
  </div>

  <!-- Listing Name -->
  <div class="form-row">
    <label for="service-name">Listing Name</label>
    <input
      type="text"
      bind:value={$serviceName}
      id="service-name"
      required
      autocomplete="off"
    />
    <p>Enter the name of the app, software or service</p>
  </div>

  <!-- Listing URL -->
  <div class="form-row">
    <label for="service-url">Listing URL</label>
    <input
      type="url"
      bind:value={$serviceUrl}
      id="service-url"
      required
      autocomplete="off"
    />
    <p>
      Enter the fully-qualified domain name of the homepage for this listing
    </p>
  </div>

  <!-- Listing Icon -->
  <div class="form-row">
    <label for="service-icon">Listing Icon</label>
    <input
      type="url"
      bind:value={$serviceIcon}
      id="service-icon"
      required
      autocomplete="off"
    />
    <p>
      Paste a URL to a square logo for the service. Dimensions must be no less
      than 64x64, and no more than 512x512 pixels
    </p>
  </div>

  <!-- Listing Description -->
  <div class="form-row">
    <label for="service-description">Listing Description</label>
    <textarea
      bind:value={$serviceDescription}
      id="service-description"
      required
      autocomplete="off"
    ></textarea>
    <p>
      Please provide a description for this listing. Keep it factual and
      objective. Markdown is supported.
    </p>
  </div>

  <!-- Section 2 -->
  <h3>Third-Party Referencing</h3>
  <p class="sub-title-description">
    In order to create a comprehensive listing, we combine the data inputted
    above with other sources, to give additional context and help users make
    informed decisions. Metrics from these services are fetched automatically at
    build-time from our API.
    <br />
    All fields are optional, but the more information you provide, the better!
  </p>

  <!-- GitHub Repository -->
  <div class="form-row">
    <label for="service-github">GitHub Repository</label>
    <input
      type="text"
      bind:value={$serviceGithub}
      id="service-github"
      required
      autocomplete="off"
    />
    <p>
      Share a link to where the project's source is located.<br />
      Use the format [user]/[repo] e.g, lissy93/dashy
    </p>
  </div>

  <!-- ToS;DR ID -->
  <div class="form-row">
    <label for="service-tosdr-id">ToS;DR ID</label>
    <input
      type="number"
      bind:value={$serviceTosdrId}
      id="service-tosdr-id"
      autocomplete="off"
    />
    <p>
      Has the Privacy policy been documented by <a href="https://tosdr.org/"
        >tosdr.org</a
      >? If so, please include the report reference below (this is a 3 or
      4-digit numerical ID). Skip section if not applicable.
    </p>
  </div>

  <!-- Apple App Store URL -->
  <div class="form-row">
    <label for="service-tosdr-id">iOS App</label>
    <input
      type="url"
      bind:value={$serviceIosApp}
      id="service-ios-app"
      autocomplete="off"
    />
    <p>
      Paste the link to the mobile app on the Apple App Store.<br />
      E.g. https://apps.apple.com/us/app/bitwarden-password-manager/id1137397744
    </p>
  </div>

  <!-- Google Play App Store URL -->
  <div class="form-row">
    <label for="service-tosdr-id">Android App</label>
    <input
      type="url"
      bind:value={$serviceAndroidApp}
      id="service-android-app"
      autocomplete="off"
    />
    <p>
      Paste the link to the mobile app on the Google Play Store.<br />
      E.g. https://play.google.com/store/apps/details?id=com.x8bit.bitwarden
    </p>
  </div>

  <!-- Discord Server Invite Code -->
  <div class="form-row">
    <label for="service-tosdr-id">Discord Invite</label>
    <input
      type="text"
      bind:value={$serviceDiscordInvite}
      id="service-discord-invite"
      autocomplete="off"
    />
    <p>
      Paste the invite code to the Discord server for this service.<br />
      E.g. If the invite URL is https://discord.com/invite/4JMAauFZBq the code is
      4JMAauFZBq
    </p>
  </div>

  <!-- Reddit sub name -->
  <div class="form-row">
    <label for="service-tosdr-id">Subreddit</label>
    <input
      type="text"
      bind:value={$serviceSubreddit}
      id="service-subreddit"
      autocomplete="off"
    />
    <p>
      If the service has a subreddit, please provide the name here.<br />
      Don't include `r/` in the name, nor the full URL - just the sub name.
    </p>
  </div>

  <!-- Section 3 - Checklist and details -->
  <h3>Privacy Checklist</h3>
  <p class="sub-title-description">
    Finally, check the boxes that apply to the service you are submitting, and
    then provide any additional information to back this up in the text area
    below.
  </p>

  <!-- Open Source Checkbox -->
  <div class="form-row">
    <label for="service-open-source">Is Open Source?</label>
    <input
      type="checkbox"
      bind:checked={$serviceOpenSource}
      id="service-open-source"
    />
    <p>
      Is this service fully open source? Aka, can it be compiled from source by
      the user, or self-hosted?
    </p>
  </div>

  <!-- Security Audited Checkbox -->
  <div class="form-row">
    <label for="service-security-audited">Security Audited?</label>
    <input
      type="checkbox"
      bind:checked={$serviceSecurityAudited}
      id="service-security-audited"
    />
    <p>
      Has this service been independently security audited by an accredited
      auditor?
    </p>
  </div>

  <!-- Accepts Crypto Checkbox -->
  <div class="form-row">
    <label for="service-crypto">Accepts Anon Payment?</label>
    <input type="checkbox" bind:checked={$serviceCrypto} id="service-crypto" />
    <p>
      If this is a hosted and paid for service, does it accept anonymous payment
      methods, including crypto (e.g., Monero)?
    </p>
  </div>

  <div class="final-info">
    <p>Finally, please provide any supporting material, including:</p>
    <ul>
      <li>
        A justification of why this app/service should be included in the list
      </li>
      <li>Links to any published security audit, if they exist</li>
      <li>
        Links to the services privacy policy, terms of service and other
        relevant documents where applicable
      </li>
      <li>
        Your affiliation with the service. For transparency, you must disclose
        if you are associated with them or any similar items in any way
      </li>
      <li>
        Links to relevant discussions, past issues/PRs related to this service
      </li>
    </ul>
    <textarea bind:value={$additionalInfo} id="additional-info" rows="5"
    ></textarea>
  </div>

  <button type="submit">Submit</button>
  <a href={issueUrl} target="_blank" class="open-in-gh">Open in GitHub Issues</a
  >
</form>

<div class="output-yaml">
  <p>
    Below is the YAML content, which will be appended to the appropriate section
    within <a
      href="github.com/lissy93/awesome-privacy/blob/main/awesome-privacy.yml"
      >awesome-privacy.yml</a
    >
    upon approval.
  </p>
  {#if !interactiveActivated || !codeBlock}
    <pre><code class="language-yaml">{@html yamlText}</code></pre>
  {/if}
  <pre><code bind:this={codeBlock} class="language-yaml"></code></pre>
  <p>
    Your submission will need to be reviewed by a maintainer and the community
    before it can be merged.
  </p>
</div>

<style lang="scss">
  .form-row {
    display: grid;
    grid-template-columns: 1fr 3fr 2fr;
    gap: 1rem;
    padding: 0.5rem 0;
    &:not(:last-child) {
      border-bottom: 1px solid var(--transparent-accent);
    }
    p {
      margin: 0;
      font-size: 0.8rem;
      opacity: 0.6;
    }
  }

  .final-info {
    display: flex;
    flex-direction: column;
    padding: 1rem 0;
    gap: 1rem;
    p {
      margin: 0.5rem 0;
    }
    ul {
      padding-left: 0.25rem;
      margin: 0 0 0.5rem 0;
      font-size: 0.8rem;
      opacity: 0.6;
      list-style: circle;
    }
  }

  input,
  textarea,
  select {
    width: 100%;
    border: 1px solid var(--accent-3);
    border-radius: var(--curve-md);
    font-size: 1.2rem;
    padding: 0.5rem 0.25rem;
    background: var(--background-form);
    color: var(--foreground);
    &:focus {
      outline: none;
      border: 1px solid var(--accent);
    }
  }
  input {
    height: fit-content;
    &[type='number']::-webkit-outer-spin-button,
    &[type='number']::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }
    &[type='number'] {
      -moz-appearance: textfield;
    }
    &[type='checkbox'] {
      width: 2rem;
      height: 2rem;
      background: var(--background-form);
    }
  }
  textarea {
    resize: vertical;
  }
  .open-in-gh {
    margin: 0 auto;
    font-size: 0.8rem;
    opacity: 0.6;
    display: block;
    text-align: center;
  }

  button {
    cursor: pointer;
    background: var(--accent-3);
    color: var(--accent-fg);
    padding: 0.5rem 2rem;
    border: 1px solid var(--box-outline);
    box-shadow: 3px 3px 0 var(--box-outline);
    border-radius: var(--curve-lg);
    font-size: 1.8rem;
    font-family: 'Lekton', sans-serif;
    margin: 1rem auto;
    display: flex;
    transition: all 0.2s ease-in-out;
    &:hover {
      background: var(--accent);
    }
  }

  .sub-title-description {
    margin-top: 0;
    font-size: 0.8rem;
    opacity: 0.6;
  }

  .output-yaml {
    pre {
      font-family: 'Courier New', Courier, monospace;
      background: var(--background-form);
      padding: 0.2rem 0.4rem;
      border-radius: var(--curve-sm);
      font-size: 0.9rem;
    }
  }
</style>
