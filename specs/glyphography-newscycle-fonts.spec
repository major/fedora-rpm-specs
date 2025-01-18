Version:        0.5.2
Release:        15%{?dist}
URL:            https://launchpad.net/newscycle

%global foundry           glyphography
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        newscycle
%global fontsummary       A realist sans-serif font family based on News Gothic

%global fonts             *.ttf
%global fontconfs         %{SOURCE10}

%global fontdescription   %{expand:
Inspired by the original News Gothic, which found an eminently useful
life in print media news coverage, the goal of this project is to design
a highly readable open font suitable for large bodies of text, even at
small sizes, and that is available at multiple weights. In addition to
the readability and weight, however, the project is extending News
Gothic's glyph coverage to alphabets derived from Latin, Cyrillic, and
Greek, including the accent marks and diacritics required by languages
outside of Western Europe.
}

Source0:        %{url}/trunk/%{version}/+download/%{fontfamily}-%{version}.zip
Source10:       61-%{fontpkgname}.conf

%fontpkg

%prep
%setup -n %{fontfamily}-%{version}
rm -f *~ *.svg

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.2-4
- Fix path to fonts.dtd

* Wed Feb 26 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.2-3
- Add "glyphography" as foundry name, rename package

* Wed Feb 26 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.2-2
- Adapt to the new guidelines https://pagure.io/packaging-committee/issue/935

* Tue Feb 25 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.5.2-1
- Initial packaging for Fedora
