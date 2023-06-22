%undefine __cmake_in_source_build
%define _vpath_srcdir toonz/sources

Name:    opentoonz
Version: 1.7.1
Release: 1%{?dist}
Summary: 2D animation software

License: BSD
URL:     https://opentoonz.github.io/
Source0: https://github.com/opentoonz/opentoonz/archive/refs/tags/v%{version}.tar.gz

Patch0: opentoonz-1.5.0-lzo-fix.patch
# https://github.com/opentoonz/opentoonz/issues/4199
Patch1: opentoonz-1.5.0-tiff-fix.patch
Patch2: opentoonz-1.6.0-exr-fix.patch
# https://github.com/opentoonz/opentoonz/pull/4239
Patch3: opentoonz-1.7.0-gethostbyname.patch
Patch4: opentoonz-1.7.0-install-path-fix.patch
Patch5: opentoonz-1.7.0-kissfft-fix.patch       
Patch6: opentoonz-1.7.0-toonzrle-rm.patch
Patch7: opentoonz-1.7.0-tzp-tiffiop-fix.patch
Patch8: opentoonz-1.7.1-appdata.patch

BuildRequires: flexiblas-devel
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: freeglut-devel
BuildRequires: freetype-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glew-devel
BuildRequires: kiss-fft-devel
BuildRequires: libappstream-glib
BuildRequires: libjpeg-turbo-devel
BuildRequires: libmypaint-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: lz4-devel
BuildRequires: lzo-devel
BuildRequires: opencv-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-devel
BuildRequires: SuperLU-devel
BuildRequires: tinyexr-devel
BuildRequires: turbojpeg-devel
BuildRequires: xz-devel

BuildRequires: qt5-qttools-static
BuildRequires: kiss-fft-static

Requires: opencv
Requires: hicolor-icon-theme
Requires: %{name}-data = %{version}-%{release}

%description
OpenToonz is a 2D animation software published by DWANGO. It is based on 
Toonz Studio Ghibli Version, originally developed in Italy by 
Digital Video, Inc., and customized by Studio Ghibli over many years of 
production.
This version was packaged for Fedora using the latest stable libraries
available in the distribution, in exchange some features were disabled.


%package data
Summary: OpenToonz data files
BuildArch: noarch

%description data
Data files for the OpenToonz application.


%package doc
Summary: OpenToonz doc files
BuildArch: noarch

%description doc
Documentation about the OpenToonz application.


%prep
%autosetup -p1

# Remove all thirdparty libraries
rm -rf thirdparty
find stuff/doc/LICENSE/ -type f -not -name 'LICENSE.txt' -delete

# add flexiblas
sed -i 's/OPENBLAS_LIB NAMES/& flexiblas/' toonz/sources/CMakeLists.txt


%build
%cmake \
    -DWITH_SYSTEM_LZO:BOOL=ON \
    -DCMAKE_SKIP_RPATH:BOOL=YES \
    -DWITH_TRANSLATION:BOOL=OFF
    
%cmake_build


%install
%cmake_install
chmod 0755 ${RPM_BUILD_ROOT}%{_libdir}/%{name}/*.so
desktop-file-validate \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/io.github.OpenToonz.desktop
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/io.github.OpenToonz.appdata.xml

%files
%license LICENSE.txt
%{_bindir}/OpenToonz
%{_bindir}/opentoonz
%{_bindir}/tcleanup
%{_bindir}/tcomposer
%{_bindir}/tconverter
%{_bindir}/tfarmcontroller
%{_bindir}/tfarmserver
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so
%{_datadir}/applications/io.github.OpenToonz.desktop
%{_metainfodir}/io.github.OpenToonz.appdata.xml
%{_datadir}/icons/hicolor/256x256/apps/io.github.OpenToonz.png

%files data
%license LICENSE.txt
%{_datadir}/%{name}/


%files doc
%doc doc/*.md
%doc doc/*.JPG


%changelog
* Tue Jun 20 2023 Diego Herrera <dherrera@redhat.com> 1.7.1-1
- Updated to 1.7.1
- Update package description

* Wed May 10 2023 Diego Herrera <dherrera@redhat.com> 1.7.0-1
- Updated to 1.7.0

* Mon Feb 6 2023 Diego Herrera <dherrera@redhat.com> 1.6.0-11
- Fix size_t redefinition issue on tgc::hash class.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 1.6.0-9
- Rebuild for opencv 4.7.0

* Wed Nov 2 2022 Diego Herrera <dherrera@redhat.com> 1.6.0-8
- Expose static library dependency

* Thu Aug 25 2022 Diego Herrera <dherrera@redhat.com> 1.6.0-7
- Make exr patch compatible with upstream

* Thu Aug 25 2022 Diego Herrera <dherrera@redhat.com> 1.6.0-6
- Fix exr linking problems

* Thu Aug 25 2022 Iñaki Úcar <iucar@fedoraproject.org> - 1.6.0-5
- Adhere to BLAS/LAPACK guidelines

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 1.6.0-3
- Rebuilt for opencv 4.6.0

* Fri Apr 29 2022 Diego Herrera <dherrera@redhat.com> 1.6.0-2
- Disable exr format because of linking problems

* Mon Apr 18 2022 Diego Herrera <dherrera@redhat.com> 1.6.0-1
- Updated to 1.6.0

* Wed Mar 16 2022 Diego Herrera <dherrera@redhat.com> 1.5.0-5
- Fixed build problems with cmake
- libusb retired from rawhide

* Sat Feb 5 2022 Diego Herrera <dherrera@redhat.com> 1.5.0-4
- Restored metainfo 

* Fri Feb 4 2022 Diego Herrera <dherrera@redhat.com> 1.5.0-3
- Added version macro to the source url 

* Fri Feb 4 2022 Diego Herrera <dherrera@redhat.com> 1.5.0-2
- Added cmake macros
- Used desktop-file-validate instead of desktop-file-install
- Cleaned up requirements

* Wed Feb 2 2022 Diego Herrera <dherrera@redhat.com> 1.5.0-1
- First commit
