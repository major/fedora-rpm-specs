Name:           wayqt
Version:        0.3.0
Release:        1%{?dist}
Summary:        The Qt-based library to handle Wayland and Wlroots protocols
License:        MIT
URL:            https://gitlab.com/desktop-frameworks/%{name}

Source0:        %{url}/-/archive/v%{version}/wayqt-v%{version}.tar.gz

# Fix for a build error with newer meson
# https://gitlab.com/desktop-frameworks/wayqt/-/work_items/7

Patch0: buildfix.patch

# Also fails to build with newer qt
# https://gitlab.com/desktop-frameworks/wayqt/-/merge_requests/5/diffs
Patch1: buildfix2.patch

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  wayland-devel
BuildRequires:  libpng-devel
# Explicitely requires the qt6 private libraries
BuildRequires:  qt6-qtbase-private-devel

%global _description \
A Qt-based library to handle Wayland and Wlroots protocols, to be used with \
any Qt project. \
Wayfire's private protocol is also supported. As the project develops, support \
for custom protocols may be added.

%description %{_description}

%package -n %{name}-devel
Summary:  Development subpackage for %{name}
Requires: %{name}%{?dist} = %{version}
%description -n %{name}-devel %{_description}

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install
# Delete empty release notes file
rm -f %{buildroot}%{docdir}/wayqt/ReleaseNotes

%check
%meson_test

%files
%doc README.md
%license LICENSE
%{_libdir}/libwayqt-qt6.so.0
%{_libdir}/libwayqt-qt6.so.%{version}

%files -n %{name}-devel
%{_includedir}/DFL/DF6/wayqt
%{_libdir}/libwayqt-qt6.so
%{_libdir}/pkgconfig/wayqt-qt6.pc

%changelog
* Tue Apr 23 2024 Steve Cossette <farchord@gmail.com> - 0.3.0-1
- Initital release of WayQt
