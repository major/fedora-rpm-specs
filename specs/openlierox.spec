%define prever rc5

Name:           openlierox
# Because we downgraded from 0.59 to 0.58 as 0.59 never became stable
Epoch:          1
Version:        0.58
Release:        0.36.%{prever}%{?dist}
Summary:        Addictive realtime multi-player 2D shoot-em-up
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://openlierox.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/OpenLieroX_%{version}_%{prever}.src.tar.bz2
Source1:        %{name}.desktop
Source2:        README.fedora
Patch1:         openlierox-gcc13.patch
Patch2:         openlierox-libxml2-buildfix.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL_mixer-devel SDL_image-devel gd-devel
BuildRequires:  libxml2-devel zlib-devel desktop-file-utils libappstream-glib
BuildRequires:  libzip-devel curl-devel binutils-devel cmake
BuildRequires:  hawknl-devel >= 1.68-22
# rhbz#818911
BuildRequires:  binutils-static
Requires:       hicolor-icon-theme
# for people who try to install this using upstream capitalization
Provides:       OpenLieroX = %{version}-%{release}

%description
OpenLierox is an extremely addictive realtime multi-player 2D shoot-em-up
backed by an active gaming community. Dozens of levels and mods are available
to provide endless gaming pleasure.


%prep
%autosetup -p1 -n OpenLieroX
sed -i 's/\r//g' doc/original_lx_docs/*.*
cp -a %{SOURCE2} .
# Remove bundled libs to ensure they are not used
for i in libs/*; do
    if [ "$i" = "libs/pstreams" -o "$i" = "libs/linenoise" ]; then
        # Except for the pstreams and linenoise copylibs
        continue
    fi
    rm -r "$i"
done
# Remove execute permissions from various data files
find -type f -print0 | xargs -0 chmod -x
# Drop obsolete Python 2 scripts which are only for people running a
# dedicated server (which we do not package)
rm -rf share/gamedir/scripts share/gamedir/cfg/*.py


%build
%cmake -DDEBUG=OFF -DHAWKNL_BUILTIN=OFF -DBREAKPAD=OFF -DSYSTEM_DATA_DIR=%{_datadir}
# The CMakefile is not written with out of tree builds in minds. It expects
# this dir, which is part of the source-tree, to be present
mkdir %{_vpath_builddir}/bin
%cmake_build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/OpenLieroX
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 755 %{_vpath_builddir}/bin/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -pr share/gamedir/* $RPM_BUILD_ROOT%{_datadir}/OpenLieroX
install -p -m 644 doc/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 share/OpenLieroX.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 share/%{name}.appdata.xml \
  $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc README.fedora doc/original_lx_docs/*
%license COPYING.LIB
%{_bindir}/%{name}
%{_datadir}/OpenLieroX
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.36.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.58-0.35.rc5
- convert license to SPDX

* Mon Jul 29 2024 Hans de Goede <hdegoede@redhat.com> - 1:0.58-0.34.rc5
- Fix FTBFS (rhbz#2261428)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.33.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.32.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.31.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.30.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 27 2023 Hans de Goede <hdegoede@redhat.com> - 1:0.58-0.29.rc5
- Fix FTBFS (rhbz#2171632)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.28.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.27.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.26.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.25.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.24.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Hans de Goede <hdegoede@redhat.com> - 1:0.58-0.23.rc5
- Fix FTBFS, somewhat non-trivial cmake macro fix (rhbz#1865161)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.22.rc5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.21.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.20.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 Hans de Goede <hdegoede@redhat.com> - 1:0.58-0.19.rc5
- Drop obsolete Python 2 scripts which are only for people running a
  dedicated server (which we do not package) (rhbz#1738061)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.18.rc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 19 2019 Hans de Goede <hdegoede@redhat.com> - 1:0.58-0.17.rc5
- New upstream release 0.58-rc5
- Switch to upstream appdata
- Fix FTBFS (rhbz#1675580)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.16.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.15.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.14.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.58-0.13.rc3
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.12.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.11.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.58-0.10.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 28 2017 Remi Collet <remi@fedoraproject.org> - 1:0.58-0.9.rc3
- rebuild for new libzip

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.8.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 20 2016 Hans de Goede <hdegoede@redhat.com> - 1:0.58-0.7.rc3
- Fix FTBFS (rhbz#1307823)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.58-0.6.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.58-0.5.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Remi Collet <remi@fedoraproject.org> - 1:0.58-0.4.rc3
- rebuild for new libzip

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1:0.58-0.3.rc3
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:0.58-0.2.rc3
- Add an AppData file for the software center

* Fri Jan 16 2015 Hans de Goede <hdegoede@redhat.com> - 1:0.58-0.1.rc3
- 0.59 never left the beta phase and is rather buggy, so most openlierox
  community member play 0.58, downgrade to 0.58 to allow online playing

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-0.20.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-0.19.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.59-0.18.beta10
- Rebuild for boost 1.55.0

* Wed Aug 21 2013 Remi Collet <rcollet@redhat.com> - 0.59-0.17.beta10
- rebuild for new libzip

* Mon Aug 05 2013 Hans de Goede <hdegoede@redhat.com> - 0.59-0.16.beta10
- Don't try to build the mmx code on non x86 (ie arm)

* Sun Aug 04 2013 Hans de Goede <hdegoede@redhat.com> - 0.59-0.15.beta10
- Build with compat-lua on f20+
- Fix crash on startup (rhbz#916407)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-0.14.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.59-0.13.beta10
- Rebuild for boost 1.54.0

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 0.59-0.12.beta10
- rebuild for new GD 2.1.0

* Tue Apr 30 2013 Jon Ciesla <limburgher@gmail.com> - 0.59-0.11.beta10
- Drop desktop vendor tag.

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.59-0.10.beta10
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.59-0.9.beta10
- Rebuild for Boost-1.53.0

* Sun Aug 12 2012 Hans de Goede <hdegoede@redhat.com> - 0.59-0.8.beta10
- Rebuilt for new boost

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-0.7.beta10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 16 2012 Hans de Goede <hdegoede@redhat.com> - 0.59-0.6.beta10
- Add BuildRequires: binutils-static for Static Library Packaging Guidelines
  adherence (rhbz#818911)

* Fri Apr 20 2012 Hans de Goede <hdegoede@redhat.com> - 0.59-0.5.beta10
- New upstream release 0.59-beta10

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-0.4.beta9
- Rebuilt for c++ ABI breakage

* Sat Feb 04 2012 Remi Collet <remi@fedoraproject.org> - 0.59-0.3.beta9
- rebuild for new libzip

* Thu Jan 19 2012 Hans de Goede <hdegoede@redhat.com> - 0.59-0.2.beta9
- Drop always_inline macro it is not used anywhere and is causing compilation
  issues with recent boost versions (also see rhbz#781859)

* Sun Jan 15 2012 Hans de Goede <hdegoede@redhat.com> - 0.59-0.1.beta9
- New upstream release 0.59-beta9
- Fix building with gcc-4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-0.17.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-0.16.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.57-0.15.beta8
- recompiling .py files against Python 2.7 (rhbz#623342)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-0.14.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Hans de Goede <hdegoede@redhat.com> 0.57-0.13.beta8
- Fix building with bash 4.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-0.12.beta8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.57-0.11.beta8
- Rebuild for Python 2.6

* Mon Oct 20 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.10.beta8
- New upstream release 0.57beta8

* Sun Mar 16 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.9.beta5
- New upstream release 0.57beta5

* Mon Feb 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.8.beta4
- New upstream release 0.57beta4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.57-0.7.beta3
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.6.beta3
- Rebuild for buildId

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.5.beta3
- New upstream release 0.57beta3
- Update License tag for new Licensing Guidelines compliance

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 0.57-0.4.beta2
- Rebuild against SDL_gfx 2.0.16.

* Fri Apr 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.3.beta2
- New upstream release 0.57beta2

* Thu Mar 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.2.beta1
- Various specfile fixes from review (bz 232071)
- Source instead of execute the bash scripts to avoid umask problems

* Mon Mar 12 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.57-0.1.beta1
- Initial Fedora Extras package
