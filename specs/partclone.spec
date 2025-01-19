# Testsuite is CPU and disk space intensive, partially also just broken
%{!?testsuite: %global testsuite 1}

Summary:        Utility to clone and restore a partition
Name:           partclone
Version:        0.3.33
Release:        2%{?dist}
# Partclone itself is GPL-2.0-or-later but uses other source codes, breakdown:
# GPL-3.0-or-later: fail-mbr/fail-mbr.S
# BSD-2-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-3.0-or-later: src/btrfs*
# GPL-2.0-or-later: src/exfat*
# GPL-2.0-only: src/f2fs/
# GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-only: src/xfs*
# GPL-2.0-or-later: src/{apfs,dd,extfs,fat,f2fs,hfsplus,minix,nilfs,ntfsclone-ng,part}clone*
# GPL-2.0-or-later: src/{{fuseimg,info,main,ntfsfixboot,readblock}.c,progress*}
# LGPL-2.0-or-later: src/gettext.h
# Unused source code (= not built): src/{jfs,reiser,ufs,vmfs}*
License:        BSD-2-Clause AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://partclone.org/
Source0:        https://github.com/Thomas-Tsai/partclone/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/Thomas-Tsai/partclone/pull/257.patch#/partclone-0.3.33-byteswap.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libuuid-devel
BuildRequires:  fuse-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel >= 1.1.0
BuildRequires:  e2fsprogs-devel
BuildRequires:  ntfs-3g-devel
BuildRequires:  libblkid-devel
BuildRequires:  libmount-devel
%if 0%{?fedora}
BuildRequires:  nilfs-utils-devel
%endif
# Building fail-mbr.bin requires a compiler that can build x86 binaries
%ifnarch %{ix86} x86_64
BuildRequires:  gcc-x86_64-linux-gnu
%endif
BuildRequires:  pkgconfig(bash-completion)
%if 0%{?testsuite}
BuildRequires:  e2fsprogs
BuildRequires:  ntfsprogs
BuildRequires:  dosfstools
BuildRequires:  xfsprogs
BuildRequires:  exfatprogs
%if 0%{?fedora}
BuildRequires:  btrfs-progs
BuildRequires:  f2fs-tools
BuildRequires:  hfsplus-tools
%endif
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
Recommends:     bash-completion
# Partclone depends on specific source files, either not exposed to -devel package or no -devel package exists
# Version information origin: src/btrfs/libbtrfs/version.h
Provides:       bundled(libbtrfs) = 6.8.1
Provides:       bundled(libbtrfsutil) = 6.8.1
# Version information origin: src/xfs/include/builddefs
Provides:       bundled(xfsprogs-libs) = 4.20.0

%description
Partclone provides utilities to clone and restore used blocks on a partition
and is designed for higher compatibility of the file system by using existing
libraries, e.g. e2fslibs is used to read and write the ext2 partition.

%prep
%autosetup -p1
autoreconf -i -f

# Building fail-mbr.bin requires a compiler that can build x86 binaries
%ifnarch %{ix86} x86_64
sed -e '/^case\s/{N;/.*)/d}' -e '/^\s*;;$/,$d' -e 's/\(gcc\|obj\S\)/x86_64-linux-gnu-\1/g' \
    -i fail-mbr/compile-mbr.sh
%endif

%build
%configure \
  --enable-fuse \
  --enable-extfs \
  --enable-xfs \
  --disable-reiserfs \
  --disable-reiser4 \
  --enable-hfsp \
  --enable-apfs \
  --enable-fat \
  --enable-exfat \
  --enable-f2fs \
%if 0%{?fedora}
  --enable-nilfs2 \
%else
  --disable-nilfs2 \
%endif
  --enable-ntfs \
  --disable-ufs \
  --disable-vmfs \
  --disable-jfs \
  --enable-btrfs \
  --enable-minix \
  --enable-ncursesw \
  --enable-fs-test
%make_build

%install
%make_install
mv -f $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/%{name}{-prompt,}

%find_lang %{name}

%if 0%{?testsuite}
%check
# NILFS2 tests must be run as root (mockbuild is unprivileged)
sed -e 's/^\(am__append_[[:digit:]]* = nilfs2.test\)/#\1/' \
    -i tests/Makefile

# Reiser4 tests require reiser4progs (which are not packaged)
sed -e 's/^\(am__append_[[:digit:]]* = reiser4.test\)/#\1/' \
    -i tests/Makefile

# No btrfs-progs, f2fs-tools and hfsplus-tools in RHEL or EPEL
%if 0%{?rhel}
sed -e 's/^\(am__append_[[:digit:]]* = btrfs.test\)/#\1/' \
    -e 's/^\(am__append_[[:digit:]]* = f2fs.test\)/#\1/' \
    -e 's/^\(am__append_[[:digit:]]* = hfsplus.test\)/#\1/' \
    -i tests/Makefile
%endif

make check || { cat tests/test-suite.log; exit 1; }
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_sbindir}/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man8/%{name}*.8*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 Robert Scheck <robert@fedoraproject.org> 0.3.33-1
- Upgrade to 0.3.33 (#2332011)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Robert Scheck <robert@fedoraproject.org> 0.3.32-1
- Upgrade to 0.3.32 (#2298013)

* Mon Jun 24 2024 Robert Scheck <robert@fedoraproject.org> 0.3.31-1
- Upgrade to 0.3.31 (#2292376 #c1)

* Fri Jun 14 2024 Robert Scheck <robert@fedoraproject.org> 0.3.29-1
- Upgrade to 0.3.29 (#2292376)

* Fri Jun 14 2024 Robert Scheck <robert@fedoraproject.org> 0.3.28-1
- Upgrade to 0.3.28 (#2291472)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 25 2023 Robert Scheck <robert@fedoraproject.org> 0.3.27-2
- Build fail-mbr.bin on all architectures (using cross-compile)

* Wed Oct 04 2023 Robert Scheck <robert@fedoraproject.org> 0.3.27-1
- Upgrade to 0.3.27 (#2242163)

* Mon Sep 25 2023 Robert Scheck <robert@fedoraproject.org> 0.3.26-1
- Upgrade to 0.3.26 (#2240676)

* Mon Aug 07 2023 Robert Scheck <robert@fedoraproject.org> 0.3.25-1
- Upgrade to 0.3.25 (#2229342)

* Sat Jul 22 2023 Robert Scheck <robert@fedoraproject.org> 0.3.24-1
- Upgrade to 0.3.24 (#2224618)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 28 2023 Robert Scheck <robert@fedoraproject.org> 0.3.23-1
- Upgrade to 0.3.23 (#2165166)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Robert Scheck <robert@fedoraproject.org> 0.3.22-1
- Upgrade to 0.3.22 (#2159671)

* Sun Jan 08 2023 Robert Scheck <robert@fedoraproject.org> 0.3.21-1
- Upgrade to 0.3.21 (#2159036)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 29 2022 Robert Scheck <robert@fedoraproject.org> 0.3.20-1
- Upgrade to 0.3.20 (#2079497)

* Fri Mar 18 2022 Robert Scheck <robert@fedoraproject.org> 0.3.19-1
- Upgrade to 0.3.19 (#2065858)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 28 2021 Robert Scheck <robert@fedoraproject.org> 0.3.18-1
- Upgrade to 0.3.18 (#2008368)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.3.17-5
- Rebuilt with OpenSSL 3.0.0

* Thu Sep 02 2021 Robert Scheck <robert@fedoraproject.org> 0.3.17-4
- Rebuilt for ntfs-3g 2021.8.22 (#2000495)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Robert Scheck <robert@fedoraproject.org> 0.3.17-1
- Upgrade to 0.3.17 (#1911716)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Robert Scheck <robert@fedoraproject.org> 0.3.12-4
- Added patch to declare variables as extern in header files

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Robert Scheck <robert@fedoraproject.org> 0.3.12-1
- Upgrade to 0.3.12

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Robert Scheck <robert@fedoraproject.org> 0.3.11-1
- Upgrade to 0.3.11

* Thu Aug 17 2017 Robert Scheck <robert@fedoraproject.org> 0.3.5a-3
- Added licensing breakdown comment based on components (#1404895)

* Wed Aug 16 2017 Robert Scheck <robert@fedoraproject.org> 0.3.5a-2
- Added improvements suggested by Robert-André Mauchin (#1404895)

* Fri Jan 27 2017 Robert Scheck <robert@fedoraproject.org> 0.3.5a-1
- Upgrade to 0.3.5a (#1404895)
- Initial spec file for Fedora and Red Hat Enterprise Linux
