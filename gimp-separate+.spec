%global        gimpver          2.0
%global        _gimppluginsdir  %{_libdir}/gimp/%{gimpver}/plug-ins
%global        appdata_dir      %{_datadir}/appdata

Name:          gimp-separate+
Version:       0.5.8
Release:       34%{?dist}
Summary:       Rudimentary CMYK support for The GIMP
URL:           http://cue.yellowmagic.info/softwares/separate.html
Source0:       http://iij.dl.sourceforge.jp/separate-plus/47873/separate+-%{version}.zip
Source1:       %{name}.metainfo.xml
Patch0:        separate+-0.5.8-lcms2.patch
Patch1:        gimp-separate+-c99.patch
# The entire source code is GPLv2+ except srgb_profile.h which is MIT/X11 (BSD like)
License:       GPLv2+ and MIT

BuildRequires: gcc
BuildRequires: gettext
BuildRequires: gimp-devel
BuildRequires: lcms2-devel
BuildRequires: libtiff-devel
BuildRequires: libjpeg-devel
BuildRequires: make

Provides:      gimp-cmyk = %{version}-%{release}

Requires:      gimp%{?_isa} >= %{gimpver}


%description
Separate+ is a GIMP plug-in that convert an RGB image to CMYK format.

%prep

%setup -q -n separate+-%{version}
%patch0 -p1
%patch1 -p1

%build
# XXX to fix "/usr/bin/ld: psd.o: undefined reference to symbol
# 'ceil@@GLIBC_2.2.5'" we hijack JPEG_LIB to pass additional stuff
%{__make} %{?_smp_mflags} \
    JPEG_LIB="-ljpeg -lm"

%install
install -pDm755 separate \
   %{buildroot}%{_gimppluginsdir}/separate
install -pDm755 separate_import \
   %{buildroot}%{_gimppluginsdir}/separate_import 
install -pDm755 icc_colorspace \
   %{buildroot}%{_gimppluginsdir}/icc_colorspace 

# Install AppData.
mkdir -p %{buildroot}%{appdata_dir}
install -m 644 %{SOURCE1} %{buildroot}%{appdata_dir}


%files
%{_gimppluginsdir}/separate
%{_gimppluginsdir}/separate_import
%{_gimppluginsdir}/icc_colorspace
%doc COPYING README README_ICC_COLORSPACE
%{appdata_dir}/%{name}.metainfo.xml


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Florian Weimer <fweimer@redhat.com> - 0.5.8-33
- Port to C99 (#2151332)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 Than Ngo <than@redhat.com> - 0.5.8-26
- built with lcms2 (lcms is dropped in fedora > 31)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Peter Hanecak <hany@hany.sk> - 0.5.8-22
- Added BuildRequires: gcc
  (https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 16 2016 Peter Hanecak <hany@hany.sk> - 0.5.8-16
- Updated AppStream metadata file (rhbz#1316299): updated homepage URL and
  added bugtracker URL

* Thu Feb  4 2016 Peter Hanecak <hany@hany.sk> - 0.5.8-15
- Added metainfo.xml from Luya Tshimbalanga <luya@fedoraproject.org>

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec  5 2013 Peter Hanecak <hany@hany.sk> 0.5.8-10
- %%{gimpver} changed from 2.8.0 to 2.0 to fix bug #1038024
 
* Mon Nov 18 2013 Peter Hanecak <hany@hany.sk> 0.5.8-9
- gimp%%{?_isa} used in requires (see comment #34 - still bug #913289)
- shortened summary (see comment #35)

* Tue Sep  3 2013 Peter Hanecak <hany@hany.sk> 0.5.8-8
- bundled sRGB_type2.icc not included in the package as Fedora ships other
  profiles (see https://bugzilla.redhat.com/show_bug.cgi?id=913289#c30)

* Tue Aug 27 2013 Peter Hanecak <hany@hany.sk> 0.5.8-7
- trimmed build requires as suggested
  in https://bugzilla.redhat.com/show_bug.cgi?id=913289#c24

* Tue Aug  6 2013 Peter Hanecak <hany@hany.sk> 0.5.8-6
- removed EPEL related stuff and -pDm755 used in install as sugested in
  https://bugzilla.redhat.com/show_bug.cgi?id=913289#c18
- to preserve the timestamp also for sRGB_type2.icc, install used instead of cp
- fixed another mixed use of spaces and tabs

* Mon Aug  5 2013 Peter Hanecak <hany@hany.sk> 0.5.8-5
- version provided for 'provides: gimp-cmyk' (see
  https://bugzilla.redhat.com/show_bug.cgi?id=913289#c10)

* Mon Aug  5 2013 Peter Hanecak <hany@hany.sk> 0.5.8-4
- fixed mixed used of spaces and tabs (see
  https://bugzilla.redhat.com/show_bug.cgi?id=913289#c10)

* Wed Apr 17 2013 Peter Hanecak <hany@hany.sk> 0.5.8-3
- another set of updates to address review comments
  (https://bugzilla.redhat.com/show_bug.cgi?id=913289#c4)

* Thu Feb 21 2013 Peter Hanecak <hany@hany.sk> 0.5.8-2
- updates to address review comments
  (https://bugzilla.redhat.com/show_bug.cgi?id=913289#c1)

* Mon Feb 11 2013 Peter Hanecak <hany@hany.sk> 0.5.8-1
- initial spec using the one created by Tiziana Ferro <tiziana.ferro@email.it>
