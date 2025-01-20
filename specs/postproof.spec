%global commit      65bcbbb9d2cf9e44e71d9cfa3bd4e4eddd32ec38
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       postproof
Version:    0
Release:    0.24.20150331git65bcbbb9%{?dist}
Summary:    Mail abuse incident tool

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:    LGPL-3.0-only
URL:        https://github.com/sys4/%{name}
Source0:    https://github.com/sys4/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:  noarch

Requires:   postfix

%description
Collect messages from a Postfix mail queue and preserve them as incident.

%prep
%setup -qn %{name}-%{commit}


%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 *.1 %{buildroot}%{_mandir}/man1


%files
%doc README
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/*.1*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.24.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.23.20150331git65bcbbb9
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.22.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20150331git65bcbbb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 31 2015 Florian Lehner <dev@der-flo.net> 0-0.3.20150331git65bcbbb9
- Update to latest snapshot before importing

* Sun Mar 29 2015 Florian Lehner <dev@der-flo.net> 0-0.2.20150324gita7427efd
- Fix release tag

* Tue Mar 24 2015 Florian Lehner <dev@der-flo.net> 0-1.20150324gita7427efd
- Initial packaging (#1205361)
