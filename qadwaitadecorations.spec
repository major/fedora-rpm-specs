%bcond qt5 %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           qadwaitadecorations
Version:        0.1.1
Release:        1%{?dist}
Summary:        Qt decoration plugin implementing Adwaita-like client-side decorations

License:        LGPL-2.1-or-later
URL:            https://github.com/FedoraQt/QAdwaitaDecorations
Source0:        https://github.com/FedoraQt/QAdwaitaDecorations/archive/%{version}/QAdwaitaDecorations-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  wayland-devel

%description
%{summary}.

%if %{with qt5}
%package qt5
Summary:        Qt decoration plugin implementing Adwaita-like client-side decorations
BuildRequires:  qt5-qtbase-devel >= 5.15.2
BuildRequires:  qt5-qtbase-static >= 5.15.2
BuildRequires:  qt5-qtwayland-devel >= 5.15.2
BuildRequires:  qt5-qtbase-private-devel >= 5.15.2
BuildRequires:  qt5-qtsvg-devel >= 5.15.2
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

# When GNOME Shell and Qt 5 are installed, we want this by default
Supplements:   (qt5-qtbase and gnome-shell)

%description qt5
%{summary}.
%endif

%package qt6
Summary:        Qt decoration plugin implementing Adwaita-like client-side decorations
BuildRequires:  qt6-qtbase-devel >= 6.5.0
BuildRequires:  qt6-qtbase-static >= 6.5.0
BuildRequires:  qt6-qtwayland-devel >= 6.5.0
BuildRequires:  qt6-qtbase-private-devel >= 6.5.0
BuildRequires:  qt6-qtsvg-devel >= 6.5.0
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

# When GNOME Shell and Qt 6 are installed, we want this by default
Supplements:   (qt6-qtbase and gnome-shell)

%description qt6
%{summary}.


%prep
%autosetup -p1 -n  QAdwaitaDecorations-%{version}

%build
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake
%cmake_build
%endif

%global _vpath_builddir %{_target_platform}-qt6
%cmake -DUSE_QT6=true
%cmake_build

%install
%if %{with qt5}
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%if %{with qt5}
%files qt5
%doc README.md
%license LICENSE
%{_qt5_plugindir}/wayland-decoration-client/libqadwaitadecorations.so
%endif

%files qt6
%doc README.md
%license LICENSE
%{_qt6_plugindir}/wayland-decoration-client/libqadwaitadecorations.so

%changelog
* Mon Sep 11 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.1-1
- 0.1.1

* Tue Aug 15 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.0
- Initial package
