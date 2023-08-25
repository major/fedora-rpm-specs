# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global moz_extensions %{_datadir}/mozilla/extensions

%global ext_id jid1-MnnxcxisBPnSXQ@jetpack

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

Name:           mozilla-privacy-badger
Version:        2023.6.23
Release:        1%{?dist}
Summary:        Protects your privacy by blocking spying ads and invisible trackers

License:        ASL 2.0 and GPLv3+ and MPLv2.0 and MIT and OFL and Public Domain
URL:            https://www.eff.org/privacybadger
Source0:        https://github.com/EFForg/privacybadger/archive/release-%{version}/privacybadger-%{version}.tar.gz
Requires:       mozilla-filesystem
BuildArch:      noarch
BuildRequires:  sed
BuildRequires:  zip
# lib/vendor/jquery-3.5.1.min.js
# https://jquery.com MIT
Provides:       bundled(js-jquery) = 3.5.1
# lib/vendor/jquery.smooth-scroll.js
# https://github.com/kswedberg/jquery-smooth-scroll MIT
Provides:       bundled(js-jquery-smooth-scroll) = 2.2.0
# lib/vendor/jquery-ui.custom/jquery-ui.min.js
# lib/vendor/jquery-ui.custom/jquery-ui.structure.min.css
# lib/vendor/jquery-ui.custom/jquery-ui.theme.min.css
# https://jqueryui.com MIT
Provides:       bundled(js-jquery-ui) = 1.13.0
# lib/vendor/jquery-ui-iconfont-2.3.2
Provides:       bundled(js-jquery-ui-iconfont) = 2.3.2
# skin/fonts/Chunk.ttf
# https://www.fontsquirrel.com/fonts/chunkfive OFL
Provides:       bundled(fontsquirrel-chunk-five-fonts)
# skin/fonts/OpenSans-*.ttf
# http://www.google.com/fonts/specimen/Open+Sans ASL 2.0
Provides:       bundled(open-sans-fonts)
# lib/vendor/select2-4.0.11
# https://select2.github.io MIT
Provides:       bundled(js-select2) = 4.0.11
# lib/vendor/tooltipster-4.2.6
# http://iamceege.github.io/tooltipster/ MIT
Provides:       bundled(tooltipster) = 4.2.6
#
# lib/basedomain.js
# parts of original code from ipv6.js <https://github.com/beaugunderson/javascript-ipv6> MIT
#
# js/contentscripts/fingerprinting.js
# js/contentscripts/supercookie.js
# js/webrequest.js
# derived from https://github.com/ghostwords/chameleon MPL or GPLv3+
#
# js/contentscripts/socialwidgets.js
# js/socialwidgetloader.js
# skin/socialwidgets/socialwidgets.css
# Derived from ShareMeNot https://sharemenot.cs.washington.edu MIT
# 
# js/background.js
# js/options.js
# js/popup.js
# js/utils.js
# js/webrequest.js
# lib/i18n.js
# skin/options.html
# skin/popup.html
# derived from https://adblockplus.org/en/firefox GPLv3+
#
# js/firstparties/facebook.js
# adapted from https://github.com/mgziminsky/FacebookTrackingRemoval GPLv3+

%description
Privacy Badger is a browser add-on that stops advertisers and other third-party
trackers from secretly tracking where you go and what pages you look at on the
web. If an advertiser seems to be tracking you across multiple websites without
your permission, Privacy Badger automatically blocks that advertiser from
loading any more content in your browser. To the advertiser, it's like you
suddenly disappeared.

%prep
%setup -q -n privacybadger-release-%{version}
rm -rv src/data/dnt-policy.txt src/tests

%build
# https://github.com/EFForg/privacybadger/blob/master/release-utils/make-signed-xpi.sh
mkdir pkg

sed -i -e '/eff.software.projects@gmail.com/,+1d' -e 's/"author": {/"author": "privacybadger-owner@eff.org",/' src/manifest.json

sed -i -e '/"update_url": "https:\/\/clients2.google.com\/service\/update2\/crx"/,+0d' src/manifest.json

rm -fv pkg/privacybadger-%{version}.zip
pushd src
zip -v -q -x pkg -r ../pkg/privacybadger-%{version}.zip ./*
popd

%install
install -Dpm644 pkg/privacybadger-%{version}.zip %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi

%files
%license LICENSE
%doc doc/Changelog
%doc doc/fixing-broken-sites.md
%doc doc/permissions.md
%doc doc/yellowlist-criteria.md
%dir %{firefox_inst_dir}
%{firefox_inst_dir}/%{ext_id}.xpi

%changelog
* Wed Aug 23 2023 Dominik Mierzejewski <dominik@greysector.net> - 2023.6.23-1
- update to 2023.6.23 (#2215417)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Dominik Mierzejewski <dominik@greysector.net> - 2023.5.10-1
- update to 2023.5.10 (#2166099)
- "build" from source
- include useful docs

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.9.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Dominik Mierzejewski <dominik@greysector.net> - 2022.9.27-1
- update to 2022.9.27 (#2130321)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.11.23.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.11.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2021.11.23.1-1
- update to 2021.11.23.1 (#2026143)

* Fri Aug 20 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2021.8.17-1
- update to 2021.8.17 (#1993105)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2021.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2021.6.8-1
- update to 2021.6.8 (#1969738)
- drop Provides: for removed bundled libraries

* Sat Feb 20 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2021.2.2-1
- update to 2021.2.2 (#1924367)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2020.12.10-1
- update to 2020.12.10 (#1906210)

* Fri Oct 09 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2020.10.7-1
- update to 2020.10.7 (#1886250)

* Wed Sep 02 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2020.8.25-1
- update to 2020.8.25 (#1872503)

* Mon Jul 27 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2020.7.21-1
- update to 2020.7.21 (#1835050)

* Tue Apr 21 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2020.2.19-1
- update to 2020.2.19 (#1788939)
- update bundled deps

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.11.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2019.11.18-1
- update to 2019.11.18 (#1766845)

* Fri Oct 11 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2019.10.8-1
- update to 2019.10.8 (#1759756)

* Sat Sep 28 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2019.9.23-1
- update to 2019.9.23 (#1754627)

* Fri Sep 13 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2019.7.1.1-1
- update to 2019.7.1.1 (#1726648)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.2.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2019.2.19-2
- fix erroneous Provides: (#1698596)

* Thu Feb 21 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2019.2.19-1
- update to 2019.2.19 (#1671219)
- update bundled components version list

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2018.10.3.1-1
- update to 2018.10.3.1
- update bundled components and license list

* Sun Aug 05 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2018.8.1-1
- update to 2018.8.1 (#1611031)
- update bundled components list

* Mon Jul 30 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2018.7.18.1-1
- update to 2018.7.18.1
- update bundled components list

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2018.2.5-2
- drop BSD from license list (no BSD-licensed components anymore)
- own firefox_inst_dir

* Wed Feb 21 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2018.2.5-1
- update to 2018.2.5
- update bundled components list
- drop SeaMonkey support

* Sun Jul 02 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2017.6.13.1-1
- update to 2017.6.13.1
- update source URL
- update bundled components list
- drop support for RHEL5

* Tue Mar 21 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 2017.1.26.1-1
- update to 2017.1.26.1
- update source URL
- update bundled components list
- bump minimum firefox version for RHEL5

* Wed Nov 02 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.8.1-1
- update to 1.8.1
- bump minimum firefox version for RHEL5

* Thu Jul 28 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.7.0-1
- update to 1.7.0
- drop CC-BY from License: (not sure how it got there)

* Fri Mar 11 2016 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.0.6-1
- update to 1.0.6

* Thu Dec 17 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.0.5-1
- update to 1.0.5 (signed, from addons.mozilla.org)

* Thu Dec 10 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.0.3-1
- update to 1.0.3 (git commit 5145fa1)

* Sun Aug 09 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.0.0-1
- update to 1.0.0 (git commit b086016)

* Thu May 21 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.2.6.1-2.2b4e077
- update to latest git master

* Wed May 13 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.2.6.1-1.d219f00
- update to latest git master
- build from github source
- unbundle jquery
- drop obsolete patch

* Mon Apr 13 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.2.6-1
- update to 0.2.6
- remove bundled sha1 implementation and use built-in Firefox API

* Mon Jan 12 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.2.4-2
- replace non-free sha1 implementation

* Sun Jan 11 2015 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.2.4-1
- update to 0.2.4

* Mon Dec 15 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.2.3-1
- update to 0.2.3
- switch source URL to EFF site
- minimum firefox version is 26
- simplify and improve install commands
- fix install path for seamonkey

* Mon Oct 20 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 0.1.4-1
- Initial package
