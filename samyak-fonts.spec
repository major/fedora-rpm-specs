%global	fontname	samyak
%global fontconf	67-%{fontname}

# Common description
%global common_desc \
The Samyak package contains fonts for the display of \
Scripts Devanagari, Gujarati, Malayalam, Odia and Tamil

Name:	 %{fontname}-fonts
Version:	1.2.2
Release:	29%{?dist}
Summary:	Free Indian truetype/opentype fonts
License:	GPLv3+ with exceptions
URL:	http://sarovar.org/projects/samyak/
# Source0: http://sarovar.org/frs/?group_id=461&release_id=821
Source:	samyak-fonts-%{version}.tar.gz
Source1: 66-samyak-devanagari.conf
Source2: 67-samyak-tamil.conf
Source3: 68-samyak-malayalam.conf
Source4: 67-samyak-gujarati.conf
Source5: 67-samyak-odia.conf
Source7: %{fontname}-devanagari.metainfo.xml
Source8: %{fontname}-tamil.metainfo.xml
Source9: %{fontname}-malayalam.metainfo.xml
Source10: %{fontname}-gujarati.metainfo.xml
Source11: %{fontname}-odia.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires: fontforge >= 20080429
Patch1: bug-1040288.patch

%description
%common_desc

%package common
Summary:  Common files for samyak-fonts
Requires: fontpackages-filesystem
%description common
%common_desc

%package -n %{fontname}-devanagari-fonts
Summary: Open Type Fonts for Devanagari script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-devanagari-fonts
This package contains truetype/opentype font for the display of \
Scripts Devanagari.

%_font_pkg -n devanagari -f 66-samyak-devanagari.conf Samyak-Devanagari.ttf 
%{_datadir}/appdata/%{fontname}-devanagari.metainfo.xml

%package -n %{fontname}-tamil-fonts
Summary: Open Type Fonts for Tamil script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-tamil-fonts
This package contains truetype/opentype font for the display of \
Scripts Tamil.

%_font_pkg -n tamil -f %{fontconf}-tamil.conf Samyak-Tamil.ttf 
%{_datadir}/appdata/%{fontname}-tamil.metainfo.xml

%package -n %{fontname}-malayalam-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-malayalam-fonts
This package contains truetype/opentype font for the display of \
Scripts Malayalam.

%_font_pkg -n malayalam -f 68-samyak-malayalam.conf Samyak-Malayalam.ttf 
%{_datadir}/appdata/%{fontname}-malayalam.metainfo.xml

%package -n %{fontname}-gujarati-fonts
Summary: Open Type Fonts for Gujarati script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-gujarati-fonts
This package contains truetype/opentype font for the display of \
Scripts Gujarati.

%_font_pkg -n gujarati -f %{fontconf}-gujarati.conf Samyak-Gujarati.ttf 
%{_datadir}/appdata/%{fontname}-gujarati.metainfo.xml

%package -n %{fontname}-odia-fonts
Summary: Open Type Fonts for Odia script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides:	%{fontname}-oriya-fonts = %{version}-%{release}
Obsoletes:	%{fontname}-oriya-fonts < 1.2.2-12
%description -n %{fontname}-odia-fonts
This package contains truetype/opentype font for the display of \
Scripts Odia.

%_font_pkg -n odia -f %{fontconf}-odia.conf Samyak-Odia.ttf 
%{_datadir}/appdata/%{fontname}-odia.metainfo.xml

%prep
%setup -q -n samyak-fonts-%{version}
%patch1 -p1 -b .1-change-name-from-oriya-to-odia


%build
mkdir -p TTFfiles/
./generate.pe */*.sfd

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p TTFfiles/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/66-samyak-devanagari.conf

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-tamil.conf

install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/68-samyak-malayalam.conf

install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gujarati.conf

install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-odia.conf


for fconf in 66-samyak-devanagari.conf \
		%{fontconf}-tamil.conf \
		68-samyak-malayalam.conf \
		%{fontconf}-gujarati.conf \
		%{fontconf}-odia.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE7} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-devanagari.metainfo.xml
install -Dm 0644 -p %{SOURCE8} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-tamil.metainfo.xml
install -Dm 0644 -p %{SOURCE9} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-malayalam.metainfo.xml
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-gujarati.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-odia.metainfo.xml


%files common
%doc COPYING README AUTHORS
%dir %{_fontdir}

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 17 2014 Pravin Satpute <psatpute@redhat.com> 1.2.2-14
- Added Metainfo for gnome-software

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Pravin Satpute <psatpute@redhat.com> 1.2.2-12
- Resolved bug #1040288 - Changed name from Oriya to Odia

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Pravin Satpute <psatpute@redhat.com> 1.2.2-9
- spec file clean up

* Tue Nov 20 2012 Pravin Satpute <psatpute@redhat.com> 1.2.2-8
- spec file clean up

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Pravin Satpute <psatpute@redhat.com> 1.2.2-5
- Resolved bug 714926

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Naveen Kumar <nkumar@redhat.com> - 1.2.2-3
- rectify error to directly install fonts in fontdir instead of subdir in fontdir

* Thu Jun 10 2010 Naveen Kumar <nkumar@redhat.com> 1.2.2-2
- OOPS! forgot to add pkg fontforge in BuildRequires

* Thu Jun 10 2010 Naveen Kumar <nkumar@redhat.com> 1.2.2-1
- new release from upstream with source
- changes in spec file to source compile

* Tue May 4 2010 Naveen Kumar <nkumar@redhat.com> 1.2.1-10
- remove binding="same" from all .conf files

* Tue Mar 23 2010 Naveen Kumar <nkumar@redhat.com> 1.2.1-9
- corrected ne-IN to ne-np in 67-samyak-devanagari.conf

* Wed Mar 3 2010 Naveen Kumar <nkumar@redhat.com> 1.2.1-8
- Updated .conf file
- Resolves Bug#568254

* Wed Oct 28 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-7
- added fontconf files for each subpackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-4
- renamed samyak-common-fonts to samyak-fonts-common

* Tue Feb 03 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-3
- renamed font package as per fedora new Font_package_naming guideline
- updated spec

* Mon Jan 12 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-2
- bugzilla 477451
- updated spec

* Thu Sep 18 2008 Pravin Satpute <psatpute@redhat.com> 1.2.1-1
- upstream release 1.2.1
- Added Unicode 5.1 support in Samyak-Devanagari 

* Fri Apr 04 2008 Pravin Satpute <psatpute@redhat.com> 1.2.0-2
- given proper license name
- fc-cache now run on samyak-langname folder

* Thu Feb 28 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.0-1
- update to samyak-fonts-1.2.0 from upstream cvs
- major bug fixes for devanagari and malayalam
- licence update to 'GNU Gplv3 or later with font exceptions'
- update spec file

* Fri Feb 08 2008 Pravin Satpute <psatpute@redhat.com> - 1.1.0-2
- added sub packaging support in spec file based on lohit-fonts.spec file 

* Fri Jan 18 2008 Pravin Satpute <psatpute@redhat.com> - 1.1.0-1
- initial packaging
