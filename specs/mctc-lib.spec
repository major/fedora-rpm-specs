%global soversion 0

Name:           mctc-lib
Version:        0.5.2
Release:        %autorelease
Summary:        Modular computation tool chain library
License:        Apache-2.0
URL:            https://grimme-lab.github.io/mctc-lib/
Source0:        https://github.com/grimme-lab/mctc-lib/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-gfortran
BuildRequires:  cmake
BuildRequires:  cmake(jonquil)
BuildRequires:  cmake(toml-f)
# For docs
BuildRequires:  rubygem-asciidoctor

%description
Common tool chain for working with molecular structure data in various
applications. This library provides a unified way to perform
operations on molecular structure data, like reading and writing to
common geometry file formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1


%conf
# TODO: Account for absolute path CMAKE_INSTALL_INCLUDEDIR so we can use %%{_fmoddir}
%cmake \
  -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_lib}/gfortran/modules \
  -Dmctc-lib-module-dir:STRING=mctc-lib \
  -DMCTCLIB_WITH_OpenMP:BOOL=ON \
  -DMCTCLIB_WITH_JSON:BOOL=ON


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_bindir}/mctc-convert
%{_libdir}/libmctc-lib.so.%{soversion}{,.*}

%files devel
%{_fmoddir}/mctc-lib/
%{_libdir}/cmake/mctc-lib/
%{_libdir}/pkgconfig/mctc-lib.pc
%{_libdir}/libmctc-lib.so


%changelog
%autochangelog
