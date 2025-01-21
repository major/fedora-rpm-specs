Name:           simcoupe
Version:        1.0
Release:        37%{?dist}
Summary:        SAM Coupe emulator (spectrum compatible)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.simcoupe.org
Source0:        http://downloads.sourceforge.net/%{name}/SimCoupe-%{version}.tar.gz
Source1:        B-DOS-License.txt
Patch0:         simcoupe-1.0-userpmopts.patch
Patch1:         simcoupe-1.0-saasound.patch
Patch2:         simcoupe-1.0-no-builtin-rom.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  SAASound-devel SDL-devel zlib-devel
BuildRequires:  ImageMagick desktop-file-utils
Requires:       samcoupe-rom hicolor-icon-theme

%description
SimCoupe emulates an 8bit Z80 based home computer, released in 1989 by Miles
Gordon Technology. The SAM Coupe was largely spectrum compatible, with much
improved hardware


%prep
%setup -q -n SimCoupe
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Clean up bundled SAASound to avoid accidentally building against it.
rm -f Extern/SAASound.h Extern/SAASound.cpp
cp -a %{SOURCE1} .


%build
pushd SDL
make %{?_smp_mflags} CFLAGSRPM="%{optflags}"
popd

#Build icon image
convert SDL/SimCoupe.bmp -transparent '#ffffff' %{name}.png

#Build desktop icon
cat >%{name}.desktop<<EOF
[Desktop Entry]
Encoding=UTF-8
Name=SimCoupe
GenericName=SAM Coupe Emulator
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -pm 0755 SDL/%{name} %{buildroot}%{_bindir}
install -pm 0644 SDL/SimCoupe.bmp %{buildroot}%{_datadir}/%{name}
install -pm 0644 %{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
    --vendor fedora \
%endif
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop


%files
%doc ChangeLog.txt License.txt SimCoupe.txt B-DOS-License.txt
%{_bindir}/%{name}
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/%{name}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-36
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-21
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0-15
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0-11
- Remove --vendor from desktop-file-install for F19+  https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Apr 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0-4
- Some small cleanups as preparation for Fedora submission
- Remove the included samcoupe 3.0 rom from the binary, instead always load
  it from disk (reusing the custom rom loading code). This is done because the
  rom included in a .h file as one byte array, is hardly the prefered form for
  editing, iow the rom is not GPL compatible licensed (as it does not come with
  source) and thus may not be linked into the GPL binary
- Requires samcoupe-rom, which provides the now needed rom file
- Add B-DOS-License.txt, which gives license info for the included B-DOS ROM
  patches

* Wed Dec 12 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-3
- Minor spec changes for devel
- License change due to new guidelines

* Sun Mar 11 2007 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-2
- Dropped dribble-menus requirement, due to be obsoleted
- Changed .desktop category to Game;Emulator;

* Sun Aug 06 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-1
- Upgraded to official release
- Added patch to use system SAASound and not the bundled one.
- Now builds icon image rather than bundling it

* Mon Jul 17 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-0.4.cvs
- Moved icon installation to make it freedesktop compliant
- Added %%post and %%postun sections to update icon cache at installation

* Sat Jun 24 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-0.3.cvs
- Cosmetic fixes for the Dribble repository

* Mon May 29 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-0.2.cvs
- Corrected release name format to 0.%%{X}.%%{alphatag} from 0.%%{alphatag}.%%{X}
- Added patch to compile using rpmoptflags

* Sun May 07 2006 Ian Chapman <packages[AT]amiga-hardware.com> 1.0-0.cvs.1.iss
- Altered spec file to more closely follow Fedora guidelines
- Updated to latest cvs sources

* Mon Feb 28 2005 Ian Chapman <packages[AT]amiga-hardware.com> 0.90-2.iss
- Added sound support. Suitable SAASound package found with compatible license

* Tue Feb 22 2005 Ian Chapman <packages[AT]amiga-hardware.com> 0.90-1.iss
- Initial Release
