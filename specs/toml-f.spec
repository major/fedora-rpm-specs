%global soversion 0

Name:           toml-f
Version:        0.5.2
Release:        %autorelease
Summary:        TOML parser implementation for data serialization and deserialization in Fortran
License:        MIT OR Apache-2.0
URL:            https://toml-f.readthedocs.io/
Source0:        https://github.com/toml-f/toml-f/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-gfortran
BuildRequires:  cmake(test-drive)

%description
A TOML parser implementation for data serialization and deserialization in
Fortran.

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
  -Dtoml-f-module-dir:STRING=toml-f


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE-MIT LICENSE-Apache
%doc README.md
%{_libdir}/libtoml-f.so.%{soversion}{,.*}

%files devel
%{_fmoddir}/toml-f/
%{_libdir}/cmake/toml-f/
%{_libdir}/pkgconfig/toml-f.pc
%{_libdir}/libtoml-f.so

%changelog
%autochangelog
