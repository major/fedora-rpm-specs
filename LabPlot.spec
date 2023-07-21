# Features in Fedora/Free Electronic Lab

# Known Bugs fixed:
# S#2759043 Segfault in TableModel::handleAspectRemoved() - can't reproduce

%global genname labplot

Name:		LabPlot
Version:	2.8.1
Release:	12%{?dist}
Summary:	Data Analysis and Visualization

License:	GPLv2+
URL:		http://labplot.sourceforge.net/

Source0:	http://download.kde.org/stable/%{genname}/%{version}/%{genname}-%{version}.tar.xz
# Patch0, 1 : required by https://github.com/KDE/syntax-highlighting/commit/42a061b04c507de11b0fb240808fc65a7528d946
# https://github.com/KDE/labplot/commit/9e77b593030fdae0fbbad113415483b3ca51a654
Patch0:   labplot-KSyntaxHighlighting-5_94-include.patch
# slightly modified the below to apply cleanly
# https://github.com/KDE/labplot/commit/375786ca124a1a6773c609236f8341890f23e1d8
Patch1:   labplot-KSyntaxHighlighting-5_94-include-2.patch

BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-syntax-highlighting-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtconfiguration-devel 
BuildRequires:	qt5-qtserialport-devel
BuildRequires:	desktop-file-utils 
BuildRequires:	gsl-devel
BuildRequires:	gettext-devel
BuildRequires:	extra-cmake-modules
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:	cantor-devel
%endif
BuildRequires:	bison
BuildRequires:  cfitsio-devel
BuildRequires:	fftw-devel
BuildRequires:	hdf5-devel
BuildRequires:  libcerf-devel
BuildRequires:  libspectre-devel
BuildRequires:  lz4-devel
BuildRequires:	netcdf-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  libappstream-glib

ExcludeArch:	sparc64 s390 s390x

Requires:	electronics-menu

%description
LabPlot is for scientific 2D and 3D data and function plotting.
The various display and analysis functions are explained in the
handbook (KDE help center). LabPlot also provides a component
for easily viewing the project files in Konqueror.


%prep
%setup -q -n %{genname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{genname}2 --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{genname}2.appdata.xml


%files -f %{genname}2.lang
%license COPYING
%doc README.md ChangeLog AUTHORS INSTALL
%{_datadir}/icons/hicolor/*/apps/%{genname}*
%{_bindir}/%{genname}2
%{_datadir}/kxmlgui5/%{genname}2/
%{_datadir}/mime/packages/%{genname}2.xml
%{_datadir}/%{genname}2/
%{_datadir}/applications/org.kde.%{genname}2.desktop
%{_datadir}/metainfo/org.kde.%{genname}2.appdata.xml
%{_mandir}/man1/labplot2.1.gz
%{_mandir}/*/man1/labplot2.1.gz

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Maxwell G <gotmax@e.email> - 2.8.1-10
- Rebuild for cfitsio 4.2

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.1-9
- Rebuild for gsl-2.7.1

* Sat Aug 13 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.1-8
- Backport upstream fix for KSyntaxHighlighting 5.94 header path change

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 12 2022 Christoph Junghans <junghans@lanl.gov> - 2.8.1-6
- Rebuild for libcerf-2.1

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 2.8.1-4
- Rebuild for hdf5 1.12.1

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 2.8.1-3
- Rebuild for hdf5 1.10.7/netcdf 4.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 2.8.1-1
- 2.8.1

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 2.7.0-9
- rebuild (cantor)

* Tue Feb 02 2021 Christian Dersch <lupinix@mailbox.org> - 2.7.0-8
- Rebuilt for libcfitsio.so.7

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Mohan Boddu <mboddu@bhujji.com> - 2.7.0-6
- Rebuilt for cantor soname-bump

* Fri Aug 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.7.0-5
- rebuild (cantor)
- adapt to new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2.7.0-2
- Rebuild for hdf5 1.10.6

* Sun Feb 23 2020 Christian Dersch <lupinix@fedoraproject.org> - 2.7.0-1
- new version

* Sun Feb 23 2020 Christian Dersch <lupinix@fedoraproject.org> - 2.5.0-9
- Rebuilt for cantor soname-bump

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.0-7
- Rebuild for new cantor-libs

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.5.0-6
- Rebuilt for GSL 2.6.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 2.5.0-4
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.5.0-1
- Update to 2.5.0
- BR:kf5-syntax-highlighting-devel, qt5-qtserialport-devel, bison

* Sat May 19 2018 Kevin Fenzi <kevin@scrye.com> - 2.4.0-9
- Rebuild for cantorlibs. 

* Tue Feb 13 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.0-8
- Fix appdata file install location (fixes FTBFS)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4.0-6
- Remove obsolete scriptlets

* Sun Oct 15 2017 Mukundan Ragavan <nonamedotc@gmail.com> - 2.4.0-5
- bump release and rebuild for cantor

* Fri Sep 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.4.0-4
- rebuild for cantor
- %%build: use %%cmake_kf5
- %%install: use better install/fast target
- %%files: fix dir ownership
- fix scriptlets

* Tue Aug 01 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.0-3
- rebuild for gsl 2.4

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0
- Add buildrequires to kf5-knewstuff-devel
- Fix appdata install location

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.0-6
- Simplify files section

* Tue Nov 01 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.0-5
- Add new BR
- Fix desktop file properly

* Mon Oct 17 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.0-4
- Fix desktop file

* Wed Oct 12 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.0-3
- Fix files section

* Wed Oct 12 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.0-2
- Spec file cleanup - use license macro, edit doc list

* Wed Oct 12 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sat Jul 09 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Drop already upstream gsl2 patch

* Sun Mar 13 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-9
- Apply the fix - correctly without typos

* Fri Mar 11 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-8
- Apply the complete fix (#1314798)

* Fri Mar 11 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-7
- Fix desktop file
- Fixes bug#1314798

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-6
- Rebuild for gsl 2.1

* Tue Feb 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-5
- Added fixes for GCC-6 FTBFS - Thanks Yaakov Selkowitz

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-3
- Add upstream patch to support GSL 2.X

* Thu Oct 29 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-2
- use kf5 tarball
- added kf5 dependencies

* Wed Oct 28 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Tue Oct 20 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2
- Cleanup and modernize spec file

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.6.0.3-10
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.0.3-9
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 08 2015 Orion Poplawski <orion@cora.nwra.com> - 1.6.0.3-8
- Rebuild for hdf5 1.8.14

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.6.0.3-3
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Mon Nov 19 2012 Thibault North <tnorth@fedoraproject.org> - 1.6.0.3-1
- Update to 1.6.0.3

* Sun Dec 4 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.6.0.2-9
- Fixes Bug RH#715933 - FTBFS LabPlot-1.6.0.2-8.fc12

* Wed Oct 28 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.6.0.2-8
- fix FTBFS with current GSL (GSL_CONST_CGSM_GAUSS undefined, patch from Debian)

* Sat Oct 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.6.0.2-7
- drop ExcludeArch ppc64, OCaml is available for ppc64 these days

* Tue Sep 22 2009 Dennis Gilmore <dennis@ausil.us> - 1.6.0.2-6
- ExcludeArch s390 s390x and sparc64 no ocaml

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 16 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.6.0.2-3
- handle libLabPlotnetCDF.so* on F-8 and F-9

* Wed Sep 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0.2-2
- handle libLabPlotnetCDF.so*

* Wed Sep 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6.0.2-1
- update to 1.6.0.2
- drop useless gcc43 patch, init-smg-before-open-files patch

* Tue Jun 10 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.6.0.1-1
- New upstream release 1.6.0.1
- Now compatible with liborigin 20080225
- Bugfix: #449653: FTBFS LabPlot-1.5.1.6-6.fc9
- Bugfix: #434019: LabPlot failed massrebuild attempt for GCC 4.3
- Added qhull-devel as BR

* Tue Jun 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.5.1.6-7
- fix build against latest liborigin on F10 (backported from 1.6.0)

* Sat Apr 12 2008 Thibault North <tnorth [AT] fedoraproject DOT org> - 1.5.1.6-6
- Fixes for GCC 4.3
- Updated dependencies
- Now requires electronics-menu

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.6-4
- complying to freedesktop policies - categories
- queued for mass rebuild for Fedora 8 - BuildID
- dropped duplicates - examples/

* Mon Aug 06 2007  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.6-3
- Excluding PPC64 since it misses ocaml

* Mon Aug 06 2007  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.6-2
- Update License tag for new Licensing Guidelines compliance

* Mon Jul 30 2007  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.6-1
- New upstream release

* Mon Apr 23 2007  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.5-7
- removed parallel build for ppc

* Mon Apr 23 2007  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.5-6
- added texvc back in %%files
- removed useless .so

* Thu Apr 12 2007  Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.5-5
- split for doc-fr
- duplicate kmenu entries - removed category Science
- corrected missing index.html file from Help -> LabPlot Handbook
- merge -devel package with the main package

* Thu Apr 12 2007 Mamoru Tasaka <mtasaka [AT] ioa.s.u-tokyo.ac.jp> - 1.5.1.5-4.2
- Use system liborigin library
- Shut up undefined non-weak symbols
- Fix end-of-line encodings of [Mm]ap file
- Change the encoding of a part of documents

* Tue Feb 27 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.5-4
- Added mediawiki and koffice-devel as BR
- using liborigin system wide
- Dropped mediawiki as BR
- Fixed presence on gnome menu

* Sat Jan 13 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.5-3
- manual dependencies removed
- dropped additional arguments for x86_64 sparc64 ppc64 amd64

* Wed Jan 03 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.5-2
- Added audiofile-devel, qwtplot3d-devel, ocaml and netcdf-devel as BR
- using qwtplot3d and netcdf system wide #221022
- Fixed qt-qsa headers

* Sun Dec 31 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.5-1
- New stable release 1.5.1.5
- Fixed symlink-should-be-relative rpmlint issues
- Removed numerous entries on kmenu
- Added examples in a new -doc package
- Building pdf handbook for different languages
- Breaking down -doc package for different languages

* Sun Nov 19 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.5.1.4-1
- Initial package
