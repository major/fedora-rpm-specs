%bcond docs 1

Name:     gmobile
Version:  0.4.0
Release:  %autorelease
Summary:  Functions useful in mobile related, glib based projects

# LGPL-2.1-or-later: src/
# GPL-3.0-or-later: examples/ tests/
License:  LGPL-2.1-or-later AND GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/gmobile
Source:   %{url}/-/archive/v%{version}/gmobile-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.78
BuildRequires:  pkgconfig(gio-2.0) >= 2.78
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.6.2
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  marshalparser
BuildRequires:  systemd
%if %{with docs}
BuildRequires:  gi-docgen
BuildRequires:  python3dist(docutils)
%endif

Requires:  systemd-udev

%description
gmobile carries some helpers for glib based environments on mobile devices.

%package devel
Summary:   Development headers for the gmobile library
Requires:  %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development headers for the gmobile library.

%if %{with docs}
%package docs
Summary:  Documentation for the gmobile library
# LGPL-2.1-or-later:
#  - *.html
# Apache-2.0 OR GPL-3.0-or-later:
#  - fonts.css
#  - main.js
#  - search.js
#  - style.css
# GPL-3.0-or-later:
#  - urlmap.js
# MIT:
#  - fzy.js
#  - solarized-dark.css
#  - solarized-light.css
License:  LGPL-2.1-or-later AND GPL-3.0-or-later AND (Apache-2.0 OR GPL-3.0-or-later) AND MIT

%description docs
Documentation for the gmobile library.
%endif

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson \
%if %{with docs}
    -Dgtk_doc=true \
    -Dman=true \
%endif
    -Dexamples=false \
    -Dvapi=false
%meson_build

%install
%meson_install
rm -v %{buildroot}/%{_libdir}/libgmobile.a

%check
%meson_test

%files
%doc README.md
%license COPYING COPYING.LIB
%{_libdir}/libgmobile.so.0
%{_libdir}/girepository-1.0
%if %{with docs}
%{_mandir}/man5/gmobile.udev.5.*
%endif
%{_udevrulesdir}/*.rules
%{_udevhwdbdir}/*.hwdb

%files devel
%{_includedir}/gmobile
%{_libdir}/libgmobile.so
%{_libdir}/pkgconfig/gmobile.pc
%{_datadir}/gir-1.0

%if %{with docs}
%files docs
%license COPYING COPYING.LIB
%doc examples/
%{_docdir}/gmobile-0/
%endif

%changelog
%autochangelog
