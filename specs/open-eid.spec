Name:           open-eid
Version:        17.12
Release:        21%{?dist}
Summary:        Meta-package for Estonian Electronic Identity Software

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.ria.ee
BuildArch:      noarch

Requires:       qdigidoc
Requires:       web-eid
Provides:       estonianidcard = %{version}-%{release}
Obsoletes:      estonianidcard <= 3.12.0-2

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running ID-card utilities.

%prep
%setup -c -T


%build


%install


%files


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 24 2024 Germano Massullo <germano.massullo@gmail.com> - 17.12-20
- Replaced Requires: firefox-pkcs11-loader with web-eid

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 17.12-19
- convert license to SPDX

* Sun Jul 21 2024 Germano Massullo <germano.massullo@gmail.com> - 17.12-18
- Remove deprecated webextension-token-signing

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 28 2018 Germano Massullo <germano@germanomassullo.org> - 17.12-4
- removed Requires: qesteidutil

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 16 2018 Germano Massullo <germano.massullo@gmail.com> - 17.12-2
- rebuilt

* Fri Mar 02 2018 Germano Massullo <germano.massullo@gmail.com> - 17.12-1
- 17.12-1 release

* Tue Feb 02 2016 Mihkel Vain <mihkel@fedoraproject.org> - 3.12.0-1
- Bump version number

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 10 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.1-2
- Remove doc since there is no documentation
- Remove opensc and pcsc-lite package from requires

* Tue Mar  4 2014 Mihkel Vain <mihkel@fedoraproject.org> - 3.8.1-1
- Initial meta-package

