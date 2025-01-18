Name:          crrcsim
Version:       0.9.13
Release:       24%{?dist}
Summary:       Model-Airplane Flight Simulation Program
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           http://sourceforge.net/apps/mediawiki/crrcsim/
Source0:       http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# upstream report: http://preview.tinyurl.com/bnryakb
Patch0:        %{name}-0.9.13-support-for-platforms-without-sys-io.h.patch
# aarch64 support added
# upstream report: http://preview.tinyurl.com/cass62h
Patch1:        %{name}-0.9.13-aarch64-support-added.patch
# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1307411
# upstream report: https://sourceforge.net/p/crrcsim/bugs/35/
Patch2:        %{name}-0.9.13-gcc-7-fixes.patch
# hg export -r 1554 >crrcsim-0.9.13-issue-41.patch
# fix fof rhbz#1575624
Patch3:        %{name}-0.9.13-issue-41.patch
# Fix compilation with CGAL >5.x
# upstream report: https://sourceforge.net/p/crrcsim/bugs/44/
Patch4:        %{name}-0.9.13-cgal-header-mode-only.patch

# It is only meant for development purposes.
%global build_with_cmake %{?_with_cmake:1}%{!?_with_cmake:0}

%global the_desktop_file packages/Fedora/CRRCsim.desktop
%global the_icon_file %{_datadir}/%{name}/icons/%{name}.png


%if %{build_with_cmake}
BuildRequires: cmake
%endif
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: /usr/bin/git
BuildRequires: portaudio-devel
BuildRequires: SDL-devel
BuildRequires: freeglut-devel
BuildRequires: plib-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: CGAL-devel
BuildRequires: desktop-file-utils
BuildRequires: make


%description
Crrcsim is a model-airplane flight simulation program.
Using it, you can learn how to fly model aircraft, test new aircraft designs,
and improve your skills by practicing on your computer.

The flight model is very realistic.
The flight model parameters are calculated based on a 3D representation
of the aircraft. Stalls are properly modeled as well.
Model control is possible with your own RC transmitter, or any input device
such as joystick, mouse, keyboard.


%package doc
Summary:       Documentation for %{name}
BuildArch:     noarch


%description doc
Documentation for %{name} package.


%prep
%autosetup -S git

# Correct EOL.
for i in \
    documentation/input_method/PARALLEL_1_to_3/crrcsim_at90s1200.hex \
    documentation/models/*.txt \
    documentation/Install_Win32.txt \
    documentation/dlportio.txt; do
        sed -i 's#\r##g' $i;
done

# Remove executable permission.
chmod a-x src/mod_landscape/heightdata.h

# Correct file encoding.
for i in documentation/thermals/table*.cpp; do
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,} && mv $i{.utf8,}
done

# Desktop file: correct the icon file location.
sed -i 's#^\(Icon.*=\).*#\1%{the_icon_file}#g' %{the_desktop_file}

# Desktop file: correct categories.
# Reported upstream: http://preview.tinyurl.com/cep8rvp
sed -i 's#^\(Categories=\).*#\1Game;Simulation;#g' %{the_desktop_file}

# Desktop file: remove deprecated "Encoding" key.
# Reported upstream: http://preview.tinyurl.com/cep8rvp
sed -i 's#^Encoding=.*##g' %{the_desktop_file}

# Minimal approach to satisfy the linker.
# Reported upstream: http://preview.tinyurl.com/d3cg4s2
sed -i 's#-lboost_thread-mt#-lboost_thread#g' Makefile.in configure

%if %{build_with_cmake}
# Remove reference to not existing file.
sed -i 's#\(.*m44_test.*\)#\#\1#g' src/mod_math/CMakeLists.txt
%endif


%build
%if %{build_with_cmake}
 mkdir -p build
 pushd build
 %cmake ..
 make %{?_smp_mflags}
 popd
%else
 %configure
 make %{?_smp_mflags}
%endif


%install
make DESTDIR=%{buildroot} install
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{the_desktop_file}
rm -f %{buildroot}%{_datadir}/%{name}/icons/%{name}.{ico,xpm}
%find_lang %{name} --with-man

# adding to installed docs in order to avoid using %%doc magic
for f in AUTHORS COPYING HISTORY ; do
    cp -p $f %{buildroot}%{_docdir}/%{name}/${f}
done

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/CRRCsim.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/crrcsim/feature-requests/37/
SentUpstream: 2014-07-11
-->
<application>
  <id type="desktop">CRRCsim.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>Charles River RC Flight Simulator</name>
  <summary>Flight simulator for model remote controlled aircraft</summary>
  <description>
    <p>
      The Charles River RC Flight Simulator (CRRCSim) is a flight simulator to
      test fly model aircraft.
      CRRCSim comes with over 15 different types of model gliders and planes, and
      lets you fly in 3 different locations.
    </p>
  </description>
  <url type="homepage">https://sourceforge.net/projects/crrcsim/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/CRRCsim/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/CRRCsim/b.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%{_bindir}/crrcsim
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/CRRCsim.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/HISTORY


%files doc
# all documentation in this package (including the license)
%{_docdir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.13-23
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.13-12
- Use CGAL (>=5.0x) in header mode only

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 0.9.13-8
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.13-6
- Fix for rhbz#1575624

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.13-5
- Add missing BR (gcc, gcc-c++).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.9.13-3
- Rebuilt for Boost 1.66

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.13-2
- Remove obsolete scriptlets

* Thu Dec 21 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.13-1
- Update to the latest avilable version (rhbz#1510107)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.12-27
- Rebuilt for Boost 1.64

* Sun Jun 04 2017 Miro Hrončok <mhroncok@redhat.com> - 0.9.12-26
- Rebuilt for new CGAL

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.9.12-23
- Rebuilt for Boost 1.63

* Mon Sep 26 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.12-22
- Rebuilt for new CGAL

* Tue Mar 29 2016 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.12-21
- Fixes gcc 6 compilation, RHBZ#1307411

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.12-19
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.9.12-18
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 0.9.12-17
- Rebuilt for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.12-15
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.12-14
- Add an AppData file for the software center

* Fri Mar 06 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.12-13
- Rebuild for libCGAL.so.11.

* Mon Feb 09 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9.12-12
- Rebuild for boost-1.57.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.9.12-9
- rebuild for boost 1.55.0

* Mon Apr 28 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.12-8
- BR corrected.

* Sat Dec 14 2013 Michael Schwendt <mschwendt@fedoraproject.org>
- Fix duplicate documentation (#1001277)
- Simplify the %%files list
- Drop base package dependency from -doc subpackage

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.9.12-6
- Rebuild for boost 1.54.0
- Link against -lboost_thread, the -mt variant is not shipped anymore.

* Sat Mar 23 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.12-5
- aarch64 support added, fixes #925200
- updating icon cache scriplets added

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.12-4
- Rebuild for Boost-1.53.0

* Fri Feb 01 2013 Dan Horák <dan[at]danny.cz> - 0.9.12-3
- fix build on platforms without io.h

* Tue Jan 29 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.12-2
- doc subpackage BuildArch adn Requires corrected.

* Tue Jun 12 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.12-1
- initial RPM release.
