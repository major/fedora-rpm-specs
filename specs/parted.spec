Summary: The GNU disk partition manipulation program
Name:    parted
Version: 3.6.37
Release: 1%{?dist}
License: GPL-3.0-or-later
URL:     http://www.gnu.org/software/parted

Source0: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1: https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2: pubkey.phillip.susi
Source3: pubkey.brian.lane

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
%{_libdir}/libparted.so.2.0.5
%{_libdir}/libparted-fs-resize.so.0
%{_libdir}/libparted-fs-resize.so.0.0.5
%{_infodir}/parted.info*

%files devel
%doc TODO doc/API.md doc/FAT
%{_includedir}/parted
%{_libdir}/libparted.so
%{_libdir}/libparted-fs-resize.so
%{_libdir}/pkgconfig/libparted.pc
%{_libdir}/pkgconfig/libparted-fs-resize.pc


%changelog
* Tue Mar 24 2026 Brian C. Lane <bcl@redhat.com> - 3.6.37-1
- Remove patches, all are included in the new release
- Dropping pre-3.6 changelog entries
- maint: regenerate .po, .pot files (bcl)
- NEWS: Update news (bcl)
- tests: t2420: New test confirming updating msdos doesn't add boot code
  (mike.fleetwood)
- libparted: Stop adding boot code in MBR when updating msdos table
  (mike.fleetwood)
- disk.c: Update metadata after reading partition table (pascal)
- Fix initialization of atr_c_locale inside PED_ASSERT (felipe)
- fat: Reword the failed to resize error (bcl)
- doc: Add more detail to --script documentation (bcl)
- Change AUTHORS urls to point to savannah.gnu.org (bcl)
- bootstrap.conf: Remove unused gnulib-tests (bcl)
- doc: API documentation moved to API.md (bcl)
- cfg.mk: Adjust maint.mk for the parted codebase (bcl)
- maint: Mention COPYING and INSTALL in README (bcl)
- Upate include error.h (bcl)
- tests: Use license URL not the old address (bcl)
- doc: Use license URL not the old address (bcl)
- maint: Update copyright statements to 2026 (bcl)
- maint: Update to latest gnulib and bootstrap script (bcl)
- hurd: Support USB device names (samuel.thibault)
- doc: Fix some groff/mandoc linting complaints (bcl)
- nilfs2: Fixed possible sigsegv in case of corrupted superblock (abutenko)
- libparted: Do not detect ext4 without journal as ext2 (pascal)
- tests: probing ext4 without journal should still indicate ext4 (bcl)
- tests: Add test for dvh with a bad checksum (bcl)
- libparted: Fix dvh disklabel unhandled exception (bcl)
- tests: Add test for SUN disklabel handling (bcl)
- libparted: Fix sun disklabel unhandled exception (bcl)
- bug#74444: [PATCH] parted: fix do_version declaration (rudi)
- libparted: Fail early when detecting nilfs2 (oldium.pro)
- doc: Document IEC unit behavior in the manpage (bcl)
- parted: Print the Fixing... message to stderr (bcl)
- docs: Finish setup of libparted API docs (bcl)
- m4: Remove unused parted.m4 (bcl)
- bug#64034: [PATCH] libparted: link libparted-fs-resize.so to libuuid
  (raj.khem)
- maint: Add .dirstamp files to .gitignore (yegorslists)
- parted: link to libuuid (yegorslists)
- maint: post-release administrivia (bcl)

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri May 30 2025 Brian C. Lane <bcl@redhat.com> - 3.6-12
- doc: Fix some groff/mandoc linting complaints (bcl)
- nilfs2: Fixed possible sigsegv in case of corrupted superblock (abutenko)
- libparted: Do not detect ext4 without journal as ext2 (pascal)
- tests: probing ext4 without journal should still indicate ext4 (bcl)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Brian C. Lane <bcl@redhat.com> - 3.6-10
- tests: Add test for dvh with a bad checksum (bcl)
- libparted: Fix dvh disklabel unhandled exception (bcl)
- tests: Add test for SUN disklabel handling (bcl)
- libparted: Fix sun disklabel unhandled exception (bcl)

* Wed Nov 20 2024 Brian C. Lane <bcl@redhat.com> - 3.6-9
- parted: Fix do_version declaration (rudi)

* Thu Oct 17 2024 Brian C. Lane <bcl@redhat.com> - 3.6-8
- libparted: Fail early when detecting nilfs2 (oldium.pro)

* Fri Aug 23 2024 Brian C. Lane <bcl@redhat.com> - 3.6-7
- tests: Move to tmt tests and switch to a functional test (bcl)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Brian C. Lane <bcl@redhat.com> - 3.6-5
- doc: Document IEC unit behavior in the manpage (bcl)
- parted: Print the Fixing... message to stderr (bcl)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 10 2023 Brian C. Lane <bcl@redhat.com> - 3.6-1
- Upstream 3.6 stable release
- Dropping pre-3.5 changelog entries
