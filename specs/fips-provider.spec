%bcond check 1

# Enable gpg signature verification by default
%bcond gpgcheck 1

%global osslver 4.0.0-beta1

%global features fips,nssdb,ossl400

%global srpmhash() %{lua:
local files = rpm.expand("%_specdir/%{name}.spec")
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

Name:           fips-provider
Version:        1.5.0
Release:        %autorelease
Summary:        A FIPS provider built from the Kryoptic project

SourceLicense:        GPL-3.0-or-later and Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# BSD-3-Clause
# GPL-3.0-or-later
# ISC
# MIT
# MIT OR Apache-2.0
# MIT-0 OR Apache-2.0
# Unlicense OR MIT
# Zlib
License: Apache-2.0 AND (Apache-2.0 OR MIT) AND BSD-3-Clause AND GPL-3.0-or-later AND ISC AND MIT AND (MIT-0 OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/latchset/kryoptic
Source0:        https://github.com/latchset/kryoptic/releases/download/v%{version}/kryoptic-%{version}.tar.gz
%if %{with gpgcheck}
Source1:        https://github.com/latchset/kryoptic/releases/download/v%{version}/kryoptic-%{version}.tar.gz.asc
Source2:        https://people.redhat.com/~ssorce/simo_redhat.asc
%endif
Source3:        https://github.com/openssl/openssl/releases/download/openssl-%{osslver}/openssl-%{osslver}.tar.gz
Source4:        fips-hmacify.sh

Patch101:       0001-Re-enable-FIPS-security-checks.patch
Patch102:       0001-Zeroize-sensitive-memory-in-TLS-KDF.patch
Patch103:       0001-Use-libc-getrandom-for-GRND_RANDOM-flag.patch
Patch104:       0001-Update-RSA-test-vectors-for-FIPS-compliance.patch
Patch105:       0001-Remove-bundled-rusqlite-from-fips-feature.patch
Patch200:       openssl-%{osslver}-kryoptic.patch

BuildRequires:  cargo-rpm-macros >= 26
%if %{with gpgcheck}
BuildRequires: gnupg2
%endif
BuildRequires:  gcc, clang
BuildRequires:  coreutils, perl-interpreter, sed, zlib-devel, /usr/bin/cmp
BuildRequires:  perl(Test::Harness), perl(Test::More), perl(Math::BigInt)
BuildRequires:  perl(Module::Load::Conditional), perl(File::Temp) perl(Time::Piece)
BuildRequires:  perl(Time::HiRes), perl(IPC::Cmd), perl(Pod::Html), perl(Digest::SHA)
BuildRequires:  perl(FindBin), perl(lib), perl(File::Compare), perl(File::Copy), perl(bigint)

Provides:       fips-provider-so
Provides:       bundled(openssl) = %{osslver}

%description
This package provides a cryptographic module that is both an OpenSSL provider
as well as a PKCS#11 software token.

%files
%attr(0755,root,root) %{_libdir}/pkcs11
%attr(0755,root,root) %{_libdir}/ossl-modules
# These so-files are plugins, not libraries, and need not be versioned
%{_libdir}/ossl-modules/fips.so
%{_libdir}/pkcs11/fipstokn.so
%license LICENSE.txt
%license LICENSE.dependencies

%prep
%if %{with gpgcheck}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
# Preps kryoptic
%setup -n kryoptic-%{version} -q
%autopatch -p1 -M 199
%cargo_prep
%setup -n kryoptic-%{version} -q -T -D -a 3
pushd openssl-%{osslver}
%autopatch -p1 -m 200

%generate_buildrequires
%cargo_generate_buildrequires -n -f %{features}

%build
# Figure out which flags we want to use.
# default
sslarch=%{_os}-%{_target_cpu}
%ifarch x86_64
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch s390x
sslarch="linux64-s390x"
sslflags=no-ec_nistp_64_gcc_128
%endif
%ifarch aarch64
sslarch="linux-aarch64"
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch ppc64le
sslarch="linux-ppc64le"
sslflags=enable-ec_nistp_64_gcc_128
%endif
%ifarch %ix86
sslarch=linux-elf
%endif

# Add -Wa,--noexecstack here so that libcrypto's assembler modules will be
# marked as not requiring an executable stack.
# Also add -DPURIFY to make using valgrind with openssl easier as we do not
# want to depend on the uninitialized memory as a source of entropy anyway.
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wa,--noexecstack -Wa,--generate-missing-build-notes=yes -DPURIFY $RPM_LD_FLAGS -Wl,--allow-multiple-definition"

pushd openssl-%{osslver}

./Configure \
    --prefix=%{_prefix} --openssldir=%{_sysconfdir}/pki/tls \
    ${sslflags} ${sslarch} enable-fips \
    no-deprecated no-engine no-legacy no-tests \
    no-atexit no-comp no-egd no-static-engine no-ui-console \
    no-dgram no-http no-ssl no-ssl-trace no-sock no-srtp \
    no-dtls no-dtls1-method no-dtls1_2-method \
    no-tls no-tls1-method no-tls1_1-method no-tls1_2-method \
    no-aria no-argon2 no-blake2 no-camellia no-cast no-chacha \
    no-des no-dsa no-ec2m no-gost no-idea no-ktls no-mdc2 \
    no-md4 no-poly1305 no-rc2 no-rc4 no-rc5 no-rmd160 no-seed no-siphash \
    no-sm2 no-sm2-precomp no-sm3 no-sm4 no-whirlpool \
    -DDEVRANDOM='"\"/dev/urandom\""' \
    -DOPENSSL_PEDANTIC_ZEROIZATION \
    -DKRYOPTIC_FIPS_VENDOR='"\"Kryoptic FIPS Provider\""' \
    -DKRYOPTIC_FIPS_VERSION='"\"%{version}\""' \
    -DKRYOPTIC_FIPS_BUILD='"\"%{srpmhash}\""'

#Log selection in build logs
perl configdata.pm --dump

make -s %{?_smp_mflags} all

popd

export KRYOPTIC_OPENSSL_SOURCES=${PWD}/openssl-%{osslver}
%cargo_build -n -f %{features}
%{cargo_license_summary}
%{cargo_license -n -f %{features}} > LICENSE.dependencies

%if %{with check}
%check
export KRYOPTIC_OPENSSL_SOURCES=${PWD}/openssl-%{osslver}
%cargo_test -n -f %{features}
%endif

%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    pushd openssl-%{osslver} \
    %{SOURCE4} $RPM_BUILD_ROOT/%{_libdir}/ossl-modules/fips.so \
%{nil}

%install
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/ossl-modules
install -m755 target/release/libkryoptic_pkcs11.so $RPM_BUILD_ROOT/%{_libdir}/ossl-modules/fips.so
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/pkcs11
ln -s ../ossl-modules/fips.so $RPM_BUILD_ROOT%{_libdir}/pkcs11/fipstokn.so

%changelog
%autochangelog
