Summary: The GNU disk partition manipulation program
Name:    parted
Version: 3.5
Release: 9%{?dist}
License: GPL-3.0-or-later
URL:     http://www.gnu.org/software/parted

Source0: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2: pubkey.phillip.susi
Source3: pubkey.brian.lane

# Upstream patches since v3.5 release
Patch0001: 0001-maint-post-release-administrivia.patch
Patch0002: 0002-parted-add-type-command.patch
Patch0003: 0003-libparted-add-swap-flag-for-DASD-label.patch
Patch0004: 0004-parted-Reset-the-filesystem-type-when-changing-the-i.patch
Patch0005: 0005-tests-t3200-type-change-now-passes.patch
Patch0006: 0006-libparted-Fix-check-for-availability-of-_type_id-fun.patch
Patch0007: 0007-parted-Simplify-code-for-json-output.patch
Patch0008: 0008-disk.in.h-Remove-use-of-enums-with-define.patch
Patch0009: 0009-libparted-Fix-handling-of-gpt-partition-types.patch
Patch0010: 0010-tests-Add-a-libparted-test-for-ped_partition_set_sys.patch
Patch0011: 0011-libparted-Fix-handling-of-msdos-partition-types.patch
Patch0012: 0012-tests-Add-a-libparted-test-for-ped_partition_set_sys.patch
Patch0013: 0013-show-GPT-UUIDs-in-JSON-output.patch
Patch0014: 0014-gpt-Add-no_automount-partition-flag.patch
Patch0015: 0015-tests-XFS-requires-a-minimum-size-of-300M.patch

BuildRequires: gcc
BuildRequires: e2fsprogs-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: gettext-devel
BuildRequires: texinfo
BuildRequires: device-mapper-devel
BuildRequires: libuuid-devel
BuildRequires: libblkid-devel >= 2.17
BuildRequires: gnupg2
BuildRequires: git
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: e2fsprogs
BuildRequires: xfsprogs
BuildRequires: dosfstools
BuildRequires: perl-Digest-CRC
BuildRequires: bc
BuildRequires: python3
BuildRequires: gperf
BuildRequires: make
BuildRequires: check-devel

# bundled gnulib library exception, as per packaging guidelines
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
Provides: bundled(gnulib)

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.


%package devel
Summary:  Files for developing apps which will manipulate disk partitions
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The GNU Parted library is a set of routines for hard disk partition
manipulation. If you want to develop programs that manipulate disk
partitions and filesystems using the routines provided by the GNU
Parted library, you need to install this package.


%prep
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S git_am
iconv -f ISO-8859-1 -t UTF8 AUTHORS > tmp; touch -r AUTHORS tmp; mv tmp AUTHORS

%build
autoreconf -fiv
CFLAGS="$RPM_OPT_FLAGS -Wno-unused-but-set-variable"; export CFLAGS
%configure --disable-static --disable-gcc-warnings
# Don't use rpath!
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%{__rm} -rf %{buildroot}
%make_install

# Remove components we do not ship
%{__rm} -rf %{buildroot}%{_libdir}/*.la
%{__rm} -rf %{buildroot}%{_infodir}/dir
%{__rm} -rf %{buildroot}%{_bindir}/label
%{__rm} -rf %{buildroot}%{_bindir}/disk

%find_lang %{name}


%check
export LD_LIBRARY_PATH=$(pwd)/libparted/.libs:$(pwd)/libparted/fs/.libs
make check

%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_sbindir}/parted
%{_sbindir}/partprobe
%{_mandir}/man8/parted.8*
%{_mandir}/man8/partprobe.8*
%{_libdir}/libparted.so.2
%{_libdir}/libparted.so.2.0.4
%{_libdir}/libparted-fs-resize.so.0
%{_libdir}/libparted-fs-resize.so.0.0.4
%{_infodir}/parted.info*

%files devel
%doc TODO doc/API doc/FAT
%{_includedir}/parted
%{_libdir}/libparted.so
%{_libdir}/libparted-fs-resize.so
%{_libdir}/pkgconfig/libparted.pc
%{_libdir}/pkgconfig/libparted-fs-resize.pc


%changelog
* Mon Jan 30 2023 Brian C. Lane <bcl@redhat.com> - 3.5-9
- SPDX migration

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Brian C. Lane <bcl@redhat.com> - 3.5-7
- libparted: Fix handling of msdos partition types
- tests: Add a libparted test for ped_partition_set_system on msdos
- parted: Add display of GPT UUIDs in JSON output
- Add no_automount flag support
- increase xfs size to 300M

* Mon Aug 08 2022 Brian C. Lane <bcl@redhat.com> - 3.5-6
- Fix ped_partition_set_system handling of existing flags

* Thu Aug 04 2022 Brian C. Lane <bcl@redhat.com> - 3.5-5
- Update enum patch description for upstream

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Adam Williamson <awilliam@redhat.com> - 3.5-3
- Set _FIRST_ and _LAST_ macro values directly

* Tue May 17 2022 Brian C. Lane <bcl@redhat.com> - 3.5-2
- tests: t3200-type-change now passes (bcl)
- parted: Reset the filesystem type when changing the id/uuid (bcl)
- libparted: add swap flag for DASD label (aschnell)
- parted: add type command (aschnell)
- maint: post-release administrivia (bcl)

* Mon Apr 18 2022 Brian C. Lane <bcl@redhat.com> - 3.5-1
- Upstream 3.5 stable release

* Wed Mar 30 2022 Brian C. Lane <bcl@redhat.com> - 3.4.64-1
- Upstream 3.4.64 Alpha release
- Dropped all patches included in new upstream release
- Bumped minor version on libparted.so and libparted-fs-resize.so

* Thu Feb 17 2022 Brian C. Lane <bcl@redhat.com> - 3.4-12
- gnulib: Use newer cdefs.h from gnulib (bcl)
- Update parted.spec to allow flatpak builds

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 06 2021 Brian C. Lane <bcl@redhat.com> - 3.4-11
- docs: Update documentation to be consistent

* Wed Oct 06 2021 Brian C. Lane <bcl@redhat.com> - 3.4-10
- gpt: Revert to filesystem GUID when setting flag to off (bcl)
- tests: Add a test to make sure GPT GUIDs default to filesystem (bcl)
- doc: Document gpt linux-home flag (bcl)
- gpt: Add linux-home flag (aschnell)
- gpt: Map PED_PARTITON_ flags to GUID values (aschnell)

* Thu Sep 23 2021 Brian C. Lane <bcl@redhat.com> - 3.4-9
- keep GUID specific attributes (aschnell)
- hurd: Implement partition table rereading (cjwatson)
- hurd: Support rumpdisk-based device names (samuel.thibault)
- hurd: Fix partition paths (cjwatson)

* Wed Aug 25 2021 Brian C. Lane <bcl@redhat.com> - 3.4-8
- parted: Add --json cmdline switch to output JSON (aschnell)
- parted: Allow empty string for partition name (aschnell)
- libparted: Check devpath before passing to strlen (bcl)

* Tue Aug 10 2021 Brian C. Lane <bcl@redhat.com> - 3.4-7
- libparted: Tell libdevmapper to retry remove when BUSY (bcl)
  Resolves: rhbz#1980697
- parted: Escape colons and backslashes in machine output (bcl)
- tests: check for vfat kernel support and tools (ross.burton)
- tests: add a helper to check the kernel knows about a file system (ross.burton)
- tests: add aarch64 and mips64 as a valid 64-bit machines (ross.burton)
- libparted: Add swap flag to msdos disklabel (bcl)
- Move Exception Option values into enum (bcl)

* Tue Aug 03 2021 Brian C. Lane <bcl@redhat.com> - 3.4-6
- spec: Use the %%gpgverify macro for the signature check
- tests/t3000: Use mkfs.hfsplus and fsck.hfsplus for resize tests (bcl)
- tests/t3000: Check for hfs and vfat support separately (bcl)
- tests: Reduce memory usage for tests using scsi_debug module (bcl)
- spec: Install to /usr/sbin and /usr/lib64 (bcl)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Brian C. Lane <bcl@redhat.com> - 3.4-4
- Fix issues that covscan classifies as important
  Resolves: rhbz#1938836
- Update gpg key for bcl@redhat.com
- Work around a mkswap bug

* Wed Mar 10 2021 Brian C. Lane <bcl@redhat.com> - 3.4-3
- Use autoreconf -fiv for autoconf 2.71 support
  Works with both 2.69 and 2.71

* Wed Feb 03 2021 Brian C. Lane <bcl@redhat.com> - 3.4-2
- Add --fix support from upstream

* Wed Jan 27 2021 Brian C. Lane <bcl@redhat.com> - 3.4-1
- New stable upstream release v3.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Brian C. Lane <bcl@redhat.com> - 3.3.52-1
- New upstream ALPHA release v3.3.52
- Includes all patches

* Mon Nov 30 2020 Brian C. Lane <bcl@redhat.com> - 3.3-8
- Add upstream commits to fix various gcc 10 warnings (bcl)

* Thu Nov 05 2020 Brian C. Lane <bcl@redhat.com> - 3.3-7
- Do not link to libselinux

* Fri Sep 25 2020 Brian C. Lane <bcl@redhat.com> - 3.3-6
- tests: Add a test for resizepart on a busy partition (bcl)
- parted: Preserve resizepart End when prompted for busy partition (bcl)
- tests: Add f2fs to the fs probe test (romain.perier)
- Add support for the F2FS filesystem (romain.perier)
- Removed reference to ped_file_system_create (max)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 3.3-4
- Use make macros
  https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro
- Switch to using %%autosetup instead of %%setup and git (bcl)
- Update tests.yml to install git and simplify source usage (bgoncalv)

* Fri Mar 06 2020 Brian C. Lane <bcl@redhat.com> - 3.3-3
- Add chromeos_kernel partition flag for gpt disklabels
- Add bls_boot partition flag for msdos and gpt disklabels

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Brian C. Lane <bcl@redhat.com> - 3.3-2
- tests: Test incomplete resizepart command
- Fix end_input usage in do_resizepart
  Resolves: rhbz#1701411

* Fri Oct 11 2019 Brian C. Lane <bcl@redhat.com> - 3.3-1
- New upstream release v3.3
  Includes the DASD virtio-blk fix.
- Dropping pre-3.2 changelog entries
