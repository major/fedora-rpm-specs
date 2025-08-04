Name:           tinyexr
Version:        1.0.7
Release:        %autorelease
Summary:        Small library to load and save OpenEXR images
 
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/syoyo/%{name}
Source0:        https://github.com/syoyo/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        LICENSE
# Import Timo Röhling build patches from Debian.
Patch1:         0002-Explicitly-export-required-symbols.patch
Patch2:         0003-Fix-CMake-build-system.patch
Patch3:         0004-Add-test-executable-for-CTest.patch
# Fix detection of miniz built with upstream cmake
Patch4:         %{name}-miniz.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  sed
BuildRequires:  miniz-devel

%description
TinyEXR is a small library to load and save OpenEXR images. It supports
the version 1 format and version 2 multi-part images, and it has partial
support for version 2 deep images.
 
%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
Summary:        Development files for %{name}
 
%description devel
%{summary}.


%prep
%autosetup -p1
cp %{SOURCE1} LICENSE

# Remove all thirdparty libraries
rm -rf deps

%build
%cmake

%cmake_build
# Remove static declarations from headers
sed -i '/^#ifdef TINYEXR_IMPLEMENTATION$/,/^#endif  \/\/ TINYEXR_IMPLEMENTATION$/d' tinyexr.h

%ifnarch s390x
%check
%ctest
%endif

%install
%cmake_install
 
%files
%doc README.md
%license LICENSE
%{_libdir}/libtinyexr.so.1{,.*}
 
%files devel
%{_includedir}/tinyexr.h
%{_libdir}/libtinyexr.so
%{_libdir}/cmake/tinyexr/


%changelog
%autochangelog