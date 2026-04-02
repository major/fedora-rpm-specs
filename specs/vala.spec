%global api_ver 0.56
%global priority 90

Name:           vala
Version:        0.56.19
Release:        %autorelease
Summary:        A modern programming language for GNOME

# Most files are LGPLv2.1+, curses.vapi is 2-clause BSD
License:        LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://wiki.gnome.org/Projects/Vala
Source0:        https://download.gnome.org/sources/%{name}/0.56/%{name}-%{version}.tar.xz
# warn instead of erroring out on unknown XML
# needed to build libadwaita on c10s and jhbuild but somehow not on f42
Patch0:         https://gitlab.gnome.org/GNOME/vala/-/merge_requests/423.patch#/%{name}-warn-on-unknown-xml.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphviz-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(gobject-2.0)
# only if Vala source files are patched
#BuildRequires:  vala

# for tests
BuildRequires:  dbus-x11

Requires: libvala%{?_isa} = %{version}-%{release}

# For GLib-2.0 and GObject-2.0 .gir files
Requires: gobject-introspection-devel

Provides: vala(api) = %{api_ver}
Provides: valac = %{version}-%{release}

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code. It's also planned to generate GIDL files when gobject-
introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.


%package -n     libvala
Summary:        Vala compiler library

%description -n libvala
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains the shared libvala library.


%package -n     libvala-devel
Summary:        Development files for libvala
Requires:       libvala%{?_isa} = %{version}-%{release}
# Renamed in F30
Provides:       vala-devel = %{version}-%{release}

%description -n libvala-devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files for libvala. This is not
necessary for using the %{name} compiler.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
# Don't require Devhelp on RHEL 10+ as it won't be available there,
# but continue to package the documentation in case of it gets packaged
# in EPEL
%if ! 0%{?rhel} || 0%{?rhel} < 10
Requires:       devhelp
%endif

%description    doc
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains documentation in a devhelp HTML book.


%package -n     valadoc
Summary:        Vala documentation generator
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libvala%{?_isa} = %{version}-%{release}

%description -n valadoc
Valadoc is a documentation generator for generating API documentation from Vala
source code.


%package -n     valadoc-devel
Summary:        Development files for valadoc
Requires:       valadoc%{?_isa} = %{version}-%{release}

%description -n valadoc-devel
Valadoc is a documentation generator for generating API documentation from Vala
source code.

The valadoc-devel package contains libraries and header files for
developing applications that use valadoc.


%prep
%autosetup -p1


%build
# The pre-generated compiler sources do not have the warning downgrades
# in vala-c99.patch.
%global build_type_safety_c 0
%configure
# Don't use rpath!
sed -i 's|/lib /usr/lib|/lib /usr/lib /lib64 /usr/lib64|' libtool
%make_build


%install
%make_install

# Avoid multilib conflicts in vala-gen-introspect
mv %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}{,-`uname -m`}
echo -e '#!/bin/sh\nexec %{_bindir}/vala-gen-introspect-%{api_ver}-`uname -m` "$@"' > \
  %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}
  chmod +x %{buildroot}%{_bindir}/vala-gen-introspect-%{api_ver}

find %{buildroot} -name '*.la' -delete


%check
# https://gitlab.gnome.org/GNOME/vala/-/issues/1416
export -n VALAFLAGS
%make_build check


%files
%license COPYING
%doc NEWS README.md
%{_bindir}/vala
%{_bindir}/vala-%{api_ver}
%{_bindir}/valac
%{_bindir}/valac-%{api_ver}
%{_bindir}/vala-gen-introspect
%{_bindir}/vala-gen-introspect-%{api_ver}*
%{_bindir}/vapigen
%{_bindir}/vapigen-%{api_ver}
%{_libdir}/pkgconfig/vapigen*.pc
%{_libdir}/vala-%{api_ver}/
%{_datadir}/aclocal/vala.m4
%{_datadir}/aclocal/vapigen.m4
%{_datadir}/vala/
%{_datadir}/vala-%{api_ver}/
%{_mandir}/man1/valac.1*
%{_mandir}/man1/valac-%{api_ver}.1*
%{_mandir}/man1/vala-gen-introspect.1*
%{_mandir}/man1/vala-gen-introspect-%{api_ver}.1*
%{_mandir}/man1/vapigen.1*
%{_mandir}/man1/vapigen-%{api_ver}.1*

%files -n libvala
%license COPYING
%{_libdir}/libvala-%{api_ver}.so.*

%files -n libvala-devel
%{_includedir}/vala-%{api_ver}
%{_libdir}/libvala-%{api_ver}.so
%{_libdir}/pkgconfig/libvala-%{api_ver}.pc

%files doc
%doc %{_datadir}/devhelp/books/vala-%{api_ver}

%files -n valadoc
%{_bindir}/valadoc
%{_bindir}/valadoc-%{api_ver}
%{_libdir}/libvaladoc-%{api_ver}.so.0*
%{_libdir}/valadoc-%{api_ver}/
%{_datadir}/valadoc-%{api_ver}/
%{_mandir}/man1/valadoc-%{api_ver}.1*
%{_mandir}/man1/valadoc.1*

%files -n valadoc-devel
%{_includedir}/valadoc-%{api_ver}/
%{_libdir}/libvaladoc-%{api_ver}.so
%{_libdir}/pkgconfig/valadoc-%{api_ver}.pc


%changelog
%autochangelog
