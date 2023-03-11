Name:           lazarus
Summary:        Lazarus Component Library and IDE for Freepascal

Version:        2.2.6

%global baserelease 1
Release:        %{baserelease}%{?dist}

# The qt5pas version is taken from lcl/interfaces/qt5/cbindings/Qt5Pas.pro
%global qt5pas_version 2.6
%global qt5pas_release %(relstr="%{version}.%{baserelease}"; relstr=(${relstr//./ }); ((relno=${relstr[0]}*1000000 + ${relstr[1]}*10000 + ${relstr[2]}*100 + ${relstr[3]})); echo "${relno}%{?dist}";)

# GNU Classpath style exception, see COPYING.modifiedLGPL
License:        GPL-2.0-or-later AND LGPL-2.0 WITH Classpath-exception-2.0 AND MPL-1.1
URL:            http://www.lazarus-ide.org/
Source0:        https://downloads.sourceforge.net/project/%{name}/Lazarus%20Zip%20_%20GZip/Lazarus%20%{version}/%{name}-%{version}-0.tar.gz

Source100:      lazarus.appdata.xml

# Lazarus wants to put arch-specific stuff in /usr/share - make it go in /usr/lib istead
Patch0:         0000-Makefile_patch.diff

# Fix build errors for GTK3 widgetset
Patch2:         0002-fix-GTK3-build-error.patch

BuildRequires:  binutils
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gtk2-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

Requires:	binutils
Requires:	fpc%{?_isa}
Requires:	fpc-src
Requires:	gdb
Requires:	make

Requires:	glibc-devel%{?_isa}
Requires:	gtk2-devel%{?_isa}
Requires:	qt5pas-devel%{?_isa} = %{qt5pas_version}-%{qt5pas_release}

ExclusiveArch:  %{fpc_arches}

%description
A free and open-source RAD tool for Free Pascal using the Lazarus
Component Library - LCL, which is also included in this package.


# Qt5pas start
%package -n     qt5pas
Version:        %{qt5pas_version}
Release:        %{qt5pas_release}
Summary:        Qt5 bindings for Pascal

%description -n qt5pas
Qt5 bindings for Pascal from Lazarus.

%package -n     qt5pas-devel
Version:        %{qt5pas_version}
Release:        %{qt5pas_release}
Summary:        Development files for qt5pas
Requires:       qt5pas%{?_isa} = %{qt5pas_version}-%{qt5pas_release}

%description -n qt5pas-devel
The qt5pas-devel package contains libraries and header files for
developing applications that use qt5pas.
# Qt5pas end


%prep
%setup -c -q
%patch0 -p1
%patch2 -p1


%build
cd lazarus
# Remove the files for building other packages
rm -rf debian
cd tools
find install -depth -type d ! \( -path "install/linux/*" -o -path "install/linux" -o -path "install" \) -exec rm -rf '{}' \;
cd ..

export FPCDIR=%{_datadir}/fpcsrc/
fpcmake -Tall
cd components
fpcmake -Tall
cd ..
make bigide OPT='-gl -gw'
make tools OPT='-gl -gw'

pushd lcl/interfaces/qt5/cbindings/
    %{qmake_qt5}
    %make_build
popd


%install
make -C lazarus install INSTALL_PREFIX=%{buildroot}%{_prefix} _LIB=%{_lib}

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        lazarus/install/%{name}.desktop

install -d %{buildroot}%{_sysconfdir}/lazarus
sed 's#__LAZARUSDIR__#%{_libdir}/%{name}#;s#__FPCSRCDIR__#%{_datadir}/fpcsrc#' \
        lazarus/tools/install/linux/environmentoptions.xml \
        > %{buildroot}%{_sysconfdir}/lazarus/environmentoptions.xml

chmod 755 %{buildroot}%{_libdir}/%{name}/components/lazreport/tools/localize.sh

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 %{SOURCE100} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

# -- Install Qt5Pas

pushd lazarus/lcl/interfaces/qt5/cbindings/
    %make_install INSTALL_ROOT=%{buildroot}
popd

# Since we provide Qt5Pas as a standalone package, remove the .so files bundled in Lazarus dir
# and replace them with symlinks to the standalone .so.
for FILEPATH in $(ls %{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt5/cbindings/libQt5Pas.so*); do
    FILENAME=$(basename "$FILEPATH")
    ln -sf "%{_libdir}/${FILENAME}" "${FILEPATH}"
done

# Cannot be done earlier since "make install" expects the tmp/ directory to be present. Sigh.
rm -rf %{buildroot}%{_libdir}/%{name}/lcl/interfaces/qt5/cbindings/tmp/


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%doc lazarus/README.md
%license lazarus/COPYING*
%{_libdir}/%{name}
%{_bindir}/%{name}-ide
%{_bindir}/startlazarus
%{_bindir}/lazbuild
%{_bindir}/lazres
%{_bindir}/lrstolfm
%{_bindir}/updatepofiles
%{_datadir}/pixmaps/lazarus.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/mime/packages/lazarus.xml
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_metainfodir}/%{name}.appdata.xml
%dir %{_sysconfdir}/lazarus
%config(noreplace) %{_sysconfdir}/lazarus/environmentoptions.xml
%{_mandir}/*/*

%files -n qt5pas
%license lazarus/lcl/interfaces/qt5/cbindings/COPYING.TXT
%doc lazarus/lcl/interfaces/qt5/cbindings/README.TXT
%{_libdir}/libQt5Pas.so.*

%files -n qt5pas-devel
%{_libdir}/libQt5Pas.so


%changelog
* Wed Mar 08 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.2.6-1
- Update to v2.2.6
- Add a patch to fix build errors when using the GTK3 widgetset
- Convert License tag to SPDX
- Drop Patch1 (fix components explicitly requesting STABS debuginfo - fixed upstream)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.2.4-1
- Update to v2.2.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 19 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.2.2-1
- Update to v2.2.2

* Mon Feb 07 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.2.0-1
- Update to v2.2.0
- Drop Patch1 - disable PascalScript on ppc64le (compiles successfully now)
- Add Patch1 - use DWARF debuginfo instead of stabs

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.12-2
- Rebuild for FPC 3.2.2

* Fri Apr 30 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.12-1
- Update to 2.0.12
- Use baserelease macro to fix the rpmdev-bumspec issues

* Fri Feb 05 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.10-7
- Fix FailsToInstall due to .1 added to qt5pas release number

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.0.10-5
- Add an appdata file

* Mon Aug 24 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.10-4
- Make the package explicitly require "make"

* Mon Aug 03 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.10-3
- Fix FailsToInstall due to .1 added to qt5pas release number

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.10-1
- Update to v2.0.10

* Sun Jun 21 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.8-4
- Rebuilt for FPC 3.2.0

* Wed Jun 03 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.8-3
- Rebuilt for FPC 3.2.0-beta-r45533

* Mon May 04 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.8-2
- Rebuilt for FPC 3.2.0-beta-r45235

* Thu Apr 16 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.8-1
- Update to upstream release v.2.0.8
- Drop Patch2 ("illegal qualifier" compile-time error) - fixed upstream

* Sun Apr 12 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.6-9
- Rebuilt for FPC 3.2.0-beta-r44680

* Sat Mar 28 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.6-8
- Rebuilt for FPC 3.2.0-beta-r44375

* Mon Mar 16 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.6-7
- Rebuilt for FPC 3.2.0-beta-r44301

* Mon Feb 24 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.6-6
- Rebuilt for FPC 3.2.0-beta-r44232

* Wed Feb 12 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.6-5
- Rebuilt for FPC 3.2.0-beta-r44160

* Sat Feb 08 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.6-4
- Fix build failures in Rawhide
- Rebuilt for FPC 3.2.0-beta-r44109

* Wed Jan 29 2020 Artur Iwicki <fedora@svgames.pl> - 2.0.6-3
- Disable PascalScript on ppc64le

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.6-1
- Update to upstream release v.2.0.6

* Sun Oct 20 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.4-4
- Make Lazarus depend on qt5pas-devel instead of bundling the .so files
- Do not install the tmp/ folder left over after building qt5pas

* Fri Oct 11 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.4-3
- This time really fix the qt5pas and qt5pas-devel nvr mismatch

* Wed Aug 14 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.4-2
- Fix qt5pas and qt5pas-devel nvr mismatch

* Tue Aug 13 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.4-1
- Update to upstream version 2.0.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.2-1
- Update to upstream version 2.0.2
- Drop .1 from qt5pas release numbers

* Fri Feb 08 2019 Artur Iwicki <fedora@svgames.pl> - 2.0.0-1
- Update to upstream version 2.0.0
- Drop the .desktop file patch (issues fixed upstream)
- Drop the "Disable PascalScript on PowerPC64" patch (we no longer ship ppc64 fpc/lazarus)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Artur Iwicki <fedora@svgames.pl> - 1.8.4-2
- Use Lazarus version number to auto-calculate the qt5pas release number
  This should prevent build failures in koji due to duplicate qt5pas version-release tags.

* Sat Aug 18 2018 Artur Iwicki <fedora@svgames.pl> - 1.8.4-1
- Update to new upstream version

* Tue Aug 07 2018 Artur Iwicki <fedora@svgames.pl> - 1.8.2-3
- Add the Qt5pas package (pull request #3)
- Remove the Group: tag (no longer used in Fedora)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 5 2018 Joost van der Sluis <joost@cnoc.nl> - 1.8.2-1
- Update to upstream version 1.8.2

* Sat Feb 24 2018 Artur Iwicki <fedora@svgames.pl> - 1.8.0-1
- Update to upstream version 1.8.0
- Remove obsolete scriplets (icon cache update)
- Use the %license tag instead of %doc for licence files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Joost van der Sluis <joost@cnoc.nl> - 1.6.4-1
- Updated to version 1.6.4

* Wed Feb 8 2017 Joost van der Sluis <joost@cnoc.nl> - 1.6.2-3
- Disable PascalScript on Powerpc64

* Sat Feb 04 2017 Björn Esser <besser82@fedoraproject.org> - 1.6.2-2
- Rebuilt for changes in 'ExclusiveArch: %%{fpc_arches}'

* Sun Jan 29 2017 Joost van der Sluis <joost@cnoc.nl> - 1.6.2-1
- Compile exclusively on platforms supported by fpc (rhbz#1247925)

* Thu Jan 26 2017 Joost van der Sluis <joost@cnoc.nl> - 1.6.2-0
- Updated to version 1.6.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-0.2.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Joost van der Sluis <joost@cnoc.nl> - 1.6-0.1.RC1
- Updated to version 1.6RC1

* Sun Dec 20 2015 Joost van der Sluis <joost@cnoc.nl> - 1.4.4-1
- Updated to version 1.4.4

* Mon Jul 20 2015 Joost van der Sluis <joost@cnoc.nl> - 1.4.2-1
- Updated to version 1.4.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Joost van der Sluis <joost@cnoc.nl> - 1.4-1
- Updated to version 1.4

* Mon Mar 9 2015 Joost van der Sluis <joost@cnoc.nl> - 1.4-0.1.RC2
- Updated to version 1.4RC2
- Fixed invalid dates in changelog

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2-4
- update scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Joost van der Sluis <joost@cnoc.nl> - 1.2-1
- Updated to version 1.2

* Fri Mar 28 2014 Joost van der Sluis <joost@cnoc.nl> - 1.0.14-1
- Updated to version 1.0.14

* Mon Aug 12 2013 Joost van der Sluis <joost@cnoc.nl> - 1.0.8-4
- Rebuilt for Free Pascal with arm-support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.8-2
- Perl 5.18 rebuild

* Thu Apr 25 2013 Joost van der Sluis <joost@cnoc.nl> - 1.0.8-1
- Updated to version 1.0.8

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 1.0.4-3
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.30.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Joost van der Sluis <joost@cnoc.nl> - 0.9.30.4-1
- Updated to version 0.9.30.4
- Use default fonts, editoroptions.xml file removed

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Apr 27 2011 Joost van der Sluis <joost@cnoc.nl> - 0.9.30-1
- Updated to version 0.9.30
- Remove the obsolete .spec BuildRoot tag.
- Do not install manfiles for executables which are not in the path

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec 05 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.9.28.2-2
- Fix LazarusVersion substitution in configuration
- Do not compress manpages in %%build, RPM does this for us

* Wed May 19 2010 Joost van der Sluis <joost@cnoc.nl> - 0.9.28.2-1
- Updated to version 0.9.28.2

* Fri Oct 16 2009 Joost van der Sluis <rel-eng@lists.fedoraproject.org> - 0.9.28-1
- Updated to version 0.9.28

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.26.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Dan Horak <dan[at]danny.cz> 0.9.26.2-3
- Exclude s390/s390x architectures, FPC doesn't exist there

* Wed Apr 1 2009 Joost van der Sluis <joost@cnoc.nl> 0.9.26.2-2
 - Adapted Makefile patch for version 0.9.26.2

* Wed Apr 1 2009 Joost van der Sluis <joost@cnoc.nl> 0.9.26.2-1
 - Updated to version 0.9.26.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> 0.9.26-3
- Include /etc/lazarus directory.

* Wed Oct 29 2008 Lubomir Rintel <lkundrak@v3.sk> 0.9.26-2
- Fix path to the source tree

* Thu Oct 23 2008 Joost van der Sluis <joost@cnoc.nl> 0.9.26-1
- Updated to version 0.9.26
- Removed scripts which are vulnerable to symlink-attacks (bug 460642)
- Build bigide instead of the standard ide
- Build ideintf and the registration for gtk2
- Install the manfiles
- Install the mime-types
- Install the global .xml configuration files

* Wed Jun 18 2008 Joost van der Sluis <joost@cnoc.nl> 0.9.24-4
- removed the trailing slash from the FPCDIR export in the build section

* Thu Apr 24 2008 Joost van der Sluis <joost@cnoc.nl> 0.9.24-3
- Remove executable-bit in install-section, instead of the files section
- Enabled debug-package on x86_64

* Fri Feb 01 2008 Joost van der Sluis <joost@cnoc.nl> 0.9.24-2
- Changed license-tag according to the official license tags of Fedora
- Removed some more Debian-specific files
- Made two scripts executable
- Improved fedora-lazarus.desktop

* Mon Nov 26 2007 Joost van der Sluis <joost@cnoc.nl> 0.9.24-1
- Removed files specific for debian
- Updated to Lazarus v 0.9.24
- Changed desktop-file categories
- Disabled the debug-package for x86_64 again, see bug 337051
- If the debuginfo-packages is disabled, strip the executables manually
- Require fpc version 2.2.0
- Added -q to setup-macro
- Added OPT='-gl' option in build-section, to make sure that the debuginfo is generated by the compiler
- Removed explicit creation of {buildroot}{_mandir}/man1 and {buildroot}{_datadir}/applications
- Lazarus executable is renamed to lazarus-ide (changed upstream)

* Thu Jan 4 2007 Joost van der Sluis <joost@cnoc.nl> 0.9.20-2
- Added fpc-src as build-dependency to fix problem with fpcmake

* Tue Jan 2 2007 Joost van der Sluis <joost@cnoc.nl> 0.9.20-1
- Version 0.9.20

* Wed Oct 4 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.18-2
- Use the makefile for installing

* Wed Sep 20 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.18-1
- Updated to version 0.9.18.
- Removed obsolete copying of documentation
- Removed double requirements
- Removed part to remove debuginfo package

* Thu Jun 1 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.16-1
- Updated to version 0.9.16.

* Thu May 25 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.14-5
- Added /usr/bin/startlazarus for packaging
- Removed strip in build-section
- added gtk2-devel buildrequirement

* Tue May 23 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.14-4
- Only build the basic IDE, to remove dependencies on things which are buggy in fpc 2.0.2

* Thu May 4 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.14-3
- Added the ability to create gtk2-applications

* Thu May 4 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.14-2
- Updated to version 0.9.14-1.
- Changed the Source0 download url from prdownloads to
  downloads.sourceforge.net

* Mon Apr 10 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.14-1
- Updated to version 0.9.14.

* Tue Mar 28 2006 Joost van der Sluis <joost@cnoc.nl> 0.9.12-1
- Initial build.

