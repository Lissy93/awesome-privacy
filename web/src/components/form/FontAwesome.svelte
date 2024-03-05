<script lang="ts">
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import * as solidIcons from '@fortawesome/pro-solid-svg-icons';
  import * as brands from '@fortawesome/free-brands-svg-icons';
  import type { IconDefinition } from '@fortawesome/fontawesome-svg-core';


  export const iconMap: Record<string, IconDefinition> = {
    // Branding
    logo: solidIcons.faEyeSlash,

    // GitHub Stat Icons
    github: brands.faGithubAlt,
    stars: solidIcons.faStar,
    forks: solidIcons.faCodeFork,
    issues: solidIcons.faBug,
    license: solidIcons.faScaleBalanced,
    owner: solidIcons.faUser,
    language: solidIcons.faFileCode,

    download: solidIcons.faDownload,
    faceGood: solidIcons.faSmile,
    faceMeh: solidIcons.faMeh,
    faceBad: solidIcons.faFrown,

    // Service actions
    delete: solidIcons.faTrash,
    edit: solidIcons.faPenToSquare,

    // Website Detailed Stats
    blacklistFound: solidIcons.faDoNotEnter,
    blacklistNotFound: solidIcons.faShieldCheck,
    redirectFound: solidIcons.faDiamondTurnRight,
    redirectNotFound: solidIcons.faSquareCheck,

    // Meta info icons
    openSource: brands.faOsi,
    closedSource: solidIcons.faHexagonExclamation,
    securityAudited: solidIcons.faShieldKeyhole,
    notSecurityAudited: solidIcons.faShieldXmark,
    cryptoAccepted: brands.faMonero,

    // Sections
    essentials: solidIcons.faKey,
    communication: solidIcons.faMessages,
    networking: solidIcons.faNetworkWired,
    'security-tools': solidIcons.faShieldHalved,
    productivity: solidIcons.faBriefcase,
    utilities: solidIcons.faWrench,
    'operating-systems': brands.faLinux,
    development: solidIcons.faCode,
    'smart-home-&-iot': solidIcons.faHouseSignal,
    finance: solidIcons.faCreditCard,
    social: solidIcons.faShareNodes,
    media: solidIcons.faPhotoFilmMusic,
    creativity: solidIcons.faPaintbrushPencil,
  };

  export let iconName: string;

</script>

{#if iconMap[iconName]}
  <FontAwesomeIcon 
    class="fa-icon" 
    icon={iconMap[iconName]} />
{/if}


