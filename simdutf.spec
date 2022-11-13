Name:           simdutf
Version:        2.0.2
Release:        %autorelease
Summary:        Unicode validation and transcoding at billions of characters per second

License:        Apache-2.0 AND BSD-3-Clause
# All files are Apache-2.0, except simdutf-2.0.2/include/simdutf/internal/isadetection.h is BSD-3-Clause
URL:			https://github.com/simdutf/simdutf
Source0:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:			simdutf-fix-cmake.patch

ExcludeArch:	s390 s390x

BuildRequires:  cmake
BuildRequires:	gcc-c++
%ifnarch %{arm}
BuildRequires:	libasan
%endif

%description
Unicode (UTF8, UTF16, UTF32) validation and transcoding at billions of 
characters per second using SSE2, AVX2, NEON, AVX-512.

%package devel
Summary: Development files for %{name}

%description devel
The package contains libraries and header files for developing applications
that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1
rm -rf benchmarks

%build
%cmake -DSIMDUTF_BENCHMARKS=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE-APACHE
%doc AUTHORS README.md
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}*.so

%changelog
%autochangelog
