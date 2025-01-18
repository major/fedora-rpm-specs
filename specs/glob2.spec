Name:           glob2
Version:        0.9.4.4
Release:        70%{?dist}
Summary:        An innovative RTS game

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://globulation2.org/
Source0:        http://dl.sv.nongnu.org/releases/%{name}/0.9.4/%{name}-%{version}.tar.gz
#Source3:        glob2.desktop
#patch0 fixes polish diacritics
#Patch0:         glob2-texts.pl.patch
#Patch2:         glob2-gcc43.patch
Patch3:         glob2-0.9.4.1-gcc44.patch
# https://savannah.nongnu.org/bugs/index.php?39593
Patch4:         glob2_SConstruct.patch
Patch5:		glob2-private.patch
Patch6:		glob2-fix_missing_return_in_nonvoid_functions.patch
Patch7:		glob2-iostream.patch
# https://bitbucket.org/giszmo/glob2/pull-requests/7
Patch8:		glob2-gcc7.patch
Patch9:		glob2-python3.patch
Patch10:	glob2-scons3.patch
Patch11:	glob2-fix-tabs.patch
Patch12:	glob2-bool.patch

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libvorbis-devel
BuildRequires:  portaudio-devel
BuildRequires:  python3
BuildRequires:  python3-scons
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  SDL-devel
BuildRequires:  speex-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++

# Handle font moves more automatically
%global fonts font(dejavusans)
BuildRequires: fontconfig %{fonts}
Requires: %{fonts}

Requires:       hicolor-icon-theme

%description
Globulation 2 brings a new type of gameplay to RTS games. The player chooses
the number of units to assign to various tasks, and the units do their best to
satisfy the requests. This allows players to manage more units and focus on
strategy rather than individual unit's jobs. Globulation 2 also features AI
allowing single-player games or any possible combination of human-computer
teams. Also included is a scripting language for versatile gameplay or
tutorials and an integrated map editor. Globulation2 can be played in single
player mode, through your local network, or over the Internet with Ysagoon
Online Gaming (or YOG for short).


%prep
%setup -q
#%patch 0 -p0
#%patch 2 -p0
%patch 3 -p0
%patch 4 -p1
%patch 5 -p1
%patch 6 -p0
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1 -b.python3
%patch 10 -p1 -b.scons3
%patch 11 -p1 -b.fixtabs
%patch 12 -p1 -b.bool

sed -i -e '3d' -e '12d' data/glob2.desktop
sed -i s#"Icon=glob2-icon-48x48"#"Icon=glob2"# data/glob2.desktop

chmod -x campaigns/Tutorial_Campaign.txt
sed -i 's/\r//' campaigns/Tutorial_Campaign.txt

%build
scons %{?_smp_mflags} INSTALLDIR=$RPM_BUILD_ROOT%{_datadir} BINDIR=$RPM_BUILD_ROOT%{_bindir} DATADIR=%{_datadir} CXXFLAGS="%{optflags}" --portaudio=true

%install
scons install --portaudio=true

# Use the dejavu-sans-fonts package to supply the neeeded fonts
ln -f -s $(fc-match -f "%{file}" "sans") $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/sans.ttf

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/
cp -p data/icons/glob2-icon-64x64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/glob2.png

for f in 128x128 16x16 24x24 32x32 48x48; do
mv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$f/apps/glob2-icon-$f.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$f/apps/glob2.png
done
rm -rf $RPM_BUILD_ROOT%{_datadir}/glob2/data/icons
find $RPM_BUILD_ROOT%{_datadir} -name *~* -exec rm -rf {} \;

desktop-file-install                                    \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --remove-category=Application                   \
        --delete-original                               \
        $RPM_BUILD_ROOT%{_datadir}/applications/glob2.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://savannah.nongnu.org/bugs/?43293
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">glob2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>real time strategy game with globs</summary>
  <description>
    <p>
      Globulation 2 is a real time strategy (RTS) game where you use three
      types of globs: workers, scouts, and warriors to wage war on computer
      controlled communites of other
      globs.
      Globulation is unique from other RTS games in that it removes a lot of the
      micromanagement from the gameplay.
      You cannot control the globs directly, only place buildings and let the
      globs do what they do best.
    </p>
  </description>
  <url type="homepage">http://globulation2.org/</url>
  <screenshots>
    <screenshot type="default">http://globulation2.org/images/9/93/Beta3-Battle.jpg</screenshot>
    <screenshot>http://globulation2.org/images/5/5a/Beta2_MoreAttackingEnemy.jpg</screenshot>
    <screenshot>http://globulation2.org/images/6/6a/Beta2_ParticleEffects.jpg</screenshot>
  </screenshots>
</application>
EOF



%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.4.4-69
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-68
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 06 2024 Bruno Wolff III <bruno@wolff.to> - 0.9.4.4-67
- scons-3 appears to have been dropped

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-64
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-62
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.9.4.4-59
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-57
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-54
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-53
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-51
- Rebuilt for Boost 1.73

* Wed May 13 2020 Bruno Wolff III <bruno@wolff.to> 0.9.4.4-50
- Handle font location automatically

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 josef radinger <cheese@nosuchhost.net> - 0.9.4.4-48
- add patch for scons (remove Options Class)
- add BuildRequires on gcc-c++
- switch to python3
- fix tabs (glob2-fix-tabs.patch)
- add patch12 

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-46
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.4.4-44
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-42
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.4.4-41
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-38
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-37
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-34
- Rebuilt for Boost 1.63 and patched for GCC 7

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-32
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.9.4.4-31
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-30
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.9.4.4-29
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.4.4-27
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.4.4-26
- Add an AppData file for the software center

* Sat Feb 7 2015 josef radinger <cheese@nosuchhost.net> - 0.9.4.4-25
- adding glob2-fix_missing_return_in_nonvoid_functions.patch, taken from opensuse
- remove extension from Icon in desktop-file
- add glob2-iostream.patch

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.9.4.4-24
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 josef radinger <cheese@nosuchhost.net> - 0.9.4.4-22
- fix compile (glob2-private.patch)

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.9.4.4-21
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 Petr Machata <pmachata@redhat.com> - 0.9.4.4-19
- Rebuild for boost 1.54.0
- Move glob2_SConstruct.patch from side cache to GIT.  Fix apparent
  error in detection of boost_date_time.  Decouple detection of
  boost_system from detection of boost_thread.

* Sun Feb 24 2013 Bruno Wolff III <bruno@wolff.to> - 0.9.4.4-18
- Remove vendor prefix from desktop file

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.4.4-17
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.4.4-16
- Rebuild for Boost-1.53.0

* Sun Aug 26 2012 josef radinger <cheese@nosuchhost.net> - 0.9.4.4-15
- just fix mail in changelog

* Sun Aug 26 2012 josef radinger <cheese@nosuchhost.net> - 0.9.4.4-14
- really fix linking against boost_system-mt, quick and dirty
- add Buildrequires for portaudio

* Sat Aug 11 2012 josef radinger <cheese@nosuchhost.net> - 0.9.4.4-13
- Rebuilt for boost-update

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-11
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.4.4-9
- Rebuild for boost soname bump

* Fri Jul 22 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.4.4-8
- Rebuild for boost soname bump to 1.47 in rawhide.

* Wed Apr 06 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.4.4-7
- Rebuild for boost soname bump to 1.46.1 in rawhide.

* Wed Mar 16 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.4.4-6
- Rebuild for boost soname reversion.

* Sun Mar 13 2011 Bruno Wolff III <bruno@wolff.to> - 0.9.4.4-5
- Use the dejavu-sans-fonts package instead of included fonts - bug 477390

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 0.9.4.4-3
- rebuild for new boost

* Sun Aug 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.9.4.4-2
- rebuild for new libboost

* Sat May 01 2010 Thomas Janssen <thomasj@fedoraproject.org> 0.9.4.4-1
- beta4 hopefully fixes some crashes

* Fri Jan 22 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0.9.4-1-3
- Rebuild for Boost soname bump

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Rafał Psota <rafalzaq@gmail.com> - 0.9.4.1-1
- update to 0.9.4.1
* Thu Dec 18 2008 Petr Machata <pmachata@redhat.com> - 0.9.3-2
- rebuild for new boost
* Sun May 04 2008 Rafał Psota <rafalzaq@gmail.com> - 0.9.3-1
- update to 0.9.3
* Thu Feb 14 2008 Rafał Psota <rafalzaq@gmail.com> - 0.9.1-3
- gcc 4.3 patch
* Sun Sep 16 2007 Rafał Psota <rafalzaq@gmail.com> - 0.9.1-2
- new install method
* Tue Sep 04 2007 Rafał Psota <rafalzaq@gmail.com> - 0.9.1-1
- update to 0.9.1
* Sat Aug 25 2007 Rafał Psota <rafalzaq@gmail.com> - 0.8.21-4
- BuildID rebuild
* Mon Aug 20 2007 Rafał Psota <rafalzaq@gmail.com> - 0.8.21-3
- License tag update
* Tue May 22 2007 Rafał Psota <rafalzaq@gmail.com> - 0.8.21-2
- fix Source0
* Sun May 20 2007 Rafał Psota <rafalzaq@gmail.com> - 0.8.21-1
- back to 0.8.21
- merge data subpackage to core package
* Fri May 04 2007 Rafał Psota <rafalzaq@gmail.com> - 0.8.23-1
- Update to 0.8.23
* Mon Jan 29 2007 Rafał Psota <rafalzaq@gmail.com> - 0.8.21-2
- RPM_OPT_FLAGS fix
* Wed Jan 24 2007 Rafał Psota <rafalzaq@gmail.com> - 0.8.21-1
- Initial release
