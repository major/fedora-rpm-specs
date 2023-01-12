# Testsuite is CPU and disk space intensive, partially also just broken
%{!?testsuite: %global testsuite 1}

Summary:        Utility to clone and restore a partition
Name:           partclone
Version:        0.3.22
Release:        1%{?dist}
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
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libuuid-devel
BuildRequires:  fuse-devel
BuildRequires:  ncurses-devel
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  openssl-devel >= 1.1.0
%else
BuildRequires:  openssl11-devel
# APFS support requires modern GCC
BuildRequires:  devtoolset-8-toolchain
%endif
BuildRequires:  e2fsprogs-devel
BuildRequires:  ntfs-3g-devel
BuildRequires:  libblkid-devel
BuildRequires:  libmount-devel
%if 0%{?fedora}
BuildRequires:  nilfs-utils-devel
%endif
%if 0%{?testsuite}
BuildRequires:  e2fsprogs
BuildRequires:  ntfsprogs
BuildRequires:  dosfstools
BuildRequires:  xfsprogs
BuildRequires:  exfatprogs
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} < 8)
# RHEL 8+ (including EPEL 8+) doesn't provide any btrfs-progs RPM at all
BuildRequires:  btrfs-progs
%endif
%if 0%{?fedora}
BuildRequires:  f2fs-tools
BuildRequires:  hfsplus-tools
%endif
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel

%description
Partclone provides utilities to clone and restore used blocks on a partition
and is designed for higher compatibility of the file system by using existing
libraries, e.g. e2fslibs is used to read and write the ext2 partition.

%prep
%setup -q
autoreconf -i -f

%build
# src/progress.c:50: undefined reference to `__fpclassifyf',
# reported: https://github.com/Thomas-Tsai/partclone/issues/153
%if 0%{?rhel} && 0%{?rhel} < 8
. /opt/rh/devtoolset-8/enable
export CFLAGS="$RPM_OPT_FLAGS $(pkg-config --cflags-only-I openssl11)"
export LDFLAGS="$RPM_LD_FLAGS $(pkg-config --libs-only-L openssl11)-lm"
%endif

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

# Building fail-mbr.bin requires a compiler that can build x86 binaries
%ifnarch %{ix86} x86_64
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/
%endif

%find_lang %{name}

%if 0%{?testsuite}
%check
# NILFS2 tests must be run as root (mockbuild is unprivileged)
sed -e 's/^\(am__append_[[:digit:]]* = nilfs2.test\)/#\1/' \
    -i tests/Makefile

# No btrfs-progs, f2fs-tools and hfsplus-tools in RHEL or EPEL
%if 0%{?rhel}
sed -e 's/^\(am__append_[[:digit:]]* = btrfs.test\)/#\1/' \
    -e 's/^\(am__append_[[:digit:]]* = f2fs.test\)/#\1/' \
    -e 's/^\(am__append_[[:digit:]]* = hfsplus.test\)/#\1/' \
    -i tests/Makefile
%endif

make check || (cat tests/test-suite.log; exit 1)
%endif

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog
%{_sbindir}/%{name}.*
%ifarch %{ix86} x86_64
%{_datadir}/%{name}/
%endif
%{_mandir}/man8/%{name}*.8*

%changelog
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
