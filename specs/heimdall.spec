Name:           heimdall
Version:        2.1.0
Release:        2%{?dist}
Summary:        Flash firmware on to Samsung Galaxy S devices
License:        MIT
URL:            https://git.sr.ht/~grimler/Heimdall
Source0:        https://git.sr.ht/~grimler/Heimdall/archive/v%{version}.tar.gz
Source2:        %{name}.desktop

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  libusb1-devel >= 1.0.8
BuildRequires:  zlib-devel
BuildRequires:  desktop-file-utils

%description
Heimdall is a cross-platform open-source utility to flash firmware
on to Samsung Galaxy S devices

%package frontend
Summary:        Qt4 based frontend for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description frontend
Heimdall is a cross-platform open-source utility to flash firmware
on to Samsung Galaxy S devices

This package provides Qt5 based frontend for %{name}

%prep
%autosetup -n Heimdall-v%{version}

#remove unneeded files
rm -rf Win32
rm -rf OSX

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}
install -D -m 0755 %{_vpath_builddir}/bin/heimdall %{buildroot}%{_bindir}/heimdall
install -D -m 0755 %{_vpath_builddir}/bin/heimdall-frontend %{buildroot}%{_bindir}/heimdall-frontend
install -D -m 0644 heimdall/60-heimdall.rules %{buildroot}%{_udevrulesdir}/60-heimdall.rules
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE2}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p %{buildroot}%{_datadir}/appdata
cat > %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!--
EmailAddress: contact@glassechidna.com.au
SentUpstream: 2014-09-18
-->
<application>
 <id type="desktop">heimdall.desktop</id>
 <metadata_license>CC0-1.0</metadata_license>
 <project_license>MIT</project_license>
 <name>Heimdall</name>
 <summary>Flash firmware onto Samsung mobile devices</summary>
 <description>
  <p>
   Heimdall is a cross-platform open-source tool suite used to flash
   firmware (aka ROMs) onto Samsung mobile devices.
  </p>
 </description>
 <screenshots>
  <screenshot type="default" width="1275" height="718">http://jorti.fedorapeople.org/appdata/heimdall.png</screenshot>
 </screenshots>
 <url type="homepage">http://glassechidna.com.au/heimdall/</url>
 <url type="donation">http://glassechidna.com.au/donate</url>
 <updatecontact>jorti@fedoraproject.org</updatecontact>
</application>
EOF

%files
%doc doc/*.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_udevrulesdir}/60-heimdall.rules

%files frontend
%{_bindir}/%{name}-frontend
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 01 2024 LuK1337 <priv.luk@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Łukasz Patron <priv.luk@gmail.com> - 2.0.2-1
- Switch to grimler's Heimdall fork since upstream repo is abandoned

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Łukasz Patron <priv.luk@gmail.com> - 1.4.2-14
- Add downstream patch from https://github.com/jesec/heimdall, fixes flashing newer devices.

* Tue Aug 04 2020 Juan Orti Alcaine <jortialc@redhat.com> - 1.4.2-13
- Add missing BuildRequires. Fix RHBZ#1863848

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Jeff Law <law@redhat.com> - 1.4.2-10
- Drop build requirement for qt5-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.2-6
- Add patch to support files bigger than 3.5 GB

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.2-1
- Version 1.4.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-9
- Add donation URL to AppData file

* Wed Feb 24 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-8
- Add keywords to desktop file

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.4.1-6
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-4
- Use license macro

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.4.1-3
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.1-1
- Update to version 1.4.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.4.0-1
- Update to version 1.4.0
- Add zlib-devel BuildRequires and explicit version to qt-devel
- Update udev rules dir patch

* Mon Feb 25 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.4-0.3.rc2
- Add _udevrulesdir for f17

* Mon Feb 25 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.4-0.2.rc2
- Change BuildRequires to libusb1-devel

* Fri Feb 22 2013 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.4-0.1.rc2
- Bump version to 1.4rc2
- Use _udevrulesdir macro and add patch to modify udev rules dir in Makefile
- Patch to avoid udev service restart is no longer necessary
- Change dependency to libusbx
- Change group of heimdall-frontend

* Tue Oct 30 2012 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.3.2-3
- Don't use autogen.sh
- Improve heimdall-remove-udev-service-restart.patch
- Remove unneeded files

* Tue Oct 30 2012 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.3.2-2
- Remove dos2unix dependency

* Sun Oct 28 2012 Juan Orti Alcaine <j.orti.alcaine@gmail.com> - 1.3.2-1
- Bump version to 1.3.2
- Add missing dependencies
- Spec file clean up

* Tue Sep 18 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 1.3.1-1
- Initial packaging
