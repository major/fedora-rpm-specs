%global pkg dockerfile-mode

Name:           emacs-%{pkg}
Version:        1.9
Release:        3%{?dist}
Summary:        An emacs mode for handling Dockerfiles

License:        Apache-2.0
URL:            https://github.com/spotify/%{pkg}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-s
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-s
BuildArch:      noarch

%description
This package provides a major mode `dockerfile-mode' for use with the standard
`Dockerfile' file format.  Additional convenience functions allow images to be
built easily.


%prep
%autosetup -n %{pkg}-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 02 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.9-1
- Update to 1.9
- Migrate to SPDX license

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.8-1
- Update to 1.8

* Tue Aug 09 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.7-1
- Update to 1.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 01 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.6-1
- Update to 1.6

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 04 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5-1
- Update to 1.5

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.4-1
- Update to 1.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 13 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.3-1
- Update to 1.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.2-1
- Initial RPM release
