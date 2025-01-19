%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id https-everywhere-eff@eff.org
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

%global seamonkey_app_id \{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a}
%global seamonkey_inst_dir %{moz_extensions}/%{seamonkey_app_id}

Name:           mozilla-https-everywhere
Version:        2022.5.11
Release:        8%{?dist}
Summary:        HTTPS enforcement extension for Mozilla Firefox

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://eff.org/https-everywhere
# A git repo is available at https://github.com/EFForg/https-everywhere
Source0:        https://www.eff.org/files/https-everywhere-%{version}-eff.xpi
Source1:        mozilla-https-everywhere.metainfo.xml
Source2:        https://www.eff.org/files/https-everywhere-5.2.21-eff.xpi



Requires:       mozilla-filesystem
# GNOME Software Center not present on EL < 7
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires:  libappstream-glib
%endif
BuildArch:      noarch


%description
HTTPS Everywhere is a Firefox extension produced as a collaboration between
The Tor Project and the Electronic Frontier Foundation. It encrypts your
communications with a number of major websites.

Many sites on the web offer some limited support for encryption over HTTPS,
but make it difficult to use. For instance, they may default to unencrypted
HTTP, or fill encrypted pages with links that go back to the unencrypted site.

The HTTPS Everywhere extension fixes these problems by rewriting all requests
to these sites to HTTPS.

The Fedora RPM package includes the legacy XUL version, no longer updated,
for SeaMonkey users.

%prep
%setup -q -c

%build


%install
# Install WebExtensions (supported) version to Firefox directory
install -Dpm644 %{SOURCE0} %{buildroot}%{firefox_inst_dir}/%{src_ext_id}.xpi

# Install XUL version to SeaMonkey directory
mkdir -p %{buildroot}%{seamonkey_inst_dir}
install -Dpm644 %{SOURCE2} %{buildroot}%{seamonkey_inst_dir}/%{src_ext_id}.xpi

# install MetaInfo file for firefox
%if 0%{?fedora} || 0%{?rhel} >= 7
appstream-util validate-relax %{SOURCE1}
DESTDIR=%{buildroot} appstream-util install %{SOURCE1}
%endif

%files
%{firefox_inst_dir}/%{src_ext_id}.xpi
%{seamonkey_inst_dir}/%{src_ext_id}.xpi
# GNOME Software Center metadata
%if 0%{?fedora} || 0%{?rhel} >= 7
%{_datadir}/appdata/%{name}.metainfo.xml
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2022.5.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2022.5.11-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022.5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 2022.5.11-1
- Update to 2022.5.11 rhbz#1869604

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.8.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.8.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Russell Golden <niveusluna@fedoraproject.org> - 2020.8.13-1
- Fix port based whitelisting issue #19291
- Update documentation
- Update dependencies (NPM and Chromedriver)
- Minor code fixes in JS

* Fri Jul 31 2020 Russell Golden <niveusluna@fedoraproject.org> - 2020.5.20-1
- EASE HTTP Once CSS fix
- Allow users to whitelist hosts from the option page
- EASE mode fixes for locale issue
- Fetch Test Prep, TLS 1.2 update
- Fetch Test Prep, Updated check rules script
- Fix options page appearance on Firefox when dark mode is on
- Dark mode adjustments
- Reverting Onboarding page for the time being
- Patch for whitelisting rules and EASE mode issue
- Double rule load patch in update channels
- Fix minor JS and UX issues

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Russell Golden <niveusluna@niveusluna.org> - 2019.11.7-1
- EASE HTTP Once Exception
- Add Private network IPs to exclusion for HTTPSE
- Revert icons back to previous state
- Optimizations to url handling and hsts prune

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.6.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Russell Golden <niveusluna@fedoraproject.org> - 2019.6.27-2
- Whoops. Fix date on previous changelog entry.

* Thu Jul 11 2019 Russell Golden <niveusluna@fedoraproject.org> - 2019.6.27-1
- Making stylistic changes for mobile friendliness in Fennec
- Inclusion and use of the lib-wasm submodule, lowering memory overhead
- Refactor secure cookie logic
- Code cleanup
- Fix bug where link HTML is replaced in cancel page, instead of text
- Bundled ruleset updates

* Tue May 21 2019 Russell Golden <niveusluna@fedoraproject.org> - 2019.5.13-1
- UI and functionality patches for stable rules
- Translations string fixes
- Minor npm updates for HSTS pruning

* Mon May 06 2019 Russell Golden <niveusluna@fedoraproject.org> - 2019.5.6.1-1
- UI changes in extension menu (#17854)
- EASE interstitial UI tweaks (#17347)
- Remove support for wildcard in the middle (#12319)
- Update default timestamp for deterministic builds (#17623)
- Refactor and enhance trivialize-cookie-rules.js (#17438)
- Run HSTS-prune and fix impacted rulesets (#17338)
- Update HSTS preload max age (#17564)
- Fix DeprecationWarning in HTTPS Everywhere Checker (#17596 )
- Fix Chromium local store exception (#17557)
- Remove middle wildcard support in rules.js (#17715)
- UI tweaks for spacing and font sizes
- Fix reload bug
- Patch for offline release channel

* Fri Apr 26 2019 Russell Golden <niveusluna@fedoraproject.org> - 2019.1.31-1
- Change "Block all unencrypted requests" language to "Encrypt all sites eligible"
- EASE mode patches for interstitial page and reload to trigger for EASE mode
- ES Lint clean up
- Disable test for Chrome (will work in patch while disabled)
 -- (packager note: Included because both versions use the same codebase)
- Deprecate I.P.s in rulesets (Special case for DNS I.P.s)
- Amend check_rules.py fetch test to disable rules only if all rules are problematic,
 -- and comment rules out if other rules are functional in the set
- HSTS Prune and updates
- Bundled ruleset updates

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Russell Golden <niveusluna@niveusluna.org> - 2018.10.31-1
- Add additional error code for 'Block all unencrypted requests' interstitial
 -- page.
- Fix race condition when adding update channel
- Add UX to remove user rules in options page
- Bundled ruleset updates

* Mon Oct 01 2018 Russell Golden <niveusluna@niveusluna.org> - 2018.9.19-1
2018.9.19
- Ensure the 'Block all unencrypted requests' interstitial page catches more
  HTTPS misconfigurations (#16418)
- Allow users to disable HTTPS Everywhere on specific sites. Add additional
  UX controls in the options page for this. (#10041)
- Adding 'scope' to update channels, which defines regex limiting the URLs
  an update channel is allowed to operate on (#16430)
- Adding a warning to pages which 'Block all unencrypted requests' is unable
  to upgrade
- Adding a UX that enables users to add, delete, and edit update channels
- Reduces memory overhead by optimizing exclusion regex
- Block insecure FTP connections when 'Block all unencrypted requests'
  is checked. This triggers a permissions dialogue in Firefox 57+, see
  https://github.com/EFForg/https-everywhere/issues/16377#issuecomment-415492846
  for more info.
- Bundled ruleset updates

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Russell Golden <niveusluna@niveusluna.org> - 2018.6.21-1
- Fix: websites with a hostname of "." cause an endless loop
- Batched ruleset updates

* Sun Jun 17 2018 Russell Golden <niveusluna@niveusluna.org> - 2018.6.13-1
- Ruleset updates

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Russell Golden <niveusluna@niveusluna.org> - 2018.1.29-1
- They still aren't specifying what the ruleset updates are

* Sat Jan 13 2018 Russell Golden <niveusluna@niveusluna.org> - 2018.1.11-1
- More ruleset updates

* Wed Jan 03 2018 Russell Golden <niveusluna@niveusluna.org> - 2017.12.6-2
- Go back to WebExtensions for RHEL. Stupid me didn't test it.

* Mon Jan 01 2018 Russell Golden <niveusluna@niveusluna.org> - 2017.12.6-1
- Edit summary and description to reflect lack of SeaMonkey support
- Fix EL compatibility; RHEL isn't on Firefox 57 yet

* Wed Nov 22 2017 Russell Golden <niveusluna@niveusluna.org> - 2017.11.21-1
- XUL version will now be included for SeaMonkey users.
-- NO UPDATES FOR XUL VERSION; YOU MUST FIX THE RULES YOURSELF
- Ruleset updates

* Fri Nov 03 2017 Russell Golden <niveusluna@niveusluna.org> - 2017.10.30-1
- Introduce migrations, migrate settings from localStorage to storage api
- Firefox: full WebExtensions version

* Tue Sep 19 2017 Russell Golden <niveusluna@niveusluna.org> - 2017.9.12-1
- Decrease memory footprint by using JSON in default.rulesets
- Markup changes
- Ruleset updates

* Mon Sep 04 2017 Russell Golden <niveusluna@niveusluna.org> - 2017.8.31-1
- Comment out SeaMonkey stuff
- Add counter badge to indicate how many rulesets are active
- Use Map instead of Object for targets (improves lookups)
- Fix race condition with persistent storage
- Ruleset updates

* Sat Aug 26 2017 Russell Golden <niveusluna@niveusluna.org> - 2017.8.19-1
- Fix wildcard matching
- Remove usage of HTML string assignment
- Ruleset updates

* Thu Aug 17 2017 Russell Golden <niveusluna@niveusluna.org> - 2017.8.17-1
- Fix localStorage reference for users with cookies disabled

* Wed Aug 16 2017 Russell Golden <niveusluna@niveusluna.org> - 2017.8.15-1
- No longer SeaMonkey compatible; Fedora 26 and 25 will no longer receive updates
- Incorporating numerous fixes for WebExtensions to work within Firefox
- Firefox: Creating Embedded WebExtension wrapper to migrate legacy settings
- Removing legacy XPCOM codebase, unifying Firefox and Chrome codebase
- Ruleset updates

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.21-1
- Ruleset updates

* Thu Jul 06 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.20-1
- Ruleset updates

* Thu Jun 22 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.19-1
- Ruleset updates

* Tue Jun 06 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.18-1
- FF: Suppress request to check.torproject.org if SSL Observatory is disabled
- Yet more ruleset updates that aren't specified

* Wed May 10 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.16-2
- ACTUALLY fix changelog percentage signs once and for all

* Wed May 10 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.16-1
- Even more unspecific rule updates.
- Fix unescaped percentage sign in changelog once and for all

* Thu Apr 20 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.15-1
- More unspecified ruleset updates.

* Thu Apr 06 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.14-1
- Yet more ruleset updates
- Fix changelog entry from way back to escape the percentage signs

* Mon Mar 27 2017 Russell Golden <niveusluna@niveusluna.org> - 5.2.13-1
- Ruleset updates

* Mon Mar 13 2017 Russell Golden <niveusluna@niveusuna.org> - 5.2.12-1
- Excepting loopback hostnames from 'HTTPS Nowhere' functionality
- Ruleset updates

* Tue Feb 14 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.2.11-1
- update to 5.2.11
- update git repo link in comment

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Dominik Mierzejewski <rpm@greysector.net> - 5.2.7-2
- EL7 has gnome-software, so ship appstream data there, too

* Sat Nov 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 5.2.7-1
- update to 5.2.7
- validate appstream data
- drop patch to preserve signature validation
- drop obsolete parts

* Fri May 20 2016 Russell Golden <niveusluna@niveusluna.org> - 5.1.9-1
- Various fixes and additions

* Thu Feb 25 2016 Russell Golden <niveusluna@niveusluna.org> - 5.1.4-1
- Fix regressions introduced in 5.1.3
- Performance & memory usage improvements for Chrome
- Introduce temporary disable option on Chrome
- Bugfix: make custom rules disableable
- Improvements to tests
- Switch to using JSON to store rulesets

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 05 2015 Russell Golden <niveusluna@niveusluna.org> - 5.1.1-1
- Ruleset fixes
- Remove the AMO signature, see if it works then
- Fix the "not appearing" problem

* Mon Aug 24 2015 Russell Golden <niveusluna@niveusluna.org> - 5.1.0-1
- Ruleset fixes
- AMO signature

* Mon Aug 10 2015 Russell Golden <niveusluna@niveusluna.org> - 5.0.7-1
- Update to version 5
- So sorry I'm so late. There are a great many changes, so I won't bother
-- to list them.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 01 2015 Russell Golden <niveusluna@niveusluna.org> - 4.0.3-1
- Ruleset updates.
- Update SSL Observatory code to match Firefox API changes in hashing.
- Bring code in line with guidelines for addons.mozilla.org.

* Thu Oct 16 2014 Russell Golden <niveusluna@niveusluna.org> - 4.0.2-1
- Disable SSL 3 to Prevent POODLE attack:
 -- https://github.com/EFForg/https-everywhere/pull/674
- NEW: HTTP Nowhere mode. Block all plaintext http
- Updates to Yahoo APIs, Fastly, VMWare, Netflix, Maashable, LinkedIn,
  Gitorious, Mozilla, msecnd, Hotmail, Live, Eniro, Steam, Phoronix,
  net-security.org, Flickr, Craigslist, Apache.org, Joomla.org, Samsung,
  Google IMages, Expedia, Akamai, Trip Advisor, Ikea, CEll, Leo.org, Facebook,
  F-Secure, Dropbox, Courage Campaign, Box, Atlassian, Internet Archvie,
  localbitcoins.com, SOny, SciVerse, Web.com, Urgan Dictionary, Pornhub,
  Fool.com, ClickBank, MGID, Which?, Microsoft, Barnes and Noble, Royal
  Institute of GB, Wall Street Journal

* Sat Sep 13 2014 Russell Golden <niveusluna@niveusluna.org> - 4.0.1-1
- Significant new coverage: Reddit, Quora
- Fixes include:
 -- Frontier Networks, Hotmail / Live, Microsoft, Mozilla, Ohio State, Rackspace, SJ.se, Timbo.se
 -- https://github.com/EFForg/https-everywhere/issues/310
 -- https://github.com/EFForg/https-everywhere/issues/500
 -- https://trac.torproject.org/projects/tor/ticket/11402
 -- https://trac.torproject.org/projects/tor/ticket/11418
 -- https://trac.torproject.org/projects/tor/ticket/12583
 -- https://trac.torproject.org/projects/tor/ticket/12104
 -- https://trac.torproject.org/projects/tor/ticket/9466
 -- https://github.com/EFForg/https-everywhere/issues/144
- Enhancements to MCB detection and subsequent ruleset fixes
 -- https://github.com/EFForg/https-everywhere/issues/529

* Thu Sep 04 2014 Russell Golden <niveusluna@niveusluna.org> - 4.0.0-1
- Ruleset fixes to wikimedia, stanford-university, joyent, and gaytorrents.
- Merge Android Firefox branch, so Android now has the same release cycle
 -- as the stable HTTPS Everywhere branch for Firefox.
- Remove old unused ContentPolicy code.
- FEDORA/RHEL SPECIFIC - Place version conditionals for GNOME Software
 -- Center metadata in spec file.

* Tue Aug 19 2014 Richard Hughes <richard@hughsie.com> - 3.5.3-2
- Add a MetaInfo file for GNOME Software and Apper.

* Wed Jun 25 2014 Russell Golden <niveusluna@niveusluna.org> - 3.5.3-1
- Now works when installed globally!
- Various ruleset fixes, including PCWorld.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Russell Golden <niveusluna@niveusluna.org> - 3.5.1-1
- Revert https://github.com/EFForg/https-everywhere/pull/134 due to YouTube
 -- breakage.
- Re-enable ability to see all rulesets in enable/disable dialog.
- Added more Debian coverage.
- Fixes to Doubleclick, Guardian, Heroku, Home Depot, HypeMachine, IMDB,
 -- Justin.tv, Kikatek, Mozilla, MyFitnessPal, Pinterest, XKCD, Reuters,
 -- Technet, Tumblr, Wordpress, Yandex, Youtube, Flickr.
- Fix Australis icon positioning:
 -- https://github.com/EFForg/https-everywhere/pull/216

* Wed Apr 16 2014 Russell Golden <niveusluna@niveusluna.org> - 3.5-1
- Merge all non-ruleset changes from 4.0development.16
- Merge all new/modified rulesets from 4.0development.16 that are
 -- in the Alexa Top 1000 using utils/alexa-ruleset-checker.py. For a full list,
 -- see utils/alexa-logs/07042014.log.

* Sun Jan 05 2014 Russell Golden <niveusluna@niveusluna.org> - 3.4.5-1
- Tiny ruleset tweaks (XKCD is back)!
- Create an about:config setting that overrules mixedcontent ruleset disablement
- Updated license
- Updated README.md
- Updated contributors list
- Fix a performance bug when re-enabling HTTPS-Everywhere from its menu
- Observatory cert whitelist update
- Updated rules: Atlassian, Brightcove, MIT, Pidgin, Microsoft, Whonix,
 -- Skanetrafiken, Stack-Exchange, Stack-Exchange-mixedcontent

* Tue Dec 17 2013 Russell Golden <niveusluna@niveusluna.org> - 3.4.3-1
- Fixes: Cloudfront / Amazon MP3 player, Cornell/Arxiv, FlickR,
 -- AmazonAWS/spiegel.tv 
- Disable broken: Barns and Noble, Behance, Boards.ie, Elsevier, Kohls,
 -- OpenDNS, Spin.de, Svenskakyrkan
- Deprecate the ContentPolicy API, fixing a crash bug
 -- lurking since Firefox 20:
 -- https://bugzilla.mozilla.org/show_bug.cgi?id=939180
- Fix really silly Observatory UI bug that would leave the Observatory off
 -- for non-Tor users after they turned it on
- Update Observatory blacklist
- Bump maxVersion from Firefox 25 to 28.

* Wed Oct 09 2013 Russell Golden <niveusluna@niveusluna.org> - 3.4.2-1
- HTTPS Everywhere builds are now deterministic!
- Global memory leak bug fixes
- Updated rules: Craigslist, Apple.com, Microsoft, CloudFront, UKLocalGov,
 -- Bing, Cengage
- New rules from dev: IPTorrents.com, TvTorrents

* Mon Aug 19 2013 Russell Golden <niveusluna@niveusluna.org> - 3.4.1-1
- Update to upstream 3.4.1. There were a lot of changes since the last update.
 -- See https://www.eff.org/files/Changelog.txt for details.

* Sun Jul 28 2013 Russell Golden <niveusluna@niveusluna.org> - 3.3.1-1
3.3.1
- [Wikimedia] removed mixedcontent

3.3
- This major release fixed the following mixed content blocker (MCB) 
 -- related bugs in time for Firefox 23:
 -- https://trac.torproject.org/projects/tor/ticket/9196
 -- https://trac.torproject.org/projects/tor/ticket/8774
 -- https://trac.torproject.org/projects/tor/ticket/8776
- In effect, this update disables rulesets that cause mixed content errors
 -- by default, and adds platform="mixedcontent" to 950 new rules. This is
 -- necessary to prevent a massive amount of websites from breaking by default
 -- for our users when Firefox 23 comes out.
- [Internet Archive] Moved to stable
- [Linaro] Default off per webmaster request
- [Applicom] Default off per webmaster request

* Tue Jul 16 2013 Russell Golden <niveusluna@niveusluna.org> - 3.2.4-1
- [Yandex] remove maps from exclusions
- [Amazon Web Services] Add exclusion
  https://trac.torproject.org/projects/tor/ticket/8907
- [Hotmail / Live] Add exclusion
  https://trac.torproject.org/projects/tor/ticket/9026
- [Mozilla] Point labs to mozillalabs.org
  https://mail1.eff.org/pipermail/https-everywhere-rules/2013-July/001636.html
- [Yandex] Exclude ll
- [Brightcove] Add exclusion
  https://mail1.eff.org/pipermail/https-everywhere-rules/2013-May/001587.html
- [NYTimes] Add exclusion, disabled
- [News Corporation] Exclude 2013 images
  https://trac.torproject.org/projects/tor/ticket/9040
- [imgbox] Fix typo
  https://trac.torproject.org/projects/tor/ticket/8690

* Tue Jul 02 2013 Russell Golden <niveusluna@niveusluna.org> - 3.2.3-1
- Update to upstream 3.2.3

* Thu May 23 2013 Russell Golden <niveusluna@niveusluna.org> - 3.2.2-1
- Quick turn-around release to unbreak support.apple.com
- Fixes for a number of other ruleset bugs:
  https://eff.org/r.5bSj
- Incremental observatory cert whitelist update

* Sat May 18 2013 Russell Golden <niveusluna@niveusluna.org> - 3.2.1-1
- Implement XHR outstanding request limits to work around TCP connection
  -- exhaustion if the SSL Observatory server is slow or down:
  -- https://trac.torproject.org/projects/tor/ticket/8670
  -- https://bugzilla.mozilla.org/show_bug.cgi?id=856748
- Overdue update to the Observatory cert whitelist
- Other known ruleset fixes: EA, Yandex, Apple
  -- https://trac.torproject.org/projects/tor/ticket/8584
  -- https://trac.torproject.org/projects/tor/ticket/8571

* Wed May 01 2013 Russell Golden <niveusluna@niveusluna.org> - 3.2-1
- Related trac bugs for this release:
  https://eff.org/r.b9Qc
- New: MoinMoin
- Fixes: Adobe, Bahn.de, Cloudfront, Dell, Droplr, FBI, Google Maps,
  Joomla, Juno Download, Lenovo, New York Times, SEC, Soundcloud,
  Tweakers.net, Univ Strasbourg, Vkontakte, Zend
- Disable broken: AirAsia, Netvibes, Newgrounds, Pirate Bay, Russia Today, SVT,
  Wolfram Alpha
- Maybe fixed: Quantcast/Tumblr:
  https://trac.torproject.org/projects/tor/ticket/8406 (maybe fixed)
- Sync languages and translations from the master branch.
- New languages: Finnish, Norwegian (Bokmål), Slovak, Bulgarian.
- All HTTPS Everywhere users will be now prompted about using the
  SSL Observatory.

* Fri Mar 08 2013 Russell Golden <niveusluna@niveusluna.org> - 3.1.4-1
- The circles are stable releasee
- Fixes:
  - AmazonAWS/Atomsforpeace.info, Disqus, Eventbrite, ImageShack.us, MySQL,
    NuGet, NYTimes, Ooyala, Opera, Scientific American, SourceForge,
    University of Southampton, UserVoice, WebType, Zendesk
  - https://trac.torproject.org/projects/tor/ticket/8056
  - https://trac.torproject.org/projects/tor/ticket/8349
  - https://trac.torproject.org/projects/tor/ticket/7690
  - https://trac.torproject.org/projects/tor/ticket/8025
  - http://bugs.mysql.com/bug.php?id=67311
  - https://trac.torproject.org/projects/tor/ticket/7615
  - https://trac.torproject.org/projects/tor/ticket/8077
  - https://trac.torproject.org/projects/tor/ticket/8199
  - https://trac.torproject.org/projects/tor/ticket/8198
- Disable broken:
  - American Public Media (for real this time), Asymmetric Publications, 
    Salsa Labs, Vimeo
  - https://trac.torproject.org/projects/tor/ticket/7650
  - https://trac.torproject.org/projects/tor/ticket/8280
  - https://trac.torproject.org/projects/tor/ticket/7569
- Update cert whitelist

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Russell Golden <niveusluna@niveusluna.org> - 3.1.3-1
- Internet Freedom Day stable bugfix release
- Fixes: CloudFront/Spotify, AmazonAWS (Amazon MP3s and product images), Libav, 
         Google Maps, UserEcho
  https://trac.torproject.org/projects/tor/ticket/7931
  https://trac.torproject.org/projects/tor/ticket/7888
  https://trac.torproject.org/projects/tor/ticket/7594
  https://trac.torproject.org/projects/tor/ticket/7539
  https://trac.torproject.org/projects/tor/ticket/7698
- Disable broken: Coursera, EBay, Etsy, OpenOffice, Ping.fm, Pinterest :(
  https://trac.torproject.org/projects/tor/ticket/7336
  https://trac.torproject.org/projects/tor/ticket/7825
  https://trac.torproject.org/projects/tor/ticket/7774
  https://trac.torproject.org/projects/tor/ticket/7695
  https://trac.torproject.org/projects/tor/ticket/7777
  https://trac.torproject.org/projects/tor/ticket/7865
- Update cert whitelist

* Thu Jan 03 2013 Russell Golden <niveusluna@niveusluna.org> - 3.1.2-1
- Fixes for: AmazonAWS/Datawrapper, Cachefly, Cloudfront/C-SPAN, Hetzner.de KeyDrive/Snapnames, QT, openDesktop, OpenTTD, WhiskeyMedia https://mail1.eff.org/pipermail/https-everywhere-rules/2012-December/001432.html https://trac.torproject.org/projects/tor/ticket/7608 https://trac.torproject.org/projects/tor/ticket/7567 https://mail1.eff.org/pipermail/https-everywhere-rules/2012-December/001432.html https://trac.torproject.org/projects/tor/ticket/7560 https://trac.torproject.org/projects/tor/ticket/7796
- Disable broken: FlossManuals, Pastebin, Poste.it, Ustream, TED, AusGamers https://trac.torproject.org/projects/tor/ticket/7731 https://trac.torproject.org/projects/tor/ticket/7850 https://trac.torproject.org/projects/tor/ticket/7840 https://trac.torproject.org/projects/tor/ticket/7548
- Increase Observatory deployment (65 percent-> 85 percent)
- Update cert whitelist

* Wed Dec 12 2012 Russell Golden <niveusluna@niveusluna.org> - 3.1-1
- Hacky solution to a very nasty bug in which <securecookie> directives
    would cause cookies to be flagged as secure even if they were set from
    HTTP origins!
    https://trac.torproject.org/projects/tor/ticket/7491
    https://mail1.eff.org/pipermail/https-everywhere-rules/2012-November/001397.html
- Fixes: Akamai, Biomed central, BYU, Cachefly / Topix, DuckDuckGo, Focus.de,
    Fortum, Mashable, Mail.ru, MayFirst/People Link, MIT, Rackspace, 
    Salsa Labs, SurveyMonkey, Tumblr
- Disable: Adtech.de, AllthingsD American Public Media, Dafont, MediaFire,
    Verizon, vk.com, Wired, Conde Nast
- Observatory-only translations into Hebrew and Croatian
- Offer the SSL Observatory popup to a larger cohort of users

* Sat Nov 10 2012 Russell Golden <niveusluna@niveusluna.org> - 3.0.4-1
- Fixes:
  -- ACLU, Amazon, Barnes & Noble, CharityNavigator, Cloudfront/Turntable.fm,
     Coursera, itella.fi, posti.fi, Uservoice
     https://trac.torproject.org/projects/tor/ticket/7336
     https://trac.torproject.org/projects/tor/ticket/7273
     https://trac.torproject.org/projects/tor/ticket/7227
- Disable broken:
  -- Asterisk, Boston Globe (separated out from NYTimes.com), Extabit, Gawker,
     Google Services (Followers widget), NPR, SF.se, SonyMusic, Statcounter, WebType
     https://trac.torproject.org/projects/tor/ticket/7270
     https://trac.torproject.org/projects/tor/ticket/7243
     https://trac.torproject.org/projects/tor/ticket/7361
     https://trac.torproject.org/projects/tor/ticket/7120
     https://trac.torproject.org/projects/tor/ticket/7278
     https://trac.torproject.org/projects/tor/ticket/7363
     https://trac.torproject.org/projects/tor/ticket/7294
- No longer cacert: lawblog.de
- Offer the SSL Observatory popup to a larger cohort of users
- Update translations: Spanish, Russian, Turkish, Swedish


* Tue Oct 30 2012 Russell Golden <niveusluna@niveusluna.org> - 3.0.3-1
- Work around a nasty bug that was affecting some high-volume Live Youtube streams
  -- (but not other live YouTube streams)
  -- https://trac.torproject.org/projects/tor/ticket/7127
- Other Fixes: 
  -- AdaCore, Akamai/MTV3 Katsomo, Akamai/HP, Atlassian, Bahn.de, DemocracyNow, MySQL, NuGet,
  -- PBS, Phronoix Media/Openbenchmarking, SSRN, Spoki
  -- https://trac.torproject.org/projects/tor/ticket/7219
  -- https://trac.torproject.org/projects/tor/ticket/7180
  -- https://trac.torproject.org/projects/tor/ticket/7135
  -- https://trac.torproject.org/projects/tor/ticket/7206
  -- https://trac.torproject.org/projects/tor/ticket/7198
- Disable broken/buggy:
  -- CBS/Last.fm, Citibank Australia, Bytename, HP, NIFTY, Microchip, MyOpenID,  NttDocomo
  -- https://trac.torproject.org/projects/tor/ticket/6587
  -- https://trac.torproject.org/projects/tor/ticket/7226
  -- https://trac.torproject.org/projects/tor/ticket/7111
  -- https://trac.torproject.org/projects/tor/ticket/7161
  -- https://trac.torproject.org/projects/tor/ticket/7114
  -- https://trac.torproject.org/projects/tor/ticket/7138
  -- https://trac.torproject.org/projects/tor/ticket/7107
- Updated translations:
  -- Greek, Russian, Latvian
- New translation:
  -- Turkish
- Offer the SSL Observatory popup to a larger cohort of users

* Sun Oct 21 2012 Russell Golden <niveusluna@niveusluna.org> - 3.0.2-1
- Some fixes that should have shipped in 3.0.1, but actually didn't:
  European Southern Observatory, Indeed, LibriVox
- New fixes:
  Microsoft (Bing login button), ZeniMax, Ubuntuone, TrueCrypt, Springer
  (fix / reenable), Optical Society, IMDB, Facebook, EzineArticles,
  Broadband Reports, Apache, Akamai (exclude Zynga content to prevent
  breakage of some Zynga games), Costco

* Mon Oct 15 2012 Russell Golden <niveusluna@niveusluna.org> - 3.0.1-1
- Fixes: adition.com, Akamai/SVTplay.se, Bahn.de, European Southern Observatory,
  IEEE, Indeed, Java, Librivox, Pinterest, New York Times, Springer, Vimeo,
  Shannon Health, O'Reilly Media
  https://trac.torproject.org/projects/tor/ticket/7080
  https://mail1.eff.org/pipermail/https-everywhere/2012-October/001583.html
  https://mail1.eff.org/pipermail/https-everywhere-rules/2012-October/001339.html
  https://mail1.eff.org/pipermail/https-everywhere-rules/2012-October/001343.html
- Disable broken:  Springer
  https://mail1.eff.org/pipermail/https-everywhere-rules/2012-October/001340.html
- Updated translations: Basque, Hungarian, Traditional Chinese

* Fri Oct 12 2012 Russell Golden <niveusluna@niveusluna.org> - 3.0.0-2
- Replace "firefox" in EPEL builds with "firefox >= 3.5" for EL
    users who think updates are for sissies and/or voiding support
    contracts with proprietary vendors. They can't use this if their
    Firefox install is older than 3.5 anyway, so what's the harm?

* Tue Oct 09 2012 Russell Golden <niveusluna@niveusluna.org> - 3.0.0-1
- Since version 2.x:
  - 1,455 new active rulesets
  - UI improvements: 
    -- right-click to view ruleset source in the config window
    -- translate some untranslated menus
    -- better icons in a few places (breaking/redirecting rules,
       context button)
  - Numerous improvements to the SSL Observatory internals, including cached
    submissions on hostile networks, better Tor and Convergence integration,
    and a new setting to control self-signed cert submission
  - New translations: Basque, Czech, Danish, French, Greek, Hungarian,
                      Italian, Korean, Malaysian, Polish, Slovak, Turkish,
                      Traditional Chinese
- Relative to 3.0development.8:
  - Only promote the Decentralized SSL Observatory to 5 percent of non-Tor users
  - Update the SSL Observatory whitelist of common cert chains
  - Fixes, mostly in the CDN/media playback department: 
           Akamai/CNN, GO.com/ABC, AWS/Amazon Zeitgeist MP3 player,
           AWS/Spiegel.tv, Technology Review, Cloudfront/Tunein,
           Akamai/Discovery Channel, Beyond Security, OCaml, Gentoo,
           Nokia, Widgetbox.com, Squarespace
           https://trac.torproject.org/projects/tor/ticket/4199
           https://trac.torproject.org/projects/tor/ticket/6871
           https://trac.torproject.org/projects/tor/ticket/6992
           https://trac.torproject.org/projects/tor/ticket/7000
           https://trac.torproject.org/projects/tor/ticket/7020
           https://mail1.eff.org/pipermail/https-everywhere-rules/2012-October/001324.html
  - Disable buggy: Web.de, AJC.com, Feross, Bestofmedia
  - Remove a lot of off-by-default rulesets from the code, since they have
    some costs in terms of startup speed and RAM usage

* Thu Sep 27 2012 Russell Golden <niveusluna@niveusluna.org> - 2.2.3-1
- Workaround for breakage in Amazon Look Inside the Book (via Cloudfront)
  -- https://trac.torproject.org/projects/tor/ticket/6848
- Fix logout for AOL users
- Other fixes: PassThePopcorn, WhatCD, Antispam.de, RFCeditor,
  -- Weatherspark / GoogleMaps
- Disable broken: SVT.se

* Thu Sep 06 2012 Russell Golden <niveusluna@niveusluna.org> - 2.2.2-1
- Fix a bug that was preventing settings from persisting:
    https://trac.torproject.org/projects/tor/ticket/6653
- Fixes and improvements: Lenovo, YahooNew, Pirate Party, OpenDNS, Wordpress
    https://trac.torproject.org/projects/tor/ticket/6604
    https://mail1.eff.org/pipermail/https-everywhere-rules/2012-August/001267.html
- Disable broken rulesets: FAZ, Playboy, Mapquest, Imgur, F-Secure

* Fri Aug 17 2012 Russell Golden <niveusluna@niveusluna.org> - 2.2.1-1
- Update to upstream 2.2.1. Hopefully this one will actually work.

* Fri Aug 17 2012 Russell Golden <niveusluna@niveusluna.org> - 2.1-5
- Add appManaged flag to prevent update in user profile directories
- prompted by release of badly broken 2.2 upstream

* Fri Aug 17 2012 Russell Golden <niveusluna@niveusluna.org> - 2.2-2
- Prevent ruleset bugs from crashing the UI
  -- https://trac.torproject.org/projects/tor/ticket/6280
- Fix the enable/disable button in Firefox 14
  -- https://trac.torproject.org/projects/tor/ticket/6212
- Fix a nasty bug in the optional "Search www.google.com" ruleset:
  -- https://gitweb.torproject.org/https-everywhere.git/commitdiff/50ca41a1e189ef8383781f803e51ec7a06688a3b
- Disable buggy/broken: ZDNet, Globe and Mail, Blip.tv, Governo PortugÃªs,
  -- Alton Towers, McAfee :( :( :(
- Fixes: Yandex, Wikipedia, PirateParty, JBoss, Gentoo
- Hopefully the last 2.x release before 3.0 stable

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Russell Golden <niveusluna@niveusluna.org> - 2.1-3
- Change Requires to require firefox on all RHEL versions

* Sun Jun 24 2012 Russell Golden <niveusluna@niveusluna.org> - 2.1-2
- Fix context menu breakage when URIs lack a host
- Fixes: CiteULike, MozillaMessaging, Yandex, Demonoid, Pirate Party,
  --  Gentoo, NYTimes, Microsoft, Wikipedia, Lenovo
  --  https://mail1.eff.org/pipermail/https-everywhere-rules/2012-June/001189.html
  --  https://trac.torproject.org/projects/tor/ticket/6091
  --  https://mail1.eff.org/pipermail/https-everywhere-rules/2012-June/001190.html
  --  https://mail1.eff.org/pipermail/https-everywhere-rules/2012-May/001186.html
  --  https://mail1.eff.org/pipermail/https-everywhere/2012-May/001433.html
- Disable broken: MarketWatch, Disqus, Magento, Lavasoft, Project Syndicate,
  -- Typepad/Say Media
  --  https://trac.torproject.org/projects/tor/ticket/5899
  --  https://trac.torproject.org/projects/tor/ticket/5496

* Tue May 01 2012 Russell Golden <niveusluna@niveusluna.org> - 2.0.3-2
- Add file that I missed in the last build.

* Sat Apr 28 2012 Russell Golden <niveusluna@niveusluna.org> - 2.0.3-1
- Fix a downgrade attack that might allow attackers to deny HTTPS
    Everywhere protection for cookies on some domains.
    https://trac.torproject.org/projects/tor/ticket/5676
- Minor redirection mechanism fixes
- Fixes: WordPress, Yandex, OpenDNS, Via.me/AWS
- Improvements: Mozilla
- Disable broken: ReadWriteWeb

* Fri Apr 20 2012 Russell Golden <niveusluna@niveusluna.org> - 2.0.2-1
- Fix a weird wrong DOM-origin bug that occurred while redirects were in
  --  progress (this might have security implications, although we are unsure
  --  if it was exploitable).
  --  https://trac.torproject.org/projects/tor/ticket/5477
- By default, use https://google.co.cctld instead of
  --  encrypted.google.com
- Add an optional ruleset to use https://www.google.com
  -- instead of encrypted.google.com, too
- Ruleset fixes: Debian, Kohls, Malwarebytes, Yandex, Wikipedia, Mises.org,
  -- OpenDNS, Wizards of the Coast, Lenovo, Barnes and Noble
  --  https://trac.torproject.org/projects/tor/ticket/5509
  --  https://trac.torproject.org/projects/tor/ticket/5491
  --  https://trac.torproject.org/projects/tor/ticket/5303
- Stumble across more horrible security holes in the Verizon website:
  --  https://mail1.eff.org/pipermail/https-everywhere-rules/2012-February/001003.html
- Disable the Gentoo ruleset on non-CAcert platforms
- Disable buggy rulesets: IBM, Scribd, Wunderground :( :( :(
  --  https://trac.torproject.org/projects/tor/ticket/5344
  --  https://trac.torproject.org/projects/tor/ticket/5435
  --  https://trac.torproject.org/projects/tor/ticket/5630

* Wed Feb 29 2012 Russell Golden <niveusluna@niveusluna.org> - 2.0.1-1
- Sync to upstream 2.0.x branch
- Too many changes to all list here. None affect the end user experience.
    Being a Mozilla extension, it'll auto-update anyway.

* Wed Jan 11 2012 Russell Golden <niveusluna@niveusluna.org> - 1.2.2-1
- Google Cache is back!
- Fixes: Wikipedia, Identi.ca, Verizon, CCC.de, UserScripts, Yandex
- Improvements: EFF
- Disable broken: NSF.gov, WHO.int

* Wed Nov 16 2011 Russell Golden <niveusluna@niveusluna.org> - 1.2.1-1
- Google Cache is broken, remove it from GoogleServices :( :( :(
- Fix for the Google Image Search homepage
- Exclude help.duckduckgo.com:
--    https://trac.torproject.org/projects/tor/ticket/4399
- Disable Yahoo! Mail:
--    https://trac.torproject.org/projects/tor/ticket/4441
- Installable on Firefox 10

* Tue Nov 15 2011 Russell Golden <niveusluna@niveusluna.org> - 1.2-1
- Fixes: WordPress, Statcounter, Java, Bahn.de, SICS.se
- Improvements: use fancy new HTTPS Wikipedia
- Disable broken: OpenUniversity, TV.com, Random.org, kb.CERT

* Thu Oct 20 2011 Russell Golden <niveusluna@niveusluna.org> - 1.1-1
- Further tweaks to internals, will hopefully fix a number of weird issues:
--      https://trac.torproject.org/projects/tor/ticket/4194
--      https://trac.torproject.org/projects/tor/ticket/4149
--      https://mail1.eff.org/pipermail/https-everywhere/2011-October/001208.html
- YouTube is enabled by default!
- Fixes: Yandex, Statcounter, Polldaddy, SBB.ch
- Improvements: Facebook+
- Disable broken: Bloglines, EPEAT

* Sat Oct 8 2011 Russell Golden <niveusluna@niveusluna.org> - 1.0.3-2
- Changelog added for current version

* Fri Sep 16 2011 Russell Golden <niveusluna@niveusluna.org> - 1.0.1-1
- Initial packaging for Fedora

