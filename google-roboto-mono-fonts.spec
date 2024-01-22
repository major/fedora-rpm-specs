%global fontconf 64-%{fontname}
%global fontname google-roboto-mono
%global commit0 90d7886db9000c893b9559828bf028aaed5f9c10

Name:          google-roboto-mono-fonts
Version:       3.000
Release:       0.5.20220620git%{?dist}
Summary:       Google Roboto Mono fonts

License:       ASL 2.0
URL:           https://www.google.com/fonts/specimen/Roboto+Mono
# There are no tar archive so let's pick all the individual source files from github
Source0:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono-Italic%5Bwght%5D.ttf
Source1:       https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/RobotoMono%5Bwght%5D.ttf
Source10:      https://raw.githubusercontent.com/google/fonts/%{commit0}/apache/robotomono/LICENSE.txt
Source11:      %{fontname}-fontconfig.conf
Source12:      %{fontname}.metainfo.xml
BuildArch:     noarch

BuildRequires: fontpackages-devel

%description
Roboto Mono is a monospaced addition to the Roboto type family. Like the other
members of the Roboto family, the fonts are optimized for readability on
screens across a wide variety of devices and reading environments. While the
monospaced version is related to its variable width cousin, it doesn't hesitate
to change forms to better fit the constraints of a monospaced environment. For
example, narrow glyphs like 'I', 'l' and 'i' have added serifs for more even
texture while wider glyphs are adjusted for weight. Curved caps like 'C' and
'O' take on the straighter sides from Roboto Condensed.

%prep
cp -p %{SOURCE0} %{SOURCE1} .
cp -p %{SOURCE10} %{SOURCE11} %{SOURCE12} .

%build
# nothing to build here

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{SOURCE0} %{buildroot}%{_fontdir}/RobotoMono-Italic[wght].ttf
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontdir}/RobotoMono[wght].ttf

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE11} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-fontconfig.conf

install -m 0755 -d %{buildroot}%{_metainfodir}
install -m 0644 -p %{SOURCE12} %{buildroot}%{_metainfodir}

%_font_pkg -f %{fontconf}-fontconfig.conf RobotoMono*.ttf
%{_metainfodir}/%{fontname}.metainfo.xml
%license LICENSE.txt

%changelog
* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.000-0.5.20220620git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.000-0.4.20220620git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.000-0.3.20220620git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.000-0.2.20220620git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Link Dupont <linkdupont@fedoraproject.org> - 3.000-0.1.20220620git
- New upstream version (RHBZ#2098473)
- Switch to variable weight fonts (RHBZ#2098473)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-0.5.20200129git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-0.4.20200129git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-0.3.20200129git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.002-0.2.20200129git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Link Dupont <linkdupont@fedoraproject.org> - 2.002-0.1.20200129git
- New upstream version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000986-0.6.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000986-0.5.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000986-0.4.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000986-0.3.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.000986-0.2.20150923git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.000986-0.1.20150923git
- Initial package
