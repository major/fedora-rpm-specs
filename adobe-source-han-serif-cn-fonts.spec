%global fontname adobe-source-han-serif-cn
%global fontconf 65-2-%{fontname}.conf

%global archivename SourceHanSerifCN

Name:           adobe-source-han-serif-cn-fonts
Version:        2.001
Release:        3%{?dist}
Summary:        Adobe OpenType Pan-CJK font family for Simplified Chinese

License:        OFL
URL:            https://github.com/adobe-fonts/source-han-serif/
Source0:        https://github.com/adobe-fonts/source-han-serif/raw/release/SubsetOTF/%{archivename}.zip
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Source Han Serif is a set of OpenType/CFF Pan-CJK fonts.

%prep
%autosetup -c

%build


%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.otf

%license LICENSE.txt


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 28 2022 Peng Wu <pwu@redhat.com> - 2.001-1
- Update to 2.001

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Peng Wu <pwu@redhat.com> - 2.000-1
- Update to 2.000

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Akira TAGOH <tagoh@redhat.com> - 1.001-6
- Update the fontconfig priority to ensure this as default for upgrading.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb  1 2018 Peng Wu <pwu@redhat.com> - 1.001-4
- Update the priority to change the default font to Noto

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Peng Wu <pwu@redhat.com> - 1.001-2
- Use Source Han Sans for Mono and Sans
- Use Source Han Serif for Serif

* Mon Jun 12 2017 Peng Wu <pwu@redhat.com> - 1.001-1
- Initial Version
