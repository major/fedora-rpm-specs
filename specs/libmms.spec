Name:          libmms
Version:       0.6.4
Release:       28%{?dist}
Summary:       Library for Microsoft Media Server (MMS) streaming protocol
License:       LGPL-2.1-or-later
URL:           https://www.sf.net/projects/libmms
Source0:       https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# https://sourceforge.net/p/libmms/code/ci/b9bbe17c08e5dcbe3ce841e6bed52ce8d8b10f9e/
Patch1:        0001-Remove-Requires-glib-2.0-since-libmms-no-longer-depe.patch
# https://sourceforge.net/p/libmms/code/ci/34060b0c0cb13eed323577becf72a13b43654c00/
Patch2:        0002-Add-a-new-testfiledownload.c-example.patch
# https://sourceforge.net/p/libmms/code/ci/67d54003b8075b8ea8102bc4a808df4543ab113a/
Patch3:        0003-Fix-build-if-strndup-is-missing.patch
# https://sourceforge.net/p/libmms/code/ci/5cface3df0e0213d8bc593d82a9a7c1e648dd71a/
Patch4:        0004-Patch-to-remove-redundant-comparison-in-file-mmsh.c.patch
# https://sourceforge.net/p/libmms/code/ci/8b5e303fc1f01521c727e351270dd68c4f15190b/
Patch5:        0005-Avoid-possible-overflow-in-sprintf.patch
# https://sourceforge.net/p/libmms/code/ci/5cface3df0e0213d8bc593d82a9a7c1e648dd71a/
Patch6:        0006-Fix-possible-NULL-Pointer-deref-in-mmsh.c.patch
# https://sourceforge.net/p/libmms/code/ci/5d39f692d55c04839be78e470820f49d53e40bcb/
Patch7:        0007-Add-check-for-sys-select.h-and-use-it.patch
# https://sourceforge.net/p/libmms/code/ci/a9f692323e597324e6f01263c12b6f4290d5b56f/
Patch8:        0008-C89-fixes-for-Haiku.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

%description
MMS is a streaming protocol used in Microsoft server products, commonly used to
stream WMV data. You can encounter mms:// style URLs all over the net,
especially on news sites and other content-serving sites. Libmms allows you to
download content from such sites, making it easy to add MMS support to your
media applications.

%package devel
Summary:       Development package for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}
Requires:      pkgconf-pkg-config

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1
chmod -x ChangeLog src/mmsh.c

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la

%files
%doc AUTHORS ChangeLog README*
%license COPYING.LIB
%{_libdir}/%{name}.so.0{,.*}

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 25 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.6.4-24
- add explicit build dependencies
- use a modern pkgconf runtime dependency
- annotate upstream patch origin

* Wed Aug 16 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.6.4-23
- fix license field

* Fri Aug 04 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.6.4-22
- adopt for Fedora
- hard-code ABI SONAME to avoid inadvertent breaks
- use SPDX identifier
- fix spurious executable permission
- drop redundant configure flag

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.6.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 25 2023 Sérgio Basto <sergio@serjux.com> - 0.6.4-20
- Remove option Werror was added by mistake

* Sat Feb 25 2023 Sérgio Basto <sergio@serjux.com> - 0.6.4-19
- Add last 8 commits from upstream

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.6.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.6.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Leigh Scott <leigh123linux@gmail.com> - 0.6.4-13
- Rebuilt for i686

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Hans de Goede <j.w.r.degoede@gmail.com> - 0.6.4-10
- Fix FTBFS on ppc64le

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.6.4-8
- Spec file clean-up

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 15 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 0.6.4-2
- Add patch from upstream to drop glib requires from the pkg-config file
  (rhbz#1109495)

* Thu Apr 10 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 0.6.4-1
- New upstream bugfix release 0.6.4

* Sun Apr 06 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 0.6.3-1
- New upstream bugfix release 0.6.3

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6.2-3
- Mass rebuilt for Fedora 19 Features

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jan 19 2011 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.2-1
- New upstream bugfix release 0.6.2

* Tue Jan 11 2011 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6.1-1
- New upstream bugfix release 0.6.1
- Fixes the use of the this reserved keyword in public headers (rf1596)

* Sun May 30 2010 Hans de Goede <j.w.r.degoede@hhs.nl> 0.6-1
- New upstream release 0.6
- Update URL (upstream has moved back to sf.net)

* Thu Feb 18 2010 Hans de Goede <j.w.r.degoede@hhs.nl> 0.5-1
- New upstream release 0.5 (rf1053)
- Fix some regressions introduced by upstream
- Add a bunch of home grown patches (I used to be part of upstream, but
  upstream has moved to launchpad), fixing several bugs and cleaning up
  the code left and right, all these are submitted upstream

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.4-4
- rebuild for new F11 features

* Thu Jul 24 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-3
- Rebuild for buildsys cflags issue

* Wed Jul 23 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-2
- Release bump for rpmfusion build

* Fri Dec 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4-1
- New upstream release 0.4
- Drop all patches (all upstreamed)

* Tue Dec 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-6
- Add a patch with various fixes from CVS
- Add a patch fixing a small bug I introduced in mmsh

* Sat Dec  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-5
- Add a patch from debian adding mms seeking support
- Add various fixes to Debians seeking patch
- Add self written mmsh seeking patch
- Add patch exporting some asf header info

* Wed Sep 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-4
- Add a patch from Debian fixing another crash
- Merge freshrpms spec into livna spec for rpmfusion:
- Set release to 4 to be higher as both livna and freshrpms latest release
- Update License tag for new Licensing Guidelines compliance
- Add pkgconfig Requires to -devel package
- Include some more doc files

* Wed Mar 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-3
- Add a patch fixing a crash (livna-bz 1463)

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.3-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3-1
- New upstream release 0.3
- This new release fixes CVS-2006-2200

* Sun Sep 24 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-2
- Rebuild for FC-6

* Sat Jul 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.2-1
- Minor specfile cleanups for livna submission.

* Mon Jun 12 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.2-0.gst.2
- new release

* Wed Jan 05 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1-0.gst.1
- initial package
