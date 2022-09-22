%bcond_without docs

Name:           lib3270
Version:        5.4
Release:        %autorelease
Summary:        TN3270 Protocol Library

License:        LGPLv3
URL:            https://github.com/PerryWerneck/lib3270
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Use environment compiler flags if set
Patch0:         %{url}/commit/c7e2c43227695b259e98febaa6e7c17358e9d460.patch
# Backport of https://github.com/PerryWerneck/lib3270/pull/24
Patch1:         autoconf-fix.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
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
NOCONFIGURE=1 ./autogen.sh
%configure
# override SHELL to make the build more verbose
%make_build SHELL='sh -x'
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
%dir %{_datadir}/pw3270

%files devel
%dir %{_datadir}/pw3270/pot
%{_datadir}/pw3270/pot/%{name}.pot
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%if %{with docs}
%files doc
%license LICENSE
%doc html
%endif

%changelog
%autochangelog
