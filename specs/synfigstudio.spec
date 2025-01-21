%define debug_package %{nil}
Name:           synfigstudio
Version:        1.5.3
Release:        2%{?dist}
Summary:        Vector-based 2D animation studio

License:        GPL-2.0-or-later
URL:            http://synfig.org/
Source0:        http://download.sourceforge.net/synfig/%{name}-%{version}.tar.gz
# git clone, d4e547
#Source0:        synfig-studio.tar.gz
Patch1:         synfig-studio-m4_pattern_allow.patch

BuildRequires: make
BuildRequires:  desktop-file-utils
BuildRequires:  synfig-devel >= %{version}
BuildRequires:  ETL-devel >= %{version}
BuildRequires:	gcc-c++
BuildRequires:  gtkmm30-devel
BuildRequires:  autoconf
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  ladspa

%description
Synfig Animation Studio is a powerful, industrial-strength vector-based
2D animation software, designed from the ground-up for producing
feature-film quality animation with fewer people and resources.
It is designed to be capable of producing feature-film quality
animation. It eliminates the need for tweening, preventing the
need to hand-draw each frame. Synfig features spatial and temporal
resolution independence (sharp and smoothat any resolution or framerate),
high dynamic range images, and a flexible plugin system.

This package contains the GUI-based animation studio.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch -P1 -p0 -b .m4allow

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
# build script regeneration needed for cflags and m4allow patches
autoreconf -fi
# autoreconf entirely screws up po/Makefile.in.in , for some reason
intltoolize -f

%configure --disable-update-mimedb
%make_build


%install
%make_install
%find_lang %{name}
desktop-file-install \
        --delete-original                                       \
        --dir=%{buildroot}%{_datadir}/applications           \
        %{buildroot}%{_datadir}/applications/org.synfig.SynfigStudio.desktop


%ldconfig_scriptlets

%files -f %{name}.lang
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime-info/synfigstudio.*
%{_datadir}/mime/packages/org.synfig.SynfigStudio.xml
#%%{_datadir}/pixmaps/*.png
#%%{_datadir}/pixmaps/synfigstudio
%{_datadir}/synfig/plugins/
%{_datadir}/synfig/brushes/
%{_datadir}/synfig/sounds/
%{_datadir}/synfig/ui/
%{_datadir}/synfig/css/
%{_datadir}/synfig/icons/
%{_datadir}/synfig/images/
%{_datadir}/appdata/org.synfig.SynfigStudio.appdata.xml
%doc AUTHORS COPYING README


%files devel
%{_includedir}/synfigapp-0.0
%{_libdir}/*.so
%exclude %{_libdir}/*.la
%doc COPYING TODO


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.5.3-1
- 1.5.3

* Tue Aug 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-1
- 1.5.2

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-9
- Enable ppc64le builds.

* Fri Apr 26 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.5.1-8
- Rebuilt for openexr 3.2.4

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-5
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.5.1-3
- Rebuild for ImageMagick 7

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 08 2022 Sérgio Basto <sergio@serjux.com> - 1.5.1-1
- Update synfigstudio to 1.5.1 for https://fedoraproject.org/wiki/Changes/F36MLT-7

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-3
- ImageMagick rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-10
- rebuild against New OpenEXR properly

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 1.2.2-9
- Rebuild for OpenEXR 2.5.3.

* Wed Aug 19 2020 Jeff Law <law@redhat.com> - 1.2.2-8
- Force C++14 as this code is not C++17 ready

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Richard Shaw <hobbes1069@gmail.com> - 1.2.2-3
- Rebuild for OpenEXR 2.3.0.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.2.2-1
- 1.2.2.
- Modernise spec

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 1.2.1-7
- Rebuild for ImageMagick 6.9.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1.2.1-5
- Rebuild for fixed ETL spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-3
- Remove obsolete scriptlets

* Thu Sep 14 2017 Pete Walter <pwalter@fedoraproject.org> - 1.2.1-2
- Rebuilt for ImageMagick 6.9.9 soname bump

* Mon Sep 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-1
- 1.2.1.

* Fri Aug 25 2017 Adam Williamson <awilliam@redhat.com> - 1.2.0-6
- Adjust build so cflags are used properly, re-enable debugsource

* Thu Aug 24 2017 Adam Williamson <awilliam@redhat.com> - 1.2.0-5
- Rebuild for new ImageMagick

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Jon Ciesla <limburgher@gmail.com> - 1.2.0-1
- 1.2.0

* Wed Jul 06 2016 Jon Ciesla <limburgher@gmail.com> - 1.1.10-0.20160706gitd4e547
- Restore cflags patch, BZ 1352537.

* Fri Jun 24 2016 Jon Ciesla <limburgher@gmail.com> - 1.1.10-0.20160624gitd4e547
- 1.1.10 prerelease.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.64.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 0.64.3-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Dec 23 2014 Jon Ciesla <limburgher@gmail.com> - 0.64.3-1
- Latest upstream, BZ 1176892.
- Added synfig version BR.

* Fri Oct 17 2014 Jon Ciesla <limburgher@gmail.com> - 0.64.2-1
- Latest upstream, BZ 1154006.

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.64.1-4
- update scriptlets
- tighten subpkg deps via %%_isa
- %%build with --disable-update-mimedb
- run autoconf in %%prep (instead of %%build)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 05 2013 Jon Ciesla <limburgher@gmail.com> - 0.64.1-1
- Latest upstream, BZ 1026738.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.64.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.64.0-1
- Latest upstream, BZ 962137.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.63.05-5.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63.05-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Luya Tshimbalanga <luya@fedoraproject.org> - 0.63.05-3.1
- Really remove all but xml file (rhbz#821740)

* Mon May 21 2012 Luya Tshimbalanga <luya@fedoraproject.org> - 0.63.05-2
- Fix mime.cache issue (rhbz#821740)

* Mon Apr 23 2012 Jon Ciesla <limburgher@gmail.com> - 0.63.05-1
- Latest upstream.
- Dialog color patch upstreamed.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.63.04-2
- Rebuilt for c++ ABI breakage

* Sat Feb 11 2012 Luya Tshimbalanga <luya@fedoraproject.org>
- New upstream release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com>
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.62.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 04 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.62.02-1
- Rebase

* Sat Dec 04 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.62.00-3
- Fix build

* Thu Dec 24 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.62.00-2
- Fix optflags use (Ville Skyttä, #549420)

* Tue Nov 17 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.62.00-1
- Bump version

* Fri Jan 09 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.61.09-1
- Initial packaging attempt
