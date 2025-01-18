Name:           fuse-encfs
Version:        1.9.5
Release:        24%{?dist}
Summary:        Encrypted pass-thru filesystem in userspace

License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Url:            https://github.com/vgough/encfs
Source0:        https://github.com/vgough/encfs/releases/download/v%{version}/encfs-%{version}.tar.gz
Source1:        https://github.com/vgough/encfs/releases/download/v%{version}/encfs-%{version}.tar.gz.asc
Source2:        895F5BC123A02740.gpg

Requires:       fuse >= 2.6
Provides:       encfs = %{version}-%{release}
Provides:       encfs%{?_isa} = %{version}-%{release}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel >= 0.18
BuildRequires:  gnupg2
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  perl(Locale::TextDomain)
#BuildRequires:  pkgconfig(easyloggingpp)
BuildRequires:  pkgconfig(fuse) >= 2.6
%if 0%{?fedora} < 41
BuildRequires: pkgconfig(openssl)
%else
BuildRequires: openssl-devel-engine
%endif
BuildRequires:  pkgconfig(tinyxml2)

%description
EncFS implements an encrypted filesystem in userspace using FUSE.  FUSE
provides a Linux kernel module which allows virtual filesystems to be written
in userspace.  EncFS encrypts all data and filenames in the filesystem and
passes access through to the underlying filesystem.  Similar to CFS except that
it does not use NFS.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n encfs-%{version}
rm -rf vendor/github.com/leethomasson
mkdir %{_target_platform}

%build
%cmake \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DINSTALL_LIBENCFS=ON \
    -DUSE_INTERNAL_TINYXML=OFF

%cmake_build

%install
%cmake_install
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.so

%find_lang encfs

%files -f encfs.lang
%doc AUTHORS ChangeLog README.md
%license COPYING COPYING.GPL COPYING.LGPL
%{_bindir}/encfs*
%{_libdir}/libencfs.so.*
%{_mandir}/man1/encfs*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.9.5-23
- rebuild for tinyxml2

* Tue Jul 23 2024 Vasiliy Glazov <vascom2@gmail.com> - 1.9.5.-22
- Fix build with openssl

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Peter Lemenkov <lemenkov@gmail.com> - 1.9.5-18
- Switch to SPDX license tag
- Check GPG signature

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 1.9.5-15
- Rebuild for tinyxml2-9.0.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Peter Lemenkov <lemenkov@gmail.com> - 1.9.5-13
- No longer requires rlog

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.9.5-11
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.9.5-3
- rebuilt against new tinyxml2-7.x

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 28 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.5-1
- Update to 1.9.5

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.4-1
- Update to 1.9.4

* Tue Jan 23 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.2-5
- Rebuild because libtinyxml2 api change

* Mon Oct 02 2017 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.2-4
- Added fix patch (rhbz #1487354)

* Fri Aug 11 2017 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.2-3
- Correct exec permission (rhbz #1382894)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.2-1
- Update to 1.9.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.1-5
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.1-3
- Rebuilt for Boost 1.63

* Sat Oct 08 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.1-2
- Correct exec permission (rhbz #1382894)

* Mon Sep 19 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.1-1
- Update to 1.9.1

* Thu Sep 15 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.0-1
- Update to 1.9.0

* Thu Aug 04 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.1-2
- Add default-permissions revert patch

* Thu Mar 31 2016 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.1-1
- Update to 1.8.1
- Clean spec

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.7.4-23
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.7.4-22
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-21
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.7.4-20
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.4-18
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.7.4-17
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.7.4-14
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.7.4-12
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.7.4-11
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.7.4-10
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 1.7.4-9
- Rebuild for new boost

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Till Maas <opensource@till.name> - 1.7.4-7
- Add el5 conditionals for obsoleted macros
- Use less globbing in %%files
- Use boost141 in el5

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Thomas <thomas.spura@googlemail.com> - 1.7.4-4
- rebuild for https://fedoraproject.org/wiki/Features/F17Boost148

* Fri Sep 09 2011 Adam Jackson <ajax@redhat.com> 1.7.4-3
- Rebuild for boost 1.47

* Thu Aug 25 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.7.4-2
- Rebuilt for new boost

* Mon Apr 11 2011 Peter Lemenkov <lemenkov@gmail.com> - 1.7.4-1
- Ver. 1.7.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.7.2-2
- rebuild for new boost

* Tue Sep  7 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.7.2-1
- Ver. 1.7.2

* Sun Sep  5 2010 Peter Lemenkov <lemenkov@gmail.com> - 1.7.1-1
- Fixed three security flaws (see rhbz #630460)
- Cleaned up spec-file a little

* Sun Aug 01 2010 Josh Kayse <jokajak@fedoraproject.org> - 1.6.1-1
- update to 1.6-1
- remove patch because it's been incorporated

* Thu Jul 29 2010 Bill Nottingham <notting@redhat.com> - 1.5-13
- Rebuild for boost-1.44

* Tue Jul 27 2010 Bill Nottingham <notting@redhat.com> - 1.5-12
- Rebuild for boost-1.44

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 1.5.11
- Rebuild for Boost soname bump

* Sat Oct 17 2009 Peter Lemenkov <lemenkov@gmail.com> 1.5-10
- Added version in Requires for boost-devel

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> 1.5-9
- rebuilt with new fuse

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.5-8
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 03 2009 Caolán McNamara <caolanm@redhat.com> - 1.5-6
- constify ret of strchr(const char*)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> 1.5-4
- rebuild with new openssl

* Tue Dec 30 2008 Peter Lemenkov <lemenkov@gmail.com> 1.5-3
- Fixed URL

* Thu Dec 18 2008 Petr Machata <pmachata@redhat.com> - 1.5-2
- Rebuild with new boost

* Sun Oct 26 2008 Peter Lemenkov <lemenkov@gmail.com> 1.5-1
- Ver. 1.5
- Dropped upstreamed patches

* Tue Aug 12 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.2-5
- Rebuild with new boost

* Fri Aug  1 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.2-4
- Fix build with new rlog

* Sat Jul 12 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.2-3
- rebuild due to rlog soname bump

* Mon May  5 2008 Tomas Hoger <thoger@redhat.com> - 1.4.2-2
- Work-around broken boost library path auto detection causing build failures
  on 64-bit architectures.

* Mon Apr 14 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.2-1
- Ver. 1.4.2
- add option to pass-through file 'holes'.  Only available in expert mode
- config file format changed to XML via boost serialization
  (config file is now .encfs6.xml)
- remove ulockmgr support, caused numerous locking issues. (bz# 440483)
- fix symlink handling in encfsctl export
- fix stdinpass option parsing, reported by Scott Hendrickson
- fix path suffix in encfsctl

* Fri Mar 28 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.4.1.1-5
- Update patch for building with GCC 4.3 (use <cstring> throughout)

* Tue Mar 25 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.1.1-4.1
- Another attempt to fix GCC 4.3 builds

* Tue Mar 25 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.1.1-4
- Another attempt to fix GCC 4.3 builds

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.4.1.1-3
- Autorebuild for GCC 4.3

* Sat Feb  9 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.1.1-2
- Rebuild for GCC 4.3

* Wed Jan 23 2008 Peter Lemenkov <lemenkov@gmail.com> 1.4.1.1-1
- Ver. 1.4.1.1
- Changed License tag according to Fedora policy
- Added new BR - boost-devel
- Proper locale handling
- Some other cosmetic changes

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.3.2-2
- Rebuild for deps

* Thu Apr 12 2007 Peter Lemenkov <lemenkov@gmail.com> 1.3.2-1
- Version 1.3.2

* Tue Sep 12 2006 Peter Lemenkov <lemenkov@gmail.com> 1.3.1-3%{?dist}
- Rebuild for FC6

* Sat Aug 26 2006 Peter Lemenkov <lemenkov@newmail.ru> 1.3.1-2%{?dist}
- Added necessary 'requires'field

* Wed May 03 2006 Peter Lemenkov <lemenkov@newmail.ru> 1.3.1-1%{?dist}
- Version 1.3.1

* Thu Mar 30 2006 Peter Lemenkov <lemenkov@newmail.ru> 1.3.0-1%{?dist}
- Version 1.3.0

* Fri Dec 16 2005 Peter Lemenkov <lemenkov@newmail.ru> 1.2.5-1
- Initial build for FE

* Fri Nov 11 2005 Valient Gough <vgough@pobox.com>
- Release 1.2.5
- Fix race condition when using newer versions of GCC.  Fixes problem reported
  by Chris at x.nu.
- add encfssh script, thanks to David Rosenstrauch
* Fri Aug 26 2005 Valient Gough <vgough@pobox.com>
- Release 1.2.4
- fix segfault if small invalid filenames were encountered in the encrypted
  directory, reported by paulgfx.
- try and detect if user tries to mount the filesystem over the top of the
  encrypted directory, problem reported by paulgfx.
- environment variable ENCFS5_CONFIG can be used to override the location of
  the .encfs5 configuration file.
- add encfsctl 'export' command, patch from Janne Hellsten
  
* Tue Apr 19 2005 Valient Gough <vgough@pobox.com>
- Release 1.2.1
- add --public mount option
- add --stdinpass option to read password from stdin for scripting
- import latest rosetta translation updates

* Thu Feb 10 2005 Valient Gough <vgough@pobox.com>
- Release 1.2.0
- Fix bug with MAC headers and files > 2GB, reported by Damian Frank
- Fix bug with external password interface which could result in problems
  communicating with external password program.  Found by Olivier Dournaux.
- Switch to FUSE 2.2 API -- support for FUSE 1.x has been dropped.
- Add support for inode numbering pass-thru (when used 'use_ino' option to
  fuse).  This allows encoded filesystem to use the same inode numbers as the
  underlying filesystem.

* Wed Jan 12 2005 Valient Gough <vgough@pobox.com>
- Release 1.1.11
- add internationalization support.  Thanks to lots of contributors, there are
  translations for serveral languages.
- added workaround for libfuse mount failure with FUSE 1.4
- fix compile failure with FUSE 1.4

* Mon Nov 8 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.10
- fix problems with recursive rename
- fix incorrect error codes from xattr functions

* Sun Aug 15 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.9
- fix another rename bug (affected filesystems with 'paranoia' configuration)

* Sat Aug 14 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.8
- Improve MAC block header processing.

* Thu Aug 12 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.7
- fix bug in truncate() for unopened files.

* Mon Aug 9 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.6
- fix header IV creation when truncate() used to create files.
- add support for IV chaining to old 0.x filesystem support code (useful for
  systems with old OpenSSL, like RedHat 7.x).

* Thu Jul 22 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.5

* Sat Jul 10 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.4
- add external password prompt support.

* Thu Jun 24 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.3

* Fri May 28 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.2
- Fix bug affecting filesystems with small empty directories (like XFS)
- Updates to recursive rename code to undo all changes on failure.
- Fix OpenSSL dependency path inclusion in build.

* Wed May 19 2004 Valient Gough <vgough@pobox.com>
- Release 1.1.1
- Fix MAC header memory size allocation error.
- Add file rename-while-open support needed for Evolution.

* Thu May 13 2004 Valient Gough <vgough@pobox.com>
- Second release candidate for version 1.1
- Add support for block mode filename encryption.
- Add support for per-file initialization vectors.
- Add support for directory IV chaining for per-directory initialization
  vectors.
- Add support for per-block MAC headers for file contents.
- Backward compatibility support dropped for filesystems created by version
  0.x.  Maintains backward compatible support for versions 1.0.x.

* Sun Apr 4 2004 Valient Gough <vgough@pobox.com>
- Release 1.0.5
- Allow truncate call to extend file (only shrinking was supported)

* Fri Mar 26 2004 Valient Gough <vgough@pobox.com>
- Release 1.0.4
- Large speed improvement.
- Add support for FUSE major version 2 API.

* Thu Mar 18 2004 Valient Gough <vgough@pobox.com>
- Release 1.0.3
- Fix bugs in truncation and padding code.

* Sat Mar 13 2004 Valient Gough <vgough@pobox.com>
- Release 1.0.2
- Use pkg-config to check for OpenSSL and RLog build settings
- Add support for '--' argument to encfs to pass arbitrary options to FUSE /
  fusermount.
- Add man pages.

* Tue Mar 2 2004 Valient Gough <vgough@pobox.com>
- Release 1.0.1
- Fix problem with using OpenSSL's EVP_BytesToKey function with variable
  key length ciphers like Blowfish, as it would only generate 128 bit keys.
- Some configure script changes to make it possible to use --with-extra-include
  configure option to pick up any necessary directories for OpenSSL.

* Fri Feb 27 2004 Valient Gough <vgough@pobox.com>
- Release 1.0
- Added some pre-defined configuration options at startup to make filesystem
  creation a bit more user friendly.

* Mon Feb 23 2004 Valient Gough <vgough@pobox.com>
- Merge development branch to mainline.  Source modularized to make it easier
  to support different algorithms.
- Added encfsctl program which can show information about an encrypted
  directory and can change the user password used to store the volume key.
- Added support for AES and BlowFish with user specified keys and block sizes
  (when building with OpenSSL >= 0.9.7).
- Backward compatible with old format, but new filesystems store configuration
  information in a new format which is not readable by old encfs versions.

* Sat Feb 7 2004 Valient Gough <vgough@pobox.com>
- Improved performance by fixing cache bug which caused cached data to not be
  used as often as it could have been.  Random seek performance improved by
  600% according to Bonnie++ benchmark.
- Fixed bugs preventing files larger then 2GB.  Limit should now be around
  128GB (untested - I don't have that much drive space).  > 2GB also requires
  recent version of FUSE module (from Feb 6 or later) and an underlying
  filesystem which supports large files.
- Release 0.6
