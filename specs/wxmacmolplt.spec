%global commit 161e14621640775e98bd7d7f46520b09c84d8f09
%global date 20210927
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: wxmacmolplt
Version: 7.7.3
Release: 4%{?dist}
Summary: A graphics program for plotting 3-D molecular structures and normal modes
License: GPL-2.0-or-later
URL: http://brettbode.github.io/wxmacmolplt/
Source0: https://github.com/brettbode/wxmacmolplt/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: wxGTK-devel
BuildRequires: automake
Requires: hicolor-icon-theme

%description
MacMolPlt is:
* A modern graphics program for plotting 3-D molecular structures and
  normal modes (vibrations). Modern means:
  o Mouse driven interface for real-time rotation and translation.
  o copy and paste functionality for interfacing to other programs such
    as word processors or other graphics programs (like ChemDraw).
  o simple printing to color or black and white printers (publication
    quality).
  o multiple files open at once.
* It reads a variety of file formats including any GAMESS input, log or
  IRC file directly to create animations of IRC's, DRC's, and
  optimizations. You may also import a $VEC group from any file (such as
  a GAMESS .DAT file). In addition xMol XYZ files, MolDen format files
  and Chemical Markup Language (CML) files are supported. Also some PDB
  file support and MDL MolFile support is included.

%prep
%setup -q
chmod -x MacMolPlt_Manual.html
rm -rv src/glew.{cpp,h}

%build
autoreconf -vif
%configure \
  --docdir=%{_pkgdocdir} \
  --with-glew \
  --with-wx-config=%{_bindir}/wx-config-3.2 \


%make_build

%install
%make_install
install -Dpm644 resources/wxmacmolplt.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/wxmacmolplt.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications resources/wxmacmolplt.desktop
rm %{buildroot}%{_pkgdocdir}/LICENSE

%files
%license LICENSE
%{_bindir}/wxmacmolplt
%{_mandir}/man1/wxmacmolplt.1*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/wxmacmolplt.png
%{_datadir}/wxmacmolplt

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Dominik Mierzejewski <rpm@greysector.net> 7.7.3-1
- update to 7.7.3 (resolves rhbz#2256352)
- use SPDX identifier in License tag

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 24 2022 Dominik Mierzejewski <dominik@greysector.net> - 7.7.2-8
- switch to tagged tarball source URL
- rebuild for wxGLCanvas change

* Mon Jul 25 2022 Scott Talbert <swt@techie.net> - 7.7.2-7
- Rebuild for wxGTK 3.2.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 10 2022 Scott Talbert <swt@techie.net> - 7.7.2-5
- Rebuild for wxGTK 3.1.7

* Tue Apr 12 2022 Dominik Mierzejewski <dominik@greysector.net> - 7.7.2-4
- rebuilt for wxGTK 3.1.6

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 7.7.2-3
- Rebuild for glew 2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 28 2021 Dominik Mierzejewski <rpm@greysector.net> 7.7.2-1
- update to 7.7.2
- use modern make macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.7.1-0.3.20210718gitfc6f3c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Dominik Mierzejewski <rpm@greysector.net> 7.7.1-0.2.20210718gitfc6f3c1
- latest git commit
- fixes wxGTK assertion (https://github.com/brettbode/wxmacmolplt/issues/124)

* Tue Jul 06 2021 Dominik Mierzejewski <rpm@greysector.net> 7.7.1-0.1.20200517git5107134
- update to 7.7.1 pre-release
- ensure bundled glew and ming are not used for build
- build against wxGTK 3.1
- stop forcing C++14 (only ming glue was failing to build with C++17)

* Mon Jun 07 2021 Dominik Mierzejewski <rpm@greysector.net> 7.7-17
- drop ming support (package orphaned)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 7.7-15
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 7.7-10
- Rebuilt for glew 2.1.0

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 7.7-9
- Rebuild with fixed binutils

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 7.7-2
- Rebuild for glew 2.0.0

* Sat Aug 27 2016 Dominik Mierzejewski <rpm@greysector.net> 7.7-1
- update to 7.7
- use wxGTK3 (F25+ only)

* Mon Feb 22 2016 Dominik Mierzejewski <rpm@greysector.net> 7.6.2-1
- update to 7.6.2
- update URL to new upstream location
- drop defattr and use license macro

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 7.5-8
- Rebuild for glew 1.13

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 7.5-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Dominik Mierzejewski <rpm@greysector.net> 7.5-4
- enable SWF output (depends on ming)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Dominik Mierzejewski <rpm@greysector.net> 7.5-2
- fix docdir location
- re-run autoreconf before build to fix aarch64 support (rhbz #926733)

* Tue Feb 11 2014 Dominik Mierzejewski <rpm@greysector.net> 7.5-1
- update to 7.5
- update source URL
- drop obsolete spec file parts
- use upstream desktop file and icon

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 7.4.4-3
- rebuilt for GLEW 1.10

* Wed Jul 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 7.4.4-2
- Drop unnecessary --docdir %%configure arg.

* Sun Mar 17 2013 Dominik Mierzejewski <rpm@greysector.net> 7.4.4-1
- updated to 7.4.4
- dropped system glew patch (obsolete)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 7.4.1-8
- Rebuild for glew 1.9.0

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 7.4.1-7
- -Rebuild for new glew

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 ajax@redhat.com - 7.4.1-3
- Rebuild for new glew soname

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Dominik Mierzejewski <rpm@greysector.net> 7.4.1-1
- updated to 7.4.1

* Wed Dec 02 2009 Dominik Mierzejewski <rpm@greysector.net> 7.4-1
- adapted upstream specfile
- patched to use system glew
- added desktop file and icon from project website
