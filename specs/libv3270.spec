%bcond docs 1
%global major_sover 5
%global minor_sover 5

Name:           libv3270
Version:        5.5.0
Release:        %autorelease
Summary:        3270 Virtual Terminal for GTK+3

License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/libv3270
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
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
%meson
%meson_build
%if %{with docs}
doxygen doxygen
%endif

%install
%meson_install
%find_lang %{name}-%{major_sover}.%{minor_sover}

# Removed unused glade catalog
rm -r %{buildroot}%{_datadir}/glade/

%files -f %{name}-%{major_sover}.%{minor_sover}.lang
%license LICENSE
%doc README.md AUTHORS
%{_libdir}/%{name}.so.%{major_sover}*
%{_datadir}/pw3270/

%files devel
%{_includedir}/v3270.h
%{_includedir}/v3270/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc

%if %{with docs}
%files doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog
