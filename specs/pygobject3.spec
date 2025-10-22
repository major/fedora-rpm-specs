%define glib2_version                  2.80.0
%define gobject_introspection_version  1.81.0
%define pycairo_version                1.16.0
%define python3_version                3.8

Name:           pygobject3
Version:        3.54.5
Release:        %autorelease
Summary:        Python bindings for GObject Introspection

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/PyGObject
Source0:        https://download.gnome.org/sources/pygobject/3.54/pygobject-%{version}.tar.gz

BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(py3cairo) >= %{pycairo_version}
BuildRequires:  meson
BuildRequires:  python3-devel >= %{python3_version}
BuildRequires:  python3-setuptools
# Test dependencies.
# Keep TEST_GTK_VERSION in %%check in sync with gtk version used here
BuildRequires:  python3dist(pytest)
BuildRequires:  gtk3
BuildRequires:  xwayland-run
BuildRequires:  mutter
BuildRequires:  mesa-dri-drivers

%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package     -n python3-gobject
Summary:        Python 3 bindings for GObject Introspection
Requires:       python3-gobject-base%{?_isa} = %{version}-%{release}
# The cairo override module depends on this
Requires:       python3-cairo%{?_isa} >= %{pycairo_version}

%description -n python3-gobject
The python3-gobject package provides a convenient wrapper for the GObject 
library and and other libraries that are compatible with GObject Introspection, 
for use in Python 3 programs.

%package     -n python3-gobject-base
Summary:        Python 3 bindings for GObject Introspection base package
Requires:       gobject-introspection%{?_isa} >= %{gobject_introspection_version}
# Noarch package removed in F40.
Obsoletes:      python3-gobject-base-noarch < 3.46.0-5
Provides:       python3-gobject-base-noarch = %{version}-%{release}

%description -n python3-gobject-base
This package provides the non-cairo specific bits of the GObject Introspection
library.

%package     -n python3-gobject-devel
Summary:        Development files for embedding PyGObject introspection support
Requires:       python3-gobject%{?_isa} = %{version}-%{release}
Requires:       gobject-introspection-devel%{?_isa}

%description -n python3-gobject-devel
This package contains files required to embed PyGObject

%prep
%autosetup -n pygobject-%{version} -p1

%build
%meson -Dpython=%{__python3}
%meson_build

%install
%meson_install

%check
export TEST_GTK_VERSION=3.0
# The refcounting tests fail with Python 3.14
# Reported: https://gitlab.gnome.org/GNOME/pygobject/-/issues/694
export PYTEST_ADDOPTS="-k 'not (ref_count or has_two_refs)'"
# Tests are disabled until Xwayland can run in mock (i.e. it finds
# /tmp/.X11-unix owned by root).
%{shrink:xwfb-run -c mutter -- %meson_test --timeout-multiplier=5 || exit 0}


%files -n python3-gobject
%{python3_sitearch}/gi/_gi_cairo*.so

%files -n python3-gobject-base
%license COPYING
%doc NEWS
%dir %{python3_sitearch}/gi/
%{python3_sitearch}/gi/overrides/
%{python3_sitearch}/gi/repository/
%pycached %{python3_sitearch}/gi/*.py
%{python3_sitearch}/gi/_gi.*.so
%{python3_sitearch}/PyGObject-*.dist-info/
%{python3_sitearch}/pygtkcompat/

%files -n python3-gobject-devel
%dir %{_includedir}/pygobject-3.0/
%{_includedir}/pygobject-3.0/pygobject.h
%{_libdir}/pkgconfig/pygobject-3.0.pc

%changelog
%autochangelog
