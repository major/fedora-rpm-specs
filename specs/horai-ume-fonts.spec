%global fontname horai-ume
%global fontconf 65-%{fontname}
%global archivename umefont_%{version}
%global _docdir_fmt %{name}

%global common_desc \
This package contains fonts published by Wataru Horai. It contains Gothic and\
Mincho styles in 20 variants total:\
\
 * Ume Gothic Original, O5, C4, C5, S4, S5\
 * Ume Hy Gothic, O5\
 * Ume P Gothic Original, O5, C4, C5, S4, S5\
 * Ume UI Gothic Original, O5\
 * Ume Mincho Original, S3\
 * Ume P Mincho Original, S3\
\
In addition to Latin, Greek and Cyrilics scripts it provides Hiragana, Katakana\
and CJK. These fonts are suitable for easy on-screen legibility.


Name:           %{fontname}-fonts
Version:        670
Release:        18%{?dist}
Summary:        Gothic and Mincho fonts designed for easy on-screen legibility

License:        mplus
URL:            https://osdn.jp/projects/ume-font/
Source0:        https://osdn.jp/projects/ume-font/downloads/22212/%{archivename}.tar.xz
Source1:        %{fontname}-gothic-fontconfig.conf
Source2:        %{fontname}-hgothic-fontconfig.conf
Source3:        %{fontname}-pgothic-fontconfig.conf
Source4:        %{fontname}-uigothic-fontconfig.conf
Source5:        %{fontname}-mincho-fontconfig.conf
Source6:        %{fontname}-pmincho-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel


%description
%common_desc


%package -n %{fontname}-gothic-fonts
# tgc4    Ume Gothic C4 / Regular
# tgc5    Ume Gothic C5 / Medium
# tgo4    Ume Gothic / Regular
# tgo5    Ume Gothic O5 / Medium
# tgs4    Ume Gothic S4 / Regular
# tgs5    Ume Gothic S5 / Medium
Summary:        Free Japanese fonts family Ume Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-gothic-fonts
%common_desc

The Ume Gothic family features sans-serif fonts.


%package -n %{fontname}-hgothic-fonts
# hgo4    Ume Hy Gothic / Regular
# hgo5    Ume Hy Gothic O5 / Regular?
Summary:        Free Japanese fonts family Ume Hy Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-hgothic-fonts
%common_desc

The Ume Hy Gothic family features sans-serif fonts.


%package -n %{fontname}-pgothic-fonts
# pgc4    Ume P Gothic C4 / Regular
# pgc5    Ume P Gothic C5 / Medium
# pgo4    Ume P Gothic / Regular
# pgo5    Ume P Gothic O5 / Medium
# pgs4    Ume P Gothic S4 / Regular
# pgs5    Ume P Gothic S5 / Medium
Summary:        Free Japanese fonts family Ume P Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-pgothic-fonts
%common_desc

The Ume P Gothic family features sans-serif fonts.


%package -n %{fontname}-uigothic-fonts
# ugo4    Ume UI Gothic / Regular
# ugo5    Ume UI Gothic O5 / Medium
Summary:        Free Japanese fonts family Ume UI Gothic
Requires:       fontpackages-filesystem

%description -n %{fontname}-uigothic-fonts
%common_desc

The Ume Gothic family features sans-serif fonts.


%package -n %{fontname}-pmincho-fonts
# pmo3    Ume P Mincho / Regular
# pms3    Ume P Mincho S3 / Regular
Summary:        Free Japanese fonts family Ume P Mincho
Requires:       fontpackages-filesystem

%description -n %{fontname}-pmincho-fonts
%common_desc

The Ume P Mincho family features serif fonts.


%package -n %{fontname}-mincho-fonts
# tmo3    Ume Mincho / Regular
# tms3    Ume Mincho S3 / Regular
Summary:        Free Japanese fonts family Ume Mincho
Requires:       fontpackages-filesystem

%description -n %{fontname}-mincho-fonts
%common_desc

The Ume Mincho family features serif fonts.


%prep
%setup -q -n %{archivename}


%build
chmod -x *


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-hgothic.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pgothic.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-uigothic.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mincho.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pmincho.conf

for fconf in %{fontconf}-gothic.conf \
             %{fontconf}-hgothic.conf \
             %{fontconf}-pgothic.conf \
             %{fontconf}-uigothic.conf \
             %{fontconf}-mincho.conf \
             %{fontconf}-pmincho.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%_font_pkg -n gothic   -f %{fontconf}-gothic.conf   ume-tg??.ttf
%license license.html

%_font_pkg -n hgothic  -f %{fontconf}-hgothic.conf  ume-hg??.ttf
%license license.html

%_font_pkg -n pgothic  -f %{fontconf}-pgothic.conf  ume-pg??.ttf
%license license.html

%_font_pkg -n uigothic -f %{fontconf}-uigothic.conf ume-ug??.ttf
%license license.html

%_font_pkg -n mincho   -f %{fontconf}-mincho.conf   ume-tm??.ttf
%license license.html

%_font_pkg -n pmincho  -f %{fontconf}-pmincho.conf  ume-pm??.ttf
%license license.html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 670-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 670-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 670-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 670-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 670-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 670-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 670-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 670-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 670-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 670-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 670-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 670-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 670-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 670-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 670-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 670-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 670-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Karel Volný <kvolny@redhat.com> 670-1
- New version 670
- Adds Ume Hy Gothic O5 font

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 641-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 12 2016 Karel Volný <kvolny@redhat.com> 641-1
- New version 641

* Mon Jun 06 2016 Karel Volný <kvolny@redhat.com> 620-1
- New version 620
- Adds Ume Hy Gothic font in a new subpackage

* Sat May 14 2016 Karel Volný <kvolny@redhat.com> 610-2
- Fixed fontconfig issue, thanks to Parag Nemade (rhbz#1330613)

* Mon Apr 25 2016 Karel Volný <kvolny@redhat.com> 610-1
- New version 610
- Fixes as per the review request (rhbz#1301144)
 - dropped -common subpackage, license included everywhere
 - changed summary

* Fri Jan 22 2016 Karel Volný <kvolny@redhat.com> 580-1
- Initial release
