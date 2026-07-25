%global soversion 0

Name:           test-drive
Version:        0.6.1
Release:        %autorelease
Summary:        The simple testing framework
License:        MIT OR Apache-2.0
URL:            https://github.com/fortran-lang/test-drive
Source0:        https://github.com/fortran-lang/test-drive/archive/v%{version}/%{name}-%{version}.tar.gz

# Better control of the module dir install path
Patch:          https://github.com/fortran-lang/test-drive/pull/69.patch

BuildRequires:  gcc-gfortran
BuildRequires:  cmake

%description
This project offers a lightweight, procedural unit testing framework
based on nothing but standard Fortran.

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
  -Dtest-drive-module-dir:STRING=test-drive


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE-Apache LICENSE-MIT
%doc README.md
%{_libdir}/libtest-drive.so.%{soversion}{,.*}

%files devel
%{_fmoddir}/test-drive/
%{_libdir}/pkgconfig/test-drive.pc
%{_libdir}/cmake/test-drive/
%{_libdir}/libtest-drive.so


%changelog
%autochangelog
