Name:    python-shamir-mnemonic
Version: 0.3.0
Release: 3%{?dist}
Summary: Reference implementation of SLIP-0039: Shamir’s Secret-Sharing for Mnemonic Codes

License: MIT
URL:     https://github.com/trezor/python-shamir-mnemonic
Source0: %{pypi_source shamir_mnemonic}

BuildArch:     noarch
BuildRequires: python3-devel


%global _description %{expand:
This SLIP describes a standard and interoperable implementation of
Shamir's secret sharing (SSS). SSS splits a secret into unique parts which can
be distributed among participants, and requires a specified minimum number of
parts to be supplied in order to reconstruct the original secret.
Knowledge of fewer than the required number of parts does not leak information
about the secret.}

%description %_description

%package -n python3-shamir-mnemonic
Summary: %{summary}

%description -n python3-shamir-mnemonic %_description


%prep
%autosetup -n shamir_mnemonic-%{version}


%generate_buildrequires
%pyproject_buildrequires -x cli


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files shamir_mnemonic


%check
%pyproject_check_import


%files -n python3-shamir-mnemonic -f %{pyproject_files}
%license LICENSE
%doc README.rst
%doc CHANGELOG.rst
%{_bindir}/shamir


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.14

* Sat Apr 05 2025 Jonny Heggheim <hegjon@gmail.com> - 0.3.0-1
- Updated to 0.3.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.2.2-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.2.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Jonny Heggheim <hegjon@gmail.com> - 0.2.2-1
- Updated to 0.2.2

* Mon Aug 02 2021 Jonny Heggheim <hegjon@gmail.com> - 0.2.1-4
- Relax the version depenendcy on click to support version 8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.10

* Fri Apr 02 2021 Jonny Heggheim <hegjon@gmail.com> - 0.2.1-1
- Updated to 0.2.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Jonny Heggheim <hegjon@gmail.com> - 0.1.0-1
- Inital packaging
