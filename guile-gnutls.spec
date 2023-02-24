Name:    guile-gnutls
Version: 3.7.11
Release: %{?autorelease}%{!?autorelease:1%{?dist}}
Summary: Guile bindings for the GNUTLS library

License: GPL-3.0-or-later AND LGPL-2.1-or-later
URL:     https://gitlab.com/gnutls/guile
Source0: https://ftpmirror.gnu.org/gnutls/%{name}-%{version}.tar.gz
Source1: https://ftpmirror.gnu.org/gnutls/%{name}-%{version}.tar.gz.sig
Source2: https://ftp.gnu.org/gnu/gnu-keyring.gpg

Requires:      guile22
BuildRequires: gcc make
BuildRequires: gnupg2
BuildRequires: gnutls-devel
BuildRequires: guile22-devel

Provides:  gnutls-guile = %{version}-%{release}
Obsoletes: gnutls-guile <= 3.7.8-4


%description
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS
protocols and technologies around them. It provides a simple C language
application programming interface (API) to access the secure communications
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and
other required structures.
This package contains Guile bindings for the library.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
guile_snarf=%{_bindir}/guile-snarf2.2
GUILD=%{_bindir}/guild2.2
export guile_snarf GUILD

%configure \
    --with-guile-extension-dir=%{_libdir}/guile/2.2

%make_build


%install
%make_install
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_infodir}/gnutls*
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/2.2/guile-gnutls*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/2.2/guile-gnutls*.la


%check
make check


%files
%license COPYING
%doc README ChangeLog AUTHORS NEWS
%{_libdir}/guile/2.2/guile-gnutls*.so*
%{_libdir}/guile/2.2/site-ccache/gnutls.go
%dir %{_libdir}/guile/2.2/site-ccache/gnutls/
%{_libdir}/guile/2.2/site-ccache/gnutls/extra.go
%{_datadir}/guile/site/2.2/gnutls.scm
%dir %{_datadir}/guile/site/2.2/gnutls/
%{_datadir}/guile/site/2.2/gnutls/extra.scm


%changelog
%autochangelog
