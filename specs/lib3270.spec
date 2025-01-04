%bcond docs 1
%global major_sover 5
%global minor_sover 5

Name:           lib3270
Version:        5.5.0
Release:        %autorelease
Summary:        TN3270 Protocol Library

License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/lib3270
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  libcurl-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  graphviz
%endif

%description
lib3270 is a TN3270 protocol library, originally designed as part of the pw3270
application.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

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

# Remove static libraries
rm %{buildroot}%{_libdir}/%{name}.a
rm %{buildroot}%{_libdir}/pkgconfig/%{name}-static.pc

%files -f %{name}-%{major_sover}.%{minor_sover}.lang
%license LICENSE
%doc README.md AUTHORS CHANGELOG
%{_libdir}/%{name}.so.%{major_sover}*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%if %{with docs}
%files doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog
