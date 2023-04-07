%undefine __cmake_in_source_build

%bcond_without gui

Summary:       Hardware lister
Name:          lshw
Version:       B.02.19.2
Release:       11%{?dist}
License:       GPLv2
URL:           http://ezix.org/project/wiki/HardwareLiSter
Source0:       http://www.ezix.org/software/files/lshw-%{version}.tar.gz
Source1:       https://salsa.debian.org/openstack-team/third-party/lshw/raw/debian/stein/debian/patches/lshw-gtk.1
Patch1:        lshw-B.02.18-scandir.patch
Patch4:        lshw-B.02.19.2-cmake.patch
Patch9:        0003-report-CPU-family-model-stepping.patch
Patch10:       0004-move-PnP-devices-to-the-ISA-LPC-bridge.patch
Patch11:       0005-correctly-format-SMBIOS-UUID.patch
Patch12:       0006-cosmetic-clean-up.patch
Patch13:       0007-begin-work-on-input-devices.patch
Patch14:       0008-cosmetic-fixes.patch
Patch15:       0009-detect-sound-devices.patch
Patch16:       0010-detect-framebuffers.patch
Patch17:       0011-try-to-connect-input-devices-to-the-right-parent.patch
Patch18:       0012-devtree-Add-chip-id-from-the-dimm-module.patch
Patch19:       0013-devtree-Add-chip-id-from-CPU-node.patch
Patch20:       0014-volumes-fix-segfault-in-apfs-volume-code.patch
Patch21:       0015-merge-Github-PR-53.patch
Patch22:       0016-devtree-Add-capabilites-to-the-OPAL-Firmware.patch
Patch23:       0017-fix-issue-with-logical-names-being-truncated-dev-sda.patch
Patch24:       0018-code-clean-up-for-read-3.patch
Patch25:       0019-JSON-output-clean-up-list-object.patch
Patch26:       0020-clean-up-JSON-output.patch
Patch27:       0021-report-product-model-on-Power-systems.patch
Patch28:       0022-Fix-few-memory-leaks.patch
Patch29:       0023-Build-against-gtk3-instead-of-gtk2.patch
Patch30:       0024-Remove-deprecated-stock-messages.patch
Patch31:       0025-Remove-hack-which-is-apparently-not-useful-anymore.patch
Patch32:       0026-Use-GtkFileChooserNative-instead-of-GtkFileChooserDi.patch
Patch33:       0027-Replace-deprecated-GtkIconFactory-with-GHashTable.patch
Patch34:       0028-Replace-the-last-GtkStock-in-overwrite-dialog.patch
Patch35:       0029-Remove-deprecated-widgets.patch
Patch36:       0030-Remove-deprecated-use_action_appearance-property.patch
Patch37:       0031-Move-to-GtkApplication.patch
Patch38:       0032-Replace-signals-with-GSimpleActions.patch
Patch39:       0033-Enable-Disable-GSimpleAction-instead-of-button-sensi.patch
Patch40:       0034-Move-from-GtkMenuBar-to-GMenu.patch
Patch41:       0035-Replace-the-about-GtkDialog-with-a-GtkAboutDialog.patch
Patch42:       0036-Update-docs-TODO.patch
Patch43:       0037-Update-docs-TODO.patch
Patch44:       0038-update-man-page.patch
Patch45:       0039-fix-man-page-after-previous-update.patch
Patch46:       0040-Report-correct-memory-size-on-SMBIOS-2.7.patch
Patch47:       0041-Add-JEDEC-manufacturer.patch
Patch48:       0042-Avoid-crash-on-device-tree-parsing.patch
#Patch49:      0043-add-static-target-to-Makefile.patch -- Makefile change only, no need
Patch50:       0044-fix-potential-crash.patch
Patch51:       0045-improve-portability-esp.-musl.patch
Patch52:       0046-code-clean-up.patch
Patch53:       0047-devtree-Add-UUID-property.patch
Patch54:       0048-Fix-getting-size-of-memory-banks-32GiB.patch
Patch55:       0049-Fix-typos-in-translatable-messages.patch
Patch56:       0050-Fix-another-typo.patch
Patch57:       0051-Translate-all-words-of-a-phrase-together.patch
Patch58:       0052-Remove-unnecessary-space-before-closing-parenthesis.patch
#Patch59:      0053-allow-pkg-config-override.patch -- ditto
#Patch60:      0054-allow-pkg-config-override.patch -- ditto
Patch61:       0055-code-clean-up.patch
Patch62:       0056-code-clean-up.patch
Patch63:       0057-support-for-new-ethtool-capabilities.patch
Patch64:       0058-cosmetic-fixes.patch
Patch65:       0059-fix-typo.patch
Patch66:       0060-add-some-includes.patch
Patch67:       0061-Add-more-network-speeds.patch
Patch68:       0062-Update-POT-file.patch
Patch69:       0063-Add-Catalan-translation.patch
#Patch70:      0064-use-max-9-Gzip-compression.patch -- ditto
Patch71:       0065-merge-Github-PR-77.patch
Patch72:       0066-Fix-mistakes-in-Catalan-translation.patch
Patch73:       0067-Add-Spanish-translation.patch
Patch74:       0001-Github-PR85-Set-product-name-for-all-netdevs-sharing.patch
Patch75:       0002-make-version-check-optional.patch
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
%if %{with gui}
BuildRequires: gtk3-devel >= 3.24
BuildRequires: libappstream-glib
%endif
BuildRequires: ninja-build
BuildRequires: python3-devel
BuildRequires: sqlite-devel
Requires:      hwdata
%description
lshw is a small tool to provide detailed informaton on the hardware
configuration of the machine. It can report exact memory
configuration, firmware version, mainboard configuration, CPU version
and speed, cache configuration, bus speed, etc. on DMI-capable x86
systems and on some PowerPC machines (PowerMac G4 is known to work).

Information can be output in plain text, XML or HTML.

%if %{with gui}
%package       gui
Summary:       Graphical hardware lister
Requires:      polkit
Requires:      %{name} = %{version}-%{release}
%description   gui
Graphical frontend for the hardware lister (lshw) tool. If desired,
hardware information can be saved to file in plain, XML or HTML
format.
%endif

%prep
%autosetup -p1

%build
%if %{with gui}
%global gui_config -DGUI=ON
%else
%global gui_config -DGUI=OFF
%endif

%cmake -DNOLOGO=ON -DHWDATA=OFF -DPOLICYKIT=ON -DSQLITE=ON -DBUILD_SHARED_LIBS=OFF %{gui_config} -GNinja
%cmake_build

%install
%cmake_install
%if %{with gui}
install -m0644 -D %{SOURCE1} %{buildroot}%{_mandir}/man1/lshw-gui.1
ln -s gtk-lshw %{buildroot}%{_sbindir}/lshw-gui
%endif
# translations seems borken, remove for now
#find_lang %{name}
rm -rf %{buildroot}%{_datadir}/locale/*/

%check
%if %{with gui}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%endif

# check json output is valid
%{_vpath_builddir}/src/lshw -json \
    -disable usb -disable pcmcia -disable isapnp \
    -disable ide -disable scsi -disable dmi -disable memory \
    -disable cpuinfo 2>/dev/null | %{__python3} -m json.tool

#files -f %{name}.lang
%files
%license COPYING
%doc README.md
%{_mandir}/man1/lshw.1*
%{_sbindir}/lshw

%if %{with gui}
%files gui
%license COPYING
%{_bindir}/lshw-gui
%{_sbindir}/gtk-lshw
%{_sbindir}/lshw-gui
%{_mandir}/man1/lshw-gui.1*
%dir %{_datadir}/lshw
%{_datadir}/lshw/artwork
%dir %{_datadir}/lshw/ui
%{_datadir}/lshw/ui/gtk-lshw.ui
%{_datadir}/pixmaps/gtk-lshw.svg
%{_datadir}/applications/gtk-lshw.desktop
%{_datadir}/appdata/gtk-lshw.appdata.xml
%{_datadir}/polkit-1/actions/org.ezix.lshw.gui.policy
%endif

%changelog
* Wed Apr 05 2023 Terje Rosten <terje.rosten@ntnu.no> - B.02.19.2-11
- Use modern macros

* Tue Apr 04 2023 Yaakov Selkowitz <yselkowi@redhat.com> - B.02.19.2-10
- Update to upstream commit 76afbaaf40e

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - B.02.19.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - B.02.19.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Stewart Smith <trawets@amazon.com> - B.02.19.2-7
- Make GUI an optional bcond
- Disable remote DNS lookup on 'lshw -version'

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - B.02.19.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - B.02.19.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - B.02.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - B.02.19.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 24 2020 Terje Rosten <terje.rosten@ntnu.no> - B.02.19.2-2
- Add patch from openSUSE to fix rhbz#1822455

* Tue Mar 24 2020 Terje Rosten <terje.rosten@ntnu.no> - B.02.19.2-1
- B.02.19.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-21
- Update to commit 6cc0581
- Rebase cmake patch on top 6cc0581
- Add NVME patch from PR#45

* Sat May 25 2019 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-20
- Add lshw-gui man page (from Debian, thanks!)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - B.02.18-17
- Rebuilt for Python 3.7

* Mon Apr 02 2018 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-16
- Update to commit 20cda77
- Convert to cmake build system

* Thu Feb 08 2018 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-15
- Fix JSON issue (rhbz#1543320)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-13
- Fix date
- Need gettext

* Fri Jan 26 2018 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-12
- Update to commit d05baa7

* Mon Aug 28 2017 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-11
- Prefer lshw-gui in lshw-gui context

* Sun Aug 13 2017 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-10
- Add AppData bz#1476498

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - B.02.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-5
- Modify lshw gui wrapper to fix bz#1368404

* Thu Aug 11 2016 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-4
- Add patches to fix sysconf/long_bit issue and crash (bz#1342792)

* Wed May 18 2016 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-3
- Add patch to fix crash (bz#1332486)

* Mon Apr 25 2016 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-2
- Date fix

* Mon Apr 25 2016 Terje Rosten <terje.rosten@ntnu.no> - B.02.18-1
- B.02.18

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - B.02.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - B.02.17-5
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 30 2013 Terje Rosten <terje.rosten@ntnu.no> - B.02.17-2
- Add patch to fix segfault in scan fat code

* Thu Sep 26 2013 Terje Rosten <terje.rosten@ntnu.no> - B.02.17-1
- B.02.17

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Terje Rosten <terje.rosten@ntnu.no> - B.02.16-8
- Rename macro

* Sun Jun 09 2013 Terje Rosten <terje.rosten@ntnu.no> - B.02.16-7
- Fix desktop file (bz #953684)
- Remove broken translations (bz #905896)
- Add vendor macro
 
* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - B.02.16-6
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 08 2012 Terje Rosten <terje.rosten@ntnu.no> - B.02.16-3
- Switch from consolehelper to PolicyKit (bz #502730)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.16-2
- Rebuilt for c++ ABI breakage

* Sun Jan 29 2012 Terje Rosten <terje.rosten@ntnu.no> - B.02.16-1
- B.02.16

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Terje Rosten <terje.rosten@ntnu.no> - B.02.15-3
- Own all dirs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 21 2010 Terje Rosten <terje.rosten@ntnu.no> - B.02.15-1
- B.02.15
- Remove patches now upstream
- Build with sqlite support

* Sun Sep 05 2010 Terje Rosten <terje.rosten@ntnu.no> - B.02.14-5
- Add patch to fix build with gcc-4.5

* Sun Sep 05 2010 Terje Rosten <terje.rosten@ntnu.no> - B.02.14-4
- Add patch to fix ext4 issue

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 06 2009 Adam Jackson <ajax@redhat.com> - B.02.14-2
- Requires: hwdata
- Drop redundant copies of pci.ids and friends, since we'll pick up the
  copies in hwdata at runtime

* Sun Mar  1 2009 Terje Rosten <terjeros@phys.ntnu.no> - B.02.14-1
- B.02.14
- Drop gcc43 patch now upstream

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - B.02.13-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 13 2008 Terje Rosten <terjeros@phys.ntnu.no> - B.02.13-3
- rebuild

* Wed Aug 13 2008 Terje Rosten <terjeros@phys.ntnu.no> - B.02.13-2
- proper patch macro

* Wed Aug 13 2008 Terje Rosten <terjeros@phys.ntnu.no> - B.02.13-1
- B.02.13
- remove patches now upstream
- add new gcc43 patch

* Tue Apr 15 2008 Terje Rosten <terjeros@phys.ntnu.no> - B.02.12.01-5
- rebuild

* Tue Apr 15 2008 Terje Rosten <terjeros@phys.ntnu.no> - B.02.12.01-4
- add patch to fix bz #442501

* Mon Feb 11 2008 Terje Rosten <terjeros@phys.ntnu.no> - B.02.12.01-3
- add patch to build with gcc-4.3

* Sat Feb 09 2008 Terje Rosten <terjeros@phys.ntnu.no> - B.02.12.01-2
- rebuild

* Mon Nov  5 2007 Terje Rosten <terjeros@phys.ntnu.no> - B.02.12.01-1
- B.02.12.01
- Replace trademark icons

* Tue Aug 14 2007 Terje Rosten <terjeros@phys.ntnu.no> - B.02.11.01-3
- Move desktop and pam config to files
- Simplify build

* Tue Aug 07 2007 Terje Rosten <terjeros@phys.ntnu.no> - B.02.11.01-2
- Remove trademarks

* Mon Aug 06 2007 Terje Rosten <terjeros@phys.ntnu.no> - B.02.11.01-1
- B.02.11.01

* Sun Aug 05 2007 Terje Rosten <terjeros@phys.ntnu.no> - B.02.11-3
- Move artwork to gui subpackage
- Implement consolehelper support

* Sat Aug 04 2007 Terje Rosten <terjeros@phys.ntnu.no> - B.02.11-2
- License is GPLv2 (only)
- Fix ui %%description

* Wed Aug 01 2007 Terje Rosten <terjeros@phys.ntnu.no> - B.02.11-1
- Follow upstream version scheme

* Wed Jul 25 2007 Terje Rosten <terjeros@phys.ntnu.no> - 2.11-1
- 2.11

* Wed Jun 27 2007 Terje Rosten <terjeros@phys.ntnu.no> - 2.10-2
- minor fixes
- add patch to avoid stripping
- add desktop file
- strip changelog
- move from sbin to bin
- new url

* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 2.10-1 - 4876+/dag
- Updated to release B.02.10.

* Tue Dec 21 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)

