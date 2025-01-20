Name:		putty
Version:	0.82
Release:	2%{?dist}
Summary:	SSH, Telnet and Rlogin client
License:	MIT
URL:		http://www.chiark.greenend.org.uk/~sgtatham/putty/
Source0:	http://the.earth.li/~sgtatham/putty/latest/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.svg
Source3:	uk.org.greenend.chiark.sgtatham.putty.metainfo.xml
BuildRequires:	gtk3-devel
BuildRequires:	krb5-devel
BuildRequires:	halibut
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	perl-Digest-SHA
BuildRequires:	coreutils
BuildRequires:	python3-devel
BuildRequires:	sed
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	cmake
Requires:	hicolor-icon-theme

%description
Putty is a SSH, Telnet & Rlogin client - this time for Linux.

%prep
%autosetup

# fix python shebangs to use python3 (python bits aren't currently packaged)
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;

%build
export CFLAGS="%{build_cflags} -DNOT_X_WINDOWS -Wno-error=unused-function"
%cmake
%cmake_build
make -C icons putty-48.png
cd %{__cmake_builddir}
make -C doc

%install
%cmake_install
install -d html
install -pm 0644 doc/html/*.html html

desktop-file-install \
  --vendor "" \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

install -m644 -D -p icons/putty-48.png %{buildroot}%{_datadir}/pixmaps/putty.png
install -m644 -D -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/putty.svg

install -m644 -D -p %{SOURCE3} %{buildroot}%{_metainfodir}/uk.org.greenend.chiark.sgtatham.putty.metainfo.xml

%files
%doc LICENCE html
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/uk.org.greenend.chiark.sgtatham.putty.metainfo.xml

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.82-1
- New version
  Resolves: rhbz#2329243

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 17 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.81-1
- New version
  Resolves: rhbz#2275179
- Fixed vulnerability allowing recovery of NIST P-521 private keys
  Resolves: CVE-2024-31497

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 0.80-1
- New version
  Resolves: rhbz#2255025
- Fixed Terrapin vulnerability in some SSH protocol extensions
  Resolves: CVE-2023-48795

* Thu Aug 31 2023 Jaroslav Škarvada <jskarvad@redhat.com> - 0.79-1
- New version
  Resolves: rhbz#2235091

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Daniel Rusek <mail@asciiwolf.com> - 0.78-3
- Add AppStream metadata, svg icon
  Resolves: rhbz#1792733

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.78-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov  1 2022 Jaroslav Škarvada <jskarvad@redhat.com> - 0.78-1
- New version
  Resolves: rhbz#2138511

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.76-1
- New version
  Resolves: rhbz#1983289

* Mon May 10 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.75-1
- New version
  Resolves: rhbz#1958503

* Tue Mar 16 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 0.74-4
- Fixed crash when running under Wayland
  Resolves: rhbz#1905268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.74-1
- New version
  Resolves: rhbz#1851584
- Dropped LTO fixes patch, it seems to be upstreamed

* Fri May 15 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.73-5
- Added fixes for link time optimization (LTO), patch provided
  by Jeff Law <law@redhat.com>

* Fri Feb 28 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 0.73-4
- Switched to python3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.73-2
- Cleaned up the spec file and simplified the build process
- Switched to gtk3

* Mon Sep 30 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.73-1
- New version
  Resolves: rhbz#1756746

* Fri Aug 16 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.72-1
- New version
  Resolves: rhbz#1742144

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 0.71-1
- New version
  Resolves: rhbz#1689559

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 0.70-8
- Fixed FTBFS
  Resolves: rhbz#1605526

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.70-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 19 2018 Ondřej Lysoněk <olysonek@redhat.com> - 0.70-5
- Add gcc to BuildRequires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.70-1
- New version
  Resolves: rhbz#1468324
  Resolves: rhbz#1468324
- Dropped gtk2-compile-fix patch (not needed)

* Wed May  3 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.69-1
- New version
  Resolves: rhbz#1446835

* Thu Feb 23 2017 Jaroslav Škarvada <jskarvad@redhat.com> - 0.68-1
- New version
  Resolves: rhbz#1425642
- Dropped add-xdg-support patch (upstreamed)
- Minor specfile cleanup

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.67-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Ondřej Lysoněk <olysonek@redhat.com> - 0.67-2
- Added support for XDG
  Resolves: rhbz#1154304

* Mon Mar  7 2016 Jaroslav Škarvada <jskarvad@redhat.com> - 0.67-1
- New version
  Resolves: rhbz#1314985

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.66-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.66-1
- New version
  Resolves: rhbz#1279881

* Mon Nov  9 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.65-2
- Fixed integer overflow and buffer underrun in erase characters (ECH) handling
  Resolves: CVE-2015-5309

* Mon Jul 27 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.65-1
- New version
  Resolves: rhbz#1246753

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar  3 2015 Jaroslav Škarvada <jskarvad@redhat.com> - 0.64-1
- New version
  Resolves: CVE-2015-2157

* Tue Nov 11 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.63-4
- Increased icon size to 48x48
  Resolves: rhbz#1157564

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 12 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.63-1
- New version
  Resolves: rhbz#995610
- Dropped perms, CVE-2013-4852, CVE-2013-4206, CVE-2013-4207,
  CVE-2013-4208 patches (all in upstream)

* Thu Aug  8 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.62-7
- Fixed a heap-corrupting buffer underrun bug in the modmul function
  Resolves: CVE-2013-4206
- Fixed a buffer overflow vulnerability in the calculation of modular
  inverses when verifying a DSA signature
  Resolves: CVE-2013-4207
- Fixed problem when private keys are left in memory after being
  used by PuTTY tools
  Resolves: CVE-2013-4208

* Mon Aug  5 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 0.62-6
- Fixed integer overflow
  Resolves: CVE-2013-4852
- Fixed bogus dates in changelog (best estimated)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0.62-3
- Added missing ImageMagick BuildRequires

* Wed Sep 19 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0.62-2
- Generated icon from sources

* Tue Aug  7 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 0.62-1
- New version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-9.20100910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.60-8.20100910svn
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-7.20100910svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Mark Chappell <tremble@fedoraproject.org> - 0.60-6.20100910svn
- Bump version in line with packaging specs

* Fri Sep 10 2010 Mark Chappell <tremble@fedoraproject.org> - 0.60-6.8991svn
- Update to latest GTK2 version from SVN (r8991)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 13 2008 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.60-3
- Bump-n-build for GCC 4.3

* Tue Aug 21 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.60-2
- Rebuild for BuildID

* Mon Apr 30 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.60-1
- New upstream version (mostly bugfixes)
- Previous release pre-emptively fixed CVE-2006-7162/BZ#231726
- Added patch to make "private" files (keys/logs) non-executable

* Thu Jan 25 2007 Patrick "Jima" Laughton <jima@beer.tclug.org> 0.59-1
- New upstream version
- Macro-ized Source filenames
- Cleanup of spaces/tabs to eliminate rpmlint warnings

* Sun Aug 27 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.58-3
- Rebuild for FC6

* Wed May 03 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.58-2
- rebuild

* Tue Apr 19 2005 Adrian Reber <adrian@lisas.de> - 0.58-1
- Updated to 0.58

* Tue Mar 01 2005 Adrian Reber <adrian@lisas.de> - 0.57-2
- fix build with gcc4

* Mon Feb 21 2005 Adrian Reber <adrian@lisas.de> - 0.57-1
- Updated to 0.57

* Tue Oct 26 2004 Adrian Reber <adrian@lisas.de> - 0.56-0.fdr.1
- Updated to 0.56 (bug #2209)

* Fri Aug  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.55-0.fdr.2
- Fix URL and source location.

* Thu Aug 05 2004 Andreas Pfaffeneder <fedora@zuhause-local.de> 0:0.55.fdr.1
- Update to 0.55 due to security problem (CORE-2004-0705).

* Tue Nov 18 2003 Andreas Pfaffeneder <fedora@zuhause-local.de> 0:0.0-0.fdr.2.20030821
- Add desktop-file-utils to build requires

* Sun Aug 24 2003 Adrian Reber <adrian@lisas.de> 0:0.0-0.fdr.1.20030821
- now honouring $RPM_OPT_FLAGS
- moved make to the build section; binaries are now stripped
- inserted _smp_mflags
- using makeinstall
- created a icon for the menu entry
- optimized the category of the .desktop file from Internet to Network
- more fedorafication

* Thu Aug 21 2003 Andreas Pfaffeneder <fedora@zuhause-local.de> 0:0.0-0.fdr.0.20030821
- Quick and dirty spec for cvs of putty
