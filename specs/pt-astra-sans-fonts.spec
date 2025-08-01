Version: 1.002
Release: 9%{?dist}

URL: https://astralinux.ru/en/information/#section-fonts-astra

%global foundry  PT
%global fontlicense  OFL-1.1
%global fontlicenses  LICENSE.txt

%global fontfamily  PT Astra Sans
%global fontsummary  Sans fonts that are metric analogs of Times New Roman
%global fontdescription  %{expand:Russian free-for-all fonts that are 
metric analogs of the Times New Roman font. The use of these fonts 
instead of Times New Roman doesn’t lead to document distortion, and 
freeware distribution and cross-platform combined with modern design make
them suitable and user-friendly in the any operating system and office 
program.}

%global fonts  %{name}-%{version}/*.ttf
%global fontconfs  %{SOURCE10}

Source0: https://astralinux.ru/information/fonts-astra/font-ptastrasans-ttf-ver1002.zip 
Source10: 60-%{fontpkgname}.xml
# https://astralinux.ru/en/ofl
Source11: LICENSE.txt

%fontpkg


%prep
%setup -q -c
unzip -n %{SOURCE0} -d %{name}-%{version}

%build
%fontbuild
install -p -m 0644 %{SOURCE11} .


%install
%fontinstall


%check
%fontcheck


%fontfiles


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 23 2025 Akira TAGOH <tagoh@redhat.com> - 1.002-8
- Fix FTBFS issue.
  Resolves: rhbz#2341115

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Benson Muite <benson_muite@emailplus.org> - 1.002-1
- Update to latest release

* Tue Aug 16 2022 Benson Muite <benson_muite@emailplus.org> - 1.001-3
- Name spec file correctly, simplify spec file and indicate source of LICENSE

* Sun Aug 07 2022 Benson Muite <benson_muite@emailplus.org> - 1.001-2
- Update foundry according to review from Parag AN

* Sun Jul 31 2022 Benson Muite <benson_muite@emailplus.org> - 1.001-1
- Initial packaging
