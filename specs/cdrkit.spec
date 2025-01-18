Name:    cdrkit
Version: 1.1.11
Release: 58%{?dist}
Summary: A collection of CD/DVD utilities
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     http://cdrkit.org/
Source:  http://cdrkit.org/releases/cdrkit-%{version}.tar.gz

Patch1: cdrkit-1.1.8-werror.patch
Patch2: cdrkit-1.1.9-efi-boot.patch
Patch4: cdrkit-1.1.9-no_mp3.patch
Patch5: cdrkit-1.1.9-buffer_overflow.patch
Patch6: cdrkit-1.1.10-build-fix.patch
Patch7: cdrkit-1.1.11-manpagefix.patch
Patch8: cdrkit-1.1.11-rootstat.patch
Patch9: cdrkit-1.1.11-usalinst.patch
Patch10: cdrkit-1.1.11-readsegfault.patch
Patch11: cdrkit-1.1.11-format.patch
Patch12: cdrkit-1.1.11-handler.patch
Patch13: cdrkit-1.1.11-dvdman.patch
Patch14: cdrkit-1.1.11-paranoiacdda.patch
Patch15: cdrkit-1.1.11-utf8.patch
Patch16: cdrkit-1.1.11-cmakewarn.patch
Patch17: cdrkit-1.1.11-memset.patch
Patch19: cdrkit-1.1.11-ppc64le_elfheader.patch
Patch20: cdrkit-1.1.11-werror_gcc5.patch
Patch21: cdrkit-1.1.11-devname.patch
Patch22: cdrkit-1.1.11-sysmacros.patch
Patch23: cdrkit-1.1.11-gcc10.patch
BuildRequires:  gcc
BuildRequires: cmake libcap-devel zlib-devel perl-interpreter perl-generators file-devel bzip2-devel

%description
cdrkit is a collection of CD/DVD utilities.

%package -n wodim
Summary: A command line CD/DVD recording program
Requires: libusal%{?_isa} = %{version}-%{release}
Requires(preun): /usr/sbin/alternatives coreutils
Requires(post): /usr/sbin/alternatives coreutils

%description -n wodim
Wodim is an application for creating audio and data CDs. Wodim
works with many different brands of CD recorders, fully supports
multi-sessions and provides human-readable error messages.

%package -n genisoimage
Summary: Creates an image of an ISO9660 file-system
Requires: libusal%{?_isa} = %{version}-%{release}
Requires(preun): /usr/sbin/alternatives coreutils
Requires(post): /usr/sbin/alternatives coreutils

%description -n genisoimage
The genisoimage program is used as a pre-mastering program; i.e., it
generates the ISO9660 file-system. Genisoimage takes a snapshot of
a given directory tree and generates a binary image of the tree
which will correspond to an ISO9660 file-system when written to
a block device. Genisoimage is used for writing CD-ROMs, and includes
support for creating boot-able El Torito CD-ROMs.

Install the genisoimage package if you need a program for writing
CD-ROMs.

%package -n dirsplit
Summary: Utility to split directories
Requires: perl-interpreter >= 4:5.8.1
Requires: genisoimage%{?_isa} = %{version}-%{release}

%description -n dirsplit
This utility is used to split directories into chunks before burning. 
Chunk size is usually set to fit to a CD/DVD.

%package -n icedax
Summary: A utility for sampling/copying .wav files from digital audio CDs
Requires: libusal%{?_isa} = %{version}-%{release}
Requires(preun): /usr/sbin/alternatives coreutils
Requires(post): /usr/sbin/alternatives coreutils
Requires: vorbis-tools
Requires: cdparanoia
BuildRequires: cdparanoia-devel

%description -n icedax
Icedax is a sampling utility for CD-ROM drives that are capable of
providing a CD's audio data in digital form to your host. Audio data
read from the CD can be saved as .wav or .sun format sound files.
Recording formats include stereo/mono, 8/12/16 bits and different
rates. Icedax can also be used as a CD player.

%package -n libusal
Summary: Library to communicate with SCSI devices

%description -n libusal
The libusal package contains C libraries that allows applications
to communicate with SCSI devices and is well suitable for writing
CD-R media.

%package -n libusal-devel
Summary: Development files for libusal
Requires: libusal%{?_isa} = %{version}-%{release}

%description -n libusal-devel
The libusal-devel package contains C libraries and header files
for developing applications that use libusal for communication with
SCSI devices.

%prep
%setup -q 
%patch -P1 -p1 -b .werror
%patch -P2 -p1 -b .efi
%patch -P4 -p1 -b .no_mp3
%patch -P5 -p1 -b .buffer_overflow
%patch -P6 -p1 -b .build-fix
%patch -P7 -p1 -b .manpagefix
%patch -P8 -p1 -b .rootstat
%patch -P9 -p1 -b .usalinst
%patch -P10 -p1 -b .readsegfault
%patch -P11 -p1 -b .format
%patch -P12 -p1 -b .handler
%patch -P13 -p1 -b .dvdman
%patch -P14 -p1 -b .paranoiacdda
# not using -b since otherwise backup files would be included into rpm
%patch -P15 -p1
%patch -P16 -p1 -b .cmakewarn
%patch -P17 -p1 -b .edcspeed
%patch -P19 -p1 -b .elfheader
%patch -P20 -p1 -b .werror_gcc5
%patch -P21 -p1 -b .devname
%patch -P22 -p1 -b .sysmacros
%patch -P23 -p1 -b .gcc10

# we do not want bundled paranoia library
rm -rf libparanoia

find . -type f -print0 | xargs -0 perl -pi -e 's#/usr/local/bin/perl#/usr/bin/perl#g'
find doc -type f -print0 | xargs -0 chmod a-x 


%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=format-security -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
export FFLAGS="$CFLAGS"

%cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DBUILD_SHARED_LIBS:BOOL=ON

%cmake_build

%install
%cmake_install
perl -pi -e 's#^require v5.8.1;##g' $RPM_BUILD_ROOT%{_bindir}/dirsplit
ln -s genisoimage $RPM_BUILD_ROOT%{_bindir}/mkisofs
ln -s genisoimage $RPM_BUILD_ROOT%{_bindir}/mkhybrid
ln -s icedax $RPM_BUILD_ROOT%{_bindir}/cdda2wav
ln -s wodim $RPM_BUILD_ROOT%{_bindir}/cdrecord
ln -s wodim $RPM_BUILD_ROOT%{_bindir}/dvdrecord

# missing man page. Do symlink like in debian
ln -sf wodim.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/netscsid.1.gz

# we don't need cdda2mp3 since we don't have any mp3 {en,de}coder
rm $RPM_BUILD_ROOT%{_bindir}/cdda2mp3

%post -n wodim
link=`readlink %{_bindir}/cdrecord`
if [ "$link" == "%{_bindir}/wodim" ]; then
	rm -f %{_bindir}/cdrecord
fi
link=`readlink %{_bindir}/dvdrecord`
if [ "$link" == "wodim" ]; then
	rm -f %{_bindir}/dvdrecord
fi

/usr/sbin/alternatives --install %{_bindir}/cdrecord cdrecord \
		%{_bindir}/wodim 50 \
	--slave %{_mandir}/man1/cdrecord.1.gz cdrecord-cdrecordman \
		%{_mandir}/man1/wodim.1.gz \
	--slave %{_bindir}/dvdrecord cdrecord-dvdrecord %{_bindir}/wodim \
	--slave %{_mandir}/man1/dvdrecord.1.gz cdrecord-dvdrecordman \
		%{_mandir}/man1/wodim.1.gz \
	--slave %{_bindir}/readcd cdrecord-readcd %{_bindir}/readom \
	--slave %{_mandir}/man1/readcd.1.gz cdrecord-readcdman \
		%{_mandir}/man1/readom.1.gz 

%preun -n wodim
if [ $1 = 0 ]; then
	/usr/sbin/alternatives --remove cdrecord %{_bindir}/wodim
fi

%post -n genisoimage
link=`readlink %{_bindir}/mkisofs`
if [ "$link" == "genisoimage" ]; then
	rm -f %{_bindir}/mkisofs
fi

/usr/sbin/alternatives --install %{_bindir}/mkisofs mkisofs \
		%{_bindir}/genisoimage 50 \
	--slave %{_mandir}/man1/mkisofs.1.gz mkisofs-mkisofsman \
		%{_mandir}/man1/genisoimage.1.gz \
	--slave %{_bindir}/mkhybrid mkisofs-mkhybrid %{_bindir}/genisoimage \
	--slave %{_mandir}/man1/mkhybrid.1.gz mkisofs-mkhybridman \
		%{_mandir}/man1/genisoimage.1.gz

%preun -n genisoimage
if [ $1 = 0 ]; then
	/usr/sbin/alternatives --remove mkisofs %{_bindir}/genisoimage
fi

%post -n icedax
link=`readlink %{_bindir}/cdda2wav`
if [ "$link" == "icedax" ]; then
	rm -f %{_bindir}/cdda2wav
fi
/usr/sbin/alternatives --install %{_bindir}/cdda2wav cdda2wav \
		%{_bindir}/icedax 50 \
	--slave %{_mandir}/man1/cdda2wav.1.gz cdda2wav-cdda2wavman \
		%{_mandir}/man1/icedax.1.gz 

%preun -n icedax
if [ $1 = 0 ]; then
	/usr/sbin/alternatives --remove cdda2wav %{_bindir}/icedax
fi

%ldconfig_scriptlets -n libusal

%files -n wodim
%license COPYING
%doc Changelog FAQ FORK START
%doc doc/READMEs doc/wodim
%{_bindir}/devdump
%{_bindir}/wodim
%ghost %{_bindir}/cdrecord
%ghost %{_bindir}/dvdrecord
%{_bindir}/readom
%{_sbindir}/netscsid
%{_mandir}/man1/devdump.*
%{_mandir}/man1/wodim.*
%{_mandir}/man1/netscsid.*
%{_mandir}/man1/readom.*

%files -n icedax
%license COPYING
%doc doc/icedax
%{_bindir}/icedax
%ghost %{_bindir}/cdda2wav
%{_bindir}/cdda2ogg
%{_mandir}/man1/icedax.*
%{_mandir}/man1/cdda2ogg.*
%{_mandir}/man1/list_audio_tracks.*

%files -n genisoimage
%license COPYING
%doc doc/genisoimage
%{_bindir}/genisoimage
%ghost %{_bindir}/mkisofs
%ghost %{_bindir}/mkhybrid
%{_bindir}/isodebug
%{_bindir}/isodump
%{_bindir}/isoinfo
%{_bindir}/isovfy
%{_bindir}/pitchplay
%{_bindir}/readmult
%{_mandir}/man5/genisoimagerc.*
%{_mandir}/man1/genisoimage.*
%{_mandir}/man1/isodebug.*
%{_mandir}/man1/isodump.*
%{_mandir}/man1/isoinfo.*
%{_mandir}/man1/isovfy.*
%{_mandir}/man1/pitchplay.*
%{_mandir}/man1/readmult.*

%files -n dirsplit
%license COPYING
%{_bindir}/dirsplit
%{_mandir}/man1/dirsplit.*

%files -n libusal
%license COPYING
%doc doc/plattforms/README.linux Changelog FAQ FORK START
%{_libdir}/libusal.so.*
%{_libdir}/librols.so.*

%files -n libusal-devel
%license COPYING
%{_libdir}/libusal.so
%{_libdir}/librols.so
%{_includedir}/usal

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.11-57
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.11-55
- Fix alternatives usage

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-46
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Than Ngo <than@redhat.com> - 1.1.11-44
- Fixed FTBFS

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul  4 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.11-39
- Spec cleanup and modernise, use %%license

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.1.11-35
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Wed Feb 22 2017 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-34
- FTBFS with gcc7, removed -Werror (no upstream to fix problems anyway)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-32
- FTBFS: <sys/sysmacros.h> included where "major" and "minor" macros are in use
  (cdrkit-1.1.11-sysmacros.patch added)
- https://bugzilla.redhat.com/show_bug.cgi?id=1263599 - man page clarified
  (cdrkit-1.1.11-manpagefix.patch modified)

* Tue Feb 16 2016 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-31
- FTBFS: added -Wno-error=misleading-indentation

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-28
- libusal: added /dev/srN next to /dev/scdN path when scanning for devices
  added cdrkit-1.1.11-devname.patch
  bz#1053056

* Wed Feb 25 2015 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-27
- fixed FTBFS with gcc5, added cdrkit-1.1.11-werror_gcc5.patch

* Fri Nov 07 2014 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-26
- reverted back to cdda-paranoia, cdio has now incompatible GPLv3+ license

* Wed Nov 05 2014 Dan Horák <dan[at]danny.cz> - 1.1.11-25
- fix build on ppc* (#1144072)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.1.11-22
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-20
- do not include empty fedora/* directories in debuginfo package

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.1.11-19
- Perl 5.18 rebuild

* Wed Jul 17 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-18
- ported from cdda-paranoia to libcdio-paranoia, modified paranoia-cdda.patch
- fixed bogus date in changelog

* Mon Feb 25 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-17
- modified the memset patch, memsetting the whole array

* Fri Feb 22 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.1.11-16
- changed or deleted faulty and unneeded memset's that caused build failure with gcc-4.8 -Werror

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 03 2012 Honza Horak <hhorak@redhat.com> - 1.1.11-14
- Add coreutils as preun/post requirements for wodim and genisoimage
  Resolves: #862554

* Mon Aug 27 2012 Honza Horak <hhorak@redhat.com> - 1.1.11-13
- Add mkhybrid(1) as a symlink to genisoimage(1)
- Spec file cleanup

* Mon Jul 30 2012 Honza Horak <hhorak@redhat.com> - 1.1.11-12
- Use system cdparanoia instead of old bundled version
- Build libusal as a shared library
- Messages from rpmlint clean-up

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Honza Horak <hhorak@redhat.com> - 1.1.11-9
- Fix driver specification in man pages
  (Resolves: #711623)

* Thu Jun 02 2011 Honza Horak <hhorak@redhat.com> - 1.1.11-8
- Fix segmentation fault when icedax exits while sleeping after ctrl-c
  (Resolves: #709902)

* Tue May 17 2011 Honza Horak <hhorak@redhat.com> - 1.1.11-7
- Fix automatic formatting of DVD+RW if needed
  (Resolves: #519465)

* Thu Mar 17 2011 Honza Horak <hhorak@redhat.com> - 1.1.11-6
- Added Provides: libusal-static for libusal-devel subpackage
  (Resolves: #688347)

* Mon Mar 07 2011 Honza Horak <hhorak@redhat.com> - 1.1.11-5
- Fix segmentation fault in readom
  (Resolves: #682591)

* Thu Feb 17 2011 Honza Horak <hhorak@redhat.com> - 1.1.11-4
- Library libusal is installed in order to be used by other apps
  (Resolves: #588508)
  https://bugzilla.redhat.com/show_bug.cgi?id=588508

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Honza Horak <hhorak@redhat.com> 1.1.11-2
- fixed man page missing arguments (Resolves: #647024)
  https://bugzilla.redhat.com/show_bug.cgi?id=647024
- fixed erroneous "Unknown file type (unallocated)" warning 
  (Resolves: #174667)
  https://bugzilla.redhat.com/show_bug.cgi?id=174667

* Mon Oct 18 2010 Nikola Pajkovsky <npajkovs@redhat.com> 1.1.11-1
- new upstream version 1.1.11

* Mon Jun 21 2010 Roman Rakus <rrakus@redhat.com> - 1.1.10-2
- Added missing manpage for netscsid (symlink to wodim manpage)

* Wed Jan 20 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 1.1.10-1
- new upstream version 1.1.10

* Tue Aug 11 2009 Nikola Pajkovsky <npajkovs@redhat.com> 1.1.9-10
- fix #508449. fix string overflow breakage when using the -root

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Nikola Pajkovsky <npajkovs@redhat.com> 1.1.9-8
- fix buffer overflow

* Fri Jul 10 2009 Adam Jackson <ajax@redhat.com> 1.1.9-7
- Move dirsplit to a subpackage to isolate the perl dependency.

* Mon Jun 15 2009 Roman Rakus <rrakus@redhat.com> - 1.1.9-6
- rename functions as they conflict with glibc
- Don't push cdda2mp3 because we don't have any mp3 coder
  Resolves: #505918

* Tue Jun 02 2009 Roman Rakus <rrakus@redhat.com> - 1.1.9-5
- Added Requires vorbis-tools in icedax (rhbz #503699)

* Wed Feb 25 2009 Peter Jones <pjones@redhat.com> - 1.1.9-4
- Add support for EFI boot images.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Roman Rakus <rrakus@redhat.com> - 1.1.9-2
- Use -fno-strict-aliasing to prevent strict_aliasing warnings/errors

* Mon Oct 27 2008 Roman Rakus <rrakus@redhat.com> - 1.1.9-1
- Bump to version 1.1.9

* Tue May 27 2008 Roman Rakus <rrakus@redhat.com> - 1.1.8-1
- Version 1.1.8 - old patches included
                - added bzip2-devel to build requirements
- fixed #171510 - preserve directory permissions

* Wed Feb 27 2008 Harald Hoyer <harald@redhat.com> 1.1.6-11
- refined -Werror patch

* Mon Feb 25 2008 Harald Hoyer <harald@redhat.com> 1.1.6-10
- patched to compile with -Werror (rhbz#429385)

* Thu Feb 21 2008 Harald Hoyer <harald@redhat.com> 1.1.6-9
- fixed loop on error message for old dev syntax (rhbz#429386)

* Thu Feb 21 2008 Harald Hoyer <harald@redhat.com> 1.1.6-8
- added file-devel to build requirements

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.6-7
- Autorebuild for GCC 4.3

* Tue Sep 25 2007 Harald Hoyer <harald@redhat.com> - 1.1.6-6
- fixed readcd man page symlink

* Fri Sep 21 2007 Harald Hoyer <harald@redhat.com> - 1.1.6-5
- fixed rhbz#255001 - icedax --devices segfaults
- fixed rhbz#249357 - Typo in wodim output

* Fri Sep 21 2007 Harald Hoyer <harald@redhat.com> - 1.1.6-4
- play stupid tricks, to let alternatives make the links and
  rpm not removing them afterwards
- removed bogus warning for "." and ".."

* Thu Sep 20 2007 Harald Hoyer <harald@redhat.com> - 1.1.6-3
- fixed rhbz#248262
- switched to alternatives

* Fri Aug 17 2007 Harald Hoyer <harald@redhat.com> - 1.1.6-2
- changed license to GPLv2

* Wed Jun 20 2007 Harald Hoyer <harald@redhat.com> - 1.1.6-1
- version 1.1.6
- added readcd symlink

* Mon Apr 23 2007 Harald Hoyer <harald@redhat.com> - 1.1.2-4
- bump obsoletes/provides

* Tue Feb 27 2007 Harald Hoyer <harald@redhat.com> - 1.1.2-3
- applied specfile changes as in bug #224365

* Wed Jan 24 2007 Harald Hoyer <harald@redhat.com> - 1.1.2-1
- version 1.1.2
