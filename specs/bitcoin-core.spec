%define _hardened_build 1
%global _compldir %{_datadir}/bash-completion/completions
%global project_name bitcoin

%bcond_with extended_tests

Name:       bitcoin-core
Version:    30.0
Release:    %autorelease
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

# AppStream metadata
Source18:   %{project_name}-qt.metainfo.xml

# Patch verify script to use local keyring
Patch0:     %{project_name}-verify-offline.patch

# Patch to set the shared object version to the main version
Patch1:     %{project_name}-shared.patch

BuildRequires:  boost-devel >= 1.64.0
BuildRequires:  capnproto
BuildRequires:  capnproto-devel
BuildRequires:  checkpolicy
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gnupg2
BuildRequires:  libappstream-glib
BuildRequires:  cmake > 3.22
BuildRequires:  procps-ng
BuildRequires:  python3
BuildRequires:  pkgconfig(libevent) >= 2.1.8
BuildRequires:  pkgconfig(libevent_pthreads) >= 2.1.8
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libzmq) >= 4
BuildRequires:  pkgconfig(sqlite3) >= 3.7.17
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  systemd
BuildRequires:  systemtap-sdt-devel

Requires:   %{name}-desktop = %{version}-%{release}
Requires:   %{name}-server = %{version}-%{release}
Requires:   %{name}-utils = %{version}-%{release}
Requires:   lib%{project_name}kernel = %{version}-%{release}

%description
Bitcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitcoins is carried out collectively by the network.

This package installs the full Bitcoin Core distribution, with utilities, server
and desktop (graphical wallet) components.

%package -n lib%{project_name}kernel
Summary:    Consensus engine and support library

%description -n lib%{project_name}kernel
Bitcoin Core consensus engine. A stateful library that can spawn threads, do
caching, do I/O, and many other things which one may not normally expect from a
library.

%package desktop
Summary:    Peer to Peer Cryptographic Currency
Provides:   bundled(leveldb)
Provides:   bundled(libmultiprocess)
Provides:   bundled(secp256k1)
Provides:   bundled(univalue)

%description desktop
Bitcoin is a digital cryptographic currency that uses peer-to-peer technology to
operate with no central authority or banks; managing transactions and the
issuing of bitcoins is carried out collectively by the network.

This package contains the Qt based graphical client and node. If you are looking
to run a Bitcoin wallet, this is probably the package you want.

%package devel
Summary:    Peer-to-peer digital currency
Requires:   lib%{project_name} = %{version}-%{release}

%description devel
This package contains the bitcoin utility tool.

Most people do not need this package installed.

%package utils
Summary:    Peer-to-peer digital currency

%description utils 
Bitcoin is an experimental new digital currency that enables instant payments to
anyone, anywhere in the world. Bitcoin uses peer-to-peer technology to operate
with no central authority: managing transactions and issuing money are carried
out collectively by the network.

This package provides bitcoin-cli, a utility to communicate with and
control a Bitcoin server via its RPC protocol, and bitcoin-tx, a utility
to create custom Bitcoin transactions.

%package server
Summary:    Peer-to-peer digital currency
Requires:   (%{name}-selinux >= 0.1 if selinux-policy)
Provides:   bundled(leveldb)
Provides:   bundled(libmultiprocess)
Provides:   bundled(secp256k1)
Provides:   bundled(univalue)

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

# Documentation (sources can not be directly reference with doc)
cp -p %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} .

# Create a sysusers.d config file
cat >bitcoin-core.sysusers.conf <<EOF
u bitcoin - 'Bitcoin wallet server' /var/lib/%{project_name} -
EOF

%build

# Bitcoin kernel library used only as part of the testing for now:
%cmake \
    -DBUILD_CLI=ON \
    -DBUILD_DAEMON=ON \
    -DBUILD_GUI=ON \
    -DBUILD_KERNEL_LIB=ON \
    -DBUILD_TESTS=ON \
    -DBUILD_TX=ON \
    -DBUILD_UTIL=ON \
    -DBUILD_UTIL_CHAINSTATE=ON \
    -DENABLE_IPC=ON \
    -DENABLE_WALLET=ON \
    -DINSTALL_MAN=ON \
    -DWITH_DBUS=ON \
    -DWITH_QRENCODE=ON \
    -DWITH_SQLITE=ON \
    -DWITH_USDT=ON \
    -DWITH_ZMQ=ON

%cmake_build

%install
%cmake_install

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

install -m0644 -D bitcoin-core.sysusers.conf %{buildroot}%{_sysusersdir}/bitcoin-core.conf

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{project_name}-qt.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{project_name}-qt.metainfo.xml
%ctest
%if %{with extended_tests}
test/functional/test_runner.py --tmpdirprefix `pwd` --extended
%endif

%post server
%systemd_post %{project_name}.service

%preun server
%systemd_preun %{project_name}.service

%postun server
%systemd_postun_with_restart %{project_name}.service

%files
%{_bindir}/%{project_name}
%{_libexecdir}/bitcoin-chainstate
%{_libexecdir}/bitcoin-gui
%{_libexecdir}/bitcoin-node
%{_libexecdir}/test_bitcoin
%{_libexecdir}/test_bitcoin-qt
%{_mandir}/man1/bitcoin.1*

%files -n libbitcoinkernel
%{_libdir}/lib%{project_name}kernel.so.%(echo %{version} | cut -d. -f 1)
%{_libdir}/lib%{project_name}kernel.so.%{version}

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
%{_libdir}/pkgconfig/lib%{project_name}kernel.pc
%{_libdir}/lib%{project_name}kernel.so
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
%{_sysusersdir}/bitcoin-core.conf

%changelog
%autochangelog
