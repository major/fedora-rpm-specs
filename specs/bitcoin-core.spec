%define _hardened_build 1
%global _compldir %{_datadir}/bash-completion/completions
%global project_name bitcoin

%bcond_with extended_tests

Name:       bitcoin-core
Version:    28.1
Release:    5%{?dist}
Summary:    Peer to Peer Cryptographic Currency
License:    MIT
URL:        https://bitcoincore.org/

# In .gitignore, so no chance to commit to SCM:
Source0:    https://bitcoincore.org/bin/bitcoin-core-%{version}/%{project_name}-%{version}.tar.gz
Source1:    https://bitcoincore.org/bin/bitcoin-core-%{version}/SHA256SUMS.asc
Source2:    https://bitcoincore.org/bin/bitcoin-core-%{version}/SHA256SUMS

# Key verificaton process - Make official verify method work offline
# - Keys listed to sign the release are listed in SHA256SUMS.asc.
# - Keys can be hosted on different key servers.
# - Keys used to sign the release might have been revoked or removed.
# - Three or more keys is enough to validate the release, but there is no preferred key.
# - Verification needs to happen offline.
# - We don't want to touch the original SHA256SUM.asc file.
Source3:    %{project_name}-gpg.sh
Source4:    %{project_name}-offline-pubring.gpg

Source5:    %{project_name}-tmpfiles.conf
Source6:    %{project_name}.sysconfig
Source7:    %{project_name}.service.system
Source8:    %{project_name}.service.user
Source9:    %{project_name}-qt.protocol
Source10:   %{project_name}-qt.desktop

# Documentation
Source11:   %{project_name}.conf.example
Source12:   README.gui.redhat
Source13:   README.utils.redhat
Source14:   README.server.redhat

# Berkeley DB non-strong cryptography variant (NC)
Source15:   https://download.oracle.com/berkeley-db/db-4.8.30.NC.tar.gz
Source16:   db-4.8.30.NC-format-security.patch
Source17:   db-4.8.30.NC-configure-c99.patch

# AppStream metadata
Source18:   %{project_name}-qt.metainfo.xml

# Patch verify script to use local keyring
Patch0:     %{project_name}-verify-offline.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel >= 1.64.0
BuildRequires:  checkpolicy
BuildRequires:  desktop-file-utils
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  libnatpmp-devel
BuildRequires:  libtool
BuildRequires:  miniupnpc-devel
BuildRequires:  procps-ng
BuildRequires:  python3
BuildRequires:  pkgconfig(libevent) >= 2.1.8
BuildRequires:  pkgconfig(libevent_pthreads) >= 2.1.8
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libzmq) >= 4
BuildRequires:  pkgconfig(sqlite3) >= 3.7.17
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd
BuildRequires:  systemtap-sdt-devel

%description
Bitcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitcoins is carried out collectively by the network.

%package desktop
Summary:    Peer to Peer Cryptographic Currency
Conflicts:  bitcoin
Provides:   bundled(leveldb) = 1.22.0
Provides:   bundled(libdb) = 4.8.30.NC
Provides:   bundled(secp256k1) = 0.1
Provides:   bundled(univalue) = 1.1.3

%description desktop
Bitcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitcoins is carried out collectively by the network.

This package contains the Qt based graphical client and node. If you are looking
to run a Bitcoin wallet, this is probably the package you want.

%package devel
Summary:    Peer-to-peer digital currency
Conflicts:  bitcoin-devel
Provides:   %{name}-libs = %{version}-%{release}
Obsoletes:  %{name}-libs < %{version}-%{release}

%description devel
This package contains the bitcoin utility tool.

Most people do not need this package installed.

%package utils
Summary:    Peer-to-peer digital currency
Conflicts:  bitcoin-utils

%description utils 
Bitcoin is an experimental new digital currency that enables instant payments to
anyone, anywhere in the world. Bitcoin uses peer-to-peer technology to operate
with no central authority: managing transactions and issuing money are carried
out collectively by the network.

This package provides bitcoin-cli, a utility to communicate with and
control a Bitcoin server via its RPC protocol, and bitcoin-tx, a utility
to create custom Bitcoin transactions.

%package server
Summary:        Peer-to-peer digital currency
Conflicts:      bitcoin-server
Requires(pre):  shadow-utils
Requires:       (%{name}-selinux >= 0.1 if selinux-policy)
Provides:       bundled(leveldb) = 1.22.0
Provides:       bundled(libdb) = 4.8.30.NC
Provides:       bundled(secp256k1) = 0.1
Provides:       bundled(univalue) = 1.1.3

%description server
This package provides a stand-alone bitcoin-core daemon. For most users, this
package is only needed if they need a full-node without the graphical client.

Some third party wallet software will want this package to provide the actual
bitcoin-core node they use to connect to the network.

If you use the graphical bitcoin-core client then you almost certainly do not
need this package.

%prep
%autosetup -p1 -n %{project_name}-%{version}

# Bundled script to verify release signatures using offline pubring:
cp %{SOURCE4} .
contrib/verify-binaries/verify.py --min-good-sigs 3 bin %{SOURCE2} %{SOURCE0}

# Check the hash of the tarball, not in the same folder where we are now:
grep -q $(sha256sum %{SOURCE0}) %{SOURCE2}

# No publicly available hash file, check it against what bitcoin-core expects:
export BDB_HASH=$(grep sha256_hash depends/packages/bdb.mk | sed -e "s/.*=//g")
echo $BDB_HASH %{SOURCE15} | sha256sum -c

# Berkeley DB:
mkdir db4
tar --strip-components=1 -xzf %{SOURCE15} -C db4
patch -d db4 -p1 -i ../depends/patches/bdb/clang_cxx_11.patch
patch -d db4 -p1 -i %{SOURCE16}
patch -d db4 -p1 -i %{SOURCE17}
# Avoid any modification timestamp based regeneration of the configure
# script due to patching above:
touch -r db4/dist/configure db4/dist/configure.ac db4/dist/aclocal/*.m4

# Documentation (sources can not be directly reference with doc)
cp -p %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} .

%build
# Build static Berkeley DB reusing all compiler flags / hardening:
pushd db4/build_unix

%define _configure ../dist/configure
%configure \
    --disable-shared \
    --enable-cxx \
    --disable-replication
%undefine _configure

%make_build
make install DESTDIR=%{_builddir}/%{buildsubdir}/db4
popd

export BDB_CFLAGS="-I%{_builddir}/%{buildsubdir}/db4%{_includedir}/"
export BDB_LIBS="-L%{_builddir}/%{buildsubdir}/db4%{_libdir}/ -ldb_cxx-4.8"
autoreconf -vif
%configure \
    --disable-bench \
    --disable-silent-rules \
    --disable-static \
    --enable-reduce-exports \
    --enable-threadlocal \
    --enable-usdt \
    --with-daemon \
    --with-gui=qt5 \
    --with-libs \
    --with-miniupnpc \
    --with-qrencode \
    --with-qtdbus \
    --with-utils

%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

# Temporary files
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{project_name}.conf

# Install ancillary files
install -D -m600 -p %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/%{project_name}
install -D -m644 -p %{SOURCE7} %{buildroot}%{_unitdir}/%{project_name}.service
install -D -m644 -p %{SOURCE8} %{buildroot}%{_userunitdir}/%{project_name}.service
install -D -m644 -p %{SOURCE9} %{buildroot}%{_datadir}/kde4/services/%{project_name}-qt.protocol
install -d -m750 -p %{buildroot}%{_sharedstatedir}/%{project_name}
install -d -m750 -p %{buildroot}%{_sysconfdir}/%{project_name}

# Desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE10}

# Icons
for size in 16 32 64 128 256; do
    install -p -D -m 644 share/pixmaps/%{project_name}${size}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{project_name}.png
done
rm -f %{buildroot}%{_datadir}/pixmaps/%{project_name}*

# Bash completion
install -D -m644 -p contrib/completions/bash/%{project_name}-cli.bash %{buildroot}%{_compldir}/%{project_name}-cli
install -D -m644 -p contrib/completions/bash/%{project_name}-tx.bash %{buildroot}%{_compldir}/%{project_name}-tx
install -D -m644 -p contrib/completions/bash/%{project_name}d.bash %{buildroot}%{_compldir}/%{project_name}d

# Server log directory
mkdir -p %{buildroot}%{_localstatedir}/log/%{project_name}/

# AppStream metadata
install -p -m 644 -D %{SOURCE18} %{buildroot}%{_metainfodir}/%{project_name}-qt.metainfo.xml

# Remove test files so that they aren't shipped. Tests have already been run.
rm -f %{buildroot}%{_bindir}/test_*

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{project_name}-qt.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{project_name}-qt.metainfo.xml
make check
%if %{with extended_tests}
test/functional/test_runner.py --tmpdirprefix `pwd` --extended
%endif

%pre server
getent group %{project_name} >/dev/null || groupadd -r %{project_name}
getent passwd %{project_name} >/dev/null ||
    useradd -r -g %{project_name} -d /var/lib/%{project_name} -s /sbin/nologin \
    -c "Bitcoin wallet server" %{project_name}
exit 0

%post server
%systemd_post %{project_name}.service

%preun server
%systemd_preun %{project_name}.service

%postun server
%systemd_postun_with_restart %{project_name}.service

%files desktop
%license COPYING
%doc %{project_name}.conf.example README.gui.redhat README.md SECURITY.md
%doc doc/assets-attribution.md doc/bips.md doc/files.md doc/reduce-traffic.md doc/release-notes.md doc/tor.md
%{_bindir}/%{project_name}-qt
%{_datadir}/applications/%{project_name}-qt.desktop
%{_datadir}/kde4/services/%{project_name}-qt.protocol
%{_datadir}/icons/hicolor/*/apps/%{project_name}.png
%{_mandir}/man1/%{project_name}-qt.1*
%{_metainfodir}/%{project_name}-qt.metainfo.xml

%files devel
%doc doc/developer-notes.md
%{_bindir}/%{project_name}-util
%{_mandir}/man1/%{project_name}-util.1*

%files utils
%license COPYING
%doc %{project_name}.conf.example README.utils.redhat SECURITY.md
%doc doc/README.md
%{_bindir}/%{project_name}-cli
%{_bindir}/%{project_name}-tx
%{_bindir}/%{project_name}-wallet
%{_compldir}/%{project_name}-cli
%{_compldir}/%{project_name}-tx
%{_mandir}/man1/%{project_name}-cli.1*
%{_mandir}/man1/%{project_name}-tx.1*
%{_mandir}/man1/%{project_name}-wallet.1*

%files server
%license COPYING
%doc %{project_name}.conf.example README.server.redhat SECURITY.md
%doc doc/README.md doc/REST-interface.md doc/bips.md doc/dnsseed-policy.md doc/files.md doc/reduce-traffic.md doc/release-notes.md doc/tor.md doc/zmq.md
%dir %attr(750,%{project_name},%{project_name}) %{_sharedstatedir}/%{project_name}
%dir %attr(750,%{project_name},%{project_name}) %{_sysconfdir}/%{project_name}
%dir %attr(750,%{project_name},%{project_name}) %{_localstatedir}/log/%{project_name}
%ghost %{_localstatedir}/log/%{project_name}/debug.log
%ghost %dir %{_rundir}/%{project_name}/
%ghost %{_rundir}/%{project_name}.pid
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/sysconfig/%{project_name}
%{_compldir}/%{project_name}d
%{_mandir}/man1/%{project_name}d.1*
%{_bindir}/%{project_name}d
%{_tmpfilesdir}/%{project_name}.conf
%{_unitdir}/%{project_name}.service
%{_userunitdir}/%{project_name}.service

%changelog
* Fri Feb 07 2025 Simone Caronni <negativo17@gmail.com> - 28.1-5
- Rebuild for updated dependencies.

* Tue Jan 28 2025 Simone Caronni <negativo17@gmail.com> - 28.1-4
- Rebuild for updated dependencies.

* Tue Jan 28 2025 Simone Caronni <negativo17@gmail.com> - 28.1-3
- Update for https://fedoraproject.org/wiki/Changes/Unify_bin_and_sbin.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 11 2025 Simone Caronni <negativo17@gmail.com> - 28.1-1
- Update to 28.1.

* Sat Jan 11 2025 Simone Caronni <negativo17@gmail.com> - 28.0-4
- Enable Statically Defined Tracing (USDT).

* Wed Oct 16 2024 Simone Caronni <negativo17@gmail.com> - 28.0-3
- Remove leftover of bitcoin-libs being erroneusly required by the devel
  subpackage.

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 28.0-2
- Rebuild for updated miniupnpc 2.2.8.

* Tue Oct 08 2024 Simone Caronni <negativo17@gmail.com> - 28.0-1
- Update to 28.0.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Simone Caronni <negativo17@gmail.com> - 27.1-1
- Update to 27.1.

* Wed May 22 2024 Simone Caronni <negativo17@gmail.com> - 27.0-1
- Update to 27.0.

* Wed Apr 24 2024 Simone Caronni <negativo17@gmail.com> - 26.1-1
- Update to 26.1.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Simone Caronni <negativo17@gmail.com> - 26.0-1
- Update to 26.0.

* Fri Oct 20 2023 Simone Caronni <negativo17@gmail.com> - 25.1-1
- Update to 25.1.

* Fri Aug 11 2023 Simone Caronni <negativo17@gmail.com> - 25.0-3
- Adjust verify script invocation.
- Fix build on el8.
- Drop unused build requirement.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Simone Caronni <negativo17@gmail.com> - 25.0-1
- Update to 25.0.
- Update verification of signatures to use the new bundled script.

* Mon May 22 2023 Simone Caronni <negativo17@gmail.com> - 24.1-1
- Update to 24.1.

* Fri Mar 17 2023 Arjun Shankar <arjun@redhat.com> - 24.0.1-3
- Port bundled Berkeley DB 4.8 configure script to C99 (#2179373)

* Fri Mar 17 2023 Arjun Shankar <arjun@redhat.com>
- Fix build failure due to GCC 13 compile error (#2171449)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Simone Caronni <negativo17@gmail.com> - 24.0.1-1
- Update to 24.0.1

* Mon Nov 21 2022 Simone Caronni <negativo17@gmail.com> - 24.0-1
- Update to 24.0.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 26 2022 Simone Caronni <negativo17@gmail.com> - 23.0-1
- Update to 23.0.

* Thu Apr 07 2022 Simone Caronni <negativo17@gmail.com> - 22.0-7
- Add AppStream metadata.

* Tue Apr 05 2022 Simone Caronni <negativo17@gmail.com> - 22.0-6
- Hide extended tests behind a flag.
- Allow to run the full set of extended tests including network when requested,
  they run fine in mock with network enabled.

* Sun Jan 23 2022 Simone Caronni <negativo17@gmail.com> - 22.0-5
- Update GPG verification script (thanks Björn Persson).

* Sun Oct 03 2021 Simone Caronni <negativo17@gmail.com> - 22.0-4
- Switch to bundled statically linked Berkeley DB 4.8.30 (NC).

* Sat Sep 25 2021 Simone Caronni <negativo17@gmail.com> - 22.0-3
- Remove obsolete scriptlets.
- With RHEL/CentOS 7 no longer a target, improve systemd unit security.
- Add systemd user unit to start bitcoind in your user session.
- Move bitcoin-wallet to utils subpackage for offline wallet manipulation.
- Update README files.

* Sat Sep 25 2021 Simone Caronni <negativo17@gmail.com> - 22.0-2
- Prepare all keys with a script and verify all keys against the signature file.
  Add reasoning on the process in the SPEC file.

* Wed Sep 22 2021 Simone Caronni <negativo17@gmail.com> - 22.0-1
- Update to 22.0, versioning convention change.
- Implement signature verification with a public GPG keyring and at least one
  valid signature.
- Also the relative selinux package has been renamed to bitcoin-core-selinux.
- Add bitcoin-util to devel subpackage.
- Update docs.
- Add SQLite as dependency for descriptor wallets.
- Drop RHEL/CentOS 7 support.

* Tue Sep 21 2021 Simone Caronni <negativo17@gmail.com> - 0.21.1-2
- Rename package to bitcoin-core.
- Conflicts with bitcoin.
- Desktop subpackage renamed from "core" to "desktop".

* Wed May 12 2021 Simone Caronni <negativo17@gmail.com> - 0.21.1-1
- Update to 0.21.1.

* Wed Mar 10 2021 Simone Caronni <negativo17@gmail.com> - 0.21.0-4
- Fix build on RHEL/CentOS 8.
- Adjust SELinux requirement for server subpackage.

* Wed Mar 10 2021 Simone Caronni <negativo17@gmail.com> - 0.21.0-3
- Remove requirements for utils subpackage in server subpackage.
- Separate SELinux package in its own subpackage and use RPM rich booleans on
  Fedora and RHEL/CentOS 8+ to install the SELinux package if the base policy is
  installed.
- Update server README.

* Wed Jan 20 2021 Simone Caronni <negativo17@gmail.com> - 0.21.0-2
- Update to 0.21.0.
- Remove java build requirement.
- Use local folder for test output.

* Fri Jan 15 2021 Simone Caronni <negativo17@gmail.com> - 0.21.0-1
- Update to 0.21.0.

* Thu Nov 19 2020 Simone Caronni <negativo17@gmail.com> - 0.20.1-2
- Remove openssl/protobuf from build requirements.

* Wed Oct 21 2020 Simone Caronni <negativo17@gmail.com> - 0.20.1-1
- Update to 0.20.1.

* Wed Jul 22 2020 Simone Caronni <negativo17@gmail.com> - 0.20.0-7
- Use libdb 5.x instead of deprecated 4.x. Fixes build on RHEL/CentOS 8.

* Tue Jul 21 2020 Simone Caronni <negativo17@gmail.com> - 0.20.0-6
- Update systemd unit.
- Update configuration options.
- Declared bundled libraries/forks.

* Tue Jul 21 2020 Simone Caronni <negativo17@gmail.com> - 0.20.0-5
- Use HTTPS for url tag.
- Reorganize sources. Add cleaned files from the packaging repository directly;
  bash completion snippets are now supported in the main sources.
- Move check section after install and include desktop file validating in there.

* Sun Jul 19 2020 Simone Caronni <negativo17@gmail.com> - 0.20.0-4
- Fix tests on RHEL/CentOS 7.

* Sat Jul 18 2020 Simone Caronni <negativo17@gmail.com> - 0.20.0-3
- Add signature verification.
- Trim changelog.
- Fix typo in the libs description.

* Tue Jun 30 2020 Simone Caronni <negativo17@gmail.com> - 0.20.0-2
- Update Source0 URL.
- Do not obsolete "bitcoin", just leave the provider for it.
- Let the build install the man pages.
- Make sure old post scriptlets run only on RHEL/CentOS 7.
- Do not install static library and archive.
- Be explicit with shared object versions.
- Use macros for more directories.
- Use GCC 9 and not 7 to build on RHEL/CentOS 7.

* Fri Jun 26 2020 Simone Caronni <negativo17@gmail.com> - 0.20.0-1
- Update to 0.20.0.

* Mon May 04 2020 Simone Caronni <negativo17@gmail.com> - 0.19.1-1
- Update to 0.19.1.
- Fix deprecation message with Python tests.
- Trim changelog.

* Fri Feb 21 2020 Simone Caronni <negativo17@gmail.com> - 0.19.0.1-2
- Fix dependencies with Python SELinux interfaces.

* Tue Nov 19 2019 Simone Caronni <negativo17@gmail.com> - 0.19.0.1-1
- Update to 0.19.0.1.

* Sun Nov 17 2019 Simone Caronni <negativo17@gmail.com> - 0.19.0-1
- Update to 0.19.0.

* Thu Sep 12 2019 Simone Caronni <negativo17@gmail.com> - 0.18.1-1
- Update to 0.18.1.

* Tue May 07 2019 Simone Caronni <negativo17@gmail.com> - 0.18.0-2
- Update systemd unit.

* Mon May 06 2019 Simone Caronni <negativo17@gmail.com> - 0.18.0-1
- Update to 0.18.0.
- Force C.UTF-8 for tests on Fedora and disable EPEL 7 test run.

* Thu Jan 24 2019 Simone Caronni <negativo17@gmail.com> - 0.17.1-1
- Update to 0.17.1.
