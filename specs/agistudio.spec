Name: agistudio
Version: 1.3.0
Release: 33%{?dist}
Summary: AGI integrated development environment
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Patch0: agistudio-1.3.0-format.patch
URL: http://agistudio.sourceforge.net/

BuildRequires: qt4-devel desktop-file-utils
BuildRequires: make
#Requiring nagi, needed at runtime, not picked up by rpm.
Requires: hicolor-icon-theme, nagi, gtk2

%description
AGI (Adventure Game Interpreter) is the adventure game engine used by
Sierra On-Line to create some of their early games. QT AGI Studio
is a program which allows you to view, create and edit AGI games.

%prep

%setup -q

%patch -P0 -p0

%build
CXXFLAGS="$RPM_OPT_FLAGS $CXXFLAGS -std=gnu++98 -fPIC"
export CXXFLAGS
cd src
%{qmake_qt4}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio
install -m 755 src/agistudio %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/agistudio/template
mkdir -p %{buildroot}%{_datadir}/agistudio/help
install -p -m 0644 help/* %{buildroot}%{_datadir}/agistudio/help
cp -pr template/* %{buildroot}%{_datadir}/%{name}/template 

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644  src/app_icon.xpm %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

# desktop file
desktop-file-install  \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE1}

%files
%doc COPYING README relnotes help/*
%{_bindir}/agistudio
%{_datadir}/agistudio/
%{_datadir}/applications/agistudio.desktop
%{_datadir}/icons/hicolor/32x32/apps/agistudio.xpm

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-28
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-15
- Remove obsolete scriptlets

* Mon Aug 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-14
- Patch for format string error.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 24 2016 Jon Ciesla <limburgher@gmail.com> - 1.3.0-10
- Respect RPM_OPT_FLAGS

* Mon Feb 22 2016 Jon Ciesla <limburgher@gmail.com> - 1.3.0-9
- Fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-7
- use %%qmake_qt4 macro to ensure proper build flags

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 03 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.0-1
- Latest upstream.

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.2.4-8
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- drop all unapplied patches

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Jon Ciesla <limb@jcomserv.net> - 1.2.4-5
- Explicitly require gtk2 for gtk-update-icon-cache, BZ 715416.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 26 2009 Jon Ciesla <limb@jcomserv.net> - 1.2.4-2
- Explicitly require nagi.

* Wed Apr 08 2009 Jon Ciesla <limb@jcomserv.net> - 1.2.4-1
- New upstream, dropping relevant patches.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Jon Ciesla <limb@jcomserv.net> - 1.2.3-8
- Description fix.

* Mon Mar 24 2008 Jon Ciesla <limb@jcomserv.net> - 1.2.3-7
- qt3 BR rename fix.

* Fri Feb 08 2008 Jon Ciesla <limb@jcomserv.net> - 1.2.3-6
- GCC 4.3 rebuild.

* Thu Jan 03 2008 Jon Ciesla <limb@jcomserv.net> - 1.2.3-5
- Fixed cstdlib, string.h includes.

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> - 1.2.3-4
- Corrected license tag.

* Tue May 29 2007 Jon Ciesla <limb@jcomserv.net> - 1.2.3-3
- Added disttag.

* Thu May 24 2007 Jon Ciesla <limb@jcomserv.net> - 1.2.3-2
- Preserved timestamps where possible.
- Added help to docs.

* Fri Apr 27 2007 Jon Ciesla <limb@jcomserv.net> - 1.2.3-1
- Initial packaging very loosely based on .spec provided in upstream tarball.
