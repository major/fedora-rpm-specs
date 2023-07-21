Name:           easystroke
Version:        0.6.0
Release:        42%{?dist}
Summary:        Gesture-recognition application for X11
License:        ISC
URL:            https://github.com/thjaeger/easystroke
Source0:        http://downloads.sourceforge.net/easystroke/%{name}-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/thjaeger/easystroke/master/easystroke.appdata.xml
Patch0:		easystroke-0.6.0-fix-desktop-file.patch
# https://github.com/thjaeger/easystroke/commit/d14b2740bf3b0ec867d7a0abe4e1f64fb6687aba
Patch1:		easystroke-0.6.0-gnome3-fix.patch
# Fix build with lambda (now that sigc++ dropped sigc::group)
Patch2:		easystroke-0.6.0-lambda.patch
# https://github.com/thjaeger/easystroke/pull/8
Patch3:		easystroke-0.6.0-abs.patch
# https://github.com/thjaeger/easystroke/pull/10/commits/140b9cae66ba874bf0994eea71210baf417a136e
Patch4:		easystroke-0.6.0-iconfix.patch
# https://github.com/thjaeger/easystroke/commit/5388934e722308cd314d65e362ddfaf6e5ab6c94
Patch5:		easystroke-0.6.0-sendfix.patch
# https://github.com/thjaeger/easystroke/commit/7bda4bd9c705413598ee9b534884bc7f23704932
Patch6:		easystroke-0.6.0-signal-handler-fix.patch
# https://github.com/thjaeger/easystroke/commit/040ba64e8c7dbf5b270aa3e7145e625ccb8d49c8
Patch7:		easystroke-0.6.0-unused.patch
# https://github.com/thjaeger/easystroke/commit/30a879fc81c4093c0a0c66116042079f11d246ab
Patch8:		easystroke-0.6.0-c11.patch
# https://github.com/thjaeger/easystroke/commit/cdf1d1a73c255c198ff0356472bb0ea76937ae76
Patch9:		easystroke-0.6.0-fix-no-select-crash.patch
# https://github.com/thjaeger/easystroke/pull/6
Patch10:	easystroke-0.6.0-g_spawn_async.patch
# https://github.com/thjaeger/easystroke/pull/9/commits/5f6885c59d1366e28317c9553c2e406fbd6569f9
Patch11:	easystroke-0.6.0-no-absolutes.patch
# https://github.com/thjaeger/easystroke/pull/9/commits/c328ef36d7d85e899fa1ccbc9f11aa1b2317f7bc
Patch12:	easystroke-0.6.0-scorefix.patch
# https://aur.archlinux.org/cgit/aur.git/tree/add-toggle-option.patch?h=easystroke-git
Patch13:	easystroke-0.6.0-toggle.patch
# https://aur.archlinux.org/cgit/aur.git/tree/dont-ignore-xshape-when-saving.patch?h=easystroke-git
Patch14:	easystroke-0.6.0-dont-ignore-xshape-when-saving.patch
# https://github.com/debuggerx01/easystroke/commit/31023e7a253bde9fabb273a294fc3d0837dcaf96
Patch15:	easystroke-0.6.0-missingcase.patch
# https://github.com/tzraeq/easystroke/commit/1c0a0609489035805fedfe88fe97542d2aa37bf5
Patch16:	easystroke-0.6.0-duplicate-actions.patch
# Replace gdk_screen_width/gdk_screen_height
Patch17:	easystroke-0.6.0-workarea.patch
# fix private handling
# Work in progress
Patch18:	easystroke-0.6.0-privatefix.patch

BuildRequires:  gcc-c++
BuildRequires:  gtkmm30-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  boost-devel
BuildRequires:  libXtst-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  xorg-x11-server-devel
BuildRequires:	libappstream-glib
BuildRequires: make
ExcludeArch:    s390 s390x

%description
Easystroke is a gesture-recognition application for X11. Gestures or strokes 
are movements that you make with you mouse (or your pen, finger etc.) while 
holding down a specific mouse button. Easystroke will execute certain actions 
if it recognizes the stroke; currently easystroke can emulate key presses, 
execute shell commands, hold down modifiers and emulate a scroll wheel. 

%prep
%setup -q
%patch0 -p1 -b .fixme
%patch1 -p1 -b .gnome3fix
%patch2 -p1 -b .lambda
%patch3 -p1 -b .abs
%patch4 -p1 -b .iconfix
%patch5 -p1 -b .sendfix
%patch6 -p1 -b .signal-handler-fix
%patch7 -p1 -b .unused
%patch8 -p1 -b .c11
%patch9 -p1 -b .fix-no-select-crash
%patch10 -p1 -b .g_spawn_async
%patch11 -p1 -b .no-absolutes
%patch12 -p1 -b .scorefix
%patch13 -p1 -b .toggle
%patch14 -p1 -b .dont-ignore-xshape-when-saving
%patch15 -p1 -b .missingcase
%patch16 -p1 -b .duplicate
%patch17 -p1 -b .workarea
# %%patch18 -p1 -b .privatefix
cp -a %{SOURCE1} .

# Resolve debuginfo
sed -i 's|install -Ds|install -D|' Makefile
# Preserve timestamps:
sed -i 's|install |install -p |' Makefile
# Use true system path
sed -i 's|/usr/local|/usr|g' Makefile

%build
make  %{?_smp_mflags} CXX="g++ %{optflags}" CC="gcc -std=c99 %{optflags}"

%install
make install PREFIX="%{_prefix}" DESTDIR=$RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_datadir}/appdata
cp -a %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files -f %{name}.lang
%doc changelog LICENSE 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-41
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.6.0-38
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-36
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-33
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-31
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 2019 Tom Callaway <spot@fedoraproject.org> - 0.6.0-29
- merge a big old pile of patches from various places, thanks to revast on github

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-26
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-23
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.0-22
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-19
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-18
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-16
- Rebuilt for Boost 1.63 and patched for GCC 7.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 1 2016 Tom Callaway <spot@fedoraproject.org> - 0.6.0-14
- rebuild for boost
- fix build against sigc++ with lambda (and no sigc::group)
- update URL

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.0-13
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.6.0-11
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.6.0-8
- Rebuild for boost 1.57.0

* Tue Dec  9 2014 Tom Callaway <spot@fedoraproject.org> - 0.6.0-7
- add appdata

* Tue Dec  2 2014 Tom Callaway <spot@fedoraproject.org> - 0.6.0-6
- fix black squares issue on gnome 3 (bz1084308)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.6.0-3
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.6.0-2
- rebuild for boost 1.55.0

* Tue Nov 19 2013 Tom Callaway <spot@fedoraproject.org> - 0.6.0-1
- update to 0.6.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.5.5.1-7
- Rebuild for boost 1.54.0

* Mon Mar 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.5.1-6
- Drop xorg sdk dependency as it's been provided by devel since F-9

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.5.5.1-5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.5.5.1-4
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 0.5.5.1-3
- Rebuilt for new boost

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 14 2012 Tom Callaway <spot@fedoraproject.org> - 0.5.5.1-1
- update to 0.5.5.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.4-3
- Rebuild for new libpng

* Mon Aug  8 2011 Tom Callaway <spot@fedoraproject.org> - 0.5.4-2
- rebuild against new boost
- cleanup spec file

* Thu Apr 21 2011 Tom Callaway <spot@fedoraproject.org> - 0.5.4-1
- update to 0.5.4

* Sun Apr 17 2011 Kalev Lember <kalev@smartlink.ee> - 0.5.3-5
- Rebuilt for boost 1.46.1 soname bump

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 02 2010 Dan Horák <dan[at]danny.cz> - 0.5.3-3
- no graphics on s390(x)

* Wed Aug 04 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.3-2
- Rebuild for Boost soname bump
- Update spec to match current guidelines

* Wed Mar 17 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.5.3-1
- update to 0.5.3
- drop timing patch (upstreamed)
- add patch to fix indirect linking issue

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.5.2-2
- Rebuild for Boost soname bump

* Wed Jan 13 2010 Zarko Pintar <zarko.pintar@gmail.com> - 0.5.2-1
- new version for XServer 1.7 and up

* Wed Sep 09 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.9-1
- new version

* Wed Jun 24 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.6-1
- new version

* Wed Jun 03 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.5-1
- new version
- added gcc4.3.0 patch and resolve optflags 

* Mon Jun 01 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.4-3
- spec cleaning

* Fri May 29 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.4-2
- resolved debuginfo

* Wed May 27 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.4-1
- initial release
