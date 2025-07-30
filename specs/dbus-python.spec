Name:    dbus-python
Version: 1.4.0
Release: %autorelease
Summary: D-Bus Python Bindings

License: MIT
URL:     http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0: http://dbus.freedesktop.org/releases/dbus-python/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
# for %%check
BuildRequires: dbus-x11
BuildRequires: python3-gobject

BuildRequires: gcc
BuildRequires: meson

%global _description\
D-Bus python bindings for use with python programs.

%description %_description

%package -n python3-dbus
Summary: D-Bus bindings for python3
%{?python_provide:%python_provide python3-dbus}
BuildRequires: python3-devel
# for py3_build
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(ninja)
BuildRequires: make

%description -n python3-dbus
%{summary}.

%package devel
Summary: Libraries and headers for dbus-python

%description devel
Headers and static libraries for hooking up custom mainloops to the dbus python
bindings.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%py3_install

%check
%meson_test

%files -n python3-dbus
%doc NEWS
%license COPYING
%{python3_sitearch}/*.so
%{python3_sitearch}/dbus/
%{python3_sitearch}/dbus_python*egg-info

%files devel
%doc README ChangeLog doc/API_CHANGES.txt doc/tutorial.txt
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
%autochangelog
