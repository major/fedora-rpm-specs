%bcond qt5 %[%{undefined rhel} || 0%{?rhel} < 10]

Name:           qadwaitadecorations
Version:        0.1.4
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
%cmake -DHAS_QT6_SUPPORT=true
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
* Fri Jan 26 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.4-1
- 0.1.4

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jan Grulich <jgrulich@redhat.com> - 0.1.3-5
- Rebuild (qt5)

* Mon Dec 11 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-4
- Skip empty icon themes

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-3
- Rebuild (qt6)

* Wed Nov 22 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-2
- Backport upstream fixes and improvements
  - fix crash on forcing repaint on non-existing decorations
  - fix indentation of buttons when placed on the left side
  - apply correct button order
  - use Adwaita icons as fallback

* Mon Oct 16 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.3-1
- 0.1.3

* Sun Oct 15 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-5
- Upstream backport: do not use lambda function for DBus response

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-4
- Rebuild (qt6)

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-3
- Rebuild (qt5)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 0.1.2-2
- Rebuild for Qt Private API

* Wed Sep 27 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.2-1
- 0.1.2

* Mon Sep 11 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.1-1
- 0.1.1

* Tue Aug 15 2023 Jan Grulich <jgrulich@redhat.com> - 0.1.0
- Initial package
