%global		oname torbrowser_launcher
Name:		torbrowser-launcher
Version:	0.3.7
Release:	6%{?dist}
Summary:	Tor Browser Bundle managing tool
License:	MIT
URL:		https://github.com/micahflee/torbrowser-launcher/
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
ExclusiveArch: %{ix86} x86_64
BuildRequires:	desktop-file-utils
BuildRequires:	python3-devel
BuildRequires:	gettext
BuildRequires:	libappstream-glib
BuildRequires:  python3-distro
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
Requires:	python3
Requires:	gnupg2
Requires:	tor
Requires:	python3-pysocks
Requires:	python3-gpg
Requires:	python3-qt5
Requires:	python3-requests
Requires:       python3-packaging
Requires:       dbus-glib

%description
Tor Browser Launcher is intended to make Tor Browser easier to
install and use for GNU/Linux users. You install torbrowser-launcher
from your distribution's package manager and it handles everything else:

* Downloads and installs the most recent version of Tor Browser in your language
  and for your computer's architecture, or launches Tor Browser if it's already
  installed (Tor Browser will automatically update itself)
* Verifies Tor Browser's signature for you, to ensure the version you downloaded
  was cryptographically signed by Tor developers and was not tampered with
* Adds "Tor Browser" and "Tor Browser Launcher Settings" application launcher
  to your desktop environment's menu
* Optionally plays a modem sound when you open Tor Browser
  (because Tor is so slow)

%prep
%setup -q -n %{name}-%{version}

# We need to specify the distro we are building on, Fedora!
sed -i 's#distro = .*#distro = "Fedora"#g' setup.py
sed -i 's/Ubuntu/Fedora/g' setup.py
sed -i "s#'update_over_tor': True#'update_over_tor': False#g" torbrowser_launcher/common.py
sed -i -r "s/^([ \t]+)self.label1 = gtk.Label\(_\('Not installed'\)\)/\
\1self.label1 = gtk.Label\(_\('Not installed'\)\)\n\1self.tor_update_checkbox.\
set_active\(False\)/g" torbrowser_launcher/settings.py


%build
%pyproject_wheel
desktop-file-validate share/applications/torbrowser.desktop
desktop-file-validate share/applications/torbrowser-settings.desktop

%install
find . -name apparmor -type d -print0|xargs -0 rm -r --
%pyproject_install
install -m 644 -D share/metainfo/org.torproject.torbrowser-launcher.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/org.torproject.torbrowser-launcher.metainfo.xml

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.torproject.torbrowser-launcher.metainfo.xml

%files -f %{name}.lang
%{_bindir}/%{name}
%doc README.md
%license LICENSE
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/128x128/apps/torbrowser.png
%{_datadir}/%{name}/*
%{python3_sitelib}/%{oname}/*
%{_metainfodir}/org.torproject.torbrowser-launcher.metainfo.xml
%{python3_sitelib}/%{oname}-%{version}.dist-info/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.7-4
- Rebuilt for Python 3.13

* Tue May 28 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3.7-3
- Require dbus-glib

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.3.7-1
- 0.3.7

* Fri Oct 13 2023 Daniel Rusek <mail@asciiwolf.com> - 0.3.6-7
- Fixed TBB archive name format

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.6-5
- Rebuilt for Python 3.12

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.6-4
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.3.6-2
- BR setuptools.

* Wed Dec 14 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.3.6-1
- 0.3.6

* Mon Dec 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.3.5-7
- URL patch

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.5-5
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 02 2021 Łukasz Patron <priv.luk@gmail.com> - 0.3.5-3
- Add patch to fix startup with Python 3.10

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.3.5-1
- 0.3.5

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.3.3-2
- Require python3-packaging

* Wed Oct 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.3.3-1
- 0.3.3

* Wed Sep 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-17
- Fix version comparison.

* Tue Sep 08 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-16
- Update upstream key.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-14
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-13
- Make intel-only, to match torbrowser builds available.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-11
- Correct two appdata tags.

* Wed Oct 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-10
- Fix appdata.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Sep 05 2019 Bhavin Gandhi <bhavin7392@gmail.com> - 0.3.2-8
- Use correct commit id of v0.3.2

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-7
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-6
- Patch setup to honor prefix.

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-5
- Appdata fix.

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-4
- Create appdata dir.

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-3
- Validate desktop files in build.

* Thu Jul 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-2
- Cleanup.

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.2-1
- 0.3.2

* Mon Apr 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.1-7
- Fix appdata filename.

* Fri Mar 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.3.1-6
- Switch to python3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-4
- Require python2 variants of packages explicitly.

* Wed Jan 09 2019 Gwyn Ciesla <limburgher@gmail.com> - 0.3.1-3
- Require python2-requests.

* Tue Jan 08 2019 Gwyn Ciesla <limburgher@gmail.com> - 0.3.1-2
- Fix dependencies.

* Wed Dec 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.3.1-1
- 0.3.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.9-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 13 2018 Robert Mayr <robyduck@fedoraoproject.org> 0.2.9-1
- Updated AppStream metadata
- Add appdata check

* Mon Aug 07 2017 Robert Mayr <robyduck@fedoraoproject.org> 0.2.8-1
- Automatically refresh GPG keyring, to prevent signature verification false positives
- Improve GnuPG code by using GPGME if available
- Added Czech, Hungarian localization

* Fri Feb 03 2017 Robert Mayr <robyduck@fedoraoproject.org> 0.2.7-1
- Updated Tor Browser signing key because they added a new subkey and verification was failing
- Improved localization, and added Russian

* Thu Aug 11 2016 Robert Mayr <robyduck@fedoraoproject.org> 0.2.6-1
- Fix issue where Tor Browser Launcher failed to launch if currently installed version
  of Tor Browser was too old
- Fixed bug related to fallback to English feature that caused Settings to crash

* Mon Mar 14 2016 Robert Mayr <robyduck@fedoraoproject.org> 0.2.4-1
- Fix signature verification bypass attack, reported by Jann Horn

* Sat Mar 05 2016 Robert Mayr <robyduck@fedoraoproject.org> 0.2.3-1
- Removed certificate pinning to https://www.torproject.org to avoid issues with upcoming
  certificate change, and hard-coded minimum Tor Browser version in the release
- Fix issue with detecting language
- Make Tor SOCKS5 proxy configurable, for users not running on 9050
- Added translations
- Switched from xpm icons to png icons
- Changed "Exit" button to "Cancel" button
- New package description

* Sat Nov 14 2015 Robert Mayr <robyduck@fedoraoproject.org> 0.2.2-1
- Torbrowser Launcher no longer attempts to auto-update, now that Tor Browser has this feature
- System Tor is now an optional dependency
- Fix issue where downloads fail because of unicode URLs
- Removed window management code that stopped working many releases ago, and removed wmctrl dependency
- Removed test code that caused signature verification to happen at the wrong time

* Sat Nov 07 2015 Robert Mayr <robyduck@fedoraoproject.org> 0.2.1-1
- Stop using RecommendedTBBVersions and start using more reliable "release" channel XML
- Converted settings file from pickle format to JSON
- Download tarball signatures to verify, rather than SHA256SUMS and signature

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Robert Mayr <robyduck@fedoraoproject.org> 0.2.0-1
- bump release to version 0.2.0
- no need to set active flags in settings
- Added better support for updating over Tor
- Print less console output

* Mon Mar 02 2015 Robert Mayr <robyduck@fedoraoproject.org> 0.1.9-2
- bump release to version 0.1.9
- fix bug when firefox browser is already open
- don't check for updates at first install

* Wed Feb 25 2015 Robert Mayr <robyduck@fedoraoproject.org> 0.1.8-1
- downgrade to latest working version and fix minor bugs
- Import new TBB GPG keys for download
- fix insane spec file and changelog

* Sat Jan 24 2015 Robert Mayr <robyduck@fedoraoproject.org> 0.1.9-1
- fix required txsocksx and service-identity
- bump to last version available

* Wed Nov 26 2014 Robert Mayr <robyduck@fedoraoproject.org> 0.1.7-1
- Fixes bug #1167576
- You can now pass URLs into TBL, and set it as your default browser
- Hides TBL window before launching TBB
- Default mirror switched to https://dist.torproject.org/
- Added AppData file to look better in software centers
- Exclude AppArmor profiles in Ubuntu, where they're broken

* Thu Nov 06 2014 Robert Mayr <robyduck@fedoraoproject.org> 0.1.6-3
- Fix broken dependencies bug

* Sat Oct 18 2014 Robert Mayr <robyduck@fedoraoproject.org> 0.1.6-2
- Remove shortcommit from spec file

* Thu Oct 16 2014 Robert Mayr <robyduck@fedoraoproject.org> 0.1.6-1
- Fixed bug related to TBB 4.0's new folder structure
- Updated .desktop files to comply with standards
- Updated licensing confusion to just be MIT in all locations

* Sun Oct 12 2014 Robert Mayr <robyduck@fedoraoproject.org> 0.1.5-3
- Remove apparmor and bump release

* Sat Oct 11 2014 Robert Mayr <robyduck@fedoraoproject.org> 0.1.5-2
- License fix and Source URL commit

* Fri Oct 10 2014 Robert Mayr <robyduck@fedoraoproject.org> 0.1.5-1
- Initial package for Fedora
