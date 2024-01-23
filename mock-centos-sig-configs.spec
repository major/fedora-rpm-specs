Name:           mock-centos-sig-configs
Version:        0.5.2
Release:        3%{?dist}
Summary:        Mock configs for CentOS SIGs

License:        MIT
URL:            https://pagure.io/centos-sig-hyperscale/mock-centos-sig-configs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
Requires:       mock-core-configs
%if 0%{?el7}
%else
Enhances:       mock-core-configs
%endif

BuildArch:      noarch

%description
This package contains mock configs for various CentOS SIGs.

%prep
%setup -q

%build

%install
%if 0%{?el7}
mkdir -p %{buildroot}%{_sysconfdir}/mock/templates
%endif
%make_install

%files
%license LICENSE
%doc README.md
%defattr(0644, root, mock)
%config(noreplace) %{_sysconfdir}/mock/*.cfg
%config(noreplace) %{_sysconfdir}/mock/templates/*.tpl

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2; fixes centos-stream-hyperscale-spin-9.tpl

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Thu Sep 08 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.5-1
- Update to 0.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 03 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.4-2
- Fix build on el7

* Sun Apr 03 2022 Davide Cavalca <dcavalca@fedoraproject.org> - 0.4-1
- Update to 0.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.3-1
- Update to 0.3

* Wed May 12 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.2-1
- Update to 0.2

* Tue Apr 20 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1-3
- Gate out Enhances for el7 as it's not supported there

* Sat Apr 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1-2
- Add Enhances for mock-core-configs

* Fri Apr 16 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.1-1
- Initial package
