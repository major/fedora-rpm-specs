Name:		gssntlmssp
Version:	1.1.0
Release:	%autorelease
Summary:	GSSAPI NTLMSSP Mechanism

License:	LGPLv3+
URL:		https://github.com/gssapi/gss-ntlmssp
Source0:        https://github.com/gssapi/gss-ntlmssp/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires: krb5-libs%{?_isa} >= 1.19

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: m4
BuildRequires: libxslt
BuildRequires: libxml2
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: gettext-devel
BuildRequires: pkgconfig
BuildRequires: krb5-devel >= 1.11.2
BuildRequires: libunistring-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig(wbclient)
BuildRequires: zlib-devel
BuildRequires: make

%description
A GSSAPI Mechanism that implements NTLMSSP

%package devel
Summary: Development header for GSSAPI NTLMSSP
License: LGPLv3+

%description devel
Adds a header file with definition for custom GSSAPI extensions for NTLMSSP


%prep
%setup -q

%build
autoreconf -fiv
%configure \
    --with-wbclient \
    --disable-static \
    --disable-rpath

make %{?_smp_mflags} all

%install
%make_install
rm -f %{buildroot}%{_libdir}/gssntlmssp/gssntlmssp.la
mkdir -p %{buildroot}%{_sysconfdir}/gss/mech.d
install -pm644 examples/mech.ntlmssp %{buildroot}%{_sysconfdir}/gss/mech.d/ntlmssp.conf
%{find_lang} %{name}

%check
make test_gssntlmssp

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/gss/mech.d/ntlmssp.conf
%{_libdir}/gssntlmssp/
%{_mandir}/man8/gssntlmssp.8*
%doc COPYING

%files devel
%{_includedir}/gssapi/gssapi_ntlmssp.h

%autochangelog
