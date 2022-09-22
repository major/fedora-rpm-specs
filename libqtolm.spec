%global appname QtOlm
%global libname lib%{appname}

Name: libqtolm
Version: 3.0.1
Release: 5%{?dist}

License: GPLv3+
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
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jun 30 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 3.0.1-1
- Updated to version 3.0.1.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20190930gitf2d8e23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0-4.20190930gitf2d8e23
- Updated to latest Git snapshot.
