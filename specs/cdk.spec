%global mainver 5.0
%global datever 20250116

Name:           cdk
Version:        %{mainver}.%{datever}
Release:        %autorelease
Summary:        Curses Development Kit
License:        MIT-X11
URL:            https://invisible-island.net/cdk/
Source0:        https://invisible-island.net/cdk-%{mainver}-%{datever}.tgz
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  make

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

%prep
%autosetup -n %{name}-%{mainver}-%{datever}

%build
%configure --with-ncurses --enable-const
make cdkshlib %{?_smp_mflags}

%check
echo "sample programs are interactive"

%install
make install installCDKSHLibrary DESTDIR=%{buildroot} INSTALL="install -pD"

# fixes rpmlint unstripped-binary-or-object
chmod +x %{buildroot}%{_libdir}/*.so

find %{buildroot} -name '*.a' -delete -print

rm -vrf %{buildroot}%{_docdir}

%ldconfig_scriptlets

%files
%license COPYING
%doc CHANGES README VERSION examples demos
%{_libdir}/libcdk.so.*
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*

%files devel
%{_bindir}/cdk5-config
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/libcdk.so

%changelog
%autochangelog
