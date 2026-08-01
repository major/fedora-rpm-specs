%global apiver 2.68

%global libsigc_version 3.0.0
%global glib2_version 2.81.0

Name:           glibmm2.68
Version:        2.88.1
Release:        %autorelease
Summary:        C++ interface for the GLib library

License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/glibmm/%{gnome_major_minor_version}/glibmm-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/glibmm/-/commit/d26083c41219958e802d5da733d4b4d3c342ec89
# Fix type definition conflict with GLib 2.89.2
# NOTE: Remove -Dmaintainer-mode=true from meson config, added Perl dependencies
# and make -doc again noarch when dropping this patch
Patch1:         glibmm2.68-2.88.1-glib_2.89.2-dont-derive-gtkmm-gxxx-types.patch

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(sigc++-3.0) >= %{libsigc_version}
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(feature)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Parser)

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libsigc++30%{?_isa} >= %{libsigc_version}

# Do not export private Perl modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)

%description
glibmm is the official C++ interface for the popular cross-platform
library GLib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.


%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the static libraries and header files needed for
developing glibmm applications.


%package        doc
Summary:        Documentation for %{name}, includes full API docs
# FIXME: Restore noarch once -Dmaintainer-mode=true is removed
# BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       libsigc++30-doc

%description    doc
This package contains the full API documentation for %{name}.


%prep
%autosetup -p1 -n glibmm-%{version}


%build
%meson -Dbuild-documentation=true \
    -Dmaintainer-mode=true
%meson_build


%install
%meson_install

chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/generate_wrap_init.pl
chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/gmmproc


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libgiomm-%{apiver}.so.1*
%{_libdir}/libglibmm-%{apiver}.so.1*
%{_libdir}/libglibmm_generate_extra_defs-%{apiver}.so.1*

%files devel
%{_includedir}/glibmm-%{apiver}/
%{_includedir}/giomm-%{apiver}/
%{_libdir}/*.so
%{_libdir}/glibmm-%{apiver}/
%{_libdir}/giomm-%{apiver}/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_datadir}/devhelp/
%doc %{_docdir}/glibmm-%{apiver}/


%changelog
%autochangelog
