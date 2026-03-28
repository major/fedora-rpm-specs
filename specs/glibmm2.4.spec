%global apiver 2.4
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glib2_version 2.61.2
%global libsigc_version 2.9.1

Name:           glibmm2.4
Version:        2.66.8
Release:        %autorelease
Summary:        C++ interface for the GLib library

# Library sources are LGPL 2.1+, tools used to generate sources are GPL 2+.
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://gtkmm.org/
Source0:        https://download.gnome.org/sources/glibmm/%{release_version}/glibmm-%{version}.tar.xz

Patch0:         glibmm24-gcc11.patch

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Getopt::Long)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(sigc++-2.0) >= %{libsigc_version}

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       libsigc++20%{?_isa} >= %{libsigc_version}

# Renamed in F37
Obsoletes:      glibmm24 < %{version}-%{release}
Provides:       glibmm24 = %{version}-%{release}
Provides:       glibmm24%{?_isa} = %{version}-%{release}

# Do not export private Perl modules
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((DocsParser|Enum|Function|FunctionBase|GtkDefs|Object|Output|Property|Util|WrapParser)\\)

%description
glibmm is the official C++ interface for the popular cross-platform
library GLib. It provides non-UI API that is not available in standard
C++ and makes it possible for gtkmm to wrap GObject-based APIs.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Renamed in F37
Obsoletes:      glibmm24-devel < %{version}-%{release}
Provides:       glibmm24-devel = %{version}-%{release}
Provides:       glibmm24-devel%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       libsigc++20-doc
# Renamed in F37
Obsoletes:      glibmm24-doc < %{version}-%{release}
Provides:       glibmm24-doc = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%autosetup -p1 -n glibmm-%{version}


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install

chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/generate_wrap_init.pl
chmod +x $RPM_BUILD_ROOT%{_libdir}/glibmm-%{apiver}/proc/gmmproc


%files
%license COPYING COPYING.tools
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
