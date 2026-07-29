%global soversion 0

Name:           jonquil
Version:        0.3.2
Release:        %autorelease
Summary:        Bringing TOML blooms to JSON land
License:        MIT OR Apache-2.0
URL:            https://toml-f.github.io/jonquil
Source0:        https://github.com/toml-f/jonquil/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-gfortran
BuildRequires:  cmake(toml-f)
BuildRequires:  cmake(test-drive)

%description
Jonquil is a JSON library for Fortran, built on top of TOML Fortran.
It provides a simple API for parsing and serializing JSON data, with
seamless interoperability with TOML data structures.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(toml-f)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%conf
# TODO: Account for absolute path CMAKE_INSTALL_INCLUDEDIR so we can use %%{_fmoddir}
%cmake \
  -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_lib}/gfortran/modules \
  -Djonquil-module-dir:STRING=jonquil


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE-MIT LICENSE-Apache
%doc README.md
%{_libdir}/libjonquil.so.%{soversion}{,.*}

%files devel
%{_fmoddir}/jonquil/
%{_libdir}/cmake/jonquil/
%{_libdir}/pkgconfig/jonquil.pc
%{_libdir}/libjonquil.so

%changelog
%autochangelog
