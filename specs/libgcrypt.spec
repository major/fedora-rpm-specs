Name: libgcrypt
Version: 1.12.3
Release: %autorelease
URL: https://www.gnupg.org/
Source0: https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
Source1: https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc
# Pass the annobin flags to the libgcrypt.so (#2016349)
Patch1: libgcrypt-1.10.1-annobin.patch
# https://gitlab.com/redhat-crypto/libgcrypt/libgcrypt-mirror/-/merge_requests/19/
Patch5: libgcrypt-1.11.0-marvin.patch

%global gcrylibdir %{_libdir}
%global gcrysoname libgcrypt.so.20

License: BSD-3-Clause AND (BSD-3-Clause OR GPL-2.0-only) AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND MIT-Modern-Variant
Summary: A general-purpose cryptography library
BuildRequires: gcc
BuildRequires: gawk, libgpg-error-devel >= 1.56, pkgconfig
# This is needed only when patching the .texi doc.
BuildRequires: texinfo
BuildRequires: autoconf, automake, libtool
BuildRequires: make
BuildRequires: annobin-annocheck binutils
BuildRequires: openpgpverify

%package devel
Summary: Development files for the %{name} package
Requires: libgpg-error-devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This is a development version.

%description devel
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.  This package contains files needed to develop
applications using libgcrypt.

%prep
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch 1 -p1
%patch 5 -p1

%build
# should be all algorithms except SM3 and SM4, aria
export DIGESTS='crc gostr3411-94 md4 md5 rmd160 sha1 sha256 sha512 sha3 tiger whirlpool stribog blake2'
export CIPHERS='arcfour blowfish cast5 des aes twofish serpent rfc2268 seed camellia idea salsa20 gost28147 chacha20'

autoreconf -f
%configure --disable-static \
%ifarch sparc64
     --disable-asm \
%endif
     --enable-noexecstack \
     --disable-jent-support \
     --disable-O-flag-munging \
     --enable-digests="$DIGESTS" \
     --enable-ciphers="$CIPHERS" \
     --enable-marvin-workaround
sed -i -e '/^sys_lib_dlsearch_path_spec/s,/lib /usr/lib,/usr/lib /lib64 /usr/lib64 /lib,g' libtool
%make_build

%check
make check

%define libpath $RPM_BUILD_ROOT%{gcrylibdir}/%{gcrysoname}.?.?

# Disabled now due to failing in F44
# https://github.com/rpminspect/rpminspect/issues/1546
# export PROFILE=%{?dist}
# annocheck --ignore-unknown --verbose --profile=${PROFILE:1} %{libpath}

%install
%make_install

# Change /usr/lib64 back to /usr/lib.  This saves us from having to patch the
# script to "know" that -L/usr/lib64 should be suppressed, and also removes
# a file conflict between 32- and 64-bit versions of this package.
# Also replace my_host with none.
sed -i -e 's,^libdir="/usr/lib.*"$,libdir="/usr/lib",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config
sed -i -e 's,^my_host=".*"$,my_host="none",g' $RPM_BUILD_ROOT/%{_bindir}/libgcrypt-config

rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir ${RPM_BUILD_ROOT}/%{_libdir}/*.la
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_libdir}

%if "%{gcrylibdir}" != "%{_libdir}"
# Relocate the shared libraries to %{gcrylibdir}.
mkdir -p $RPM_BUILD_ROOT%{gcrylibdir}
for shlib in $RPM_BUILD_ROOT%{_libdir}/*.so* ; do
	if test -L "$shlib" ; then
		rm "$shlib"
	else
		mv "$shlib" $RPM_BUILD_ROOT%{gcrylibdir}/
	fi
done

# Add soname symlink.
/sbin/ldconfig -n $RPM_BUILD_ROOT/%{_lib}/
%endif

# Overwrite development symlinks.
pushd $RPM_BUILD_ROOT/%{gcrylibdir}
for shlib in lib*.so.?? ; do
	target=$RPM_BUILD_ROOT/%{_libdir}/`echo "$shlib" | sed -e 's,\.so.*,,g'`.so
%if "%{gcrylibdir}" != "%{_libdir}"
	shlib=%{gcrylibdir}/$shlib
%endif
	ln -sf $shlib $target
done
popd

# Create /etc/gcrypt (hardwired, not dependent on the configure invocation) so
# that _someone_ owns it.
mkdir -p -m 755 $RPM_BUILD_ROOT/etc/gcrypt

%ldconfig_scriptlets

%files
%dir /etc/gcrypt
%{gcrylibdir}/libgcrypt.so.*.*
%{gcrylibdir}/%{gcrysoname}
%license COPYING.LIB
%doc AUTHORS NEWS THANKS

%files devel
%{_bindir}/%{name}-config
%{_bindir}/dumpsexp
%{_bindir}/hmac256
%{_bindir}/mpicalc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgcrypt.pc
%{_datadir}/aclocal/*
%{_mandir}/man1/*

%{_infodir}/gcrypt.info*
%license COPYING

%changelog
%autochangelog
