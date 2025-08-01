%global fontname ucs-miscfixed
%global fontconf 66-%{fontname}.conf

%global common_desc \
The usc-fixed-fonts package provides bitmap fonts for\
locations such as terminals.

Name: %{fontname}-fonts
Version: 0.3
Release: 36%{?dist}
License: LicenseRef-Fedora-Public-Domain
URL: http://www.cl.cam.ac.uk/~mgk25/ucs-fonts.html
Source0: http://www.cl.cam.ac.uk/~mgk25/download/ucs-fonts.tar.gz
Source1: 66-ucs-miscfixed.conf
BuildArch: noarch
Summary: Selected set of bitmap fonts
BuildRequires: fontpackages-devel
BuildRequires: mkfontdir bdftopcf fonttosfnt
Conflicts: ucs-miscfixed-opentype-fonts

%description
%common_desc

%package -n ucs-miscfixed-opentype-fonts
Summary:        Selected set of bitmap fonts (opentype version)
Conflicts:      ucs-miscfixed-fonts

%description -n ucs-miscfixed-opentype-fonts
%common_desc

This package contains the fonts in OpenType format.

%prep
%setup -q -c
rm helvR12.bdf

%build
for i in `ls *.bdf`;
do fonttosfnt -v -b -c -g 2 -m 2 -o ${i%%.bdf}.otb $i;
done

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.bdf %{buildroot}%{_fontdir}

install -m 0644 -p *.otb %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.bdf

%doc README	

%_font_pkg -n ucs-miscfixed-opentype-fonts -f %{fontconf} *.otb

%doc README

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3-31
- Convert to SPDX license.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Parag Nemade <pnemade AT redhat DOT com> - 0.3-26
- Resolves: rhbz#1933581 - Don't BuildRequires xorg-x11-font-utils

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Peng Wu <pwu@redhat.com> - 0.3-24
- Rebuilt with fonttosfnt 1.2.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb  6 2020 Peng Wu <pwu@redhat.com> - 0.3-22
- Provide OpenType Bitmap fonts
- Add ucs-miscfixed-opentype-fonts sub package

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 12 2012 Pravin Satpute <psatpute@redhat.com> - 0.3-8
- removed gzip 
- upstream new source , #597403

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 25 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-5
- removed \ from description

* Thu Oct 22 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-4
- chnaged conf file priority

* Thu Sep 29 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-3
- modified license field

* Thu Sep 29 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-2
- updated as per package review suggestion, bug 526204


* Thu Sep 29 2009 Pravin Satpute <psatpute@redhat.com> - 0.3-1
- initial packaging
- these fonts was there in bitmap-fonts package previously, packaging it separate as per merger review suggetion.
