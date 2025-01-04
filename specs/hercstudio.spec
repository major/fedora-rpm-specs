Name:           hercstudio
Version:        1.6.0
Release:        1%{?dist}
Summary:        GUI front-end to the Hercules mainframe Emulator

License:        GPL-3.0-or-later
URL:            https://hercstudio.sourceforge.io/
Source0:        %{url}/herculesstudio-%{version}-src.tar.gz
# borrowed from Debian
Source1:        HerculesStudio.1

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  sed

BuildRequires:  cmake(Qt6)

Requires:       (hercules or sdl-hercules)

%description
GUI front-end to the Hercules mainframe Emulator.


%prep
%autosetup -n master -p1

# Do not clobber the compiler flags
sed -i '/CMAKE_CXX_FLAGS/d' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install
rm -r %{buildroot}%{_prefix}/local
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 %{SOURCE1}
install -Dpm0644 -t %{buildroot}%{_metainfodir} %{name}.appdata.xml
install -Dpm0644 HercStudio/icons/tray.xpm \
  %{buildroot}%{_datadir}/pixmaps/HerculesStudio.xpm
desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
  hercules-studio.desktop


%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license COPYING
%{_bindir}/HerculesStudio
%{_datadir}/applications/hercules-studio.desktop
%{_datadir}/pixmaps/HerculesStudio.xpm
%{_mandir}/man1/HerculesStudio.1*
%{_metainfodir}/%{name}.appdata.xml


%changelog
* Wed Jan 01 2025 Davide Cavalca <dcavalca@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0
- Require hercules or sdl-hercules

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5.0-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Dan Horák <dan[at]danny.cz> - 1.5.0-8
- fix MIPS display
- add man page
- install appdata

* Sun Jul 24 2016 Dan Horák <dan[at]danny.cz> - 1.5.0-7
- rebuilt for #1359391

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.5.0-5
- use %%qmake_qt5 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Dan Horák <dan[at]danny.cz> - 1.5.0-1
- update to 1.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 06 2013 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- update to 1.4.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for c++ ABI breakage

* Sun Jan 15 2012 Dan Horák <dan[at]danny.cz> - 1.3.0-3
- fix unistd.h include

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Dan Horák <dan[at]danny.cz> - 1.3.0-1
- update to 1.3.0

* Fri Apr 29 2011 Dan Horák <dan[at]danny.cz> - 1.2.0-3
- fix build with gcc 4.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 19 2010 Dan Horák <dan[at]danny.cz> - 1.2.0-1
- update to 1.2.0

* Sat Jan 16 2010 Dan Horák <dan[at]danny.cz> - 1.1.0-1
- update to 1.1.0

* Mon Jan 11 2010 Dan Horák <dan[at]danny.cz> - 1.0.0-3
- rebuilt with updated source archive

* Tue Nov 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.0-2
- rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Fri Oct 16 2009 Dan Horák <dan[at]danny.cz> - 1.0.0-1
- update to 1.0.0

* Mon Sep  7 2009 Dan Horák <dan[at]danny.cz> - 1.0-0.2.beta
- add patch for panel buttons from upstream

* Mon Sep  7 2009 Dan Horák <dan[at]danny.cz> - 1.0-0.1.beta
- initial Fedora version
