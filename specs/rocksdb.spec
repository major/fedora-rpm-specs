%bcond_without compression

%global forgeurl https://github.com/facebook/rocksdb

Name:    rocksdb
Version: 9.3.1
Release: 4%{?dist}
Summary: A Persistent Key-Value Store for Flash and RAM Storage

# Automatically converted from old format: GPLv2 or ASL 2.0 and BSD - review is highly recommended.
License: GPL-2.0-only OR Apache-2.0 AND LicenseRef-Callaway-BSD
URL:     %{forgeurl}

# https://git.alpinelinux.org/aports/tree/community/rocksdb/11-shared-liburing.patch
Patch1: shared-liburing.patch

# Do not build tools with rpath These will be installed semi-manual to usr/bin
# and will use system libraries.
Patch2: https://sources.debian.org/data/main/r/rocksdb/7.6.0-2/debian/patches/no_rpath.patch

Patch3: disable-static.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gflags-devel
BuildRequires: liburing-devel

%if %{with compression}
BuildRequires: bzip2-devel
BuildRequires: lz4-devel
BuildRequires: snappy-devel
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
%endif

BuildRequires: /usr/bin/perl
BuildRequires: python3-devel

%forgemeta
Source: %{forgesource}


%description
RocksDB is a library that forms the core building block for a fast key value
server, especially suited for storing data on flash drives. It has a
Log-Structured-Merge-Database (LSM) design with flexible trade offs between
Write-Amplification-Factor (WAF), Read-Amplification-Factor (RAF) and
Space-Amplification-Factor (SAF). It has multi-threaded compaction, making it
specially suitable for storing multiple terabytes of data in a single database.

%package tools
Summary: Utility tools for RocksDB
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Utility tools for RocksDB.

%package devel
Summary: Development files for RocksDB
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for RocksDB.


%prep
%forgesetup
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%build
%cmake \
%if %{with compression}
  -DWITH_BZ2=ON \
  -DWITH_SNAPPY=ON \
  -DWITH_LZ4=ON \
  -DWITH_ZSTD=ON \
  -DWITH_ZLIB=ON \
%endif
  -DZSTD_INCLUDE_DIRS=%{_includedir} \
  -DROCKSDB_BUILD_SHARED=ON \
  -DWITH_BENCHMARK_TOOLS=ON \
  -DWITH_CORE_TOOLS=ON \
  -DWITH_TOOLS=ON \
  -DUSE_RTTI=ON \
  -DPORTABLE=1 \
  -DFAIL_ON_WARNINGS=OFF \
  -DWITH_TESTS=ON

%cmake_build


%install
%cmake_install

# Missing steps in build script
install -dD -m 755 %{buildroot}%{_bindir}
install -m 755 %{__cmake_builddir}/cache_bench %{buildroot}%{_bindir}/cache_bench
install -m 755 %{__cmake_builddir}/db_bench %{buildroot}%{_bindir}/db_bench
install -m 755 %{__cmake_builddir}/tools/ldb %{buildroot}%{_bindir}/ldb
install -m 755 %{__cmake_builddir}/tools/sst_dump %{buildroot}%{_bindir}/sst_dump


%files
%doc README.md
%doc HISTORY.md
%doc AUTHORS
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so.9
%{_libdir}/librocksdb.so.9.3.1


%files tools
%doc README.md
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_bindir}/cache_bench
%{_bindir}/db_bench
%{_bindir}/ldb
%{_bindir}/sst_dump


%files devel
%doc README.md
%doc LANGUAGE-BINDINGS.md
%license COPYING
%license LICENSE.Apache
%license LICENSE.leveldb
%{_libdir}/librocksdb.so
%{_libdir}/cmake/rocksdb
%{_libdir}/pkgconfig/rocksdb.pc
%{_includedir}/rocksdb


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 9.3.1-3
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Jonny Heggheim <hegjon@gmail.com> - 9.3.1-1
- Updated to version 9.3.1

* Wed Mar 20 2024 Jonny Heggheim <hegjon@gmail.com> - 9.0.0-1
- Updated to version 9.0.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Jonny Heggheim <hegjon@gmail.com> - 8.10.0-1
- Updated to version 8.10.0

* Fri Aug 11 2023 Jonny Heggheim <hegjon@gmail.com> - 8.3.2-1
- Updated to version 8.3.2

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 22 2023 Jonny Heggheim <hegjon@gmail.com> - 8.1.1-1
- Updated to version 8.1.1

* Wed Apr 19 2023 Jonny Heggheim <hegjon@gmail.com> - 8.0.0-1
- Updated to version 8.0.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Jonny Heggheim <hegjon@gmail.com> - 7.8.3-1
- Updated to version 7.8.3

* Fri Oct 14 2022 Jonny Heggheim <hegjon@gmail.com> - 7.7.3-1
- Updated to version 7.7.3

* Sat Oct 08 2022 Jonny Heggheim <hegjon@gmail.com> - 7.7.2-1
- Updated to version 7.7.2

* Sun Oct 02 2022 Jonny Heggheim <hegjon@gmail.com> - 7.6.0-1
- Updated to version 7.6.0

* Thu Aug 11 2022 Jonny Heggheim <hegjon@gmail.com> - 7.4.5-3
- Added tools sub-package

* Fri Aug 05 2022 Jonny Heggheim <hegjon@gmail.com> - 7.4.5-2
- Use liburing

* Thu Aug 04 2022 Jonny Heggheim <hegjon@gmail.com> - 7.4.5-1
- Updated to version 7.4.5

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022 Jonny Heggheim <hegjon@gmail.com> - 7.2.2-3
- Re-enabled armhfp

* Sat May 21 2022 Jonny Heggheim <hegjon@gmail.com> - 7.2.2-2
- Re-enabled x86

* Wed May 18 2022 Jonny Heggheim <hegjon@gmail.com> - 7.2.2-1
- Updated to version 7.2.2

* Sat Apr 30 2022 Jonny Heggheim <hegjon@gmail.com> - 7.1.2-1
- Updated to version 7.1.2

* Thu Feb 24 2022 Jonny Heggheim <hegjon@gmail.com> - 6.29.3-1
- Updated to version 6.29.3

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Jonny Heggheim <hegjon@gmail.com> - 6.26.1-1
- Updated to version 6.26.1

* Thu Oct 14 2021 Jonny Heggheim <hegjon@gmail.com> - 6.25.1-1
- Updated to version 6.25.1
- Enabled compression support

* Wed Aug 25 2021 Yaakov Selkowitz <yselkowi@redhat.com> - 6.22.1-3
- Enabled s390x https://bugzilla.redhat.com/show_bug.cgi?id=1997426

* Wed Aug 25 2021 Jonny Heggheim <hegjon@gmail.com> - 6.22.1-2
- Disabled armv7hl https://bugzilla.redhat.com/show_bug.cgi?id=1997416
- Disabled s390x https://bugzilla.redhat.com/show_bug.cgi?id=1997426

* Mon Aug 02 2021 Jonny Heggheim <hegjon@gmail.com> - 6.22.1-1
- Updated to version 6.22.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 06 2021 Jonny Heggheim <hegjon@gmail.com> - 6.20.3-1
- Updated to 6.20.3

* Thu Apr 01 2021 Jonathan Wakely <jwakely@redhat.com> - 6.15.5-2
- Rebuilt for removed libstdc++ symbols (#1937698)

* Wed Mar 03 2021 Jonny Heggheim <hegjon@gmail.com> - 6.15.5-1
- Updated to version 6.15.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Jonny Heggheim <hegjon@gmail.com> - 6.13.3-1
- Updated to version 6.13.3

* Thu Sep 03 2020 Jonny Heggheim <hegjon@gmail.com> - 6.11.4-3
- Disable building on x86 due to compile errors

* Sat Jul 25 2020 Jonny Heggheim <hegjon@gmail.com> - 6.11.4-2
- Use RTTI

* Wed Jul 22 2020 Jonny Heggheim <hegjon@gmail.com> - 6.11.4-1
- Updated to 6.11.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 5.7.3-3
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Matej Mužila <mmuzila@redhat.com> - 5.7.3-1
- Update to version 5.7.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jan 24 2017 Matej Muzila <mmuzila@redhat.com> 5.2.1-1
- Packaged rocksdb
