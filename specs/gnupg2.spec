%bcond_with bootstrap

%global split_min_version 2.4.9-4.fc42.1

Summary: Utility for secure communication and data storage
Name:    gnupg2
Version: 2.4.9
Release: %autorelease

License: CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND (BSD-3-Clause OR LGPL-3.0-or-later OR GPL-2.0-or-later) AND CC-BY-4.0 AND MIT
Source0: https://gnupg.org/ftp/gcrypt/%{?pre:alpha/}gnupg/gnupg-%{version}%{?pre}.tar.bz2
Source1: https://gnupg.org/ftp/gcrypt/%{?pre:alpha/}gnupg/gnupg-%{version}%{?pre}.tar.bz2.sig
Source2: https://gnupg.org/signature_key.asc
Source3: gnupg2.sh
Source4: gnupg2.csh
# initialize small amount of secmem for list of algorithms in help
# (#598847) (necessary in the FIPS mode of libgcrypt)
Patch1:  gnupg-2.4.7-secmem.patch
# non-upstreamable patch adding file-is-digest option needed for Copr
# https://dev.gnupg.org/T1646
Patch2:  gnupg-2.4.7-file-is-digest.patch
# Disable brainpool tests as they are not built into our libgcrypt
# Disable MD160 in FIPS mode (#879047)
Patch3:  gnupg-2.4.7-fips-algo.patch
# CVE-2026-24882: Stack-based buffer overflow in tpm2daemon allows arbitrary code execution
# https://dev.gnupg.org/T8045
Patch4:  gnupg-2.4.9-tpm2daemon.patch

# Patches from FreePG:
# https://gitlab.com/freepg/gnupg/-/tree/main/STABLE-BRANCH-2-4-freepg
Patch20: 0002-gpg-accept-subkeys-with-a-good-revocation-but-no-sel.patch
Patch21: 0003-gpg-allow-import-of-previously-known-keys-even-witho.patch
Patch22: 0004-tests-add-test-cases-for-import-without-uid.patch
Patch23: 0005-gpg-drop-import-clean-from-default-keyserver-import-.patch
Patch24: 0006-Do-not-use-OCB-mode-even-if-AEAD-OCB-key-preference-.patch
Patch25: 0007-Revert-the-introduction-of-the-RFC4880bis-draft-into.patch
Patch26: 0008-avoid-systemd-deprecation-warning.patch
Patch27: 0009-Add-systemd-support-for-keyboxd.patch
Patch28: 0010-Ship-sample-systemd-unit-files.patch
Patch29: 0011-el-gamal-default-to-3072-bits.patch
Patch30: 0012-gpg-default-digest-algorithm-SHA512.patch
Patch31: 0013-gpg-Prefer-SHA-512-and-SHA-384-in-personal-digest.patch
Patch32: 0018-Avoid-simple-memory-dumps-via-ptrace.patch
Patch34: 0029-Add-keyboxd-systemd-support.patch
Patch35: 0033-Support-large-RSA-keygen-in-non-batch-mode.patch

# Fixes for issues found in Coverity scan - reported upstream
Patch40: gnupg-2.4.7-coverity.patch

# add a root certificate bundle due to changes in ca-certificates (#2380121)
Patch45: gnupg-2.4.8-ca-certificates-bundle.patch

URL:     https://www.gnupg.org/

BuildRequires: gcc
BuildRequires: bzip2-devel
BuildRequires: curl-devel
BuildRequires: docbook-utils
BuildRequires: gettext
%if %{without bootstrap}
# Require gnupg2 to verify sources, unless bootstrapping
BuildRequires: gnupg2
%endif
BuildRequires: libassuan-devel >= 2.5.0
BuildRequires: libgcrypt-devel >= 1.9.1
BuildRequires: libgpg-error-devel >= 1.46
BuildRequires: libksba-devel >= 1.6.3
BuildRequires: openldap-devel
BuildRequires: pcsc-lite-libs
BuildRequires: ncurses-devel
BuildRequires: npth-devel
BuildRequires: readline-devel
BuildRequires: zlib-devel
BuildRequires: gnutls-devel
BuildRequires: sqlite-devel
BuildRequires: fuse
BuildRequires: make
BuildRequires: systemd-rpm-macros
BuildRequires: texinfo
BuildRequires: tpm2-tss-devel
# for tests
BuildRequires: openssh-clients
BuildRequires: swtpm

Requires: libgcrypt >= 1.9.1
Requires: libgpg-error >= 1.46

Requires: gnupg2-dirmngr%{?_isa} = %{version}-%{release}
Requires: gnupg2-gpgconf%{?_isa} = %{version}-%{release}
Requires: gnupg2-gpg-agent%{?_isa} = %{version}-%{release}
Requires: gnupg2-keyboxd%{?_isa} = %{version}-%{release}
Requires: gnupg2-verify%{?_isa} = %{version}-%{release}

Recommends: pinentry

# pgp-tools, perl-GnuPG-Interface requires 'gpg' (not sure why) -- Rex
Provides: gpg = %{version}-%{release}
# Obsolete GnuPG-1 package
Provides: gnupg = %{version}-%{release}
Obsoletes: gnupg < 1.4.24

# ensures upgrade path for existing installs
Obsoletes: gnupg2 < %{split_min_version}

Provides: dirmngr = %{version}-%{release}
Obsoletes: dirmngr < 1.2.0-1

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
GnuPG is GNU's tool for secure communication and data storage.  It can
be used to encrypt data and to create digital signatures.  It includes
an advanced key management facility and is compliant with the proposed
OpenPGP Internet standard as described in RFC2440 and the S/MIME
standard as described by several RFCs.

GnuPG 2.0 is a newer version of GnuPG with additional support for
S/MIME.  It has a different design philosophy that splits
functionality up into several modules. The S/MIME and smartcard functionality
is provided by the gnupg2-smime package.

%package dirmngr
Summary: GnuPG network certificate management service
Requires: gnupg2-gpgconf%{?_isa} = %{version}-%{release}
Conflicts: gnupg2 < %{split_min_version}

%description dirmngr
GnuPG is GNU's tool for secure communication and data storage. This
package contains the network certificate management service.

%package g13
Summary: GnuPG tool for managing encrypted file system containers
Requires: gnupg2%{?_isa} = %{version}-%{release}
Conflicts: gnupg2 < %{split_min_version}
Obsoletes: gnupg2 < %{split_min_version}

%description g13
GnuPG is GNU's tool for secure communication and data storage. This
package contains the g13 tool managing encrypted file system containers.

%package gpgconf
Summary: GnuPG core configuration utilities
Conflicts: gnupg2 < %{split_min_version}

%description gpgconf
GnuPG is GNU's tool for secure communication and data storage. This
package contains the core configuration utilities.

%package gpg-agent
Summary: GnuPG cryptographic agent
Requires: gnupg2-gpgconf%{?_isa} = %{version}-%{release}
Conflicts: gnupg2 < %{split_min_version}

%description gpg-agent
GnuPG is GNU's tool for secure communication and data storage. This
package contains the cryptographic agent.

%package keyboxd
Summary: GnuPG public key material service
Conflicts: gnupg2 < %{split_min_version}

%description keyboxd
GnuPG is GNU's tool for secure communication and data storage. This
package contains the public key material service.

%package scdaemon
Summary: GnuPG SmartCard daemon
Requires: gnupg2%{?_isa} = %{version}-%{release}
Conflicts: gnupg2 < %{split_min_version}
Obsoletes: gnupg2 < %{split_min_version}
# for USB smart card support
Recommends: pcsc-lite-ccid

%description scdaemon
GnuPG is GNU's tool for secure communication and data storage. This
package contains the SmartCard daemon.

%package smime
Summary: CMS encryption and signing tool and smart card support for GnuPG
Requires: gnupg2%{?_isa} = %{version}-%{release}

%description smime
GnuPG is GNU's tool for secure communication and data storage. This
package adds support for smart cards and S/MIME encryption and signing
to the base GnuPG package.

%package utils
Summary: GnuPG utilities
Requires: gnupg2%{?_isa} = %{version}-%{release}
Conflicts: gnupg2 < %{split_min_version}
Obsoletes: gnupg2 < %{split_min_version}

%description utils
GnuPG is GNU's tool for secure communication and data storage. This
package includes additional utilities.

%package verify
Summary: GnuPG signature verification tool
Conflicts: gnupg2 < %{split_min_version}

%description verify
GnuPG is GNU's tool for secure communication and data storage. This
package contains the signature verification tool.

%package wks
Summary: GnuPG Web Key Service client and server
Requires: gnupg2%{?_isa} = %{version}-%{release}
Conflicts: gnupg2 < %{split_min_version}
Obsoletes: gnupg2 < %{split_min_version}

%description wks
GnuPG is GNU's tool for secure communication and data storage. This
package contains the GnuPG Web Key Service client and server.


%prep
%if ! %{with bootstrap}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q -n gnupg-%{version}

%patch 1 -p1 -b .secmem
%patch 2 -p1 -b .file-is-digest
%patch 3 -p1 -b .fips
%patch 4 -p1 -b .tpm2d

%patch 20 -p1 -b .good_revoc
%patch 21 -p1 -b .prev_known_key
%patch 22 -p1 -b .test_missing_uid
%patch 23 -p1 -b .import-clean
%patch 24 -p1 -b .do-not-use-OCB
%patch 25 -p1 -b .revert-rfc4880bis
%patch 26 -p1 -b .systemd-deprecation
%patch 27 -p1 -b .systemd-keybox
%patch 28 -p1 -b .systemd-units
%patch 29 -p1 -b .elgamal-3k
%patch 30 -p1 -b .default-sha512
%patch 31 -p1 -b .prefer-sha512
%patch 32 -p1 -b .dump-ptrace
%patch 34 -p1 -b .keyboxd-units
%patch 35 -p1 -b .large-rsa

%patch 40 -p1 -b .coverity
%patch 45 -p1 -b .cert-bundle

# pcsc-lite library major: 0 in 1.2.0, 1 in 1.2.9+ (dlopen()'d in pcsc-wrapper)
# Note: this is just the name of the default shared lib to load in scdaemon,
# it can use other implementations too (including non-pcsc ones).
%global pcsclib %(basename $(ls -1 %{_libdir}/libpcsclite.so.? 2>/dev/null ) 2>/dev/null )

sed -i -e 's/"libpcsclite\.so"/"%{pcsclib}"/' scd/scdaemon.c


%build
%configure \
  --disable-rpath \
  --enable-g13 \
  --disable-ccid-driver \
  --with-tss=intel \
  --enable-large-secmem

# need scratch gpg database for tests
mkdir -p $HOME/.gnupg

%make_build


%install
%make_install \
  docdir=%{_pkgdocdir}

%find_lang %{name}

# gpgconf.conf
mkdir -p %{buildroot}%{_sysconfdir}/gnupg
touch %{buildroot}%{_sysconfdir}/gnupg/gpgconf.conf
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -p %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d

# more docs
install -m644 -p AUTHORS NEWS THANKS TODO \
  %{buildroot}%{_pkgdocdir}

# compat symlinks
ln -sf gpg %{buildroot}%{_bindir}/gpg2
ln -sf gpgv %{buildroot}%{_bindir}/gpgv2
ln -sf gpg.1 %{buildroot}%{_mandir}/man1/gpg2.1
ln -sf gpgv.1 %{buildroot}%{_mandir}/man1/gpgv2.1
ln -sf gnupg.7 %{buildroot}%{_mandir}/man7/gnupg2.7

# info dir
rm -f %{buildroot}%{_infodir}/dir

# drop the gpg scheme interpreter
rm -f %{buildroot}%{_bindir}/gpgscm

# Move the systemd user units to appropriate directory
install -d -m755 %{buildroot}%{_userunitdir}
install -p doc/examples/systemd-user/*.socket %{buildroot}%{_userunitdir}
install -p doc/examples/systemd-user/*.service %{buildroot}%{_userunitdir}

%check
# need scratch gpg database for tests
mkdir -p $HOME/.gnupg
make -k check


%post dirmngr
%systemd_user_post dirmngr.service

%preun dirmngr
%systemd_user_preun dirmngr.service

%postun dirmngr
%systemd_user_postun_with_restart dirmngr.service

%post gpg-agent
%systemd_user_post gpg-agent.service

%preun gpg-agent
%systemd_user_preun gpg-agent.service

%postun gpg-agent
%systemd_user_postun_with_restart gpg-agent.service

%post keyboxd
%systemd_user_post keyboxd.service

%preun keyboxd
%systemd_user_preun keyboxd.service

%postun keyboxd
%systemd_user_postun_with_restart keyboxd.service


%files -f %{name}.lang
%license COPYING
%{_sysconfdir}/profile.d/gnupg2.sh
%{_sysconfdir}/profile.d/gnupg2.csh
## docs say to install suid root, but fedora/rh security folk say not to
%{_bindir}/gpg
%{_bindir}/gpg2
%{_infodir}/gnupg.info*
%{_mandir}/man?/gpg.*
%{_mandir}/man?/gpg2.*
%{_mandir}/man?/gnupg.*
%{_mandir}/man?/gnupg2.*
%{_pkgdocdir}/
%{_datadir}/gnupg/help*.txt

%files dirmngr
%license COPYING
%{_bindir}/dirmngr
%{_bindir}/dirmngr-client
%{_libexecdir}/dirmngr_ldap
%{_userunitdir}/dirmngr.*
%{_mandir}/man?/dirmngr.*
%{_mandir}/man?/dirmngr-client.*
%dir %{_datadir}/gnupg/
%{_datadir}/gnupg/sks-keyservers.netCA.pem

%files g13
%{_bindir}/g13
%{_sbindir}/g13-syshelp

%files gpgconf
%license COPYING
%dir %{_sysconfdir}/gnupg
%ghost %config(noreplace) %{_sysconfdir}/gnupg/gpgconf.conf
%{_bindir}/gpgconf
%{_bindir}/gpg-connect-agent
%{_mandir}/man?/gpgconf*
%{_mandir}/man?/gpg-connect-agent.*
%dir %{_datadir}/gnupg
%{_datadir}/gnupg/distsigkey.gpg

%files gpg-agent
%license COPYING
%{_bindir}/gpg-agent
%{_libexecdir}/gpg-check-pattern
%{_libexecdir}/gpg-preset-passphrase
%{_libexecdir}/gpg-protect-tool
%{_libexecdir}/tpm2daemon
%{_userunitdir}/gpg-agent.*
%{_userunitdir}/gpg-agent-*.socket
%{_mandir}/man?/gpg-agent.*
%{_mandir}/man?/gpg-check-pattern.*
%{_mandir}/man?/gpg-preset-passphrase.*

%files keyboxd
%license COPYING
%{_libexecdir}/keyboxd
%{_userunitdir}/keyboxd.*

%files scdaemon
%{_bindir}/gpg-card
%{_libexecdir}/gpg-auth
%{_libexecdir}/scdaemon
%{_mandir}/man?/gpg-card.*
%{_mandir}/man?/scdaemon.*

%files smime
%{_bindir}/gpgsm
%{_mandir}/man?/gpgsm.*

%files utils
%{_bindir}/gpg-mail-tube
%{_bindir}/gpgparsemail
%{_bindir}/gpgsplit
%{_bindir}/gpgtar
%{_bindir}/kbxutil
%{_bindir}/watchgnupg
%{_sbindir}/addgnupghome
%{_sbindir}/applygnupgdefaults
%{_libexecdir}/gpg-pair-tool
%{_mandir}/man?/addgnupghome.*
%{_mandir}/man?/applygnupgdefaults.*
%{_mandir}/man?/gpg-mail-tube.*
%{_mandir}/man?/gpgparsemail.*
%{_mandir}/man?/gpgtar.*
%{_mandir}/man?/watchgnupg.*

%files verify
%license COPYING
%{_bindir}/gpgv
%{_bindir}/gpgv2
%{_mandir}/man?/gpgv.*
%{_mandir}/man?/gpgv2.*

%files wks
%{_bindir}/gpg-wks-client
%{_bindir}/gpg-wks-server
%{_libexecdir}/gpg-wks-client
%{_mandir}/man?/gpg-wks-client.*
%{_mandir}/man?/gpg-wks-server.*


%changelog
%autochangelog
