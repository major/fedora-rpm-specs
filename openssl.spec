# For the curious:
# 0.9.8jk + EAP-FAST soversion = 8
# 1.0.0 soversion = 10
# 1.1.0 soversion = 1.1 (same as upstream although presence of some symbols
#                        depends on build configuration options)
# 3.0.0 soversion = 3 (same as upstream)
%define soversion 3

# Arches on which we need to prevent arch conflicts on opensslconf.h, must
# also be handled in opensslconf-new.h.
%define multilib_arches %{ix86} ia64 %{mips} ppc ppc64 s390 s390x sparcv9 sparc64 x86_64

%define srpmhash() %{lua:
local files = rpm.expand("%_specdir/openssl.spec")
for i, p in ipairs(patches) do
   files = files.." "..p
end
for i, p in ipairs(sources) do
   files = files.." "..p
end
local sha256sum = assert(io.popen("cat "..files.." 2>/dev/null | sha256sum"))
local hash = sha256sum:read("*a")
sha256sum:close()
print(string.sub(hash, 0, 16))
}

%global _performance_build 1

Summary: Utilities from the general purpose cryptography library with TLS implementation
Name: openssl
Version: 3.0.5
Release: 5%{?dist}
Epoch: 1
# We have to remove certain patented algorithms from the openssl source
# tarball with the hobble-openssl script which is included below.
# The original openssl upstream tarball cannot be shipped in the .src.rpm.
Source: openssl-%{version}-hobbled.tar.xz
Source1: hobble-openssl
Source2: Makefile.certificate
Source3: genpatches
Source4: openssl.rpmlintrc
Source6: make-dummy-cert
Source7: renew-dummy-cert
Source9: configuration-switch.h
Source10: configuration-prefix.h
Source12: ec_curve.c
Source13: ectest.c
Source14: 0025-for-tests.patch

# Patches exported from source git
# Aarch64 and ppc64le use lib64
Patch1: 0001-Aarch64-and-ppc64le-use-lib64.patch
# Use more general default values in openssl.cnf
Patch2: 0002-Use-more-general-default-values-in-openssl.cnf.patch
# Do not install html docs
Patch3: 0003-Do-not-install-html-docs.patch
# Override default paths for the CA directory tree
Patch4: 0004-Override-default-paths-for-the-CA-directory-tree.patch
# apps/ca: fix md option help text
Patch5: 0005-apps-ca-fix-md-option-help-text.patch
# Disable signature verification with totally unsafe hash algorithms
Patch6: 0006-Disable-signature-verification-with-totally-unsafe-h.patch
# Add support for PROFILE=SYSTEM system default cipherlist
Patch7: 0007-Add-support-for-PROFILE-SYSTEM-system-default-cipher.patch
# Add FIPS_mode() compatibility macro
Patch8: 0008-Add-FIPS_mode-compatibility-macro.patch
# Add check to see if fips flag is enabled in kernel
Patch9: 0009-Add-Kernel-FIPS-mode-flag-support.patch
# remove unsupported EC curves
Patch11: 0011-Remove-EC-curves.patch
# Disable explicit EC curves
# https://bugzilla.redhat.com/show_bug.cgi?id=2066412
Patch12: 0012-Disable-explicit-ec.patch
# https://github.com/openssl/openssl/pull/17981
# Patch13: 0013-FIPS-provider-explicit-ec.patch
# https://github.com/openssl/openssl/pull/17998
# Patch14: 0014-FIPS-disable-explicit-ec.patch
# https://github.com/openssl/openssl/pull/18609
# Patch15: 0015-FIPS-decoded-from-explicit.patch
# Instructions to load legacy provider in openssl.cnf
Patch24: 0024-load-legacy-prov.patch
# Tmp: test name change
Patch31: 0031-tmp-Fix-test-names.patch
# We load FIPS provider and set FIPS properties implicitly
Patch32: 0032-Force-fips.patch
# Embed HMAC into the fips.so
Patch33: 0033-FIPS-embed-hmac.patch
# Comment out fipsinstall command-line utility
Patch34: 0034.fipsinstall_disable.patch
# Skip unavailable algorithms running `openssl speed`
Patch35: 0035-speed-skip-unavailable-dgst.patch
# Extra public/private key checks required by FIPS-140-3
Patch44: 0044-FIPS-140-3-keychecks.patch
# Minimize fips services
Patch45: 0045-FIPS-services-minimize.patch
# Backport of s390x hardening, https://github.com/openssl/openssl/pull/17486
# Patch46: 0046-FIPS-s390x-hardening.patch
# Execute KATS before HMAC verification
Patch47: 0047-FIPS-early-KATS.patch
# Backport of correctly handle 2^14 byte long records #17538
# Patch48: 0048-correctly-handle-records.patch
%if 0%{?rhel}
# Selectively disallow SHA1 signatures
Patch49: 0049-Selectively-disallow-SHA1-signatures.patch
%else
# Selectively disallow SHA1 signatures rhbz#2070977
Patch49: 0049-Allow-disabling-of-SHA1-signatures.patch
%endif
# Backport of patch for RHEL for Edge rhbz #2027261
Patch51: 0051-Support-different-R_BITS-lengths-for-KBKDF.patch
%if 0%{?rhel}
# Allow SHA1 in seclevel 2 if rh-allow-sha1-signatures = yes
Patch52: 0052-Allow-SHA1-in-seclevel-2-if-rh-allow-sha1-signatures.patch
%else
# Support SHA1 in TLS in LEGACY crypto-policy (which is SECLEVEL=1)
Patch52: 0052-Allow-SHA1-in-seclevel-1-if-rh-allow-sha1-signatures.patch
%endif
%if 0%{?rhel}
# no USDT probe instrumentation required
%else
# Instrument with USDT probes related to SHA-1 deprecation
Patch53: 0053-Add-SHA1-probes.patch
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=2004915, backport of 2c0f7d46b8449423446cfe1e52fc1e1ecd506b62
# Patch54: 0054-Replace-size-check-with-more-meaningful-pubkey-check.patch
# https://github.com/openssl/openssl/pull/17324
# Patch55: 0055-nonlegacy-fetch-null-deref.patch
# https://github.com/openssl/openssl/pull/18103
# The patch is incorporated in 3.0.3 but we provide this function since 3.0.1
# so the patch should persist
Patch56: 0056-strcasecmp.patch
# https://github.com/openssl/openssl/pull/18175
# Patch57: 0057-strcasecmp-fix.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2053289
Patch58: 0058-FIPS-limit-rsa-encrypt.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2069235
Patch60: 0060-FIPS-KAT-signature-tests.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2087147
Patch61: 0061-Deny-SHA-1-signature-verification-in-FIPS-provider.patch
Patch62: 0062-fips-Expose-a-FIPS-indicator.patch
# https://github.com/openssl/openssl/pull/18141
# Patch63: 0063-CVE-2022-1473.patch
# upstream commits 55c80c222293a972587004c185dc5653ae207a0e 2eda98790c5c2741d76d23cc1e74b0dc4f4b391a
# Patch64: 0064-CVE-2022-1343.diff
# upstream commit 1ad73b4d27bd8c1b369a3cd453681d3a4f1bb9b2
# Patch65: 0065-CVE-2022-1292.patch
# https://github.com/openssl/openssl/pull/18444
# https://github.com/openssl/openssl/pull/18467
# Patch66: 0066-replace-expired-certs.patch
# https://github.com/openssl/openssl/pull/18512
# Patch67: 0067-fix-ppc64-montgomery.patch
#https://github.com/openssl/openssl/commit/2c9c35870601b4a44d86ddbf512b38df38285cfa
#https://github.com/openssl/openssl/commit/8a3579a7b7067a983e69a4eda839ac408c120739
# Patch68: 0068-CVE-2022-2068.patch
# https://github.com/openssl/openssl/commit/a98f339ddd7e8f487d6e0088d4a9a42324885a93
# https://github.com/openssl/openssl/commit/52d50d52c2f1f4b70d37696bfa74fe5e581e7ba8
# Patch69: 0069-CVE-2022-2097.patch
# https://github.com/openssl/openssl/commit/edceec7fe0c9a5534ae155c8398c63dd7dd95483
# Patch70: 0070-EVP_PKEY_Q_keygen-Call-OPENSSL_init_crypto-to-init-s.patch
# https://github.com/openssl/openssl/commit/44a563dde1584cd9284e80b6e45ee5019be8d36c
# https://github.com/openssl/openssl/commit/345c99b6654b8313c792d54f829943068911ddbd
# Regression on Power8, see rhbz2124845, https://github.com/openssl/openssl/issues/19163; fix in 0079-Fix-AES-GCM-on-Power-8-CPUs.patch
Patch71: 0071-AES-GCM-performance-optimization.patch
# https://github.com/openssl/openssl/commit/f596bbe4da779b56eea34d96168b557d78e1149
# https://github.com/openssl/openssl/commit/7e1f3ffcc5bc15fb9a12b9e3bb202f544c6ed5aa
# hunks in crypto/ppccap.c from https://github.com/openssl/openssl/commit/f5485b97b6c9977c0d39c7669b9f97a879312447
Patch72: 0072-ChaCha20-performance-optimizations-for-ppc64le.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2102535
Patch73: 0073-FIPS-Use-OAEP-in-KATs-support-fixed-OAEP-seed.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2102535
%if 0%{?rhel}
Patch74: 0074-FIPS-Use-digest_sign-digest_verify-in-self-test-eln.patch
%else
Patch74: 0074-FIPS-Use-digest_sign-digest_verify-in-self-test.patch
%endif
# https://bugzilla.redhat.com/show_bug.cgi?id=2102535
Patch75: 0075-FIPS-Use-FFDHE2048-in-self-test.patch
# Downstream only. Reseed DRBG using getrandom(GRND_RANDOM)
# https://bugzilla.redhat.com/show_bug.cgi?id=2102541
Patch76: 0076-FIPS-140-3-DRBG.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2102542
Patch77: 0077-FIPS-140-3-zeroization.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2114772
Patch78: 0078-Add-FIPS-indicator-parameter-to-HKDF.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2124845, https://github.com/openssl/openssl/pull/19182
Patch79: 0079-Fix-AES-GCM-on-Power-8-CPUs.patch

License: ASL 2.0
URL: http://www.openssl.org/
BuildRequires: gcc g++
BuildRequires: coreutils, perl-interpreter, sed, zlib-devel, /usr/bin/cmp
BuildRequires: lksctp-tools-devel
BuildRequires: /usr/bin/rename
BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/sbin/sysctl
BuildRequires: perl(Test::Harness), perl(Test::More), perl(Math::BigInt)
BuildRequires: perl(Module::Load::Conditional), perl(File::Temp)
BuildRequires: perl(Time::HiRes), perl(IPC::Cmd), perl(Pod::Html), perl(Digest::SHA)
BuildRequires: perl(FindBin), perl(lib), perl(File::Compare), perl(File::Copy), perl(bigint)
BuildRequires: git-core
BuildRequires: systemtap-sdt-devel
Requires: coreutils
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

%package libs
Summary: A general purpose cryptography library with TLS implementation
Requires: ca-certificates >= 2008-5
Requires: crypto-policies >= 20180730
Recommends: openssl-pkcs11%{?_isa}

%description libs
OpenSSL is a toolkit for supporting cryptography. The openssl-libs
package contains the libraries that are used by various applications which
support cryptographic algorithms and protocols.

%package devel
Summary: Files for development of applications which will use OpenSSL
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
OpenSSL is a toolkit for supporting cryptography. The openssl-devel
package contains include files needed to develop applications which
support various cryptographic algorithms and protocols.

%package perl
Summary: Perl scripts provided with OpenSSL
Requires: perl-interpreter
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description perl
OpenSSL is a toolkit for supporting cryptography. The openssl-perl
package provides Perl scripts for converting certificates and keys
from other formats to the formats used by the OpenSSL toolkit.

%prep
%autosetup -S git -n %{name}-%{version}

# The hobble_openssl is called here redundantly, just to be sure.
# The tarball has already the sources removed.
%{SOURCE1} > /dev/null

cp %{SOURCE12} crypto/ec/
cp %{SOURCE13} test/

%build
# Figure out which flags we want to use.
# default
sslarch=%{_os}-%{_target_cpu}
%ifarch %ix86
sslarch=linux-elf
if ! echo %{_target} | grep -q i686 ; then
	sslflags="no-asm 386"
fi
%endif
%ifarch x86_64
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch sparcv9
sslarch=linux-sparcv9
sslflags=no-asm
%endif
%ifarch sparc64
sslarch=linux64-sparcv9
sslflags=no-asm
%endif
%ifarch alpha alphaev56 alphaev6 alphaev67
sslarch=linux-alpha-gcc
%endif
%ifarch s390 sh3eb sh4eb
sslarch="linux-generic32 -DB_ENDIAN"
%endif
%ifarch s390x
sslarch="linux64-s390x"
%endif
%ifarch %{arm}
sslarch=linux-armv4
%endif
%ifarch aarch64
sslarch=linux-aarch64
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch sh3 sh4
sslarch=linux-generic32
%endif
%ifarch ppc64 ppc64p7
sslarch=linux-ppc64
%endif
%ifarch ppc64le
sslarch="linux-ppc64le"
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch mips mipsel
sslarch="linux-mips32 -mips32r2"
%endif
%ifarch mips64 mips64el
sslarch="linux64-mips64 -mips64r2"
%endif
%ifarch mips64el
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch riscv64
sslarch=linux-generic64
%endif
ktlsopt=enable-ktls
%ifarch armv7hl
ktlsopt=disable-ktls
%endif

# Add -Wa,--noexecstack here so that libcrypto's assembler modules will be
# marked as not requiring an executable stack.
# Also add -DPURIFY to make using valgrind with openssl easier as we do not
# want to depend on the uninitialized memory as a source of entropy anyway.
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS"

export HASHBANGPERL=/usr/bin/perl

%define fips %{version}-%{srpmhash}
# ia64, x86_64, ppc are OK by default
# Configure the build tree.  Override OpenSSL defaults with known-good defaults
# usable on all platforms.  The Configure script already knows to use -fPIC and
# RPM_OPT_FLAGS, so we can skip specifiying them here.
./Configure \
	--prefix=%{_prefix} --openssldir=%{_sysconfdir}/pki/tls ${sslflags} \
	--system-ciphers-file=%{_sysconfdir}/crypto-policies/back-ends/openssl.config \
	zlib enable-camellia enable-seed enable-rfc3779 enable-sctp \
	enable-cms enable-md2 enable-rc5 ${ktlsopt} enable-fips\
	no-mdc2 no-ec2m no-sm2 no-sm4 enable-buildtest-c++\
	shared  ${sslarch} $RPM_OPT_FLAGS '-DDEVRANDOM="\"/dev/urandom\"" -DREDHAT_FIPS_VERSION="\"%{fips}\""'

# Do not run this in a production package the FIPS symbols must be patched-in
#util/mkdef.pl crypto update

make -s %{?_smp_mflags} all

# Clean up the .pc files
for i in libcrypto.pc libssl.pc openssl.pc ; do
  sed -i '/^Libs.private:/{s/-L[^ ]* //;s/-Wl[^ ]* //}' $i
done

%check
# Verify that what was compiled actually works.

# Hack - either enable SCTP AUTH chunks in kernel or disable sctp for check
(sysctl net.sctp.addip_enable=1 && sysctl net.sctp.auth_enable=1) || \
(echo 'Failed to enable SCTP AUTH chunks, disabling SCTP for tests...' &&
 sed '/"msan" => "default",/a\ \ "sctp" => "default",' configdata.pm > configdata.pm.new && \
 touch -r configdata.pm configdata.pm.new && \
 mv -f configdata.pm.new configdata.pm)

# We must revert patch4 before tests otherwise they will fail
patch -p1 -R < %{PATCH4}
#We must disable default provider before tests otherwise they will fail
patch -p1 < %{SOURCE14}

OPENSSL_ENABLE_MD5_VERIFY=
export OPENSSL_ENABLE_MD5_VERIFY
%if 0%{?rhel}
OPENSSL_ENABLE_SHA1_SIGNATURES=
export OPENSSL_ENABLE_SHA1_SIGNATURES
%endif
OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE
#embed HMAC into fips provider for test run
LD_LIBRARY_PATH=. apps/openssl dgst -binary -sha256 -mac HMAC -macopt hexkey:f4556650ac31d35461610bac4ed81b1a181b2d8a43ea2854cbae22ca74560813 < providers/fips.so > providers/fips.so.hmac
objcopy --update-section .rodata1=providers/fips.so.hmac providers/fips.so providers/fips.so.mac
mv providers/fips.so.mac providers/fips.so
#run tests itself
make test HARNESS_JOBS=8

# Add generation of HMAC checksum of the final stripped library
# We manually copy standard definition of __spec_install_post
# and add hmac calculation/embedding to fips.so
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    LD_LIBRARY_PATH=. apps/openssl dgst -binary -sha256 -mac HMAC -macopt hexkey:f4556650ac31d35461610bac4ed81b1a181b2d8a43ea2854cbae22ca74560813 < $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so > $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.hmac \
    objcopy --update-section .rodata1=$RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.hmac $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.mac \
    mv $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.mac $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so \
    rm $RPM_BUILD_ROOT%{_libdir}/ossl-modules/fips.so.hmac \
%{nil}

%define __provides_exclude_from %{_libdir}/openssl

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
# Install OpenSSL.
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir},%{_mandir},%{_libdir}/openssl,%{_pkgdocdir}}
%make_install
rename so.%{soversion} so.%{version} $RPM_BUILD_ROOT%{_libdir}/*.so.%{soversion}
for lib in $RPM_BUILD_ROOT%{_libdir}/*.so.%{version} ; do
	chmod 755 ${lib}
	ln -s -f `basename ${lib}` $RPM_BUILD_ROOT%{_libdir}/`basename ${lib} .%{version}`
	ln -s -f `basename ${lib}` $RPM_BUILD_ROOT%{_libdir}/`basename ${lib} .%{version}`.%{soversion}
done

# Remove static libraries
for lib in $RPM_BUILD_ROOT%{_libdir}/*.a ; do
	rm -f ${lib}
done

# Install a makefile for generating keys and self-signed certs, and a script
# for generating them on the fly.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}/Makefile.certificate
install -m755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/make-dummy-cert
install -m755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/renew-dummy-cert

# Move runable perl scripts to bindir
mv $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/misc/*.pl $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/misc/tsget $RPM_BUILD_ROOT%{_bindir}

# Rename man pages so that they don't conflict with other system man pages.
pushd $RPM_BUILD_ROOT%{_mandir}
mv man5/config.5ossl man5/openssl.cnf.5
popd

mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA
mkdir -m700 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/private
mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/certs
mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/crl
mkdir -m755 $RPM_BUILD_ROOT%{_sysconfdir}/pki/CA/newcerts

# Ensure the config file timestamps are identical across builds to avoid
# mulitlib conflicts and unnecessary renames on upgrade
touch -r %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/openssl.cnf
touch -r %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/ct_log_list.cnf

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/openssl.cnf.dist
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/ct_log_list.cnf.dist
#we don't use native fipsmodule.cnf because FIPS module is loaded automatically
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/pki/tls/fipsmodule.cnf

# Determine which arch opensslconf.h is going to try to #include.
basearch=%{_arch}
%ifarch %{ix86}
basearch=i386
%endif
%ifarch sparcv9
basearch=sparc
%endif
%ifarch sparc64
basearch=sparc64
%endif

# Next step of gradual disablement of SSL3.
# Make SSL3 disappear to newly built dependencies.
sed -i '/^\#ifndef OPENSSL_NO_SSL_TRACE/i\
#ifndef OPENSSL_NO_SSL3\
# define OPENSSL_NO_SSL3\
#endif' $RPM_BUILD_ROOT/%{_prefix}/include/openssl/opensslconf.h

%ifarch %{multilib_arches}
# Do an configuration.h switcheroo to avoid file conflicts on systems where you
# can have both a 32- and 64-bit version of the library, and they each need
# their own correct-but-different versions of opensslconf.h to be usable.
install -m644 %{SOURCE10} \
	$RPM_BUILD_ROOT/%{_prefix}/include/openssl/configuration-${basearch}.h
cat $RPM_BUILD_ROOT/%{_prefix}/include/openssl/configuration.h >> \
	$RPM_BUILD_ROOT/%{_prefix}/include/openssl/configuration-${basearch}.h
install -m644 %{SOURCE9} \
	$RPM_BUILD_ROOT/%{_prefix}/include/openssl/configuration.h
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc NEWS.md README.md
%{_bindir}/make-dummy-cert
%{_bindir}/renew-dummy-cert
%{_bindir}/openssl
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_pkgdocdir}/Makefile.certificate
%exclude %{_mandir}/man1/*.pl*
%exclude %{_mandir}/man1/tsget*

%files libs
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%dir %{_sysconfdir}/pki/tls
%dir %{_sysconfdir}/pki/tls/certs
%dir %{_sysconfdir}/pki/tls/misc
%dir %{_sysconfdir}/pki/tls/private
%config(noreplace) %{_sysconfdir}/pki/tls/openssl.cnf
%config(noreplace) %{_sysconfdir}/pki/tls/ct_log_list.cnf
%attr(0755,root,root) %{_libdir}/libcrypto.so.%{version}
%{_libdir}/libcrypto.so.%{soversion}
%attr(0755,root,root) %{_libdir}/libssl.so.%{version}
%{_libdir}/libssl.so.%{soversion}
%attr(0755,root,root) %{_libdir}/engines-%{soversion}
%attr(0755,root,root) %{_libdir}/ossl-modules

%files devel
%doc CHANGES.md doc/dir-locals.example.el doc/openssl-c-indent.el
%{_prefix}/include/openssl
%{_libdir}/*.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc

%files perl
%{_bindir}/c_rehash
%{_bindir}/*.pl
%{_bindir}/tsget
%{_mandir}/man1/*.pl*
%{_mandir}/man1/tsget*
%dir %{_sysconfdir}/pki/CA
%dir %{_sysconfdir}/pki/CA/private
%dir %{_sysconfdir}/pki/CA/certs
%dir %{_sysconfdir}/pki/CA/crl
%dir %{_sysconfdir}/pki/CA/newcerts

%ldconfig_scriptlets libs

%changelog
* Mon Sep 12 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.5-5
- Update patches to make ELN build happy
  Resolves: rhbz#2123755

* Fri Sep 09 2022 Clemens Lang <cllang@redhat.com> - 1:3.0.5-4
- Fix AES-GCM on Power 8 CPUs
  Resolves: rhbz#2124845

* Thu Sep 01 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.5-3
- Sync patches with RHEL
  Related: rhbz#2123755

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Clemens Lang <cllang@redhat.com> - 1:3.0.5-1
- Rebase to upstream version 3.0.5
  Related: rhbz#2099972, CVE-2022-2097

* Wed Jun 01 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.3-1
- Rebase to upstream version 3.0.3

* Thu Apr 28 2022 Clemens Lang <cllang@redhat.com> - 1:3.0.2-5
- Instrument with USDT probes related to SHA-1 deprecation

* Wed Apr 27 2022 Clemens Lang <cllang@redhat.com> - 1:3.0.2-4
- Support rsa_pkcs1_md5_sha1 in TLS 1.0/1.1 with rh-allow-sha1-signatures = yes
  to restore TLS 1.0 and 1.1 support in LEGACY crypto-policy.
  Related: rhbz#2069239

* Tue Apr 26 2022 Alexander Sosedkin <asosedkin@redhat.com> - 1:3.0.2-4
- Instrument with USDT probes related to SHA-1 deprecation

* Wed Apr 20 2022 Clemens Lang <cllang@redhat.com> - 1:3.0.2-3
- Disable SHA-1 by default in ELN using the patches from CentOS
- Fix a FIXME in the openssl.cnf(5) manpage

* Thu Apr 07 2022 Clemens Lang <cllang@redhat.com> - 1:3.0.2-2
- Silence a few rpmlint false positives.

* Thu Apr 07 2022 Clemens Lang <cllang@redhat.com> - 1:3.0.2-2
- Allow disabling SHA1 signature creation and verification.
  Set rh-allow-sha1-signatures = no to disable.
  Allow SHA1 in TLS in SECLEVEL 1 if rh-allow-sha1-signatures = yes. This will
  support SHA1 in TLS in the LEGACY crypto-policy.
  Resolves: rhbz#2070977
  Related: rhbz#2031742, rhbz#2062640

* Fri Mar 18 2022 Dmitry Belyavskiy <dbelyavs@redhat.com> - 1:3.0.2-1
- Rebase to upstream version 3.0.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Sahana Prasad <sahana@redhat.com> - 1:3.0.0-1
- Rebase to upstream version 3.0.0
