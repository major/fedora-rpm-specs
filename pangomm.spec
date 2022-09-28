%define apiver 1.4
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glibmm_version 2.48.0
%global cairomm_version 1.2.2
%global pango_version 1.45.1

Name:           pangomm
Version:        2.46.3
Release:        %autorelease
Summary:        C++ interface for Pango

License:        LGPLv2+
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/pangomm/%{release_version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(cairomm-1.0) >= %{cairomm_version}
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  glibmm2.4-devel >= %{glibmm_version}
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pango-devel >= %{pango_version}

Requires:       glibmm2.4%{?_isa} >= %{glibmm_version}
Requires:       cairomm1.0%{?_isa} >= %{cairomm_version}
Requires:       pango%{?_isa} >= %{pango_version}

%description
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and header files needed for
developing pangomm applications.


%package          doc
Summary:          Developer's documentation for the pangomm library
BuildArch:        noarch
Requires:         %{name} = %{version}-%{release}
Requires:         libsigc++20-doc
Requires:         glibmm2.4-doc

%description      doc
This package contains developer's documentation for the pangomm
library. Pangomm is the C++ API for the Pango font layout library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep
%autosetup -p1 -n pangomm-%{version}


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libpangomm-%{apiver}.so.1*


%files devel
%{_includedir}/pangomm-%{apiver}
%{_libdir}/libpangomm-%{apiver}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-%{apiver}

%files doc
%doc %{_docdir}/pangomm-%{apiver}/
%{_datadir}/devhelp/


%changelog
%autochangelog
