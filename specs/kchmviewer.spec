Name:           kchmviewer
Version:        8.0
%global _tag RELEASE_%(echo %{version} | sed 's/\\./_/g')
%global _appid net.%{name}.%{name}
Release:        11%{?dist}
Summary:        CHM viewer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.kchmviewer.net/
Source0:        https://github.com/gyunaev/%{name}/archive/refs/tags/%{_tag}.tar.gz#/%{name}-%{_tag}.tar.gz
# applied in upstream git 9ac73e7ad15de08aab6b1198115be2eb44da7afe
Patch0:         0001-Custom-URL-scheme-registration-needs-to-be-applied-o.patch
# applied in upstream git a4a3984465cb635822953350c571950ae726b539
Patch1:         0001-Only-add-Webkit-stuff-to-QT-if-we-re-compiling-under.patch
# https://github.com/gyunaev/kchmviewer/pull/17
Patch2:         0001-Rename-the-desktop-entry-file-to-match-the-applicati.patch
Provides:       %{name}-qt = %{version}-%{release}
Obsoletes:      %{name}-qt < 7.3

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  chmlib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libzip-devel
BuildRequires:  qt5-qtwebengine-devel
ExclusiveArch:  %{qt5_qtwebengine_arches}

Requires: %{name}-common = %{version}-%{release}

%description
KchmViewer is a chm (MS HTML help file format) viewer.

This package contains the Qt-only version.

%package common
Summary: Common data files for KchmViewer
BuildArch: noarch
Requires: hicolor-icon-theme
%description common
Common data files for KchmViewer.

%prep
%autosetup -p1 -n %{name}-%{_tag}

%build
# make the Qt-only version
%qmake_qt5
%make_build

%install
# install the Qt-only version
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -p bin/%{name} $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications packages/%{_appid}.desktop
install -Dpm 644 packages/%{name}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%check

%files
%{_bindir}/kchmviewer
%{_datadir}/applications/%{_appid}.desktop

%files common
%doc README ChangeLog FAQ
%license COPYING
%{_datadir}/icons/hicolor/*/apps/kchmviewer.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 8.0-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Robin Lee <cheeselee@fedoraproject.org> - 8.0-1
- Update to 8.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Robin Lee <cheeselee@fedoraproject.org> - 7.7-1
- Update to 7.7 (RHBZ#1382189)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 7.5-8
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Remi Collet <remi@fedoraproject.org> - 7.5-5
- rebuild for new libzip

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 7.5-2
- use %%qmake_qt5 to ensure proper build flags

* Sun Nov 15 2015 Robin Lee <cheeselee@fedoraproject.org> - 7.5-1
- Update to 7.5
- Build with qt5

* Sun Oct 11 2015 Robin Lee <cheeselee@fedoraproject.org> - 7.3-1
- Update to 7.3
- Build only the qt version, since kde4 is obsolete in Fedora and kchmviewer
  no longer uses KHTML
- BR added: gcc-c++, qt4-devel; BR removed: perl, openssl-devel, phonon-devel

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 7.1-4
- rebuild for new libzip

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 7.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Nov  2 2014 Robin Lee <cheeselee@fedoraproject.org> - 7.1-2
- BR: qtwebkit-devel

* Sun Nov  2 2014 Robin Lee <cheeselee@fedoraproject.org> - 7.1-1
- Update to 7.1
- BR: perl, openssl-devel, phonon-devel, libzip-devel

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Robin Lee <cheeselee@fedoraproject.org> - 6.0-1
- Update to 6.0
- Remove Requires kio_msits and kchmviewer-5.1-no_msits.patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 15 2011 Robin Lee <cheeselee@fedoraproject.org> - 5.3-1
- Update to 5.3
- Remove kchmviewer-5.2-missed-src.patch

* Tue Oct 12 2010 Robin Lee <cheeselee@fedoraproject.org> - 5.2-5
- _smp_mflags will break compilation of the Qt version, remove it

* Mon Oct 11 2010 Robin Lee <cheeselee@fedoraproject.org> - 5.2-4
- Make a subpackage for the Qt-only version
- Make a subpackage owning the common data files

* Fri Jun  4 2010 Robin Lee <robinlee.sysu@gmail.com> - 5.2-3
- fix tag

* Fri Jun  4 2010 Robin Lee <robinlee.sysu@gmail.com> - 5.2-2
- Tar ball updated

* Wed Apr 28 2010 Robin Lee <robinlee.sysu@gmail.com> - 5.2-1
- update to 5.2

* Sat Apr 17 2010 LI Rui Bin <cheeseli@hotmail.com> - 5.1-1
- correct License tag
- remove BuildRoot tag

* Fri Mar 19 2010 Emilio Scalise <emisca@rocketmail.com> - 5.1-0
- update to 5.1
- provides new translations

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.0-4
- fix conflicts with kdegraphics (#484861)
- optimize scriptlets
- ship only hicolor icons
- cleanup, use kde4-macros

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  8 2008 Patrice Dumas <pertusus@free.fr> 4.0-2
- reenable kde support

* Thu Dec  4 2008 Patrice Dumas <pertusus@free.fr> 4.0-1
- update to 4.0

* Wed Aug 13 2008 Patrice Dumas <pertusus@free.fr> 4.0-0.4.beta3
- update to 4.0beta3

* Thu Feb 14 2008 Patrice Dumas <pertusus@free.fr> 4.0-0.2.beta2
- update to 4.0beta2

* Thu Aug  2 2007 Patrice Dumas <pertusus@free.fr> 3.1-1.5
- update to 3.1

* Sun Apr  1 2007 Patrice Dumas <pertusus@free.fr> 3.0-2
- update to 3.0

* Fri Feb 16 2007 Patrice Dumas <pertusus@free.fr> 2.7-2
- fixes in desktop file. Fix #229070

* Mon Jan 29 2007 Patrice Dumas <pertusus@free.fr> 2.7-1
- update to 2.7

* Tue Sep 12 2006 Patrice Dumas <pertusus@free.fr> 2.6-2
- rebuild for FC6

* Sat Jul 22 2006 Patrice Dumas <pertusus@free.fr> 2.6-1
- update to 2.6
- remove upstreamed patch kchmviewer-2.5-iconstorage.h.patch

* Thu May 18 2006 Patrice Dumas <pertusus@free.fr> 2.5-1
- update to 2.5
- patch from Jose Pedro Oliveira (jpo)

* Tue May 16 2006 Patrice Dumas <pertusus@free.fr> 2.0-4
- remove the old menu entry file from /usr/share/applnk/

* Mon Mar 13 2006 Patrice Dumas <pertusus@free.fr> 2.0-3
- use update-desktop-database

* Mon Mar 13 2006 Patrice Dumas <pertusus@free.fr> 2.0-2
- enable kde support

* Sun Mar 12 2006 Patrice Dumas <pertusus@free.fr> 2.0-1
- Fedora Extras submission
