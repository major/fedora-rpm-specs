%global debug_package %{nil}

Name:		pinta
Version:	1.7.1
Release:	10%{?dist}
Summary:	An easy to use drawing and image editing program

# the code is licensed under the MIT license while the icons are licensed as CC-BY
# Automatically converted from old format: MIT and CC-BY - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:		http://pinta-project.com/

Source0:	http://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz

# Mono only available on these:
ExclusiveArch:	%mono_arches

# Pinta fails to build on armv7hl. Mono crashes.
# https://bugzilla.redhat.com/show_bug.cgi?id=1869214
ExcludeArch:	armv7hl

BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	mono-devel
BuildRequires:	mono-addins-devel
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
Requires:	hicolor-icon-theme
Requires:	mono-addins

%description
Pinta is an image drawing/editing program.
It's goal is to provide a simplified alternative to GIMP for casual users.

%prep
%setup -q


%build
%configure
%make_build


%install
%make_install

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%find_lang %name


%files -f %{name}.lang
%license license-mit.txt license-pdn.txt
%doc readme.md
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%exclude %{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/man/man1/%{name}*
%{_datadir}/pixmaps/%{name}*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.1-9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Andrea Musuruane <musuruan@gmail.com> - 1.7.1-1
- Updated to new upstream release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Andrea Musuruane <musuruan@gmail.com> - 1.7-2
- Exclude building on armv7hl (BZ #1869214)

* Sun Aug 09 2020 Andrea Musuruane <musuruan@gmail.com> - 1.7-1
- Updated to new upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Andrea Musuruane <musuruan@gmail.com> - 1.6-15
- Rebuilt (BZ #1755274)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 1.6-11
- Added gcc dependency
- Added license tag
- Used new AppData directory
- Removed obsolete scriptlets
- Spec file clean up

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Timotheus Pokorra <tpokorra@fedoraproject.org> 1.6-3
- More fixes for mono4

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.6-2
- Rebuild (mono4)

* Sat Mar 28 2015 Andrea Musuruane <musuruan@gmail.com> - 1.6-1
- Updated to v1.6
- Minor cleanup

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.5-2
- Add an AppData file for the software center

* Mon Oct 27 2014 Andrea Musuruane <musuruan@gmail.com> 1.5-1
- Updated to v1.5
- Updated Source0 tag
- Dropped obsolete Group tags
- Pinta doesn't build on arm (#992798)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Paul Lange <palango@gmx.de> - 1.4-1
- Update to 1.4

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Paul Lange <palango@gmx.de> - 1.3-1
- update to 1.3

* Wed Apr 18 2012 Paul Lange <palango@gmx.de> - 1.2-1
- update to 1.2

* Sat Feb 18 2012 Paul Lange <palango@gmx.de> - 1.1-4
- correct path in bin/pinta

* Sat Feb 11 2012 Paul Lange <palango@gmx.de> - 1.1-3
- Update libdir

* Fri Feb 10 2012 Paul Lange <palango@gmx.de> - 1.1-2
- Add intltool to BuildRequires

* Fri Feb 10 2012 Paul Lange <palango@gmx.de> - 1.1-1
- Update to 1.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 28 2011 Paul Lange <palango@gmx.de> - 1.0-1
- Upload right sources

* Tue Apr 19 2011 Dan Horák <dan[at]danny.cz> - 0.8-2
- updated the supported arch list

* Wed Apr 06 2011 Paul Lange <palango@gmx.de> - 0.8-1
- Update to version 0.8

* Thu Mar 03 2011 Paul Lange <palango@gmx.de> - 0.7-1
- Update to version 0.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Paul Lange <palango@gmx.de> - 0.6-1
- Update to version 0.6

* Thu Dec 09 2010 Paul Lange <palango@gmx.de> - 0.5-6
- Upload right sources

* Thu Dec 09 2010 Paul Lange <palango@gmx.de> - 0.5-5
- Fix build for x86_64

* Wed Dec 08 2010 Paul Lange <palango@gmx.de> - 0.5-4
- Fix issues from review

* Sun Dec 05 2010 Paul Lange <palango@gmx.de> - 0.5-3
- Fix build for x86_64

* Wed Dec 01 2010 Paul Lange <palango@gmx.de> - 0.5-2
- Fix rpmlint warnings

* Sat Nov 20 2010 Paul Lange <palango@gmx.de> - 0.5-1
- update to version 0.5

* Sun Aug 01 2010 Paul Lange <palango@gmx.de> - 0.4-3
- Fix links in /bin
- Improve patch naming and add upstream links
- Fix mimetype patch

* Thu Jul 29 2010 Paul Lange <palango@gmx.de> - 0.4-2
- Fix icon cache handling
- Add some Requires and BuildRequires
- Add docs
- Add patches from debian

* Sat May 08 2010 Paul Lange <palango@gmx.de> - 0.4-1
- Initial packaging
