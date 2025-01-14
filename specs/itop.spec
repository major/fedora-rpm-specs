%global commit      fb22eff1cde008dc009e738736d844bfd6c594f2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       itop
Version:    0.1
Release:    22.20220502gitfb22eff1%{?dist}
Summary:    Interactive interrupt viewer

License:    MIT
URL:        https://github.com/kargig/%{name}
Source0:    https://github.com/kargig/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:  noarch
BuildRequires:  perl-generators


%description
Interrupts 'top-like' utility for Linux


%prep
%setup -qn %{name}-%{commit}


%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%doc README.md
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/%{name}


%changelog
* Sun Jan 12 2025 Florian Lehner <dev@der-flo.net> 0.1-22.20220502gitfb22eff1
- Update package to commit fb22eff1cde008dc009e738736d844bfd6c594f2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-20.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3.20150225git6dbb3c42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 26 2015 Florian Lehner <dev@der-flo.net> 0.1-2.20150225git6dbb3c42
- Fix issue in Package Versioning
- Fix issue of missing license-tag in EL6
- Fix naming of downloaded Source0

* Wed Feb 25 2015 Florian Lehner <dev@der-flo.net> 20150225git6dbb3c42-1
- Initial packaging (#1196353)
