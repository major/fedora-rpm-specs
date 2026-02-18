%undefine __cmake_in_source_build
%global sover 2.5

Name:           OpenImageIO2.5
Version:        2.5.19.1
Release:        9%{?dist}
Summary:        Library for reading and writing images

License:        BSD-3-Clause AND MIT
# The included fmtlib is MIT licensed
# src/include/OpenImageIO/fmt
URL:            https://openimageio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenImageIO/archive/v%{version}/OpenImageIO-%{version}.tar.gz

# LifHeif modifies the headers to make things work for multilib systems.
Patch0:         oiio-libheif_version.patch

# OpenVDB no longer builds for i686
ExcludeArch:    i686


# Utilities
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  txt2man
# Libraries
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  dcmtk-devel
BuildRequires:  fmt-devel
BuildRequires:  freetype-devel
BuildRequires:  giflib-devel
BuildRequires:  glew-devel
BuildRequires:  hdf5-devel
BuildRequires:  jasper-devel
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


%package devel
Summary:        Documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencv-devel
Requires:       cmake(OpenEXR)
Requires:       OpenEXR-devel ilmbase-devel
Conflicts:      OpenImageIO-devel

%description devel
Development files for package %{name}


%prep
%autosetup -p1 -n OpenImageIO-%{version}

# Remove bundled pugixml
rm -f src/include/OpenImageIO/pugixml.hpp \
      src/include/OpenImageIO/pugiconfig.hpp \
      src/libutil/OpenImageIO/pugixml.cpp 

# Remove bundled tbb
rm -rf src/include/tbb


%build
# CMAKE_SKIP_RPATH is OK here because it is set to FALSE internally and causes
# CMAKE_INSTALL_RPATH to be cleared, which is the desiered result.
mkdir build/linux && pushd build/linux
%cmake  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_CXX_STANDARD=17 \
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
       -DBUILD_DOCS:BOOL=FALSE \
	   -DOIIO_BUILD_TESTS:BOOL=FALSE \
       -DINSTALL_DOCS:BOOL=FALSE \
       -DINSTALL_FONTS:BOOL=FALSE \
       -DUSE_EXTERNAL_PUGIXML:BOOL=TRUE \
       -DSTOP_ON_WARNING:BOOL=FALSE \
       -DJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libjpeg) \
       -DOPENJPEG_INCLUDE_DIR=$(pkgconf --variable=includedir libopenjp2) \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DVERBOSE=TRUE \
	   -USE_PYTHON=FALSE

%cmake_build


%install
%cmake_install

# Delete everything but the library as we don't want anything to conflict with
# the main package.
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{python3_sitearch}


%files
%doc CHANGES.md CREDITS.md README.md
%license LICENSE.md THIRD-PARTY.md
%{_libdir}/libOpenImageIO.so.%{sover}*
%{_libdir}/libOpenImageIO_Util.so.%{sover}*

%files devel
%{_libdir}/libOpenImageIO.so
%{_libdir}/libOpenImageIO_Util.so
%{_libdir}/cmake/OpenImageIO/*.cmake
%{_libdir}/pkgconfig/OpenImageIO.pc
%{_includedir}/OpenImageIO/


%changelog
* Mon Feb 16 2026 Gwyn Ciesla <gwync@protonmail.com> - 2.5.19.1-9
- LibRaw rebuild

* Mon Feb 02 2026 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.19.1-8
- Rebuilt for ptex 2.5.1 (close RHBZ#2435886)

* Thu Jan 29 2026 Nicolas Chauvet <kwizart@gmail.com> - 2.5.19.1-7
- Rebuilt for OpenCV 4.13

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.19.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.19.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Dec 11 2025 Nicolas Chauvet <kwizart@gmail.com> - 2.5.19.1-4
- Rebuilt for OpenCV-4.12

* Sun Nov 23 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.19.1-3
- Rebuilt for OpenVDB 13.0.0

* Thu Oct 02 2025 Richard Shaw <hobbes1069@gmail.com> - 2.5.19.1-2
- Rebuild for OpenVDB 12.1.1.

* Thu Sep 11 2025 Richard Shaw <hobbes1069@gmail.com> - 1:2.5.19.1-1
- Initial release of compatibility package.
