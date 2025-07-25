Name:           python-ibm-vpc
Version:        0.28.0
Release:        3%{?dist}
Summary:        Python client library for IBM Cloud VPC Services

License:        Apache-2.0
URL:            https://github.com/IBM/vpc-python-sdk
Source0:        %{url}/archive/v%{version}/vpc-python-sdk-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# test dependencies are in requirements-dev.txt but mixed with coverage and linters
# tox configuration uses the same file
BuildRequires:  python3-pytest
BuildRequires:  python3-responses

%global _description %{expand:
Python client library to interact with various IBM Cloud Virtual Private Cloud
(VPC) Service APIs.
}


%description %_description

%package -n     python3-ibm-vpc
Summary:        %{summary}

%description -n python3-ibm-vpc %_description


%prep
%autosetup -p1 -n vpc-python-sdk-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'ibm_vpc'


%check
%pytest -v test/unit


%files -n python3-ibm-vpc -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 0.28.0-2
- Rebuilt for Python 3.14

* Mon Apr 28 2025 Packit <hello@packit.dev> - 0.28.0-1
- Update to version 0.28.0
- Resolves: rhbz#2362764

* Mon Mar 24 2025 Packit <hello@packit.dev> - 0.27.0-1
- Update to version 0.27.0
- Resolves: rhbz#2351745

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Packit <hello@packit.dev> - 0.26.3-1
- Update to version 0.26.3
- Resolves: rhbz#2336082

* Thu Nov 14 2024 Packit <hello@packit.dev> - 0.25.0-1
- Update to version 0.25.0
- Resolves: rhbz#2326209

* Tue Nov 05 2024 Packit <hello@packit.dev> - 0.24.1-1
- Update to version 0.24.1
- Resolves: rhbz#2323981

* Thu Sep 12 2024 Packit <hello@packit.dev> - 0.23.0-1
- Update to version 0.23.0
- Resolves: rhbz#2267845

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild
* Mon Jul 08 2024 Packit <hello@packit.dev> - 0.23.0-1
- Update to version 0.23.0
- Resolves: rhbz#2267845

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.20.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 16 2023 Packit <hello@packit.dev> - 0.20.0-1
- chore(release): 0.20.0 release notes (semantic-release-bot)
- Update version 0.19.1 -> 0.20.0 (semantic-release-bot)
- feat(release): Update SDK to use API released on 2023-11-07 travis (#60) (Deepak Selvakumar)
- feat(release): Update SDK to use API released on 2023-11-07 (#59) (Deepak Selvakumar)
- feat(release): Update SDK to use API released on 2023-11-07 (#58) (Deepak Selvakumar)
- Resolves rhbz#2250149

* Sat Oct 07 2023 Packit <hello@packit.dev> - 0.19.1-1
- chore(release): 0.19.1 release notes (semantic-release-bot)
- Update version 0.19.0 -> 0.19.1 (semantic-release-bot)
- fix(headers): updated common headers for request id (#57) (Ujjwal Kumar)

* Wed Aug 02 2023 Pavel Raiskup <praiskup@redhat.com> - 0.18.0-1
- new upstream release, per release notes:
  https://github.com/IBM/vpc-python-sdk/releases/tag/v0.18.0
  https://github.com/IBM/vpc-python-sdk/releases/tag/v0.17.0
  https://github.com/IBM/vpc-python-sdk/releases/tag/v0.16.0
  https://github.com/IBM/vpc-python-sdk/releases/tag/v0.15.0
  https://github.com/IBM/vpc-python-sdk/releases/tag/v0.14.0
  https://github.com/IBM/vpc-python-sdk/releases/tag/v0.13.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.12.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 02 2022 Pavel Raiskup <praiskup@redhat.com> - 0.12.0-1
- new upstream release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Pavel Raiskup <praiskup@redhat.com> - 0.9.0-3
- drop the TODO generated by pyp2spec

* Sat Jan 01 2022 Pavel Raiskup <praiskup@redhat.com> - 0.9.0-2
- drop +auto, per review, rhbz#2035004

* Wed Dec 22 2021 Pavel Raiskup <praiskup@redhat.com> - 0.9.0-1
- initial package, pre-generated by pyp2spec
