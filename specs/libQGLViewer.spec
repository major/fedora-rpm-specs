Name:           libQGLViewer
Version:        2.9.1
Release:        7%{?dist}
Summary:        Qt based OpenGL generic 3D viewer library

# Automatically converted from old format: GPLv2 with exceptions or GPLv3 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions OR LicenseRef-Callaway-GPLv3-with-exceptions 
URL:            http://www.libqglviewer.com/index.html
Source0:        http://www.libqglviewer.com/src/%{name}-%{version}.tar.gz

# QGLViewer/VRender/gpc.cpp uses exit(0) to "abort" from a failure of malloc
# Use abort() instead.
Patch0:         libQGLViewer-2.9.1-exit.patch
# libQGLViewer .pro files explicitely remove "-g" from compile flags. Make
# them back.
Patch1:         libQGLViewer-2.6.3-dbg.patch

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: make
BuildRequires: gcc-c++
Obsoletes:     %{name}-qt5 < %{version}-%{release}
Provides:      %{name}-qt5 = %{version}-%{release}

%description
%{name} is a C++ library based on Qt that eases the creation of OpenGL
3D viewers. It provides some of the typical 3D viewer functionality, such
as the possibility to move the camera using the mouse, which lacks in most
of the other APIs. Other features include mouse manipulated frames,
interpolated key-frames, object selection, stereo display, screenshot saving
and much more. It can be used by OpenGL beginners as well as to create
complex applications, being fully customizable and easy to extend.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       qt5-qttools-devel
Obsoletes:      %{name}-qt5-devel < %{version}-%{release}
Provides:       %{name}-qt5-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: API documentation, demos and example programs for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .exit
%patch -P1 -p1 -b .dbg

# Fix permissions
chmod a-x examples/*/*.vcproj

%build

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%{!?_qt5_qmake: %define _qt5_qmake /usr/bin/qmake-qt5}
%{!?qmake_qt5: %define qmake_qt5 \
  %{_qt5_qmake} \\\
  QMAKE_CFLAGS_DEBUG="${CFLAGS:-%optflags}" \\\
  QMAKE_CFLAGS_RELEASE="${CFLAGS:-%optflags}" \\\
  QMAKE_CXXFLAGS_DEBUG="${CXXFLAGS:-%optflags}" \\\
  QMAKE_CXXFLAGS_RELEASE="${CXXFLAGS:-%optflags}" \\\
  QMAKE_LFLAGS_DEBUG="${LDFLAGS:-%{?__global_ldflags}}" \\\
  QMAKE_LFLAGS_RELEASE="${LDFLAGS:-%{?__global_ldflags}}" \\\
  QMAKE_STRIP=
}

cd QGLViewer
%{qmake_qt5} \
    LIB_DIR=%{_libdir} \
    DOC_DIR=%{_pkgdocdir} \
    INCLUDE_DIR=%{_includedir} \
    TARGET_x=%{name}-qt5.so.%{version}
# The TARGET_x variable gives the SONAME. However, qmake behavior is not
# correct when the SONAME is customized: it create wrong symbolic links
# that must be cleaned after the installation.
make %{?_smp_mflags}
cd ../designerPlugin
%{qmake_qt5} LIB_DIR=../QGLViewer
make %{?_smp_mflags}

%install
cd QGLViewer
make -f Makefile -e INSTALL_ROOT=$RPM_BUILD_ROOT install_target install_include STRIP=/usr/bin/true
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt5.prl
# Clean symbolic links
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt5.so.?.?
rm $RPM_BUILD_ROOT%{_libdir}/libQGLViewer-qt5.so.%{version}\\* || true

cd ../designerPlugin
make -e INSTALL_ROOT=$RPM_BUILD_ROOT install STRIP=/usr/bin/true



%ldconfig_scriptlets


%files
%doc README LICENCE CHANGELOG GPL_EXCEPTION
%{_libdir}/libQGLViewer-qt5.so.%{version}

%files devel
%{_includedir}/QGLViewer/
%{_libdir}/libQGLViewer-qt5.so
%{_libdir}/qt5/plugins/designer/libqglviewerplugin.so

%files doc
%doc doc
%doc examples

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9.1-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.9.1-1
- Drop qt4 package, as qt4 does not appear to have the required headers.
- Update to 2.9.1.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Rich Mattes <richmattes@gmail.com> - 2.6.4-1
- Update to release 2.6.4, with upstream fix for qreal on armv7 (rhbz#1556028)
- Remove upstream patch and update library names

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  5 2016 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 2.6.3-1
- New upstream release
- Refresh patches, remove patch2 (about a compilation error)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug  3 2015 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 2.5.1-8
- Fix the build on Rawhide

* Mon Aug  3 2015 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 2.5.1-7
- Add the support for Qt5
- Define missing macros if needed
- Add post/postun for the qt5 sub-package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.5.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar  3 2014 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 2.5.1-2
- Use %%{qmake_qt4}
- Disable 'strip'

* Mon Mar  3 2014 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 2.5.1-1
- New upstream version.
- No latin1 files anymore.
- Patch2 (about <GL/glu.h>) is no longer needed.

* Tue Aug  6 2013 Laurent Rineau <lrineau@renoir.geometryfactory.com> - 2.3.9-8
- Honor %%{_pkgdocdir} where available.
  See https://fedoraproject.org/wiki/Changes/UnversionedDocdirs
- No longer use the macro %%{_qt4_qmake} and %%{_qt4_plugindir}.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-4
- Rebuilt for c++ ABI breakage

* Thu Feb  9 2012 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.9-3
- New patch to include <GL/glu.h>. Needed on F17.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun  7 2011 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.9-1
- New upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul  2 2010 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.6-1
- New upstream release
- Fix an incorrect changelog entry

* Wed Apr 21 2010 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.5-2
- Tweak the configuration and compilation so that the soname of the library is
  equal to its soversion. The binary compilatibility is not ensured by 
  upstream.

* Tue Apr 20 2010 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.5-1
- New upstream release
- Rebase the dbg patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-9
- noarch -doc subpackage.

* Wed Apr  1 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-8
- Add a patch, so that "-g" flags are not removed.

* Mon Mar 30 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-7
- Remove glibc-common from BR:

* Tue Jan  6 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-6
- Merge the subpackage -designer-plugin into -devel.
- Add Requires: qt4-devel to -devel.

* Tue Jan  6 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-5
- Correct License: tag.

* Tue Jan  6 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-4
- Add the file GPL_EXCEPTION to docs.

* Tue Jan  6 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-3
- Untabify the spec file.

* Tue Jan  6 2009 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-2
- Update the URL.
- Add a patch that change exit(0) to abort() in QGLViewer/VRender/gpc.cpp.
- Use macros %%{_qt4_qmake} and %%{_qt4_plugindir} from /etc/rpm/macros.qt4
- Remove %%{_libdir}/libQGLViewer.prl (useless, and rpmlint outputs an
  error about it in %%{_libdir}

* Wed Dec 17 2008 Laurent Rineau <Laurent.Rineau__fedora@normalesup.org> - 2.3.1-1
- New release.

* Tue Oct 23 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 2.2.6-2
- Add examples in %%{name}-doc

* Tue Oct 23 2007 Laurent Rineau <laurent.rineau__fedora@normalesup.org> - 2.2.6-1
- New upstream release.

* Tue Apr  3 2007 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 2.2.5-2
- Add the designer-plugin sub-package.

* Mon Jan 29 2007 Laurent Rineau <laurent.rineau__fedora_extras@normalesup.org> - 2.2.5-1
- First release to be submitted to Fedora.

