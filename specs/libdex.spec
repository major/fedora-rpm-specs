%global tarball_version %%(echo %{version} | tr '~' '.')

Name:    libdex
Version: 1.1~alpha
Release: %autorelease
Summary: a library supporting "Deferred Execution" for GNOME and GTK

License: LGPL-2.1-or-later
URL:     https://gitlab.gnome.org/GNOME/libdex
Source0: https://download.gnome.org/sources/libdex/1.1/%{name}-%{tarball_version}.tar.xz

BuildRequires: /usr/bin/vapigen
BuildRequires: gcc
BuildRequires: gi-docgen
BuildRequires: libatomic
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: python3-gobject-base
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(liburing)
BuildRequires: pkgconfig(sysprof-capture-4)

%description
Dex is a library supporting "Deferred Execution" with the explicit goal
of integrating with GNOME and GTK-based applications.
It provides primatives for supporting futures in a variety of ways with both
read-only and writable views. Additionally, integration with existing
asynchronous-based APIs is provided through the use of wrapper promises.
"Fibers" are implemented which allows for writing synchronous looking code
which calls asynchronous APIs from GIO underneath.

%package  devel
Summary:  Development files for libdex
Requires: libdex%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed for
writing applications with libdex.

%package   devel-docs
Summary:   Developer documentation for libdex
BuildArch: noarch
Requires:  libdex = %{version}-%{release}

%description devel-docs
This package contains developer documentation for writing applications with
libdex.

%package -n  python3-libdex
Summary:     Python3 bindings for %{name}
BuildArch:   noarch
Requires:    %{name} = %{version}-%{release}
Requires:    python3-gobject-base-noarch

%description -n python3-libdex
This package contains the python3 bindings for %{name}

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
  -Ddocs=true \
  -Dexamples=false \
  -Dsysprof=true
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libdex-1.so.1{,.*}
%{_libdir}/girepository-1.0/

%files devel
%{_datadir}/gir-1.0/
%{_datadir}/vala/
%{_includedir}/libdex-1/
%{_libdir}/libdex-1.so
%{_libdir}/pkgconfig/libdex-1.pc

%files devel-docs
%doc %{_docdir}/libdex-1/

%files -n python3-libdex
%pycached %{python3_sitelib}/gi/overrides/Dex.py
%dir %{_libexecdir}/libdex-1
%{_libexecdir}/libdex-1/dex-gdbus-codegen-extension.py

%changelog
%autochangelog
