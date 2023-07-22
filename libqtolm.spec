%global appname QtOlm
%global libname lib%{appname}

Name: libqtolm
Version: 3.0.1
Release: 7%{?dist}

License: GPL-3.0-or-later
URL: https://gitlab.com/b0/%{name}
Summary: Qt wrapper for libolm
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Special Qt wrapper for libolm library.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-v%{version}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH="include/%{appname}"
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/%{libname}.so.3*

%files devel
%{_includedir}/%{appname}/
%{_libdir}/cmake/%{appname}/
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/%{libname}.so

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
