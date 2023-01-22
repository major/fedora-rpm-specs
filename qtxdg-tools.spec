%define __cmake_in_source_build 1

Name:    qtxdg-tools
Summary: User tools for libqtxdg
Version: 3.10.0
Release: 2%{?dist}
License: LGPL-2.0-or-later
URL:     https://lxqt-project.org/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: pkgconfig(lxqt) >= 0.12.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: gcc-c++
Requires: cmake-filesystem

%description
%{summary}.

%prep
%setup -q

%build
%{cmake_lxqt} -DBUNDLE_XDG_UTILS=NO -DPULL_TRANSLATIONS=NO ..

make %{?_smp_mflags} -C %{_vpath_builddir}

%install
make install/fast DESTDIR=%{buildroot} -C %{_vpath_builddir}

%files
%{_bindir}/qtxdg-mat
%{_datadir}/cmake/qtxdg-tools/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Zamir SUN <sztsian@gmail.com> - 3.10.0-1
- Initial version
