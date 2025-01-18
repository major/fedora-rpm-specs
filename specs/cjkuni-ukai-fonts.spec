# SPDX-License-Identifier: MIT

%define catalogue        %{_sysconfdir}/X11/fontpath.d

Version: 0.2.20080216.2
Release: 7%{?dist}
URL:     http://www.freedesktop.org/wiki/Software/CJKUnifonts

%global foundry           CJKUni
%global fontlicense       Arphic-1999

%global fontlicenses      license
%global fontdocs          CONTRIBUTERS FONTLOG KNOWN_ISSUES NEWS README TODO

%global fontfamily        UKai
%global fontsummary       Chinese Unicode TrueType font in Kai face

%global fonts             ukai.ttc
%global fontconfs         %{SOURCE10} %{SOURCE11}

%global fontdescription   %{expand:
CJK Unifonts are Unicode TrueType fonts derived from original fonts made \
available by Arphic Technology under "Arphic Public License" and extended by \
the CJK Unifonts project.

CJK Unifonts in Kai face.}

Source0:  http://deb.debian.org/debian/pool/main/f/fonts-arphic-ukai/fonts-arphic-ukai_%{version}.orig.tar.bz2
Source10: 65-%{fontpkgname}.conf
Source11: 90-%{fontpkgname}-embolden.conf

%fontpkg

%prep
%autosetup -n fonts-arphic-ukai-%{version}

%build
%fontbuild

%install
%fontinstall

# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{fontdir}/ %{buildroot}%{catalogue}/%{name}


%check
%fontcheck

%fontfiles
%{catalogue}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct  7 2023 Peng Wu <pwu@redhat.com> - 0.2.20080216.2-3
- Fix the spec file
- Resolves: RHBZ#2241232

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr  6 2023 Peng Wu <pwu@redhat.com> - 0.2.20080216.2-1
- Update to 0.2.20080216.2
- Resolves: RHBZ#2184836

* Tue Feb 28 2023 Peng Wu <pwu@redhat.com> - 0.2.20080216.1-68
- Update to follow New Fonts Packaging Guidelines
- Migrate to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-67
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-65
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-61
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-58
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-57
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.20080216.1-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 16 2011  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-47
- Clean up spec.
  Remove fonts.dir, fonts.scale and 25-ttf-arphic-ukai-render.conf.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.20080216.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-45
- Fixes font_pkg macro usage.

* Mon Jul 19 2010  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-44
- Clean up the spec.

* Tue Jul 13 2010  Peng Wu <pwu@redhat.com> - 0.2.20080216.1-43
- The Initial Version.
  Split from cjkuni-fonts.

