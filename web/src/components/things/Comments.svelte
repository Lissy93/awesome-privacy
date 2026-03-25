<svelte:head>
  <script async lang="javascript">
    var remark_config = {
      host: 'https://comments.as93.net',
      site_id: 'awesome-privacy.xyz',
      components: ['embed'],
      show_rss_subsription: true,
      theme: 'dark',
    };
    !(function (e, n) {
      for (var o = 0; o < e.length; o++) {
        var r = n.createElement('script'),
          d = n.head || n.body;
        ('noModule' in r
          ? ((r.type = 'module'),
            (r.src = remark_config.host + '/web/' + e[o] + '.mjs'))
          : ((r.async = !0),
            (r.defer = !0),
            (r.src = remark_config.host + '/web/' + e[o] + '.js')),
          d.appendChild(r));
      }
    })(remark_config.components || ['embed'], document);
  </script>
</svelte:head>

<div id="remark42" />
