Name:           python-qcelemental
Version:        0.28.0
Release:        5%{?dist}
Summary:        Periodic table, physical constants, and molecule parsing for quantum chemistry
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/MolSSI/QCElemental
Source0:        https://github.com/MolSSI/QCElemental/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-numpy
BuildRequires:  python3-pint
BuildRequires:  python3-pydantic
BuildRequires:  python3-networkx

%description
QCElemental is a resource module for quantum chemistry containing
physical constants and periodic table data from NIST and molecule
handlers.

Periodic Table and Physical Constants data are pulled from NIST srd144
and srd121, respectively (details) in a renewable manner (class around
NIST-published JSON file).

This project also contains a generator, validator, and translator for
Molecule QCSchema.

%package -n     python3-qcelemental
Summary:        %{summary}
%{?python_provide:%python_provide python3-qcelemental}
# For some reason, these dependencies aren't picked up automatically
Requires: python3-numpy
Requires: python3-pint
Requires: python3-pydantic
Requires: python3-networkx

%description -n python3-qcelemental
QCElemental is a resource module for quantum chemistry containing
physical constants and periodic table data from NIST and molecule
handlers.

Periodic Table and Physical Constants data are pulled from NIST srd144
and srd121, respectively (details) in a renewable manner (class around
NIST-published JSON file).

This project also contains a generator, validator, and translator for
Molecule QCSchema.

%prep
%setup -q -n QCElemental-%{version}
# Remove bundled egg-info
rm -rf QCElemental.*-info

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest qcelemental

%files -n python3-qcelemental
%license LICENSE
%doc README.md
%{python3_sitelib}/qcelemental
%{python3_sitelib}/qcelemental-%{version}.dist-info

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 07 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.28.0-4
- Add Requires: python3-networkx which appears to be necessary.

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.28.0-3
- convert license to SPDX

* Mon Sep 02 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.28.0-2
- Restore dependencies that haven't been detected automatically
  (erroneously removed in 0.25.0-3).

* Wed Aug 28 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.28.0-1
- Update to 0.28.0.
- Enable tests.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 0.26.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 04 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.26.0-1
- Update to 0.26.0.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.25.1-1
- Update to 0.25.1.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Miro Hrončok <mhroncok@redhat.com> - 0.25.0-3
- Remove build dependencies from runtime

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.25.0-1
- Update to 0.25.0.

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.12.0-10
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.12.0-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.12.0-2
- Fix FTBFS: also pytest-cov is needed.

* Mon Jan 06 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0.
- Review fixes.

* Sat Jul 27 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.5.0-1
- Initial package.
