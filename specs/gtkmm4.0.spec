%global apiver 4.0
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glibmm_version 2.68.0
%global gtk4_version 4.15.5
%global cairomm_version 1.15.4
%global pangomm_version 2.50.0
%global gdk_pixbuf2_version 2.35.5

Name:           gtkmm4.0
Version:        4.17.0
Release:        %autorelease
Summary:        C++ interface for the GTK+ library

License:        LGPL-2.1-or-later
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/gtkmm/%{release_version}/gtkmm-%{version}.tar.xz

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig(cairomm-1.16) >= %{cairomm_version}
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= %{gdk_pixbuf2_version}
BuildRequires:  pkgconfig(glibmm-2.68) >= %{glibmm_version}
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(pangomm-2.48) >= %{pangomm_version}

Requires:       cairomm1.16%{?_isa} >= %{cairomm_version}
Requires:       gdk-pixbuf2%{?_isa} >= %{gdk_pixbuf2_version}
Requires:       glibmm2.68%{?_isa} >= %{glibmm_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       pangomm2.48%{?_isa} >= %{pangomm_version}

%description
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        API documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm2.68-doc

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
%{_libdir}/libgtkmm-%{apiver}.so.0*

%files devel
%{_includedir}/gtkmm-%{apiver}/
%{_libdir}/libgtkmm-%{apiver}.so
%{_libdir}/gtkmm-%{apiver}/
%{_libdir}/pkgconfig/gtkmm-%{apiver}.pc

%files doc
%doc %{_docdir}/gtkmm-%{apiver}/
%doc %{_datadir}/devhelp/
%doc _docs/*


%changelog
%autochangelog
