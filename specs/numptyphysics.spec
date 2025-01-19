%global commit c0abd473857106cd13459fe04f4444099e0d0b59
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           numptyphysics
# Last known version number
Version:        0.4
Release:        0.32.20151231git%{shortcommit}%{?dist}
Summary:        A crayon-drawing based physics puzzle game 

License:        GPL-3.0-or-later
URL:            http://thp.io/2015/numptyphysics/
Source0:        https://github.com/thp/numptyphysics/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/thp/numptyphysics/pull/17.patch#/%{name}-qsort.patch
Patch1:         include.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Provides:       bundled(Box2D) = 2.0.1
ExcludeArch:    ppc64le

%description
Harness gravity with your crayon and set about creating blocks, ramps,
levers, pulleys and whatever else you fancy to get the little red thing to
the little yellow thing.


%prep
%setup -q -n %{name}-%{commit}
%patch -P0 -p1
%patch -P1 -p1

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" make %{?_smp_mflags} V=1


%install
make install DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/numptyphysics.desktop


%files
%{_bindir}/numptyphysics
%{_datadir}/numptyphysics
%{_datadir}/applications/numptyphysics.desktop
%{_datadir}/icons/hicolor/256x256/apps/numptyphysics.png
%{_mandir}/man6/numptyphysics.6*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.32.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.31.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.30.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.29.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.28.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.4-0.27.20151231gitc0abd47
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.26.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.25.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.24.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.23.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.22.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.21.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.20.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.4-0.19.20151231gitc0abd47
- Patch for GCC 10.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.18.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.17.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.16.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.15.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.14.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.13.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Jon Ciesla <limburgher@gmail.com> - 0.4-0.12.20151231gitc0abd47
- ExcludeArch ppc64le.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.11.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-0.10.20151231gitc0abd47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.4-0.9.20151231gitc0abd47
- Fix the patch

* Sat Jan 30 2016 Lubomir Rintel <lkundrak@v3.sk> - 0.4-0.8.20151231gitc0abd47
- Update to a later upstream
- Drop upstreamed patches
- Fix a crash on startup (rh #1299186)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.8.20140108git4837e29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4-0.7.20140108git4837e29
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 20 2015 Lubomir Rintel <lkundrak@v3.sk> - 0.4-0.6.20140108git4837e29
- Update. New upstream.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.6.20120726gita22cde2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.5.20120726gita22cde2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-0.4.20120726gita22cde2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.4-0.3.20120726gita22cde2
- Drop desktop vendor tag.

* Thu Jul 26 2012 Adam Williamson <awilliam@redhat.com> - 0.4-0.2.20120726gita22cde2
- correct the NEVR per the guidelines

* Thu Jul 26 2012 Jonathan Dieter <jdieter@lesbg.com> - 0.4-0.1.git.20120726.a22cde2
- Update to latest git
- Remove upstreamed patches
- Add patches to fix build problems
- Fixup whitespace and preserve changelog. - Jon Ciesla <limburgher@gmail.com>
- Added SDL_devel, vim-common, zlib-devel BuildRequires. - JC

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.9.20080925svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.8.20080925svn
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.7.20080925svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.6.20080925svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.5.20080925svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-0.4.20080925svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 30 2008 Lubomir Rintel <lkundrak@v3.sk> 0.3-0.4.20080925svn
- Add more levels

* Mon Sep 29 2008 Lubomir Rintel <lkundrak@v3.sk> 0.3-0.2.20080925svn
- Review, small tidy-ups

* Thu Sep 25 2008 Lubomir Rintel <lkundrak@v3.sk> 0.3-0.1.20080925svn
- Initial packaging attempt
