%global sover           3
%global aom_version     v3.13.1

%if 0%{?fedora} || 0%{?rhel} >= 9
%ifarch x86_64
%bcond_without vmaf
%endif
%if 0%{?fedora} > 40 || 0%{?rhel} > 9
%bcond_with jpegxl
%else
%bcond_without jpegxl
%endif
%endif

Name:       aom
Version:    3.13.1
Release:    %autorelease
Summary:    Royalty-free next-generation video format

License:    BSD-3-Clause
URL:        http://aomedia.org/
Source:     https://aomedia.googlesource.com/%{name}/+archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://aomedia.issues.chromium.org/issues/448994065
Patch:      0001-cmake-fix-nasm-detection-w-3.0.patch
# Building static library breaks .cmake files if we don't ship it, so drop it
Patch:      aom-nostatic.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  git-core
# BuildRequires:  graphviz
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  python3-devel
BuildRequires:  nasm
%if %{with jpegxl}
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libhwy)
%endif
%if %{with vmaf}
BuildRequires:  pkgconfig(libvmaf)
%endif

Provides:       av1 = %{version}-%{release}
Requires:       libaom%{?_isa} = %{version}-%{release}

%description
The Alliance for Open Media’s focus is to deliver a next-generation
video format that is:

 - Interoperable and open;
 - Optimized for the Internet;
 - Scalable to any modern device at any bandwidth;
 - Designed with a low computational footprint and optimized for hardware;
 - Capable of consistent, highest-quality, real-time video delivery; and
 - Flexible for both commercial and non-commercial content, including
   user-generated content.

This package contains the reference encoder and decoder.

%package -n libaom
Summary:        Library files for aom

%description -n libaom
Library files for aom, the royalty-free next-generation
video format.

%package -n libaom-devel
Summary:        Development files for aom
# cmake files assume /usr/bin/aomdec is present
Requires:       aom%{?_isa} = %{version}-%{release}
Requires:       libaom%{?_isa} = %{version}-%{release}

%description -n libaom-devel
Development files for aom, the royalty-free next-generation
video format.

%package -n libaom-devel-docs
Summary:        Documentation for libaom
Requires:       libaom-devel%{?_isa} = %{version}-%{release}

%description -n libaom-devel-docs
Documentation for libaom, the royalty-free next-generation
video format.

%prep
%autosetup -p1 -c %{name}-%{version}
# Set GIT revision in version
sed -i 's@set(aom_version "")@set(aom_version "%{aom_version}")@' build/cmake/version.cmake
# Disable PDF generation which is buggy
sed -i "s@GENERATE_LATEX         = YES@GENERATE_LATEX         = NO@" libs.doxy_template

%build
%cmake3 -DENABLE_CCACHE=1 \
        -DCMAKE_SKIP_RPATH=1 \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DCONFIG_WEBM_IO=1 \
        -DENABLE_DOCS=1 \
        -DENABLE_TESTS=0 \
        -DCONFIG_ANALYZER=0 \
        -DBUILD_SHARED_LIBS=1 \
%if %{with jpegxl}
        -DCONFIG_TUNE_BUTTERAUGLI=1 \
%endif
%if %{with vmaf}
        -DCONFIG_TUNE_VMAF=1 \
%endif
        %{nil}
%cmake3_build

%install
%cmake3_install

%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE PATENTS
%{_bindir}/aomdec
%{_bindir}/aomenc

%files -n libaom
%license LICENSE PATENTS
%{_libdir}/libaom.so.%{sover}*

%files -n libaom-devel
%{_includedir}/%{name}
%{_libdir}/libaom.so
%{_libdir}/cmake/AOM/
%{_libdir}/pkgconfig/%{name}.pc

%files -n libaom-devel-docs
%doc %{_vpath_builddir}/docs/html/

%changelog
%autochangelog
