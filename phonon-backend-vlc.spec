%bcond qt5 %[!(0%{?rhel} >= 10)]
%bcond qt6 %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

Name:           phonon-backend-vlc
Summary:        VLC backend for Phonon
Version:        0.12.0
Release:        %autorelease
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/phonon-vlc
Source:         https://download.kde.org/stable/phonon/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++

BuildRequires:  pkgconfig(libvlc) >= 3.0.0

%if %{with qt5}
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(Phonon4Qt5) >= 4.12
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
%endif

%if %{with qt6}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Phonon4Qt6) >= 4.12
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
%endif

%global phonon_ver %(pkg-config --modversion phonon4qt5 2>/dev/null || echo 4.12)
%global vlc_ver %(pkg-config --modversion libvlc 2>/dev/null || echo 3.0.0)

%description
%{summary}.

%if %{with qt5}
%package -n phonon-qt5-backend-vlc
Summary:        VLC backend for PhononQt5
Provides:       phonon-qt5-backend%{?_isa} = %{phonon_ver}
Requires:       %{name}-common = %{version}-%{release}
Requires:       vlc-plugins-base%{?_isa} >= %{vlc_ver}
Requires:       phonon-qt5%{?_isa} >= %{phonon_ver}
%description -n phonon-qt5-backend-vlc
%{summary}.
%endif

%if %{with qt6}
%package -n phonon-qt6-backend-vlc
Summary:        VLC backend for PhononQt6
Provides:       phonon-qt6-backend%{?_isa} = %{phonon_ver}
Requires:       %{name}-common = %{version}-%{release}
Requires:       vlc-plugins-base%{?_isa} >= %{vlc_ver}
Requires:       phonon-qt6%{?_isa} >= %{phonon_ver}
%description -n phonon-qt6-backend-vlc
%{summary}.
%endif

%package common
Summary:        Translation files for %{name}
BuildArch:      noarch
%description common
%{summary}.

%prep
%autosetup -p1


%build
%if %{with qt5}
mkdir -p phononqt5
pushd phononqt5
%cmake_kf5 -S .. -DPHONON_BUILD_QT5:BOOL=ON -DPHONON_BUILD_QT6:BOOL=OFF
%cmake_build
popd
%endif

%if %{with qt6}
mkdir -p phononqt6
pushd phononqt6
%cmake_kf6 -S .. -DPHONON_BUILD_QT5:BOOL=OFF -DPHONON_BUILD_QT6:BOOL=ON
%cmake_build
popd
%endif


%install
%if %{with qt5}
pushd phononqt5
%cmake_install
popd
%endif

%if %{with qt6}
pushd phononqt6
%cmake_install
popd
%endif

%find_lang phonon_vlc --with-qt


%if %{with qt5}
%files -n phonon-qt5-backend-vlc
%doc AUTHORS
%license COPYING.LIB
%{_qt5_plugindir}/phonon4qt5_backend/phonon_vlc_qt5.so
%endif

%if %{with qt6}
%files -n phonon-qt6-backend-vlc
%doc AUTHORS
%license COPYING.LIB
%{_qt6_plugindir}/phonon4qt6_backend/phonon_vlc_qt6.so
%endif

%files common -f phonon_vlc.lang


%changelog
%autochangelog
