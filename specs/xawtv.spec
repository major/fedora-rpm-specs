%bcond_with	quicktime

Summary: TV applications for video4linux compliant devices
Name: xawtv
Version: 3.107
Release: 14%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://linuxtv.org/wiki/index.php/Xawtv

Source0: http://linuxtv.org/downloads/xawtv/%{name}-%{version}.tar.bz2
Patch0: xawtv-strsignal.patch
Patch1: xawtv-3.107-XawListChange.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: mesa-libGL-devel, libXaw-devel, libXext-devel
BuildRequires: libXft-devel, libXinerama-devel
BuildRequires: libXpm-devel, libXrandr-devel, libXt-devel
BuildRequires: libXxf86dga-devel, libXv-devel
BuildRequires: motif-devel
%{?with_quicktime:BuildRequires: libquicktime-devel}

BuildRequires: ncurses-devel, coreutils, libjpeg-devel, libpng-devel
BuildRequires: alsa-lib-devel
%ifnarch s390 s390x
BuildRequires: libdv-devel
%endif
BuildRequires: zvbi-devel, aalib-devel
BuildRequires: gpm-devel, slang-devel
BuildRequires: ImageMagick desktop-file-utils libappstream-glib
BuildRequires: libv4l-devel
BuildRequires: perl-interpreter

Requires: usermode xorg-x11-fonts-misc hicolor-icon-theme

%description
Xawtv is a simple xaw-based TV program which uses the bttv driver or
video4linux. Xawtv contains various command-line utilities for
grabbing images and .avi movies, for tuning in to TV stations, etc.
Xawtv also includes a grabber driver for vic.


%package motv
Summary: MoTV Analog Television Viewer
Requires: %{name} = %{version}-%{release}

%description motv
Motif UI version of the xawtv analog television viewer.


%package mtt
Summary: Analog TV Teletext viewing application
Requires: %{name} = %{version}-%{release}

%description mtt
Easy to use Motif UI for viewing analog tv teletext on video4linux devices
which support teletext.


%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -fcommon"
%configure %{!?_with_quicktime: --disable-quicktime}
make %{?_smp_mflags} verbose=yes


%install
make DESTDIR=$RPM_BUILD_ROOT SUID_ROOT="" install

%if %{without quicktime}
rm -f $RPM_BUILD_ROOT%{_bindir}/showqt
%endif

for i in 16x16 32x32 48x48; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$i/apps
  convert contrib/%{name}$i.xpm \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$i/apps/%{name}.png
done

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
for i in xawtv motv mtt; do
   desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
       contrib/$i.desktop
   install -p -m 0644 contrib/$i.*.xml $RPM_BUILD_ROOT%{_datadir}/appdata
   appstream-util validate-relax --nonet \
       $RPM_BUILD_ROOT%{_datadir}/appdata/$i.*.xml
done

#   v4l-conf  stuff

mkdir -p $RPM_BUILD_ROOT%{_sbindir} \
	$RPM_BUILD_ROOT%{_sysconfdir}/pam.d \
	$RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps \

cat >v4l-conf.pam <<!
#%%PAM-1.0
auth		sufficient	pam_rootok.so
auth		required	pam_console.so
account		required	pam_permit.so
session		required	pam_permit.so
session		optional	pam_xauth.so
!
install -m 0644 v4l-conf.pam $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/v4l-conf

cat >v4l-conf.apps <<!
SESSION=true
USER=root
PROGRAM=%{_sbindir}/v4l-conf
!
install -p -m 0644 v4l-conf.apps $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/v4l-conf

mv $RPM_BUILD_ROOT%{_bindir}/v4l-conf $RPM_BUILD_ROOT%{_sbindir}/
ln -s consolehelper $RPM_BUILD_ROOT%{_bindir}/v4l-conf

%files
%doc README TODO contrib/frequencies*
%license COPYING
%config(noreplace) %{_sysconfdir}/pam.d/v4l-conf
%config(noreplace) %{_sysconfdir}/security/console.apps/v4l-conf
%{_bindir}/*
%exclude %{_bindir}/motv
%exclude %{_bindir}/mtt
%{_sbindir}/*
%{_libdir}/xawtv
%{_datadir}/xawtv
%{_datadir}/X11/app-defaults/Xawtv
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man?/*
%exclude %{_mandir}/man1/motv.1*
%exclude %{_mandir}/man1/mtt.1*
%lang(es) %{_mandir}/es/*/*
%lang(fr) %{_mandir}/fr/*/*

%files motv
%{_bindir}/motv
%{_mandir}/man1/motv.1*
%{_datadir}/X11/app-defaults/MoTV*
%lang(de) %{_datadir}/X11/de_DE.UTF-8/app-defaults/MoTV*
%lang(fr) %{_datadir}/X11/fr_FR.UTF-8/app-defaults/MoTV*
%lang(it) %{_datadir}/X11/it_IT.UTF-8/app-defaults/MoTV*
%{_datadir}/appdata/motv.metainfo.xml
%{_datadir}/applications/motv.desktop

%files mtt
%{_bindir}/mtt
%{_mandir}/man1/mtt.1*
%{_datadir}/X11/app-defaults/mtt*
%{_datadir}/appdata/mtt.metainfo.xml
%{_datadir}/applications/mtt.desktop


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.107-13
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.107-11
- fix incompatible pointer types warnings (#2261796)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Jeff Law <law@redhta.com> - 3.107-2
- Use strsignal, not sys_siglist

* Sat May 16 2020 Mauro Carvalho Chehab <mchehab+samsung@kernel.org> - 3.107-1
- upgrade to version 3.107

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.106-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
- Use gcc -fcommon flag to build

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.106-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Mauro Carvalho Chehab <mchehab+samsung@kernel.org> - 3.106-1
- upgrade to version 3.106

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.105-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.105-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org> - 3.105-2
- cleanup FB console if an error happens

* Mon Jun 11 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org> - 3.105-1
- upgrade to version 3.105

* Fri Jun  1 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.103-15
- fix default console font for fbtv(1) (#1406549)

* Thu Mar 15 2018 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.103-14
- fileutils no more exists (#1556548)
- explicitly include sys/sysmacros.h

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.103-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.103-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.103-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.103-10
- Add BR: perl (Fix F26BFS).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.103-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 15 2016 Hans de Goede <hdegoede@redhat.com> - 3.103-8
- Bring in several bugfix patch from upstream
- Fix crash with saa7134 driver (rhbz#1305389)
- Use png instead of xpm for icons
- Add appdata
- Build motv and mtt now that we have a FOSS motif, put them in
  xawtv-motv resp xawtv-mtt sub-packages
- Remove changelog entries older then 10 years

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.103-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.103-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan  4 2015 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.103-5
- add workaround for kernels >= 3.16 (#1155784, patch from Stas Sergeev <stsp@list.ru>)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr  2 2013 Hans de Goede <hdegoede@redhat.com> 3.103-1
- New upstream version 3.103

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 3.101-7
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 3.101-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.101-5
- rebuild against new libjpeg

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.101-2
- Rebuild for new libpng

* Sun Jul  3 2011 Mauro Carvalho Chehab <mchehab@redhat.com> - 3.101-1
- update to Xawtv version 3.101: Adds support for alsa streams

* Wed Mar  2 2011 Mauro Carvalho Chehab <mchehab@redhat.com> - 3.100-1
- update to Xawtv version 3.100. Fixes control handling on xawtv.

* Thu Feb 17 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.99.rc6-1
- update to Xawtv version 3.99.rc6

* Thu Feb  3 2011 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.99.rc4-1
- update to Xawtv version 3.99.rc4

* Wed Feb  2 2011 Mauro Carvalho Chehab <mchehab@redhat.com> 3.99.rc3-1
- Update to Xawtv version 3.99.rc3
- Upstream applied some patches from Debian and from Fedora, making
  compilation more portable along different distros. It also incudes
  a couple minor fixes.

* Tue Feb  1 2011 Mauro Carvalho Chehab <mchehab@redhat.com> 3.99.rc2-1
- Update to Xawtv version 3.99.rc2
- All other patches from Fedora are now upstream

* Fri Jan 28 2011 Mauro Carvalho Chehab <mchehab@redhat.com> 3.99.rc1-1
- Update to Xawtv version 3.99.rc1
- Applied some fixes upstream fixing radio application and also some
  improvements from other patches that were found on Fedora.

* Thu Jan 27 2011 Mauro Carvalho Chehab <mchehab@redhat.com> 3.98-1
- Update to Xawtv version 3.98
- Removes V4L1 support and adds some new stuff

* Wed Nov 17 2010 Hans de Goede <hdegoede@redhat.com> 3.95-14
- Protect the exit code from being called twice. This fixes a double
  free error when the user tries to exit twice when xawtv is stuck (#608344)

* Fri Mar 12 2010 Hans de Goede <hdegoede@redhat.com> 3.95-13
- Fix xawtv not starting due to it not finding its fonts

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.95-12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Karsten Hopp <karsten@redhat.com> 3.95-11.1
- we have no libdv on mainframe, don't require that on s390(x)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.95-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-10
- fix some typos in manuals  (patch7, derived from Debian)
- fix recording from oss  (patch8, derived from Debian)
- allow scantv to use another card's input  (patch9, derived from Debian)
- some v4l2 code fixes (patch10, Hans de Goede <j.w.r.degoede@hhs.nl>)
- skip dga automatically when not available (patch11, Hans de Goede)
- specifying of bpl pitch for v4l-conf (patch12, Hans de Goede)
- drop drv0-v4l2-old.so driver (assume not needed anyway now)
- optional (default yes) build with libv4l wrapper library
  (patch100, Hans de Goede <j.w.r.degoede@hhs.nl>)

* Mon Jul 21 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-9
- rebuild for new gpm
- update strip patch

* Tue Feb 19 2008 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-8
- add gpm-devel and slang-devel to BuildRequires
- rebuild for GCC 4.3

* Thu Aug 30 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-7
- add patch for "open(2) call now is a macro" issue (#265081).

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.95-6
- Rebuild for selinux ppc32 issue.

* Fri Aug 17 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2+

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 3.95-5
- rebuild for toolchain bug

* Tue Jul 24 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-4
- don't assume v4l-conf as system config util (#249130)

* Tue Jun 26 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- drop X-Fedora category from desktop file

* Mon Jun 25 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-3
- add patch for use getpagesize() instead of a kernel headers macro

* Thu Jun 21 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-1
- spec file cleanup
- accepted for Fedora (review by Jason Tibbitts <tibbs@math.uh.edu>)

* Thu Mar  1 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 3.95-0
- upgrade to 3.95
- adapt for Fedora Extras, spec file cleanups
- add UTF-8 support for console apps
- drop tv-fonts package (you can use zvbi-fonts package for that purpose),
  bitstream-vera is now a default for "big" fullscreen-mode fonts.
- add desktop entry and icons
- add ALEVTD_REGION environment to change default teletext's region
