Name:           gnupg-pkcs11-scd
Version:        0.11.0
Release:        %autorelease
Summary:        GnuPG-compatible smart-card daemon with PKCS#11 support

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://gnupg-pkcs11.sourceforge.net
Source0:        https://github.com/alonbl/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpkcs11-helper-1)
BuildRequires:  libassuan-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  make
Requires:       openssl
Requires:       pkcs11-helper >= 1.03

%description
gnupg-pkcs11-scd is a drop-in replacement for the smart-card daemon (scd)
shipped with the next-generation GnuPG (gnupg2). The daemon interfaces
with smart-cards by using RSA Security Inc.'s PKCS#11 Cryptographic Token
Interface.

%prep
%setup -q

%build
%configure
%{make_build}

%install
%{make_install}
rm -rf ${RPM_BUILD_ROOT}%{_docdir}

%files
%license COPYING
%doc AUTHORS README THANKS gnupg-pkcs11-scd/gnupg-pkcs11-scd.conf.example
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
