Name:           libQGLViewer
Version:        3.0.0
Release:        3%{?dist}
Summary:        Qt based OpenGL generic 3D viewer library
License:        LGPL-3.0-or-later
URL:            https://gillesdebunne.github.io/libQGLViewer/
Source0:        https://gillesdebunne.github.io/libQGLViewer/src/libQGLViewer-%{version}.tar.gz

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
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       qt5-qttools-devel
Obsoletes:      %{name}-qt5-devel < %{version}-%{release}
Provides:       %{name}-qt5-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: API documentation, demos and example programs for %{name}
BuildArch: noarch
%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .exit
%patch -P1 -p1 -b .dbg

# Remove hidden apple binary files
find . -name '._*' -delete

# Fix permissions
chmod a-x examples/*/*.vcproj

%build

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

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
make -f Makefile -e INSTALL_ROOT=%{buildroot} install_target install_include STRIP=/usr/bin/true
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm %{buildroot}%{_libdir}/libQGLViewer-qt5.prl
# Clean symbolic links
rm %{buildroot}%{_libdir}/libQGLViewer-qt5.so.?.?
rm %{buildroot}%{_libdir}/libQGLViewer-qt5.so.%{version}\\* || true

cd ../designerPlugin
make -e INSTALL_ROOT=%{buildroot} install STRIP=/usr/bin/true

%files
%doc README CHANGELOG
%license LICENSE
%{_libdir}/libQGLViewer-qt5.so.%{version}

%files devel
%{_includedir}/QGLViewer/
%{_libdir}/libQGLViewer-qt5.so
%{_libdir}/qt5/plugins/designer/libqglviewerplugin.so

%files doc
%license LICENSE
%doc doc
%doc examples

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Mon Oct 06 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.0-2
- More review fixes

* Mon Oct 06 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0.0-1
- update to 3.0.0, changing license to LGPL

* Mon Oct 06 2025 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.9.1-9
- modernize spec, bring back package to Fedora.
