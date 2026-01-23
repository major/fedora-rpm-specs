Name:           mpvqt
Version:        1.1.1
Release:        %autorelease
Summary:        QML wrapper for libmpv
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/libraries/mpvqt
Source:         https://download.kde.org/%{stable_kf6}/mpvqt/mpvqt-%{version}.tar.xz

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
%{_libdir}/libMpvQt.so.{2,%{version}}

%files devel
%{_includedir}/MpvQt/
%{_libdir}/libMpvQt.so
%{_libdir}/cmake/MpvQt/


%changelog
%autochangelog
