Name:           mpvqt
Version:        1.0.0
Release:        3%{?dist}
Summary:        QML wrapper for libmpv
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/libraries/mpvqt
Source:         https://download.kde.org/stable/mpvqt/mpvqt-%{version}.tar.xz

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
%autosetup


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
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 17 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.0-1
- 1.0.0

* Sun Dec 03 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 1.0.0~20231202gitac03349-1
- Initial import
