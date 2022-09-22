# force out-of-tree build for spec compatibility with older releases
%undefine __cmake_in_source_build

Name:		brewtarget
Version:	2.1.0
Release:	20%{?dist}
Summary:	An open source beer recipe creation tool
License:	GPLv3 and WTFPL and LGPLv2
URL:		http://www.brewtarget.org
Source0:    https://github.com/Brewtarget/brewtarget/archive/v%{version}.tar.gz 
BuildRequires:	cmake
BuildRequires:	qt-devel
BuildRequires:	qt-webkit-devel
BuildRequires:	phonon-devel
BuildRequires:	desktop-file-utils
Requires:  sqlite

%description
Brewtarget is an open source beer recipe creation tool. It automatically 
calculates color, bitterness, and other parameters for you while you drag and 
drop ingredients into the recipe. Brewtarget also has many other tools such as 
priming sugar calculators, OG correction help, and a unique mash designing tool. 
It also can export and import recipes in BeerXML.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake -DDO_RELEASE_BUILD:BOOL=ON 
%cmake_build

%install
%cmake_install
/usr/bin/install -m 0644 -Dp doc/brewtarget.1 %buildroot%{_mandir}/man1/brewtarget.1

%check
desktop-file-validate %buildroot%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}*
%{_mandir}/man1/brewtarget.1*
%doc CHANGES.markdown README.markdown COPYRIGHT COPYING.GPLv3 COPYING.WTFPL doc/brewtarget-manual.html 



%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Kevin Fenzi <kevin@scrye.com> - 2.1.0-13
- Fix FTBFS bug #1734987

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 12 2014 Pete Travis <me@petetravis.com> - 2.1.0-2
- Update to upstream 2.1.0
- Adds inventory tracking for ingredients
- Folders for organizing recipes
- Recipe parameter sliders
- Various bugfixes, ref http://www.brewtarget.org/changelog.html

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 17 2014 Pete Travis <immanetize@fedoraproject.org> - 2.0.2-1
- Update to version 2.0.2
- Mostly a bugfix release, see http://www.brewtarget.org/changelog.html

* Sat Aug 03 2013 Pete Travis <immanetize@fedoraproject.org> - 2.0.1-2
- Update to version 2.0.1
- Removing patches where integrated upstream
- patch for unversioned docdirs on Fedora releases >= 20

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 18 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.3-4
- Fixing permissions on manpage

* Sat Nov 17 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-3
- Including bundled manpage, updating SPEC

* Fri Nov 16 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-2
- Changes to SPEC file per packaging guidelines.

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Initial build of 1.2.5 release

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Added patch to correct .desktop file

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Added patch to install documentation to appropriate directory

* Mon Nov 12 2012 Pete Travis <immanetize@fedoraproject.org> 1.2.5-1
- Patching to warn if no documentation instead of exit.

