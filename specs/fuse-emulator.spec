Name:           fuse-emulator
Version:        1.6.0
Release:        12%{?dist}
Summary:        The Free UNIX Spectrum Emulator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fuse-emulator.sourceforge.net
Source0:        fuse-%{version}-noroms.tar.gz
# we use
# this script to remove the roms binary before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory:
# ./generate-tarball.sh 0.9.0
Source1:        generate-tarball.sh
Source2:        README.z88sdk
Source3:        README_fuseroms.fedora
BuildRequires:  alsa-lib-devel
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  libgcrypt-devel >= 1.1.42
BuildRequires:  libICE-devel
BuildRequires:  libpng-devel
BuildRequires:  libspectrum-devel >= 1.4.3
BuildRequires:  libxml2-devel
BuildRequires:  zlib-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  SDL2-devel
BuildRequires:  perl
BuildRequires: make
Requires:       hicolor-icon-theme

%description
Fuse is a spectrum emulator which emulates multiple models, including the 16K,
48K, 128K, +2, +2A, +3 and various clones.


%prep
%setup -qn fuse-%{version}

# Filter unwanted dependency in the debuginfo rpm
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
    sed -e '/perl(Fuse)/d' | \
    sed -e '/perl(strict)/d' | \
    sed -e '/perl(lib)/d'
EOF

%define __perl_requires %{_builddir}/fuse-%{version}/%{name}-req
chmod +x %{__perl_requires}


%build
%configure --enable-desktop-integration
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -pm0644 %{SOURCE2} .
install -pm0644 %{SOURCE3} .

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications \
        %{buildroot}/%{_datadir}/applications/fuse.desktop



%files
%{_mandir}/man1/fuse.1.gz
%{_bindir}/fuse
%{_datadir}/fuse
%{_datadir}/applications/fuse.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-spectrum.png
%{_datadir}/icons/hicolor/*/apps/fuse.png
%{_datadir}/mime/packages/fuse.xml
%doc AUTHORS ChangeLog COPYING README THANKS README.z88sdk README_fuseroms.fedora


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Michel Lind <salimma@fedoraproject.org> - 1.6.0-9
- Use GTK3 and SDL2 rather than GTK2 and SDL1 (rhbz#2000729)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 29 2021 Lucian Langa <lucilanga@gnome.eu.org> - 1.6.0-1
- sync with latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Lucian Langa <lucilanga@gnome.eu.org> - 1.5.7-1
- update to latest upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Lucian Langa <lucilanga@gnome.eu.org> - 1.5.4-1
- new upstream release

* Fri Apr 06 2018 Lucian Langa <lucilanga@gnome.eu.org> - 1.5.2-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-2
- Remove obsolete scriptlets

* Wed Nov 01 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.1-1
- new upstream release

* Thu Sep 28 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.4.0-1
- new upstream release

* Sun Aug 27 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.8-2
- update BR

* Tue Aug 22 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.8-1
- new upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 04 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.7-1
- new upstream release

* Sun May 14 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.5-1
- new upstream release

* Wed Feb 08 2017 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.3-1
- new upstream release

* Sat Dec 10 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.2-1
- new upstream release

* Tue Nov 15 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.1-1
- new upstream release

* Tue Oct 04 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.3.0-1
- add desktop integration files
- drop source2 (icon file) - project supplies its own icon file
- new upstream release

* Thu Sep 01 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.2-1
- update generation script
- new upstream release

* Wed Jul 20 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.1-1
- new upstream release

* Sat Jun 11 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.0-2
- bump BR libspectrum version (thanks Sergio B)

* Tue Jun 07 2016 Lucian Langa <lucilanga@gnome.eu.org> - 1.2.0-1
- update generate-tarbal script
- misc cleanups
- update to latest upstream

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Lucian Langa <cooly@gnome.eu.org> - 1.1.1-1
- drop old build requires
- add missing requires
- new upstream release

* Tue May 21 2013 Lucian Langa <cooly@gnome.eu.org> - 1.1.0-1
- new upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 Lucian Langa <cooly@gnome.eu.org> - 1.0.0.1-6
- rebuilt with newer libaudiofile

* Wed Aug 01 2012 Jon Ciesla <limburgher@gmail.com> - 1.0.0.1-5
- Tom Lane's zlib fixes for libpng15, BZ 843645.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0.1-2
- Rebuild for new libpng

* Thu Mar 03 2011 Lucian Langa <cooly@gnome.eu.org> - 1.0.0.1-1
- new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Lucian Langa <cooly@gnome.eu.org> - 1.0.0-1
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Lucian Langa <cooly@gnome.eu.org> - 0.10.0.2-1
- new upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 13 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10.0.1-1
- new upstream critial fix release

* Fri Dec 05 2008 Lucian Langa <cooly@gnome.eu.org> - 0.10.0-1
- new upstream release 0.10.0

* Sat Aug 23 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9.0-4
- fix rh bug 458817

* Sat Aug  2 2008 Lucian Langa <cooly@gnome.eu.org> - 0.9.0-3
- strip source before uploading it
- fix for BADSOURCE

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.0-2
- Autorebuild for GCC 4.3

* Mon Jan 07 2008 Ian Chapman <packages[AT]amiga-hardware.com> 0.9.0-1
- Upgrade to 0.9.0
- Use DESTDIR and noroms patch
- Added several new BRs for the new version

* Tue Aug 21 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.0.1-3
- Release bump for F8 mass rebuild
- License change due to new guidelines

* Sun Jul 15 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.0.1-2
- Filter unwanted dependancies dragged in by rpm (BZ #248265)

* Sat Jun 30 2007 Ian Chapman <packages[AT]amiga-hardware.com> 0.8.0.1-1
- Upgrade to 0.8.0.1
- Various cleanups to the SPEC including conforming to new guidelines

* Thu Feb 9 2006 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.7.0-6
- Removed pre and post as they were empty
- Fixed the "fuse-emulator" problem

* Wed Oct 26 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.7.0-5
- Altered package name to fuse-emulator (macro)
- Removed BR: zlib-devel and BR: glibc-devel and both Requires
- Included comment regarding the SRPM not containing the ROMS
- Added README.z88sdk file to the archive
- Made the source of the tarball a valid one!
- Removed a comma from after xml2-devel

* Mon Oct 17 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.7.0-4
- Minor alteration to spec file (Build require=perl gone)
- Addition of sound.c patch file

* Fri Sep 02 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.7.0-3.fc
- Removal of ROMS and addition to documentation of where to get ROMS

* Mon Aug 29 2005 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.7.0-2.fc
- Fixes to both the source and spec for FC

* Mon Feb 28 2005 Ian Chapman <packages[AT]amiga-hardware.com> - 0.7.0-2.iss
- Rebuild for newer version of lib765 (0.3.3)

* Fri Jul 16 2004 Ian Chapman <packages[AT]amiga-hardware.com> - 0.7.0-1.iss
- Updated to version 0.7.0
- Updated for Fedora Core 2
- Added a graphic for the menu icon

* Fri Dec 05 2003 Ian Chapman <packages[AT]amiga-hardware.com> - 0.6.1.1-2
- Minor fixes to changelog
- Improved use of macros
- Removed most explicit library dependancies
- Added menu icon

* Sun Nov 30 2003 Ian Chapman <packages[AT]amiga-hardware.com> - 0.6.1.1-1
- Initial Release
