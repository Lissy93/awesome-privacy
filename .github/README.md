<p align="center" id="top"><a href="https://github.com/Lissy93/awesome-privacy"><img src="https://i.ibb.co/80Y5x2T/Awesome-Privacy.png" /></a></p>

<p align="center">🌐 <b><a href="https://awesome-privacy.xyz">awesome-privacy.xyz</a></b></p>

*<p align="center">A curated list of privacy & security-focused apps, software, and providers 🔐</p>*

[⏬ Skip to Content ⏬](#password-managers)

## Intro [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Large data-hungry corporations dominate the digital world but with little, or no respect for your privacy.
Migrating to open-source applications with a strong emphasis on privacy and security will help stop
corporations, governments, and hackers from logging, storing or selling your personal data.

**Note**: Remember that [no software is perfect](#important-considerations), and it is important to follow good [security practices](https://github.com/Lissy93/personal-security-checklist/blob/HEAD/CHECKLIST.md).

A Codeberg mirror is available [here](https://codeberg.org/alicia/awesome-privacy).

<!-- awesome-privacy-start -->
<!-- awesome-privacy-end -->

---

## Final Notes

### Conclusion

Many corporations put profit before people, collecting data and exploiting privacy. They claim to be secure but without being open source it can't be verified, until there's been a breach and it's too late. Switching to privacy-respecting open source software will drastically help improving your security, privacy and anonymity online.

However, that's not all you need to do. It is also important to: use strong and unique passwords, 2-factor authentication,
adopt good networking practices and be mindful of data that are collected when browsing the web. You can see the full
**[personal security checklist](https://github.com/Lissy93/personal-security-checklist/blob/HEAD/CHECKLIST.md)** for more tips to stay safe. 


### Important Considerations

**Compartmentalise, Update and Be Ready**<br>
No piece of software is truly secure or private.  Further to this, software can only as secure as the system it is running on. Vulnerabilities are being discovered and patched all the time, so you much keep your system up-to-date. Breaches occur regularly, so compartmentalise your data to minimise damage. It's not just about choosing secure software, you must also follow good security practices.

**Attack Surface**<br>
It is a good idea to keep your trusted software base small, to reduce potential attack surface. At the same time trusting a single application for too many tasks or too much personal data could be a weakness in your system. So you will need to judge the situation according to your threat model, and carefully plan which software and applications you trust with each segment of your data.

**Convenience Vs Security**<br>
There is often a trade-off between convenience and security. Construct a threat model, and choose a balance that is right for you. In a similar way in some situations there is privacy and security conflict (e.g. Find My Phone is great for security, but terrible for privacy, and anonymous payments may be good for privacy but less secure than insured fiat currency). Again it is about assessing your situation, understanding the risks and making an informed decision.

**Hosted Vs Self-Hosted Considerations**<br>
When using a hosted or managed application that is open-source software - there is often no easy way to tell if the version running is the same as that of the published source code (even published signatures can be faked). There is always the possibility that additional backdoors may have been knowingly or unknowingly implemented in the running instance. One way round this is to self-host software yourself. When self-hosting you will then know for sure which code is running, however you will also be responsible for the managing security of the server, and so may not be recommended for beginners.

**Open Source Software Considerations**<br>
Open source software has long had a reputation of being more secure than its closed source counterparts. Since bugs are raised transparently, fixed quickly, the code can be checked by experts in the community and there is usually little or no data collection or analytics. 
That being said, there is no piece of software that it totally bug free, and hence never truly secure or private. Being open source, is in no way a guarantee that something is safe. There is no shortage of poorly-written, obsolete or sometimes harmful open source projects on the internet. Some open source apps, or a dependency bundled within it are just plain malicious (such as, that time [Colourama was found in the PyPI Repository](https://hackaday.com/2018/10/31/when-good-software-goes-bad-malware-in-open-source/))

**Proprietary Software Considerations**<br>
When using a hosted or proprietary solution - always check the privacy policy, research the reputation of the organisation, and be weary about which data you trust them with. It may be best to choose open source software for security-critical situations, where possible.

**Maintenance**<br>
When selecting a new application, ensure it is still being regularly maintained, as this will allow for recently discovered security issues to be addressed. Software in an alpha or beta phase, may be buggy and lacking in features, but  more importantly - it could have critical vulnerabilities open to exploit. Similarly, applications that are no longer being actively maintained may pose a security risk, due to lack of patching. When using a forked application, or software that is based on an upstream code base, be aware that it may receive security-critical patches and updates at a slightly later date than the original application. 

**This List: Disclaimer**<br>
This list contains packages that range from entry-level to advanced, a lot of the software here will not be appropriate for all audiences. It is in no way a definitive list of secure applications, and aims only to be a guide, a collection of software and services that myself and other contributors have used, and would recommend. There will always be new vulnerabilities discovered or introduced, bugs and security-critical glitches, malicious actors and poorly configured systems. It is up to you to do your research, draw up a threat model, and decide where and how your data are managed.

If you find something on this list that should no longer be deemed secure or private/ or should have a warning note attached, please raise an issue. In the same way if you know of something that is missing, or would like to make an edit, then pull requests are welcome, and are much appreciated!

### Further Reading

**More Awesome Software Lists**<br>

This list was focused on privacy-respecting software. Below are other awesome lists, maintained by the community of open source software, categorised by operating system.

- Windows: [awesome-windows-apps](https://github.com/Awesome-Windows/Awesome) by 'many'
- MacOS: [awesome-macOS-apps](https://github.com/iCHAIT/awesome-macOS) by @iCHAIT
- Linux: [awesome-linux-software](https://github.com/luong-komorebi/Awesome-Linux-Software) by @luong-komorebi
- iOS: [open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps) by @dkhamsing
- Android: [open-source-android-apps](https://github.com/pcqpcq/open-source-android-apps) by @pcqpcq
- Server: [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) by 'many'
- [**More GitHub Awesome Lists →**](https://github.com/Lissy93/personal-security-checklist/blob/master/articles/4_Privacy_And_Security_Links.md#more-awesome-github-lists)

**Security List**<br>
- [Personal Security Checklist](https://github.com/lissy93/personal-security-checklist) - A curated list of security and privacy advice, tools, and resources.

**News & Updates**<br>
A custom Reddit feed covering news and updates for all the apps covered here can be found [here](https://www.reddit.com/user/lissy93/m/software_projects/)

---

## The Website
The easist way to browse Awesome Privacy, is via our website, at **[awesome-privacy.xyz](https://awesome-privacy.xyz)**

[![screenshots](https://raw.githubusercontent.com/Lissy93/awesome-privacy/main/.github/screenshots/grid.png)](https://awesome-privacy.xyz)

### About Website
The source for the website is in the [`web/`](https://github.com/Lissy93/awesome-privacy/tree/main/web) directory.

This is a statically generated site, built with Astro, Svelte, TypeScript an SCSS.<br>
At build-time, it reads the data from [`awesome-privacy.yml`](https://github.com/Lissy93/awesome-privacy/blob/main/awesome-privacy.yml) and generates the pages.

### Running the Website Locally
You'll need [Node.js](https://nodejs.org/en) (20.11.1 or later) and [Git](https://git-scm.com/) installed.<br>
Then run the following commands to fetch the code, install dependencies and start the dev server.

```shell
git clone git@github.com:Lissy93/awesome-privacy.git
cd awesome-privacy/web
yarn
yarn dev
# Then open 127.0.0.1:4321 in your browser
```

### Deploying the Website
Follow the steps above, then run `yarn build` to generate the static files.<br>
You can then upload the `./dist` directory to any web server, static host or CDN.<br>
Alternatively, you can fork the repo and import it into either Vercel or Netlify.

---

## Contributing
We welcome suggestions, additions, edits and removals to the list.<br>
It's thanks to contributors like you that this project is possible 💜 

All data is stored in [`awesome-privacy.yml`](https://github.com/Lissy93/awesome-privacy/blob/main/awesome-privacy.yml).
If you're adding, editing or removing a listing - **this is the only file you need to edit**.

Please familiarise yourself with the [Contributing Guidelines](https://github.com/Lissy93/awesome-privacy/blob/main/.github/CONTRIBUTING.md) before submiting your pull request, as we have some guidelines that **must be followed** to ensure your PR can be accepted.

If you're new to open source, you can find some resources to get you started at [git-in.to](https://git-in.to),
but feel free to reach out if you need any help 😊 

---

## Acknowledgements

### Sponsors
Huge thanks to the following sponsors, for their ongoing support 💖

<!-- readme: sponsors -start -->
<!-- readme: sponsors -end -->


### Contributors
This project exists thanks to all the people who've helped build and maintain it  🌟
<!-- readme: contributors -start -->
<!-- readme: contributors -end -->

---

## License

> _**[Lissy93/Awesome-Privacy](https://github.com/Lissy93/awesome-privacy)** is licensed under [MIT](https://github.com/Lissy93/awesome-privacy/blob/HEAD/LICENSE) © [Alicia Sykes](https://aliciasykes.com) 2024._<br>
> <sup align="right">For information, see <a href="https://tldrlegal.com/license/mit-license">TLDR Legal > MIT</a></sup>

<details>
<summary>Expand License</summary>

```
The MIT License (MIT)
Copyright (c) Alicia Sykes <alicia@omg.com> 

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sub-license, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished 
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included install 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANT ABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

</details>


<!-- License + Copyright -->
<p  align="center">
  <i>© <a href="https://aliciasykes.com">Alicia Sykes</a> 2024</i><br>
  <i>Licensed under <a href="https://gist.github.com/Lissy93/143d2ee01ccc5c052a17">MIT</a></i><br>
  <a href="https://github.com/lissy93"><img src="https://i.ibb.co/4KtpYxb/octocat-clean-mini.png" /></a><br>
  <sup>Thanks for visiting :)</sup>
</p>

<!-- Dinosaurs are Awesome -->
<!-- 
                        . - ~ ~ ~ - .
      ..     _      .-~               ~-.
     //|     \ `..~                      `.
    || |      }  }              /       \  \
(\   \\ \~^..'                 |         }  \
 \`.-~  o      /       }       |        /    \
 (__          |       /        |       /      `.
  `- - ~ ~ -._|      /_ - ~ ~ ^|      /- _      `.
              |     /          |     /     ~-.     ~- _
              |_____|          |_____|         ~ - . _ _~_-_
-->

