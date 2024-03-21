%global apiver 3.0
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glibmm24_version 2.54.0
%global gtk3_version 3.24.0
%global cairomm_version 1.12.0
%global pangomm_version 2.38.2
%global gdk_pixbuf2_version 2.35.5
%global atkmm_version 2.24.2

Name:           gtkmm3.0
Version:        3.24.9
Release:        %autorelease
Summary:        C++ interface for the GTK+ library

License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gtkmm/%{release_version}/gtkmm-%{version}.tar.xz

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig(atkmm-1.6) >= %{atkmm_version}
BuildRequires:  pkgconfig(cairomm-1.0) >= %{cairomm_version}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= %{gdk_pixbuf2_version}
BuildRequires:  pkgconfig(glibmm-2.4) >= %{glibmm24_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(pangomm-1.4) >= %{pangomm_version}

Requires:       atkmm%{?_isa} >= %{atkmm_version}
Requires:       cairomm%{?_isa} >= %{cairomm_version}
Requires:       gdk-pixbuf2%{?_isa} >= %{gdk_pixbuf2_version}
Requires:       glibmm2.4%{?_isa} >= %{glibmm24_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       pangomm%{?_isa} >= %{pangomm_version}

# Renamed in F37
Obsoletes:      gtkmm30 < %{version}-%{release}
Provides:       gtkmm30 = %{version}-%{release}
Provides:       gtkmm30%{?_isa} = %{version}-%{release}

%description
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Renamed in F37
Obsoletes:      gtkmm30-devel < %{version}-%{release}
Provides:       gtkmm30-devel = %{version}-%{release}
Provides:       gtkmm30-devel%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm2.4-doc
# Renamed in F37
Obsoletes:      gtkmm30-doc < %{version}-%{release}
Provides:       gtkmm30-doc = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%setup -q -n gtkmm-%{version}

# Copy demos before build to avoid including built binaries in -doc package
mkdir -p _docs
cp -a demos/ _docs/


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libgdkmm-%{apiver}.so.1*
%{_libdir}/libgtkmm-%{apiver}.so.1*

%files devel
%{_includedir}/gtkmm-%{apiver}/
%{_includedir}/gdkmm-%{apiver}/
%{_libdir}/libgdkmm-%{apiver}.so
%{_libdir}/libgtkmm-%{apiver}.so
%{_libdir}/gtkmm-%{apiver}/
%{_libdir}/gdkmm-%{apiver}/
%{_libdir}/pkgconfig/*.pc

%files doc
%doc %{_docdir}/gtkmm-%{apiver}/
%doc %{_datadir}/devhelp/
%doc _docs/*


%changelog
%autochangelog
