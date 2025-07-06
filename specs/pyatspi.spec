%global debug_package %{nil}

Name:           pyatspi
Version:        2.57.0
Release:        1%{?dist}
Summary:        Python bindings for at-spi

License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:        https://download.gnome.org/sources/pyatspi/2.57/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig(atk) >= 2.11.2
BuildRequires:  pkgconfig(atspi-2) >= 2.46
BuildRequires:  pkgconfig(dbus-1) >= 1.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.1

BuildRequires:  python3-dbus
BuildRequires:  python3-devel

BuildArch:      noarch

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python3 client library for at-spi.


%package -n python3-pyatspi
Summary:        Python3 bindings for at-spi
Requires:       at-spi2-core
Requires:       python3-gobject

%description -n python3-pyatspi
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python3 client library for at-spi.


%prep
%autosetup -p1


%build
%meson -Denable_tests=true
%meson_build


%install
%meson_install

# Fix up the shebang for python3 example
sed -i '1s|^#!/usr/bin/python|#!%{__python3}|' examples/magFocusTracker.py


%check
# Done by the 'build' step, with --enable-tests


%files -n python3-pyatspi
%license COPYING COPYING.GPL
%doc AUTHORS README.md
%doc examples/magFocusTracker.py
%{python3_sitelib}/pyatspi/


%changelog
%autochangelog
