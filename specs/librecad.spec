# Changes incorporated from Rallaz's spec file, which is
#
# Copyright (c) 2010-2012 Rallaz
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

%global commit 17041794360634e063c644aa355d5b7e354abd54
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global dxfrw_includedir %(%___build_pre; pkg-config --cflags-only-I libdxfrw | sed 's|-I||g')

Name:			librecad
Version:		2.2.0.2
Release:		6%{?dist}
Summary:		Computer Assisted Design (CAD) Application
License:		GPL-2.0-only AND GPL-2.0-or-later
URL:			http://librecad.org/
Source0:		https://github.com/LibreCAD/LibreCAD/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:		ttf2lff.1
# GPL licensed parts files
Source2:		Architect8-LCAD.zip
Source3:		Electronic8-LCAD.zip
Patch0:			librecad-use-system-libdxfrw.patch
Patch2:			librecad-install.patch
Patch3:			librecad-plugindir.patch
# Patch4:		librecad-use-system-shapelib.patch
Patch6:			librecad-gcc6.patch
# need to use unique symbol names
Patch8:			librecad-unique-symbol-names.patch

BuildRequires:	gcc-c++ make
BuildRequires:	qt5-qtbase-devel, wqy-microhei-fonts, muParser-devel, freetype-devel, libdxfrw-devel >= 1.1.0-0.2.rc1
BuildRequires:	qt5-qtsvg-devel, qt5-linguist
BuildRequires:	desktop-file-utils, boost-devel, shapelib-devel
Requires:		%{name}-fonts = %{version}-%{release}
Requires:		%{name}-langs = %{version}-%{release}
Requires:		%{name}-parts = %{version}-%{release}
Requires:		%{name}-patterns = %{version}-%{release}
# needed for LibreCad specific changes
Requires:		libdxfrw >= 1.1.0-0.2.rc1

# Do not check any files in the librecad plugin dir for requires
%global __provides_exclude_from ^(%{_libdir}/%{name}/plugins/.*\\.so)$

%description
A graphical and comprehensive 2D CAD application.

%package devel
Summary:	Development files for LibreCAD
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for LibreCAD.

%package fonts
Summary:	Fonts in LibreCAD (lff) format
# Amiri Regular - SIL OFL 1.1
# AZOmix - KST32B 2.0 (LicenseRef-Fedora-UltraPermissive)
# cursive - GPL-2.0-or-later
# cyrillic_ii - GPL-2.0-or-later
# gothgbt - GPL-2.0-or-later
# gothgrt - GPL-2.0-or-later
# gothitt - GPL-2.0-or-later
# greekc - GPL-2.0-or-later
# greekcs - LicenseRef-Fedora-Public-Domain
# greek_ol - GPL-2.0-or-later
# greekp - LicenseRef-Fedora-Public-Domain
# greeks - GPL-2.0-or-later
# iso3098_i - GPL-2.0-or-later
# iso3098 - GPL-2.0-or-later
# iso - GPL-2.0-or-later
# italicc - GPL-2.0-or-later
# italiccs - LicenseRef-Fedora-Public-Domain
# italict - GPL-2.0-or-later
# kochigothic - LicenseRef-Fedora-Public-Domain
# kochimincho - LicenseRef-Fedora-Public-Domain
# kst3b - LicenseRef-Fedora-UltraPermissive AND GPL-2.0-or-later
# lc_opengost-* - SIL OFL 1.1
# opengosttypea - SIL OFL 1.1
# opengosttypeb - SIL OFL 1.1
# romanc - LicenseRef-Fedora-Public-Domain
# romancs - LicenseRef-Fedora-Public-Domain
# romand - LicenseRef-Fedora-Public-Domain
# romanp - LicenseRef-Fedora-Public-Domain
# romansi - LicenseRef-Fedora-Public-Domain
# romans - GPL-2.0-or-later
# romant - LicenseRef-Fedora-Public-Domain
# scriptc - LicenseRef-Fedora-Public-Domain
# scripts - LicenseRef-Fedora-Public-Domain
# simplex - GPL-2.0-or-later
# standard - GPL-2.0-or-later
# syastro - GPL-2.0-or-later
# symap - GPL-2.0-or-later
# symbol - GPL-2.0-or-later
# symbol_misc1 - LicenseRef-Fedora-Public-Domain
# symbol_misc2 - LicenseRef-Fedora-Public-Domain
# symteo - GPL-2.0-or-later
# symusic - GPL-2.0-or-later
# unicode - GPL-2.0-or-later
# wqy-microhei - Apache-2.0 OR GPL-3.0-only WITH Font-exception-2.0

License:	GPL-2.0-or-later AND LicenseRef-Fedora-UltraPermissive AND OFL-1.1 AND LicenseRef-Fedora-Public-Domain AND (LicenseRef-Fedora-UltraPermissive AND GPL-2.0-or-later) AND (Apache-2.0 OR GPL-3.0-only WITH Font-exception-2.0)
BuildArch:	noarch

%description fonts
Fonts converted to LibreCAD (lff) format.

%package langs
Summary:	Language (qm) files for LibreCAD
BuildArch:	noarch

%description langs
Language (qm) files for	LibreCAD.

%package parts
Summary:	Parts collection for LibreCAD
BuildArch:	noarch

%description parts
Collection of parts for LibreCAD.

%package patterns
Summary:	Pattern files for LibreCAD
BuildArch:	noarch

%description patterns
Pattern files for LibreCAD.


%prep
%setup -qn LibreCAD-%{commit} -a 2 -a 3
%patch -P0 -p1 -b .system
# %%patch2 -p1 -b .install
%patch -P3 -p1
# %%patch4 -p1 -b .system-shapelib
%patch -P6 -p1 -b .gcc6
# %%patch8 -p1 -b .unique
sed -i 's|##LIBDIR##|%{_libdir}|g' librecad/src/lib/engine/rs_system.cpp
sed -i 's|$${DXFRW_INCLUDEDIR}|%{dxfrw_includedir}|g' librecad/src/src.pro

## Fix plugin search path
#sed -i 's|"/../share/"|"/../%{_lib}/"|'  librecad/src/lib/engine/rs_system.cpp

# Nuke bundled libraries
# rm -rf libraries/libdxfrw
# rm -rf plugins/importshp/shapelib

# unset +x flags on some source files
for i in plugins/*/*.cpp plugins/*/*.h librecad/src/plugins/qc_plugininterface.h; do
  chmod -x $i
done

# copy font licenses here
%if 0%{?epel} == 7
cp /usr/share/doc/wqy-microhei-fonts*/LICENSE_* .
%else
cp /usr/share/licenses/wqy-microhei-fonts/LICENSE_* .
%endif

sed -i 's|LRELEASE="lrelease"|LRELEASE="lrelease-qt5"|g' scripts/postprocess-unix.sh

# Fix the version string
sed -i 's|LC_VERSION="2.2.0-undef"|LC_VERSION="%{version}"|g' librecad/src/src.pro

%build
%{qmake_qt5} librecad.pro 'CONFIG+=release' 'BOOST_DIR=%{_prefix}' 'BOOST_LIBDIR=%{_libdir}' 'MUPARSER_DIR=%{_prefix}' 'QMAKE_LFLAGS_RELEASE=' 'DISABLE_POSTSCRIPT=true'

make %{?_smp_mflags} MUPARSER_DIR=%{_prefix}
rm -rf unix/resources/fonts/wqy-unicode.lff
mkdir -p unix/resources/fonts
./unix/ttf2lff -L "Apache-2.0 OR GPL-3.0-only WITH Font-exception-2.0" /usr/share/fonts/wqy-microhei-fonts/wqy-microhei.ttc unix/resources/fonts/wqy-unicode.lff


%install
export BUILDDIR="%{buildroot}%{_datadir}/%{name}"
sh scripts/postprocess-unix.sh

mkdir -p %{buildroot}%{_libdir}/%{name}/plugins
mv unix/resources/plugins/* %{buildroot}%{_libdir}/%{name}/plugins/
%{__install} -Dpm 755 -s unix/%{name} %{buildroot}%{_bindir}/%{name}
%{__install} -Dpm 755 -s unix/ttf2lff %{buildroot}%{_bindir}/ttf2lff
%{__install} -Dpm 644 desktop/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
#%{__install} -Dpm 644 unix/appdata/%{name}.appdata.xml  %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%{__install} -Dpm 644 librecad/res/main/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -Dpm 644 desktop/%{name}.sharedmimeinfo %{buildroot}%{_datadir}/mime/packages/%{name}.xml
%{__install} -Dpm 644 desktop/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%{__install} -Dpm 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/ttf2lff.1
%{__install} -Dpm 644 librecad/src/plugins/document_interface.h %{buildroot}%{_includedir}/%{name}/document_interface.h
%{__install} -Dpm 644 librecad/src/plugins/qc_plugininterface.h %{buildroot}%{_includedir}/%{name}/qc_plugininterface.h
mkdir -p %{buildroot}%{_datadir}/%{name}/fonts
cp -a unix/resources/fonts/*.lff %{buildroot}%{_datadir}/%{name}/fonts/
mkdir -p %{buildroot}%{_datadir}/%{name}/qm
cp -a unix/resources/qm/* %{buildroot}%{_datadir}/%{name}/qm/
mkdir -p %{buildroot}%{_datadir}/%{name}/library
cp -a unix/resources/library/* %{buildroot}%{_datadir}/%{name}/library/
mkdir -p %{buildroot}%{_datadir}/%{name}/patterns
cp -a unix/resources/patterns/* %{buildroot}%{_datadir}/%{name}/patterns/


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
BugReportURL: https://sourceforge.net/p/librecad/feature-requests/158/
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">librecad.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>2D Computer Aided Design (CAD)</summary>
  <description>
    <p>
      LibreCAD is an 2D Computer Aided Design (CAD) application for creating plans
      and designs on your computer.
      It can be used to make  accurate 2D representations of floorplans, part designs,
      and just about anything that can be represented as a flat 2D plan.
    </p>
  </description>
  <url type="homepage">http://librecad.org/</url>
  <screenshots>
    <screenshot type="default">http://wiki.librecad.org/images/f/f8/Lcnotclosed.png</screenshot>
  </screenshots>
</application>
EOF

mkdir -p %{buildroot}%{_datadir}/%{name}/library/architecture
cp -a Architect8-LCAD %{buildroot}%{_datadir}/%{name}/library/architecture

mkdir -p %{buildroot}%{_datadir}/%{name}/library/electronics
cp -a Electronic8-LCAD %{buildroot}%{_datadir}/%{name}/library/electronics

%{_fixperms} %{buildroot}

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%license LICENSE
%doc README.md
%doc %{_mandir}/man1/%{name}.1*
%doc %{_mandir}/man1/ttf2lff.1*
%{_bindir}/%{name}
%{_bindir}/ttf2lff
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_libdir}/%{name}/

%files devel
%{_includedir}/%{name}/

%files fonts
%doc LICENSE LICENSE_Apache2.txt LICENSE_GPLv3.txt
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/fonts/

%files langs
%doc LICENSE
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/qm/

%files parts
%doc LICENSE
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/library/

%files patterns
%doc LICENSE
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/patterns/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 11 2024 Tom Callaway <spot@fedoraproject.org> - 2.2.0.2-4
- fix font licensing tags

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug  3 2023 Tom Callaway <spot@fedoraproject.org> - 2.2.0.2-1
- make sure LC_VERSION is set properly
- update to 2.2.0.2
- fix license tags

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Tom Callaway <spot@fedoraproject.org> - 2.2.0-1
- update to 2.2.0 final

* Sat Sep 24 2022 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-0.15.rc4
- Update to 2.2.0 RC4.
- Apply patch from upstream to make sure plugins are found.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.14.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  1 2022 Tom Callaway <spot@fedoraproject.org> - 2.2.0-0.13.rc3
- update to rc3
- apply upstream fix for CVE-2021-45342, CVE-2021-45341

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.12.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 22 2021 Tom Callaway <spot@fedoraproject.org> - 2.2.0-0.11.rc2
- rebuild against new libdxfrw
- rebase to 1d31427

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.10.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.9.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Tom Callaway <spot@fedoraproject.org> - 2.2.0-0.8.rc2
- update to rc2

* Wed Nov  4 2020 Tom Callaway <spot@fedoraproject.org> - 2.2.0-0.7.rc1
- update to latest git main

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.6.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.5.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.4.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun  6 2019 Tom Callaway <spot@fedoraproject.org> - 2.2.0-0.3.rc1
- apply fix for non-unique shared object naming conflicts

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 2.2.0-0.1.rc1
- update to 2.2.0-rc1
- add BuildRequires: gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.1.0-3
- Rebuilt for Boost 1.63

* Sun Dec 11 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.0-2
- Rebuild for shapelib SONAME bump

* Mon Jun  6 2016 Tom Callaway <spot@fedoraproject.org> - 2.1.0-1
- update to 2.1.0

* Mon May 16 2016 Tom Callaway <spot@fedoraproject.org> - 2.0.10-1
- update to 2.0.10

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.0.9-2
- Rebuilt for Boost 1.60

* Tue Jan 12 2016 Tom Callaway <spot@fedoraproject.org> - 2.0.9-1
- update to 2.0.9

* Fri Sep 11 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.8-1
- update to 2.0.8

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.0.7-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.0.7-6
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.7-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.0.7-3
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2.0.7-2
- Rebuild for boost 1.57.0

* Mon Jan  5 2015 Tom Callaway <spot@fedoraproject.org> - 2.0.7-1
- update to 2.0.7

* Wed Nov  5 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.6-1
- update to 2.0.6

* Thu Sep 11 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.5-2
- add Architect8 and Electronic8 parts libraries

* Mon Aug 18 2014 Richard Shaw <hobbes1069@gmail.com> - 2.0.5-1
- Update to latest upstream release.

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 2.0.4-4
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun  2 2014 Richard Shaw <hobbes1069@gmail.com> - 2.0.4-1
- Update to latest upstream release.

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2.0.3-2
- Rebuild for boost 1.55.0

* Fri May  2 2014 Richard Shaw <hobbes1069@gmail.com> - 2.0.3-1
- Update to 2.0.3.

* Wed Jan 22 2014 Tom Callaway <spot@fedoraproject.org> - 2.0.2-1
- update to 2.0.2

* Sun Oct 20 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.6.rc2
- add missing LICENSE files to subpackages
- add dir ownership to subpackages
- readd all mime scriptlets

* Sun Oct 20 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.5.rc2
- fix mime-type desktop scriptlets
- unbundle shapelib
- do not have provides for unversioned plugins
- fix permissions
- nuke unused code
- make patterns and langs noarch subpackages
- preserve timestamps in install commands
- fix link flags to not have -O1 by overriding 

* Fri Oct 18 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.4.rc2
- update to rc2

* Tue Apr 30 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.3.beta5
- add BR: boost-devel
- update to beta5

* Tue Apr  9 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.2.beta2
- update to beta2

* Sun Feb 24 2013 Tom Callaway <spot@fedoraproject.org> - 2.0.0-0.1.beta1
- initial package
