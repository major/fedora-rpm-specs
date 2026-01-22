%global nixbld_group nixbld

# needs mdbook: https://bugzilla.redhat.com/show_bug.cgi?id=2332609
%bcond docs 1
# test failures complain NIX_STORE undefined
# and missing rapidcheck
%bcond tests 0

Name:           nix
# 2.32 needs boost >= 1.87 (https://bugzilla.redhat.com/show_bug.cgi?id=2406036)
# (https://github.com/NixOS/nix/pull/14340)
Version:        2.31.3
Release:        %autorelease
Summary:        A purely functional package manager

License:        LGPL-2.1-or-later
URL:            https://github.com/NixOS/nix
Source0:        https://github.com/NixOS/nix/archive/%{version}/nix-%{version}.tar.gz
Source1:        nix.conf
Source2:        registry.json
Source3:        README.md
Source4:        nix.sysusers
Source5:        nix-filesystem.conf
# soversion patches:
# https://github.com/NixOS/nix/pull/13995
Patch0:         https://patch-diff.githubusercontent.com/raw/NixOS/nix/pull/13995.patch
# https://github.com/NixOS/nix/pull/14001
Patch1:         https://patch-diff.githubusercontent.com/raw/NixOS/nix/pull/14001.patch
# https://github.com/NixOS/nix/pull/14005
Patch2:         https://patch-diff.githubusercontent.com/raw/NixOS/nix/pull/14005.patch
# https://github.com/NixOS/nix/pull/14018
Patch3:         https://patch-diff.githubusercontent.com/raw/NixOS/nix/pull/14018.patch
# disable mdbook
# https://github.com/NixOS/nix/issues/14548
Patch4:         nix-disable-mdbook.patch
# https://github.com/NixOS/nix/pull/14593
Patch5:         https://patch-diff.githubusercontent.com/raw/NixOS/nix/pull/14593.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2425413
# https://github.com/NixOS/nix/pull/14922
Patch6:         https://patch-diff.githubusercontent.com/raw/NixOS/nix/pull/14922.patch

# https://nixos.org/manual/nix/unstable/installation/prerequisites-source
# missing aws-cpp-sdk-s3 aws-c-auth aws-c-s3
#BuildRequires:  aws-c-common
BuildRequires:  bison
BuildRequires:  blake3-devel
BuildRequires:  bzip2-devel
BuildRequires:  boost-devel
BuildRequires:  boost-url
BuildRequires:  brotli-devel
%ifarch x86_64 aarch64 ppc64le
BuildRequires:  busybox
%endif
# needed for toml11
BuildRequires:  cmake
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  rsync
%endif
BuildRequires:  flex
BuildRequires:  gc-devel
BuildRequires:  gcc-c++
%if %{with tests}
BuildRequires:  gmock-devel
%endif
BuildRequires:  libgit2-devel
BuildRequires:  jq
BuildRequires:  json-devel
BuildRequires:  libarchive-devel
%if %{defined fedora}
%ifarch x86_64
BuildRequires:  libcpuid-devel
%endif
%endif
BuildRequires:  libcurl-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libsodium-devel
BuildRequires:  lowdown
BuildRequires:  lowdown-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
%if %{with tests}
#BuildRequires:  rapidcheck-devel
%endif
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  toml11-devel
BuildRequires:  xz-devel
Requires:       nix-core = %{version}-%{release}
Requires:       nix-system = %{version}-%{release}
Recommends:     (nix-daemon = %{version}-%{release} if systemd)
Recommends:     nix-legacy = %{version}-%{release}

%description
Nix is a purely functional package manager.
It allows multiple versions of a package to be installed side-by-side,
ensures that dependency specifications are complete,
supports atomic upgrades and rollbacks,
allows non-root users to install software, and has many other features.
It is the basis of the NixOS Linux distribution,
but it can be used equally well under other Unix systems.

See the README.fedora.md file for setup instructions.


%package        core
Summary:        Core nix tool
Requires:       nix-libs%{?_isa} = %{version}-%{release}
%ifarch x86_64 aarch64 ppc64le
Recommends:     busybox
%endif

%description    core
This package provides the core nix tool for modern flake-based commands.

Most users should probably install nix-legacy as well,
or the main nix package for a complete default setup.

See the README.fedora.md file for setup instructions.


%package daemon
Summary:        The nix daemon for multiuser mode
BuildArch:      noarch
Requires:       nix-core = %{version}-%{release}
Requires:       nix-system = %{version}-%{release}
Requires:       systemd

%description daemon
This package provides nix-daemon and associated files.


%package devel
Summary:        Development files for nix
Requires:       nix-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains library and header files for
developing applications that use nix.

Note the API is considered unstable and upstream does not recommend its usage.


%if %{with docs}
%package doc
Summary:        Documentation files for nix
BuildArch:      noarch

%description doc
This package contains documentation files for nix.
%endif


%package        filesystem
Summary:        Filesystem for nix
BuildArch:      noarch
# added at f43
Obsoletes:      nix-singleuser < %{version}-%{release}

%description    filesystem
The package provides the /nix root directory for the nix package manager.


%package        legacy
Summary:        Nix classical commands
BuildArch:      noarch
Requires:       nix-core = %{version}-%{release}

%description    legacy
This package provides the symlinks for the older nix-* commands.


%package libs
Summary:        Runtime libraries for nix

%description libs
The package provides the the runtime libraries for nix.


%if %{with tests}
%package test
Summary:        Nix test programs
Requires:       nix%{?_isa} = %{version}-%{release}

%description test
This package provides the nix-test programs.
%endif


%package        system
Summary:        Nix directories and sysusers setup
BuildArch:      noarch
Requires:       nix-filesystem = %{version}-%{release}

%description    system
This package sets up the nix directories and sysusers.


%prep
%autosetup -p1

install -p -m 0644 %{SOURCE3} README.fedora.md

# https://github.com/NixOS/nix/issues/14666
# remove unicode RLO (0x202E) characters
sed -i 's/\xe2\x80\xae//g' doc/manual/source/release-notes/rl-2.26.md


%build
MESON_OPTS=(
    --sysconfdir=%{_sysconfdir}
    --localstatedir=/nix/var
    --libexecdir=%{_libexecdir}
    -Dbindings=false
    -Ddoc-gen=%[%{with docs}?"true":"false"]
    -Dlibcmd:readline-flavor=readline
    -Dlibstore:sandbox-shell=%{_bindir}/busybox
    -Dnix:profile-dir=%{_sysconfdir}/profile.d
    -Dunit-tests=%[%{with tests}?"true":"false"]
%ifarch x86_64
# missing from epel10: https://bugzilla.redhat.com/show_bug.cgi?id=2368495
%if %{undefined fedora}
    -Dlibutil:cpuid=disabled
%endif
%else
    -Dlibutil:cpuid=disabled
%endif
    )

%meson "${MESON_OPTS[@]}"
%meson_build


%install
%meson_install

# nix config
mkdir -p %{buildroot}/etc/nix
cp %{SOURCE1} %{SOURCE2} %{buildroot}/etc/nix/

# Nix has multiuser and singleuser installation modes
# https://nix.dev/manual/nix/stable/installation/nix-security.html

mkdir -p %{buildroot}/nix/store
mkdir -p %{buildroot}/nix/var/log/nix/drvs
mkdir -p %{buildroot}/nix/var/nix

install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/nix.conf
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/nix-filesystem.conf

# filter out relative doc links
# https://bugzilla.redhat.com/show_bug.cgi?id=2415126
# https://github.com/kristapsdz/lowdown/issues/170
# (sed expression generated by Gemini Pro: removes pairs of .UR and .UE lines)
sed -i -e '/^\.UR [@#.]/,/^\.UE/{ /^\.UR [@#.]/d; /^\.UE/d}' %{buildroot}%{_mandir}/man*/*


%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{buildroot}%{_bindir}/nix --help
%if %{with tests}
#export TEST_ROOT=$HOME/tmp/nix-test
%meson_test
%endif


%post daemon
%systemd_post nix-daemon.service

%preun daemon
%systemd_preun nix-daemon.service

%postun daemon
%systemd_postun_with_restart nix-daemon.service


%files


%files core
%doc README.md README.fedora.md
%{_bindir}/nix
%{_libexecdir}/nix
%config(noreplace) %{_sysconfdir}/nix/nix.conf
%config(noreplace) %{_sysconfdir}/nix/registry.json
%config(noreplace) %{_sysconfdir}/profile.d/nix.sh
%config(noreplace) %{_sysconfdir}/profile.d/nix.fish
%{bash_completions_dir}/nix
%{fish_completions_dir}/nix.fish
%{zsh_completions_dir}/_nix
%{zsh_completions_dir}/run-help-nix
%if %{with docs}
%{_mandir}/man1/nix.1*
%{_mandir}/man1/nix3-*.1*
%{_mandir}/man5/nix.conf.5*
%{_mandir}/man5/nix-profiles.5*
%endif


%files daemon
%{_bindir}/nix-daemon
%{_sysconfdir}/profile.d/nix-daemon.sh
%{_sysconfdir}/profile.d/nix-daemon.fish
%{_unitdir}/nix-daemon.service
%{_unitdir}/nix-daemon.socket
%{_tmpfilesdir}/nix-daemon.conf
%ghost %dir /nix/var/nix/builds
%ghost %dir /nix/var/nix/daemon-socket
%ghost /nix/var/nix/daemon-socket/socket
%if %{with docs}
%{_mandir}/man8/nix-daemon.8*
%endif


%files devel
%{_includedir}/nix
%{_includedir}/nix_api_*.h
%{_includedir}/nix_api_*.hh
%{_libdir}/libnixcmd.so
%{_libdir}/libnixexpr.so
%{_libdir}/libnixexprc.so
%{_libdir}/libnixfetchers.so
%{_libdir}/libnixfetchersc.so
%{_libdir}/libnixflake.so
%{_libdir}/libnixflakec.so
%{_libdir}/libnixmain.so
%{_libdir}/libnixmainc.so
%{_libdir}/libnixstore.so
%{_libdir}/libnixstorec.so
%{_libdir}/libnixutil.so
%{_libdir}/libnixutilc.so
%{_libdir}/pkgconfig/*.pc


%if %{with docs}
%files doc
%{_defaultdocdir}/nix
%endif


%files filesystem
# FHS Exception: https://pagure.io/fesco/issue/3473
%{_tmpfilesdir}/nix-filesystem.conf
%ghost %dir /nix
%ghost %dir /nix/var
%ghost %dir /nix/var/log
%ghost %dir /nix/var/log/nix


%files legacy
%{_bindir}/nix-build
%{_bindir}/nix-channel
%{_bindir}/nix-collect-garbage
%{_bindir}/nix-copy-closure
%{_bindir}/nix-env
%{_bindir}/nix-hash
%{_bindir}/nix-instantiate
%{_bindir}/nix-prefetch-url
%{_bindir}/nix-shell
%{_bindir}/nix-store
%if %{with docs}
%{_mandir}/man1/nix-*.1*
%endif


%files libs
%license COPYING
%{_libdir}/libnixcmd.so.%{version}
%{_libdir}/libnixexpr.so.%{version}
%{_libdir}/libnixexprc.so.%{version}
%{_libdir}/libnixfetchers.so.%{version}
%{_libdir}/libnixfetchersc.so.%{version}
%{_libdir}/libnixflake.so.%{version}
%{_libdir}/libnixflakec.so.%{version}
%{_libdir}/libnixmain.so.%{version}
%{_libdir}/libnixmainc.so.%{version}
%{_libdir}/libnixstore.so.%{version}
%{_libdir}/libnixstorec.so.%{version}
%{_libdir}/libnixutil.so.%{version}
%{_libdir}/libnixutilc.so.%{version}


%files system
%{_sysusersdir}/nix.conf
%dir %attr(1775,root,%{nixbld_group}) /nix/store
%dir %attr(775,root,%{nixbld_group}) /nix/var/log/nix/drvs
%dir %attr(775,root,%{nixbld_group}) /nix/var/nix
%ghost %dir /nix/var/nix/db
%ghost /nix/var/nix/gc.lock
%ghost %dir /nix/var/nix/gcroots
%ghost %dir /nix/var/nix/gcroots/per-user
%ghost %dir /nix/var/nix/gc-socket
%ghost /nix/var/nix/gc-socket/socket
%ghost %dir /nix/var/nix/profiles
%ghost %dir /nix/var/nix/profiles/per-user
%ghost %dir /nix/var/nix/temproots


%if %{with tests}
%files test
%{_bindir}/nix*-test
%endif


%changelog
%autochangelog
