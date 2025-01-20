Name:           qgit
Version:        2.10
Release:        9%{?dist}
Summary:        GUI browser for git repositories

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/tibirna/qgit
Source0:        https://github.com/tibirna/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libappstream-glib
Requires:       git-core >= 1.4.0

%description
With qgit you are able to browse revisions history, view patch content
and changed files, graphically following different development branches.

%prep
%setup -q -n %{name}-%{name}-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install

# appdata handling
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml


%files
%doc README.adoc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.10-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 11 2022 Dan Horák <dan[at]danny.cz> - 2.10-1
- Update to the new upstream version 2.10

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 27 2021 Pino Toscano <ptoscano@redhat.com> - 2.9-6
- Drop compatibility with RHEL 7, no more needed at this point
- Drop our local application icon, as upstream installs it already
- Drop our local desktop file, as upstream installs it already
- Stop moving the appdata file to /usr/share/appdata, as this location is
  legacy and deprecated

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Dan Horák <dan[at]danny.cz> - 2.9-1
- Update to the new upstream version 2.9 (#1763542)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Dan Horák <dan[at]danny.cz> - 2.8-2
- Fix EPEL-7 build

* Mon Jul 16 2018 Dan Horák <dan[at]danny.cz> - 2.8-1
- Update to the new upstream version 2.8

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Dan Horák <dan[at]danny.cz> - 2.7-1
- Update to the new upstream version 2.7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Dan Horák <dan[at]danny.cz> - 2.6-4
- Fix custom actions (#1411191)

* Mon Aug 22 2016 Dan Horák <dan[at]danny.cz> - 2.6-3
- Fix handling of unappllied StGit patches (#1367575)

* Thu Jun 30 2016 Ville Skyttä <ville.skytta@iki.fi> - 2.6-2
- Patch to build with $RPM_OPT_FLAGS (#1351438)

* Sun Apr 24 2016 Luigi Toscano <luigi.toscano@tiscali.it> - 2.6-1
- Update to the new upstream version 2.6 (#1336144)

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.5-8
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.5-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Nov 27 2014 Dan Horák <dan[at]danny.cz> - 2.5-5
- cleanup spec

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Dan Horák <dan[at]danny.cz> - 2.5-1
- update to 2.5

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.4-6
- iremove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 14 2012 Dan Horák <dan[at]danny.cz> - 2.4-4
- fix line skew (#823176)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 01 2011 Dan Horák <dan[at]danny.cz> - 2.4-1
- update to 2.4
- switched to new upstream

* Fri May 27 2011 Dan Horák <dan[at]danny.cz> - 2.3-4
- update for git 1.7.5 (#708251)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 10 2009 Dan Horak <dan[at]danny.cz> 2.3-1
- update to upstream version 2.3

* Sat Feb 28 2009 Dan Horak <dan[at]danny.cz> 2.2-4
- update desktop file for recent standards

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 25 2008 Dan Horak <dan[at]danny.cz> 2.2-2
- shorten Summary

* Thu Jul 17 2008 Dan Horak <dan[at]danny.cz> 2.2-1
- update to upstream version 2.2

* Sun Feb 10 2008 Dan Horak <dan[at]danny.cz> 2.1-3
- rebuild for gcc 4.3

* Mon Dec 31 2007 Dan Horak <dan[at]danny.cz> 2.1-2
- add missing patch

* Mon Dec 31 2007 Dan Horak <dan[at]danny.cz> 2.1-1
- update to upstream version 2.1

* Sat Sep  8 2007 Dan Horak <dan[at]danny.cz> 1.5.7-1
- update to upstream version 1.5.7
- fixes #268381

* Tue Aug 21 2007 Dan Horak <dan[at]danny.cz> 1.5.6-2
- update license tag
- rebuild for F8

* Fri May 25 2007 Dan Horak <dan[at]danny.cz> 1.5.6-1
- update to upstream version 1.5.6

* Mon Apr  9 2007 Dan Horak <dan[at]danny.cz> 1.5.5-2
- added an icon for the desktop file

* Sun Feb 25 2007 Dan Horak <dan[at]danny.cz> 1.5.5-1
- update to upstream version 1.5.5

* Fri Dec 29 2006 Dan Horak <dan[at]danny.cz> 1.5.4-1
- update to upstream version 1.5.4

* Sat Nov 11 2006 Dan Horak <dan[at]danny.cz> 1.5.3-1
- update to upstream version 1.5.3

* Sat Sep 30 2006 Dan Horak <dan[at]danny.cz> 1.5.2-1
- update to upstream version 1.5.2

* Tue Sep 12 2006 Dan Horak <dan[at]danny.cz> 1.5.1-1
- update to upstream version 1.5.1

* Sat Sep  9 2006 Dan Horak <dan[at]danny.cz> 1.5-1
- update to upstream version 1.5

* Fri Sep  1 2006 Dan Horak <dan[at]danny.cz> 1.4-3
- rebuild for FC6

* Sun Jul 16 2006 Dan Horak <dan@danny.cz> 1.4-2
- remove the patch also from the spec file

* Sun Jul 16 2006 Dan Horak <dan@danny.cz> 1.4-1
- update to upstream version 1.4
- remove the patch as upstream reverted the linking behaviour
- requires git-core >= 1.4.0

* Sun Jun 11 2006 Dan Horak <dan@danny.cz> 1.3-2
- added patch for creating of usable debug package (#194782)

* Mon Jun 05 2006 Dan Horak <dan@danny.cz> 1.3-1
- update to upstream version 1.3

* Sat Apr 29 2006 Dan Horak <dan@danny.cz> 1.2-1
- update to upstream version 1.2

* Sun Mar 19 2006 Dan Horak <dan@danny.cz> 1.1.1-1
- update to upstream version 1.1.1

* Tue Mar  7 2006 Dan Horak <dan@danny.cz> 1.1-2
- change requires from git to git-core only

* Sun Feb 19 2006 Dan Horak <dan@danny.cz> 1.1-1
- updated to upstream version 1.1
- fixed download URL for Source0 from sourceforge.net
- requires git >= 1.2.0

* Sat Feb 11 2006 Dan Horak <dan@danny.cz> 1.1-0.1.rc3.3
- added docs

* Sat Feb 11 2006 Dan Horak <dan@danny.cz> 1.1-0.1.rc3.2
- added desktop file

* Wed Feb  8 2006 Dan Horak <dan@danny.cz> 1.1-0.1.rc3.1
- first version
