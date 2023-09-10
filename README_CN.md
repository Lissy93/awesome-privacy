<p align="center"> <a href="https://github.com/Lissy93/awesome-privacy"> <img src="https://i.ibb.co/80Y5x2T/Awesome-Privacy.png" /> </a> </p>

*<p align="center"> A curated list of privacy & security-focused apps, software, and providers 🔐 </p>*

[⏬ 直接阅读 ⏬](#密码管理器)

## 简介 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

大型数据饥渴的企业主导着数字世界，但对您的隐私几乎没有或没有足够的尊重。

迁移到注重安全性的开源应用程序将有助于阻止企业、政府和黑客记录、存储或出售您的个人数据。

**注意**：请记住 [没有完美的软件](#disclaimer)，遵循良好的 [安全实践](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#contents) 非常重要。

[这里](https://codeberg.org/alicia/awesome-privacy) 提供了一个 Codeberg 上的镜像。

### Categories

**Translated content will be replaced with Chinese。已翻译的内容将用中文替换，用以区分。**

- **网上冲浪必需品**
  - [密码管理器](#密码管理器)
  - [双因素身份验证（2FA）](#双因素身份验证（2FA）)
  - [文件加密](#文件加密)
  - [私密浏览器](#浏览器)
  - [非跟踪搜索引擎](#搜索引擎)
- **通信交流**   
  - [加密消息](#加密消息)
  - [P2P 通信](#P2P通信（点对点通信）)
  - [加密电子邮件](#加密电子邮件)
  - [邮箱客户端](#邮箱客户端)
  - [匿名邮件转发](#匿名邮件转发)
  - [邮件安全工具](#邮件安全工具)
  - [VOIP客户端](#VOIP客户端)
  - [虚拟手机号](#虚拟手机号)
  - [团队协作平台](#团队协作平台)
- **Security Tools**
  - [Browser Extensions](#browser-extensions)
  - [Mobile Apps](#mobile-apps)
  - [Online Tools](#online-tools)
- **Networking**
  - [Virtual Private Networks](#virtual-private-networks)
  - [Self-Hosted Network Security](#self-hosted-network-security)
  - [Mix Networks](#mix-networks)
  - [Proxies](#proxies)
  - [DNS Providers](#dns)
  - [DNS Clients](#dns-clients)
  - [Firewalls](#firewalls)
  - [Ad Blockers](#ad-blockers)
  - [Host Block Lists](#host-block-lists)
  - [Router Firmware](#router-firmware)
  - [Network Analysis](#network-analysis)
  - [Cloud Hosting](#cloud-hosting)
  - [Domain Registrars](#domain-registrars)
  - [DNS Hosting](#dns-hosting)
  - [Pre-Configured Mail-Servers](#pre-configured-mail-servers)
- **Productivity**
  - [Digital Notes](#digital-notes)
  - [Cloud Productivity Suites](#cloud-productivity-suites)
  - [Backup and Sync](#backup-and-sync)
  - [Encrypted Cloud Storage](#encrypted-cloud-storage)
  - [File Drop](#file-drop)
  - [Browser Sync](#browser-sync)
  - [Secure Conference Calls](#video-conference-calls)
- **Utilities**
  - [Virtual Machines](#virtual-machines)
  - [PGP Managers](#pgp-managers)
  - [Metadata Removal](#metadata-removal-tools)
  - [Data Erasers](#data-erasers)
- **Social**
  - [Social Networks](#social-networks)
  - [Video Platforms](#video-platforms)
  - [Blogging Platforms](#blogging-platforms)
  - [News Readers](#news-readers-and-aggregation)
  - [Proxy Sites](#proxy-sites)
- **Operating Systems**
  - [Mobile Operating Systems](#mobile-operating-systems)
  - [Desktop Operating Systems](#desktop-operating-systems)
  - [Linux Defences](#linux-defences)
  - [Windows Defences](#windows-defences)
  - [Mac OS Defences](#mac-os-defences)
  - [Anti-Malware](#anti-malware)
- **Development**
  - [Code Hosting](#code-hosting)
- **Home/ IoT**
  - [Home Automation](#home-automation)
  - [Voice Assistants](#ai-voice-assistants)
- **Finance**
  - [Cryptocurrencies](#cryptocurrencies)
  - [Crypto Wallets](#crypto-wallets)
  - [Crypto Exchanges](#crypto-exchanges)
  - [Virtual Credit Cards](#virtual-credit-cards)
  - [Other Payment Methods](#other-payment-methods)
  - [Secure Budgeting](#budgeting-tools)
- **Bonus**
  - [Alternatives to Google](#bonus-1---alternatives-to-google)
  - [Open Source Media Applications](#bonus-2---open-source-media-applications)
  - [Self-Hosted Services](#bonus-3---self-hosted-services)
  - [Self-Hosted Sys-Admin](#bonus-4---self-hosted-sysadmin)
  - [Self-Hosted Dev Tools](#bonus-5---self-hosted-development-tools)
  - [Security Testing Tools](#bonus-6---security-testing-tools)
  - [Raspberry Pi Security Projects](#bonus-7---raspberry-pi-iot-security-software)

#### See Also
- [Personal Security Checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md)

<hr id="essentials" />

## 密码管理器

| 服务提供者 | 简介                                                         |
| --- | --- |
|**[Bitwarden](https://bitwarden.com)**  | （Bitwarden）是一个功能齐全、开源的密码管理器，支持云同步。它具有简洁的用户界面并且适用于桌面、Web 和移动设备的客户端应用程序，非常易于使用。当然，您还可以了解一下 [Vaultwarden](https://github.com/dani-garcia/vaultwarden)，它是一个自托管的、使用 Rust 语言实现的 Bitwarden 服务端程序，与 [官方 Bitwarden 客户端](https://bitwarden.com/download/) 兼容。 |
|**[KeePass](https://keepass.info)** | （KeePass）是一款经过强化、安全且离线的密码管理器。它不内置云同步功能，被认为是安全密码管理器的 [黄金标准](https://keepass.info/ratings.html)。KeePass 有多个客户端可供选择：[Strongbox](https://apps.apple.com/us/app/strongbox-keepass-pwsafe/id897283731)（适用于 Mac 和 iOS）、[KeePassDX](https://play.google.com/store/apps/details?id=com.kunzisoft.keepass.free)（适用于 Android）、[KeeWeb](https://keeweb.info)（基于 Web 或自托管）、[KeePassXC](https://keepassxc.org)（适用于 Windows 、Mac 和 Linux）。您还可以在 @lgg 的 [awesome-keepass](https://github.com/lgg/awesome-keepass) 项目下找到更多 KeePass 客户端和扩展。 |
|**[LessPass](https://lesspass.com)** *(自托管)* | LessPass 与众不同，它使用网站名称、用户名和一个重复使用的（主）密码短语的哈希值来生成密码。这样一来，您就不需要存储或同步密码。LessPass 提供了适用于常见平台的应用程序和命令行界面（CLI），但您也可以选择自行托管它。 |
|**[Padloc](https://padloc.app)** | （Padloc）是一款现代化的、开源的个人和团队密码管理器。界面美观、直观，极其简单易用。支持所有平台的应用程序，同时也可以自行托管。 |

#### 小提示

**[Password Safe](https://www.pwsafe.org/)** 是一款由 [Bruce Schneier](https://www.schneier.com/academic/passsafe/) 开发的离线、开源密码管理器，它是原生应用程序。适用于 Windows、Linux、MacOS、Android 和 iOS，并支持 YubiKey。虽然它的用户界面有些陈旧，并且没有官方的浏览器扩展，相比其他选择来说使用起来略显不便。

**[PassBolt](https://www.passbolt.com/)** 是团队使用的一个很好的选择。它是免费、开源、支持自托管、可扩展，并基于 OpenPGP。PassBolt 特别适用于开发和 DevOps 领域，它提供了与终端、浏览器和聊天工具的集成，并且可以轻松扩展以满足定制需求，使用 Docker 可以快速部署。

**[1Password](https://1password.com)** 是一个功能齐全的跨平台密码管理器，支持同步功能。选择自托管数据是免费的（或者每月 3 美元托管）。请注意，1Password 并非完全开源，但他们定期公布独立的 [安全审计结果](https://support.1password.com/security-assessments)，并且以透明披露和修复漏洞的方式赢得了良好的声誉。

**其他开源密码管理器**： [Buttercup](https://buttercup.pw), [Clipperz](https://clipperz.is), [Pass](https://www.passwordstore.org), [Padloc](https://padloc.app), [TeamPass](https://teampass.net), [PSONO](https://psono.com), [UPM](http://upm.sourceforge.net), [Gorilla](https://github.com/zdia/gorilla/wiki), [Seahorse](https://gitlab.gnome.org/GNOME/seahorse) （适用于 GNOME 环境）, [GNOME Keyring](https://wiki.gnome.org/Projects/GnomeKeyring), [KDE Wallet Manager](https://userbase.kde.org/KDE_Wallet_Manager).

如果你正在使用一个已经停止维护的密码管理器，你应该迁移到一款仍在积极维护的工具。以下是一些推荐的选择： [Firefox Lockwise](https://www.mozilla.org/en-US/firefox/lockwise), [Encryptr](https://spideroak.com/encryptr), [Mitro](https://www.mitro.co), [Rattic](https://spideroak.com/encryptr), [JPasswords](http://jpws.sourceforge.net/jpasswords.html), [Passopolis](https://passopolis.com), [KYPS](https://en.wikipedia.org/wiki/KYPS), [Factotum](http://man.9front.org/4/factotum).

**另请参阅** [密码管理清单](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#passwords)


## 双因素身份验证（2FA）

| 服务提供者 | 简介 |
| --- | --- |
|**[Aegis](https://getaegis.app)** (Android)  | 一款免费、安全且开源的安卓身份验证应用程序。具有备份、恢复功能和可自定义的用户界面，支持暗黑模式。 |
|**[Authenticator Pro](https://github.com/jamie-mh/AuthenticatorPro)** (Android) | 一款免费且开源的安卓双因素身份验证应用程序。它具有加密备份、图标、分类和高度的自定义功能。此外，它还提供了与 Wear OS 配套的应用程序。 |
|**[Tofu](https://www.tofuauth.com)** (iOS) | 一款专为 iOS 设计的易于使用的开源双因素身份验证应用程序。 |
|**[Authenticator](https://mattrubin.me/authenticator/)** (iOS) | 一款简单、本地化、开源的 iOS 双因素身份验证客户端，永远不会连接到互联网 - 由 @mattrubin.me 开发。 |
|**[Raivo OTP](https://github.com/raivo-otp/ios-application)** (iOS) | 一款本地化、轻量级和安全的 iOS 一次性密码（OTP）客户端；Raivo OTP! - 由 @tijme 开发。 |
|**[WinAuth](https://winauth.github.io/winauth)** (Windows) | 一款便携式、加密的 Windows 桌面端身份验证器应用程序。它具有一些实用的功能，如热键和一些附加的安全工具，是高级桌面用户的绝佳身份验证器。该应用程序是开源的，并且已经成熟稳定（自 2010 年中期以来）。 |
|**[Authenticator](https://gitlab.gnome.org/World/Authenticator)** (Linux) | 一款基于 Rust 的 OTP 身份验证器。它具有与 GNOME Shell 的原生集成。你也可以通过 [flathub](https://flathub.org/apps/details/com.belmoussaoui.Authenticator) 获取。 |
|**[Authenticator](https://authenticator.cc/)** (浏览器扩展) | Authenticator Extension 是一款浏览器内的一次性密码（OTP）客户端，支持基于时间的一次性密码（TOTP，详见 [RFC 6238](https://tools.ietf.org/html/rfc6238)）和基于 HMAC 的一次性密码（HOTP，详见 [RFC 4226](https://tools.ietf.org/html/rfc4226)）两种规范。 |

*查阅支持多因素身份验证的网站： [2fa.directory](https://2fa.directory/)*

#### 小提示

[OTPClient](https://github.com/paolostivanin/OTPClient) *(Linux)*，[gauth](https://github.com/gbraadnl/gauth) *(自托管，基于 Web)*，[Etopa](https://play.google.com/store/apps/details?id=de.ltheinrich.etopa) *(Android)*

对于 KeePass 用户而言，[TrayTop](https://keepass.info/plugins.html#traytotp) 是一个用于管理 TOTP 的插件，可以离线使用，并且兼容 Windows、Mac 和 Linux。

[Authy](https://authy.com/) 是新用户中流行的选择，因为它易于使用且具备设备同步功能。云同步可能很方便，但也会增加攻击面。Authy 不是开源软件，因此不能推荐使用。

**另请参阅** [2FA Security Checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#2-factor-authentication)


## 文件加密

| 服务提供者 | 简介                                                         |
| --- | --- |
|**[VeraCrypt](https://www.veracrypt.fr)** | VeraCrypt 是一款开源的跨平台磁盘加密软件。你可以使用它来加密特定的文件或目录，或者整个磁盘或分区。VeraCrypt 功能丰富，提供了全面的加密选项，同时其 GUI 使得使用变得简单。它还有一个命令行版本和便携版。VeraCrypt 是（现已停止维护的）TrueCrypt 的后继者。 |
|**[Cryptomator](https://cryptomator.org)** | Cryptomator 是一款针对云文件的开源客户端端到端加密软件，它专为与云备份解决方案配合使用而设计，因此保留了独立的文件结构，以便可以上传。它同样易于使用，但与 VeraCrypt 相比，在数据加密的技术自定义方面较少。Cryptomator 适用于 Windows、Linux 和 Mac，并且还有出色的移动应用程序。 |
|**[age](https://github.com/FiloSottile/age)** | `age` 是一个简单、现代且安全的命令行界面文件加密工具和 Go 库。它采用小型明确的密钥，没有配置选项，并具有 UNIX 风格的可组合性。 |


#### 小提示
[AES Crypt](https://www.aescrypt.com/) 是一个轻量级且易于使用的文件加密工具。它包括适用于 Windows、Mac OS、BSD 和 Linux 的应用程序，可以通过 GUI、命令行界面 (CLI) 或通过 API（适用于 Java、C、C# 和 Python）进行交互。虽然它已经建立了良好的声誉，但最近也出现了一些 [安全问题](https://www.reddit.com/r/privacytoolsIO/comments/b7riov/aes_crypt_security_audit_1_serious_issue_found/)。

[CryptSetup](https://gitlab.com/cryptsetup/cryptsetup) 是在 [dm-crypt](https://wiki.archlinux.org/index.php/Dm-crypt) 之上使用的便捷层。[EncFS](https://www.arg0.net/encfs) 是一个跨平台的基于文件的加密模块，在用户本地目录中使用。[geli](https://www.freebsd.org/cgi/man.cgi?query=geli&sektion=8) 是 FreeBSD 附带的磁盘加密子系统。

PGP 可能对加密单个文件和文件夹、准备文件传输或为敏感数据添加额外的安全层非常有用。使用 PGP，您可以对文件和文件夹进行加密、解密、签名和验证：请参阅 [PGP 工具](#pgp-managers)。

[BitLocker](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview) 在 Microsoft Windows 和企业用户中很受欢迎，提供快速、高效且（如果正确配置）相对安全的全盘加密。然而，它不是开源的，与其他操作系统的兼容性较差，并且具有一些非常有风险的 [默认设置](https://www.diskcryptor.org/why-not-bitlocker/)，可能导致系统被入侵。同样，苹果的 [FileVault](https://support.apple.com/en-us/HT204837) 在 MacOS 上易于使用且安全，但同样，其源代码是闭源的。

[DiskCryptor](https://www.diskcryptor.org/) 是一个仅适用于 Windows 的开源文件和卷加密解决方案，是 BitLocker 的一个很好的替代选择。

如果您需要创建压缩存档，那么 [PeaZip](https://www.peazip.org/) 是一个非常棒的跨平台开源文件压缩工具。它可以创建、打开和提取 RAR、TAR 和 ZIP 存档。它还具有 [密码保护功能](https://peazip.github.io/peazip-password.html)，可以使用 AES-256 加密压缩文件，与大多数其他存档工具兼容。

#### 警告
在可能的情况下，选择跨平台和经过良好验证的加密方法，以确保您始终能够使用当前系统访问您的文件。

虽然经过良好验证的加密方法通常非常安全，但如果密码不够强大，那么使用强大的 GPU，对手可能能够访问您的文件。如果您的系统被入侵，密码也可能被键盘记录器或其他类似恶意软件窃取，因此请注意遵循良好的基本安全实践。

## 浏览器

| 服务提供者 | 简介 |
| --- | --- |
|**[LibreWolf](https://librewolf.net/)** | LibreWolf 是 Firefox 的一个独立分支，旨在通过改善默认设置来提升隐私、安全和用户自由。它禁用了 Mozilla 的遥测功能，断开了与谷歌（Safe Browsing）的连接，还包含了内容拦截器 [uBlock Origin](https://github.com/gorhill/uBlock)，隐私默认设置受到像 [Arkenfox 项目](https://github.com/arkenfox/user.js/) 这样的研究的指导。 |
|**[Brave 浏览器](https://brave.com)** | Brave 浏览器，目前是最受欢迎的隐私浏览器之一，它通过阻止跟踪器并提供简洁而功能齐全的用户界面，提供了速度、安全和隐私保护。此外，使用 Brave 浏览器还可以获得 [BAT 代币](https://basicattentiontoken.org/) 奖励。当您打开一个私密的标签页/窗口时，Brave 还内置了 Tor 功能。 |
|**[Firefox](https://www.mozilla.org/firefox)** | 相比 Chrome、Internet Explorer 和 Safari，Brave 浏览器在隐私方面提供了更多的保护，并提供了一些巧妙的隐私功能。安装后，您需要进行一些小的调整来增强 Firefox 的安全性。有关详细的配置，请参考 [@arkenfox 的 user.js](https://github.com/arkenfox/user.js/)。您还可以按照 [Restore Privacy](https://restoreprivacy.com/firefox-privacy/) 或 [12Bytes](https://12bytes.org/7750) 的指南进行操作。 |
|**[Tor Browser](https://www.torproject.org/)** | Tor 通过对每个请求进行加密，并将其路由通过多个节点，为您提供了额外的匿名保护层，几乎不可能被您的 ISP 或供应商跟踪到。然而，使用 Tor 会使日常浏览速度稍慢，并且某些网站可能无法正常工作。就像任何事物一样，使用 Tor 也存在一些权衡之处。您可以参考 [trade-offs](https://github.com/Lissy93/personal-security-checklist/issues/19) 以了解更多信息。 |
|**[Bromite](https://www.bromite.org/)** | 这是一个针对 Android 的强化版、注重隐私的 Chromium 分支。它内置了广告拦截功能，并提供了额外的设置以增强安全性。 |

#### 小提示
移动浏览器： [Mull](https://f-droid.org/en/packages/us.spotco.fennec_dos/) 基于 FF-Fenix 的强化版 (Android), [Firefox Focus](https://support.mozilla.org/en-US/kb/focus) (Android/ iOS), [DuckDuckGo Browser](https://help.duckduckgo.com/duckduckgo-help-pages/mobile/ios/) (Android/ iOS), [Orbot](https://guardianproject.info/apps/orbot/) + [Tor](https://www.torproject.org/download/#android) (Android), [Onion Browser](https://onionbrowser.com/) (iOS)

其他桌面浏览器： [Nyxt](https://nyxt.atlas.engineer/), [WaterFox](https://www.waterfox.net), [Epic Privacy Browser](https://www.epicbrowser.com), [PaleMoon](https://www.palemoon.org), [Iridium](https://iridiumbrowser.de/), [Sea Monkey](https://www.seamonkey-project.org/), [Ungoogled-Chromium](https://github.com/Eloston/ungoogled-chromium), [Basilisk Browser](https://www.basilisk-browser.org/) 和 [IceCat](https://www.gnu.org/software/gnuzilla/)

12Bytes 也维护着一个隐私和安全扩展的列表，[点这里查看](https://12bytes.org/articles/tech/firefox/firefox-extensions-my-picks/)

#### 警告
新的漏洞不断被发现并修补 - 使用一个正在积极维护的浏览器，以便及时获得这些关键的安全更新。

即使是注重隐私的浏览器，通常默认情况下也没有启用最佳的隐私选项。安装后，请检查设置，并将配置更新为您所满意的内容。12Bytes 维护了一份全面的指南，介绍了有关 [Firefox Configuration for Privacy and Performance](https://12bytes.org/articles/tech/firefox/firefoxgecko-configuration-guide-for-privacy-and-performance-buffs/) 的内容。

**另请参阅** [Browser & Search Security Checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#browser-and-search) ，推荐 [Browser Extensions](#browser-extensions) 用与隐私和安全。

## 搜索引擎

谷歌经常修改和操纵搜索结果，追求消除竞争并推广自己的服务。他们还会跟踪、收集、使用和出售用户的详细搜索和元数据。

| 服务提供者 | 简介 |
| --- | --- |
|**[DuckDuckGo](https://duckduckgo.com/)** | DuckDuckGo 是一个非常用户友好、快速和安全的搜索引擎。它完全私密，没有跟踪器、Cookie 或广告。它还具有高度可定制性，包括暗黑模式、多种语言和功能。他们甚至还提供了一个 [.onion](https://3g2upl4pq6kufc4m.onion) 的 URL，供 Tor 使用，以及一个 [没有 Javascript 的版本](https://duckduckgo.com/html/)。 |
|**[Qwant](https://www.qwant.com/)** | Qwant 是一个法国的搜索服务，它汇集了 Bing 的搜索结果，并添加了自己的结果。Qwant 不会设置任何 Cookie，也没有任何跟踪器或第三方广告。它返回无偏见的搜索结果，没有任何推广内容。Qwant 拥有独特而美观的用户界面。 |
|**[Startpage](https://www.startpage.com/)** | 这是一个荷兰的搜索引擎，它在谷歌上进行搜索并显示结果（稍作调整）。它有几个配置选项，可以在使用过程中提高隐私保护（但它不是开源的）。 |

#### 小提示
[MetaGear](https://metager.org), [YaCy](https://yacy.net), [Brave Search](https://search.brave.com/). 

[Searx](https://searx.github.io/searx/) 和 [SearXNG](https://github.com/searxng/searxng) 是两个可以自托管的搜索引擎，它们同时使用多个其他引擎（如 Google 和 Bing）的搜索结果。它们是开源的，并且可以自行托管，不过使用 [公共实例](https://searx.space) 的好处是不会将您的查询 **单独** 发送给使用的引擎。

12Bytes 也维护了一个 [尊重隐私的搜索引擎列表](https://12bytes.org/articles/tech/alternative-search-engines-that-respect-your-privacy/)。

**另请参阅** [Browser & Search Security Checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#browser-and-search)

<hr id="communication" />

## 加密消息

如果不使用安全的即时通讯应用程序，你的所有对话、元数据等都是不受保护的。Signal 是最佳选择之一，它既易于使用，又高度安全和注重隐私保护。

| 服务提供者 | 简介 |
| --- | --- |
| **[Signal](https://signal.org/)**     | Signal 可能是最受欢迎的安全私密消息应用之一，它将强大的加密技术（参见 [Signal Protocol](https://en.wikipedia.org/wiki/Signal_Protocol)）与简洁的用户界面和丰富的功能相结合。它在全球范围内被广泛使用，类似于 WhatsApp，提供即时消息、已读回执、支持媒体附件，并允许高质量的语音和视频通话。它跨平台、开源且完全免费。Signal 被 [Edward Snowden 推荐](https://twitter.com/Snowden/status/661313394906161152)，对大多数用户来说是一个完美的解决方案。 |
| **[Session](https://getsession.org)** | Session 是 Signal 的一个分支，但与 Signal 不同，它不需要手机号码（或任何其他个人数据）进行注册，而是通过公钥来识别每个用户。它也是去中心化的，通过 [Loki Net](https://loki.network) 社区提供服务器并运营，消息经过多个节点进行加密和路由。所有通信都是端到端加密的，没有元数据。 |
| **[XMPP](https://xmpp.org/)**     | XMPP，也被称为 Jabber，是一种用于分布式消息传递的开放标准，已经广泛使用了几十年。实际上，WhatsApp、Facebook 的 Chat 和 Google 的 Talk 就是基于它构建的，但这些公司（最终）选择删除了与其他服务器的互操作性。著名的 XMPP 客户端支持 [OMEMO 端到端加密](https://en.wikipedia.org/wiki/OMEMO)，它基于 Signal 中使用的 [双螺旋算法](https://en.wikipedia.org/wiki/Double_Ratchet_Algorithm)。要获取更多实际操作信息并注册账号，你可以访问 [JoinJabber](https://joinjabber.org)。下面是一些适用于主要平台的支持 OMEMO 的客户端列表：<br> <br> <table> <thead> <tr> <th> 程序 </th> <th> Linux </th> <th> MacOS </th> <th> Windows </th> <th> Android </th> <th> iOS </th> </tr> </thead> <tbody> <tr> <td> <a href="https://gajim.org"> Gajim </a> （<a href="https://gajim.org/download/#install-instructions"> OMEMO 插件 </a>）</td> <td> ✓ </td> <td> <a href="https://dev.gajim.org/gajim/gajim/-/wikis/help/Gajim-on-macOS">~</a> </td> <td> ✓ </td> <td> </td> <td> </td> </tr> <tr> <td> <a href="https://dino.im"> Dino </a> ✆ </td> <td> ✓ </td> <td> </td> <td> <a href="https://github.com/LAGonauta/dino/releases"> ✓ </a> </td> <td> </td> <td> </td> </tr> <tr> <td> <a href="https://conversations.im"> Conversations </a> / <a href="https://blabber.im"> Blabber </a> ✆ </td> <td> </td> <td> </td> <td> </td> <td> ✓ </td> <td> </td> </tr> <tr> <td> <a href="https://monal-im.org"> Monal IM </a> </td> <td> </td> <td> ✓ </td> <td> </td> <td> </td> <td> ✓ </td> </tr> <tr> <td> <a href="https://beagle.im"> Beagle IM </a> / <a href="https://siskin.im"> Siskin IM </a> ✆ </td> <td> </td> <td> ✓ </td> <td> </td> <td> </td> <td> ✓ </td> </tr> </tbody> </table> |
| **[Matrix](https://matrix.org)**  | Matrix 是一个去中心化的开放网络，用于安全通信，通过 Olm 和 Megolm 实现端到端加密。它与 [Element](https://element.io/) 客户端一起支持 VOIP + 视频通话和 IM + 群聊。由于 Matrix 具有开放的规范和简单实用的 RESTful HTTP/JSON API，因此很容易与现有的第三方身份验证和用户发现系统集成，以及在其上构建应用程序。 |

#### 小提示
其他私密、加密且开源的消息应用包括：[Surespot](https://www.surespot.me), [Chat Secure](https://chatsecure.org/)（仅限 iOS）和 [Status](https://status.im/)。需要注意的是，由于 [Tor Messenger](https://blog.torproject.org/category/tags/tor-messenger) 的开发已经停止，它已从列表中移除。

[KeyBase](keybase.io/inv/6d7deedbc1) 允许进行加密的实时聊天、群聊和公共/私密文件共享。它还具有一些有关加密证明社交身份的好功能，并且可以轻松进行 PGP 签名、加密和解密消息。然而，自从它在 2020 年被 [Zoom 收购](https://keybase.io/blog/keybase-joins-zoom) 以后，它已经不再定期更新。

[OpenPGP](https://www.openpgp.org/) 可以在现有的聊天网络（如电子邮件或留言板）上使用。它提供了加密隐私和身份验证，PGP 用于加密消息。<br>
**有关 PGP 的提示和问题** 对于初学者来说，PGP 并 [不容易](https://restoreprivacy.com/let-pgp-die/) 使用，可能会导致人为错误，这可能比使用其他简单的系统更糟糕。不要使用 [32 位密钥 ID](https://evil32.com/)，它们过于短小，不安全。OpenPGP 和 S/MIME 存在漏洞，详见 [EFAIL](https://efail.de/)，因此，尽管它仍被认为在一般用途下是安全的，但对于一般聊天来说，最好使用加密的消息或电子邮件应用。

#### 警告
许多消息应用声称自己是安全的，但如果它们不是开源的，那么这一点是无法验证的，因此 **不应该被信任**。这适用于 [Telegram](https://telegram.org), [Threema](https://threema.ch), [Cypher](https://www.goldenfrog.com/cyphr), [Wickr](https://wickr.com/), [Silent Phone](https://www.silentcircle.com/products-and-solutions/silent-phone/) 和 [Viber](https://www.viber.com/) 等应用，这些应用不应用于传输任何敏感数据。由于 [Wire](https://wire.com/) 最近被 [收购](https://blog.privacytools.io/delisting-wire/)，它也已被移除。


## P2P 通信（点对点通信）

在 [点对点](https://zh.wikipedia.org/wiki/点对点) 网络中，没有中央服务器，因此没有任何可以被查封、关闭或强制交出数据的东西。有一些开源的 P2P 网络可用，它们支持端到端加密，通过 Tor 服务进行路由，完全匿名，并且不收集元数据。

| 服务提供者 | 简介 |
| --- | --- |
| **[Session](https://getsession.org)** + **[LokiNet](https://loki.network)** 客户端 | Loki 是一套开源工具，允许用户通过去中心化、加密、基于洋葱路由的网络匿名和私密地进行交易和通信。Session 是一个桌面和移动应用程序，使用这些私密路由协议来保护消息、媒体和元数据。 |
| **[Briar](https://briarproject.org)**                        | 基于 Tor 的 Android 应用，用于点对点的加密消息和论坛。内容安全存储在您的设备上（而非云端）。它还允许您直接与附近的联系人建立连接，无需互联网访问（使用蓝牙或 WiFi）。 |
| **[Ricochet Refresh](https://www.ricochetrefresh.net)**      | 桌面即时通讯工具，使用 Tor 网络与您的联系人建立会话，而不会泄露您的身份、位置/IP 或元数据。没有服务器可以监视、审查或黑客入侵，因此 Ricochet 是安全、自动且易于使用的。 |
| **[Jami](https://jami.net)**                                 | P2P 加密聊天网络，具有跨平台的 GNU 客户端应用程序。Jami 支持音频和视频通话、屏幕共享、会议主持和即时消息。 |
| **[Tox](https://tox.chat)** + **[qTox](https://qtox.github.io)** 客户端 | 开源、加密的分布式聊天网络，具有桌面和移动客户端 - 请参阅 [支持的客户端](https://tox.chat/clients.html)。清晰文档化的代码和多种语言包使开发者能够轻松地与 Tox 集成。 |

#### 小提示
[Cwtch](https://cwtch.im), [BitMessage](https://github.com/Bitmessage/PyBitmessage), [RetroShare](https://retroshare.cc), [Tor Messenger](https://blog.torproject.org/sunsetting-tor-messenger) *(已弃用)*、[TorChat2](https://github.com/prof7bit/TorChat) *(已弃用)*、[Ricochet](https://ricochet.im) *(已弃用)*


## 加密电子邮件

电子邮件并不安全 - 您的消息很容易被拦截和阅读。公司会扫描您邮件的内容，以建立您的个人画像，用于展示定向广告或出售给第三方。通过 [棱镜计划](https://zh.wikipedia.org/wiki/%E6%A3%B1%E9%95%9C%E8%AE%A1%E5%88%92)，政府也可以完全访问您的电子邮件（如果没有端到端加密）- 这适用于 Gmail、Outlook Mail、Yahoo Mail、GMX、ZoHo、iCloud、AOL 等。

以下电子邮件提供者是私密的、端到端加密（E2EE）且相对安全的。这应与 [良好的电子邮件实践](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#emails) 结合使用。

| 服务提供者 | 简介 |
| --- | --- |
| **[ProtonMail](https://protonmail.com/)**           | ProtonMail 是一个开源的端到端加密匿名电子邮件服务。ProtonMail 具有现代化、易于使用和可自定义的用户界面，以及快速、安全的原生移动应用程序。ProtonMail 具备现代电子邮件服务的所有功能，基于简洁性而不牺牲安全性。它提供免费订阅以及高级选项，可使用自定义域名（起价每月 5 美元）。ProtonMail 在注册时不需要个人身份信息，他们还有一个.onion 服务器，可通过 Tor 访问，并接受匿名付款：比特币和现金（以及常规信用卡和 PayPal）。 |
| **[Tutanota](https://tutanota.com/)**               | 德国的免费开源电子邮件服务。它具有基本的直观的用户界面、安全的原生移动应用、匿名注册和一个.onion 网站。Tutanota 提供功能齐全的免费订阅，以及用于企业的高级订阅，允许使用自定义域名（每月 12 美元）。Tutanota 与大多数加密邮件提供商不使用 OpenPGP，而是使用标准化的混合方法，包括对称和非对称算法（128 位 AES 和 2048 位 RSA）。这在与使用 PGP 的联系人进行通信时会导致兼容性问题。但它确实允许加密更多的标头数据（正文、附件、主题行和发件人姓名等），而 PGP 邮件提供商无法做到这一点。 |
| **[Mailfence](https://mailfence.com?src=digitald)** | Mailfence 支持 OpenPGP，因此您可以独立于 Mailfence 服务器手动交换加密密钥，完全掌控加密过程。Mailfence 具有类似 Outlook 的简单用户界面，并附带日历、通讯录和文件功能。所有邮件设置都可以高度自定义，同时仍然清晰易用。注册不是匿名的，因为需要您的姓名和先前的电子邮件地址。有一个功能齐全的免费订阅，或者您可以订阅高级版，并使用自定义域名（每月 2.50 美元，或每月 7.50 美元，适用于 5 个域名），接受比特币、LiteCoin 或信用卡付款。 |
| **[MailBox.org](https://mailbox.org/)**             | 总部位于柏林的环保、安全电子邮件提供商。没有免费订阅，标准服务费用为 12 欧元/年。您可以使用自己的域名，并选择使用 [Catch-All 邮箱别名](https://kb.mailbox.org/display/MBOKBEN/Using+catch-all+alias+with+own+domain)。他们提供良好的帐户安全性和电子邮件加密，使用 OpenPGP，以及加密存储。没有专用应用程序，但它可以与任何标准的带有 SSL 的邮件客户端很好地配合使用。目前还没有匿名付款选项。 |
| **[Skiff](https://skiff.com/)**                     | 端到端加密的开源隐私优先电子邮件，还集成了 Web3 功能，如加密钱包和分散存储。Skiff 具有简单直观的用户界面，在 iOS 和 Android 上支持 [移动应用程序](https://skiff.com/download)，注册或创建帐户时不需要个人身份信息。Skiff 提供专业版订阅，提供额外的存储空间、别名、自定义域名等功能，每月收费 8 美元，可使用信用卡或加密钱包付款。 |

有关更多详细信息，请参阅 [OpenTechFund - Secure Email](https://github.com/OpenTechFund/secure-email)。

**另请参阅** [Comparison or Private Email Providers](https://github.com/Lissy93/email-comparison) 和 [Email Security Checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#emails)

#### 小提示
[HushMail](https://www.hushmail.com/tapfiliate/?tap_a=44784-d2adc0&tap_s=724845-260ce4&program=hushmail-for-small-business), [Soverin](https://soverin.net), [StartMail](https://www.startmail.com), [Posteo](https://posteo.de), [Lavabit](https://lavabit.com). 对于激进主义者和记者, 参阅 [Disroot](https://disroot.org/en), [Autistici](https://www.autistici.org), [CriptText](https://www.criptext.com/) 和 [RiseUp](https://riseup.net/en)

### 警告
使用端到端加密技术（如 OpenPGP）时，电子邮件标头中的一些元数据将不会被加密。
OpenPGP 也不支持前向安全性，这意味着如果您或收件人的私钥被盗，所有使用该私钥加密的先前消息都将被暴露。您应该谨慎保管好您的私钥。

### 自托管电子邮件

如果您不信任电子邮件提供者，可以自行托管邮件服务器。如果没有经验，正确配置邮件服务器可能会非常困难，尤其是在涉及到安全性方面。您可能会发现成本、性能和功能使其变得不太吸引人。如果您决定选择这个方案，[Mail-in-a-box](https://mailinabox.email/) 是一个易于部署的开源邮件服务器。它旨在促进 Web 上的去中心化、创新和隐私，并具有自动化、可审计和“幂等”系统配置。其他可用的自托管邮件选项包括 [Mailu](https://mailu.io/1.7/) 和 [Mail Cow](https://mailcow.email/)，它们都是 Docker 容器。

## 邮箱客户端
电子邮件客户端是用于与邮件服务器进行交互的程序。对于托管的电子邮件，您的电子邮件服务提供的 Web 和移动客户端通常是足够的，也可能是最安全的选择。对于自托管的电子邮件，您需要安装和配置适用于 Web、桌面或移动设备的邮件客户端。使用 IMAP 客户端的好处是，您始终可以获得所有电子邮件消息的离线备份（然后可以对其进行加密和归档），许多应用程序还允许您方便地聚合多个邮箱。桌面邮件客户端不容易受到常见的浏览器攻击，这是 Web 应用程序的弱点所在。


| 服务提供者 | 简介 |
| --- | --- |
| **[Mozilla Thunderbird](https://www.thunderbird.net)**（桌面） | 由 Mozilla 开发和支持的免费开源电子邮件应用程序，它安全、私密、易用且可自定义。~~Enigmail 附加组件可轻松加密/解密 PGP 消息~~，自版本 78.2.1 起已内置加密功能，而 TorBirdy 扩展可以通过 Tor 网络路由所有流量。分支版本（如 Betterbird）可能添加额外功能。 |
| **[eM Client](https://www.emclient.com/)**（桌面）           | 基于提高生产力的电子邮件客户端，适用于 Windows 和 MacOS。eM Client 拥有清晰的用户界面、快速的性能和良好的兼容性。付费版本提供一些实用功能，包括延迟收件箱、跟踪特定主题的回复、消息翻译、定时发送以及内置的日历、任务、联系人和备忘录。请注意，eM Client 是专有软件，不是开源的。 |
| **[SnappyMail](https://snappymail.eu)**（Web）               | 简洁、现代、快速的基于 Web 的邮件客户端。这是 [RainLoop](http://www.rainloop.net) 的仅支持 IMAP 的分支版本，修复了 [RainLoop 的一个严重漏洞](https://thehackernews.com/2022/04/unpatched-bug-in-rainloop-webmail-could.html)，并添加了几个新的 [功能](https://snappymail.eu/comparison)。 |
| **[RoundCube](https://roundcube.net)**（Web）                | 基于浏览器的多语言 IMAP 客户端，具有类似应用程序的用户界面。它提供了您对电子邮件客户端的所有期望功能，包括 MIME 支持、通讯录、文件夹操作、消息搜索和拼写检查。 |
| **[FairEmail](https://email.faircode.eu/)**（Android）       | 适用于 Android 的开源、功能齐全且易于使用的邮件客户端。支持无限数量的账户和电子邮件地址，并提供统一收件箱选项。简洁的用户界面，可选择暗黑模式，非常轻量且数据使用量极小。 |
| **[K-9 Mail](https://k9mail.app/)**（Android）               | K-9 是开源的，得到了很好的支持和信任——它的存在几乎与 Android 本身同样长久！支持多个账户、搜索、IMAP 推送邮件、多文件夹同步、标记、归档、签名、自我密送、PGP/MIME 等功能。安装 OpenKeychain 以便使用 OpenPGP 加密/解密电子邮件。 |
| **[p ≡ p](https://www.pep.security/)** (Android/ iOS)          | "Pretty Easy Privacy"（p ≡ p）客户端是一个完全去中心化且端到端加密的邮件客户端，用于实现 "自动隐私保护"。它具有一些不错的功能，但不是开源的。 |

#### 警告
邮件客户端的一个缺点是，许多客户端不支持双重身份验证（2FA），因此保护设备的安全性和加密很重要。

## 匿名邮件转发

在网上透露您真实的电子邮件地址可能会使您面临风险。电子邮件别名允许将消息发送到 [anything]@my-domain.com，而这些消息仍然会进入您的主要收件箱。这样可以保护您的真实电子邮件地址不被泄露。别名会在首次使用时自动生成。这种方法可以让您确定是哪个提供商泄露了您的电子邮件地址，并且可以通过一次点击来暂停别名的使用。

| 提供商                                                       | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **[Anonaddy](https://anonaddy.com)**                         | 一个开源的匿名电子邮件转发服务，允许您创建无限的电子邮件别名。有免费计划。 |
| **[33Mail](http://33mail.com/Dg0gkEA)**                      | 一个历史悠久的别名服务。除了接收邮件外，33Mail 还允许您匿名回复转发的地址。有免费计划，以及如果您想使用自定义域名的话，还有高级计划（每月 1 美元）。 |
| **[SimpleLogin](https://simplelogin.io?slref=bridsqrgvrnavso)** | 完全开源的别名服务，拥有许多附加功能。可以自行托管，或者使用托管的版本有免费计划，以及使用自定义域名的托管高级选项（每月 2.99 美元）。 |
| **[Firefox Private Relay](https://relay.firefox.com)**       | 由 Mozilla 开发和管理的 Firefox 插件，可让您通过一次点击创建电子邮件别名，并将所有消息转发到您的个人电子邮件。Relay 完全免费使用，非常适合经验较少的用户，同时也是 [开源的](https://github.com/mozilla/fx-private-relay)，并且可以自行托管以进行高级用途。 |
| **[ForwardEmail](https://forwardemail.net)**                 | 简单的开源全能邮件转发服务。易于自行托管（在 [GitHub 上查看](https://github.com/forwardemail/free-email-forwarding)），或者托管版本有免费计划以及高级计划（每月 3 美元）。 |
| **[ProtonMail](https://protonmail.com/pricing)（专业版或更高版本）** | 如果您已经拥有 ProtonMail 的专业版（8 欧元/月）或 Visionary 版（30 欧元/月），则可以通过 Catch-All Email 功能来实现此功能。 |

或者，您可以自己托管全能邮件服务。[Mailu](https://github.com/Mailu/Mailu) 可以配置为接受通配符，或者对于 Microsoft Exchange，请参阅 [exchange-catchall](https://github.com/Pro/exchange-catchall)。

#### 小提示
[mailhero.io](https://mailhero.io) 是一个小型服务，它没有内置的加密功能，因此您需要使用 PGP，但它是免费的。

## 邮件安全工具

| 服务提供者 | 简介 |
| --- | --- |
|**[Enigmail](https://www.enigmail.net)** | 邮件客户端附加组件，使用 OpenPGP 轻松加密、解密、验证和签署电子邮件。Enigmail 是免费且开源的，与 Interlink Mail & News 和 Postbox 兼容。他们的网站提供详尽的文档和快速入门指南，一旦设置完成，使用起来非常方便。 |
|**[Email Privacy Tester](https://www.emailprivacytester.com/)** | 快速工具，可以测试您的邮件客户端在您打开邮件之前是否“读取”您的邮件，并检查您的邮件客户端允许发送给发件人的哪些分析数据、已读回执或其他跟踪数据。这个系统是开源的（[在 GitLab 上](https://gitlab.com/mikecardwell/ept3)），可信的，由 [Mike Cardwell](https://www.grepular.com/) 开发，但如果您不想使用真实的电子邮件，可以创建一个与同一提供商的第二个帐户，应该会得到相同的结果。 |
|**[DKIM Verifier](https://addons.thunderbird.net/en-US/thunderbird/addon/dkim-verifier/?collection_id=a5557f08-eafd-7a39-81c6-09127da790f7)** | 验证 DKIM 签名并在电子邮件头中显示结果，以帮助发现伪造的邮件（不来自它们声称的域）。 |

#### 小提示
如果您正在使用 ProtonMail，那么 [ProtonMail Bridge](https://protonmail.com/bridge/thunderbird) 可以让您将电子邮件同步到您自己的桌面邮件客户端。它与 Thunderbird、Microsoft Outlook 和其他客户端配合良好。

## VOIP客户端

| 服务提供者 | 简介 |
| --- | --- |
|**[Mumble](https://github.com/mumble-voip/mumble)** | 开源的、低延迟、高质量的语音聊天软件。您可以托管自己的服务器，或使用托管的实例，它支持 Windows、MacOS 和 Linux 的客户端应用程序，以及 Android 和 iOS 的第三方应用程序。 |
|**[Linphone](https://www.linphone.org)** | 开源的音频、视频和即时通讯群组，具有端到端加密和内置媒体服务器。基于 [SIP](https://en.wikipedia.org/wiki/Session_Initiation_Protocol)，正在发展为 [RCS](https://en.wikipedia.org/wiki/Rich_Communication_Services)。原生应用程序适用于 Android、iOS、Windows、GNU/Linux 和 MacOS。 |

#### 小提示
[SpoofCard](https://www.spoofcard.com/) 可以让您进行匿名电话呼叫和留言，但它不是开源的，并且关于安全性的信息有限（请避免发送任何敏感信息）。
[MicroSip](https://www.microsip.org/) 是一个基于 PJSIP 堆栈的开源便携式 Windows SIP 软件电话。

## 虚拟手机号

| 服务提供者 | 简介 |
| --- | --- |
|**[Silent.link](https://silent.link/)** | 匿名的 eSIM，用于发送/接收短信、接听电话和使用 4G/5G 互联网+全球漫游。注册时不需要个人数据。价格实惠，接受比特币付款和充值。需要支持 eSIM 的设备。 |
|**[Crypton.sh](https://crypton.sh/)** | 云中的物理 SIM 卡，用于发送和接收短信。使用您选择的私钥加密消息。提供 Web 界面和 API，可从任何设备进行交互。价格约为 7.00 欧元/月，接受比特币、门罗币或信用卡付款。 |
|**[Jmp.chat](https://jmp.chat/)** | 提供由 Soprani 提供的用于呼入和呼出电话和短信的电话号码。适用于 Jabber、Matrix、Snikket、XMPP 或任何 SIP 客户端。定价从每月 2.99 美元起。目前仅在美国和加拿大提供，因为（截至 2022 年）该服务仍处于测试阶段。 |
|**[MoneroSMS](https://monerosms.com)** | 匿名短信服务，可用于激活账户。可通过 Web、CLI 或电子邮件访问。定价从每月 3.60 美元起。该服务截至 2022 年仍处于测试阶段。 |

## 团队协作平台

现在，我们越来越依赖软件来帮助团队协作。不幸的是，许多流行的选项，如 [Slack](https://www.wired.co.uk/article/slack-privacy-settings-notifications)、[Microsoft Teams](https://www.wired.co.uk/article/microsoft-teams-meeting-data-privacy)、[Google for Work](https://www.wired.com/story/google-tracks-you-privacy/) 和 [Discord](https://cybernews.com/privacy/discord-privacy-tips-that-you-should-use-in-2020/)，都存在一些严重的隐私问题。

团队协作软件的典型功能包括：即时消息、封闭和开放的群组消息、语音和视频会议、文件共享/文件传输以及一定程度的日程安排功能。

| 服务提供者 | 简介 |
| --- | --- |
|**[Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)** | 易于部署的自托管团队协作平台，配备稳定且功能丰富的跨平台客户端应用程序。用户界面快速、美观且直观，因此用户对该平台的要求很少需要技术经验。Rocket.Chat 的功能集类似于 Slack，使其成为希望更好地控制数据的团队的良好替代品。 |
|**[RetroShare](https://retroshare.cc/)** | 安全的群组通信，可选择通过 Tor 或 I2P 使用。使用分散式聊天室进行快速直观的群组和一对一聊天，支持文本和富媒体，具有向离线联系人发送消息的邮件功能。频道功能使不同团队的成员能够保持互相更新，并共享文件。还包括内置论坛、链接聚合、文件共享以及语音和视频通话。RetroShare 的使用相对复杂，用户界面相当 "复古"，因此可能不适合非技术团队。 |
|**[Element](https://element.io/)** | 使用 Matrix 协议的注重隐私的即时通讯工具。Element 客户端支持群组聊天室、媒体共享以及语音和视频群组通话。 |
|**Internet Relay Chat** | 基于 IRC 的解决方案是另一个选择，由于其分散化的特性，没有单点故障，并且易于自行托管。但是，在配置 IRC 实例时保持安全性非常重要，并确保频道得到适当加密-IRC 更适用于开放式通信。有多种客户端可供选择-流行的选项包括：[The Longe](https://thelounge.chat/)（基于 Web）、[HexChat](https://hexchat.github.io/)（Linux）、[Pidgin](https://pidgin.im/help/protocols/irc/)（Linux）、[WeeChat](https://weechat.org/)（Linux，基于终端）、[IceChat](https://www.icechat.net/)（Windows）、[XChat Aqua](https://xchataqua.github.io/)（MacOS）、[Palaver](https://palaverapp.com/)（iOS）和 [Revolution](https://github.com/MCMrARM/revolution-irc)（Android）。 |
|**[Mattermost](https://mattermost.org/)** | Mattermost 有一个开源版本，可以自行托管。它是 Slack 的良好替代品，具有原生的桌面、移动和 Web 应用程序，以及各种各样的 [集成](https://integrations.mattermost.com/)。 |
|**[Dialog](https://dlg.im/en/)** | 一款企业安全的协作信息工具。简洁的用户界面和所有基本功能，包括群组、文件共享、音频/视频通话、搜索和聊天机器人。 |

### 小提示
有些聊天平台允许进行跨平台的群组聊天、语音和视频会议，但没有额外的协作功能。例如，[Tox](https://tox.chat/)、[Session](https://getsession.org/)、[Ricochet](https://ricochet.im/)、[Mumble](https://www.mumble.info/) 和 [Jami](https://jami.net/)。

对于会议，[OSEM](https://osem.io) 是一个开源的全能会议管理工具，提供注册、日程安排、直播和录播会议、论文提交、营销页面和管理功能。

<hr id="security-tools" />

## Browser Extensions

The following browser add-ons give you better control over what content is able to be loaded and executed while your browsing.

| Provider | Description |
| --- | --- |
**[Privacy Badger](https://www.eff.org/privacybadger)** | Blocks invisible trackers, in order to stop advertisers and other third-parties from secretly tracking where you go and what pages you look at. **Download**: [Chrome][privacy-badger-chrome] \ [Firefox][privacy-badger-firefox]
**[HTTPS Everywhere](https://eff.org/https-everywhere)** | Forces sites to load in HTTPS, in order to encrypt your communications with websites, making your browsing more secure (Similar to [Smart HTTPS](https://mybrowseraddon.com/smart-https.html)). Note this functionality is now included by default in most modern browsers. **Download**: [Chrome][https-everywhere-chrome] \ [Firefox][https-everywhere-firefox]
**[uBlock Origin](https://github.com/gorhill/uBlock)** | Block ads, trackers and malware sites. **Download**: [Chrome][ublock-chrome] \ [Firefox][ublock-firefox]
**[ScriptSafe](https://github.com/andryou/scriptsafe)** | Allows you to block the execution of certain scripts. **Download**: [Chrome][script-safe-chrome] \ [Firefox][script-safe-firefox]
**[Firefox Multi-Account Containers](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)** | Firefox Multi-Account Containers lets you keep parts of your online life separated into color-coded tabs that preserve your privacy. Cookies are separated by container, allowing you to use the web with multiple identities or accounts simultaneously. **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/)
**[Temporary Containers](https://github.com/stoically/temporary-containers)** | This Extension, combined with Firefox Multi-Account Containers, let's you isolate cookies and other private data for each web site. **Download**: [Firefox](https://github.com/stoically/temporary-containers)
**[WebRTC-Leak-Prevent](https://github.com/aghorler/WebRTC-Leak-Prevent)** | Provides user control over WebRTC privacy settings in Chromium, in order to prevent WebRTC leaks. **Download**: [Chrome][web-rtc-chrome]. For Firefox users, you can do this through [browser settings](https://www.privacytools.io/browsers/#webrtc). Test for WebRTC leaks, with [browserleaks.com/webrtc](https://browserleaks.com/webrtc)
**[Canvas Fingerprint Blocker](https://add0n.com/canvas-fingerprint-blocker.html)** | Block fingerprint without removing access to HTML5 Canvas element. Canvas fingerprinting is commonly used for tracking, this extension helps to mitigate this through disallowing the browser to generate a true unique key <br> **Download:** [Chrome](https://chrome.google.com/webstore/detail/canvas-blocker-fingerprin/nomnklagbgmgghhjidfhnoelnjfndfpd) \ [Firefox](https://addons.mozilla.org/en-US/firefox/addon/canvas-blocker-no-fingerprint/) \ [Edge](https://microsoftedge.microsoft.com/addons/detail/ahiddppepedlomdleppkbljnmkchlmdc) \ [Source](https://github.com/joue-quroi/canvas-fingerprint-blocker)
**[ClearURLs](https://gitlab.com/KevinRoebert/ClearUrls)** | This extension will automatically remove tracking elements from the GET parameters of URLs to help protect some privacy <br> **Download**: [Chrome](https://chrome.google.com/webstore/detail/clearurls/lckanjgmijmafbedllaakclkaicjfmnk) \ [Firefox](https://addons.mozilla.org/en-US/firefox/addon/clearurls/) / [Source](https://gitlab.com/KevinRoebert/ClearUrls)
**[CSS Exfil Protection](https://www.mike-gualtieri.com/css-exfil-vulnerability-tester)** | Sanitizes and blocks any CSS rules which may be designed to steal data, in order to guard against Exfil attacks <br> **Download**: [Chrome](https://chrome.google.com/webstore/detail/css-exfil-protection/ibeemfhcbbikonfajhamlkdgedmekifo) \ [Firefox](https://addons.mozilla.org/en-US/firefox/addon/css-exfil-protection/) \ [Source](https://github.com/mlgualtieri/CSS-Exfil-Protection)
**[First Party Isolation](https://github.com/mozfreddyb/webext-firstpartyisolation)** | Enables the First Party isolation preference (Clicking the Fishbowl icon temporarily disables it) <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/first-party-isolation/)
**[Privacy-Oriented Origin Policy](https://claustromaniac.github.io/poop/)** | Prevent Firefox from sending Origin headers when they are least likely to be necessary, to protect your privacy <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/privacy-oriented-origin-policy/) \ [Source](https://github.com/claustromaniac/poop)
**[LocalCDN](https://codeberg.org/nobody/LocalCDN/)** | Emulates remote frameworks (e.g. jQuery, Bootstrap, Angular) and delivers them as local resource. Prevents unnecessary 3rd party requests to tracking CDNs <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/localcdn-fork-of-decentraleyes/)
**[Decentraleyes](https://decentraleyes.org)** | Similar to LocalCDN, Serves up local versions of common scripts instead of calling to 3rd-party CDN. Improves privacy and load times. Works out-of-the-box and plays nicely with regular content blockers. **Download**: [Chrome][decentraleyes-chrome] \ [Firefox][decentraleyes-firefox] \ [Opera][decentraleyes-opera] \ [Pale Moon][decentraleyes-pale-moon] \ [Source][decentraleyes-source]
**[Privacy Essentials](https://duckduckgo.com/app)** | Simple extension by DuckDuckGo, which grades the security of each site. **Download**: [Chrome][privacy-essentials-chrome] \ [Firefox][privacy-essentials-firefox]
**[Self-Destructing Cookies](https://add0n.com/self-destructing-cookies.html)** | Prevents websites from tracking you by storing unique cookies (note Fingerprinting is often also used for tracking). It removes all related cookies whenever you end a session. **Download**: [Chrome][self-destructing-cookies-chrome] \ [Firefox][self-destructing-cookies-firefox] \ [Opera][self-destructing-cookies-opera] \ [Source][self-destructing-cookies-source]
**[Privacy Redirect](https://github.com/SimonBrazell/privacy-redirect)** | A simple web extension that redirects Twitter, YouTube, Instagram & Google Maps requests to privacy friendly alternatives <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/privacy-redirect/) / [Chrome](https://chrome.google.com/webstore/detail/privacy-redirect/pmcmeagblkinmogikoikkdjiligflglb)
**[Site Bleacher](https://github.com/wooque/site-bleacher)** | Remove automatically cookies, local storages, IndexedDBs and service workers <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/site-bleacher/) \ [Chrome](https://chrome.google.com/webstore/detail/site-bleacher/mlcfcepfmnjphcdkfbfgokkjodlkmemo) \ [Source](https://github.com/wooque/site-bleacher)
**[User Agent Switcher](https://add0n.com/useragent-switcher.html)** | Spoofs browser's User-Agent string, making it appear that you are on a different device, browser and version to what you are actually using. This alone does very little for privacy, but combined with other tools, can allow you to keep your fingerprint changing, and feed fake info to sites tracking you. Some websites show different content, depending on your user agent.<br> **Download**: [Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher/bhchdcejhohfmigjafbampogmaanbfkg) \ [Fireforx](https://addons.mozilla.org/firefox/addon/user-agent-string-switcher/) \ [Edge](https://microsoftedge.microsoft.com/addons/detail/cnjkedgepfdpdbnepgmajmmjdjkjnifa) \ [Opera](https://addons.opera.com/extensions/details/user-agent-switcher-8/) \ [Source](https://github.com/ray-lothian/UserAgent-Switcher/)
**[PrivacySpy](https://privacyspy.org)** | The companian extension for PrivacySpy.org - an open project that rates, annotates, and archives privacy policies. The extension shows a score for the privacy policy of the current website.<br> **Download**: [Chrome](https://chrome.google.com/webstore/detail/privacyspy/ppembnadnhiknioggbglgiciihgmkmnd) \ [Fireforx](https://addons.mozilla.org/en-US/firefox/addon/privacyspy/)
**[HTTPZ](https://github.com/claustromaniac/httpz)** | Simplified HTTPS upgrades for Firefox (lightweight alternative to HTTPS-Everywhere) <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/httpz/)
**[Skip Redirect](https://github.com/sblask/webextension-skip-redirect)** | Some web pages use intermediary pages before redirecting to a final page. This add-on tries to extract the final url from the intermediary url and goes there straight away if successful <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/skip-redirect/) \ [Source](https://github.com/sblask/webextension-skip-redirect)
**[Web Archives](https://github.com/dessant/web-archives/wiki/Search-engines)** | View archived and cached versions of web pages on 10+ search engines, such as the Wayback Machine, Archive.is, Google etc Useful for checking legitimacy of websites, and viewing change logs <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/view-page-archive/) \ [Chrome](https://chrome.google.com/webstore/detail/web-archives/hkligngkgcpcolhcnkgccglchdafcnao) \ [Edge](https://microsoftedge.microsoft.com/addons/detail/apcfghlggldjdjepjnahfdjgdcdekhda) \ [Source](https://github.com/dessant/web-archives)
**[Flagfox](https://flagfox.wordpress.com/)** | Displays a country flag depicting the location of the current website's server, which can be useful to know at a glance. Click icon for more tools such as site safety checks, whois, validation etc <br> **Download**: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/flagfox/)
**[Lightbeam](https://github.com/mozilla/lightbeam-we)** | Visualize in detail the servers you are contacting when you are surfing on the Internet. Created by Gary Kovacs (former CEO of Mozilla), presented in his [TED Talk](https://www.ted.com/talks/gary_kovacs_tracking_our_online_trackers). **Download**: [Firefox][lightbeam-firefox] \ [Source][lightbeam-source]
**[Track Me Not](http://trackmenot.io)** | Helps protect web searchers from surveillance and data-profiling, through creating meaningless noise and obfuscation, outlined in their [whitepaper][tmn-whitepaper]. Controversial whether or not this is a good approach **Download**: [Chrome][tmn-chrome] \ [Firefox][tmn-firefox] \ [Source][tmn-source]
**[AmIUnique Timeline](https://amiunique.org/timeline)** | Enables you to better understand the evolution of browser fingerprints (which is what websites use to uniquely identify and track you). **Download**: [Chrome][amiunique-chrome] \ [Firefox][amiunique-firefox]
**[Netcraft Extension](https://www.netcraft.com/apps/browser)** | Notifies you when visiting a known or potential phishing site, and detects suspicious JavaScript (including skimmers and miners). Also provides a simple rating for a given sites legitimacy and security. Great for less technical users. Netcraft also has a handy online tool: [Site Report](https://sitereport.netcraft.com/) for checking what any given website is running. **Download**: [Chrome](https://chrome.google.com/webstore/detail/netcraft-anti-phishing-ex/bmejphbfclcpmpohkggcjeibfilpamia) \ [Firefox](https://addons.mozilla.org/en-us/firefox/addon/netcraft-toolbar?src=external-apps-hero) \ [Opera](https://addons.opera.com/en/extensions/details/netcraft-anti-phishing-extension/) \ [Edge](https://microsoftedge.microsoft.com/addons/detail/netcraft-extension/ngjhgbnmdjjnmejmpamalgnlnmopllkm)

#### Notable Mention
[Extension source viewer](https://addons.mozilla.org/en-US/firefox/addon/crxviewer) is a handy extension for viewing the source code of another browser extension, which is a useful tool for verifying the code does what it says 

#### Word of Warning
- _Having many extensions installed raises entropy, causing your fingerprint to be more unique, hence making tracking easier._
- _Much of the functionality of the above addons can be applied without installing anything, by configuring browser settings yourself. For Firefox this is done in the user.js_
- _Be careful when installing unfamiliar browser add-ons, since some can compromise your security and privacy. At the time of writing, the above list were all open source, verified and 'safe' extensions._
- _In most situations, only a few of the above extensions will be needed in combination._
- _See the [arkenfox wiki](https://github.com/arkenfox/user.js/wiki/4.1-Extensions) for more information on the obsolescence and purposelessness of many popular extensions, and why you may only need a very limited set._

**See also** [Browser & Search Security Checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#browser-and-search)


## Mobile Apps

| Provider | Description |
| --- | --- |
**[Orbot]** | System-wide Tor proxy, which encrypts your connection through multiple nodes. You can also use it alongside [Tor Browser] to access .onion sites.
**[NetGuard]** | A firewall app for Android, which does not require root. NetGuard provides simple and advanced ways to block access to the internet, where applications and addresses can individually be allowed or denied access to your Wi-Fi and/or mobile connection.
**[Island]** | A sandbox environment, allowing you to clone selected apps and run them in an isolated box, preventing it from accessing your personal data, or device information
**[Insular]** | An actively-maintained fork of the dead Island project with additional enhancements
**[Exodus]** | Shows which trackers, each of your installed apps is using, so that you can better understand how your data is being collected. Uses data from the Exodus database of scanned APKs.
**[Bouncer]** | Gives you the ability to grant permissions temporarily, so that you could for example use the camera to take a profile picture, but when you close the given app, those permissions will be revoked
**[XPrivacyLua](https://github.com/M66B/XPrivacyLua/)** | Simple to use privacy manager for Android, that enables you to feed apps fake data when they request intimate permissions. Solves the problem caused by apps malfunctioning when you revoke permissions, and protects your real data by only sharing fake information. Enables you to hide call log, calendar, SMS messages, location, installed apps, photos, clipboard, network data plus more. And prevents access to camera, microphone, telemetry, GPS and other sensors
**[SuperFreezZ]** | Makes it possible to entirely freeze all background activities on a per-app basis. Intended purpose is to speed up your phone, and prolong battery life, but this app is also a great utility to stop certain apps from collecting data and tracking your actions while running in the background
**[Haven]** | Allows you to protect yourself, your personal space and your possessions - without compromising on security. Leveraging device sensors to monitor nearby space, Haven was developed by [The Guardian Project](https://guardianproject.info/), in partnership with [Edward Snowden](https://techcrunch.com/2017/12/24/edward-snowden-haven-app/)
**[XUMI Security]** |  Checks for, and resolves known security vulnerabilities. Useful to ensure that certain apps, or device settings are not putting your security or privacy at risk
**[Daedalus]** | No root required Android DNS modifier and hosts/DNSMasq resolver, works by creating a VPN tunnel to modify the DNS settings. Useful if you want to change your resolver to a more secure/ private provider, or use DNS over HTTPS
**[Secure Task]** | Triggers actions, when certain security conditions are met, such as multiple failed login attempts or monitor settings changed. It does require [Tasker], and needs to be set up with ADB, device does not need to be rooted
**[Cryptomator]** | Encrypts files and folders client-side, before uploading them to cloud storage (such as Google Drive, One Drive or Dropbox), meaning none of your personal documents leave your device in plain text
**[1.1.1.1]** | Lets you use CloudFlares fast and secure 1.1.1.1 DNS, with DNS over HTTPS, and also has the option to enable CloudFlares WARP+ VPN
**[Fing App]** | A network scanner to help you monitor and secure your WiFi network. The app is totally free, but to use the advanced controls, you will need a [Fing Box](https://amzn.to/2vFDF4n)
**[FlutterHole]** | Easy monitoring and controll over your [Pi Hole](https://pi-hole.net/) instance. Pi Hole is great for security, privacy and speed
**[DPI Tunnel](https://github.com/zhenyolka/DPITunnel)** | An application for Android that uses various techniques to bypass DPI (Deep Packet Inspection) systems, which are used to block some sites (not available on Play store)
**[Blokada](https://blokada.org/)** | This application blocks ads and trackers, doesn't require root and works for all the apps on your Android phone. Check out how it works [here](https://block.blokada.org/post/2018/06/17/how-does-blokada-work/).
**[SnoopSnitch](https://f-droid.org/en/packages/de.srlabs.snoopsnitch/)** | Collects and analyzes mobile radio data to make you aware of your mobile network security and to warn you about threats like fake base stations (IMSI catchers), user tracking and over-the-air updates
**[TrackerControl](https://f-droid.org/en/packages/net.kollnig.missioncontrol.fdroid/)** | Monitor and control hidden data collection in mobile apps about user behavior/ tracking
**[Greentooth](https://f-droid.org/en/packages/com.smilla.greentooth/)** | Auto-disable Bluetooth, then it is not being used. Saves battery, and prevent some security risks
**[PrivateLock](https://f-droid.org/en/packages/com.wesaphzt.privatelock/)** | Auto lock your phone based on movement force/ acceleration
**[CamWings](https://schiffer.tech/camwings-mobile.html)** | Prevent background processes gaining unauthorized access to your devices camera. Better still, use a [webcam sticker](https://supporters.eff.org/shop/laptop-camera-cover-set-ii)
**[ScreenWings](https://schiffer.tech/screenwings-mobile.html)** | Prevent background processes taking unauthorized screenshots, which could expose sensitive data
**[AFWall+](https://github.com/ukanth/afwall/)** | Android Firewall+ (AFWall+) is an advanced iptables editor (GUI) for rooted Android devices, which provides very fine-grained control over which Android apps are allowed to access the network
**[Catch the Man-in-the-Middle](https://play.google.com/store/apps/details?id=me.brax.certchecker)** | Simple tool, that compares SHA-1 fingerprints of the the SSL certificates seen from your device, and the certificate seen from an external network. If they do not match, this may indicate a man-in-the-middle modifying requests
**[RethinkDNS + Firewall](https://github.com/celzero/rethink-app)** | An open-source ad-blocker and firewall app for Android 6+ (does not require root)
**[F-Droid](https://f-droid.org/)** | F-Droid is an installable catalogue of FOSS applications for Android. The client enabled you to browse, install, and keep track of updates on your device

#### Word of Warning
Too many installed apps will increase your attack surface - only install applications that you need 

#### Other Notable Mentions
For more open source security & privacy apps, check out these publishers: [The Guardian Project], [The Tor Project], [Oasis Feng], [Marcel Bokhorst], [SECUSO Research Group] and [Simple Mobile Tools]- all of which are trusted developers or organisations, who've done amazing work.

For offensive and defensive security, see The Kali [Nethunter Catalogue](https://store.nethunter.com/en/packages) of apps

For *advanced* users, the following tools can be used to closely monitor your devise and networks, in order to detect any unusual activity. [PortDroid] for network analysis, [Packet Capture] to monitor network traffic, [SysLog] for viewing system logs, [Dexplorer] to read .dex or .apk files for your installed apps, and [Check and Test] to check status and details of devices hardware.

**See also** [Mobile Security Checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md#mobile-devices)


## Online Tools

A selection of free online tools and utilities, to check, test and protect

| Provider | Description |
| --- | --- |
**[';--have i been pwned?](https://haveibeenpwned.com)** | Checks if your credentials (Email address or Password) have been compromised in a data breach. See also [Firefox Monitor](https://monitor.firefox.com)
**[ε xodus](https://reports.exodus-privacy.eu.org)** | Checks how many, and which trackers any Android app has. Useful to understand how data is being collected before you install a certain APK, it also shows which permissions the app asks for
**[Am I Unique?](https://amiunique.org)** | Show how identifiable you are on the Internet by generating a fingerprint based on device information. This is how many websites track you (even without cookies enabled), so the aim is to not be unique
**[Panopticlick](https://panopticlick.eff.org/)** | Check if your browser safe against tracking. Analyzes how well your browser and add-ons protect you against online tracking techniques, and if your system is uniquely configured—and thus identifiable
**[Phish.ly](https://phish.ly/)** | Analyzes emails, checking the URLs and creating a SHA256 and MD5 hash of attachments, with a link to VirusTotal. To use the service, just forward a potentially malicious or suspicious email to scan@phish.ly, and an automated reply will include the results. They claim that all email data is purged after analysis, but it would be wise to not include any sensitive information, and to use a forwarding address
**[Browser Leak Test](https://browserleaks.com)** | Shows which of personal identity data is being leaked through your browser, so you can better protect yourself against fingerprinting
**[IP Leak Test](https://ipleak.net)** | Shows your IP address, and other associated details (location, ISP, WebRTC check, DNS, and lots more)
**[EXIF Remove](https://www.exifremove.com)** | Displays, and removes Meta and EXIF data from an uploaded photo or document
**[Redirect Detective](https://redirectdetective.com)** | Check where a suspicious URL redirects to (without having to click it). Lets you avoid being tracked by not being redirected via adware/tracking sites, or see if a shortened link  actually resolves a legitimate site, or see if link is an affiliate ad
**[Blocked.org](https://www.blocked.org.uk)** | Checks if a given website is blocked by filters applied by your mobile and broadband Internet Service Providers (ISP)
**[Virus Total](https://www.virustotal.com)** | Analyses a potentially-suspicious web resources (by URL, IP, domain or file hash) to detect types of malware (*note: files are scanned publicly*)
**[Hardenize](https://www.hardenize.com/)** | Scan websites and shows a security overview, relating to factors such as HTTPS, domain info, email data, www protocols and so on
**[Is Legit?](https://www.islegitsite.com/)** | Checks if a website or business is a scam, before buying something from it
**[Deseat Me](https://www.deseat.me)** | Tool to help you clean up your online presence - Instantly get a list of all your accounts, delete the ones you are not using
**[Should I Remove It?](https://www.shouldiremoveit.com)** | Ever been uninstalling programs from your Windows PC and been unsure of what something is? Should I Remove It is a database of Windows software, detailing whether it is essential, harmless or dangerous
**[10 Minute Mail](https://10minemail.com/)** | Generates temporary disposable email address, to avoid giving your real details
**[MXToolBox Mail Headers](https://mxtoolbox.com/Public/Tools/EmailHeaders.aspx)** | Tool for analyzing email headers, useful for checking the authenticity of messages, as well as knowing what info you are revealing in your outbound messages
**[Am I FloCed?](https://amifloced.org/)** | Google testing out a new tracking feature called Federated Learning of Cohorts (aka "FLoC"). It currently effects 0.5% of Chrome users, this tool developed by the EFF will detect if you are affected, and provide additional info on how to stay protected
**[Site Report](https://sitereport.netcraft.com/)** | A tool from Netcraft, for analysing what any given website is running, where it's located and information about its host, registrar, IP and SSL certificates.

#### Word of Warning
*Browsers are inherently insecure, be careful when uploading, or entering personal details.*

<hr id="networking" />

## Virtual Private Networks

VPNs are good for getting round censorship, increasing protection on public WiFi, obscuring your IP address, and reducing what data your ISP can log. But for the best anonymity, you should use [Tor](https://www.torproject.org/). VPNs do not mean you are magically protected, or anonymous (see below). 

| Provider | Description |
| --- | --- |
**[Mullvad](http://mullvad.net/en/)** | Mullvad is one of the best for privacy, they have a totally anonymous sign up process, you don't need to provide any details at all, you can choose to pay anonymously too (with Monero, BTC or cash)
**[Azire](https://www.azirevpn.com/)** |  Azire is a Swedish VPN provider, who owns their own hardware with physically removed storage and a no logging policy. Pricing starts at € 3.25/mo, with crypto (including XMR) supported. Note that they've not yet been audited, and client applications are not open source, for more info, see [#140](https://github.com/Lissy93/personal-security-checklist/issues/140).
**[IVPN](https://www.ivpn.net/)** | Independently Security Audited VPN with anonymous signup, no logs, no cloud or customer data stored, open-source apps and website. Strong ethics: no trackers, no false promises, no surveillance ads. Accepts various payment methods including crypotcurrencies. 
**[ProtonVPN](https://protonvpn.com/)** | From the creators of ProtonMail, ProtonVPN has a solid reputation. They have a full suite of user-friendly native mobile and desktop apps. ProtonVPN is one of the few "trustworthy" providers that also offer a free plan
**[OVPN](https://www.ovpn.com/)** | A court-proven VPN service with support for Wireguard and OpenVPN support, and optional ad-blocking. Running on dedicated hardware, with no hard drives

#### Word of Warning
- *A VPN does not make you anonymous - it merely changes your public IP address to that of your VPN provider, instead of your ISP. Your browsing session can still be linked back to your real identity either through your system details (such as user agent, screen resolution even typing patterns), cookies/ session storage, or by the identifiable data that you enter. [Read more about fingerprinting](https://pixelprivacy.com/resources/browser-fingerprinting/)*
- *Logging - If you choose to use a VPN because you do not agree with your ISP logging your full browsing history, then it is important to keep in mind that your VPN provider can see (and mess with) all your traffic. Many VPNs claim not to keep logs, but you cannot be certain of this ([VPN leaks](https://vpnleaks.com/)). See [this article](https://gist.github.com/joepie91/5a9909939e6ce7d09e29) for more*
- *IP Leaks - If configured incorrectly, your IP may be exposed through a DNS leak. This usually happens when your system is unknowingly accessing default DNS servers rather than the anonymous DNS servers assigned by an anonymity network or VPN. Read more: [What is a DNS leak](https://www.dnsleaktest.com/what-is-a-dns-leak.html), [DNS Leak Test](https://www.dnsleaktest.com), [How to Fix a DNS Leak](https://www.dnsleaktest.com/how-to-fix-a-dns-leak.html)*
- *Stealth - It will be visible to your adversary that you are using a VPN (usually from the IP address), but other system and browser data, can still reveal information about you and your device (such as your local time-zone, indicating which region you are operating from)*
- *Many reviews are sponsored, and hence biased. Do your own research, or go with one of the above options*
- *Using [Tor](https://www.torproject.org) (or another [Mix Network](/5_Privacy_Respecting_Software.md#mix-networks)) may be a better option for anonimity*

#### Considerations
*While choosing a VPN, consider the following: Logging policy (logs are bad), Jurisdiction (avoid 5-eyes), Number of servers, availability and average load. Payment method (anonymous methods such as BTC, Monero or cash are better), Leak protection (1st-party DNS servers = good, and check if IPv6 is supported), protocols (OpenVPN and WireGuard = good). Finally, usability of their apps, user reviews and download speeds.*

#### Self-Hosted VPN
If you don't trust a VPN provider not to keep logs, then you could self-host your own VPN. This gives you you total control, but at the cost of anonymity (since your cloud provider, will require your billing info). See [Streisand](https://github.com/StreisandEffect/streisand), to learn more, and get started with running a VPN.
[Digital Ocean](https://m.do.co/c/3838338e7f79) provides flexible, secure and easy Linux VMs, (from $0.007/hour or $ 5/month), this guide explains how to set up VPN on: [CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-set-up-and-configure-an-openvpn-server-on-centos-7) or [Ubuntu 18.4+](https://www.digitalocean.com/community/tutorials/how-to-set-up-and-configure-an-openvpn-server-on-centos-7). See more about configuring [OpenVPN](https://openvpn.net/vpn-server-resources/digital-ocean-quick-start-guide/) or [IKEv2](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-ikev2-vpn-server-with-strongswan-on-ubuntu-18-04-2). Alternatively, here is a [1-click install script](http://dovpn.carlfriess.com/) for  on [Digital Ocean](https://m.do.co/c/3838338e7f79), by Carl Friess.

Recently distributed self-hosted solutions for running your own VPNs have become more popular, with services like [Outline](https://getoutline.org/) letting you spin up your own instance and share it with friends and family. Since it's distributed, it is very resistant to blocking, and gives you world-wide access to the free and open internet. And since you have full control over the server, you can be confident that there is no logging or monitoring happening. However it comes at the cost of anonymity, especially if it's only you using your instance.

## Self-Hosted Network Security

Fun little projects that you can run on a Raspberry Pi, or other low-powered computer. In order to help detect and prevent threats, monitor network and filter content

| Provider | Description |
| --- | --- |
**[Pi-Hole](https://pi-hole.net)** | Network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole. Pi-Hole can significantly speed up your internet, remove ads and block malware. It comes with a nice web interface and a mobile app with monitoring features, it's open source, easy to install and very widely used
**[Technitium](https://technitium.com/dns/)** | Another DNS server for blocking privacy-invasive content at it's source. Technitium doesn't require much of a setup, and basically works straight out of the box, it supports a wide range of systems (and can even run as a portable app on Windows). It allows you to do some additional tasks, such as add local DNS addresses and zones with specific DNS records. Compared to Pi-Hole, Technitium is very lightweight, but lacks the deep insights that Pi-Hole provides, and has a significantly smaller community behind it
**[IPFire](https://www.ipfire.org)** | A hardened, versatile, state-of-the-art open source firewall based on Linux. Its ease of use, high performance and extensibility make it usable for everyone
**[PiVPN](https://pivpn.io)** | A simple way to set up a home VPN on a any Debian server. Supports OpenVPN and WireGuard with elliptic curve encryption keys up to 512 bit. Supports multiple DNS providers and custom DNS providers - works nicely along-side PiHole
**[E2guardian](http://e2guardian.org)** | Powerful open source web content filter
**[SquidGuard](http://www.squidguard.org)** | A URL redirector software, which can be used for content control of websites users can access. It is written as a plug-in for Squid and uses blacklists to define sites for which access is redirected
**[PF Sense](https://www.pfsense.org)** | Widely used, open source firewall/router
**[Zeek](https://www.zeek.org)** |  Detect if you have a malware-infected computer on your network, and powerful network analysis framework and monitor
**[Firezone](https://github.com/firezone/firezone)** | Open-source self-hosted VPN and firewall built on WireGuard ®.

Don't want to build? See also: [Pre-configured security boxes](https://github.com/Lissy93/personal-security-checklist/blob/master/6_Privacy_and-Security_Gadgets.md#network-security)


## Mix Networks
[Mix networks](https://en.wikipedia.org/wiki/Mix_network) are routing protocols, that create hard-to-trace communications, by encrypting and routing traffic through a series of nodes. They help keep you anonymous online, and unlike VPNs -there are no logs

| Provider | Description |
| --- | --- |
**[Tor](https://www.torproject.org)** | Tor provides robust anonymity, allowing you to defend against surveillance, circumvent censorship and reduce tracking. It blocks trackers, resists fingerprinting and implements multi-layered encryption by default, meaning you can browse freely. Tor also allows access to OnionLand: hidden services
**[I2P](https://geti2p.net)** | I2P offers great generic transports, it is well geared towards accessing hidden services, and has a couple of technical benefits over Tor: P2P friendly with unidirectional short-lived tunnels, it is packet-switched (instead of circuit-switched) with TCP and UDP, and continuously profiles peers, in order to select the best performing ones. <br> I2P is less mature, but fully-distributed and self-organising, its smaller size means that it hasn't yet been blocked or DOSed much
**[Freenet](https://freenetproject.org)** | Freenet is easy to setup, provides excellent friend To Friend Sharing vs I2P, and is great for publishing content anonymously. It's quite large in size, and very slow so not the best choice for casual browsing

Tor, I2P and Freenet are all anonymity networks - but they work very differently and each is good for specific purposes. So a good and viable solution would be to use all of them, for different tasks.
*You can read more about how I2P compares to Tor, [here](https://blokt.com/guides/what-is-i2p-vs-tor-browser)*

#### Notable Mentions
See also: [GNUnet](https://gnunet.org/en/), [IPFS](https://ipfs.io/), [ZeroNet](https://zeronet.io/), [Panoramix](https://panoramix-project.eu), and [Nym](https://nymtech.neteu)

#### Word of Warning
To provide low-latency browsing, Tor does not mix packets or generate cover traffic. If an adversary is powerful enough, theoretically they could either observe the entire network, or just the victims entry and exit nodes. It's worth mentioning, that even though your ISP can not see what you are doing, they will be able determine that you are using a mix net, to hide this - a VPN could be used as well. If you are doing anything which could put you at risk, then good OpSec is essential, as the authorities have traced criminals through the Tor network before, and [made arrests](https://techcrunch.com/2019/05/03/how-german-and-us-authorities-took-down-the-owners-of-darknet-drug-emporium-wall-street-market). Don't let Tor provide you a false sense of security - be aware of information leaks through DNS, other programs or human error. Tor-supported browsers may might lag behind their upstream forks, and include exploitable unpatched issues. See [#19](https://github.com/Lissy93/personal-security-checklist/issues/19)

Note: The Tor network is run by the community. If you benefit from using it and would like to help sustain uncensored internet access for all, consider [running a Tor relay](https://trac.torproject.org/projects/tor/wiki/TorRelayGuide)


## Proxies
A proxy acts as a gateway between you and the internet, it can be used to act as a firewall or web filter, improves privacy and can also be used to provide shared network connections and cache data to speed up common requests. Never use a [free](https://whatismyipaddress.com/free-proxies) proxy.

| Provider | Description |
| --- | --- |
**[ShadowSocks](https://shadowsocks.org)** | Secure socks5 proxy, designed to protect your Internet traffic. Open source, superfast, cross-platform and easy to deploy, see [GitHub repo](https://github.com/shadowsocks)
**[Privoxy](https://www.privoxy.org)** | Non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page data and HTTP headers, controlling access, and removing ads and other obnoxious Internet junk

#### Notable Mentions
[V2ray-core](https://github.com/v2ray/v2ray-core) is a platform for building proxies to bypass network restrictions and protect your privacy. See [more](https://github.com/hugetiny/awesome-vpn)

#### Word of Warning
[Malicious Proxies](https://www.defcon.org/images/defcon-17/dc-17-presentations/defcon-17-edward_zaborowski-doppelganger.pdf) are all too common. Always use open source software, host it yourself or pay for a reputable cloud service. Never use a free proxy; it can monitor your connection, steal cookies and contain malware. VPNs are a better option, better still - use the Tor network.


## DNS
Without using a secure, privacy-centric DNS all your web requests can be seen in the clear. You should configure your DNS queries to be managed by a service that respects privacy and supports DNS-over-TLS, DNS-over-HTTPS or DNSCrypt.

| Provider | Description |
| --- | --- |
**[CloudFlare](https://developers.cloudflare.com/1.1.1.1/setting-up-1.1.1.1)** | One of the most performant options, Cloudflare's DNS supports DoH and DoT, and has a Tor implementation, providing world-class protection. They have native cross-platform apps, for easy set-up.
**[AdGuard](https://adguard.com/en/adguard-dns/overview.html)** | Open-source DNS provider, specialising in the blocking of ads, trackers and malicious domains. They have been independently audited and do not keep logs
**[NextDNS](https://nextdns.io/)** | An ad-blocking, privacy-protecting, censorship-bypassing DNS. Also comes with analytics, and the ability to shield kids from adult content

See also this [Full List of Public DoH Servers](https://github.com/curl/curl/wiki/DNS-over-HTTPS), you can then check the performance of your chosen server with [DNSPerf](https://www.dnsperf.com/). Awesome Self-Hosted also has a [good list](https://awesome.tilde.fun/d/23-list-of-dns-servers
). To read more about choosing secure DNS servers, see [this article](https://medium.com/@nykolas.z/dns-security-and-privacy-choosing-the-right-provider-61fc6d54b986), and [this article](https://geekwire.co.uk/privacy-and-security-focused-dns-resolver/).

#### Notable Mentions
- [Quad9](https://www.quad9.net) is a well-funded, performant DNS with a strong focus on privacy and security and easy set-up, however questions have been raised about the motivation of some of the financial backers.
- [BlahDNS](https://blahdns.com) (Japan, Finland or Germany) is an excellent security-focused DNS
- [OpenNIC](https://www.opennic.org/), [NixNet DNS](https://nixnet.services/dns) and [UncensoredDNS](https://blog.uncensoreddns.org) are open source and democratic, privacy-focused DNS
- [Unbound](https://nlnetlabs.nl/projects/unbound/about/) is a validating, recursive, caching DNS resolver, designed to be fast and lean. Incorporates modern features and based on open standards
- [Clean Browsing](https://cleanbrowsing.org/), is a good option for protecting kids,  they offer comprehensive DNS-based Content Filtering
- [Mullvad](https://mullvad.net/en/help/dns-over-https-and-dns-over-tls/) Mullvads public DNS with QNAME minimization and basic ad blocking. It has been audited by the security experts at Assured. You can use this privacy-enhancing service even if you don’t use Mullvad.

#### Word of Warning
Using an encrypted DNS resolver will not make you anonymous, it just makes it harder for third-partied to discover your domain history. If you are using a VPN, take a [DNS leak test](https://www.dnsleaktest.com/), to ensure that some requests are not being exposed.

#### DNS Protocols
DNS-over-TLS was proposed in [RTC-7858](https://tools.ietf.org/html/rfc7858) by the IETF, then 2 years later, the DNS-over-HTTPS specification was outlined in [RFC8484](https://tools.ietf.org/html/rfc8484) in October '18. [DNSCrypt](https://dnscrypt.info/), is a protocol that authenticates communications between a DNS client and a DNS resolver. It prevents DNS spoofing, through using cryptographic signatures to verify that responses originate from the chosen DNS resolver, and haven’t been tampered with. DNSCrypt is a well battle-tested protocol, that has been in use since 2013, and is still widely used.

## DNS Clients

| Provider | Description |
| --- | --- |
**[DNScrypt-proxy 2](https://github.com/DNSCrypt/dnscrypt-proxy)** <br>(Desktop - BSD, Linux, Solaris, Windows, MacOS & Android) | A flexible DNS proxy, with support for modern encrypted DNS protocols including DNSCrypt V2, DNS-over-HTTPS and Anonymized DNSCrypt. Also allows for advanced monitoring, filtering, caching and client IP protection through Tor, SOCKS proxies or Anonymized DNS relays.
**[Unbound](https://nlnetlabs.nl/projects/unbound/about/)** <br>(Desktop - BSD, Linux, Windows & MacOS) | Validating, recursive, caching DNS resolve with support for DNS-over-TLS. Designed to be fast, lean, and secure Unbound incorporates modern features based on open standards. It's fully open source, and recently audited. *(For an in-depth tutorial, see [this article](https://dnswatch.com/dns-docs/UNBOUND/) by DNSWatch.)*
**[Nebulo](https://git.frostnerd.com/PublicAndroidApps/smokescreen/)** <br> (Android) | Non-root, small-sized DNS changer utilizing DNS-over-HTTPS and DNS-over-TLS. *(Note, since this uses Android's VPN API, it is not possible to run a VPN while using Nebulo)* 
**[RethinkDNS + Firewall](https://github.com/celzero/rethink-app)** <br> (Android) | Free and open source DNS changer with support for DNS-over-HTTPS, DNS-over-Tor, and DNSCrypt v3 with _Anonymized Relays_. *(Note, since this uses Android's VPN API, it is not possible to run a VPN while using RethinkDNS + Firewall)* 
**[DNS Cloak](https://github.com/s-s/dnscloak)** <br> (iOS) | Simple all that allows for the use for dnscrypt-proxy 2 on an iPhone.
**[Stubby](https://dnsprivacy.org/wiki/display/DP/DNS+Privacy+Daemon+-+Stubby)** <br> (Desktop - Linux, Mac, OpenWrt & [Windows](https://dnsprivacy.org/wiki/display/DP/Windows+installer+for+Stubby)) | Acts as a local DNS Privacy stub resolver (using DNS-over-TLS). Stubby encrypts DNS queries sent from a client machine (desktop or laptop) to a DNS Privacy resolver increasing end user privacy. Stubby can be used in combination with Unbound - Unbound provides a local cache and Stubby manages the upstream TLS connections (since Unbound cannot yet re-use TCP/TLS connections), [see example configuration](https://dnsprivacy.org/wiki/display/DP/DNS+Privacy+Clients)

## Firewalls
A firewall is a program which monitors the incoming and outgoing traffic on your network, and blocks requests based on rules set during its configuration. Properly configured, a firewall can help protect against attempts to remotely access your computer, as well as control which applications can access which IPs.

| Provider | Description |
| --- | --- |
**[NetGuard](https://play.google.com/store/apps/details?id=eu.faircode.netguard)** <br>(Android) | Provides simple and advanced ways to block access to the internet. Applications and addresses can individually be allowed or denied access to Wi-Fi and/or mobile connection
**[NoRoot Firewall](https://play.google.com/store/apps/details?id=app.greyshirts.firewall)** <br>(Android) | Notifies you when an app is trying to access the Internet, so all you need to do is just Allow or Deny. Allows you to create filter rules based on IP address, host name or domain name, and you can allow or deny only specific connections of an app
**[AFWall+](https://github.com/ukanth/afwall/)** <br>(Android - Rooted) | Android Firewall+ (AFWall+) is an advanced iptables editor (GUI) for rooted Android devices, which provides very fine-grained control over which Android apps are allowed to access the network
**[RethinkDNS + Firewall](https://github.com/celzero/rethink-app)** <br>(Android) | An open-source ad-blocker and firewall app for Android 6+ (does not require root)
**[Lockdown](https://apps.apple.com/in/app/lockdown-apps/id1469783711)** <br>(iOS) | Firewall app for iPhone, allowing you to block any connection to any domain
**[SimpleWall](https://github.com/henrypp/simplewall)** <br>(Windows) | Tool to control Windows Filtering Platform (WFP), in order to configure detailed network activity on your PC
**[LuLu](https://objective-see.com/products/lulu.html)** <br>(Mac OS) | Free, open source macOS firewall. It aims to block unknown outgoing connections, unless explicitly approved by the user
**[Little Snitch](https://obdev.at/products/littlesnitch/index.html)** <br>(Mac OS) | A very polished application firewall, allowing you to easily manage internet connections on a per-app basis
**[OpenSnitch](https://github.com/evilsocket/opensnitch)** <br>(Linux) | Makes internet connections from all apps visible, allowing you to block or manage traffic on a per-app basis. GNU/Linux port of the Little Snitch application firewall
**[Gufw](http://gufw.org)** <br>(Linux) | Open source GUI firewall for Linux, allowing you to block internet access for certain applications. Supports both simple and advanced mode, GUI and CLI options, very easy to use, lightweight/ low-overhead, under active maintenance and backed by a strong community. Installable through most package managers, or compile from [source](https://answers.launchpad.net/gui-ufw)
**[Uncomplicated Firewall](https://en.wikipedia.org/wiki/Uncomplicated_Firewall)** <br>(Linux) | The ufw (Uncomplicated Firewall) is a GUI application and CLI, that allows you to configure a firewall using [`iptables`](https://linux.die.net/man/8/iptables) much more easily
**[IPFire](https://www.ipfire.org)** <br>(hardware) | IPFire is a hardened, versatile, state-of-the-art Open Source firewall based on Linux. Easy to install on a raspberry Pi, since it is lightweight and heavily customizable
**[Shorewall](https://shorewall.org)** <br>(hardware) | An open source firewall tool for Linux that builds upon the [Netfilter](https://www.netfilter.org) system built into the Linux kernel, making it easier to manage more complex configuration schemes with [iptables](https://linux.die.net/man/8/iptables)
**[OpenSense](https://opnsense.org)** <br>(hardware)  | Enterprise firewall and router for protecting networks, built on the FreeBSD system 

#### Word of Warning
There are different [types](https://www.networkstraining.com/different-types-of-firewalls) of firewalls, that are used in different circumstances. This does not omit the need to configure your operating systems defences. Follow these instructions to enable your firewall in [Windows](https://support.microsoft.com/en-us/help/4028544/windows-10-turn-windows-defender-firewall-on-or-off), [Mac OS](https://support.apple.com/en-us/HT201642), [Ubuntu](https://wiki.ubuntu.com/UncomplicatedFirewall) and other [Linux distros](https://www.tecmint.com/start-stop-disable-enable-firewalld-iptables-firewall).
Even when properly configured, having a firewall enabled does not guarantee bad network traffic can not get through and especially during boot if you don't have root privileges.

## Ad Blockers


There are a few different ways to block ads - browser-based ad-blockers, router-based / device blockers or VPN ad-blockers. Typically they work by taking a maintained list of hosts, and filtering each domain/ IP through it. Some also have other methods to detect certain content based on pattern matching

| Provider | Description |
| --- | --- |
**[Pi-Hole](https://pi-hole.net/)** (Server/ VM/ Pi) | Incredibly powerful, network-wide ad-blocker. Works out-of-the-box, light-weight with an intuitive web interface, but still allows for a lot of advanced configuration for power users. As well as blocking ads and trackers, Pi-Hole speeds up your network speeds quite significantly. The dashboard has detailed statistics, and makes it easy to pause/ resume Pi-Hole if needed.
**[Diversion](https://diversion.ch/)** (Router) | A shell script application to manage ad-blocking, Dnsmasq logging, Entware and pixelserv-tls installations and more on supported routers running [Asuswrt-Merlin firmware](https://www.asuswrt-merlin.net/), including its forks
**[DN66](https://github.com/julian-klode/dns66)** (Android) | DNS-based host and ad blocker for Android. Easy to configure, but the default config uses several widely-respected host files. aimed at stopping ads, malware, and other weird stuff
**[BlockParty](https://github.com/krishkumar/BlockParty)** (iOS/ MacOS) | Native Apple (Swift) apps, for system-wide ad-blocking. Can be customized with custom host lists, primarily aimed for just ad-blocking
**[hBlock](https://hblock.molinero.dev/)** (Unix) | A POSIX-compliant shell script, designed for Unix-like systems, that gets a list of domains that serve ads, tracking scripts and malware from multiple sources and creates a hosts file (alternative formats are also supported) that prevents your system from connecting to them. Aimed at improving security and privacy through blocking advert, tracking and malware associated domains
**[Blokada](https://blokada.org/)** (Android/ iOS) | Open source mobile ad-blocker that acts like a firewall. Since it's device-wide, once connected all apps will have ads/ trackers blocked, and the blacklist can be edited. The app is free, but there is a [premium option](https://community.blokada.org/t/what-is-blokada-plus-vpn/37), which has a built-in VPN
**[RethinkDNS + Firewall](https://rethinkdns.com/app)** (Android) | Free and open source ad-blocker and a firewall for Android 6+ (no root required)
**[Ad Block Radio](https://github.com/adblockradio/adblockradio)** (Sound) | Python script that uses machine learning to block adverts in live audio streams, such as Radio, Podcasts, Audio Books, and music platforms such as Spotify. See [live demo](https://www.adblockradio.com/en/)
**[uBlock Origin](https://github.com/gorhill/uBlock)** (Browser) | Light-weight, fast browser extension for Firefox and Chromium (Chrome, Edge, Brave Opera etc), that blocks tracking, ads and known malware. uBlock is easy-to-use out-of-the-box, but also has a highly customisable advanced mode, with a point-and-click firewall which can be configured on a per-site basis
**[uMatrix](https://github.com/gorhill/uMatrix)** (Browser) | **uMatrix is [no longer](https://www.ghacks.net/2020/09/20/umatrix-development-has-ended/) being actively maintained**. Another light-weight browser extension, for Chromium and Firefox browsers. uMatrix acts more like a firewall, giving you the option for super fine-grained control over every aspect of resource blocking. It is possible to use both uBlock (for simple/ cosmetic ad blocking) and uMatrix (for detailed JavaScript blocking) at the same time


#### Notable Mentions
[AdGuardHome](https://github.com/AdguardTeam/AdGuardHome) is a cross-platform DNS Ad Blocker, similar to Pi Hole, but with some additional features, like parental controls, per-device configuration and the option to force safe search. This may be a good solution for families with young children.

Some VPNs have ad-tracking blocking features, such as [TrackStop with PerfectPrivacy](https://www.perfect-privacy.com/en/features/trackstop?a_aid=securitychecklist). 
[Private Internet Access](https://www.privateinternetaccess.com/), [CyberGhost](https://www.cyberghostvpn.com/), [PureVPN](https://www.anrdoezrs.net/click-9242873-13842740), and [NordVPN](https://www.kqzyfj.com/l5115shqnhp4E797DC8467D69A6D) also have ad-block features.


## Host Block Lists

| Provider | Description |
| --- | --- |
**[SomeoneWhoCares/ Hosts](https://someonewhocares.org/hosts/)** | An up-to-date host list, maintained by Dan Pollock - to make the internet not suck (as much)
**[Hosts by StevenBlack](https://github.com/StevenBlack/hosts)** |  Open source, community-maintained consolidated and extending hosts files from several well-curated sources. You can optionally pick extensions to block p0rn, Social Media, gambling, fake news and other categories
**[No Google](https://github.com/nickspaargaren/no-google)** | Totally block all direct and indirect content from Google, Amazon, Facebook, Apple and Microsoft (or just some)
**[EasyList](https://easylist.to)** | Comprehensive list of domains for blocking tracking, social scripts, bad cookies and annoying stuff
**[iBlockList](https://www.iblocklist.com/)** | Variety of lists (free and paid-for) for blocking content based on certain topics, inducing: spam, abuse, political, illegal, hijacked, bad peers and more
**[Energized](https://github.com/EnergizedProtection/block)** | A variety of well-maintained lists, available in all common formats, with millions of hosts included


## Router Firmware

Installing a custom firmware on your Wi-Fi router gives you greater control over security, privacy and performance

| Provider | Description |
| --- | --- |
**[OpenWRT](https://openwrt.org)** | Plenty of scope for customization and a ton of supported addons. Stateful firewall, NAT, and dynamically-configured port forwarding protocols (UPnP, NAT-PMP + upnpd, etc), Load balancing, IP tunneling, IPv4 & IPv6 support
**[DD-WRT](https://dd-wrt.com)** | Easy and powerful user interface. Great access control, bandwidth monitoring and quality of service. [IPTables](https://linux.die.net/man/8/iptables) is built-in for firewall, and there's great VPN support as well as additional plug-and-play and wake-on-lan features

#### Notable Mentions
[Tomato](https://www.polarcloud.com/tomato), [Gargoyle](https://www.gargoyle-router.com), [LibreCMC](https://librecmc.org) and [DebWRT](http://www.debwrt.net)

#### Word of Warning
Flashing custom firmware may void your warranty. If power is interrupted mid-way through a firmware install/ upgrade it is possible for your device to become bricked. So long as you follow a guide, and use a well supported system, on a supported router, than it should be safe

## Network Analysis

Whether you live in a country behind a firewall, or accessing the internet through a proxy - these tools will help you better understand the extent of blocking, deep packet inspection and what data is being analysed

| Provider | Description |
| --- | --- |
**[OONI](https://ooni.org)** | Open Observatory of Network Interference - A free tool and global observation network, for detecting censorship, surveillance and traffic manipulation on the internet. Developed by The Tor Project, and available for [Android](https://play.google.com/store/apps/details?id=org.openobservatory.ooniprobe), [iOS](https://apps.apple.com/us/app/id1199566366) and [Linux](https://ooni.org/install/ooniprobe)
**[Mongol](https://github.com/mothran/mongol)** | A Python script, to pinpoint the IP address of machines working for the The Great Firewall of China. See also [gfwlist](https://github.com/gfwlist/gfwlist) which is the Chinese ban list, and [gfw_whitelist](https://github.com/n0wa11/gfw_whitelist). For a list of Russian government IP addresses, see [antizapret](https://github.com/AntiZapret/antizapret)
**[Goodbye DPI](https://github.com/ValdikSS/GoodbyeDPI)** | Passive Deep Packet Inspection blocker and Active DPI circumvention utility, for Windows
**[DPITunnel](https://github.com/zhenyolka/DPITunnel)** | An Android app to bypass deep packet inspection
**[Proxy Checker](https://ping.eu/proxy/)** | You can quickly check if a given IP is using a proxy, this can also be done through the [command line](https://superuser.com/questions/346372/how-do-i-know-what-proxy-server-im-using)


## Intrusion Detection

An IDS is an application that monitors a network or computer system for malicious activity or policy violations, and notifies you of any unusual or unexpected events. If you are running a server, then it's essential to know about an incident as soon as possible, in order to minimize damage.

| Provider | Description |
| --- | --- |
**[Zeek](https://zeek.org/)** | Zeek (formally Bro) Passively monitors network traffic and looks for suspicious activity
**[OSSEC](https://www.ossec.net/)** | OSSEC is an Open Source host-based intrusion detection system, that performs log analysis, integrity checking, monitoring, rootkit detection, real-time alerting and active response
**[Kismet](https://www.kismetwireless.net/)** |An 802.11 layer2 wireless network detector, sniffer, and intrusion detection system
**[Snare](https://www.snaresolutions.com/products/snare-central/)** | SNARE (System iNtrusion Analysis and Reporting Environment) is a series of log collection agents that facilitate centralized analysis of audit log data. Logs from the OS are collected and audited. Full remote access, through a web interface easy to use manually, or by an automated process
**[picosnitch](https://github.com/elesiuta/picosnitch)** | picosnitch helps protect your security and privacy by "snitching" on anything that connects to the internet, letting you know when, how much data was transferred, and to where. It uses BPF to monitor network traffic per application, and per parent to cover those that just call others. It also hashes every executable, and will complain if some mischievous program is giving it trouble.


## Cloud Hosting

Whether you are hosting a website and want to keep your users data safe, or if you are hosting your own file backup, cloud productivity suite or VP - then choosing a provider that respects your privacy and allows you to sign up anonymously, and will keep your files and data safe is be important.

| Provider | Description |
| --- | --- |
**[Njalla](https://njal.la)** | Njalla is a privacy and security-focused domain registrar and VPN hosting provider. They own and manage all their own servers, which are based in Sweden. They accept crypto, for anonymous payments, and allow you to sign up with OTR XMPP if you do not want to provide an email address. Both VPS and domain name pricing is reasonable, with packages starting at $15/ month
**[Vindo](https://www.vindohosting.com)** | Provides anonymous shared hosting, semi-managed virtual private servers and domain registration
**[Private Layer](https://www.privatelayer.com)** | Offers enterprise-grade, high-speed offshore dedicated servers, they own their own data centres, have a solid privacy policy and accept anonymous payment
**[Servers Guru](https://servers.guru)** | Servers Guru provides affordable and anonymous VPS and cloud servers with dedicated cpu resources. They accept crypto-currencies (Bitcoin, Monero, Ethereum etc..) and don't require any personal informations. They resell from reliable main actors in the industry and provide multiple hosting locations across europe. Their VPS offers starts at 4.99 €/ month

#### Notable Mentions
See also: [1984](https://www.1984.is) based in Iceland. [Shinjiru](http://shinjiru.com?a_aid=5e401db24a3a4), which offers off-shore dedicated servers. [Orange Website](https://www.orangewebsite.com) specialises in protecting online privacy and free speech, hosted in Iceland. [RackBone](https://rackbone.ch) (previously [DataCell](https://datacell.is)) provides secure and ethical hosting, based in Switzerland. And [Bahnhof](https://www.bahnhof.net) offers high-security and ethical hosting, with their data centres locates in Sweden. Finally [Simafri](https://www.simafri.com/anonymous) has a range of packages, that support Tor out of the box

#### Word of Warning
The country that your data is hosted in, will be subject to local laws and regulations. It is therefore important to avoid a jurisdiction that is part of the [5 eyes](https://en.wikipedia.org/wiki/Five_Eyes) (Australia, Canada, New Zealand, US and UK) and [other international cooperatives](https://en.wikipedia.org/wiki/Five_Eyes#Other_international_cooperatives) who have legal right to view your data.


## Domain Registrars

| Provider | Description |
| --- | --- |
**[Njal.la](https://njal.la)** | Privacy-aware domain service with anonymous sign-up and accepts crypto currency
**[Orange Website](https://www.orangewebsite.com/domain-registration.php)** | Anonymous domain registration, with low online censorship since they are based outside the 14-eyes jurisdiction (in Iceland)

## DNS Hosting

| Provider | Description |
| --- | --- |
**[deSEC](https://desec.io/)** | Free DNS hosting provider designed with security in mind, and running on purely open source software. deSEC is backed and funded by [SSE](https://securesystems.de/en/).


## Pre-Configured Mail-Servers

| Provider | Description |
| --- | --- |
**[Mail-in-a-box](https://github.com/mail-in-a-box/mailinabox)** | Easy-to-deploy fully-featured and pre-configured SMTP mail server. It includes everything from webmail, to spam filtering and backups
**[Docker Mailserver](https://github.com/tomav/docker-mailserver)** | A full-stack but simple mailserver (smtp, imap, antispam, antivirus, ssl...) using Docker. Very complete, with everything you will need, customizable and very easy to deploy with docker


#### Word of Warning
Self-hosting your own mail server is not recommended for everyone, it can be time consuming to setup and maintain and securing it correctly is critical

<hr id="productivity" />

## Digital Notes

| Provider | Description |
| --- | --- |
**[Cryptee](https://crypt.ee/)** | Private & encrypted rich-text documents. Cryptee has encryption and anonymity at its core, it also has a beautiful and minimalistic UI. You can use Cryptee from the browser, or download native Windows, Mac OS, Linux, Android and iOS apps. Comes with many additional features, such as support for photo albums and file storage. The disadvantage is that only the frontend is open source. Pricing is free for starter plan, $3/ month for 10GB, additional plans go up-to 2TB
**[Standard Notes](https://standardnotes.com/?s=chelvq36)** | S.Notes is a free, open-source, and completely encrypted private notes app. It has a simple UI, yet packs in a lot of features, thanks to the [Extensions Store](https://standardnotes.com/features), allowing for: To-Do lists, Spreadsheets, Rich Text, Markdown, Math Editor, Code Editor and many more. You can choose between a number of themes (yay, dark mode!), and it features built-in secure file store, tags/ folders, fast search and more. There is a web app as well as native Windows, Mac OS, Linux, Android and iOS apps. Standard Notes is actively developed, and fully open-source, so you can host it yourself, or use their hosted version: free without using plug-ins or $3/ month for access to all features
**[Turtle](https://turtlapp.com/)** | A secure, collaborative notebook. Self-host it yourself (see [repo](https://github.com/turtl)), or use their hosted plan (free edition or $3/ month for premium)
**[Joplin](https://joplinapp.org)** | Cross-platform desktop and mobile note-taking and todo app. Easy organisation into notebooks and sections, revision history and a simple UI. Allows for easy import and export of notes to or from other services. Supports synchronisation with cloud services, implemented with E2EE - however it is only the backed up data that is encrypted
**[Notable](https://notable.md)** | Markdown-based note editor for desktop, with a simple, yet feature-rich UI. All notes are saved individually as .md files, making them easy to manage. No mobile app, or built-in cloud-sync or encryption
**[Logseq](https://logseq.com/)** | Privacy-first, open-source knowledge base that works on top of local plain-text Markdown and Org-mode files
**[AFFiNE](https://affine.pro)** | Privacy first, open-source alternative to Notion, monday.com and Miro.
#### Notable Mentions
If you are already tied into Evernote, One Note etc, then [SafeRoom](https://www.getsaferoom.com) is a utility that encrypts your entire notebook, before it is uploaded to the cloud. 

[Org Mode](https://orgmode.org) is a mode for [GNU Emacs](https://www.gnu.org/software/emacs/) dedicated to working with the Org markup format. Org can be thought of as a more featureful Markdown alternative, with support for keeping notes, maintaining todo lists, planning projects, managing spreadsheets, and authoring documents -all in plaintext.

For a simple plain text note taking app, with strong encryption, see [Protected Text](https://www.protectedtext.com), which works well with the [Safe Notes](https://play.google.com/store/apps/details?id=com.protectedtext.android) Android app. [Laverna](https://laverna.cc/) is a cross-platform secure notes app, where all entries are formatted with markdown.


## Cloud Productivity Suites

| Provider | Description |
| --- | --- |
**[CryptPad](https://cryptpad.fr)** | A zero knowledge cloud productivity suite. Provides Rich Text, Presentations, Spreadsheets, Kanban, Paint a code editor and file drive. All notes and user content, are encrypted by default, and can only be accessed with specific URL. The main disadvantage, is a lack of Android, iOS and desktop apps - CryptPad is entirely web-based. You can use their web service, or you can host your own instance (see [CryptPad GitHub](https://github.com/xwiki-labs/cryptpad) repo). Price for hosted: free for 50mb or $5/ month for premium
**[NextCloud](https://nextcloud.com/)** | A complete self-hosted productivity platform, with a strong community and growing [app store](https://apps.nextcloud.com). NextCloud is similar to (but arguably more complete than) Google Drive, Office 365 and Dropbox, originally it was a fork from [OwnCloud](https://owncloud.org/), but since have diverged. Clear UI and stable native apps across all platforms, and also supports file sync. Supports encrypted files, but you need to configure this yourself. Fully open source, so you can self-host it yourself (or use a hosted solution, starting from $5/ month)
**[Disroot](https://disroot.org)** | A platform providing online services based on principles of freedom, privacy, federation and decentralization. It is an implementation of NextCloud, with strong encryption configured - it is widely used by journalists, activists and whistle-blowers. It is free to use, but there have been reported reliability issues of the cloud services
**[Sandstorm](https://sandstorm.io/)** | An open source platform for self-hosting web apps. Once you've set it up, you can install items from the Sandstorm [App Market](https://apps.sandstorm.io/) with -click, similar to NextCloud in terms of flexibility
**[Vikunja](https://vikunja.io)** | Vikunja is an open-source to-do application. It is suitable for a wide variety of projects, supporting List, Gantt, Table and Kanban views to visualize all tasks in different contexts. For collaboration, it has sharing support via private teams or public links. It can be self-hosted or used as a managed service for a small fee.
**[Skiff Pages](https://skiff.com/pages)** | Skiff Pages is an end-to-end encrypted, privacy-first collaborative document, note-taking, and wiki product. Skiff Pages has a modern, easy-to-use UI and supports rich text documents with embedded content. Skiff also supports end-to-end encrypted file upload and sharing ([Skiff Drive](https://skiff.com/drive)), as well as workspaces for multiple users to collaborate. [Skiff Pages is available](https://skiff.com/download) on web, iOS, and Android.

## Backup and Sync

| Provider | Description |
| --- | --- |
**[SeaFile](https://www.seafile.com)** | An open source cloud storage and sync solution. Files are grouped into Libraries, which can be individually encrypted, shared of synced. Docker image available for easy deployment, and native clients for Windows, Mac, Linux, Android and iOS
**[Syncthing](https://syncthing.net)** | Continuous file synchronization between 2 or more clients. It is simple, yet powerful, and fully-encrypted and private. Syncthing can be deployed with Docker, and there are native clients for Windows, Mac, Linux, BSD and Android
**[NextCloud](https://nextcloud.com)** | Feature-rich productivity platform, that can be used to backup and selectively sync encrypted files and folders between 1 or more clients. See [setting up sync](https://docs.nextcloud.com/desktop/3.3/navigating.html). A key benefit the wide range of plug-ins in the [NextCloud App Store](https://apps.nextcloud.com), maintained by the community. NextCloud was a hard fork off [OwnCloud](https://owncloud.org).

#### Notable Mentions
Alternatively, consider a headless utility such as [Duplicacy](https://duplicacy.com) or [Duplicity](http://duplicity.nongnu.org). Both of offer an encrypted and efficient sync between 2 or more locations, using the [rsync](https://linux.die.net/man/1/rsync) algorithm.

[SpiderOak](https://spideroak.com), [Tresorit](https://tresorit.com) and [Resilio](https://www.resilio.com/individuals) are good enterprise solutions, all with solid encryption baked-in

[FileRun](https://filerun.com) and [Pydio](https://pydio.com) are self-hosted file explorers, with cross-platform sync capabilities.

#### Word of Warning
You should always ensure that any data stored in the cloud is encrypted. If you are hosting your own server, then take the necessary precautions to [secure the server](https://med.stanford.edu/irt/security/servers.html). For hosted solutions - use a strong password, keep your credentials safe and enable 2FA.

## Encrypted Cloud Storage

Backing up important files is essential, and keeping an off-site copy is recommended. But many free providers do not respect your privacy, and are not secure enough for sensitive documents. Avoid free mainstream providers, such as Google Drive, cloud, Microsoft Overdrive, Dropbox.

It is recommended to encrypt files on your client machine, before syncing to the cloud. [Cryptomator](https://cryptomator.org) is a cross-platform, open source encryption app, designed for just this.

| Provider | Description |
| --- | --- |
**[Tresorit](https://tresorit.com)** | End-to-end encrypted zero knowledge file storage, syncing and sharing provider, based in Switzerland. The app is cross-platform, user-friendly client and with all expected features. £ 6.49/month for 500 GB
**[IceDrive](https://icedrive.net)** | Very affordable encrypted storage provider, with cross-platform apps. Starts as £ 1.50/month for 150 GB or £ 3.33/month for 1 TB
**[Sync.com](https://www.sync.com)** | Secure file sync, sharing, collaboration and backup for individuals, small businesses and sole practitioners. Starts at $8/month for 2 TB
**[pCloud](https://www.pcloud.com)** | Secure and simple to use cloud storage, with cross-platform client apps. £ 3.99/month for 500 GB
**[Peergos](https://peergos.org/)** | A peer-to-peer end-to-end encrypted global filesystem with fine grained access control. Provides a secure and private space online where you can store, share and view your photos, videos, music and documents. Also includes a calendar, news feed, task lists, chat and email client.  Fully open source and self-hostable (or use hosted solution, £ 5/month for 50 GB)
**[Internxt](https://internxt.com/)** | Store your files in total privacy. Internxt Drive is a zero-knowledge cloud storage service based on best-in-class privacy and security. Made in Spain. Open-source mobile and desktop apps. 10GB FREE and Paid plans starting from € 0.99/month for 20GB.
**[FileN](https://filen.io/)** | Zero knowledge end-to-end encrypted affordable cloud storage made in Germany. Open-source mobile and desktop apps. 10GB FREE with paid plans starting at € 0.92/month for 100GB.

#### Notable Mentions
An alternative option, is to use a cloud computing provider, and implement the syncing functionality yourself, and encrypt data locally before uploading it - this may work out cheaper in some situations. You could also run a local server that you physically own at a secondary location, that would mitigate the need to trust a third party cloud provider. Note that some knowledge in securing networks is required.

**See Also**:
- [File Encryption Software](#file-encryption)
- [File Sync Software](#backup-and-sync)
- [Cloud Hosting Providers](#cloud-hosting)


## File Drop

| Provider | Description |
| --- | --- |
**[FilePizza](https://file.pizza)** | Peer-to-peer based file transfer from the browser, using [Web Torrent](https://webtorrent.io/). It's quick and easy to use, and doesn't require any software to be installed. Can also be self-hosted: [repo](https://github.com/kern/filepizza)
**[FileSend](https://filesend.standardnotes.org)** | Simple, encrypted file sharing, with a 500mb limit and 5-day retention. Files are secured with client-side AES-256 encryption and no IP address or device info is logged. Files are permanently deleted after download or after specified duration. Developed by [StandardNotes](https://standardnotes.org/?s=chelvq36), and has built-in integration with the SN app.
**[OnionShare](https://onionshare.org/)** | An open source tool that lets you securely and anonymously share a file of any size, via Tor servers. OnionShare does require installing (compatible with Windows, Mac OS and Linux), but the benefit is that your files are transferred directly to the recipient, without needing to be hosted on an interim server. The host needs to remain connected for the duration of the transfer, but once it is complete, the process will be terminated. Source code: [repo](https://github.com/micahflee/onionshare)

#### Notable Suggestions
[Instant.io](https://github.com/webtorrent/instant.io), is another peer-to-peer based solution, using [Web Torrent](https://webtorrent.io). For specifically transferring images, [Up1](https://github.com/Upload/Up1) is a good self-hosted option, with client-side encryption. Finally [PsiTransfer](https://github.com/psi-4ward/psitransfer) is a feature-rich, self-hosted file drop, using streams.

## Browser Sync

It is not advised to sign into your browser, since it allows for more of your browsing data to be exposed, and can tie anonymous identities to your real account. If you require your bookmarks to be synced across devices or browsers then these tools can help, without you having to rely on an untrustworthy third-party.

| Provider | Description |
| --- | --- |
**[Floccus](https://floccus.org)** | Simple and efficient bookmark syncing using either [NextCloud Bookmarks](https://github.com/nextcloud/bookmarks), a WebDAV server (local or remote) or just a local folder through [LoFloccus](https://github.com/TCB13/LoFloccus). Browser extensions available for extensions for [Chrome](https://chrome.google.com/webstore/detail/floccus/fnaicdffflnofjppbagibeoednhnbjhg), [Firefox](https://addons.mozilla.org/en-US/firefox/addon/floccus/) and [Edge](https://microsoftedge.microsoft.com/addons/detail/gjkddcofhiifldbllobcamllmanombji)
**[XBrowserSync](https://www.xbrowsersync.org)** | Secure, anonymous and free browser and bookmark syncing. Easy to setup, and no sign up is required, you can either use a [community-run sync server](https://www.xbrowsersync.org/#status), or host your own with their [docker image](https://hub.docker.com/r/xbrowsersync/api). Extensions are available for [Chrome](https://chrome.google.com/webstore/detail/xbrowsersync/lcbjdhceifofjlpecfpeimnnphbcjgnc), [Firefox](https://addons.mozilla.org/en-GB/firefox/addon/xbs/) and on [Android](https://play.google.com/store/apps/details?id=com.xBrowserSync.android)
**[Unmark](https://github.com/cdevroe/unmark)** | A web application which acts as a todo app for bookmarks. You can either self-host it, or use their [managed service](https://unmark.it) which has a free and paid-for tier 
**[Reminiscence](https://github.com/kanishka-linux/reminiscence)** | A self-hosted bookmark and archive manager. Reminiscence is more geared towards archiving useful web pages either for offline viewing or to preserve a copy. It is a web application, that can be installed with Docker on either a local or remote server, although it has a comprehensive and well-documented REST API, there is currently [no browser extension](https://github.com/kanishka-linux/reminiscence/wiki/Browser-Addons)
**[Geekmarks](https://geekmarks.dmitryfrank.com)** | An API-driven, quick-to-use bookmark manager with powerful organisation features. Geekmarks is thoroughly documented, but a little more technical than other options, extension is currently only available for [Chromium-based](https://chrome.google.com/webstore/detail/geekmarks-client/nhiodffdihhkdlkfmpmmnanekkbbfkgk) browsers
**[Shiori](https://github.com/go-shiori/shiori)** | Simple bookmark manager written in Go, intended to be a clone of [Pocket](https://getpocket.com), it has both a simple and clean web interface as well as a CLI. Shiori has easy import/ export, is portable and has webpage archiving features


#### Notable Mentions
[Ymarks](https://ymarks.org) is a C-based self-hosted bookmark synchronization server and [Chrome](https://chrome.google.com/webstore/detail/ymarks/gefignhaigoigfjfbjjobmegihhaacfi) extension.
[syncmarx](https://syncmarx.gregmcleod.com) uses your cloud storage to sync bookmarks ([Chrome](https://chrome.google.com/webstore/detail/syncmarx/llcdegcpeheociggfokjkkgciplhfdgg) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/syncmarx/)).
[NextCloud Bookmarks](https://apps.nextcloud.com/apps/bookmarks) has several community browser extensions, inducing [FreedomMarks](https://addons.mozilla.org/en-US/firefox/addon/freedommarks/) (Firefox) and [OwnCloud Bookmarks](https://chrome.google.com/webstore/detail/owncloud-bookmarks/eomolhpeokmbnincelpkagpapjpeeckc) (Chrome). 
Finally, [Turtl Notes](https://turtlapp.com) has excellent link saving functionality built-in

[RainDrop](https://raindrop.io) is a fully-featured all-in-1 bookmarking and web-snip suite. It has a beautiful UI, good data controls and some very handy integrations and features. Available on desktop, mobile, web and through a browser extension. The catch is that it is not open source, there is a free and premium plan, but no option for self-hosting.

#### Word of Warning
Strip out unneeded GET parameters if they reveal any device or referrer information, so as to not inadvertently allow a website to link your devices. [ClearURLs](https://gitlab.com/KevinRoebert/ClearUrls) may help with this.


## Video Conference Calls

With the [many, many security issues with Zoom](https://www.tomsguide.com/uk/news/zoom-security-privacy-woes), and other mainstream options, it becomes clear that a better, more private and secure alternative is required. As with other categories, the "best video calling app" will be different for each of us, depending on the ratio of performance + features to security + privacy required in your situation.

| Provider | Description |
| --- | --- |
**[Jami](https://jami.net)** | A free and open source, distributed video, calling and screenshare platform with a focus on security. Jami is completely completely peer-to-peer, and has full end-to-end encryption with perfect forward secrecy for all communications, complying with the [X.509](https://en.wikipedia.org/wiki/X.509) standard. Supported nativity on Windows, macOS, iOS, GNU/Linux, Android and Android TV. Video quality is quite good, but very dependent on network speeds, some of the apps are lacking in features
**[Jitsi](https://jitsi.org)** | Encrypted, free and open source video calling app, which does not require creating an account/ providing any personal details. Availible as a web app, and native app for Windows, MacOS, Linux, Android and iOS. You can use the public Jitsi instance, self-host your own, or use a [community hosted instance](https://github.com/jitsi/jitsi-meet/wiki/Jitsi-Meet-Instances)

#### Notable Mentions
[Apache OpenMeetings](https://openmeetings.apache.org) provides self-hosted video-conferencing, chat rooms, file server and tools for meetings. [together.brave.com](https://together.brave.com) is Brave's Jitsi Fork.
For remote learning, [BigBlueButton](https://bigbluebutton.org) is self-hosted conference call software, aimed specifically at schools and Universities. It allows for the host/ teacher to have full control over the session, and provides high-quality video streaming, multi-user whiteboards, breakout rooms, and instant chat.
For 1-to-1 mobile video calls, see [Encrypted Messaging](#encrypted-messaging), and for P2P single and group calls, see [P2P Messaging](#p2p-messaging).


## PGP Managers

Tools for signing, verifying, encrypting and decrypting text and files using [GnuPG](https://www.gnupg.org) standard

| Provider | Description |
| --- | --- |
**[SeaHorse](https://wiki.gnome.org/Apps/Seahorse/)** (Linux/ GNOME) | Application for managing encryption keys and passwords, integrated with the [GNOME Keyring](https://wiki.gnome.org/action/show/Projects/GnomeKeyring?action=show&redirect=GnomeKeyring)
**[Kleopatra](https://kde.org/applications/en/utilities/org.kde.kleopatra)** (Linux/ KDE) | Certificate manager and a universal crypto GUI. It supports managing X.509 and OpenPGP certificates in the GpgSM keybox and retrieving certificates from LDAP server
**[GPG4Win](https://www.gpg4win.org)** (Windows) | Kleopatra ported to Windows
**[GPG Suite](https://gpgtools.org)** (MacOS) | Successor of [MacGPG](https://macgpg.sourceforge.io). Note: no longer free
**[OpenKeychain](https://www.openkeychain.org)** (Android) | Android app for managing keys, and encrypting messages. Works both stand-alone, and as integrated into other apps, including [k9-Mail](https://k9mail.app)
**[PGP Everywhere](https://www.pgpeverywhere.com)** (iOS) | iOS app for encrypting/ decrypting text. Has native keyboard integration, which makes it quick to use. Note: Not open source
**[FlowCrypt](https://flowcrypt.com)** (Browser) | Browser extension for using PGP within Gmail, for Chrome and Firefox. Mobile version supported on Android and iOS
**[EnigMail](https://enigmail.net)** (Thunderbird) | OpenPGP extension for [Thunderbird](https://www.thunderbird.net) and [PostBox](https://www.postbox-inc.com), integrates natively within mail app
**[p ≡ p](https://www.pep.security)** | Easy-to-use decentralied PGP encryption for Android, iOS, Thunderbird, Enigmail, and Outlook. Popular solution for enterprises
**[Mailvelope](https://www.mailvelope.com)** (Email) | Mailvelope is an addon for email applications, that makes using PGP very easy for beginners. You can use the hosted version for free, or opt to host your own instance. It has good compatibility with all common mail applications, both on desktop and mobile
**[PGP4USB](https://gpg4usb.org)** (Portable) | A portable desktop app, that can be run directly off a USB, useful for when you need to use without installing


## Metadata Removal Tools

[Exif](https://en.wikipedia.org/wiki/Exif)/ [Metadata](https://en.wikipedia.org/wiki/Metadata) is "data about data", this additional information attached to files can lead us to [share significantly more information than we intended](https://gizmodo.com/vice-magazine-just-accidentally-revealed-where-john-mca-5965295) to. 
For example, if you upload an image of a sunset to the internet, but don't remove the metadata, it [may reveal the location](https://www.nytimes.com/2010/08/12/technology/personaltech/12basics.html?_r=1) (GPS lat + long) of where it was taken, the device is was taken on, precise camera data, details about modifications and the picture source + author. Social networks that remove metadata from your photos, often collect and store it, for their own use. This could obviously pose a security risk, and that is why it is recommended to strip out this data from a file before sharing.

| Provider | Description |
| --- | --- |
**[ExifCleaner](https://exifcleaner.com)** | Cross-platform, open source, performant EXIF meta data removal tool. This GUI tool makes cleaning media files really easy, and has great batch process support. Created by @szTheory, and uses [ExifTool](https://exiftool.org)
**[ExifTool](https://exiftool.org)** (CLI) | Platform-independent open source Perl library & CLI app, for reading, writing and editing meta data. Built by Phill Harvey. Very good performance, and supports all common metadata formats (including  EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile, Photoshop IRB, FlashPix, AFCP and ID3). An official [GUI application](https://exiftool.org/gui/) is available for Windows, implemented by Bogdan Hrastnik.
**[ImageOptim](https://github.com/ImageOptim/ImageOptim)** (MacOS) | Native MacOS app, with drag 'n drop image optimization and meta data removal

#### Notable Mentions
It's possible (but slower) to do this without a third-party tool. For Windows, right click on a file, and go to: `Properties --> Details --> Remove Properties --> Remove from this File --> Select All --> OK`.

Alternatively, with [ImageMagic](https://imagemagick.org) installed, just run `convert -strip path/to/image.png` to remove all metadata. If you have [GIMP](https://www.gimp.org) installed, then just go to `File --> Export As --> Export --> Advanced Options --> Uncheck the "Save EXIF data" option`.

Often you need to perform meta data removal programmatically, as part of a script or automation process.  
GoLang: [go-exif](https://github.com/dsoprea/go-exif) by @dsoprea | JS: [exifr](https://github.com/MikeKovarik/exifr) by @MikeKovarik | Python: [Piexif](https://github.com/hMatoba/Piexif) by @hMatoba | Ruby: [Exif](https://github.com/tonytonyjan/exif) by @tonytonyjan | PHP: [Pel](https://github.com/pel/pel) by @mgeisler.


## Data Erasers
Simply deleting data, does [not remove it](https://uk.norton.com/internetsecurity-privacy-is-my-personal-data-really-gone-when-its-deleted-from-a-device.html) from the disk, and recovering deleted files is a [simple task](https://www.lifewire.com/how-to-recover-deleted-files-2622870). Therefore, to protect your privacy, you should erase/ overwrite data from the disk, before you destroy, sell or give away a hard drive.

| Provider | Description |
| --- | --- |
**[Eraser](https://eraser.heidi.ie)** (Windows) |  Allows you to completely remove sensitive data from your hard drive by overwriting it several times with carefully selected patterns
**[Hard Disk Scrubber](http://www.summitcn.com/hdscrub.html)** (Windows) | Easy to use, but with some advanced features, including custom wipe patterns. Data Sanitation Methods:  AFSSI-5020, DoD 5220.22-M, and Random Data
**[SDelete](https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete)** (Windows) | Microsoft Secure Delete is a CLI utility, uses DoD 5220.22-M
**[OW Shredder](https://schiffer.tech/ow-shredder.html)** (Windows) | File, folder and drive portable eraser for Windows. Bundled with other tools to scan, analyze, and wipe, and other traces that were left behind. Includes context menu item, recycle bin integration
**[DBAN](https://dban.org)** (bootable) | Darik's Boot and Nuke ("DBAN") is a self-contained boot disk that securely wipes the hard disks of most computers. DBAN will automatically and completely delete the contents of any hard disk that it can detect, which makes it an appropriate utility for bulk or emergency data destruction. DBAN is the free edition of [Blanco](https://www.blancco.com/products/drive-eraser/), which is an enterprise tool designed for legal compliance.
**[nwipe](https://github.com/martijnvanbrummelen/nwipe)** (Cross-platform) | C-based secure light-weight disk eraser, operated through the easy-to-use CLI or a GUI interface
**[shred](https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html)** (Unix) | A CLI utility that can be used to securely delete files and devices, to make them extremely difficult to recover. See also, [wipe](https://linux.die.net/man/1/wipe) for erasing files from magnetic media
**[Secure Remove](https://www.systutorials.com/docs/linux/man/1-srm/)** (Unix) | CLI utility for securely removing files, directories and whole disks, works on Linux, BSD and MacOS
**[Mr. Phone](https://drfone.wondershare.com)** (Android/ iOS) | Proprietary, closed-source suite of forensic data tools for mobile. The data eraser allows for both Android and iOS to be fully wiped, through connecting them to a PC.

#### Notable Mentions
There's no need to use a third-party tool. You can boot into a UNIX-based system, mount the disk you need to erase, and use a command to write it with arbitrary data. For best results, this process should be repeated several times. This is a good way to wipe a disk, before selling or destroying it, to protect your data.

Such as the [`dd`](https://en.wikipedia.org/wiki/Dd_%28Unix%29) command, is a tool to convert and copy files, but running `sudo dd if=/dev/zero of=/dev/sdX bs=1M` will quickly overwrite the whole disk with zeros. Or [badblocks](https://linux.die.net/man/8/badblocks) which is intended to search for all bad blocks, but can also be used to write zeros to a disk, by running `sudo badblocks -wsv /dev/sdd`. An effective method of erasing an SSD, it to use [hdparm](https://en.wikipedia.org/wiki/Hdparm) to issue a [secure erase](https://en.wikipedia.org/wiki/Parallel_ATA#HDD_passwords_and_security) command, to your target storage device, for this, see step-by-step instructions via: [wiki.kernel.org](https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase). Finally, `[srm](https://www.systutorials.com/docs/linux/man/1-srm/)` can be use to securely remove files or directories, just run `srm -zsv /path/to/file` for a single pass over.

<hr id="utilities" />

## Virtual Machines

A virtual machine (VM) is a sandboxed operating system, running within your current system. Useful for compartmentalisation and safely testing software, or handling potentially malicious files

| Provider | Description |
| --- | --- |
**[VirtualBox](https://www.virtualbox.org/)** | Open source, powerful, feature-rich virtualization product, supporting x86 and AMD64/Intel64 architectures. Available for Windows, MacOS, Linux and BSD, and free for both personal and enterprise use. VirtualBox is backed by a strong community, and has been under active development since 2007.
**[Xen Project](https://xenproject.org/)** (Servers) | Open source virtual machine monitor intended to serve as a type-1 hyperviser for multiple operating systems using the same hardware - very useful for servers, as it allows for fully independent virtual Linux machines 
**[UTM](https://mac.getutm.app)** | Open source, feature rich, powerful type 2 hypervisor for Mac, can emulate x86-64 OSes on Apple Silicon Macs

#### Notable Mentions

[QEMU](https://wiki.qemu.org/Main_Page) is a virtual hardware emulation tool, meaning it is less appropriate for creating fully independant sandboxes, but performance is considerable better than that of a traditional virtual machine.

[VMWare](https://www.vmware.com/) is popular in the enterprise world, it is not open source, and although there is a free version, a license is required to access all features. VMWare performs very well when running on a server, with hundreds of hosts and users. For Mac users, [Parallels](https://www.parallels.com/uk/) is a popular option which performs really well, but again is not open source. For Windows users, there's [Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v), which is a native Windows product, developed by Microsoft.

<hr id="social" />

## Social Networks

Over the past decade, social networks have revolutionized the way we communicate and bought the world closer together - but it came at the [cost of our privacy](https://en.wikipedia.org/wiki/Privacy_concerns_with_social_networking_services). Social networks are built on the principle of sharing - but you, the user should be able to choose with whom you share what, and that is what the following sites aim to do.

| Provider | Description |
| --- | --- |
**[Aether](https://getaether.net)** | Self-governing communities with auditable moderation - a similar concept to Reddit, but more privacy-sensitive, democratic and transparent. Aether is open source and peer-to-peer, it runs on Windows, Mac and Linux
**[Discourse](https://www.discourse.org/)** | A 100% open source and self-hostable discussion platform you can use as a mailing list, discussion forum or long-form chat room.
**[Mastodon](https://mastodon.social/invite/A5JwL72F)** | A shameless Twitter clone, but open-source, distributed across independent servers, and with no algorithms that mess with users timelines
**[Minds](https://www.minds.com/register?referrer=as93)** | A social media site, which aims to bring people together and support open conversations. Get paid for creating content
**[Vero](https://vero.co/)** | (closed-source) A mobile-based social network, whose USP is that they have "No Ads. No Data Mining. No Algorithms." Since Vero is not open source, it is not possible to verify the validity of these claims

#### Other Notable Mentions
- [diaspora\*](https://diasporafoundation.org), [Pleroma](https://pleroma.social), [Friendica](https://friendi.ca) and [Hubzilla ](https://hubzilla.org) - distributed, decentralized social networks, built on open protocols
- [Tildes](https://tildes.net), [Lemmy](https://dev.lemmy.ml) and [notabug.io](https://notabug.io) - bulletin boards and news aggregators (similar to Reddit)
- [Pixelfed](https://pixelfed.org) - A free, ethical, federated photo sharing platform (FOSS alternative to Instagram)

#### Main-stream networks
The content on many of these smaller sites tends to be more *niche*. To continue using Twitter, there are a couple of [tweaks](https://www.offensiveprivacy.com/blog/twitter-privacy), that will improve security. For Reddit, use a privacy-respecting client - such as [Reditr](http://reditr.com/). Other main-stream social networking sites do not respect your privacy, so should be avoided, but if you choose to keep using them see [this guide](https://proprivacy.com/guides/social-media-privacy-guide) for tips on protecting your privacy


## Video Platforms

| Provider | Description |
| --- | --- |
**[PeerTube](https://joinpeertube.org)** | Free and open-source federated video platform that uses peer-to-peer technology to reduce load on individual servers when viewing videos. You can [self-host](https://docs.joinpeertube.org/#/install-any-os), or [find an instance](https://joinpeertube.org/instances#instances-list), and then watch videos from any PeerTube server
**[DTube](https://d.tube)** | A decentralized and ad-free video platform with little to no moderation that uses cryptocurrency and blockchain technology to pay its users.
**[BitTube](https://bittube.tv)** | A peer-to-peer, decentralized, censorship-free, ad-free video sharing and live streaming platform based on IPFS and blockchain technology
**[BitChute](https://www.bitchute.com/)** | A video hosting platform, that was founded in 2017 to allow uploaders to avoid content rules enforced on other platforms, such as YouTube

#### Word of Warning
Without moderation, some of these platforms accommodate video creators whose content may not be appropriate for all audiences

#### YouTube Proxies
The content on many of the smaller video sites, often just doesn't compare to YouTube. So another alternative, is to access YouTube through a proxy client, which reduces what Google can track.
- Good options are: [Invidious](https://invidious.io/) (web), [Piped](https://piped.kavin.rocks) (web), [FreeTube](https://freetubeapp.io/) (Windows, Mac OS, Linux), [NewPipe](https://newpipe.schabi.org/) (Android), [YouTube++](https://iosninja.io/ipa-library/download-youtube-plus-ipa-ios) (iOS)
- Or download videos with [youtube-dl](https://ytdl-org.github.io/youtube-dl/) (cli) or [youtube-dl-gui](https://github.com/MrS0m30n3/youtube-dl-gui) (gui). For just audio, there is [PodSync](https://podsync.net/)

#### Video Search Engines
[Petey Vid](https://www.peteyvid.com) is a non-biased video search engine. Unlike normal search engines it indexes videos from a lot of sources, including Twitter, Veoh, Instagram, Twitch, MetaCafe, Minds, BitChute, Brighteon, D-Tube, PeerTube, and many others.

## Blogging Platforms

| Provider | Description |
| --- | --- |
**[Write Freely](https://writefreely.org)** | Free and open source software with a clean UI, for creating a minimalist, federated blog. For premium or enterprise hosted plans, see [Write.as](https://write.as), or to host your own, check out the [repo on GitHub](https://github.com/writeas/writefreely)
**[Telegraph](https://telegra.ph)** | Created by [Telegram](https://www.theverge.com/2016/11/23/13728726/telegram-anonymous-blogging-platform-telegraph), Telegraph is fast, anonymous and simple
**[Mataroa](https://mataroa.blog)** | Naked blogging platform, for minimalists. [Open source](https://github.com/mataroa-blog/mataroa) and privacy-conscious.
**[Bear Blog](https://bearblog.dev/)** | A privacy-first, no-nonsense, super-fast blogging platform. [Repo on GitHub](https://github.com/HermanMartinus/bearblog).
**[Movim](https://movim.eu/)** | An [open-source](https://github.com/movim/movim) web frontend for XMPP that supports decentralized blogging and chatrooms.

#### Notable Mentions
If you use [Standard Notes](https://standardnotes.com/?s=chelvq36), then [Listed.to](https://listed.to) is a public blogging platform with strong privacy features. It lets you publish posts directly through the Standard Notes app or web interface. Other minimalistic platforms include [Notepin.co](https://notepin.co) and [Pen.io](http://pen.io).

Want to write a simple text post and promote it yourself? Check out [telegra.ph](https://telegra.ph), [txt.fyi](https://txt.fyi) and [NotePin](https://notepin.co). For seriously anonymous platforms, aimed at activists, see [noblogs](https://noblogs.org/) and [autistici](https://www.autistici.org). It is also possible to host a normal [WordPress](https://wordpress.com) site, without it being linked to your real identity, although WP does not have the best reputation when it comes to privacy.

Of course you could also host your blog on your own server, using a standard open source blog platform, such as [Ghost](https://ghost.org) and configure it to disable all trackers, ads and analytics.


## News Readers and Aggregation

| Provider | Description |
| --- | --- |
**[Tiny RSS](https://tt-rss.org)** | A free and open source web-based news feed (RSS/Atom) reader and aggregator
**[RSSOwl](http://www.rssowl.org)** | A desktop-based RSS reader, with powerful organisation features
**[Feedly](https://feedly.com)** | A more premium option. Feedly displays news from your selected sources in an easy-to-digest clean and modern interface. It works with more than just RSS feeds, since it is well integrated with many major news outlets. It does not manipulate the stories you see, and is mostly open source

#### Notable Mentions
For iPhone users in the US, [Tonic](https://canopy.cr/tonic) is a great little app that provides you with a selection of personalized new stories and articles daily. It is possible to use [Reddit](https://www.reddit.com) anonymously too - you can use throwaway accounts for posting.

#### Word of Warning
News reader apps don't have a good [reputation](https://vpnoverview.com/privacy/apps/privacy-risks-news-apps) when it comes to protecting users privacy, and often display biased content. Many have revenue models based on making recommendations, with the aim of trying to get you to click on sponsored articles - and for that a lot of data needs to have been collected about you, your habits, interests and routines. 


## Proxy Sites

These are websites that enable you to access existing social media platforms, without using their primary website - with the aim of improving privacy & security and providing better user experience. The below options are open source (so can be self-hosted, if you wish), and they do not display ads or tracking (unless otherwise stated).

| Provider | Description |
| --- | --- |
**[Nitter](https://nitter.net/)** (Twitter) | Nitter is a free and open source alternative Twitter front-end focused on privacy, it prevents Twitter from tracking your IP or browser fingerprint. It does not include any JavaScript, and all requests go through the backend, so the client never talks directly to Twitter. It's written in Nim, is super lightweight, with multiple themes and a responsive mobile version available, as well as customizable RSS feeds. Uses an unofficial API, with no rate limits or and no developer account required.
**[Invidious](https://invidious.io/)** (YouTube) | Privacy-focused, open source alternative frontend for YouTube. It prevents/ reduces Google tracking, and adds additional features, including an audio-only mode, Reddit comment feed, advanced video playback settings. It's super lightweight, and does not require JavaScript to be enabled, and you can import/ export your subscriptions list, and customize your feed. See list of [Invidious Public Instances](https://github.com/iv-org/invidious/wiki/Invidious-Instances).
**[Libreddit](https://libreddit.spike.codes/)** (Reddit) |  Private front-end for Reddit written in Rust. Massively [faster than Reddit](https://github.com/spikecodes/libreddit#speed) by not including ads, trackers or bloat. Libreddit can be deployed and selfhosted through `cargo`, Docker and Repl.it and proxies all requests through the back-end. Libreddit currently implements most of Reddit's functionalities that don't require users to be signed in.
**[WebProxy](https://weboproxy.com/)** | Free proxy service, with Tor mode (which is recommended to enable). Designed to be used to evade censorship and access geo-blocked content. The service is maintained by [DevroLabs](https://devrolabs.com/), who also run the [OnionSite](https://onionsite.weboproxy.com/) web proxy, they claim to that all traffic is 256-bit SSL-encrypted, but this cannot be verified - never enter any potentially personally identifiable information, and use it purely for consuming content. 

#### Notable Mentions
- **[NewPipe](https://newpipe.schabi.org/)** is an open source, privacy-respecting YouTube client for Android.
- **[FreeTube](https://freetubeapp.io/)** an open source YouTube client for Windows, MacOS and Linux, providing a more private experience, with a native-feel desktop app. It is built upon the [Invidious](https://invidious.io/) API.

#### Word of Warning
When proxies are involved - only use reputable services, and **never** enter any personal information


## Cryptocurrencies 

| Provider | Description |
| --- | --- |
**[Monero](https://www.getmonero.org)** | One of the most private cryptocurrencies, since no meta data is available (not even the transaction amount). It uses complex on-chain cryptographic methods such as Ring signatures, RingCT, Kovri, and Stealth addresses all of which help protect the privacy of users
**[ZCash](https://z.cash)** | Uses zero-knowledge proofs to protect privacy cryptographic technique, that allows two users to transact without ever revealing their true identity or address. The Zcash blockchain uses two types of addresses and transactions, Z transactions and addresses are private and T transactions and addresses are transparent like Bitcoin.

It is still possible to use currencies that have a public ledger 'privately', but you will need to take great care not to cause any transactions to be linked with your identity or activity. For example, avoid exchanges that require KYC, and consider using a service such as [Local Bitcoins](https://localbitcoins.net). If you use a [Bitcoin ATM](https://coinatmradar.com), then take care to not be physically tracked (CCTV, phone location, card payments etc)

#### Notable Mentions
Other privacy-focused cryptocurrencies include: [PIVX](https://pivx.org), [Bitcoin Private](https://btcprivate.org), [Verge](https://vergecurrency.com), and [Piratechain](https://pirate.black/). 

#### Word of Warning
Not all cryptocurrencies are anonymous, and without using a privacy-focused coin, a record of your transaction will live on a publicly available distributed ledger, forever. If you send of receive multiple payments, ensure you switch up addresses or use a mixer, to make it harder for anyone trying to trace your transactions. Cryptocurrencies that allow private and public transactions may reveal meta data about your transactions and balances when funds are moving from private to public addresses which can compromise your privacy with methods similar to a knapsack problem. Store private keys somewhere safe, but offline and preferably cold.

Note: Cryptocurrency prices can go down. Storing any wealth in crypto may result in losses. If you are new to digital currencies - do your research first, don't invest more than you can afford, and be very weary of scams and cryptocurrency-related malware. 

## Crypto Wallets

| Provider | Description |
| --- | --- |
**[Wasabi Wallet](https://www.wasabiwallet.io/)** (Bitcoin) | An open source, native desktop wallet for Windows, Linux and MacOS. Wasabi implements trustless CoinJoins over the Tor network. Neither an observer nor the participants can determine which output belongs to which input. This makes it difficult for outside parties to trace where a particular coin originated from and where it was sent to, which greatly improves privacy. Since it's trustless, the CoinJoin coordinator cannot breach the privacy of the participants. Wasabi is compatible with cold storage, and hardware wallets, including OpenCard and Trezor.
**[Trezor](https://trezor.io/)** <br>(All Coins) | Open source, cross-platform, offline, crypto wallet, compatible with 1000+ coins. Your private key is generated on the device, and never leaves it, all transactions are signed by the Trezor, which ensures your wallet is safe from theft. There are native apps for Windows, Linux, MacOS, Android and iOS, but Trezor is also compatible with other wallets, such as Wasabi. You can back the Trezor up, either by writing down the seed, or by duplicating it to another device. It is simple and intuitive to use, but also incredible customisable with a large range of advanced features.
**[ColdCard](https://coldcardwallet.com/)** (Bitcoin) | An easy-to-use, super secure Bitcoin hardware wallet, which can be used independently as an air-gapped wallet. ColdCard is based on partially signed Bitcoin transactions following the [BIP174](https://github.com/bitcoin/bips/blob/main/bip-0174.mediawiki) standard. Built specifically for Bitcoin, and with a variety of unique security features, ColdCard is secure, trustless, private and easy-to-use. Companion products for the ColdCard include: [BlockClock](http://blockclockmini.com/), [SeedPlate](http://bitcoinseedbackup.com/) and [ColdPower](http://usbcoldpower.com/)
**[Electrum](https://electrum.org/)** (Bitcoin) | Long-standing Python-based Bitcoin wallet with good security features. Private keys are encrypted and do not touch the internet and balance is checked with a watch-only wallet. Compatible with other wallets, so there is no tie-in, and funds can be recovered with your secret seed. It supports proof-checking to verify transactions using SPV, multi-sig  and add-ons for compatibility with hardware wallets. A decentralized server indexes ledger transactions, meaning it's fast and doesn't require much disk space. The potential security issue here would not be with the wallet, but rather your PC - you must ensure your computer is secure and your wallet has a long, strong passphrase to encrypt it with.
**[Samourai Wallet](https://samouraiwallet.com/)** (Bitcoin) | An open-source, Bitcoin-only privacy-focused wallet, with some innovative features.<br> Samourai Wallet works under any network conditions, with a full offline mode, useful for cold storage. It also supports a comprehensive range of privacy features including: STONEWALL that helps guard against address clustering deanonymization attacks, PayNym which allows you to receive funds without revealing your public address for all to see, Stealth Mode which hides Samourai from your devices launcher, Remote SMS Commands to wipe or recover your wallet if device is seized or stolen, and Whirlpool which is similar to a coin mixer, and OpenDime is also supported for offline USB hardware wallets.
**[Sparrow Wallet](https://sparrowwallet.com/)** (Bitcoin) | Sparrow is a Bitcoin wallet for those who value financial self sovereignty. Sparrow’s emphasis is on security, privacy and usability. Sparrow does not hide information from you - on the contrary it attempts to provide as much detail as possible about your transactions and UTXOs, but in a way that is manageable and usable.                
**[Atomic Wallet](https://atomicwallet.io/)** (All Coins) | Atomic is an open source desktop and mobile based wallet, where you're private keys are stored on your local device, and do not touch the internet. Atomic has great  feature sets, and supports swapping, staking and lending directly from the app. However, most of Atomic's features require an active internet connection, and Atomic [does not support](https://support.atomicwallet.io/article/160-does-atomic-wallet-offer-hardware-wallet-integration) hardware wallets yet. Therefor, it may only be a good choice as a secondary wallet, for storing small amounts of your actively used currency
**[CryptoSteel](https://cryptosteel.com/how-it-works)** <br>(All Coins) | A steel plate, with engraved letters which can be permanently screwed - CryptoSteel is a good fire-proof, shock-proof, water-proof and stainless cryptocurrency backup solution.
**[BitBox02](https://shiftcrypto.ch/)** (Bitcoin or Ethereum & ERC-20 tokens) | Open source hardware wallet, supporting secure multisig with the option for making encrypted backups on a MicroSD card.
**[ColdCard](https://coldcardwallet.com/)** (Bitcoin) | Secure, open source Bitcoin cold storage wallet, with the option for making encrypted backups on a MicroSD card.

#### Word of Warning
Avoid using any online/ hot-wallet, as you will have no control over the security of your private keys. Offline paper wallets are very secure, but ensure you store it properly - to keep it safe from theft, loss or damage.

### Notable Mentions
[Metamask](https://metamask.io/) (Ethereum and ERC20 tokens) is a bridge that allows you to visit and interact with distributed web apps in your browser. Metamask has good hardware wallet support, so you can use it to swap, stake, sign, lend and interact with dapps without you're private key ever leaving your device. However the very nature of being a browser-based app means that you need to stay vigilant with what services you give access to.

## Crypto Exchanges

| Provider | Description |
| --- | --- |
**[Bisq](https://bisq.network)** | An open-source, peer-to-peer application that allows you to buy and sell cryptocurrencies in exchange for national currencies. Fully decentralized, and no registration required.
**[LocalBitcoins](https://localbitcoins.com/)** | Person-to-person exchange, find people local to your area, and trade directly with them, to avoid going through any central organisation. Primarily focused on Bitcoin, Ethereum, Ripple and LiteCoin, as it gets harder to find people near you selling niche alt-coins
**[AtomicDEX](https://atomicdex.io/)** | Person-to-person cryptocurrency exchange with no KYC or registration required and uses atomic swaps to perform trustless trades. The orderbook uses a modified libp2p protocol to prevent censorship and maintain decentralization. Fiat currencies are not supported, but hundreds of alt-coins and major cryptocurrencies are supported.
**[RoboSats](https://learn.robosats.com/)** | RoboSats is an easy way to privately exchange Bitcoin for national currencies It simplifies the peer-to-peer experience and makes use lightning hold invoices to minimize custody and trust requirements. The deterministically generated avatars help users stick to best privacy practices.

#### Notable Mentions

For traders, [BaseFEX](https://www.basefex.com/) doesn't require ID and has a good privacy policy. [BitMex](https://www.bitmex.com/) has more advanced trading features, but ID verification is required for higher value trades involving Fiat currency. For buying and selling alt-coins, [Binance](https://www.binance.com/en/register?ref=X2BHKID1) has a wide range of currencies, and ID verification is not needed for small-value trades.


## Virtual Credit Cards

Virtual cards generated provide an extra layer of security, improve privacy and help protect from fraud. Most providers have additional features, such as single-use cards (that cannot be charged more than once), card limits (so you can be sure you won't be charged more than you expected) and other security controls.

| Provider | Description |
| --- | --- |
**[Privacy.com](https://privacy.com/join/VW7WC)** | Privacy.com has a good reputation, and is the largest virtual card provider in the US. Unlike other providers, it is free for personal use (up to 12 cards per month) with no fees, apps and support is good. There is a premium is plan for $10/month, with 1% cashback 36 cards/ month
**[Revolut Premium](https://revolut.ngih.net/Q9jdx)** | Revolut is more of a digital bank account, and identity checks are required to sign up. Virtual cards only availible on Premium/ Metal accounts, which start at $7/month.
**[MySudo](https://mysudo.com)** | Much more than just virtual cards, MySudo is a platform for creating compartmentalised identities, each with their own virtual cards, virtual phone numbers, virtual email addresses, messaging, private browsing and more. There is a free plan for up to 3 identities, and premium plans start at $0.99/ month
**[Blur](https://dnt.abine.com/#feature/payments)** | Blur by Abine has virtual card functinality, 

*[PayLasso](https://www.paylasso.com), [JoinToken](https://jointoken.com), [EntroPay](https://www.entropay.com) are now discontinued*


## Other Payment Methods

| Provider | Description |
| --- | --- |
**Cash** | Actual physical cash is still the most private option, with no chance of leaving any transactional records
**Gift Cards** | Gift cards can be purchased for cash in many convenience stores, and redeemed online for goods or services. Try to avoid CCTV as best as possible.
**Pre-paid Cards** | Similarly to gift cards, buying a pre-paid card for cash, can enable you to purchase goods and services in stores that only accept card payments.

Paying for goods and services is a good example of where privacy and security conflict; the most secure option would be to pay with credit card, since most providers include comprehensive fraud protection, whereas the most private option would be to pay using crypto currency or cash, since neither can be easily tied back to your identity.

#### Word of Warning
Note that credit card providers heavily track transaction metadata, which build up a detailed picture of each persons spending habits. This is done both to provide improved fraud alerts, but also because the data is extremely valuable and is often 'anonymized' and sold to 3rd parties. Hence your privacy is degraded if these cards are used for daily transactions


## Budgeting Tools

| Provider | Description |
| --- | --- |
**[Firefly III](https://www.firefly-iii.org)** (Self-hosted) | A free and open source personal finance manager. Firefly III has all essential features, a clean and clear UI and is easy to set up and use (see [live demo](https://demo.firefly-iii.org)). It's backed by a strong community, and is regularly updated with new features, improvements and fixes. There is also a hass.io [addon](https://github.com/hassio-addons/addon-firefly-iii), and it works nicely with [Home Assistant](https://www.home-assistant.io). Note: Since it is self-hosted, you will need to ensure that your server (either local or remote) is correctly configured for security.
**[EasyBudget](https://play.google.com/store/apps/details?id=com.benoitletondor.easybudgetapp)** (Android) | Clean and easy-to-use app open source budgeting app. It doesn't have all the features that alternatives offer, but it does simple budget management and planning very effectively
**[HomeBank](http://homebank.free.fr)** (Desktop) | Desktop personal financial management option. Great for generating charts, dynamic reports and visualising transactions. HomeBank makes it easy to import financial data from other software (Quick Books, Microsoft Money etc) and bank accounts (in OFX/QFX, QIF, CSV format), and has all the essential features you'd expect. Available on Linux and Windows (and a 3rd-party port for Mac OS)
**[GnuCash](https://www.gnucash.org)** (Desktop) | Full-featured cross-platform accounting application, which works well for both personal and small business finance. First released in 1998, GnuCash is long standing and very stable, and despite a slightly dated UI, it's still a very popular option. Originally developed for Linux, GnuCash is now available for Windows, Mac and Linux and also has a well rated official [Android app](https://play.google.com/store/apps/details?id=org.gnucash.android&hl=en)
**[Plain Text Accounting](https://plaintextaccounting.org)** | Plain text accounting is a way of doing bookkeeping / accounting with plain text files and scriptable, command-line-friendly software, such as Ledger](https://www.ledger-cli.org), [hledger](https://hledger.org/), [Beancount](https://github.com/beancount/beancount) and [more](https://plaintextaccounting.org/#pta-apps). Unlike other tools, you have full control over your data, and are not tied to a particular vendor

#### Notable Mentions
Spreadsheets remain a popular choice for managing budgets and financial planning.  [Collabora](https://nextcloud.com/collaboraonline) or [OnlyOffice](https://nextcloud.com/onlyoffice) (on [NextCloud](https://nextcloud.com)), [Libre Office](https://www.libreoffice.org) and [EtherCalc](https://ethercalc.net) are popular open source spread sheet applications. [Mintable](https://github.com/kevinschaich/mintable) allows you to auto-populate your spreadsheets from your financial data, using publicly accessible API - mitigating the requirement for a dedicated budgeting application.

Other notable open source budgeting applications include: [Smart Wallet](https://apps.apple.com/app/smart-wallet/id1378013954) (iOS), [My-Budget](https://rezach.github.io/my-budget) (Desktop), [MoneyManager EX](https://www.moneymanagerex.org), [Skrooge](https://skrooge.org), [kMyMoney](https://kmymoney.org) and [Budget Zen](https://budgetzen.net) (a simple E2E encrypted budget manager)

See Also: [Cryptocurrencies](#cryptocurrencies), [Virtual Credit Cards](#virtual-credit-cards) and [Other Payment Methods](#other-payment-methods)

See Also: [Personal Finance Security Tips](README.md#personal-finance)

<hr id="operating-systems" />

## Mobile Operating Systems

If you are an Android user, your device has Google built-in at its core. [Google tracks you](https://digitalcontentnext.org/blog/2018/08/21/google-data-collection-research/),
collecting a wealth of information, and logging your every move. A [custom ROM](https://www.xda-developers.com/what-is-custom-rom-android/), is an open source, usually Google-free mobile OS that can be [flashed](https://www.xda-developers.com/how-to-install-custom-rom-android/) to your device.

| Provider | Description |
| --- | --- |
**[GrapheneOS](https://grapheneos.org/)** | GrapheneOS is an open source privacy and security focused mobile OS with Android app compatibility. Developed by [Daniel Micay](https://twitter.com/DanielMicay). GrapheneOS is a young project, and currently only supports Pixel devices, partially due to their [strong hardware security](https://grapheneos.org/faq#device-support).
**[CalyxOS](https://calyxos.org/)** | CalyxOS is an free and open source Android mobile operating system that puts privacy and security into the hands of everyday users. Plus, proactive security recommendations and automatic updates take the guesswork out of keeping your personal data personal. Also currently only supports Pixel devices and Xiaomi Mi A2 with Fairphone 4, OnePlus 8T, OnePlus 9 test builds available. Developed by the Calyx Foundation.
**[DivestOS](https://divestos.org)** | DivestOS is a vastly diverged unofficial more secure and private soft fork of LineageOS. DivestOS primary goal is prolonging the life-span of discontinued devices, enhancing user privacy, and providing a modest increase of security where/when possible. Project is developed and maintained solely by Tad (SkewedZeppelin) since 2014.
**[LineageOS](https://www.lineageos.org/)** | A free and open-source operating system for various devices, based on the Android mobile platform - Lineage is light-weight, well maintained, supports a wide range of devices, and comes bundled with [Privacy Guard](https://en.wikipedia.org/wiki/Android_Privacy_Guard)


#### Other Notable Mentions
[Replicant OS](https://www.replicant.us/) is a fully-featured distro, with an emphasis on freedom, privacy and security. [OmniRom](https://www.omnirom.org/), [Resurrection Remix OS](https://resurrectionremix.com/), and [Paranoid Android](http://paranoidandroid.co/) are also popular options. Alternatively, [Ubuntu Touch](https://ubports.com/) is a Linux (Ubuntu)- based OS. It is secure by design and runs on almost any device, - but it does fall short when it comes to the app store.

To install apps on the Play Store without using the Play Store app see [Aurora Store](https://gitlab.com/AuroraOSS/AuroraStore). For Google Play Service see [MicroG](https://microg.org/)


#### Word of Warning
It is not recommended to root, or flash your device with a custom ROM if you are not an advanced user. There are risks involved
- Although the above ROMs omit Google, they do open up other security issues: Without DM-verity on the system partition, the file system *could* be tampered with, and no verified boot stack, the kernel/initramfs also *could* be edited. You should understand the risks, before proceeding to flash a custom ROM to your device
- You will need to rely on updates from the community, which could be slower to be released - this may be an issue for a time-urgent, security-critical patch
- It is also possible to brick your device, through interrupted install or bad software
- Finally, rooting and flashing your device, will void your warranty


## Desktop Operating Systems

Windows 10 has many features that violate your privacy. Microsoft and Apple are able to collect all your data (including, but not limited to: keystrokes, searches and mic input, calendar data, music, photos, credit card information and purchases, identity, passwords, contacts, conversations and location data). Microsoft Windows is also more susceptible to malware and viruses, than alternative systems.

Switching to Linux is a great choice in terms of security and privacy - you don't need necessarily need to use a security distro, any well-maintained stable distro is going to be considerably better than a proprietary OS

| Provider | Description |
| --- | --- |
**[Qubes OS](https://www.qubes-os.org/)** (containerized apps) | Open-source security-oriented operating system for single-user desktop computing. It uses virtualisation, to run each application in its own compartment to avoid data being leaked. It features [Split GPG](https://www.qubes-os.org/doc/split-gpg/), [U2F Proxy](https://www.qubes-os.org/doc/u2f-proxy/), and [Whonix integration](https://www.qubes-os.org/doc/whonix/). Qubes makes is easy to create [disposable VMs](https://www.qubes-os.org/doc/disposablevm/) which are spawned quickly and destroyed when closed. Qubes is [recommended](https://twitter.com/Snowden/status/781493632293605376) by Edward Snowden
**[Whonix](https://www.whonix.org/)** (VM) | Whonix is an anonymous operating system, which can run in a VM, inside your current OS. It is the best way to use Tor, and provides very strong protection for your IP address. It comes bundled with other features too: Keystroke Anonymization, Time Attack Defences, Stream Isolation, Kernel Self Protection Settings and an Advanced Firewall. Open source, well audited, and with a strong community - Whonix is based on Debian, [KickSecure](https://www.whonix.org/wiki/Kicksecure) and [Tor](https://www.whonix.org/wiki/Whonix_and_Tor)
**[Tails](https://tails.boum.org/)** (live) | Tails is a live operating system (so you boot into it from a USB, instead of installing). It preserves your privacy and anonymity through having no persistent memory/ leaving no trace on the computer. Tails has Tor built-in system-wide, and uses state-of-the-art cryptographic tools to encrypt your files, emails and instant messaging. Open source, and built on top of Debian. Tails is simple to stop, configure and use
**[Parrot](https://parrotlinux.org/)** (security)| Parrot Linux, is a full Debian-based operating system, that is geared towards security, privacy and development. It is fully-featured yet light-weight, very open. There are 3 editions: General Purpose, Security and Forensic. The Secure distribution includes its own sandbox system obtained with the combination of [Firejail](https://firejail.wordpress.com/) and [AppArmor](https://en.wikipedia.org/wiki/AppArmor) with custom security profiles. While the Forensics Edition is bundled with a comprehensive suite of security/ pen-testing tools, similar to Kali and Black Arch
**[Discreete Linux](https://www.privacy-cd.org/)** (offline)| Aimed at journalists, activists and whistle-blowers, Discreete Linux is similar to Tails, in that it is booted live from external media, and leaves no/ minimal trace on the system. The aim of the project, was to provide all required cryptographic tools offline, to protect against Trojan-based surveillance
**[Alpine Linux](https://www.alpinelinux.org/)** | Alpine is a security-oriented, lightweight distro based on musl libc and busybox. It compiles all user-space binaries as position-independent executables with stack-smashing protection. Install and setup may be quite complex for some new users

#### Notable Mentions
[Septor](https://septor.sourceforge.io/) is a Debian-based distro with the KDE Plasma desktop environment, and Tor baked-in. Designed for surfing the web anonymously, and completing other internet-based activities (with Thunderbird, Ricochet IM, HexChat, QuiteRSS, OnionShare). Septor is light-weight, but comes bundled with all the essential privacy + security utilities (including: Gufw, Ark, Sweeper, KGpg, Kleopatra, KWallet, VeraCrypt, Metadata Anonymisation Toolkit and more).

[Subgraph OS](https://subgraph.com) is designed to be an *adversary resistant computing platform*, it includes strong system-wide attack mitigations, and all key applications run in sandbox environments. Subgraph is still in beta (at the time of writing), but still is well tested, and has some nice anonymization features

For defensive security, see [Kali](https://www.kali.org) and [BlackArch](https://blackarch.org), both are bundled with hundreds of security tools, ready for pretty much any job.  

Other security-focused distros include: [TENS OS](https://www.tens.af.mil/), [Fedora CoreOS](https://getfedora.org/coreos?stream=stable), [Kodachi](https://www.digi77.com/linux-kodachi/) and [IprediaOS](https://www.ipredia.org). (Avoid systems that are not being actively maintained)


#### General Purpose Linux Distros
If you do not want to use a specalist security-based distro, or you are new to Unix - then just switching to any well-maintained Linux distro, is going to be significantly more secure and private than Windows or Mac OS.
Since it is open source, major distros are constantly being audited by members of the community. Linux does not give users admin rights by default - this makes is much less likely that your system could become infected with malware. And of course, there is no proprietary Microsoft or Apple software constantly monitoring everything you do.

Some good distros to consider would be: **[Fedora](https://getfedora.org/)**, **[Debian](https://www.debian.org/)**, or **[Arch](https://www.archlinux.org/)**- all of which have a large community behind them. **[Manjaro](https://manjaro.org/)** (based of Arch) is a good option, with a simple install process, used by new comers, and expers alike.  **[POP_OS](https://pop.system76.com/)** and **[PureOS](https://www.pureos.net/)** are reasonably new general purpose Linux, with a strong focus on privacy, but also very user-friendly with an intuitive interfac and install process. See [Simple Comparison](https://computefreely.org/) or [Detailed Comparison](https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions).

#### BSD
BSD systems arguably have far superior network stacks. **[OpenBSD](https://www.openbsd.org)** is designed for maximum security — not just with its features, but with its implementation practices. It’s a commonly used OS by banks and critical systems. **[FreeBSD](https://www.freebsd.org)** is more popular, and aims for high performance and ease of use.

#### Windows
Two alternative options for Windows users are Windows 10 AME (ameliorated) project and the LTSC stream.
**[Windows 10 AME](https://ameliorated.info/)** AME project aims at delivering a stable, non-intrusive yet fully functional build of Windows 10 to anyone, who requires the Windows operating system natively. Core applications, such as the included Edge web-browser, Windows Media Player, Cortana, as well as any appx applications (appx apps will no longer work), have also been successfully eliminated. The total size of removed files is about 2 GB. Comes as a pre-built ISO or option to build from scratch with de-bloat scripts. Strong, supportive community on Telegram.
**[Windows 10 LTSC](https://docs.microsoft.com/en-us/windows/whats-new/ltsc/)** LTSC provides several security benefits over a standard Win 10 Installation. LTSC or Long Term Servicing Channel is a lightweight, low-cost Windows 10 version, that is intended for specialized systems, and receives less regular feature updates. What makes it appealing, is that it doesn't come with any bloatware or non-essential applications, and needs to be configured from the ground up by the user. This gives you much better control over what is running on your system, ultimately improving security and privacy. It also includes several enterprise-grade [security features](https://docs.microsoft.com/en-us/windows/whats-new/ltsc/whats-new-windows-10-2019#security), which are not available in a standard Windows 10 instance. It does require some technical knowledge to get started with, but once setup should perform just as any other Windows 10 system. Note that you should only download the LTSC ISO from the Microsoft's [official page](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-10-enterprise) 


#### Improve the Security and Privacy of your current OS
After installing your new operating system, or if you have chosen to stick with your current OS, there are a couple of things you can do to improve security. See: [Windows 10 security guide](https://heimdalsecurity.com/en/windows-10-security-guide/privacy), [Mac OS security guide](https://spreadprivacy.com/mac-privacy-tips/) or [Linux security guide](https://spreadprivacy.com/linux-privacy-tips/).

## Linux Defences

| Provider | Description |
| --- | --- |
**[Firejail](https://github.com/netblue30/firejail)** | Firejail is a SUID sandbox program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf. Written in C, virtually no dependencies, runs on any modern Linux system, with no daemon running in the background, no complicated configuration, and it's super lightweight and super secure, since all actions are implemented by the kernel. It includes security profiles for over 800 common Linux applications. FireJail is recommended for running any app that may potential pose some kind of risk, such as torrenting through Transmission, browsing the web, opening downloaded attachments
**[Gufw](http://gufw.org)** (Linux) | Open source GUI firewall for Linux, allowing you to block internet access for certain applications. Supports both simple and advanced mode, GUI and CLI options, very easy to use, lightweight/ low-overhead, under active maintenance and backed by a strong community. Installable through most package managers, or compile from [source](https://answers.launchpad.net/gui-ufw) <br> Other popular firewalls are [OpenSnitch](https://github.com/evilsocket/opensnitch) and [Uncomplicated Firewall](https://en.wikipedia.org/wiki/Uncomplicated_Firewall), see more [firewalls](#firewalls)
**[ClamTk](https://dave-theunsub.github.io/clamtk/)** | ClamTk is basically a graphical front-end for ClamAV, making it an easy to use, light-weight, on-demand virus scanner for Linux systems
**[chkrootkit](http://www.chkrootkit.org)** | Locally checks for signs of a rootkit
**[Snort](https://www.snort.org)** | open source intrusion prevention system capable of real-time traffic analysis and packet
**[BleachBit](https://www.bleachbit.org)** | Clears cache and deletes temporary files very effectively. This frees up disk space, improves performance, but most importantly helps to protect privacy

#### Notable Mentions
[SecTools.org](https://sectools.org) is a directory or popular Unix security tools.

## Windows Defences

| Provider | Description |
| --- | --- |
**[Windows Spy Blocker](https://github.com/crazy-max/WindowsSpyBlocker)** | Capture and interprets network traffic based on a set of rules, and depending on the interactions certain assignments are blocked. Open source, written in Go and delivered as a single executable
**[HardenTools]** | A utility that disables a number of risky Windows features. These "features" are exposed by the OS and primary consumer applications, and very commonly abused by attackers, to execute malicious code on a victim's computer. So this tool just reduces the attack surface by disabling the low-hanging fruit
**[ShutUp10](https://www.oo-software.com/en/shutup10)** | A portable app that lets you disable core Windows features (such as Cortana, Edge) and control which data is passed to Microsoft. (Note: Free, but not open source)
**[WPD](https://wpd.app/)** | Portable app with a GUI, that makes it really easy to safely block key telemetry features, from sending data to Microsoft and other third parties (It uses the Windows API to interact with key features of Local Group Police, Services, Tasks Scheduler, etc)
**[GhostPress]** | Anti low-level keylogger: Provides full system-wide key press protection, and target window screenshot protection
**[KeyScrambler]** | Provides protection against software keyloggers. Encrypts keypresses at driver level, and decrypts at application level, to protect against common keyloggers - read more about [how it works](https://www.techrepublic.com/blog/it-security/keyscrambler-how-keystroke-encryption-works-to-thwart-keylogging-threats). Developed by Qian Wang
**[SafeKeys V3.0](http://www.aplin.com.au)** | Portable virtual keyboard. Useful for protecting from keyloggers when using a public computer, as it can run of a USB with no administrative permissions
**[RKill]** | Useful utility, that attempts to terminate known malware processes, so that your normal security software can then run and clean your computer of infections
**[IIS Crypto]** | A utility for configuring encryption protocols, cyphers, hashing methods, and key exchanges for Windows components. Useful for sysadmins on Windows Server
**[NetLimiter]** | Internet traffic control and monitoring tool
**[Sticky-Keys-Slayer]** | Scans for accessibility tools backdoors via RDP
**[SigCheck]** | A CLI utility that shows file version number, timestamp information, and digital signature details. It's useful to audit a Windows host's root certificate store against Microsoft's Certificate Trust List (CTL), and lets you perform [VirusTotal](www.virustotal.com) lookups
**[BleachBit](https://www.bleachbit.org)** | Clears cache and deletes temporary files very effectively. This frees up disk space, improves performance, but most importantly helps to protect privacy
**[Windows Secure Baseline]** | Group Policy objects, compliance checks, and configuration tools that provide an automated and flexible approach for securely deploying and maintaining the latest releases of Windows 10
**[USBFix](https://www.usb-antivirus.com/)** | Detects infected USB removable devices
**[GMER](http://www.gmer.net)** | Rootkit detection and removal utility
**[ScreenWings](https://schiffer.tech/screenwings.html)** | Blocks malicious background applications from taking screenshots
**[CamWings](https://schiffer.tech/camwings.html)** | Blocks unauthorized webcam access
**[SpyDish](https://github.com/mirinsoft/spydish)** | Open source GUI app built upon PowerShell, allowing you to perform a quick and easy privacy check, on Windows 10 systems. Highlights many serious issues, and provides assistance with fixing
**[SharpApp](https://github.com/mirinsoft/sharpapp)** | Open source GUI app built upon PowerShell, for disabling telemetry functions in Windows 10, uninstalling preinstalled apps, installing software packages and automating Windows tasks with integrated PowerShell scripting
**[Debotnet](https://github.com/Mirinsoft/Debotnet)** | Light-weight, portable app for controlling the many privacy-related settings within Windows 10- with the aim of helping to keep private data, private 
**[PrivaZer](https://privazer.com/)** | Good alternative to CCleaner, for deleting unnecessary data - logs, cache, history, etc 

#### Word of Warning
(The above software was last tested on 01/05/20). Many of the above tools are not necessary or suitable for beginners, and can cause your system to break - only use software that you need, according to your threat model. Take care to only download from an official/ legitimate source, verify the executable before proceeding, and check reviews/ forums. Create a system restore point, before making any significant changes to your OS (such as disabling core features). From a security and privacy perspective, Linux may be a better option.  

#### See Also
- [github.com/Awesome-Windows/Awesome#security]
- [github.com/PaulSec/awesome-windows-domain-hardening]
- [github.com/meitar/awesome-cybersecurity-blueteam#windows-based-defenses]

[HardenTools]: https://github.com/securitywithoutborders/hardentools
[Sticky-Keys-Slayer]: https://github.com/linuz/Sticky-Keys-Slayer
[SigCheck]: https://docs.microsoft.com/en-us/sysinternals/downloads/sigcheck
[Windows Secure Baseline]: https://github.com/nsacyber/Windows-Secure-Host-Baseline
[IIS Crypto]: https://www.nartac.com/Products/IISCrypto
[NetLimiter]: https://www.netlimiter.com
[github.com/Awesome-Windows/Awesome#security]: https://github.com/Awesome-Windows/Awesome#security
[github.com/PaulSec/awesome-windows-domain-hardening]: https://github.com/PaulSec/awesome-windows-domain-hardening
[github.com/meitar/awesome-cybersecurity-blueteam#windows-based-defenses]: https://github.com/meitar/awesome-cybersecurity-blueteam#windows-based-defenses
[KeyScrambler]: https://www.qfxsoftware.com
[GhostPress]: https://schiffer.tech/ghostpress.html
[RKill]: https://www.bleepingcomputer.com/download/rkill/


## Mac OS Defences

| Provider | Description |
| --- | --- |
**[LuLu]** | Free, open source macOS firewall. It aims to block unknown outgoing connections, unless explicitly approved by the user
**[Stronghold]** | Easily configure macOS security settings from the terminal
**[Fortress]** | Kernel-level, OS-level, and client-level security for macOS. With a Firewall, Blackhole, and Privatizing Proxy for Trackers, Attackers, Malware, Adware, and Spammers; with On-Demand and On-Access Anti-Virus Scanning

[LuLu]: https://objective-see.com/products/lulu.html
[Stronghold]: https://github.com/alichtman/stronghold
[Fortress]: https://github.com/essandess/macOS-Fortress


## Anti-Malware

Cross-platform, open source malware detection and virus prevention tools

| Provider | Description |
| --- | --- |
**[ClamAV](https://www.clamav.net)** | An open source  cross-platform antivirus engine for detecting viruses, malware & other malicious threats. It is versatile, performant and very effective
**[VirusTotal](https://www.virustotal.com)** | Web-based malware scanner, that inspects files and URLs with over 70 antivirus scanners, URL/domain services, and other tools to extract signals and determine the legitimacy
**[Armadito](https://www.armadito.com)** | Open source signature-based anti-virus and malware detection for Windows and Linux. Supports both ClamAV signatures and YARA rules. Has a user-friendly interface, and includes a web-based admin panel for remote access.

#### Notable Mentions
For 1-off malware scans on Windows, [MalwareBytes](https://www.malwarebytes.com) is portable and very effective, but [not open source](https://forums.malwarebytes.com/topic/5495-open-source)

#### Word of Warning
For Microsoft Windows, Windows Defender provides totally adequate virus protection in most cases. These tools are intended for single-use in detecting/ removing threats on an infected machine, and are not recommended to be left running in the background, use portable editions where available.

Many anti virus products have a history of introducing vulnerabilities themselves, and several of them seriously degrade the performance of your computer, as well as decrease your privacy. Never use a free anti-virus, and never trust the companies that offer free solutions, even if you pay for the premium package. This includes (but not limited to) Avast, AVG, McAfee and Kasperky. For AV to be effective, it needs intermate access to all areas of your PC, so it is important to go with a trusted vendor, and monitor its activity closely. 


<hr id="home-iot" />

## Home Automation

If you have smart devices within your home, you should consider running the automation locally, rather than using a cloud service. This will reduce the amount of exploits you could potentially be vulnerable to. It is also important to have network monitoring and firewalls enabled, to ensure suspicious activity is flagged or blocked. The following projects will make controlling and monitoring IoT devices within your home easier, safer and more private.

| Provider | Description |
| --- | --- |
**[Home Assistant](https://www.home-assistant.io)** | Open source home automation that puts local control and privacy first - 1500+ integrations. Runs well on a Raspberry Pi, accessible though a web interface and CLI, as well as several controller apps (such as [HassKit](https://play.google.com/store/apps/details?id=com.thhkstudio.hasskit) and the official [Home Assistant App](https://play.google.com/store/apps/details?id=io.homeassistant.companion.android))
**[OpenHAB](https://www.openhab.org)** | A vendor and technology agnostic open source automation software for your home, with 2000+ supported devices and addons. Works well on a Raspberry Pi, or low-powered home server, and again there are some great apps for, such as the official [OpenHabb App](https://play.google.com/store/apps/details?id=org.openhab.habdroid) and the [HomeHabit](https://play.google.com/store/apps/details?id=app.homehabit.view) wall dashboard
**[Domoticz](https://www.domoticz.com)** | Another home automation system, Domoticz is more geared towards connecting and monitoring sensors within your space. Allows you to monitor your environment without anyone but you having access to the data
**[Node-RED](https://nodered.org)** | Node-RED is a programming tool for wiring together hardware devices, APIs and online services, it provides a browser-based editor that makes it easy to build flows with a wide range of supported nodes, and it is easy to deploy locally in your network

#### Notable Mentions 
For creating dashboard from IoT devices, see [ThingsBoard](https://thingsboard.io). Another home automation tool is [FHEM](https://fhem.de/fhem.html), which has been around for a while and needs a bit more work to get up and running, but is still a popular option.

#### Word of Warning
IoT smart home devices can open you up to many security risks and exploits. It is really important that you configure them correctly, setting strong unique passwords, turn off data sharing, and if possible restrict internet access so devices can only communicate within your local network. See [Smart Home Security Checklist](https://github.com/Lissy93/personal-security-checklist#smart-home) for more tips.

<hr id="development">

## Code Hosting

| Provider | Description |
| --- | --- |
[SourceHut](https://sourcehut.org/) | Git and mercurial code hosting, task management, mailing lists, wiki hosting and Alpine-based build pipelines. Can be self-hosted, or used through the managed instance at [sr.ht](https://sr.ht/)
[Codeberg](https://codeberg.org/) | A fully-managed instance of [Forgejo](https://forgejo.org)
[GitLab](https://gitlab.com) | Fully-featured git, CI and project management platform. Managed instance available, but can also be self-hosted
[Gitea](https://gitea.io/) | Lightweight self-hosted git platform, written in Go
[Gogs](https://gogs.io/) | Lightweight self-hosted git platform, written in Go


## AI Voice Assistants

Google Assistant, Alexa and Siri don't have the best [reputation](https://srlabs.de/bites/smart-spies) when it comes to protecting consumers privacy, there have been [many recent breaches](https://www.theverge.com/2019/10/21/20924886/alexa-google-home-security-vulnerability-srlabs-phishing-eavesdropping). For that reason it is recommended not to have these devices in your house. The following are open source AI voice assistants, that aim to provide a human voice interface while also protecting your privacy and security

| Provider | Description |
| --- | --- |
**[Mycroft](https://mycroft.ai)** | An open source privacy-respecting AI platform, that runs on many platforms (Raspberry Pi, desktop, or dedicated Mycroft device). It is in active development, with thorough documentation and a broad range of available skills, but also Mycroft makes it really easy to develop new skills
**[Kalliope](https://kalliope-project.github.io)** | An open source, modular always-on voice controlled personal assistant designed for home automation. It runs well on Raspberry Pi, Debian or Ubuntu and is easy to program with simple YAML-based skills, but does not have a wide library of pre-built add-ons

#### Notable Mentions
If you choose to continue using Google Home/ Alexa, then check out **[Project Alias](https://github.com/bjoernkarmann/project_alias)**. It's a small app that runs on a Pi, and gives you more control over your smart assistants, for both customisation and privacy.

For a desktop-based assistant, see [Dragonfire](https://github.com/DragonComputer/Dragonfire) for Ubuntu, and [Jarvis](https://github.com/sukeesh/Jarvis) for MacOS.  [LinTO](https://linto.ai), [Jovo](https://www.jovo.tech) and [Snips](https://snips.ai) are private-by-design voice assistant frameworks that can be built on by developers, or used by enterprises. [Jasper](https://jasperproject.github.io), [Stephanie](https://github.com/SlapBot/stephanie-va) and [Hey Athena](https://github.com/rcbyron/hey-athena-client) are Python-based voice assistant, but neither is under active development anymore. See also [OpenAssistant](https://openassistant.org).

#### Word of Warning
If you are building your own assistant, you may want to consider a hardware-switch for disabling the microphone. Keep tabs on issues and check the code, to ensure you are happy with how it works, from a privacy perspective.

<hr id="bonus" />

## Bonus #1 - Alternatives to Google
Moving away from Google, and using multiple alternative apps will mean there is no single source of tracking. Open source and privacy-focused software is best

- Academic: [RefSeek](https://www.refseek.com), [Microsoft Academic](https://academic.microsoft.com), [More Academic Search Engines](https://en.wikipedia.org/wiki/List_of_academic_databases_and_search_engines)
- Analytics: [Matomo](https://matomo.org), [Privalytics](https://www.privalytics.io), [Plausible](https://plausible.io), [Fathom](https://github.com/usefathom/fathom), [GoatCounter](https://www.goatcounter.com), [ShyNet](https://github.com/milesmcc/shynet), [Pirsch](https://pirsch.io/)
- Assistant: [Mycroft](https://mycroft.ai), [Kalliope](https://kalliope-project.github.io), [Project-Alias](https://github.com/bjoernkarmann/project_alias) (for Google Home/ Alexa)
- Authenticator: [Aegis](https://getaegis.app) (Android), [Authenticator](https://github.com/mattrubin/authenticator) (ios)
- Blogging: [Write Freely](https://writefreely.org), [Telegraph](https://telegra.ph), [Mataroa](https://mataroa.blog/), [Bear Blog](https://bearblog.dev/), [Ghost](https://ghost.org) (Self-Hosted)
- Browsers: [Brave](https://brave.com/?ref=ali721), [Firefox](https://www.mozilla.org/firefox) (with some [tweaks](https://restoreprivacy.com/firefox-privacy/)), [Vivaldi](https://vivaldi.com)
- Calendar: [EteSync](https://www.etesync.com/accounts/signup/?referrer=QK6g), [ProtonCalendar](https://protonmail.com/blog/protoncalendar-beta-announcement), [NextCloud Calendar](https://apps.nextcloud.com/apps/calendar) (self-hosted), [Radicale](https://radicale.org/v3.html) (self-hosted, also supports contact lists)
- Cloud: [Njalla](https://njal.la), [Vindo](https://www.vindohosting.com), [Private Layer](https://www.privatelayer.com)
- DNS: [Cloudflare](https://blog.cloudflare.com/announcing-1111), [Quad9](https://www.quad9.net)
- Docs: [NextCloud](https://nextcloud.com), [CryptPad](https://cryptpad.fr), [Skiff](https://skiff.com/pages)
- Finance: [Wallmine](https://wallmine.com), [MarketWatch](https://www.marketwatch.com/tools/quotes/lookup.asp), [Nasdaq Lookup](https://www.nasdaq.com/market-activity/stocks)
- Flights: [SkyScanner](https://www.skyscanner.net), [Kayak](https://www.kayak.co.uk) (Note: Beware of tracking, use Tor)
- Location Tracker: [Private Kit](https://play.google.com/store/apps/details?id=edu.mit.privatekit)
- Mail: [ProtonMail](https://protonmail.com), [Tutanota](https://tutanota.com), [MailFence](https://mailfence.com?src=digitald), [HushMail](https://www.hushmail.com/tapfiliate/?tap_a=44784-d2adc0&tap_s=724845-260ce4&program=hushmail-for-small-business), [Skiff](https://skiff.com/mail)
- Maps: [OpenStreetMaps](https://www.openstreetmap.org) (web), [OsmAnd](https://osmand.net) (Android + iOS)
- Messaging: [Signal](https://signal.org) (Mobile Number Required), [KeyBase](https://keybase.io), [Session](https://getsession.org)
- Mobile OS: [LineageOS](https://www.lineageos.org), [GrapheneOS](https://grapheneos.org), [Ubuntu Touch](https://ubports.com)
- Notes: [Cryptee](https://crypt.ee), [Joplin](https://joplinapp.org), [Standard Notes](https://standardnotes.com/?s=chelvq36), [Joplin](https://joplinapp.org)
- Passwords: [BitWarden](https://bitwarden.com), [1Password](https://1password.com), [KeePassXC](https://keepassxc.org), [LessPass](https://lesspass.com)
- Pay (Currencies): [Monero](https://www.getmonero.org), [ZCash](https://z.cash)
- Pay (Virtual Cards): [Privacy.com](https://privacy.com/join/VW7WC), [Revolut](https://revolut.ngih.net/Q9jdx) (disposable virtual credit cards)
- Photos: [PhotoPrism](https://photoprism.app/) (Self-Hosted)
- Play Store: [F-Droid](https://f-droid.org), [APK Mirror](https://www.apkmirror.com)
- Search: [DuckDuckGo](https://duckduckgo.com), [Searx](https://searx.github.io/searx/) (self-hosted), [Qwant](https://www.qwant.com)
- Sync: [SeaFile](https://www.seafile.com), [Syncthing](https://syncthing.net), [NextCloud](https://nextcloud.com), [Duplicacy](https://duplicacy.com)
- Translate: [Apertium](https://www.apertium.org)
- Weather: [Geometric Weather](https://play.google.com/store/apps/details?id=wangdaye.com.geometricweather) (Android), [Open Weather Map](https://openweathermap.org) (Web)
- Workspace / Group Messaging: [Riot](https://riot.im) (Through [Matrix](https://matrix.org)), [Jami](https://jami.net)
- Video Platforms: [PeerTube](https://joinpeertube.org), [BitChute](https://www.bitchute.com) (Caution: Not moderated), [Invidio](https://invidio.us) (YouTube Proxy)


## Bonus #2 - Open Source Media Applications

Community-maintained media software can help you migrate away from providers that may not respect privacy. The following creative software packages are open source, cross-platform and free.

- Graphics: [GIMP](https://www.gimp.org), [Scribus](https://www.scribus.net), [SwatchBooker](http://www.selapa.net/swatchbooker), [InkScape](https://inkscape.org), [Krita](https://krita.org)
- Audio: [Audacity](https://www.audacityteam.org), [Mixxx](https://mixxx.org), [MusicBrainz](https://picard.musicbrainz.org), [Qtractor](https://qtractor.sourceforge.io), [SpotiFlyer](https://github.com/Shabinder/SpotiFlyer)
- Video: [Shortcut](https://www.shotcutapp.com), [OpenShot](https://www.openshot.org), [kdenlive](https://kdenlive.org)
- Video Transcoders: [HandBreak](https://handbrake.fr)
- Media Players: [VLC Player](https://www.videolan.org)
- Media Servers: [Kodi](https://kodi.tv), [Plex](https://www.plex.tv), [Subsonic](http://www.subsonic.org), [Emby](https://emby.media), [Gerbera](https://gerbera.io), [OpenELEC](https://openelec.tv), [OpenFlixr 2](https://www.openflixr.com), [OCMC](https://osmc.tv)
- 3D Rendering: [Blender](https://www.blender.org), [Wings3D](http://www.wings3d.com)
- Game Engines: [GoDot](https://godotengine.org), [SpringEngine](https://springrts.com), [Panda3D](https://www.panda3d.org), [Cocos](https://www.cocos.com/en/)
- Rendering Engines: [LuxCoreRender](https://luxcorerender.org), [AppleSeed](https://appleseedhq.net)


## Bonus #3 - Self-Hosted Services

- Analytics: [Matomo](https://matomo.org), [Privalytics](https://www.privalytics.io), [Plausible](https://plausible.io), [Fathom](https://github.com/usefathom/fathom), [GoatCounter](https://www.goatcounter.com), [ShyNet](https://github.com/milesmcc/shynet)
- Blogging: [Hexo](https://hexo.io), [Noddity](http://noddity.com), [Plume](https://joinplu.me), [Ghost](https://github.com/TryGhost/Ghost), [Write.as](https://github.com/writeas)
- Bookmarks: [Shiori](https://github.com/go-shiori/shiori), [Geek Marks](https://geekmarks.dmitryfrank.com), [Ymarks](https://bitbucket.org/ymarks), [xBrowserSync](https://www.xbrowsersync.org), [reminiscence](https://github.com/kanishka-linux/reminiscence), [unmark](https://github.com/cdevroe/unmark)
- Chat Networks: [Gotify](https://gotify.net), [GNU: net](https://gnunet.org), [Centrifugo](https://github.com/centrifugal/centrifugo), [Mumble](https://www.mumble.info), [Tox](https://tox.chat), [Matrix](https://matrix.org) + [Riot](https://riot.im), [Retroshare](https://retroshare.cc)
- CMS: [Strapi](https://strapi.io) (headless), [ApostropheCMS](https://github.com/apostrophecms/apostrophe), [Plone](https://github.com/plone), [Publify](https://publify.github.io), [Pico](http://picocms.org)
- Conference: [Jami](https://jami.net), [Jitsu](https://github.com/jitsi), [BigBlueButton](https://github.com/bigbluebutton/bigbluebutton) (Academic Institutions), [OpenMeetings](https://openmeetings.apache.org)
- Document Management: [Paperless](https://github.com/the-paperless-project/paperless)
- E-Commerce: [Qor](https://getqor.com), [Magento](https://github.com/magento), [Grandnode](https://github.com/grandnode/grandnode)
- Email Clients: [Rainloop](http://www.rainloop.net), [RoundCube](https://roundcube.net)
- Email Setup: [Mailu](https://mailu.io), [MailCow](https://mailcow.email), [Mail-in-a-Box](https://mailinabox.email)
- File Drop: [PsiTransfer](https://github.com/psi-4ward/psitransfer), [Up1](https://github.com/Upload/Up1), [FilePizza](https://file.pizza)
- File Explorer: [FileRun](https://filerun.com), [Pydio](https://pydio.com)
- Groupware: [SoGo](https://github.com/inverse-inc/sogo), [SuiteCRM](https://github.com/salesagility/SuiteCRM)
- News Letters: [LewsNetter](https://github.com/bborn/lewsnetter), [PHP List](https://www.phplist.com), [Dada Mail](https://github.com/justingit/dada-mail)
- Office Suites: [CryptPad](https://cryptpad.fr), [LibreOffice](https://www.libreoffice.org), [onlyoffice](https://github.com/ONLYOFFICE), [NextCloud](https://nextcloud.com)
- Paste Bins: [Snibox](https://snibox.github.io), [PrivateBin](https://github.com/PrivateBin/PrivateBin), [0bin](https://github.com/sametmax/0bin), [Stikked](https://github.com/claudehohl/Stikked)
- Photo Managers: [PhotoPrism](https://photoprism.app/)
- Search Engine: [Searx](https://searx.github.io/searx/)
- Social Networks: [Mastodon](https://mastodon.social), [Pixelfed](https://pixelfed.org), [diaspora](https://diasporafoundation.org)
- Ticketing: [Zammad](https://github.com/zammad/zammad), [osTicket](https://github.com/osTicket/osTicket), [Helpy](https://github.com/helpyio/helpy)
- URL Shortners: [Shlink](https://shlink.io), [Polr](https://polrproject.org), [Istu](https://github.com/ldidry/lstu), [Linkr](https://github.com/LINKIWI/linkr)
- WiKi/ Knowledge Sharing: [Gollum](https://github.com/gollum/gollum), [Outline](https://github.com/outline/outline), [Wiki JS](https://github.com/Requarks/wiki), [Gitit](https://github.com/jgm/gitit), [TidyWiki5](https://github.com/Jermolene/TiddlyWiki5), [Cowyo](https://github.com/schollz/cowyo)
- XMPP: Server: [ejabberd](https://github.com/processone/ejabberd), [MongooseIM](https://github.com/esl/MongooseIM), [OpenFire](https://github.com/igniterealtime/Openfire), [Prosody](https://prosody.im). Clients: [Converse](https://github.com/conversejs/converse.js), [JSXC](https://github.com/jsxc/jsxc), [Movim](https://github.com/movim/movim), [XMPP Web](https://github.com/nioc/xmpp-web)

## Bonus #4 - Self-Hosted Sysadmin

- Ad-Block (network-wide): [PiHole](https://pi-hole.net)
- Content Filter: [E2Guardian](http://e2guardian.org), [Squid Guard](http://www.squidguard.org)
- Cron Jobs: [HealthChecks](https://healthchecks.io)
- Dashboards: [Homer](https://github.com/bastienwirtz/homer), [Heimdall](https://heimdall.site), [SWMP](https://swmp.ml), [Uchiwa](https://uchiwa.io) (for Sensu), [Linux Dash](https://github.com/afaqurk/linux-dash)
- DNS: [CoreDNS](https://coredns.io), [KnotDNS](https://www.knot-dns.cz), [Bind 9](https://www.isc.org/bind), [PowerDNS](https://www.powerdns.com)
- Domain Control: [DomainMod](https://domainmod.org), [OctoDNS](https://github.com/github/octodns), [DNSControl](https://stackexchange.github.io/dnscontrol)
- Firewall: [IPFire](https://www.ipfire.org), [PFSense](https://www.pfsense.org), [OpenSense](https://opnsense.org), [ShoreWall](https://shorewall.org)
- Log Management: [GoAccess](https://goaccess.io)
- Monitoring: [Alerta](https://github.com/alerta/alerta), [Cabot](https://github.com/arachnys/cabot), [Cadvisor](https://github.com/google/cadvisor), [CheckMK](https://checkmk.com), [Linux Dash](https://github.com/afaqurk/linux-dash). [NetData](https://www.netdata.cloud), [PS Dash](https://github.com/Jahaja/psdash)
- Proxy: [ShaddowSocks](https://shadowsocks.org), [Privoxy](https://www.privoxy.org)
- Server Status: [Statup](https://github.com/hunterlong/statping), [BotoX / ServerStatus](https://github.com/BotoX/ServerStatus), [Mojeda / ServerStatus](https://github.com/mojeda/ServerStatus), [Statusfy](https://statusfy.co), [Cachet](https://cachethq.io)
- SSH Tools: [RTop](https://github.com/rapidloop/rtop) (sts stats), [Fiche](https://github.com/solusipse/fiche) (cli pastepin)
- Storage DB: [OpenTSBD](http://opentsdb.net), [KairosDB](https://github.com/kairosdb/kairosdb), [InfluxData](https://www.influxdata.com)
- VPN: [OpenVPN](https://community.openvpn.net), [Pritunl](https://pritunl.com)
- Web Servers: [NGINX](https://nginx.org), [Caddy](https://caddyserver.com), [Light TPD](https://www.lighttpd.net)


## Bonus #5 - Self-Hosted Development Tools

- API Management: [Kong](https://github.com/Kong/kong), [Krakend](https://github.com/devopsfaith/krakend), [tyk](https://github.com/TykTechnologies/tyk), [Hasura](https://hasura.io)
- Browser-based IDE: [Code Server](https://github.com/cdr/code-server) (VS Code), [Che](https://github.com/eclipse/che) (Eclipse), [ICEcoder](https://github.com/icecoder/ICEcoder), [ml-workspace](https://github.com/ml-tooling/ml-workspace) (for Data science and ML), [r-studio](https://github.com/rstudio/rstudio) (for R programming)
- Code Reviews: [Phabricator](https://github.com/phacility/phabricator). See also: Git Servers, most of which have CR features
- Containers: [Docker](https://github.com/docker), [LXC](https://github.com/lxc/lxc), [OpenVZ](https://github.com/OpenVZ)
- Continuous Integration: [Drone](https://github.com/drone/drone), [Concourse](https://github.com/concourse/concourse), [BuildBot](https://github.com/buildbot/buildbot), [Strider](https://github.com/Strider-CD/strider), [Jenkins](https://github.com/jenkinsci/jenkins)
- Deployment Automation: [Capustrano](https://github.com/capistrano/capistrano), [Fabric](https://github.com/fabric/fabric), [Mina](https://github.com/mina-deploy/mina), [Munki](https://github.com/munki/munki), [Rocketeer](https://github.com/rocketeers/rocketeer), [Sup](https://github.com/pressly/sup)
- Doc Generators: [FlatDoc](https://github.com/rstacruz/flatdoc), [Docsify](https://github.com/docsifyjs/docsify), [Sphinx](https://github.com/sphinx-doc/sphinx), [ReadTheDocs](https://github.com/readthedocs/readthedocs.org), [Docusarus](https://github.com/facebook/docusaurus), [mkdocs](https://github.com/mkdocs/mkdocs)
- Git Server: [GitBucket](https://gitbucket.github.io), [GitTea](https://gitea.io), [GitLab](https://gitlab.com/gitlab-org/gitlab-foss), [Gogs](https://gogs.io)
- Localization: [Weblate](https://github.com/WeblateOrg/weblate), [Translate/ Pootle](https://github.com/translate/pootle), [Accent](https://github.com/mirego/accent)
- Serverless: [OpenFaas](https://www.openfaas.com), [IronFunctions](https://github.com/iron-io/functions), [LocalStack](https://github.com/localstack/localstack), [fx](https://github.com/metrue/fx)
- Static Site Gen: See [StaticGen.com](https://www.staticgen.com)
- UI Testing: [Selenoid](https://github.com/aerokube/selenoid), [Zalenium](https://github.com/zalando/zalenium), [Selenium](https://github.com/SeleniumHQ/selenium)
- More Tools:
	- [Request Bin](https://github.com/Runscope/requestbin) - Inspect HTTP requests and Debug webhooks
	- [Regexr](https://github.com/gskinner/regexr) - Web tool for for creating, testing, and learning about Regular Expressions
	- [JS Bin](https://github.com/jsbin/jsbin) - Collaborative JavaScript Debugging App, create, test, run and send web code snippets
	- [Koding](https://github.com/koding/koding) - A development platform to orchestrates your project-specific dev environment
	- [Judge0](https://github.com/judge0) - A web compiler accessed through either an API of web-IDE, for executing trusted or untrusted code
	- [SourceGraph](https://github.com/sourcegraph/sourcegraph) - Self-hosted universal code search and navigation engine


## Bonus #6 - Security Testing Tools

This list is intended to aid you in auditing the security of your own systems, and help detect and eliminate vulnerabilities. It is intended for advanced users and sysadmins. For penetration testing, see [enaqx/awesome-pentest](https://github.com/enaqx/awesome-pentest) GitHub list instead

- [Amass] - In-depth Attack Surface Mapping and Asset Discovery, to help you identify issues and secure your network
- [CloudFail] - Ensure there are no misconfigured DNS and old database records, accessible by bypassing CloudFlare network
- [CrackMapExec] - A CLI tool for pen testing all areas of your local and remote networks, to ensure their integrity
- [DNSdumpster] - A domain research tool that can discover hosts related to a domain. It can be used to test and ensure there are no visible hosts that a hacker could exploit
- [DNSTracer] - Scan your domain, to show which records are publicly visible and need to be obfuscated
- [dnstwist] - Domain name permutation engine for detecting typo squatting, phishing and corporate espionage, to protect those on your network
- [GRR] - incident response framework focused on remote live forensics
- [Impacket] - A collection of Python classes for working with network protocols, focused on providing low-level programmatic access to the packets and for the protocol implementation themselves
- [Kali Linux] - A Debian-based distro for security testing, bundled with 1000's of powerful packages and scripts. Saves a lot of time configuring sys-admin tools and drivers
- [Lynis] - A security tool that performs an extensive health scan of your systems to support system hardening and compliance testing
- [Masscan] - TCP port scanner, that checks packets asynchronously, configure it to check only your IP ranges and it completes in milliseconds
- [Metasploit] - Popular and powerful penetration testing framework, for exploitation and vulnerability validation - bundled with a full suite of tools, it makes it easy to divide your penetration testing workflow into manageable sections. Very useful for testing your entire network E2E
- [Moloch] - Full packet capture, indexing, and database system. The elastic search backend makes searching through pcaps fast, and the frontend displays captured data clearly with good support for protocol decoding
- [Nikto2] - Well-established web server testing tool, useful for firing at your web server to find known vulnerable scripts, configuration mistakes and related security problems
- [Nmap] - Powerful utility for network discovery and security auditing. Useful for your network inventory, managing service upgrade schedules, and monitoring host or service uptime
- [OpenAudit] - An application to tell you exactly what is on your network, how it is configured and when it changes
- [OpenVAS] - Fully-featured security vulnerability management system, with web-based dashboards. Useful for fast and easy scans of your network
- [OSQuery] - SQL powered operating system instrumentation, monitoring, and analytics. Very performant cross-platform tool, useful for monitoring a host for changes and providing endpoint visibility
- [OSSEC HIDS] - A host based intrusion detection system that is easy to setup and configure, which performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting and active response
- [Otseca] - Search and dump your system configuration + generate HTML reports
- [RouterSploit]: An exploitation framework for checking the security of local embedded devices, to ensure they are safe
- [Security Onion] - Linux distro for intrusion detection, enterprise security monitoring, and log management. It includes a suite of security testing tools. Useful for collecting, storing and managing a variety of system data, for use on your networks
- [Snort] - Intrusion detection system aimed at real time traffic analysis and packet logging tool
- [SPARTA] - GUI tool that makes pen testing your network infrastructure easier
- [Wireshark] - Popular, powerful feature-rich network protocol analyser. Lets you analyse everything that is going on in your network in great detail
- [Zeek] - Powerful intrusion detection system and network security monitoring, that (rather than focusing on signatures) decodes protocols and looks for anomalies within the traffic


## Bonus #7 - Raspberry Pi/ IoT Security Software

- [OnionPi](https://github.com/breadtk/onion_pi) - Create an Anonymizing Tor Proxy using a Raspberry Pi
- [CIRCLean](https://www.circl.lu/projects/CIRCLean) - A Pi-based USB Sanitizer, plug an untrusted USB in, and get clean files out
- [Pi Hole](https://pi-hole.net) - A network-wide ad-block, that improves network performance as well as privacy
- [Project Alias](https://github.com/bjoernkarmann/project_alias) - Gives you full-control, and better privacy of your Google Home or Alexa
- [Raspiblitz](https://github.com/rootzoll/raspiblitz) - Build your own Bitcoin & Lightning Node on a Pi, see also [Trezor](https://github.com/trezor/trezor-firmware) wallet
- [PiVPN](https://www.pivpn.io) - Simple low-cost yet secure VPN, for the Raspberry Pi (or set up manually, as outlined in [this guide](https://pimylifeup.com/raspberry-pi-vpn-server/))
- [DeauthDetector](https://github.com/spacehuhn/DeauthDetector) - Detect deauthentication frames using an ESP8266, useful to be aware of ongoing wireless attacks
- [IPFire](https://www.ipfire.org) - Hardened open source firewall to prevent common attacks on your network. Capable of running on a Pi
- [SquidGuard](http://www.squidguard.org) - Fast and free URL redirector, which can work well as a home caching server
- [E2guardian](http://e2guardian.org) - Comprehensive content filtering, with powerful configuration options


USB-based projects include:
- [DBAN](https://dban.org) - Bootable hard drive erasers for destroying data
- [Syncthing](https://syncthing.net) - Create automated backups to an external medium
- [KeePass Portable](https://keepass.info/download.html) - Portable password manager. For hardware-encrypted password manager, see [HardPass 2.0](https://hackaday.io/project/21227-hardpass02-hardware-passwd-manager-w-smart-card)
- [VeraCrypt](https://www.veracrypt.fr) - Full drive encryption for USB devices

See more [hardware-based security solutions](https://github.com/Lissy93/personal-security-checklist/blob/master/6_Privacy_and-Security_Gadgets.md)


## More Awesome Software Lists

This list was focused on privacy-respecting software. Below are other awesome lists, maintained by the community of open source software, categorised by operating system.

- Windows: [awesome-windows-apps](https://github.com/Awesome-Windows/Awesome) by 'many'
- MacOS: [awesome-macOS-apps](https://github.com/iCHAIT/awesome-macOS) by @iCHAIT
- Linux: [awesome-linux-software](https://github.com/luong-komorebi/Awesome-Linux-Software) by @luong-komorebi
- iOS: [open-source-ios-apps](https://github.com/dkhamsing/open-source-ios-apps) by @dkhamsing
- Android: [open-source-android-apps](https://github.com/pcqpcq/open-source-android-apps) by @pcqpcq
- Server: [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) by 'many'
- [**More GitHub Awesome Lists →**](https://github.com/Lissy93/personal-security-checklist/blob/master/4_Privacy_And_Security_Links.md#more-awesome-github-lists)

## News & Updates

A custom Reddit feed covering news and updates for privacy-respecting apps, software & services can be found [here](https://www.reddit.com/user/lissy93/m/software_projects/)

## Final Notes

### Conclusion

Many corporations put profit before people, collecting data and exploiting privacy. They claim to be secure but without being open source it can't be verified, until there's been a breach and it's too late. Switching to privacy-respecting open source software will drastically help improving your security, privacy and anonymity online.

However, that's not all you need to do. It is also important to : use strong and unique passwords, 2-factor authentication,
adopt good networking practices and be mindful of data that are collected when browsing the web. You can see the full
**[personal security checklist](https://github.com/Lissy93/personal-security-checklist/blob/master/README.md)** for more tips to stay safe. 


### Important Considerations

**Compartmentalise, Update and Be Ready** <br>
No piece of software is truly secure or private.  Further to this, software can only as secure as the system it is running on. Vulnerabilities are being discovered and patched all the time, so you much keep your system up-to-date. Breaches occur regularly, so compartmentalise your data to minimise damage. It's not just about choosing secure software, you must also follow good security practices.

**Attack Surface** <br>
It is a good idea to keep your trusted software base small, to reduce potential attack surface. At the same time trusting a single application for too many tasks or too much personal data could be a weakness in your system. So you will need to judge the situation according to your threat model, and carefully plan which software and applications you trust with each segment of your data.

**Convenience Vs Security** <br>
There is often a trade-off between convenience and security. Construct a threat model, and choose a balance that is right for you. In a similar way in some situations there is privacy and security conflict (e.g. Find My Phone is great for security, but terrible for privacy, and anonymous payments may be good for privacy but less secure than insured fiat currency). Again it is about assessing your situation, understanding the risks and making an informed decision.

**Hosted Vs Self-Hosted Considerations** <br>
When using a hosted or managed application that is open-source software - there is often no easy way to tell if the version running is the same as that of the published source code (even published signatures can be faked). There is always the possibility that additional backdoors may have been knowingly or unknowingly implemented in the running instance. One way round this is to self-host software yourself. When self-hosting you will then know for sure which code is running, however you will also be responsible for the managing security of the server, and so may not be recommended for beginners.

**Open Source Software Considerations** <br>
Open source software has long had a reputation of being more secure than its closed source counterparts. Since bugs are raised transparently, fixed quickly, the code can be checked by experts in the community and there is usually little or no data collection or analytics. 
That being said, there is no piece of software that it totally bug free, and hence never truly secure or private. Being open source, is in no way a guarantee that something is safe. There is no shortage of poorly-written, obsolete or sometimes harmful open source projects on the internet. Some open source apps, or a dependency bundled within it are just plain malicious (such as, that time [Colourama was found in the PyPI Repository](https://hackaday.com/2018/10/31/when-good-software-goes-bad-malware-in-open-source/))

**Proprietary Software Considerations** <br>
When using a hosted or proprietary solution - always check the privacy policy, research the reputation of the organisation, and be weary about which data you trust them with. It may be best to choose open source software for security-critical situations, where possible.

**Maintenance** <br>
When selecting a new application, ensure it is still being regularly maintained, as this will allow for recently discovered security issues to be addressed. Software in an alpha or beta phase, may be buggy and lacking in features, but  more importantly - it could have critical vulnerabilities open to exploit. Similarly, applications that are no longer being actively maintained may pose a security risk, due to lack of patching. When using a forked application, or software that is based on an upstream code base, be aware that it may receive security-critical patches and updates at a slightly later date than the original application. 

**This List: Disclaimer** <br>
This list contains packages that range from entry-level to advanced, a lot of the software here will not be appropriate for all audiences. It is in no way a definitive list of secure applications, and aims only to be a guide, a collection of software and services that myself and other contributors have used, and would recommend. There will always be new vulnerabilities discovered or introduced, bugs and security-critical glitches, malicious actors and poorly configured systems. It is up to you to do your research, draw up a threat model, and decide where and how your data are managed.

If you find something on this list that should no longer be deemed secure or private/ or should have a warning note attached, please raise an issue. In the same way if you know of something that is missing, or would like to make an edit, then pull requests are welcome, and are much appreciated!

### Contributors

This is a community-maintained project, which wouldn't have been possible without help from [all these wonderful people](https://github.com/Lissy93/awesome-privacy/blob/main/.github/CREDITS.md).

Top Contributors:

<a title="Click to view all contributors" href="https://github.com/Lissy93/awesome-privacy/blob/main/.github/CREDITS.md">
  <img src="https://github.com/Lissy93/awesome-privacy/raw/main/.github/assets/CONTRIBUTORS.svg" alt="Top Contributors" width="600" />
</a>

### Contributing

*Thanks for visiting! If you have suggestions, then you [open an issue](https://github.com/Lissy93/awesome-privacy/issues/new/choose), or [submit a PR](https://github.com/Lissy93/awesome-privacy/pull/new/main), see: [`CONTRIBUTING.md`](/.github/CONTRIBUTING.md). Contributions are welcome, and always much appreciated* ☺️


### License 

[![Attribution 4.0 International](https://licensebuttons.net/l/by/3.0/88x31.png)](https://github.com/Lissy93/awesome-privacy/blob/main/LICENSE)

*Licensed under [Creative Commons, CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), © [Alicia Sykes](https://aliciasykes.com) 2022*


### Thank you

Thank you for checking out this project - I hope you found it somewhat useful 😊

This list was initially compiled by Alicia Sykes / [: octocat: @Lissy93](https://github.com/Lissy93), with a lot of help from the community.

Follow me on GitHub for updates and other projects.

If you found this project helpful, consider dropping us a star, and sharing with your network.



[//]: # (BROWSER EXTENSION LINKS)
[privacy-badger-chrome]: https://chrome.google.com/webstore/detail/privacy-badger/pkehgijcmpdhfbdbbnkijodmdjhbjlgp
[privacy-badger-firefox]: https://addons.mozilla.org/en-GB/firefox/addon/privacy-badger17/
[https-everywhere-chrome]: https://chrome.google.com/webstore/detail/https-everywhere/gcbommkclmclpchllfjekcdonpmejbdp?hl=en
[https-everywhere-firefox]: https://addons.mozilla.org/en-GB/firefox/addon/https-everywhere/
[ublock-chrome]: https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=en-GB
[ublock-firefox]: https://addons.mozilla.org/en-GB/firefox/addon/ublock-origin/
[script-safe-chrome]: https://chrome.google.com/webstore/detail/scriptsafe/oiigbmnaadbkfbmpbfijlflahbdbdgdf?hl=en-GB
[script-safe-firefox]: https://addons.mozilla.org/en-GB/firefox/addon/script-safe/
[web-rtc-chrome]: https://chrome.google.com/webstore/detail/webrtc-leak-prevent/eiadekoaikejlgdbkbdfeijglgfdalml?hl=en-GB
[decentraleyes-chrome]: https://chrome.google.com/webstore/detail/decentraleyes/ldpochfccmkkmhdbclfhpagapcfdljkj
[decentraleyes-firefox]: https://addons.mozilla.org/en-US/firefox/addon/decentraleyes
[decentraleyes-pale-moon]: https://addons.palemoon.org/addon/decentraleyes
[decentraleyes-opera]: https://addons.opera.com/en/extensions/details/decentraleyes
[decentraleyes-source]: https://git.synz.io/Synzvato/decentraleyes
[vanilla-cookie-chrome]: https://chrome.google.com/webstore/detail/vanilla-cookie-manager/gieohaicffldbmiilohhggbidhephnjj?hl=en-GB
[privacy-essentials-chrome]: https://chrome.google.com/webstore/detail/duckduckgo-privacy-essent/bkdgflcldnnnapblkhphbgpggdiikppg?hl=en-GB
[privacy-essentials-firefox]: https://addons.mozilla.org/en-GB/firefox/addon/duckduckgo-for-firefox/
[self-destructing-cookies-chrome]: https://chrome.google.com/webstore/detail/self-destructing-cookies/igdpjhaninpfanncfifdoogibpdidddf
[self-destructing-cookies-firefox]: https://addons.mozilla.org/en-US/firefox/addon/self-destructing-cookies-webex/
[self-destructing-cookies-opera]: https://addons.opera.com/en/extensions/details/self-destructing-cookies/
[self-destructing-cookies-source]: https://github.com/joue-quroi/self-destructing-cookies
[lightbeam-firefox]: https://addons.mozilla.org/en-US/firefox/addon/lightbeam-3-0/
[lightbeam-source]: https://github.com/mozilla/lightbeam-we
[tmn-chrome]: https://chrome.google.com/webstore/detail/trackmenot/cgllkjmdafllcidaehjejjhpfkmanmka
[tmn-firefox]: https://addons.mozilla.org/en-US/firefox/addon/trackmenot/
[tmn-whitepaper]: http://trackmenot.io/resources/trackmenot2009.pdf
[tmn-source]: https://github.com/vtoubiana/TrackMeNot
[amiunique-chrome]: https://chrome.google.com/webstore/detail/amiunique/pigjfndpomdldkmoaiiigpbncemhjeca
[amiunique-firefox]: https://addons.mozilla.org/en-US/firefox/addon/amiunique

[//]: # (ANDROID APP LINKS)
[NetGuard]: https://play.google.com/store/apps/details?id=eu.faircode.netguard
[Island]: https://play.google.com/store/apps/details?id=com.oasisfeng.island
[Orbot]: https://play.google.com/store/apps/details?id=org.torproject.android
[Bouncer]: https://play.google.com/store/apps/details?id=com.samruston.permission
[Crypto]: https://play.google.com/store/apps/details?id=com.kokoschka.michael.crypto
[Cryptomator]: https://play.google.com/store/apps/details?id=org.cryptomator
[Daedalus]: https://play.google.com/store/apps/details?id=org.itxtech.daedalus
[Brevent]: https://play.google.com/store/apps/details?id=me.piebridge.brevent
[SuperFreezZ]: https://f-droid.org/en/packages/superfreeze.tool.android
[Secure Task]: https://play.google.com/store/apps/details?id=com.balda.securetask
[Tor Browser]: https://play.google.com/store/apps/details?id=org.torproject.torbrowser
[PortDroid]: https://play.google.com/store/apps/details?id=com.stealthcopter.portdroid
[Packet Capture]: https://play.google.com/store/apps/details?id=app.greyshirts.sslcapture
[SysLog]: https://play.google.com/store/apps/details?id=com.tortel.syslog
[Dexplorer]: https://play.google.com/store/apps/details?id=com.dexplorer
[Check and Test]: https://play.google.com/store/apps/details?id=com.inpocketsoftware.andTest
[Tasker]: https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm
[Haven]: https://play.google.com/store/apps/details?id=org.havenapp.main
[NetGaurd]: https://www.netguard.me/
[Exodus]: https://exodus-privacy.eu.org/en/page/what/#android-app
[XUMI Security]: https://xumi.ca/xumi-security/
[Fing App]: https://www.fing.com/products/fing-app
[FlutterHole]: https://github.com/sterrenburg/flutterhole
[1.1.1.1]: https://1.1.1.1/
[The Guardian Project]: https://play.google.com/store/apps/dev?id=6502754515281796553
[The Tor Project]: https://play.google.com/store/apps/developer?id=The+Tor+Project
[Oasis Feng]: https://play.google.com/store/apps/dev?id=7664242523989527886
[Marcel Bokhorst]: https://play.google.com/store/apps/dev?id=8420080860664580239
[SECUSO Research Group]: https://play.google.com/store/apps/developer?id=SECUSO+Research+Group&hl=en_US
[Simple Mobile Tools]: https://play.google.com/store/apps/dev?id=9070296388022589266

[//]: # (SECURITY TESTING TOOLS)
[Amass]: https://github.com/OWASP/Amass
[CloudFail]: https://github.com/m0rtem/CloudFail
[CrackMapExec]: https://github.com/byt3bl33d3r/CrackMapExec
[DNSdumpster]: https://dnsdumpster.com/
[DNSTracer]: http://www.mavetju.org/unix/dnstracer.php
[dnstwist]: https://github.com/elceef/dnstwist
[GRR]: https://github.com/google/grr
[Impacket]: https://github.com/SecureAuthCorp/impacket
[Kali Linux]: https://www.kali.org
[Kali Linux_source]: https://gitlab.com/kalilinux
[Lynis]: https://cisofy.com/lynis
[Masscan]: https://github.com/robertdavidgraham/masscan
[Metasploit]: https://www.metasploit.com
[Metasploit_source]: https://github.com/rapid7/metasploit-framework
[Moloch]: https://molo.ch
[Moloch_source]: https://github.com/aol/moloch
[Nikto2]: https://cirt.net/nikto2
[Nikto2_source]: https://github.com/sullo/nikto
[Nmap]: https://nmap.org
[Nmap_source]: https://github.com/nmap/nmap
[OpenAudit]: https://www.open-audit.org
[OpenVAS]: https://openvas.org
[OpenVAS_source]: https://github.com/greenbone/openvas
[OSQuery]: https://osquery.io
[OSQuery_source]: https://github.com/osquery/osquery
[OSSEC HIDS]: https://www.ossec.net
[OSSEC HIDS_source]: https://github.com/ossec/ossec-hids
[Otseca]: https://github.com/trimstray/otseca
[RouterSploit]: https://github.com/threat9/routersploit
[Security Onion]: https://securityonion.net
[Security Onion_source]: https://github.com/Security-Onion-Solutions/security-onion
[Snort]: https://snort.org
[SPARTA]: https://sparta.secforce.com
[SPARTA_source]: https://github.com/SECFORCE/sparta
[Wireshark]: https://www.wireshark.org
[Wireshark_source]: https://code.wireshark.org/review/#/admin/projects/wireshark
[Zeek]: https://zeek.org
[Zeek_source]: https://github.com/zeek/zeek
