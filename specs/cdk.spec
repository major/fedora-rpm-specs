%global mainver 5.0
%global datever 20260119

Name:           cdk
Version:        %{mainver}.%{datever}
Release:        %autorelease
Summary:        Curses Development Kit
License:        X11-distribute-modifications-variant
URL:            https://invisible-island.net/cdk/
Source0:        https://invisible-island.net/archives/cdk/cdk-%{mainver}-%{datever}.tgz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)

%description
CDK stands for "Curses Development Kit". It contains a large number of ready
to use widgets which facilitate the speedy development of full screen curses
programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation and examples for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation, examples and demos for %{name}.

%prep
%autosetup -n %{name}-%{mainver}-%{datever}

%build
%configure --with-ncurses --enable-const
%make_build cdkshlib

%check
# Sample programs are interactive
:

%install
%make_install installCDKSHLibrary

# Fixes rpmlint unstripped-binary-or-object (shared libraries should be executable)
chmod +x %{buildroot}%{_libdir}/*.so.*

# Remove static libraries
find %{buildroot} -name '*.a' -delete -print

# Remove documentation installed by 'make install' to handle it via %%doc and %%package doc
rm -vrf %{buildroot}%{_docdir}

%files
%license COPYING
%doc CHANGES README VERSION
%{_libdir}/libcdk.so.*

%files devel
%{_bindir}/cdk5-config
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/libcdk.so
%{_mandir}/man1/cdk5-config.1*
%{_mandir}/man3/*.3*

%files doc
%doc examples demos

%changelog
%autochangelog
