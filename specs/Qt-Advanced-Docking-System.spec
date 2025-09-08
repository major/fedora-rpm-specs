Name:           Qt-Advanced-Docking-System
Summary:        Advanced Docking System for Qt
Version:        4.4.1
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND BSL-1.0 AND Apache-2.0
URL:            https://github.com/githubuser0xFFFF/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)

# Required on lower Fedora Versions (41?)
BuildRequires:  qt6-qtbase-private-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake -DADS_VERSION=%{version}
%cmake_build

%install
%cmake_install
# Already included by rpm
rm -rfv %{buildroot}%{_prefix}/license/ads
rm -rfv %{buildroot}%{_datadir}/ads/license

%files
%license LICENSE gnu-lgpl-v2.1.md
%doc README.md
%{_libdir}/libqtadvanceddocking-qt6.so.%{version}

%files devel
%{_includedir}/qtadvanceddocking-qt6/
%{_libdir}/cmake/qtadvanceddocking-qt6/
%{_libdir}/libqtadvanceddocking-qt6.so

%changelog
* Sat Sep 06 2025 Steve Cossette <farchord@gmail.com> - 4.4.1-1
- 4.4.1

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Dec 17 2024 Steve Cossette <farchord@gmail.com> - 4.4.0-1
- 4.4.0
