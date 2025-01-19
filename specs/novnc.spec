Name:           novnc
Version:        1.5.0
Release:        2%{?dist}
Summary:        VNC client using HTML5 (Web Sockets, Canvas) with encryption support
Requires:       python3-websockify
Requires:       which

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/novnc/noVNC
Source0:        https://github.com/novnc/noVNC/archive/%{name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  python3-devel

%description
noVNC is both a HTML VNC client JavaScript library and an application built on
top of that library. noVNC runs well in any modern browser including mobile
browsers (iOS and Android).

%prep
%setup -q -n noVNC-%{version}

%build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/
cp -r * %{buildroot}/%{_datadir}/%{name}/

# Drop snap related files from the main package
rm -rf %{buildroot}/%{_datadir}/%{name}/snap/

# Drop tests from the main package
rm -rf %{buildroot}/%{_datadir}/%{name}/tests/

# Drop utils from the main package
rm -rf %{buildroot}/%{_datadir}/%{name}/utils/

# Drop some po utilities from the main package
rm %{buildroot}/%{_datadir}/%{name}/po/Makefile
rm %{buildroot}/%{_datadir}/%{name}/po/po2js
rm %{buildroot}/%{_datadir}/%{name}/po/xgettext-html

# provide an index file to prevent default directory browsing
install -m 444 vnc.html %{buildroot}/%{_datadir}/%{name}/index.html

# install a copy of the new vnc_lite.html page as the old <1.0.0 vnc_auto.html page
install -m 444 vnc_lite.html %{buildroot}/%{_datadir}/%{name}/vnc_auto.html

# Install novnc_proxy and the legacy novnc_server
mkdir -p %{buildroot}/%{_bindir}/
install utils/novnc_proxy  %{buildroot}/%{_bindir}/%{name}_server
install utils/novnc_proxy  %{buildroot}/%{_bindir}/%{name}_proxy

# Install the man page for both
mkdir -p %{buildroot}/%{_mandir}/man1/
install docs/novnc_proxy.1 %{buildroot}/%{_mandir}/man1/%{name}_proxy.1
install docs/novnc_proxy.1 %{buildroot}/%{_mandir}/man1/%{name}_server.1

%files
%{_datadir}/%{name}
%{_bindir}/%{name}_server
%{_bindir}/%{name}_proxy
%{_mandir}/man1/%{name}_proxy.1.gz
%{_mandir}/man1/%{name}_server.1.gz
%doc README.md LICENSE.txt docs/API.md docs/EMBEDDING.md docs/LIBRARY.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 22 2024 Jonathan Wright <jonathan@almalinux.org> - 1.5.0-1
- update to 1.5.0

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.0-1
- Update to 1.4.0 rhbz#2239160

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.3.0-5
- Add require on 'which' rhbz#2150521

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Lee Yarwood <lyarwood@redhat.com> - 1.3.0-2
- Add novnc_proxy and associated man pages
- Drop various utilities, tests and other files not required from the package
- Add docs/API.md docs/EMBEDDING.md docs/LIBRARY.md as docs

* Thu Nov 04 2021 Lee Yarwood <lyarwood@redhat.com> - 1.3.0-1
- New upstream release 1.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Lee Yarwood <lyarwood@redhat.com> - 1.2.0-2
- Drop py2 support

* Tue Aug 25 2020 Lee Yarwood <lyarwood@redhat.com> - 1.2.0-1
- New upstream release 1.2.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 Lee Yarwood <lyarwood@redhat.com> 1.1.0-6
- Drop use of pathfix for py2 builds.

* Fri Aug 09 2019 Lee Yarwood <lyarwood@redhat.com> 1.1.0-5
- Make the spec compatible for both py2 and py3.

* Fri Aug 09 2019 Lee Yarwood <lyarwood@redhat.com> 1.1.0-4
- Fix bogus changelog date.

* Thu Aug 08 2019 Lee Yarwood <lyarwood@redhat.com> 1.1.0-3
- launch.sh: Check for a local websockify directory

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Lee Yarwood <lyarwood@redhat.com> - 1.1.0-1
- Update to 1.1.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Lee Yarwood <lyarwood@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Lon Hohberger <lon@redhat.com> 0.6.1-1
- Rebase to upstream 0.6.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Solly Ross <sross@redhat.com> - 0.5.1-2
- Update Source0 to point to correct URL

* Sat Jan 10 2015 Alan Pevec <apevec@redhat.com> - 0.5.1-1
- update to the new upstream version, for changes since 0.4 see:
  https://github.com/kanaka/noVNC/releases/tag/v0.5
  https://github.com/kanaka/noVNC/releases/tag/v0.5.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Nikola Đipanov <ndipanov@redhat.com> - 0.4-7
- Remove the openstack-nova-novncproxy subpackage (moved to openstack-nova)

* Mon Apr 08 2013 Nikola Đipanov <ndipanov@redhat.com> - 0.4-6
- Import config module from oslo in nova-novncproxy

* Mon Mar 18 2013 Nikola Đipanov <ndipanov@redhat.com> - 0.4-5
- Change FLAGS to the new CONF module in nova-novncproxy
- Drop the hard dwp on whole nova package and require only nova-common

* Thu Feb 28 2013 Pádraig Brady <P@draigBrady.com> - 0.4-4
- Support /etc/sysconfig/openstack-nova-novncproxy #916479

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Nikola Đipanoov <ndipanov@redhat.com> - 0.4-2
- Fixes the supplied init script to match the new 0.4 version

* Mon Oct 22 2012 Nikola Đipanoov <ndipanov@redhat.com> - 0.4-1
- Moves to upstream version 0.4.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Till Maas <opensource@till.name> - 0.3-11
- Add a dependency for novnc on python-websockify

* Fri Jun 15 2012 Jose Castro Leon <jose.castro.leon@cern.ch> - 0.3-10
- Add a dependency for openstack-nova-novncproxy on openstack-nova

* Thu Jun 14 2012 Matthew Miller <mattdm@mattdm.org> - 0.3-9
- Remove a dependency for openstack-nova-novncproxy on numpy

* Wed Jun 13 2012 Alan Pevec <apevec@redhat.com> - 0.3-8
- Add a dependency for openstack-nova-novncproxy on python-nova

* Wed Jun 13 2012 Jose Castro Leon <jose.castro.leon@cern.ch> - 0.3-7
- Add a dependency for openstack-nova-novncproxy on novnc

* Mon Jun 11 2012 Adam Young <ayoung@redhat.com> - 0.3-6
- systemd initialization for Nova Proxy
- system V init script
- remove Flash binary supporting older browsers

* Fri Jun 8 2012 Adam Young <ayoung@redhat.com> - 0.3-3
- Added man pages
- novnc_server usese the websockify executable, not wsproxy.py

* Thu Jun 7 2012 Adam Young <ayoung@redhat.com> - 0.3-2
- Make Javascript files non-executable, as they are not script files
- Patch Nova noVNC proxy to use websockify directly

* Tue May 15 2012 Adam Young <ayoung@redhat.com> - 0.3-1
- Added in support for the Nova noVNC proxy
- Added files for the images and inclues subdirectories

* Thu May 10 2012 Adam Young <ayoung@redhat.com> - 0.2
- Initial RPM release.
