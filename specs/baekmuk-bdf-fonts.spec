# SPDX-License-Identifier: MIT

%global fontname   baekmuk-bdf
%global catalogue    %{_sysconfdir}/X11/fontpath.d

Version: 2.2
Release: 41%{?dist}
URL:     http://kldp.net/projects/baekmuk/

%global foundry           Baekmuk
%global fontlicense       Baekmuk
%global fontlicenses      COPYRIGHT COPYRIGHT.ko
%global fontdocs          README
%global fontdocsex        %{fontlicenses}

%global fontfamily        Baekmuk BDF
%global fontsummary       Korean bitmap fonts
%global fonts             bdf/*.pcf.gz
%global fontdescription   %{expand:
This package provides the Korean Baekmuk bitmap fonts.
}
%global fontappstreams    %{SOURCE1}

Source0:  http://kldp.net/frs/download.php/1428/%{fontname}-%{version}.tar.gz
Source1:  org.fedoraproject.baekmuk-bdf-fonts.metainfo.xml
Patch0:   baekmuk-bdf-fonts-fix-fonts-alias.patch
BuildRequires:  mkfontdir bdftopcf

%fontpkg

%prep
%autosetup -p1 -n %{fontname}-%{version}

%build
for file in bdf/*.bdf; do
    bdftopcf $file | gzip -9 > ${file%.bdf}.pcf.gz
done

%fontbuild

%install
%fontinstall

# for catalogue
install -d $RPM_BUILD_ROOT%{catalogue}
ln -sf ../../..%{fontdir} $RPM_BUILD_ROOT%{catalogue}/%{name}

mkfontdir $RPM_BUILD_ROOT%{fontdir} 

# convert Korean copyright file to utf8
iconv -f EUC-KR -t UTF-8 COPYRIGHT.ks > COPYRIGHT.ko

install -m 0444 bdf/fonts.alias $RPM_BUILD_ROOT%{fontdir}/

%check
%fontcheck

%fontfiles
%verify(not md5 size mtime) %{fontdir}/fonts.dir
%{fontdir}/fonts.alias
%{catalogue}/%{name}

%changelog
* Wed Feb  5 2025 Peng Wu <pwu@redhat.com> - 2.2-41
- Fix build
- Resolves: RHBZ#2339920

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb 23 2023 Peng Wu <pwu@redhat.com> - 2.2-35
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov  2 2022 Akira TAGOH <tagoh@redhat.com> - 2.2-33
- Drop old dependencies.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar  2 2021 Peng Wu <pwu@redhat.com> - 2.2-29
- Resolves: rhbz#1933565 - Don't BuildRequires xorg-x11-font-utils

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Daiki Ueno <dueno@redhat.com> - 2.2-18
- replace %%define uses with %%global

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Daiki Ueno <dueno@redhat.com> - 2.2-15
- Don't run fc-cache with /usr/share/fonts (Closes: #1021754)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 25 2011 Daiki Ueno <dueno@redhat.com> - 2.2-10
- add baekmuk-bdf-fonts-fix-fonts-alias.patch (#733105)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 07 2009 Caius 'kaio' Chance <cchance@redhat.com> - 2.2-7.fc11
- Rebuilt for Fedora 11.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 14 2007 Jens Petersen <petersen@redhat.com> - 2.2-5
- better url
- use fontname macro

* Tue Sep 25 2007 Jens Petersen <petersen@redhat.com> - 2.2-4
- fix name of fonts.alias file

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-3
- conflict with fonts-korean < 2.2-5

* Mon Sep 24 2007 Jens Petersen <petersen@redhat.com> - 2.2-2
- convert Korean copyright file to utf8 (Mamoru Tasaka, #302451)

* Tue Sep 11 2007 Jens Petersen <petersen@redhat.com> - 2.2-1
- initial packaging separated from fonts-korean (#253155)
