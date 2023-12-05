%global commit  ac0334979f8eae907ed50f280f2067d6d0df0b47
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mpvqt
Version:        1.0.0~20231202git%{shortcommit}
Release:        1%{?dist}
Summary:        QML wrapper for libmpv
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/libraries/mpvqt
Source:         %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  pkgconfig(mpv)

%description
MpvQt is a libmpv wrapper for Qt Quick 2/Qml.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Quick)
Requires:       pkgconfig(mpv)
%description devel
Development headers and link library for building packages which use %{name}.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/LGPL* LICENSES/LicenseRef-KDE*
%doc README.md
%{_libdir}/libMpvQt.so.1{,.*}

%files devel
%{_includedir}/MpvQt/
%{_libdir}/libMpvQt.so
%{_libdir}/cmake/MpvQt/


%changelog
* Sun Dec 03 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 1.0.0~20231202gitac03349-1
- Initial import
