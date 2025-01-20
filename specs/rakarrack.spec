%global commit a6208406d94a1da978f435605072ee5caefe1491
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Summary: Audio effects processing rack for guitar
Name:    rakarrack
Version: 0.6.2
Release: 0.31.20150814git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     http://%{name}.sourceforge.net/
#S#ource0: http://downloads.sourceforge.net/%#{name}/%#{name}-%#{version}.tar.bz2
#S#ource0: http://rakarrack.git.sourceforge.net/git/gitweb.cgi?p=rakarrack/rakarrack;a=snapshot;h=47245c3fd30dc326fedd7cdae444ddcf0fd97490;sf=tgz
#S#ource0:  rakarrack-47245c3.tar.gz
# The snapshot download is created when accessed:
# https://sourceforge.net/p/rakarrack/git/ci/master/tree/
# Click: Download Snapshot, the download will then succeed for some hours.
Source0: http://sourceforge.net/code-snapshots/git/r/ra/rakarrack/git.git/rakarrack-git-%{commit}.zip
Patch1:  rakarrack-0.6.2.format-security.diff


Requires: hicolor-icon-theme

# mod of doc dir in configure.in requires autoconf/automake
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: automake
# not required (https://fedoraproject.org/wiki/Packaging:Guidelines#Exceptions_2)
# BuildRequires: gcc-c++ # just a reminder
BuildRequires: jack-audio-connection-kit-devel alsa-lib-devel alsa-utils
BuildRequires: libsndfile-devel
BuildRequires: libsamplerate-devel
BuildRequires: fltk-devel
BuildRequires: libXpm-devel libpng-devel libjpeg-devel
BuildRequires: fftw-devel
BuildRequires: desktop-file-utils


%description
Rakarrack is a basic rack of effects for guitar. 10 effects. Two EQ
(multi-band and parametric), distortion, overdrive, echo, chorus,
Flanger, Phaser, compression and Reverb. Real time processing. JACK
support. Online tuner. Bank & Preset management.

Most of the effects are based on the magnificent work done by Paul
Nasca Octavian in ZynAddSubFX synthesizer. The compressor is based on
ArtsCompressor of Matthias Kretzer & Stefen Westerfeld. The tuner was
adapted from Tuneit, a tuner in text mode created by Mario Lang. Paul
Nasca is our hero and a continuous inspiration


%prep
# for releases
#%#setup -q -n %#{name}-%#{version}
# for git snapshot
%setup -q -n %{name}-git-%{commit}

%patch -P1 -p1 -b .format-security

# Fix spurious-executable-perm
find ./src/ -type f -perm /a=x -name "*" -exec chmod a-x {} \;
#find -type f -exec chmod a-x {} src\;
#-exec chmod a-x {} src\;


%{__sed} -i 's/Icon=icono_rakarrack_128x128/Icon=rakarrack/' data/%{name}.desktop
%{__sed} -i 's/Guitar Effects Processor/Real-time audio effects processing rack for guitar/' data/%{name}.desktop
echo "GenericName=Digital audio effects processor" >> data/%{name}.desktop
echo "Version=1.0" >> data/%{name}.desktop


%build
./autogen.sh

%define optimise ""
# ensure the builder arch does not influence the build 
%ifarch x86_64
  %define optimise "--enable-sse2"
%endif
%ifarch %{ix86}
  %define optimise "--enable-sse"
%endif  
 
%configure --enable-docdir=yes --docdir=%{_pkgdocdir} %{optimise}
  
# if DFortifySource is not passed to compile, try del smp_mflags
%{__make} %{?_smp_mflags}


%install
%{__make} DESTDIR=%{buildroot} install

# move icons to the proper freedesktop location
for dim in 32x32 64x64 128x128; do
  %{__mkdir} -p %{buildroot}%{_datadir}/icons/hicolor/$dim/apps
  %{__mv} %{buildroot}%{_datadir}/pixmaps/icono_%{name}_$dim.png \
      %{buildroot}%{_datadir}/icons/hicolor/$dim/apps/%{name}.png
done

# extra desktop file categories are allowed if prepended with X-
BASE="X-Fedora AudioVideo"
XTRA="X-DigitalProcessing X-Jack"
MIXER="Mixer"

%{__mkdir} -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor "" \
  `for c in ${BASE} ${XTRA} ${MIXER}; do echo "--add-category $c " ; done` \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/rakarrack.desktop

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/PACKAGERS.README
%{_bindir}/%{name}
%{_bindir}/rakconvert
%{_bindir}/rakgit2new
%{_bindir}/rakverb
%{_bindir}/rakverb2
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.31.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.6.2-0.30.20150814gita620840
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.29.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.28.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.27.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.26.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.25.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.24.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.23.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.22.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.21.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.20.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.19.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.18.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.17.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.16.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.15.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.2-0.14.20150814gita620840
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.13.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.12.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.11.20150814gita620840
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild


* Sun Mar 13 2016 David Timms <iinet.net.au @ dtimms> - 0.6.2-0.10.20150814gita620840
- Update to current git snapshot from 2015-08-14.
- Fix spurious executable permissions on src.rpm files using chmod.
- Remove redundant files defattr setting.
- Add comment indicating the need to access the git snapshot download page, 
  before trying the download link.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-0.9.20140723git7dba0c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-0.8.20140723git7dba0c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.2-0.7.20140723git7dba0c4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 0.6.2-0.6.20140723git
- rebuild (fltk)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-0.5.20140723git7dba0c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 David Timms <iinet.net.au @ dtimms> - 0.6.2-0.4.20140723git7dba0c4
- Update to current git snapshot from 2014-07-23.
- Rebase format function security patch.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-0.3.20130414gitb358630
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 12 2014 David Timms <iinet.net.au @ dtimms> - 0.6.2-0.2.20130414gitb358630
- Apply patch for format function security.

* Mon May 12 2014 David Timms <iinet.net.au @ dtimms> - 0.6.2-0.1.20130414gitb358630
- Update to current git snapshot from 2013-04-14

* Thu Aug  8 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-11.git47245c3
- Fix build with unversioned %%{_docdir_fmt} (#993195).
- Fix bogus dates in %%changelog.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-10.git47245c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-9.git47245c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-8.git47245c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Dennis Gilmore <dennis@ausil.us> - 0.6.1-7.git47245c3
- fix building on non x86 arches

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6.git47245c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 13 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.6.1-5.git47245c3
- Rebuild for fltk-1.3.0.

* Tue May 10 2011 David Timms <iinet.net.au @ dtimms> - 0.6.1-4.git47245c3
- use compile optimisation flags to avoid sse2 instructions on pentiumIII

* Fri Apr 29 2011 David Timms <iinet.net.au @ dtimms> - 0.6.1-3.git47245c3
- update to git snapshot to diagnose bug 700183

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 David Timms <iinet.net.au @ dtimms> - 0.6.1-2
- add upstream patch to improve user experience when jack quits

* Mon Dec 13 2010 David Timms <iinet.net.au @ dtimms> - 0.6.1-1
- update to 0.6.1

* Wed Jun 23 2010 David Timms <iinet.net.au @ dtimms> - 0.5.8-2
- add new --enable-docdir to configure
- del old method used to use standard doc directories

* Wed Jun 23 2010 David Timms <iinet.net.au @ dtimms> - 0.5.8-1
- update to 0.5.8 "Equinox" with many new features.

* Tue Jun 22 2010 David Timms <iinet.net.au @ dtimms> - 0.4.2-2.1
- remove obsolete patches
- add below patch to the tag

* Sun Apr  4 2010 David Timms <iinet.net.au @ dtimms> - 0.4.2-2
- add patch to explicitly link to libX11 as ld changes now require

* Sat Feb 27 2010 David Timms <iinet.net.au @ dtimms> - 0.4.2-1
- update to 0.4.2
- del upstreamed rakarrack-ChN-buffer-oveflow-fix.diff

* Thu Jan  7 2010 David Timms <iinet.net.au @ dtimms> - 0.3.0-5
- add patch for buffer overflow captured by fedora compile flags
- add BR fftw-devel so that new upstream configure.in will build
- fix being built without proper fedora flags and
      being built with empty debuginfo using patch to current
      upstream configure.in
- add BR automake so that adjusts to configure.in to fix Help|
      Help Contents,License pointing to non-versioned .../doc/ dir succeed
- move edit of configure.in to prep

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.3.0-4
- Update desktop file according to F-12 FedoraStudio feature
- Update scriptlets

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 David Timms <iinet.net.au @ dtimms> - 0.3.0-1
- update to upstream release

* Thu Oct 16 2008 David Timms <iinet.net.au @ dtimms> - 0.2.0-5
- del debug cruft left in the spec while trying to solve issues

* Tue Oct 14 2008 David Timms <iinet.net.au @ dtimms> - 0.2.0-4
- move non-install commands to setup
- fix configure .ini so that standard help path will be used

* Sun Oct 12 2008 David Timms <iinet.net.au @ dtimms> - 0.2.0-3
- don't exclude the original .desktop file

* Mon Oct 06 2008 David Timms <iinet.net.au @ dtimms> - 0.2.0-2
- mod icon names to be appname.png to fit with fallback desktop spec
- replace rakarrack with name macro
- mod .desktop via sed and cat, rather than additional Source file
- add .desktop extra categories using the desktop-file-install utils
 
* Sun Oct 05 2008 David Timms <iinet.net.au @ dtimms> - 0.2.0-1
- simplify the icon installation by looping through dimensions
- fix missing ; on category line in desktop file
- don't rename the icons since it confuses desktop-file-install
- fix spelling in description
- fix help menu contents not being displayed due to marking help files doc

* Fri Aug 01 2008 David Timms <iinet.net.au @ dtimms> - 0.2.0-0.2
- don't package the included .desktop file to solve getting two menu icons

* Sat Jul 19 2008 David Timms <iinet.net.au @ dtimms> - 0.2.0-0.1
- update to 0.2.0
- mod spec to meet Fedora packaging guidelines

* Fri May 23 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> - 0.1.2-1
- initial build.
