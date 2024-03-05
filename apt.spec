# Force out of source build
%undefine __cmake_in_source_build

%{!?jobs:%global jobs %(/usr/bin/getconf _NPROCESSORS_ONLN)}

# apt library somajor...
%global libsomajor 6.0
%global libprivsomajor 0.0

# Disable integration tests by default,
# as there is a bunch of failures on non-Debian systems currently.
# Additionally, these tests take a long time to run.
%bcond_with check_integration

Name:           apt
Version:        2.7.12
Release:        1%{?dist}
Summary:        Command-line package manager for Debian packages

License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/apt
Source0:        https://salsa.debian.org/apt-team/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:         apt_include_cstdint.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.4
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(gnutls) >= 3.4.6
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxxhash)

# Package manager BRs
BuildRequires:  dpkg-dev

# These BRs lack pkgconfig() names
BuildRequires:  libdb-devel
BuildRequires:  gtest-devel
BuildRequires:  bzip2-devel

# Misc BRs
BuildRequires:  triehash
BuildRequires:  po4a >= 0.35
BuildRequires:  docbook-style-xsl, docbook-dtds
BuildRequires:  gettext >= 0.19
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  w3m
BuildRequires:  %{_bindir}/xsltproc

%if %{with check_integration}
BuildRequires:  coreutils, moreutils,
BuildRequires:  moreutils-parallel
BuildRequires:  fakeroot, lsof, sed
BuildRequires:  tar, wget, stunnel
BuildRequires:  gnupg, gnupg2
BuildRequires:  perl(File::FcntlLock)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  debhelper >= 9
# Unbreak running tests in non-interactive terminals
BuildRequires:  expect
%endif

# For ensuring the user is created
Requires(pre):  shadow-utils

# Apt is essentially broken without dpkg
Requires:       dpkg >= 1.17.14

# To ensure matching apt libs are installed
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# apt-transport-curl-https is gone...
Provides:       %{name}-transport-https = %{version}-%{release}
Provides:       %{name}-transport-curl-https = %{version}-%{release}

%description
This package provides commandline tools for searching and
managing as well as querying information about packages
as a low-level access to all features of the libapt-pkg library.

These include:
  * apt-get for retrieval of packages and information about them
    from authenticated sources and for installation, upgrade and
    removal of packages together with their dependencies
  * apt-cache for querying available information about installed
    as well as installable packages
  * apt-cdrom to use removable media as a source for packages
  * apt-config as an interface to the configuration settings
  * apt-key as an interface to manage authentication keys

%package libs
Summary:        Runtime libraries for %{name}

%description libs
This package includes the libapt-pkg library.

libapt-pkg provides the common functionality for searching and
managing packages as well as information about packages.
Higher-level package managers can depend upon this library.

This includes:
  * retrieval of information about packages from multiple sources
  * retrieval of packages and all dependent packages
    needed to satisfy a request either through an internal
    solver or by interfacing with an external one
  * authenticating the sources and validating the retrieved data
  * installation and removal of packages in the system
  * providing different transports to retrieve data over cdrom, ftp,
    http, rsh as well as an interface to add more transports like
    debtorrent (apt-transport-debtorrent).

%package doc
Summary:        Documentation for APT
BuildArch:      noarch

%description doc
This package contains the user guide and offline guide for various
APT tools which are provided in a html and a text-only version.

%package devel
Summary:        Development files for APT's libraries
Provides:       libapt-pkg-devel%{?_isa} = %{version}-%{release}
Provides:       libapt-pkg-devel = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries for
developing with APT's libapt-pkg Debian package manipulation
library.

%package apidoc
Summary:        Documentation for developing against APT libraries
Provides:       libapt-pkg-doc = %{version}-%{release}
Obsoletes:      %{name}-devel-doc < 1.9.7-1
Provides:       %{name}-devel-doc = %{version}-%{release}
BuildArch:      noarch

%description apidoc
This package contains documentation for development of the APT
Debian package manipulation program and its libraries.

This includes the source code documentation generated by doxygen
in html format.

%package utils
Summary:        Package management related utility programs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains some less used commandline utilities related
to package management with APT.

  * apt-extracttemplates is used by debconf to prompt for configuration
    questions before installation.
  * apt-ftparchive is used to create Packages and other index files
    needed to publish an archive of Debian packages
  * apt-sortpkgs is a Packages/Sources file normalizer.

%prep
%autosetup -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%find_lang %{name}
%find_lang %{name}-utils
%find_lang libapt-pkg%{libsomajor}

cat libapt*.lang >> %{name}-libs.lang

mkdir -p %{buildroot}%{_localstatedir}/log/apt
touch %{buildroot}%{_localstatedir}/log/apt/{term,history}.log
mkdir -p %{buildroot}%{_sysconfdir}/apt/{apt.conf,preferences,sources.list,trusted.gpg}.d
install -pm 644 doc/examples/apt.conf %{buildroot}%{_sysconfdir}/apt/
touch %{buildroot}%{_sysconfdir}/apt/sources.list
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/apt <<EOF
%{_localstatedir}/log/apt/term.log {
  rotate 12
  monthly
  compress
  missingok
  notifempty
}
%{_localstatedir}/log/apt/history.log {
  rotate 12
  monthly
  compress
  missingok
  notifempty
}
EOF


%check
%ctest
%if %{with check_integration}
unbuffer ./test/integration/run-tests -q %{?jobs:-j %{jobs}}
%endif

# Create the _apt user+group for apt data
%pre
getent group _apt >/dev/null || groupadd -r _apt
getent passwd _apt >/dev/null || \
    useradd -r -g _apt -d %{_sharedstatedir}/apt -s /sbin/nologin \
    -c "APT account for owning persistent & cache data" _apt
exit 0

%ldconfig_scriptlets libs

%files -f %{name}.lang
%license COPYING*
%doc README.* AUTHORS
%{_bindir}/apt
%{_bindir}/apt-cache
%{_bindir}/apt-cdrom
%{_bindir}/apt-config
%{_bindir}/apt-get
%{_bindir}/apt-key
%{_bindir}/apt-mark
%dir %{_libexecdir}/apt
%{_libexecdir}/apt/apt-helper
%{_libexecdir}/apt/methods
%{_libexecdir}/dpkg/methods/apt
%attr(-,_apt,_apt) %{_sharedstatedir}/apt
%attr(-,_apt,_apt) %{_localstatedir}/cache/apt
%dir %attr(-,_apt,_apt) %{_localstatedir}/log/apt
%ghost %{_localstatedir}/log/apt/history.log
%ghost %{_localstatedir}/log/apt/term.log
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/apt.conf.d
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/preferences.d
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/sources.list.d
%dir %attr(-,_apt,_apt) %{_sysconfdir}/apt/trusted.gpg.d
%config(noreplace) %attr(-,_apt,_apt) %{_sysconfdir}/apt/apt.conf
%ghost %{_sysconfdir}/apt/sources.list
%config(noreplace) %{_sysconfdir}/logrotate.d/apt
%{_datadir}/bash-completion/completions/apt
%{_mandir}/*/*/apt.*
%{_mandir}/*/*/apt-cache.*
%{_mandir}/*/*/apt-cdrom.*
%{_mandir}/*/*/apt-config.*
%{_mandir}/*/*/apt-get.*
%{_mandir}/*/*/apt-key.*
%{_mandir}/*/*/apt-mark.*
%{_mandir}/*/*/apt-patterns.*
%{_mandir}/*/*/apt-secure.*
%{_mandir}/*/*/apt-transport-http.*
%{_mandir}/*/*/apt-transport-https.*
%{_mandir}/*/*/apt-transport-mirror.*
%{_mandir}/*/*/apt_auth.*
%{_mandir}/*/*/apt_preferences.*
%{_mandir}/*/*/sources.list.*
%{_mandir}/*/apt.*
%{_mandir}/*/apt-cache.*
%{_mandir}/*/apt-cdrom.*
%{_mandir}/*/apt-config.*
%{_mandir}/*/apt-get.*
%{_mandir}/*/apt-key.*
%{_mandir}/*/apt-mark.*
%{_mandir}/*/apt-patterns.*
%{_mandir}/*/apt-secure.*
%{_mandir}/*/apt-transport-http.*
%{_mandir}/*/apt-transport-https.*
%{_mandir}/*/apt-transport-mirror.*
%{_mandir}/*/apt_auth.*
%{_mandir}/*/apt_preferences.*
%{_mandir}/*/sources.list.*
%doc %{_docdir}/%{name}/*

%files libs -f %{name}-libs.lang
%license COPYING*
%{_libdir}/libapt-pkg.so.%{libsomajor}{,.*}
%{_libdir}/libapt-private.so.%{libprivsomajor}{,.*}

%files doc
%doc %{_docdir}/%{name}-doc

%files apidoc
%doc %{_docdir}/libapt-pkg-doc

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files utils -f %{name}-utils.lang
%{_bindir}/apt-extracttemplates
%{_bindir}/apt-ftparchive
%{_bindir}/apt-sortpkgs
%{_libexecdir}/apt/planners
%{_libexecdir}/apt/solvers
%{_mandir}/*/*/apt-extracttemplates.*
%{_mandir}/*/*/apt-ftparchive.*
%{_mandir}/*/*/apt-sortpkgs.*
%{_mandir}/*/apt-extracttemplates.*
%{_mandir}/*/apt-ftparchive.*
%{_mandir}/*/apt-sortpkgs.*
%doc %{_docdir}/%{name}-utils

%changelog
* Tue Feb 20 2024 Packit <hello@packit.dev> - 2.7.12-1
- Release 2.7.12 (Julian Andres Klode)
- Release 2.7.12 (Julian Andres Klode)
- Move systemd units to /usr/lib (Julian Andres Klode)
- test-snapshot: Add test case for automatic snapshot (Julian Andres Klode)
- test-snapshot: Fix a test case (Julian Andres Klode)
- Delete SHADOWED metaIndex if we don't actually use snapshots (Julian Andres Klode)
- Automatically enable snapshots where supported (Julian Andres Klode)
- Modernize standard library includes (Julian Andres Klode)
- Bump Ubuntu apt-key deprecation notice to 24.04 (Julian Andres Klode)
- Release 2.7.11 (Julian Andres Klode)
- Show a separate list of upgrades deferred due to phasing (Julian Andres Klode)
- Add the ?security pattern (Julian Andres Klode)
- Add a new ?phasing pattern (Julian Andres Klode)
- Add public phased update API (Julian Andres Klode)
- For phasing, check if current version is a security update, not just previous ones (Julian Andres Klode)
- Add documentation of autoremove to apt.conf (5) (Wesley Schwengle)
- Fix bug where ./git-clang-format.sh errors incorrectly (Wesley Schwengle)
- Configure the amount of kernels to keep (Wesley Schwengle)
- Support -a for setting host architecture in apt-get source -b (David Kalnischkies)
- Remove erroneous -a flag from apt-get synopsis in manpage (David Kalnischkies)
- Release 2.7.10 (Julian Andres Klode)
- Add Conflicts: apt-verify (Julian Andres Klode)
- pkgcachegen: Use placement new to construct header (Julian Andres Klode)
- Release 2.7.9 (Julian Andres Klode)
- Document 'dist-clean' (Gábor Németh)
- CI: Pull from testing, unstable broken atm (Julian Andres Klode)
- Accept file system disorder in test-ignored-files (David Kalnischkies)
- Typos in integration tests (Gábor Németh)
- Release 2.7.8 (Julian Andres Klode)
- Revert "Merge branch 'distclean-doc-an-test' into 'main'" (Julian Andres Klode)
- test: Disable valgrind on armhf, incompatible with stack clash protector (Julian Andres Klode)
- Do not store .diff_Index files in update (David Kalnischkies)
- Improve and test distclean implementation (David Kalnischkies)
- Prevent infinite loop in `ReadConfigFile` (Adam Saponara)
- apt.8: summarise remaining verbs (Closes: #827785) (наб)
- Test and document 'dist-clean' (Gábor Németh)
- Add 'dist-clean' to 'apt-get' too (Gábor Németh)
- Do not silently ignore directories for reserved file names (Julian Andres Klode)
- apt-pkg/cacheset.cc: set ShowErrors to true when no version matched (Tianyu Chen)
- Have Grp.FindPreferredPkg return very foreign pkgs as last resort (David Kalnischkies)
- apt-key: remove carriage returns from armored keyrings before dearmoring (Kenyon Ralph)
- Release 2.7.7 (Julian Andres Klode)
- Fix the test suite by adding new "m" flags to debug output (Julian Andres Klode)
- Add 'dist-clean' command to remove packages and list files (Gábor Németh)
- Restore ?garbage by calling MarkAndSweep before parsing (Julian Andres Klode)
- Use different variable name in GTest source path detection (David Kalnischkies)
- Raise cmake_minimum_required to 3.13 to avoid warnings (David Kalnischkies)
- Dutch program translation update (Frans Spiesschaert)
- Bump Priority to required to match Debian archive (Julian Andres Klode)
- s/AlreadDownloaded/AlreadyDownloaded/ in doc/progress-reporting.md (Julian Andres Klode)
- Revert "Do not fail on systems running in FIPSmode." (Julian Andres Klode)
- Stop calculating Description-md5 if missing (Julian Andres Klode)
- Release 2.7.6 (Julian Andres Klode)
- Downgrade unmerged-usr from error to two warnings (Julian Andres Klode)
- Portuguese manpages translation update (Américo Monteiro)
- Release 2.7.5 (Julian Andres Klode)
- doc/po/nl.po: Fix spurious translation of docbook tag (Julian Andres Klode)
- Release 2.7.4 (Julian Andres Klode)
- updated German translation (Helge Kreutzmann)
- Dutch documentation translation update (Frans Spiesschaert)
- Dutch translation update (Frans Spiesschaert)
- Remove unnecessary explicit st_dev check for merged-usr (Julian Andres Klode)
- Drop alternatives to the gpgv dependency (Julian Andres Klode)
- Only accept installs of usrmerge on unmerged-usr systems (Julian Andres Klode)
- methods: store: Use APT_BUFFER_SIZE (64k) instead of 4k buffers (Julian Andres Klode)
- Update fr.po (add a missing dot) (Patrice Duroux)
- CI: Do not require UID 1000 for our test user (Julian Andres Klode)
- Fix incorrect time unit comment for PulseInterval (sid)
- Resolves rhbz#2257250

* Tue Feb 13 2024 Sérgio M. Basto <sergio@serjux.com> - 2.7.11-1
- Release 2.7.11 (Julian Andres Klode)
- Show a separate list of upgrades deferred due to phasing (Julian Andres Klode)
- Add the ?security pattern (Julian Andres Klode)
- Add a new ?phasing pattern (Julian Andres Klode)
- Add public phased update API (Julian Andres Klode)
- For phasing, check if current version is a security update, not just previous ones (Julian Andres Klode)
- Support -a for setting host architecture in apt-get source -b (David Kalnischkies)
- Remove erroneous -a flag from apt-get synopsis in manpage (David Kalnischkies)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.7.6-1
- Update to 2.7.6 (#2239816)

* Sat Sep 16 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.7.5-1
- Update to 2.7.5 (#2222361)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 24 2023 Sérgio Basto <sergio@serjux.com> - 2.7.1-2
- Migrate to SPDX license format

* Mon Jun 12 2023 Mosaab Alzoubi <moceap[At]fedoraproject[Dot]org> - 2.7.1-1
- Update to 2.7.1

* Thu Feb 23 2023 Sérgio Basto <sergio@serjux.com> - 2.5.6-1
- Update apt to 2.5.6 (#2168285)

* Wed Jan 25 2023 Sérgio Basto <sergio@serjux.com> - 2.5.5-1
- Update apt to 2.5.5 (#2161700)
- Fix build with gcc13

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Sérgio Basto <sergio@serjux.com> - 2.5.4-1
- Update apt to 2.5.4 (#2138830)

* Mon Oct 03 2022 Sérgio Basto <sergio@serjux.com> - 2.5.3-1
- Update apt to 2.5.3 (#2130611)

* Fri Aug 05 2022 Sérgio Basto <sergio@serjux.com> - 2.5.2-1
- Update apt to 2.5.2 (#2087682)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Sérgio Basto <sergio@serjux.com> - 2.4.5-1
- Update apt to 2.4.5 (#2049183)

* Sat Feb 12 2022 Jeff Law <jeffreyalaw@gmail.com> - 2.3.14-3
- Re-enable LTO

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Sérgio Basto <sergio@serjux.com> - 2.3.14-1
- Update apt to 2.3.14 (#2037920)

* Sat Dec 18 2021 Sérgio Basto <sergio@serjux.com> - 2.3.13-1
- Update apt to 2.3.13 (#2024297)

* Thu Oct 21 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.3.11-1
- Update to 2.3.11 (#2002944)

* Sat Aug 14 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.3.8-1
- Update to 2.3.8 (#1993644)

* Thu Jul 29 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.3.7-1
- Update to 2.3.7 (#1987763)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 09 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.3.6-1
- Update to 2.3.6 (#1969935)

* Mon May 17 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.3.5-1
- Update to 2.3.5 (#1930430)

* Mon Feb 15 2021 Mosaab Alzoubi <moceap[At]hotmail[Dot]com> - 2.1.20-1
- Update to 2.1.20

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.18-1
- Update to 2.1.18 (#1906457)

* Mon Nov 23 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.12-1
- Update to 2.1.12 (#1900787)

* Wed Oct 21 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.11-1
- Update to 2.1.11 (#1890077)

* Tue Aug 11 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.10-1
- Update to 2.1.10 (#1868031)

* Mon Aug 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.9-1
- Update to 2.1.9 (#1867591)

* Tue Aug 04 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8 (#1865853)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Jeff law <law@redhat.com> - 2.1.7-3
- Disable LTO for now

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Sérgio Basto <sergio@serjux.com> - 2.1.7-1
- Update apt to 2.1.7 (#1854759)

* Wed Jun 03 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6 (#1831062)

* Tue May 26 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.5-1
- Update to 2.1.5 (#1831062)

* Tue May 19 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (#1831062)

* Thu Apr 09 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 (#1816610)

* Sat Mar 07 17:26:29 EST 2020 Neal Gompa <ngompa13@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Tue Feb 18 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.9.10-1
- Update to 1.9.10 (#1804170)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 09:50:33 EST 2020 Neal Gompa <ngompa13@gmail.com> - 1.9.7-1
- Update to 1.9.7
- Rename apt-devel-doc to apt-apidoc to better reflect the content

* Mon Dec 16 22:10:42 EST 2019 Neal Gompa <ngompa13@gmail.com> - 1.9.4-1
- Switch from apt-rpm to apt from Debian and rebase to v1.9.4
  + This drops rpm support from apt
- Truncate changelog due to complete spec rewrite and replacement of apt implementation
