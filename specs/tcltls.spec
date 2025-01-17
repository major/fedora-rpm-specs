%{!?tcl_version: %global tcl_version %((echo '8.5'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           tcltls
Version:        1.7.22
Release:        %autorelease
Summary:        OpenSSL extension for Tcl

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://core.tcl.tk/tcltls/home
Source0:        https://core.tcl.tk/tcltls/uv/%{name}-%{version}.tar.gz

Patch0:         tcltls-1.7.21-cipher-tests.patch
Patch1:         tcltls-1.7.21-hostname-tests.patch
Patch2:         tcltls-1.7.22-cert-tests.patch
Patch3:         tcltls-1.7.22-fall-through.patch
Patch4:         tcltls-1.7.22-openssl3.patch
Patch5:         tcltls-1.7.22-tcl-9_0.patch
Patch6:         tcltls-1.7.22-tcl-9_0_second.patch

BuildRequires:  make
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
BuildRequires:  tcl-devel
BuildRequires:  gcc

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
%autosetup -p1

# Disable strip via objcopy(1) to achieve -debuginfo
sed -e 's/-@\(WEAKEN\|REMOVE\)SYMS@/:/' -i Makefile.in

# Build against OpenSSL 1.1 on RHEL 7 (for TLSv1.3 support)
%if 0%{?rhel} == 7
sed -e 's|-L$openssldir/lib|-L%{_libdir}/openssl11|g' \
    -e 's|-I$openssldir/include|-I%{_includedir}/openssl11|g' \
    -i configure
%endif

%build
%configure --disable-rpath --with-ssl-dir=%{_prefix}
%make_build

%check
make test

%install
%make_install libdir=%{tcl_sitearch}

%{__install} -D -p -m 0644 tls.h %{buildroot}%{_includedir}/tls.h

%files
%license license.terms
%doc README.txt ChangeLog
%{tcl_sitearch}/%{name}%{version}

%files devel
%{_includedir}/tls.h

%changelog
%autochangelog
