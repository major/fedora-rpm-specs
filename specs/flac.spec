Summary: An encoder/decoder for the Free Lossless Audio Codec
Name: flac
Version: 1.5.0
Release: 3%{?dist}
License: BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.3-or-later
Source0: https://downloads.xiph.org/releases/flac/flac-%{version}.tar.xz
URL: https://www.xiph.org/flac/
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: libogg-devel
BuildRequires: gcc gcc-c++ automake autoconf libtool gettext-devel doxygen
BuildRequires: make

%description
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.

This package contains the command-line tools and documentation.

%package libs
Summary: Libraries for the Free Lossless Audio Codec
Obsoletes: flac < 1.2.1-11
# xmms-flac dropped in 1.3.3-8
Obsoletes: xmms-flac < 1.3.3-8

%description libs
FLAC stands for Free Lossless Audio Codec. Grossly oversimplified, FLAC
is similar to Ogg Vorbis, but lossless. The FLAC project consists of
the stream format, reference encoders and decoders in library form,
flac, a command-line program to encode and decode FLAC files, metaflac,
a command-line metadata editor for FLAC files and input plugins for
various music players.
This package contains the FLAC libraries.

%package devel
Summary: Development libraries and header files from FLAC
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains all the files needed to develop applications that
will use the Free Lossless Audio Codec.

%prep
%setup -q

%build
# use our libtool to avoid problems with RPATH
./autogen.sh -V

%configure \
    --htmldir=%{_docdir}/flac/html \
    --disable-silent-rules \
    --disable-thorough-tests

%make_build

%install
%make_install

rm -r %{buildroot}%{_docdir}/flac
rm %{buildroot}%{_libdir}/*.la

%check
make check

%ldconfig_scriptlets libs

%files
%{_bindir}/flac
%{_bindir}/metaflac
%{_mandir}/man1/*

%files libs
%doc AUTHORS README.md CHANGELOG.md
%license COPYING.*
%{_libdir}/libFLAC.so.14*
%{_libdir}/libFLAC++.so.11*

%files devel
%doc doc/api
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*.m4

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue May 27 2025 Miroslav Lichvar <mlichvar@redhat.com> 1.5.0-2
- rebuild

* Thu Feb 13 2025 Miroslav Lichvar <mlichvar@redhat.com> 1.5.0-1
- update to 1.5.0

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Miroslav Lichvar <mlichvar@redhat.com> 1.4.3-1
- update to 1.4.3
- convert license tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Miroslav Lichvar <mlichvar@redhat.com> 1.4.2-1
- update to 1.4.2

* Mon Sep 26 2022 Miroslav Lichvar <mlichvar@redhat.com> 1.4.1-1
- update to 1.4.1

* Mon Sep 12 2022 Miroslav Lichvar <mlichvar@redhat.com> 1.4.0-1
- update to 1.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Miroslav Lichvar <mlichvar@redhat.com> 1.3.4-1
- update to 1.3.4 (CVE-2021-0561)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.3.3-8
- drop xmms plugin (#1965618)

* Fri Feb 19 2021 Adam Jackson <ajax@redhat.com> - 1.3.3-7
- Fix the previous change to actually build in RHEL

* Thu Feb 18 2021 Adam Jackson <ajax@redhat.com> - 1.3.3-6
- Disable xmms in RHEL

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Miroslav Lichvar <mlichvar@redhat.com> 1.3.3-4
- fix out-of-bounds read in decoder (CVE-2020-0499)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Miroslav Lichvar <mlichvar@redhat.com> 1.3.3-1
- update to 1.3.3
- include soname in file list

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 1.3.2-11
- Remove obsolete requirements for %%post/%%postun scriptlets

* Tue Feb 05 2019 Miroslav Lichvar <mlichvar@redhat.com> 1.3.2-10
- rebuild again
- fix indentation in buildrequires

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Miroslav Lichvar <mlichvar@redhat.com> 1.3.2-7
- fix memory leak in parsing of vorbis comments (CVE-2017-6888)
- add gcc to build requirements

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.2-5
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Miroslav Lichvar <mlichvar@redhat.com> 1.3.2-1
- update to 1.3.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 10 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.1-5
- add xmms-flac plugin as a conditionalized subpackage

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.3.1-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Thu Nov 27 2014 Miroslav Lichvar <mlichvar@redhat.com> 1.3.1-1
- update to 1.3.1 (CVE-2014-8962, CVE-2014-9028)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.3.0-2
- fix memory corruption in metaflac (#969259)
- disable slower assembly code

* Tue May 28 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.3.0-1
- update to 1.3.0

* Tue Apr 02 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.3.0-0.2.pre3
- update to 1.3.0pre3

* Tue Mar 05 2013 Miroslav Lichvar <mlichvar@redhat.com> 1.3.0-0.1.pre1
- update to 1.3.0pre1
- make some dependencies arch-specific

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-13.20121204gita43f56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Kalev Lember <kalevlember@gmail.com> - 1.2.1-12.20121204gita43f56
- Added self-obsoletes to help multilib upgrades

* Tue Dec 04 2012 Miroslav Lichvar <mlichvar@redhat.com> 1.2.1-11.20121204gita43f56
- update to 20121204gita43f56
- create libs subpackage
- split documentation to base and devel subpackages
- drop defattr macros
- add GFDL to License tag

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec  9 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2.1-8
- Rebuild to fix FTBFS

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 17 2008 Miroslav Lichvar <mlichvar@redhat.com> 1.2.1-4
- speed up decoding
- CFLAGS cleanup

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.1-3
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Miroslav Lichvar <mlichvar@redhat.com> 1.2.1-2
- fix building with gcc-4.3 
- reenable some assembly optimizations
- hide private libFLAC symbols (#285961)
- update license tag
- add %%check
- remove -maltivec from CFLAGS

* Mon Sep 17 2007 - Bastien Nocera <bnocera@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Wed Sep 12 2007 - Bastien Nocera <bnocera@redhat.com> - 1.2.0-3
- Make a few functions hidden, to try and avoid textrels
- Disable optimisations on x86 for the same reason
  (#285961)

* Tue Sep 11 2007 - Bastien Nocera <bnocera@redhat.com> - 1.2.0-2
- Update GNU stack patch to cover all the NASM sources used

* Mon Sep 10 2007 - Bastien Nocera <bnocera@redhat.com> - 1.2.0-1
- Update for 1.20 and drop obsolete patches (#285161)

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 1.1.4-5
- Rebuild for build ID

* Thu Apr 12 2007 - Bastien Nocera <bnocera@redhat.com> - 1.1.4-4
- The byteSwap symbol shouldn't be global, reported by Joe Orton
  <jorton@redhat.com> (#215920)

* Wed Feb 14 2007 - Bastien Nocera <bnocera@redhat.com> - 1.1.4-3
- Also include the new pkgconfig files

* Wed Feb 14 2007 - Bastien Nocera <bnocera@redhat.com> - 1.1.4-2
- Update link-ogg patch for 1.1.4

* Wed Feb 14 2007 - Bastien Nocera <bnocera@redhat.com> - 1.1.4-1
- Update to upstream 1.1.4

* Tue Feb 13 2007 - Bastien Nocera <bnocera@redhat.com> - 1.1.3-2
- A few fixes from the the Fedora merge review
- Remove the static library

* Tue Feb 13 2007 - Bastien Nocera <bnocera@redhat.com> - 1.1.3-1
- Update with work from Matthias Clasen <mclasen@redhat.com> up
  to upstream 1.1.3 (#229462)
- Remove xmmx-flac Obsolete, as we don't ship the xmms plugin

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.2-27
- rebuild
- Try building w/ glib2-devel

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 1.1.2-26
- rebuild for -devel deps

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.1.2-25.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.1.2-25.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Apr 21 2005 Warren Togami <wtogami@redhat.com> - 1.1.2-25
- Fix buildreqs  (#154649 thias)
- obsolete older xmms-flac

* Mon Apr  4 2005 Elliot Lee <sopwith@redhat.com> - 1.1.2-24
- Removed xmms-flac subpackage

* Tue Mar 29 2005 John (J5) Palmieri <johnp@redhat.com> 1.1.2-2
- Rebuild (flac picked up a dependancy on it's older version)

* Mon Mar 28 2005 John (J5) Palmieri <johnp@redhat.com> 1.1.2-1
- Update to upstream version 1.1.2
- Replace flac-1.1.0-libtool.patch with flac-1.1.2-libtool.patch

* Wed Mar 02 2005 John (J5) Palmieri <johnp@redhat.com> 1.1.0-9
- rebuild for gcc 4.0

* Wed Feb 23 2005 Colin Walters <walters@redhat.com> 1.1.0-8
- New patch flac-1.1.0-gnu-stack.patch from Ulrich Drepper to mark asm
  as not requiring an executable stack

* Thu Jul 15 2004 Tim Waugh <twaugh@redhat.com> 1.1.0-7
- Fixed warnings in shipped m4 file.

* Mon Jun 21 2004 Colin Walters <walters@redhat.com> 1.1.0-6
- BuildRequire glib-devel for xmms plugin
- BuildRequire nasm

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Apr 04 2004 Warren Togami <wtogami@redhat.com> 1.1.0-4
- #119551 flac-xmms -> xmms-flac to match fedora.us and freshrpms.net
- Obsoletes flac-libs to upgrade smoothly from fedora.us

* Thu Mar 11 2004 Bill Nottingham <notting@redhat.com> 1.1.0-3
- fix x86_64 linkage (#117893)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Aug  6 2003 Bill Nottingham <notting@redhat.com> 1.1.0-1
- initial build
