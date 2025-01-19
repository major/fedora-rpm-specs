%global priority 67
%global fontname paktype-tehreer
%global fontconf %{priority}-%{fontname}

Name:        %{fontname}-fonts
Version:     6.0
Release:     11%{?dist}
Summary:     Fonts for Arabic from PakType
License:     GPL-2.0-only WITH Font-exception-2.0
URL:	     https://sourceforge.net/projects/paktype/
Source0:     https://sourceforge.net/p/paktype/code/HEAD/tree/Fonts/Release/PakType-Tehreer-%{version}.tar.gz?format=raw#/%{name}-%{version}.tar.gz

Source1:     %{fontconf}.conf
BuildArch:   noarch
BuildRequires:	fontpackages-devel
Requires:   fontpackages-filesystem
Obsoletes: paktype-fonts-common < %{version}i-%{release}

%description 
The paktype-tehreer-fonts package contains fonts for the display of \
Arabic from the PakType by Lateef Sagar.

%prep
%setup -q -c
rm -rf Code
# get rid of the white space (' ')
mv PakType\ Tehreer\ License.txt  PakType_Tehreer_License.txt
mv PakType\ Tehreer\ Features.pdf PakTypeTehreerFeatures.pdf

%{__sed} -i 's/\r//' PakType_Tehreer_License.txt
chmod a-x PakType_Tehreer_License.txt PakTypeTehreerFeatures.pdf


%build
echo "Nothing to do in Build."

%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p PakTypeTehreer.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

%_font_pkg -f %{fontconf}.conf PakTypeTehreer.ttf
%ghost %attr(644, root, root) %{_fontdir}/.uuid

%doc PakType_Tehreer_License.txt PakTypeTehreerFeatures.pdf 

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Parag Nemade <pnemade@fedoraproject.org> - 6.0-7
- Convert to SPDX license expression

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 01 2021 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 6.0-1
- Upstream release 6.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 5.0-1
- Upstream 5.0 Release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Pravin Satpute <psatpute@redhat.com> - 4.1-1
- Upstream 4.1 release

* Tue Feb 05 2013 Pravin Satpute <psatpute@redhat.com> - 4.0-3
- upstream changed tarball

* Wed Nov 21 2012 Pravin Satpute <psatpute@redhat.com> - 4.0-2
- corrected upstream source url

* Tue Nov 20 2012 Pravin Satpute <psatpute@redhat.com> - 4.0-1
- upstream 4.0 release

* Mon Sep 03 2012 Pravin Satpute <psatpute@redhat.com> - 2.1-1
- upstream 2.1 release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-10
- obsoleted paktype-fonts-common, bug 656375 

* Tue May 11 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-9
- improved .conf file, bug 586799

* Thu Mar 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-8
- new upstream release with license, rh bugfix 567300
- added .conf file

* Fri Feb 05 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-7
- updated as per package review bug #561271

* Wed Feb 03 2010 Pravin Satpute <psatpute@redhat.com> - 2.0-6
- Initial build
- Split from paktype fonts
- keeping release 6, since paktype producing rpm with 2.0-5
