Name:           qsstv
Version:        9.5.8
Release:        22%{?dist}
Summary:        Qt-based slow-scan TV and fax

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.qsl.net/on4qz/

Source0:        https://www.qsl.net/o/on4qz/qsstv/downloads/%{name}_%{version}.tar.gz
Source1:        qsstv.1
Source2:        net.qsl.QSSTV.metainfo.xml
Source3:        qsstv.png

Patch0:         qsstv-install.patch

ExcludeArch:    i686

BuildRequires:  gcc-c++ doxygen desktop-file-utils
BuildRequires:  make
BuildRequires:  libappstream-glib
BuildRequires:  fftw-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qwt-qt5-devel
BuildRequires:  hamlib-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  libv4l-devel


%description
Qsstv is a program for receiving slow-scan television and fax. These are
modes used by hamradio operators. Qsstv uses a soundcard to send and
receive images.


%package doc
Summary:             User manual for Qsstv.
BuildArch:           noarch
Requires:            %{name} = %{version}-%{release}

%description doc
User manual for Qsstv.


%prep
%autosetup -p1 -n %{name}

# Honor build flags...
sed -i "s/\-O0/\-O2/g" qsstv.pro


%build 
# mode_and_occupancy_code_table has different sizes  in its declaration
# vs its definition.  This is a hard error when using LTO and must be
# resolved before this package can use LTO
%define _lto_cflags %{nil}

qmake-qt5 PREFIX=%{_prefix} CONFIG+=debug QMAKE_CXXFLAGS+="-std=c++14 %{optflags}"
make %{?_smp_mflags}


%install
export INSTALL_ROOT=%{buildroot}
make install 

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -pm 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install man page borrowed from Debian
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

# Install metainfo file
%if 0%{?fedora}
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE2} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%endif

find %{buildroot} -type f -name "*.a" -exec rm -f {} \;


%files
%license COPYING
%doc README.txt
%{_bindir}/* 
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{?fedora:%{_metainfodir}/*.metainfo.xml}

%files doc
%{_pkgdocdir}/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 9.5.8-21
- Rebuild for Hamlib 4.6.

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 9.5.8-20
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 26 2024 Daniel Rusek <mail@asciiwolf.com> - 9.5.8-18
- Added better quality desktop icon

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 9.5.8-13
- Rebuild (qwt)

* Tue Dec 06 2022 Daniel Rusek <mail@asciiwolf.com> - 9.5.8-12
- Use new QSSTV homepage url

* Sun Dec 04 2022 Daniel Rusek <mail@asciiwolf.com> - 9.5.8-11
- Use larger desktop icon

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 9.5.8-10
- Rebuild for updated hamlib 4.5.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 9.5.8-8
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Sat Mar 26 2022 Richard Shaw <hobbes1069@gmail.com> - 9.5.8-7
- Rebuild after icon fix for appdata file.

* Sat Mar 26 2022 Daniel Rusek <mail@asciiwolf.com> - 9.5.8-6
- Install desktop icon into a standard location

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.8-4
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.8-3
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.8-2
- Rebuild for hamlib 4.3.1.

* Wed Aug 25 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.8-1
- Update to 9.5.8.

* Mon Aug 02 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.7-1
- Update to 9.5.7.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.3-2
- Rebuild for hamlib 4.2.

* Thu Mar 11 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.3-1
- Update to 9.5.3.

* Tue Mar 02 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.1-1
- Update to 9.5.1.

* Sun Feb 21 2021 Richard Shaw <hobbes1069@gmail.com> - 9.5.0-1
- Update to 9.5.0.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 9.4.4-8
- Rebuild for hamlib 4.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 9.4.4-6
- Force C++14 as this code is not C++17 ready

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Jeff Law <law@redhat.com> - 9.4.4-4
- Disable LTO

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 9.4.4-3
- Rebuild for hamlib 4.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Richard Shaw <hobbes1069@gmail.com> - 9.4.4-1
- Update to 9.4.4.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Richard Shaw <hobbes1069@gmail.com> - 9.4.1-1
- Update to 9.4.1.

* Thu Apr 18 2019 Richard Shaw <hobbes1069@gmail.com> - 9.3.3-1
- Update to 9.3.3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Richard Shaw <hobbes1069@gmail.com> - 9.2.6-4
- Rebuild for hamlib 3.3.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard Shaw <hobbes1069@gmail.com> - 9.2.6-1
- Upate to latest upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Richard Shaw <hobbes1069@gmail.com> - 9.2.4-3
- Rebuild for hamlib 3.1.

* Mon Dec 26 2016 Richard Shaw <hobbes1069@gmail.com> - 9.2.4-2
- Rebuild to honor build flags.

* Sat Oct 22 2016 Richard Shaw <hobbes1069@gmail.com> - 9.2.4-1
- Update to latest upstream release.

* Mon Oct 10 2016 Richard Shaw <hobbes1069@gmail.com> - 9.2.2-1
- Beta release.

* Mon Jul 25 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.8-1
- Update to latest upstream release.

* Mon Jul  4 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.7-1
- Update to latest upstream release.

* Wed Jun 29 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.6-1
- Update to latest upstream release.

* Sun Apr 17 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.5-1
- Update to latest upstream release.

* Sat Apr 16 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.4-1
- Update to latest upstream release.

* Mon Apr 11 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.3-1
- Update to latest upstream release.

* Sun Apr 10 2016 Richard Shaw <hobbes1069@gmail.com> - 9.1.1-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 8.2.12-2
- use %%qmake_qt5 macro to ensure proper build flags

* Sun Jul 12 2015 Richard Shaw <hobbes1069@gmail.com> - 8.2.12-1
- Fix grey pictures TX for some modes.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8.2.11-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Richard Shaw <hobbes1069@gmail.com> - 8.2.11-1
- Update to latest upstream release, 8.2.11.
- Fixes CAT control bug.

* Sun Mar  1 2015 Richard Shaw <hobbes1069@gmail.com> - 8.2.10-1
- Update to latest upstream release, 8.2.10.

* Sun Dec  7 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.9-1
- Update to latest upstream release.

* Sat Oct 11 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.8-1
- Update to latest upstream release.
- Move documentation to a doc subpackage.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.7-1
- Update to latest upstream release.

* Fri Apr  4 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.6-1
- Update to latest upstream release.

* Sat Mar  8 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 8.2.4-2
- Rebuild against fixed qt to fix -debuginfo (#1074041)

* Sun Mar  2 2014 Richard Shaw <hobbes1069@gmail.com> - 8.2.4-1
- Update to latest upstream release.

* Tue Feb 11 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.17-1
- Update to latest upstream release.

* Wed Jan 29 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.14-1
- Update to latest upstream release.

* Sun Jan 26 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.13-1
- Update to latest upstream release.

* Mon Jan  6 2014 Richard Shaw <hobbes1069@gmail.com> - 8.1.12-1
- Update to latest upstream release.

* Tue Dec 17 2013 Richard Shaw <hobbes1069@gmail.com> - 8.1.3
- Update to latest upstream release.

* Sun Aug 05 2012 Richard Shaw <hobbes1069@gmail.com> - 7.1.7-1
- Update to latest upstream release.

* Fri Nov 27 2009 Lucian Langa <cooly@gnome.eu.org> - 5.3c-6
- improve desktop file (#530838)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3c-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Aug 24 2008 Lucian Langa <cooly@gnome.eu.org> - 5.3c-3
- fix build requires

* Sun Aug 17 2008 Lucian Langa <cooly@gnome.eu.org> - 5.3c-2
- add desktop file

* Sun Aug 10 2008 Lucian Langa <cooly@gnome.eu.org> - 5.3c-1
- Misc cleanups

* Mon Dec 10 2007 Sindre Pedersen Bjørdal - 0.5c-1
- Initial build

