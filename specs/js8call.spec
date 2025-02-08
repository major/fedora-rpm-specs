%define _lto_cflags %{nil}

# Commit hash for tagged release
# https://bitbucket.org/widefido/js8call/downloads/?tab=tags
%global commit c5236ed22f06
%global project widefido

Name:           js8call
Version:        2.2.0
Release:        26%{?dist}
Summary:        Amateur Radio message passing using FT8 modulation

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://js8call.com/

# Source archive from bitbucket includes project name and commit for directory.
# Use repack.sh to repack the archive.
Source0:        http://files.js8call.com/%{version}/js8call-%{version}.tgz
Source1:        com.js8call.JS8Call.metainfo.xml

# Unbundle boost libraries.
Patch0:         js8call-sys_boost.patch
# js8call assumes it's using bundled hamlib and copies and installs binaries to
# new names.
Patch1:         js8call-hamlib.patch
# Fix missing headers exposed by gcc-11
Patch2:         js8call-gcc11.patch

ExcludeArch:    i686

BuildRequires:  cmake%{?rhel:3} gcc gcc-c++ gcc-gfortran tar
BuildRequires:  asciidoc dos2unix rubygem-asciidoctor
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# Libraries and devel packages
BuildRequires:  boost-devel 
BuildRequires:  fftw-devel
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  libusbx-devel
BuildRequires:  portaudio-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  systemd-devel

Requires:       hicolor-icon-theme


%description
JS8Call is software using the JS8 Digital Mode providing weak signal keyboard
to keyboard messaging to Amateur Radio Operators.

JS8Call is an experiment to test the feasibility of a digital mode with the
robustness of FT8, combined with a messaging and network protocol layer for
weak signal communication on HF, using a keyboard messaging style interface. It
is not designed for any specific purpose other than connecting amateur radio
operators who are operating under weak signal conditions. JS8Call is heavily
inspired by WSJT-X, Fldigi, and FSQCall and would not exist without the hard
work and dedication of the many developers in the amateur radio community.


%prep
%autosetup -p1 -c %{name}-%{version}

# remove bundled boost
rm -rf boost

# convert CR + LF to LF
dos2unix *.ui *.rc *.txt

# Don't specify gnu++11 when 14 is the compiler default.
%if 0%{?fedora}
sed -i 's/--std=gnu++11 //' CMakeLists.txt
%endif


%build
# workaround for hamlib check, i.e. for hamlib_LIBRARY_DIRS not to be empty
export PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
%cmake3 -DBoost_NO_SYSTEM_PATHS=FALSE \
        -Dhamlib_STATIC=FALSE

%cmake_build


%install
%cmake_install

# Install icon to proper place and use it in desktop file
install -D -p -m644 icons/Unix/js8call_icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
desktop-file-edit --set-key=Icon --set-value="%{name}" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Install AppStream metainfo file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/

appstream-util validate-relax \
  --nonet %{buildroot}%{_metainfodir}/com.js8call.JS8Call.metainfo.xml

# Buttons don't look right with system default style.
desktop-file-edit --set-key=Exec --set-value="js8call --style=fusion" \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Remove COPYING so it can be included with %%liecnse
rm -f %{buildroot}%{_datadir}/doc/JS8Call/COPYING
# Remove unneeded install file
rm -f %{buildroot}%{_datadir}/doc/JS8Call/INSTALL*


%files
%license COPYING
%doc %{_datadir}/doc/JS8Call
%{_bindir}/js8*
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/com.js8call.JS8Call.metainfo.xml
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/pixmaps/%{name}_icon.png
%{_datadir}/%{name}/


%changelog
* Thu Feb 06 2025 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-26
- Rebuild for hamlib 4.6.

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-24
- Rebuild for Hamlib 4.6.

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0-23
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Daniel Rusek <mail@asciiwolf.com> - 2.2.0-18
- Install desktop icon into a proper location

* Wed Jun 28 2023 Daniel Rusek <mail@asciiwolf.com> - 2.2.0-17
- Add an AppStream metainfo file

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-15
- Rebuild for hamlib 4.5.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-12
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-11
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-10
- Rebuild for hamlib 4.3.1.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-8
- Rebuild for hamlib 4.2.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-7
- Rebuild for hamlib 4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-5
- Rebuilt for hamlib 4.0 release.

* Wed Oct 14 2020 Jeff Law <law@redhat.com> - 2.2.0-4
- Add missing #include for gcc-11

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Richard Shaw <hobbes1069@gmail.com> - 2.2.0-1
- Update to 2.2.0.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-3
- Rebuild for hamlib 4.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.1-1
- Update to 2.1.1.

* Sat Dec 07 2019 Richard Shaw <hobbes1069@gmail.com> - 2.0.1-1
- Update to 2.0.1.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 19 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Tue Apr 02 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-2
- Update spec per review request comments.

* Mon Apr  1 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-1
- Update to 1.0.0.

* Wed Mar 20 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-0.2.rc2
- Add patch to deal with change in fortran iand behavior with version 9.

* Fri Feb 22 2019 Richard Shaw <hobbes1069@gmail.com> - 1.0.0-0.1.rc1
- Update to 1.0.0-rc1.

* Sat Feb 09 2019 Richard Shaw <hobbes1069@gmail.com> - 0.14.1-1
- Update to 0.14.1.

* Fri Feb 08 2019 Richard Shaw <hobbes1069@gmail.com> - 0.14.0-1
- Update to 0.14.0.

* Thu Jan 24 2019 Richard Shaw <hobbes1069@gmail.com> - 0.13.0-1
- Update to 0.13.0.

* Thu Jan 03 2019 Richard Shaw <hobbes1069@gmail.com> - 0.12.0-1
- Update to 0.12.0.

* Wed Dec 19 2018 Richard Shaw <hobbes1069@gmail.com> - 0.11.0-1
- Update to 0.11.0.

* Sun Dec 02 2018 Richard Shaw <hobbes1069@gmail.com> - 0.10.1-1
- Update to 0.10.1.

* Sat Dec 01 2018 Richard Shaw <hobbes1069@gmail.com> - 0.10.0-1
- Update to 0.10.0.

* Fri Nov 16 2018 Richard Shaw <hobbes1069@gmail.com> - 0.9-1
- new version

* Tue Nov 06 2018 Richard Shaw <hobbes1069@gmail.com> - 0.8.3-1
- Update to 0.8.3.

* Sat Nov 03 2018 Richard Shaw <hobbes1069@gmail.com> - 0.8.2-1
- Update to 0.8.2.

* Fri Nov 02 2018 Richard Shaw <hobbes1069@gmail.com> - 0.8.1-1
- Update to 0.8.1.

* Fri Oct 19 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.5-1
- Update to 0.7.5.

* Thu Oct 11 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.3-1
- Update to 0.7.3.

* Thu Oct 11 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.2-2
- Specfile updates for EL 7 build.

* Mon Oct 08 2018 Richard Shaw <hobbes1069@gmail.com> - 0.7.2-1
- Update to 0.7.2.

* Fri Sep 21 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.4-4
- More fixes to work around incomplete fork of wsjtx.

* Thu Sep 20 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.4-3
- Update patch to not build/install redundant binaries with wsjtx.

* Mon Sep 17 2018 Richard Shaw <hobbes1069@gmail.com> - 0.6.4-2
- Update patch to not install duplicate binaries with wsjtx and hamlib.
