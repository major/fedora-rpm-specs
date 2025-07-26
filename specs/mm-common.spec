Name:           mm-common
Version:        1.0.7
Release:        2%{?dist}
Summary:        Common build files of the C++ bindings

BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://gtkmm.org
Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.xz

BuildRequires:  meson

Requires:       doxygen
Requires:       graphviz
Requires:       libxslt
Requires:       pkgconfig

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is a required dependency
to build glibmm and gtkmm from git.

%package docs
Summary:        Documentation for %{name}, includes example mm module skeleton
Requires:       %{name} = %{version}-%{release}

%description docs
Package contains short documentation for %{name} and example skeleton module,
which could be used as a base for new mm module.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS OVERVIEW.md README.md
%{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/aclocal/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pkgconfig/*.pc

%files docs
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog