Name:    ksanecore
Summary: Library providing logic to interface scanners
Version: 23.04.1
Release: 1%{?dist}

License: BSD and LGPLv2.1-only and LGPLv3.0-only
URL:     https://invent.kde.org/libraries/ksanecore
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Core)
BuildRequires: pkgconfig(sane-backends)

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{version}


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf5_libdir}/libKSaneCore.so.*

%files devel
%{_includedir}/KSaneCore/*
%{_kf5_libdir}/cmake/KSaneCore/*
%{_kf5_libdir}/libKSaneCore.so


%changelog
* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Wed Dec 21 2022 Justin Zobel <justin@1707.io> - 22.12.0-1
- Initial inclusion
