%bcond_without docs

Name:           libv3270
Version:        5.4
Release:        %autorelease
Summary:        3270 Virtual Terminal for GTK+3

License:        LGPLv3
URL:            https://github.com/PerryWerneck/libv3270
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fixing configure.ac
# Backport of https://github.com/PerryWerneck/libv3270/commit/1ffec2d7c84b92a175d5d193d57654a14b96fa79
Patch0:         libv3270-fix-autotools.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  lib3270-devel
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif

%description
Originally designed as part of the pw3270 application, this library provides a
TN3270 virtual terminal widget for GTK+3.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3-devel%{?_isa}
Requires:       lib3270-devel%{?_isa}
Requires:       glade-libs%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.
%endif

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
autopoint
%configure
# override SHELL to make the build more verbose
%make_build all SHELL='sh -x'
%if %{with docs}
doxygen doxygen
%endif

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_libdir}/%{name}.so.5*
%{_datadir}/pw3270/colors.conf
%{_datadir}/pw3270/remap

%files devel
%{_datadir}/glade/catalogs/v3270.xml
%{_datadir}/glade/pixmaps/hicolor/*/actions/*.png
%{_datadir}/pw3270/pot/%{name}.pot
%{_includedir}/v3270.h
%{_includedir}/v3270
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc

%if %{with docs}
%files doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog
