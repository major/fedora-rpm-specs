Name:           roxterm
Version:        3.15.2
Release:        2%{?dist}
Summary:        Terminal emulator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/realh/roxterm
Source0:        https://github.com/realh/roxterm/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  dbus-glib-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  vte291-devel
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/xsltproc

%description
ROXTerm is a terminal emulator intended to provide similar features to
gnome-terminal, based on the same VTE library. It is more configurable than
gnome-terminal and aimed more at "power" users who make heavy use of terminals.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/roxterm.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/roxterm.desktop

%files
%doc %{_pkgdocdir}
%license COPYING
%{_bindir}/roxterm
%{_bindir}/roxterm-config
%{_datadir}/metainfo/roxterm.metainfo.xml
%{_datadir}/applications/roxterm.desktop
%{_datadir}/roxterm/
%{_datadir}/icons/hicolor/scalable/apps/roxterm.svg
%{_mandir}/man1/roxterm*.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 02 2024 Pete Walter <pwalter@fedoraproject.org> - 3.15.2-1
- Update to 3.15.2

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.14.3-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Pete Walter <pwalter@fedoraproject.org> - 3.14.3-1
- Update to 3.14.3

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 19 2023 Pete Walter <pwalter@fedoraproject.org> - 3.13.1-1
- Update to 3.13.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Pete Walter <pwalter@fedoraproject.org> - 3.11.1-1
- Update to 3.11.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Pete Walter <pwalter@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1

* Tue Sep 01 2020 Than Ngo <than@redhat.com> - 3.8.5-4
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Pete Walter <pwalter@fedoraproject.org> - 3.8.5-1
- Update to 3.8.5

* Wed Feb 19 2020 Than Ngo <than@redhat.com> - 3.7.3-5
- Fixed FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Pete Walter <pwalter@fedoraproject.org> - 3.7.3-1
- Update to 3.7.3
- Update upstream URLs for the github switch
- Switch to cmake
- Use desktop-file-validate rather than desktop-file-install

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 09 2016 Pete Walter <pwalter@fedoraproject.org> - 3.3.2-2
- Spec file clean up

* Sat Feb 20 2016 Christopher Meng <rpm@cicku.me> - 3.3.2-1
- Update to 3.3.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 21 2015 Christopher Meng <rpm@cicku.me> - 3.1.5-1
- Update to 3.1.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 05 2015 Christopher Meng <rpm@cicku.me> - 2.9.7-1
- Update to 2.9.7

* Tue Jan 20 2015 Christopher Meng <rpm@cicku.me> - 2.9.5-1
- Update to 2.9.5

* Wed Aug 20 2014 Christopher Meng <rpm@cicku.me> - 2.9.3-1
- Update to 2.9.3

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Christopher Meng <rpm@cicku.me> - 2.9.1-1
- Update to 2.9.1

* Mon Jun 09 2014 Christopher Meng <rpm@cicku.me> - 2.8.3-1
- Update to 2.8.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Christopher Meng <rpm@cicku.me> - 2.8.2-2
- Add deprecated VTK3 option support.

* Wed Feb 19 2014 Christopher Meng <rpm@cicku.me> - 2.8.2-1
- Update to 2.8.2

* Tue Jan 28 2014 Christopher Meng <rpm@cicku.me> - 2.8.1-1
- Update to 2.8.1(#1055308)

* Fri Aug 23 2013 Dan Horák <dan[at]danny.cz> - 2.7.2-4
- modernize spec
- move to unversioned docdir (#993935)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Michel Salim <salimma@fedoraproject.org> - 2.7.2-2
- Properly apply optimization flags (#977149)

* Fri Jun 14 2013 Michel Salim <salimma@fedoraproject.org> - 2.7.2-1
- Update to 2.7.2

* Mon Feb 25 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.2-5
- Remove vendor from desktop files for F19+. https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.2-1
- Update to 2.2.2 (#743869)

* Wed Sep 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1 (#741887)

* Fri Sep 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.3-1
- Update to 2.1.3 (#739024)

* Thu Sep 15 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2 (#738600)

* Sat Sep 10 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1 (#732262)

* Tue Aug 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (#732262)
- Build against gtk3 and vte3

* Tue Aug 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.22.2-1
- Update to 1.22.2 (#732262)

* Sat Jul 16 2011 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.21.2-1
- Update to 1.21.2, fixes TERM variable setting (bz#719830)

* Mon Mar 28 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.21.1-1
- Update to 1.21.1
- Make GNOME 2 control-center integration conditional

* Wed Feb 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 1.20.5-2
- Temporarily disable GNOME control-center integration for
  https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  3 2011 Dan Horák <dan[at]danny.cz> - 1.20.5-1
- Update to 1.20.5

* Thu Dec 30 2010 Dan Horák <dan[at]danny.cz> - 1.20.4-1
- Update to 1.20.4

* Mon Dec 20 2010 Dan Horák <dan[at]danny.cz> - 1.20.2-1
- Update to 1.20.2

* Wed Oct 27 2010 Dan Horák <dan[at]danny.cz> - 1.19.4-1
- Update to 1.19.4

* Fri Jul 23 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.18.5-1
- Update to 1.18.5

* Mon Jun 21 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.18.4-1
- Update to 1.18.4

* Sun May 23 2010 Dan Horák <dan[at]danny.cz> - 1.18.3-1
- Update to 1.18.3

* Sun May  9 2010 Dan Horák <dan[at]danny.cz> - 1.18.2-1
- Update to 1.18.2

* Wed Mar 24 2010 Christoph Wickert <cwickert@fedoraproject.org> - 1.18.1-1
- Update to 1.18.1
- Build GNOME preferred apps integration
- BR xmlto for manpages and libSM-devel for session management
- Include new manpages and ChangeLog
- Drop README from %%doc as it only referred to index.html

* Wed Jan 06 2010 Sebastian Vahl <svahl@fedoraproject.org> - 1.17.1-1
- new upstream release: 1.17.1

* Tue Dec 22 2009 Sebastian Vahl <svahl@fedoraproject.org> - 1.16.3-1
- new upstream release: 1.16.3

* Tue Aug 11 2009 Sebastian Vahl <svahl@fedoraproject.org> - 1.15.2-1
- new upstream release: 1.15.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 1.14.2-2
- Rebuilt for libvte SONAME bump

* Thu Apr 16 2009 Sebastian Vahl <fedora@deadbabylon.de> - 1.14.2-1
- new upstream version: 1.14.2
- fix help link

* Fri Apr 10 2009 Sebastian Vahl <fedora@deadbabylon.de> - 1.14.1-1
- new upstream version: 1.14.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.13.0-1
- new upstream version: 1.13.0

* Sun Jun 22 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.12.1-2
- new upstream version: 1.12.2
- move menu entry to category "System"

* Fri May 23 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.12.1-1
- new upstream version: 1.12.1

* Tue May 20 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.12.0-1
- new upstream version: 1.12.0

* Mon Mar 31 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.11.1-1
- new upstream version: 1.11.1

* Sat Feb 09 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.10.1-1
- new upstream version: 1.10.1

* Wed Jan 23 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.10.0-1
- new upstream version: 1.10.0

* Wed Jan 02 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.9.1-1
- new upstream version: 1.9.1

* Tue Jan 01 2008 Sebastian Vahl <fedora@deadbabylon.de> - 1.9.0-1
- new upstream version: 1.9.0

* Thu Dec 13 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.8.1-1
- new upstream version: 1.8.1

* Mon Nov 12 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.8.0-1
- new upstream version: 1.8.0

* Wed Sep 19 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.7.4-4
- correct %%doc in spec

* Wed Sep 19 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.7.4-3
- own directories
- set %%{_docdir} to %%{name}-%%{version}

* Tue Sep 18 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.7.4-2
- use gtk-update-icon-cache in %%post and %%postun

* Tue Sep 18 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.7.4-1
- new upstream version: 1.7.4
- correct url

* Tue Sep 11 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.7.1-1
- new upstream version
- change license to GPLv2+
- BR: dbus-devel

* Tue May 15 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.5.1-2
- BR: dbus-glib-devel, desktop-file-utils

* Fri Mar 30 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.5.1-1
- new upstream version: 0.5.1

* Tue Feb 20 2007 Sebastian Vahl <fedora@deadbabylon.de> - 1.4.1-1
- Initial Release
