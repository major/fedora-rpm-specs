# force out-of-tree build for spec compatibility with older releases
%undefine __cmake_in_source_build

Name: aqemu
Version: 0.9.2
Release: 21%{?dist}
Summary: A QT graphical interface to QEMU and KVM
License: GPLv2+
URL: http://aqemu.sourceforge.net
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:	 %{name}-%{version}-docopt_value.h.patch
BuildRequires: qt5-qtbase-devel
BuildRequires: cmake
BuildRequires: libvncserver-devel
BuildRequires: desktop-file-utils
BuildRequires: gnutls-devel
BuildRequires: hicolor-icon-theme
BuildRequires: zlib-devel

%description
AQEMU is a graphical user interface to QEMU and KVM, written in Qt4. The
program has a user-friendly interface and allows user to set the
majority of QEMU and KVM options on their virtual machines.

%prep
%setup -q
%patch0

%build
# help find Qt5 helper binaries that were renamed (e.g. rcc-qt5)
# to be # parallel-installable with Qt4 ones
PATH=%{_qt5_bindir}:$PATH; export PATH
%cmake
%cmake_build

%install
%cmake_install
# Copy 48x48 and 64x64 icons to correct location.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,64x64}/apps
mv %{buildroot}%{_datadir}/pixmaps/%{name}_48x48.png \
   %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
mv %{buildroot}%{_datadir}/pixmaps/%{name}_64x64.png \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
# Remove directories from install which are not being deployed in RPM.
rm -rf %{buildroot}%{_datadir}/pixmaps
rm -rf %{buildroot}%{_datadir}/menu
rm -rf %{buildroot}%{_datadir}/doc/%{name}
# Validate the icon file.
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%doc AUTHORS CHANGELOG TODO
%license COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_mandir}/man1/%{name}.1*

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Jeff Law <law@redhat.com> - 0.9.2-14
- Require zlib-devel for building

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 24 2019 Stephen Gordon <sgordon@redhat.com> - 0.9.2-12
- Add patch to docopt_value.h to prepare for GCC 10.
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.2-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.9.2-4
- rebuild (libvncserver), use %%license

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 08 2016 Stephen Gordon <sgordon@redhat.com> - 0.9.2-2
- Removed qt-devel BuildRequires.

* Thu Jun 02 2016 Stephen Gordon <sgordon@redhat.com> - 0.9.2-1
- Fixed bug that prevented AQEMU from closing when no VM was created yet
- Added frugalware icon
- Fixed aqemu icon name to match .desktop file
- Fixed incorrect information for raw images
- Removed artificial 6GB limit on VM memory size
- Show "Option ... not supported" errors that are wrongly sent to stdout by qemu

* Tue May 31 2016 Stephen Gordon <sgordon@redhat.com> - 0.9.1-1
- 0.8.2 AQEMU settings and files get loaded correctly (If you want to go back to 0.8.2, make a backup)
- Embedded VNC client now can make use of the user defined VNC port number
- Error Log Window doesn't get shown for messages about deprecated options by default anymore
- The VM state is now getting reflected in the VM icon (Running, Paused, ...)
- Removed code to support qemu qemu-kvm fork, because it has been merged into qemu
- Many small UI improvements
- All new VMs are now created with the wizard, which generally gives better results
- Put all application wide settings in a single dialog
- Exchanged some deprecated qemu command line options with their new equivalents
- Fixed various bugs
- Reorganized/Restructured the main UI for more clarity
- Fixed bug that led to VMs not being terminated when closing the application
- New feature: Folder sharing
- New feature: Send clipboard as keys to the VM
- Fixed bug where SPICE dialog didn't validate correctly.
- Applied patches for Intel HDA and CS4231A sound suppport (thanks to Eli Carter and others!)
- Applied patch for fixing SPICE video stream compression support
- Applied patch that fixes typo
- Put QDom* TinyXML2 wrapper into its own namespace. Fixes runtime problems in conjunction with KDE.
- Ported to Qt5
- Ported to C++-11
- Applied downstream patches (Fedora)

* Sun Mar 20 2016 Stephen Gordon <sgordon@redhat.com> - 0.8.2-18
- Use updated QEMU -spice parameters (bz#1268553)

* Sat Mar 19 2016 Stephen Gordon <sgordon@redhat.com> - 0.8.2-17
- Apply changes for GCC 6 compatibility (bz#1307322)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.2-14
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Stephen Gordon <sgordon@redhat.com> - 0.8.2-12
- Apply changes for "-Werror=format-security" (bz#1036992)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 5 2012 Stephen Gordon <sgordon@redhat.com> - 0.8.2-7
- Added BuildRequires on hicolor-icon-theme (bz#734275).

* Mon Feb 27 2012 Stephen Gordon <sgordon@redhat.com> - 0.8.2-6
- Added BuildRequires on gnutls-devel (bz#734275).
- Added white space to spec file changelog (bz#734275).
- Added comment for desktop patch file (bz#734275).
- Added patch disabling error macro definition (bz#734275).
- Updated license in spec file to GPLv2+ (bz#734275).
- Updated man page location to include section number (bz#734275).
- Removed README file as it only detailed installation (bz#734275).

* Mon Sep 05 2011 Stephen Gordon <sgordon@redhat.com> - 0.8.2-5
- Updated to include both icon sizes supplied by upstream (bz#734275).

* Tue Aug 30 2011 Stephen Gordon <sgordon@redhat.com> - 0.8.2-4
- Updated to drop redundant slashes in paths (bz#734275).
- Updated desktop file to pass desktop-file-validate tests (bz#734275).

* Tue Aug 30 2011 Stephen Gordon <sgordon@redhat.com> - 0.8.2-3
- Escaped macros in changelog (bz#734275).
- Dropped explicit requires fields (bz#734275).
- Updated to use desktop-file-validate for desktop file (bz#734275).
- Settled on %%{buildroot} for referring to build root consistently 
  (bz#734275).
- Updated to deploy documentation files to correct location (bz#734275).

* Tue Aug 30 2011 Stephen Gordon <sgordon@redhat.com> - 0.8.2-2
- Updated Source0 to include full URL (bz#734275).
- Removed BuildRoot, %%clean, and %%defattr, not required (bz#734275).
- Moved icon file manipulation from %%prep to %%install (bz#734275).
- Modified to use %%cmake macro instead of explicit cmake call (bz#734275).
- Added smp flags to make call (bz#734275).
- Modified to use make install instead of make install/strip (bz#734275).
- Modified to ensure correct DESTDIR on make call (bz#734275).

* Mon Aug 29 2011 Stephen Gordon <sgordon@redhat.com> - 0.8.2-1
- Initial packaging of aqemu 0.8.2 for Fedora, based on SuSE aqemu 0.8.1 RPM.
