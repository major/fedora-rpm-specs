# If you want to skip building the firmware subpackage, define the macro
# _without_firmware to 1. This is not the actual firmware itself 
# (see alsa-firmware), it is some complementary tools.
# Do *NOT* set it to zero or have a commented out define here, or it will not
# work. (RPM spec file voodoo)
%if 0%{?rhel}
%global _without_tools 1
%endif

%ifarch ppc ppc64
# sb16_csp doesn't build on PPC; see bug #219010
%{?!_without_tools:     %global builddirstools as10k1 echomixer envy24control hdspconf hdspmixer hwmixvolume rmedigicontrol sbiload sscape_ctl us428control hda-verb hdajackretask hdajacksensetest }
%else
%{?!_without_tools:     %global builddirstools as10k1 echomixer envy24control hdspconf hdspmixer hwmixvolume rmedigicontrol sbiload sb16_csp sscape_ctl us428control hda-verb hdajackretask hdajacksensetest }
%endif

%{?!_without_firmware:  %global builddirsfirmw hdsploader mixartloader usx2yloader vxloader }

%{?!_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Note that the Version is intended to coincide with the version of ALSA
# included with the Fedora kernel, rather than necessarily the very latest
# upstream version of alsa-tools

Summary:        Specialist tools for ALSA
Name:           alsa-tools
Version:        1.2.11
Release:        6%{?dist}

# Checked at least one source file from all the sub-projects contained in
# the source tarball and they are consistent GPLv2+ - TJ 2007-11-15
License:        GPL-2.0-or-later
URL:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/tools/%{name}-%{version}.tar.bz2

Source1:        90-alsa-tools-firmware.rules

Patch1:         hwmixvolume-python.patch
Patch2:         gcc-fixes.patch

BuildRequires:  gcc gcc-c++
BuildRequires:  alsa-lib-devel >= %{version}
%if 0%{!?_without_tools:1}
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  fltk-devel
BuildRequires: make
Buildrequires:  desktop-file-utils
Requires:       xorg-x11-fonts-misc
# Needed for hwmixvolume
Requires:       python3-alsa
%endif

%description
This package contains several specialist tools for use with ALSA, including
a number of programs that provide access to special hardware facilities on
certain sound cards.

* as10k1 - AS10k1 Assembler
%ifnarch ppc ppc64
* cspctl - Sound Blaster 16 ASP/CSP control program
%endif
* echomixer - Mixer for Echo Audio (indigo) devices
* envy24control - Control tool for Envy24 (ice1712) based soundcards
* hdspmixer - Mixer for the RME Hammerfall DSP cards
* hwmixvolume - Control the volume of individual streams on sound cards that
  use hardware mixing
* rmedigicontrol - Control panel for RME Hammerfall cards
* sbiload - An OPL2/3 FM instrument loader for ALSA sequencer
* sscape_ctl - ALSA SoundScape control utility
* us428control - Control tool for Tascam 428
* hda-verb - Direct HDA codec access
* hdajackretask - Reassign the I/O jacks on the HDA hardware
* hdajacksensetest - The sense test for the I/O jacks on the HDA hardware


%package firmware
Summary:        ALSA tools for uploading firmware to some soundcards
Requires:       udev
Requires:       alsa-firmware
Requires:       fxload


%description firmware
This package contains tools for flashing firmware into certain sound cards.
The following tools are available:

* hdsploader   - for RME Hammerfall DSP cards
* mixartloader - for Digigram miXart soundcards
* vxloader     - for Digigram VX soundcards
* usx2yloader  - second phase firmware loader for Tascam USX2Y USB soundcards


%prep
%setup -q -n %{name}-%{version}
%patch -P 1 -p1 -b .hwmixvolume-python
%patch -P 2 -p1 -b .gcc-fixes

%build
mv seq/sbiload . ; rm -rf seq
for i in %{?builddirstools:%builddirstools} %{?builddirsfirmw:%builddirsfirmw}
do
  cd $i ; %configure
  make %{?_smp_mflags} || exit 1
  cd ..
done

%install
mkdir -p %{buildroot}%{_datadir}/{pixmaps,applications}

for i in %{?builddirstools:%builddirstools} %{?builddirsfirmw:%builddirsfirmw}
do
  case $i in
    usx2yloader)
      (cd $i ; %make_install hotplugdir=/usr/lib/udev) || exit 1
      ;;
    *)
      (cd $i ; %make_install) || exit 1
      ;;
   esac
   if [[ -s "${i}"/README ]]
   then
      if [[ ! -d "%{buildroot}%{_pkgdocdir}/${i}" ]]
      then
         mkdir -p "%{buildroot}%{_pkgdocdir}/${i}"
      fi
      cp "${i}"/README "%{buildroot}%{_pkgdocdir}/${i}"
   fi
   if [[ -s "${i}"/COPYING ]]
   then
      if [[ ! -d "%{buildroot}%{_pkgdocdir}/${i}" ]]
      then
         mkdir -p "%{buildroot}%{_pkgdocdir}/${i}"
      fi
      cp "${i}"/COPYING "%{buildroot}%{_pkgdocdir}/${i}"
   fi
   if [[ -s %{buildroot}%{_datadir}/applications/${i}.desktop ]] ; then
      desktop-file-validate %{buildroot}%{_datadir}/applications/${i}.desktop
      desktop-file-install --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/${i}.desktop
   fi
done

# convert hotplug stuff to udev
rm -f %{buildroot}/usr/lib/udev/tascam_fw.usermap
mkdir -p %{buildroot}/usr/lib/udev/rules.d
install -m 644 %{SOURCE1} %{buildroot}/usr/lib/udev/rules.d

%if 0%{!?_without_tools:1}
%files
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/as10k1
%doc %{_pkgdocdir}/echomixer
%doc %{_pkgdocdir}/envy24control
%doc %{_pkgdocdir}/hdspconf
%doc %{_pkgdocdir}/hdspmixer
%doc %{_pkgdocdir}/hwmixvolume
%doc %{_pkgdocdir}/rmedigicontrol
%doc %{_pkgdocdir}/sbiload
%doc %{_pkgdocdir}/hda-verb
%doc %{_pkgdocdir}/hdajackretask
%{_bindir}/as10k1
%{_bindir}/echomixer
%{_bindir}/envy24control
%{_bindir}/hdspconf
%{_bindir}/hdspmixer
%{_bindir}/hwmixvolume
%{_bindir}/rmedigicontrol
%{_bindir}/sbiload
%{_bindir}/sscape_ctl
%{_bindir}/us428control
%{_bindir}/hda-verb
%{_bindir}/hdajackretask
%{_bindir}/hdajacksensetest
%{_datadir}/sounds/*
%{_datadir}/man/man1/envy24control.1.gz
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps*

# sb16_csp stuff which is excluded for PPCx
%ifnarch ppc ppc64
%doc %{_pkgdocdir}/sb16_csp
%{_bindir}/cspctl
%{_datadir}/man/man1/cspctl.1.gz
%endif

%endif

%if 0%{!?_without_firmware:1}
%files firmware
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/hdsploader
%doc %{_pkgdocdir}/mixartloader
%doc %{_pkgdocdir}/usx2yloader
%doc %{_pkgdocdir}/vxloader
/usr/lib/udev/rules.d/*.rules
/usr/lib/udev/tascam_fpga
/usr/lib/udev/tascam_fw
%{_bindir}/hdsploader
%{_bindir}/mixartloader
%{_bindir}/usx2yloader
%{_bindir}/vxloader
%endif

%changelog
* Mon Jan 27 2025 Jaroslav Kysela <perex@perex.cz> - 1.2.11-6
- GCC warning fixes

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 18 2024 Jaroslav Kysela <perex@perex.cz> - 1.2.11-4
- Move remaining files to /usr tree

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Jaroslav Kysela <perex@perex.cz> - 1.2.11-2
- Updated to 1.2.11

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Florian Weimer <fweimer@redhat.com> - 1.2.5-10
- Fix C type errors using G_CALLBACK

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun  6 2023 Jaroslav Kysela <perex@perex.cz> - 1.2.5-8
- SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 08 2022 Leigh Scott <leigh123linux@gmail.com> - 1.2.5-4
- Remove unused gtk+-devel

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Jaroslav Kysela <perex@perex.cz> - 1.2.5-1
- Updated to 1.2.5

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 19 2020 Jaroslav Kysela <perex@perex.cz> - 1.2.2-1
- Updated to 1.2.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-2
- Switch python2-alsa dependency to python3-alsa as hwmixvolume runs on Python 3

* Tue Oct 16 2018 Jaroslav Kysela <perex@perex.cz> - 1.1.7-1
- Updated to 1.1.7

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 03 2018 Jaroslav Kysela <perex@perex.cz> - 1.1.6-1
- Updated to 1.1.6

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.5-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 22 2018 Tim Jackson <rpm@timj.co.uk> - 1.1.5-3
- Add missing BuildRequire on gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Jaroslav Kysela <perex@perex.cz> - 1.1.5-1
- Updated to 1.1.5

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Jaroslav Kysela <perex@perex.cz> - 1.1.3-1
- Updated to 1.1.3

* Wed Mar 16 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.0-3
- Fix FTBFS with GCC 6 (#1307312)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Jaroslav Kysela <perex@perex.cz> - 1.1.0-1
- Updated to 1.1.0

* Fri Sep 18 2015 Richard Hughes <rhughes@redhat.com> - 1.0.29-5
- Remove no longer required AppData files

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.29-3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.0.29-2
- Add an AppData file for the software center

* Thu Feb 26 2015 Jaroslav Kysela <perex@perex.cz> - 1.0.29-1
- updated to 1.0.29

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 1.0.28-4
- rebuild (fltk)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 25 2014 Tim Jackson <rpm@timj.co.uk> 1.0.28-1
- don't use %%makeinstall (RHBZ #909622)

* Thu Jul 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.28-1
- Update to 1.0.28

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug  1 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.0.27-3
- Install docs to %%{_pkgdocdir} where available.

* Tue May 21 2013 Dan Horák <dan[at]danny.cz> - 1.0.27-2
- fix build on non-x86 arches

* Fri Apr 12 2013 Jaroslav Kysela <jkysela@redhat.com> - 1.0.27-1
- Updated to 1.0.27

* Sat Feb 09 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.0.26.1-3
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines
- don't build -tools for RHEL. Bill Nottingham patch. Resolves rhbz#586030

* Fri Sep  7 2012 Jaroslav Kysela <jkysela@redhat.com> - 1.0.26.1-2
- Fixed gtk3-devel dependency (hdajackretask)
- Added description for hda-verb and hdajackretask

* Thu Sep  6 2012 Jaroslav Kysela <jkysela@redhat.com> - 1.0.26.1-1
- Updated to 1.0.26.1
- Added hda-verb and hdajackretask tools

* Thu Sep  6 2012 Jaroslav Kysela <jkysela@redhat.com> - 1.0.26-1
- Updated to 1.0.26

* Wed Aug 29 2012 Tim Jackson <rpm@timj.co.uk> - 1.0.25-4
- Move udev rules to /lib/udev/rules.d (rhbz #748206)
- remove %%BuildRoot and %%clean sections; no longer required

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.25-2
- Bump build for ARM

* Tue Jan 31 2012 Jaroslav Kysela <perex@perex.cz> - 1.0.25-1
- Update to 1.0.25

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.24.1-4
- Rebuild for new libpng

* Fri Jun 10 2011 Adam Jackson <ajax@redhat.com> 1.0.24.1-3
- Rebuild for new libfltk

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Tim Jackson <rpm@timj.co.uk> - 1.0.24.1-1
- Update to 1.0.24.1

* Mon May 03 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.23-1
- update to 1.0.23

* Sat Mar 06 2010 Tim Jackson <rpm@timj.co.uk> - 1.0.22-2
- Don't own /usr/share/sounds (#569415)

* Sun Jan 10 2010 Tim Jackson <rpm@timj.co.uk> - 1.0.22-1
- Update to 1.0.22
- use %%global instead of %%define

* Thu Sep 03 2009 Tim Jackson <rpm@timj.co.uk> - 1.0.21-1
- Update to 1.0.21

* Wed Aug 26 2009 Tim Jackson <rpm@timj.co.uk> - 1.0.20-4
- Add missing dep on xorg-x11-fonts-misc (#503284)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Tim Jackson <rpm@timj.co.uk> - 1.0.20-2

* Sun May 10 2009 Tim Jackson <rpm@timj.co.uk> - 1.0.20-1.fc12.2
- Update to 1.0.20

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Tim Jackson <rpm@timj.co.uk> - 1.0.19-2
- Fix unowned directory problem (#483323)

* Sat Jan 24 2009 Tim Jackson <rpm@timj.co.uk> - 1.0.19-1
- Update to version 1.0.19
- Mark udev rules as config

* Fri Dec  5 2008 Jon McCann <jmccann@redhat.com> - 1.0.17-2
- Convert hotplug stuff to udev

* Thu Jul 17 2008 Tim Jackson <rpm@timj.co.uk> - 1.0.17-1
- Update to version 1.0.17

* Mon May 19 2008 Tim Jackson <rpm@timj.co.uk> - 1.0.16-4
- Make it build cleanly on ppc and ppc64 by excluding sb16_csp

* Sun May 18 2008 Tim Jackson <rpm@timj.co.uk> - 1.0.16-3
- Really enable firmware subpackage

* Sun May 18 2008 Tim Jackson <rpm@timj.co.uk> - 1.0.16-2
- Enable firmware subpackage - the accompanying alsa-firmware package is
  finally in Fedora

* Sat Mar 01 2008 Tim Jackson <rpm@timj.co.uk> - 1.0.16-1
- Update to upstream 1.0.16 (fixes #434473)

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.15-3
- Autorebuild for GCC 4.3

* Sat Jan 05 2008 Tim Jackson <rpm@timj.co.uk> - 1.0.15-2
- Update License tag to GPLv2+
- ExcludeArch ppc64 (bug #219010)

* Sat Jan 05 2008 Tim Jackson <rpm@timj.co.uk> - 1.0.15-1
- Update to upstream 1.0.15
- Add icon for envy24control
- Build echomixer

* Sat Dec 09 2006 Tim Jackson <rpm@timj.co.uk> - 1.0.12-4
- ExcludeArch ppc (#219010)

* Sun Nov 26 2006 Tim Jackson <rpm@timj.co.uk> - 1.0.12-3
- Add gtk2-devel BR

* Sun Nov 26 2006 Tim Jackson <rpm@timj.co.uk> - 1.0.12-2
- Own our docdir explicitly

* Sat Nov 25 2006 Tim Jackson <rpm@timj.co.uk> - 1.0.12-1
- Update to 1.0.12
- Resubmit to Fedora Extras 6
- Replace hotplug requirement with udev

* Mon Feb 13 2006 Thorsten Leemhuis <fedora[AT]leemhuis.info>
- Rebuild for Fedora Extras 5

* Tue Dec 06 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.10-1
- Update to 1.0.10

* Fri May 06 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.9-1
- Update to 1.0.9
- Use disttag
- Remove gcc4 patch

* Fri May 06 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8-3
- prune ac3dec from sources

* Thu May 05 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8-2
- don't build ac3dec -- use a52dec instead

* Wed Apr 06 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 1.0.8-1
- Update to 1.0.8
