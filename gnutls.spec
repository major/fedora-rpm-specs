%define srpmhash() %{lua:
local files = rpm.expand("%_specdir/gnutls.spec")
for i, p in ipairs(patches) do
   files = files.." "..p
end
for i, p in ipairs(sources) do
   files = files.." "..p
end
local sha256sum = assert(io.popen("cat "..files.."| sha256sum"))
local hash = sha256sum:read("*a")
sha256sum:close()
print(string.sub(hash, 0, 16))
}

Version: 3.7.8
Release: %{?autorelease}%{!?autorelease:1%{?dist}}
Patch: gnutls-3.6.7-no-now-guile.patch
Patch: gnutls-3.2.7-rpath.patch

%bcond_without bootstrap
%bcond_without dane
%if 0%{?rhel}
%bcond_with guile
%bcond_without fips
%else
%bcond_without guile
%bcond_without fips
%endif
%bcond_with tpm12
%bcond_without tpm2
%bcond_without gost
%bcond_with certificate_compression
%bcond_without tests

Summary: A TLS protocol implementation
Name: gnutls
# The libraries are LGPLv2.1+, utilities are GPLv3+
License: GPLv3+ and LGPLv2+
BuildRequires: p11-kit-devel >= 0.21.3, gettext-devel
BuildRequires: readline-devel, libtasn1-devel >= 4.3
%if %{with certificate_compression}
BuildRequires: zlib-devel, brotli-devel, libzstd-devel
%endif
%if %{with bootstrap}
BuildRequires: automake, autoconf, gperf, libtool, texinfo
%endif
BuildRequires: nettle-devel >= 3.5.1
%if %{with tpm12}
BuildRequires: trousers-devel >= 0.3.11.2
%endif
%if %{with tpm2}
BuildRequires: tpm2-tss-devel >= 3.0.3
%endif
BuildRequires: libidn2-devel
BuildRequires: libunistring-devel
BuildRequires: net-tools, datefudge, softhsm, gcc, gcc-c++
BuildRequires: gnupg2
BuildRequires: git-core

# for a sanity check on cert loading
BuildRequires: p11-kit-trust, ca-certificates
Requires: crypto-policies
Requires: p11-kit-trust
Requires: libtasn1 >= 4.3
Requires: nettle >= 3.4.1
%if %{with tpm12}
Recommends: trousers >= 0.3.11.2
%endif

%if %{with dane}
BuildRequires: unbound-devel unbound-libs
%endif
%if %{with guile}
BuildRequires: guile22-devel
%endif
BuildRequires: make gtk-doc
URL: http://www.gnutls.org/
%define short_version %(echo %{version} | grep -m1 -o "[0-9]*\.[0-9]*" | head -1)
Source0: https://www.gnupg.org/ftp/gcrypt/gnutls/v%{short_version}/%{name}-%{version}.tar.xz
Source1: https://www.gnupg.org/ftp/gcrypt/gnutls/v%{short_version}/%{name}-%{version}.tar.xz.sig
Source2: gnutls-release-keyring.gpg

# Wildcard bundling exception https://fedorahosted.org/fpc/ticket/174
Provides: bundled(gnulib) = 20130424

%package c++
Summary: The C++ interface to GnuTLS
Requires: %{name}%{?_isa} = %{version}-%{release}

%package devel
Summary: Development files for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-c++%{?_isa} = %{version}-%{release}
%if %{with dane}
Requires: %{name}-dane%{?_isa} = %{version}-%{release}
%endif
Requires: pkgconfig

%package utils
License: GPLv3+
Summary: Command line tools for TLS protocol
Requires: %{name}%{?_isa} = %{version}-%{release}
%if %{with dane}
Requires: %{name}-dane%{?_isa} = %{version}-%{release}
%endif

%if %{with dane}
%package dane
Summary: A DANE protocol implementation for GnuTLS
Requires: %{name}%{?_isa} = %{version}-%{release}
%endif

%if %{with guile}
%package guile
Summary: Guile bindings for the GNUTLS library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: guile22
%endif

%description
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 

%description c++
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 

%description devel
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains files needed for developing applications with
the GnuTLS library.

%description utils
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains command line TLS client and server and certificate
manipulation tools.

%if %{with dane}
%description dane
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains library that implements the DANE protocol for verifying
TLS certificates through DNSSEC.
%endif

%if %{with guile}
%description guile
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS 
protocols and technologies around them. It provides a simple C language 
application programming interface (API) to access the secure communications 
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and 
other required structures. 
This package contains Guile bindings for the library.
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1 -S git

%build
%define _lto_cflags %{nil}

%if %{with bootstrap}
autoreconf -fi
%endif

sed -i -e 's|sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/lib /usr/lib %{_libdir}|g' configure
rm -f lib/minitasn1/*.c lib/minitasn1/*.h

echo "SYSTEM=NORMAL" >> tests/system.prio

CCASFLAGS="$CCASFLAGS -Wa,--generate-missing-build-notes=yes"
export CCASFLAGS

%if %{with guile}
# These should be checked by m4/guile.m4 instead of configure.ac
# taking into account of _guile_suffix
guile_snarf=%{_bindir}/guile-snarf2.2
export guile_snarf
GUILD=%{_bindir}/guild2.2
export GUILD
%endif

%if %{with fips}
eval $(sed -n 's/^\(\(NAME\|VERSION_ID\)=.*\)/OS_\1/p' /etc/os-release)
export FIPS_MODULE_NAME="$OS_NAME ${OS_VERSION_ID%%.*} %name"
%endif

%configure \
%if %{with fips}
           --enable-fips140-mode \
           --with-fips140-module-name="$FIPS_MODULE_NAME" \
           --with-fips140-module-version=%{version}-%{srpmhash} \
%endif
%if %{with gost}
    	   --enable-gost \
%else
	   --disable-gost \
%endif
	   --enable-sha1-support \
           --disable-static \
           --disable-openssl-compatibility \
           --disable-non-suiteb-curves \
           --with-system-priority-file=%{_sysconfdir}/crypto-policies/back-ends/gnutls.config \
           --with-default-trust-store-pkcs11="pkcs11:" \
%if %{with tpm12}
           --with-trousers-lib=%{_libdir}/libtspi.so.1 \
%else
           --without-tpm \
%endif
%if %{with tpm2}
           --with-tpm2 \
%else
           --without-tpm2 \
%endif
           --enable-ktls \
           --htmldir=%{_docdir}/manual \
%if %{with guile}
           --enable-guile \
           --with-guile-extension-dir=%{_libdir}/guile/2.2 \
%else
           --disable-guile \
%endif
%if %{with dane}
           --with-unbound-root-key-file=/var/lib/unbound/root.key \
           --enable-libdane \
%else
           --disable-libdane \
%endif
%if %{with certificate_compression}
	   --with-zlib --with-brotli --with-zstd \
%else
	   --without-zlib --without-brotli --without-zstd \
%endif
           --disable-rpath \
           --with-default-priority-string="@SYSTEM"

%make_build

%install
%make_install
make -C doc install-html DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/2.2/guile-gnutls*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/guile/2.2/guile-gnutls*.la
%if %{without dane}
rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gnutls-dane.pc
%endif

%if %{with fips}
# doing it twice should be a no-op the second time,
# and this way we avoid redefining it and missing a future change
%{__spec_install_post}
./lib/fipshmac "$RPM_BUILD_ROOT%{_libdir}/libgnutls.so.30" > $RPM_BUILD_ROOT%{_libdir}/.gnutls.hmac
sed -i "s^$RPM_BUILD_ROOT/usr^^" $RPM_BUILD_ROOT%{_libdir}/.gnutls.hmac
%endif

%if %{with fips}
%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
%{nil}
%endif

%find_lang gnutls

%check
%if %{with tests}
make check %{?_smp_mflags} GNUTLS_SYSTEM_PRIORITY_FILE=/dev/null
%endif

%files -f gnutls.lang
%{_libdir}/libgnutls.so.30*
%if %{with fips}
%{_libdir}/.gnutls.hmac
%endif
%doc README.md AUTHORS NEWS THANKS
%license LICENSE doc/COPYING doc/COPYING.LESSER

%files c++
%{_libdir}/libgnutlsxx.so.*

%files devel
%{_includedir}/*
%{_libdir}/libgnutls*.so

%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%{_infodir}/gnutls*
%{_infodir}/pkcs11-vision*
%{_docdir}/manual/*

%files utils
%{_bindir}/certtool
%if %{with tpm12}
%{_bindir}/tpmtool
%endif
%{_bindir}/ocsptool
%{_bindir}/psktool
%{_bindir}/p11tool
%{_bindir}/srptool
%if %{with dane}
%{_bindir}/danetool
%endif
%{_bindir}/gnutls*
%{_mandir}/man1/*
%doc doc/certtool.cfg

%if %{with dane}
%files dane
%{_libdir}/libgnutls-dane.so.*
%endif

%if %{with guile}
%files guile
%{_libdir}/guile/2.2/guile-gnutls*.so*
%{_libdir}/guile/2.2/site-ccache/gnutls.go
%{_libdir}/guile/2.2/site-ccache/gnutls/extra.go
%{_datadir}/guile/site/2.2/gnutls.scm
%{_datadir}/guile/site/2.2/gnutls/extra.scm
%endif

%changelog
%autochangelog
