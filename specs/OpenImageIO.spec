%undefine __cmake_in_source_build
%global sover 2.5

Name:           OpenImageIO
Version:        2.5.16.0
Release:        4%{?dist}
Epoch:          1
Summary:        Library for reading and writing images

License:        BSD-3-Clause AND MIT
# The included fmtlib is MIT licensed
# src/include/OpenImageIO/fmt
URL:            https://openimageio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/v%{version}/%{name}-%{version}.tar.gz
# Images for test suite
#Source1:        https://github.com/OpenImageIO/oiio-images/archive/master/oiio-images.tar.gz

# LifHeif modifies the headers to make things work for multilib systems.
Patch0:         oiio-libheif_version.patch

# OpenVDB no longer builds for i686
ExcludeArch:    i686

# LibRaw on RHEL is only available on s390x and aarch64. As of RHEL 10 it looks
# like the package has moved back to EPEL and build for all architectures.
%if 0%{?rhel} >= 8 && 0%{?rhel} < 10
ExclusiveArch:  x86_64 ppc64le
%endif

# Utilities
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  txt2man
# Libraries
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
# Not currently in RHEL/EPEL
%if ! 0%{?rhel}
BuildRequires:  dcmtk-devel
%endif
BuildRequires:  fmt-devel
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  glew-devel
BuildRequires:  hdf5-devel
BuildRequires:  jasper-devel
# Only available on RPM Fusion
BuildRequires:  libheif-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  LibRaw-devel
BuildRequires:  libsquish-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  opencv-devel
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(OpenColorIO)
BuildRequires:  openjpeg2-devel
BuildRequires:  openssl-devel
BuildRequires:  openvdb-devel
BuildRequires:  pugixml-devel
BuildRequires:  ptex-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  robin-map-devel
# OpenVDB is locked to tbb 2020.3
BuildRequires:  cmake(tbb) = 2020.3
BuildRequires:  zlib-devel



%description
OpenImageIO is a library for reading and writing images, and a bunch of related
classes, utilities, and applications. Main features include:
- Extremely simple but powerful ImageInput and ImageOutput APIs for reading and
  writing 2D images that is format agnostic.
- Format plugins for TIFF, JPEG/JFIF, OpenEXR, PNG, HDR/RGBE, Targa, JPEG-2000,
  DPX, Cineon, FITS, BMP, ICO, RMan Zfile, Softimage PIC, DDS, SGI,
  PNM/PPM/PGM/PBM.
- An ImageCache class that transparently manages a cache so that it can access
  truly vast amounts of image data.


%package -n python3-openimageio
Summary:        Python 3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python3-openimageio}

%description -n python3-openimageio
Python bindings for %{name}.


%package utils
Summary:        Command line utilities for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description utils
Command-line tools to manipulate and get information on images using the
%{name} library.


%package iv
Summary:        %{name} based image viewer
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description iv
A really nice image viewer, iv, based on %{name} classes (and so will work
with any formats for which plugins are available).


%package devel
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
# The next two are required due to the binaries having cmake targets exported, see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1959632
Requires:       %{name}-iv%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-utils%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       opencv-devel
%if 0%{?fedora} > 34
Requires:       cmake(OpenEXR)
%else
Requires:       OpenEXR-devel ilmbase-devel
%endif

%description devel
Development files for package %{name}


%prep
%autosetup -p1

# Remove bundled pugixml
rm -f src/include/OpenImageIO/pugixml.hpp \
      src/include/OpenImageIO/pugiconfig.hpp \
      src/libutil/OpenImageIO/pugixml.cpp 

# Remove bundled tbb
rm -rf src/include/tbb

# Install test images
#mkdir ../oiio-images && pushd ../oiio-images
#tar --strip-components=1 -xzf %{SOURCE1}
#popd


%build
# CMAKE_SKIP_RPATH is OK here because it is set to FALSE internally and causes
# CMAKE_INSTALL_RPATH to be cleared, which is the desiered result.
mkdir build/linux && pushd build/linux
%cmake --debug-output -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_CXX_STANDARD=17 \
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
       -DPYTHON_VERSION=%{python3_version} \
       -DBUILD_DOCS:BOOL=TRUE \
	   -DOIIO_BUILD_TESTS:BOOL=FALSE \
       -DINSTALL_DOCS:BOOL=FALSE \
       -DINSTALL_FONTS:BOOL=FALSE \
       -DUSE_EXTERNAL_PUGIXML:BOOL=TRUE \
       -DSTOP_ON_WARNING:BOOL=FALSE \
       -DJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libjpeg) \
       -DOPENJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libopenjp2) \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DVERBOSE=TRUE

%cmake_build


%install
%cmake_install

# Move man pages to the right directory
pushd %{_vpath_builddir}
mkdir -p %{buildroot}%{_mandir}/man1
cp -a src/doc/*.1 %{buildroot}%{_mandir}/man1


%check
# Not all tests pass on linux
#pushd build/linux && make test


%files
%doc CHANGES.md CREDITS.md README.md
%license LICENSE.md THIRD-PARTY.md
%{_libdir}/libOpenImageIO.so.%{sover}*
%{_libdir}/libOpenImageIO_Util.so.%{sover}*

%files -n python3-openimageio
%{python3_sitearch}/%{name}/

%files utils
%exclude %{_bindir}/iv
%{_bindir}/*
%exclude %{_mandir}/man1/iv.1.gz
%{_mandir}/man1/*.1.gz

%files iv
%{_bindir}/iv
%{_mandir}/man1/iv.1.gz

%files devel
%{_libdir}/libOpenImageIO.so
%{_libdir}/libOpenImageIO_Util.so
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/


%changelog
* Tue Jan 28 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 1:2.5.16.0-4
- Roll back to 2.5.16.0 and add an Epoch

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 26 2024 Richard Shaw <hobbes1069@gmail.com> - 3.0.0.3-1
- Update to 3.0.0.3.

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 2.5.16.0-3
- Rebuild for hdf5 1.14.5

* Wed Oct 09 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.16.0-2
- Rebuild for OpenColorIO 2.4.0.

* Thu Oct 03 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.16.0-1
- Update to 2.5.16.0.

* Tue Sep 03 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.15.0-1
- Update to 2.5.15.0.

* Sat Aug 03 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.14.0-1
- Update to 2.5.14.0.

* Thu Jul 25 2024 Sérgio Basto <sergio@serjux.com> - 2.5.13.0-3
- Rebuild for opencv 4.10.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.13.0-1
- Update to 2.5.13.0.

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.5.12.0-2
- Rebuilt for Python 3.13

* Sun Jun 02 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.12.0-1
- Update to 2.5.12.0.

* Thu Apr 25 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.7.0-5
- Rebuilt for OpenColorIO 2.3.2

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.7.0-4
- Rebuilt for openexr 3.2.4

* Sun Apr 21 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.7.0-3
- Rebuild for OpenVDB 11 without backward-compatible ABI

* Tue Apr 02 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.7.0-2
- Rebuild for OpenVDB 11 with backward-compatible ABI

* Wed Feb 07 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.7.0-1
- Update to 2.5.7.0.

* Mon Feb 05 2024 Sérgio Basto <sergio@serjux.com> - 2.5.6.0-5
- Rebuild for opencv 4.9.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 2.5.6.0-2
- Rebuilt for Boost 1.83

* Thu Jan 18 2024 Richard Shaw <hobbes1069@gmail.com> - 2.5.6.0-1
- Update to 2.5.6.0.

* Thu Nov 09 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.17.0-1
- Update to 2.4.17.0.

* Fri Oct 27 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 2.4.16.0-2
- Rebuild for openvdb-10.1.0 (close RHBZ#2246603)

* Tue Oct 03 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.16.0-1
- Update to 2.4.16.0.

* Sun Sep 03 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.15.0-1
- Update to 2.4.15.0.
- Update License tag to SPDX identifiers.

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 2.4.14.0-2
- Rebuild for opencv 4.8.0

* Tue Aug 01 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.14.0-1
- Update to 2.4.14.0.

* Tue Aug 01 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.13.0-1
- Update to 2.4.13.0.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 2.4.12.0-3
- Rebuilt for Python 3.12

* Wed Jun 28 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 2.4.12.0-2
- Rebuilt due to fmt 10 update.

* Tue Jun 06 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.12.0-1
- Update to 2.4.12.0.

* Mon May 08 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.11.0-1
- Update to 2.4.11.0.

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 2.4.8.1-2
- Rebuilt for Boost 1.81

* Tue Feb 14 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.8.1-1
- Update to 2.4.8.1.

* Thu Feb 02 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.8.0-1
- Update to 2.4.8.0.

* Fri Jan 20 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.7.1-4
- Rebuild for opencv (again).

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 2.4.7.1-2
- Rebuild for opencv 4.7.0

* Wed Jan 04 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.7.1-1
- Update to 2.4.7.1.

* Mon Jan 02 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.7.0-1
- Update to 2.4.7.0.

* Mon Jan 02 2023 Richard Shaw <hobbes1069@gmail.com> - 2.4.6.1-2
- Rebuilt for OpenVDB.

* Thu Dec 22 2022 Richard Shaw <hobbes1069@gmail.com> - 2.4.6.1-1
- Update to 2.4.6.1.

* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 2.4.4.2-3
- LibRaw rebuild

* Tue Nov 15 2022 Richard Shaw <hobbes1069@gmail.com> - 2.4.4.2-2
- Rebuild for yaml-cpp 0.7.0.

* Fri Oct 07 2022 Richard Shaw <hobbes1069@gmail.com> - 2.4.4.2-1
- Update to 2.4.4.2.

* Thu Oct 06 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.20.0-1
- Update to 2.3.20.0.

* Thu Sep 01 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.19.0-1
- Update to 2.3.19.0.

* Thu Aug 04 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.3.18.0-2
- Rebuild for dcmtk 3.6.7 soname bump

* Mon Aug 01 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.18.0-1
- Update to 2.3.18.0.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.17.0-1
- Update to 2.3.17.0.

* Fri Jun 24 2022 Jonathan Wakely <jwakely@redhat.com> - 2.3.14.0-10
- Remove obsolete boost-python3-devel build dependency (#2100748)

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 2.3.14.0-9
- Rebuilt for opencv 4.6.0

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 2.3.14.0-8
- Really unbootstrap this time

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 2.3.14.0-7
- Unbootstrap

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 2.3.14.0-6
- Bootstrap for OpenColorIO with Python 3.11 and openvdb-9.1.0

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 2.3.14.0-5
- Rebuilt for opencv 4.6.0

* Sat May 21 2022 Sandro Mani <manisandro@gmail.com> - 2.3.14.0-4
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 2.3.14.0-3
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 2.3.14.0-2
- Rebuilt for Boost 1.78

* Mon Apr 04 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.14.0-1
- Update to 2.3.14.0.

* Wed Mar 02 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.13.0-1
- Update to 2.3.13.0.

* Tue Feb 01 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.12.0-1
- Update to 2.3.12.0, fixed BZ#2049299.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3.11.0-1
- Update to 2.3.11.0.

* Wed Dec 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.10.0-1
- Update to 2.3.10.0.

* Sun Nov 28 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.9.1-3
- Rebuild for OpenVDB 9.

* Mon Nov 22 2021 Orion Poplawski <orion@nwra.com> - 2.3.9.1-2
- Rebuild for hdf5 1.12.1

* Mon Nov 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.9.1-1
- Update to 2.3.9.1.
- Remove Field3D as it is now depreciated.

* Sun Oct 03 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.8.0-1
- Update to 2.3.8.0.

* Wed Sep 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.3.7.2-1
- Update to 2.3.7.2.

* Wed Sep 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.17.0-9
- Rebuild for OpenImageIO 2.1.

* Mon Aug 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.17.0-8
- Rebuild for OpenColorIO 2.

* Mon Aug 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.17.0-7
- Rebuild for OpenColorIO 2.

* Sat Aug 21 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.17.0-6
- Rebuild for OpenEXR/Imath 3.1.

* Fri Aug 20 2021 Orion Poplawski <orion@nwra.com> - 2.2.17.0-5
- Rebuild for hdf5 1.10.7

* Wed Aug 11 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.17.0-4
- Re-rebuild for dcmtk soname bump.

* Tue Aug 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.17.0-3
- Rebuild for boost 1.76

* Mon Aug 09 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.17.0-2
- Rebuild for soname bump in dcmtk.

* Wed Aug 04 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.17.0-1
- Update to 2.2.17.0.

* Sat Jul 31 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.16.0-3
- Rebuild for OpenEXR/Imath 3.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.16.0-1
- Update to 2.2.16.0.

* Tue Jun 15 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.15.0-1
- Update to 2.2.15.0.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.14.0-4
- Rebuilt for Python 3.10

* Thu May 20 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.14.0-3
- Add iv package as well, fixes #1959632.

* Wed May 19 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.14.0-2
- Require utils package in devel package, fixes #1959632.

* Sun May 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.14.0-1
- Update to 2.2.14.0.

* Sat Apr 03 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.13.0-1
- Update to 2.2.13.0.

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.12.0-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Mar 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.12.0-1
- Update to 2.2.12.0.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.11.1-1
- Update to 2.2.11.1.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 2.2.10.1-2
- Rebuilt for Boost 1.75

* Sat Jan 09 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.10.1-1
- Update to 2.2.10.1 for compatibility with upcoming OpenColorIO 2.

* Mon Jan 04 2021 Miro Hrončok <mhroncok@redhat.com> - 2.2.10.0-3
- Rebuilt for openvdb 8.0
- Fixes: rhbz#1912497

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.10.0-2
- Rebuild for OpenEXR 2.5.3.

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.10.0-1
- Update to 2.2.10.0.

* Wed Dec 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.9.0-1
- Update to 2.2.9.

* Mon Nov 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.8.0-1
- Update to 2.2.8.0.

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.2.7.0-2
- Rebuilt for OpenCV

* Thu Oct 01 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.7.0-1
- Update to 2.2.7.0.

* Wed Sep 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.6.1-1
- Update to 2.2.6.1.

* Thu Aug 20 2020 Simone Caronni <negativo17@gmail.com> - 2.1.18.1-2
- Rebuild for updated OpenVDB.

* Mon Aug 03 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.18.1-5
- Update to 2.1.18.1.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.17.0-3
- Rebuild for unannounced soname bump in libdc1394.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.17.0-1
- Update to 2.1.17.0.

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 2.1.16.0-3
- Rebuild for hdf5 1.10.6

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.16.0-2
- Rebuilt for OpenCV 4.3

* Tue Jun 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.16.0-1
- Update to 2.1.16.

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 2.1.15.0-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.15.0-3
- Rebuilt for Python 3.9

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.1.15.0-2
- Rebuild for new LibRaw

* Mon May 11 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.15.0-1
- Update to 2.1.15.0.
- Adds support for libRaw 0.20, fixes RHBZ#1833450.

* Sat May 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.14.0-1
- Update to 2.1.14.0.

* Sun Apr 12 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.13.0-2
- Rebuild for funky depdendency problem in Rawhide/33.

* Thu Apr 02 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.13.0-1
- Update to 2.1.13.

* Tue Mar 03 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.12.0-1
- Update to 2.1.12.0.

* Wed Feb 12 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.11.1-1
- Update to 2.1.11.0.

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1.10.1-3
- Rebuild for OpenCV 4.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.10.1-1
- Update to 2.1.10.1.

* Fri Jan 03 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.10.0-1
- Update to 2.1.10.

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 2.0.13-2
- Rebuilt for opencv4

* Wed Dec 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.13-1
- Update to 2.0.13.

* Fri Nov 29 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.12-1
- Update to 2.0.12.
- Add proper attribution for bundled fmtlib.

* Wed Oct 02 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.11-1
- Update to 2.0.11.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.10-2
- Rebuilt for Python 3.8

* Sun Aug 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.10-1
- Update to 2.0.10.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.9-1
- Update to 2.0.9.

* Sat May 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.8-1
- Update to 2.0.8.

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-3
- Rebuild for OpenEXR 2.3.0.

* Thu Apr 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-2
- Rebuild for OpenColorIO 1.1.1.

* Mon Apr 01 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.7-1
- Update to 2.0.7.

* Mon Mar 18 2019 Orion Poplawski <orion@nwra.com>
- Rebuild for hdf5 1.10.5

* Sun Mar 17 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.6-1
- Update to 2.0.6.

* Thu Mar 14 2019 Mohan Boddu <mboddu@bhujji.com> - 2.0.5-2
- Rebuilt for dcmtk 3.6.4

* Mon Feb 04 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.5-1
- Update to 2.0.5.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 2.0.4-2
- Rebuilt for Boost 1.69

* Sun Jan 06 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.4-1
- Update to 2.0.4:
  http://lists.openimageio.org/pipermail/oiio-dev-openimageio.org/2019-January/001391.html

* Sat Dec 08 2018 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-1
- Update to 2.0.3.

* Mon Dec 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.17-1
- Update to 1.8.17.

* Fri Nov 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.16-1
- Update to 1.8.16.

* Tue Oct 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.15-1
- Update to 1.8.15.

* Mon Sep 24 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.14-2
- Remove python2 module and replace with python3 module.

* Mon Sep 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.14-1
- Update to 1.8.14.

* Wed Jul 18 2018 Simone Caronni <negativo17@gmail.com> - 1.8.12-3
- Rebuild for LibRaw update.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.12-1
- Update to 1.8.12.

* Mon Apr 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.10-1
- Update to 1.8.10.

* Fri Mar 02 2018 Adam Williamson <awilliam@redhat.com> - 1.8.9-2
- Rebuild for opencv 3.4.1

* Thu Mar 01 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.9-1
- Update to 1.8.9

* Fri Feb 23 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.8-3
- Rebuild

* Tue Feb 13 2018 Sandro Mani <manisandro@gmail.com> - 1.8.8-2
- Rebuild (giflib)

* Fri Feb 02 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.8-1
- Update to 1.8.8.

* Thu Jan 18 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-3
- Add openjpeg2 to build dependencies.
- Re-enable dcmtk for 32bit arches.

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-2
- Rebuild for OpenColorIO 1.1.0.

* Wed Jan 03 2018 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-1
- Update to latest upstream release.
- Disable building with dcmtk until fixed, see:
  https://github.com/OpenImageIO/oiio/issues/1841

* Thu Nov 02 2017 Richard Shaw <hobbes1069@gmail.com> - 1.8.6-1
- Update to latest upstream release.
- Add dcmtk to build to enable DICOM plugin.
