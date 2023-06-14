# internal macros ???
%global _firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global _moz_extensions %{_datadir}/mozilla/extensions
%global _firefox_extdir %{_moz_extensions}/%{_firefox_app_id}

# needed for this package
%global extension_id \{73a6fe31-595d-460b-a920-fcc0f8843232\}

%global nscl_commit f84e94cdcf576ecc25da02d10b6db660c4199dce

Name:           mozilla-noscript
Version:        11.4.22
Release:        1%{?dist}
Summary:        JavaScript white list extension for Mozilla Firefox

License:        GPL-3.0-or-later AND MIT AND MPL-2.0 AND CC-BY-SA-3.0
URL:            http://noscript.net/
Source0:        https://github.com/hackademix/noscript/archive/%{version}/noscript-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=1364409
Source1:        %{name}.metainfo.xml
Source2:        https://github.com/hackademix/nscl/archive/%{nscl_commit}/nscl-%{nscl_commit}.tar.gz
# work offline
# use zip instead of web-ext
Patch0:         %{name}-fedora.patch

BuildRequires:  libappstream-glib
BuildRequires:  nodejs
BuildRequires:  publicsuffix-list
BuildRequires:  zip
Requires:       mozilla-filesystem
# https://github.com/mdmoreau/flextabs MIT
Provides:       bundled(js-flextabs) = 0.2.0
# https://mths.be/he MIT
Provides:       bundled(js-he) = 1.2.0
# https://mths.be/punycode MIT
Provides:       bundled(js-punycode) = 1.4.1
# https://github.com/emn178/js-sha256 MIT
Provides:       bundled(js-sha256) = 0.9.0
# https://github.com/hackademix/nscl GPLv3+
Provides:       bundled(js-nscl) = 0.0.1
# https://github.com/mozilla/webextension-polyfill MPL
Provides:       bundled(webextension-polyfill) = 0.8.0
Provides:       firefox-noscript = %{version}-%{release}
BuildArch:      noarch

%description
The NoScript extension provides extra protection for Firefox.
It allows JavaScript, Java, Flash and other plug-ins to be executed only by
trusted web sites of your choice (e.g. your online bank) and additionally
provides Anti-XSS protection.

%prep
%setup -q -n noscript-%{version}
tar -xz -C src/nscl --strip-components=1 -f %{S:2}
%patch 0 -p1 -b .f
cp -p src/nscl/COPYING nscl.COPYING
cp -p src/nscl/LICENSE.md nscl.LICENSE.md
ln -s /usr/share/publicsuffix/public_suffix_list.dat ./

%build
sh -x ./build.sh

%install
# install into _firefox_extdir
install -Dp -m 644 xpi/noscript-%{version}.xpi %{buildroot}%{_firefox_extdir}/%{extension_id}.xpi

# install MetaInfo file for firefox, etc
install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license LICENSE nscl.COPYING nscl.LICENSE.md src/nscl/lib/{browser-polyfill,punycode,sha256}.js.license
%{_firefox_extdir}/%{extension_id}.xpi
# GNOME Software Center metadata
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
* Mon Jun 12 2023 Dominik Mierzejewski <dominik@greysector.net> - 11.4.22-1
- update to 11.4.22 (#2204533)
- fix deprecated patchN macro usage

* Thu Apr 06 2023 Dominik Mierzejewski <dominik@greysector.net> - 11.4.21-1
- update to 11.4.21 (#2180051)
- switch to SPDX license identifiers

* Mon Mar 13 2023 Dominik Mierzejewski <dominik@greysector.net> - 11.4.18-1
- update to 11.4.18 (#2173530)

* Wed Feb 08 2023 Dominik Mierzejewski <dominik@greysector.net> - 11.4.16-1
- update to 11.4.16 (resolves rhbz#2164922)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Dominik Mierzejewski <dominik@greysector.net> - 11.4.14-1
- update to 11.4.14 (#2158071)

* Sun Dec 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 11.4.13-1
- update to 11.4.13 (#2142813)

* Tue Oct 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 11.4.11-1
- update to 11.4.11 (#2118040)

* Wed Aug 10 2022 Dominik Mierzejewski <dominik@greysector.net> - 11.4.7-1
- update to 11.4.7 (#2116118)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Dominik Mierzejewski <dominik@greysector.net> - 11.4.6-1
- update to 11.4.6 (#2096232)
- ensure publicsuffix-list is updated

* Wed May 04 2022 Dominik Mierzejewski <dominik@greysector.net> - 11.4.5-2
- replicate upstream "build" process

* Tue May 03 2022 Dominik Mierzejewski <dominik@greysector.net> - 11.4.5-1
- update to 11.4.5 (#2068417)

* Tue Feb 15 2022 Dominik Mierzejewski <rpm@greysector.net> - 11.2.25-1
- update to 11.2.25 (#2050078)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.2.11-1
- update to 11.2.11 (#1986697)

* Fri Jul 23 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.2.10-1
- update to 11.2.10 (#1985098)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.2.9-1
- update to 11.2.9 (#1975551)
- license changed to GPLv3+
- polyfill was updated
- new bundled library: he
- drop ancient RHEL6 conditionals
- dro pancient Obsoletes

* Tue May 25 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.2.8-1
- update to 11.2.8 (#1962394)

* Mon May 17 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.2.7-1
- update to 11.2.7 (#1956505)

* Thu Apr 01 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.2.4-1
- update to 11.2.4 (#1928639)

* Wed Feb 10 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.2-1
- update to 11.2 (#1920680)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Dominik Mierzejewski <rpm@greysector.net> - 11.1.9-1
- update to 11.1.9 (#1914007)
- polyfill was updated
- fastclick is no longer included

* Tue Dec 29 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.1.7-1
- update to 11.1.7 (#1906206)

* Mon Nov 16 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.1.5-1
- update to 11.1.5 (#1895341)

* Wed Nov 04 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.1.4-1
- update to 11.1.4 (#1885187)
- switch to AMO URL for source

* Mon Oct 05 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.46-1
- update to 11.0.46 (#1877073)

* Tue Sep 08 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.42-1
- update to 11.0.42 (#1876014)

* Mon Aug 31 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.41-1
- update to 11.0.41 (#1870896)

* Thu Aug 20 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.38-1
- update to 11.0.38 (#1861922)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.34-1
- update to 11.0.34 (#1841091)

* Tue May 19 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.26-1
- update to 11.0.26 (#1836699)

* Sun May 03 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.25-1
- update to 11.0.25 (#1825050)

* Sun Apr 12 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.23-1
- update to 11.0.23 (#1813501)

* Mon Mar 09 2020 Dominik Mierzejewski <rpm@greysector.net> - 11.0.15-1
- update to 11.0.15 (#1782610)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Dominik Mierzejewski <rpm@greysector.net> - 11.0.9-1
- update to 11.0.9 (#1756745)

* Thu Sep 12 2019 Dominik Mierzejewski <rpm@greysector.net> - 11.0.3-1
- update to 11.0.3 (#1751683)
- add more bundled libraries

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Dominik Mierzejewski <rpm@greysector.net> - 10.2.1-2
- update to 10.2.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 26 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.9.9-1
- update to 10.1.9.9
- sync obsoleted classic version with F28 and older

* Sun Sep 16 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.9.6-1
- update to 10.1.9.6
- drop classic version and move WebExtension back to main package
- obsolete old vulnerable classic extension versions so that users
  can install the latest version independently

* Mon Jul 30 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.16-2
- update to 10.1.8.16 (#1609266)
- make main package dependencies on subpackages versioned

* Fri Jul 20 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.8-1
- update to 10.1.8.8 (#1601456)
- update classic version to 5.1.8.6
- extract only the licenses and cfg file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.2-3
- update to 10.1.8.2 (#1583884)

* Wed May 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.8.1-2
- update to 10.1.8.1 (#1572820)

* Thu Apr 12 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.7.5-1
- update to 10.1.7.5 (#1557592)
- update classic version to 5.1.8.5

* Fri Mar 16 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.7.2-2
- update to 10.1.7.2 (#1557318)
- update bundled components Provides:

* Mon Feb 19 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.5-1
- update to 10.1.6.5 (#1543851)
- update classic version to 5.1.8.4

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.4-1
- update to 10.1.6.4 (#1539464)
- switch URL to upstream instead of AMO, they're identical
- split FF and SM extensions to separate subpackages

* Sat Jan 20 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.3-1
- update to 10.1.6.3 (#1532905)
- install metainfo file in the new standard location

* Mon Jan 01 2018 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6.2-1
- update to 10.1.6.2 (#1528835)

* Tue Dec 19 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.6-1
- update to 10.1.6 (#1527501)

* Sat Dec 16 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.5.8-1
- update to 10.1.5.8 (#1524389)
- bring back the classic version (still developed until June 2018)
  for SeaMonkey (#1526199)

* Sat Nov 25 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.2-1
- update to 10.1.2

* Mon Nov 20 2017 Dominik Mierzejewski <rpm@greysector.net> - 10.1.1-1
- update to 10.1.1 (pure WebExtension version, Firefox 57+ only)

* Thu Nov 02 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.1.4-1
- update to 5.1.4 (#1504408)

* Sun Oct 01 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.1.1-1
- update to 5.1.1 (#1491072)

* Wed Aug 23 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.9-1
- update to 5.0.9 (#1476252)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.7.1-1
- update to 5.0.7.1 (#1474552)

* Mon Jul 03 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.6-1
- update to 5.0.6 (#1467119)
- switch to AMO URL

* Tue May 30 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.5-1
- update to 5.0.5 (#1450033)

* Tue Mar 21 2017 Dominik Mierzejewski <rpm@greysector.net> - 5.0.2-1
- update to 5.0.2 (#1429065)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.9.5.3-1
- update to 2.9.5.3 (#1414179)

* Mon Dec 05 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.5.2-1
- update to 2.9.5.2 (#1400191)

* Wed Nov 23 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.5.1-1
- update to 2.9.5.1 (#1397613)

* Mon Nov 21 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.14-3
- EL7 has gnome-software, so ship appstream data there, too

* Sun Aug 21 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.14-2
- include AppStream metadata (#1364409)

* Wed Aug 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.14-1
- update to 2.9.0.14 (#1365329)

* Wed Aug 03 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.13-1
- update to 2.9.0.13 (#1362319)

* Fri Jul 29 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.12-1
- update to 2.9.0.12 (#1360761)

* Sun Apr 10 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.11-1
- update to 2.9.0.11 (#1325580)

* Tue Mar 29 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.10-1
- update to 2.9.0.10 (#1319364)

* Thu Mar 17 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.5-1
- update to 2.9.0.5 (#1318460)
- clean up spec and drop EL5-specific stuff

* Sun Feb 14 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.4-1
- update to 2.9.0.4 (#1306872)

* Sat Feb 06 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.3-1
- update to 2.9.0.3 (#1304561)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9.0.2-1
- update to 2.9.0.2 (#1296924)

* Tue Jan 05 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.9-1
- update to 2.9 (#1295023)

* Sun Dec 20 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.7-2
- package unexploded so that it doesn't get disabled in FF43+
- tag license text file appropriately

* Thu Nov 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.7-1
- update to 2.7 (#1284465)

* Mon Oct 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.39-1
- update to 2.6.9.39 (#1275118)
- internal chrome/noscript.jar is back again

* Thu Oct 15 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.38-1
- update to 2.6.9.38 (#1270625)
- internal chrome.jar is now shipped unpacked by upstream
- keep timestamps after EOL conversion

* Wed Sep 30 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.37-1
- update to 2.6.9.37 (#1267409)

* Wed Sep 02 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.36-1
- update to 2.6.9.36 (#1252869)

* Sat Aug 15 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.35-1
- update to 2.6.9.35 (#1252869)

* Tue Aug 04 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.34-1
- update to 2.6.9.34

* Fri Jul 31 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.33-1
- update to 2.6.9.33 (#1248239)

* Tue Jul 28 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.32-1
- update to 2.6.9.32 (#1247133)

* Tue Jul 21 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.31-1
- update to 2.6.9.31 (#1243616)

* Fri Jul 10 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.30-1
- update to 2.6.9.30 (#1241523)

* Thu Jul 02 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.29-1
- update to 2.6.9.29 (#1237141)

* Thu Jun 18 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.27-1
- update to 2.6.9.27 (#1232980)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.26-1
- update to 2.6.9.26 (#1226495)

* Tue May 26 2015 Dominik Mierzejewski <rpm@greysector.net> - 2.6.9.25-1
- update to 2.6.9.25 (#1197536)

* Sat Feb 21 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.6.9.15-1
- update to 2.6.9.15 (#1176917)

* Wed Dec 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.9.8-1
- update to 2.6.9.8 (#1164453)

* Tue Nov 11 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.9.3-1
- update to 2.6.9.3 (#1124181,#1162797)

* Thu Jul 24 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.33-1
- update to 2.6.8.33 (#1104527)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.26-1
- update to 2.6.8.26 (#1094684)

* Tue Apr 15 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.20-1
- update to 2.6.8.20 (#1064214)

* Fri Jan 24 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.8-1
- update to 2.6.8.13 (#1030891, #1044655)

* Sat Oct 26 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.4-1
- update to 2.6.8.4 (#1023548, #958170)

* Sun Oct 13 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.8.2-1
- update to 2.6.8.2

* Mon Aug  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.6.9-1
- update to 2.6.6.9
- fix files section to fix FTBFS (#992292)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.6.5.9-1
- update to 2.6.5.9 (#890564)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 18 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.6.4.1-1
- update to 2.6.4.1 (#888187)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Thomas Spura <tomspur@fedoraproject.org> - 2.4.6-1
- update to 2.4.6

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 30 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.4-1
- update to new version (#712331)

* Fri Aug  5 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.1-2
- change the macros to match MozillaExtensionsDraft

* Fri Jun  3 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.1.1-1
- update to new version (#691356)
- renew patch

* Thu Mar 10 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.0.9.9-1
- update to new version (#667389)
- renew patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.0.9.2-1
- update to new version
- renew patch

* Mon Oct 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.5.1-1
- update to new version

* Mon Oct 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.3.5-1
- update to new version
- renew patch

* Thu Aug 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.2.1-2
- require firefox and not mozilla-filesystem on el5

* Wed Aug 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0.2.1-1
- update to new version

* Fri Jul 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.0-1
- update to new version

* Sun Jul 18 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.10-1
- new version
- renew preferences patch

* Wed Jun 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.97-1
- new version

* Sat Jun 12 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.87-1
- new version

* Fri May 28 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.81-1
- new version

* Mon May 24 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.79-1
- new version

* Sun May 16 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.74-1
- new version
- renew patch

* Thu Apr 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.69-1
- new version

* Mon Apr 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.66-1
- new version

* Sat Apr  3 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.60-1
- new version

* Fri Mar 19 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.57-1
- update to new version
- force dos2unix on 'binary' GPL.txt
- renew patch

* Sat Feb 27 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.50-1
- update to new version
- fix some spelling errors

* Sun Feb  7 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.45-1
- update to new version

* Sat Jan 23 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.39-1
- update to new version

* Sat Jan 16 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-4
- install with -p

* Fri Jan 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-3
- also install seamonkey app_id (Thomas Moschny)

* Fri Jan 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-2
- remove R: firefox, this plugin also works for seamonky and so on
  it's up to the user, what to use (Thomas Moschny)

* Fri Jan 15 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.9.9.35-1
- update to new version
- %%global vs %%define
- install in %%{_datadir} -> noarch
- delete changelog
- R: mozilla-filesystem for owning %%{_datadir}/mozilla/extensions

* Sun Jul 19 2009 Andreas Thienemann <andreas@bawue.net> - 1.9.6-1
- Initial package
