%{!?tcl_version: %global tcl_version %((echo '8.5'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           tcltls
Version:        2.0.1
Release:        %autorelease
Summary:        OpenSSL extension for Tcl
License:        TCL
URL:            https://core.tcl.tk/tcltls/home
Source0:        https://core.tcl.tk/tcltls/uv/%{name}%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  tcl-devel

Requires:       tcl(abi) = %{tcl_version}

%description
A TLS OpenSSL extension for Tcl

%package devel
Summary:        Header files for the OpenSSL extension for Tcl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The TLS OpenSSL extension to Tcl

This package contains the development files for tls.

%prep
%autosetup -n %{name}%{version}
chmod 0644 README.txt ChangeLog license.terms

%build
%configure --enable-symbols --disable-rpath --with-ssl-dir=%{_prefix}
%make_build

%check
make test

%install
%make_install libdir=%{tcl_sitearch}
chmod 0755 %{buildroot}%{tcl_sitearch}/%{name}%{version}/*.so

install -D -p -m 0644 generic/tls.h %{buildroot}%{_includedir}/tls.h

%files
%license license.terms
%doc README.txt ChangeLog
%{tcl_sitearch}/%{name}%{version}
%{_mandir}/mann/tls.n*

%files devel
%{_includedir}/tls.h

%changelog
%autochangelog
