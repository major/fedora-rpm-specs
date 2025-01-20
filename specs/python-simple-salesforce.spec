%global pypi_name simple-salesforce
%global pypi_version 1.12.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        7%{?dist}
Summary:        Simple Salesforce is a basic Salesforce.com REST API client built for Python
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/%{pypi_name}/%{pypi_name}
Source0:        %{url}/archive/v%{pypi_version}/%{pypi_name}-v%{pypi_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Tests requirements:
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(responses)

%global _description %{expand:
Simple Salesforce is a basic Salesforce.com REST API client built for Python.
The goal is to provide a very low-level interface to the REST Resource and APEX
API, returning a dictionary of the API JSON response. }

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{pypi_version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
# Set timezone to prevent Pendulum error: `RuntimeError: Unable to find any timezone configuration`
export TZ=UTC
%pytest

%install
%pyproject_install
%pyproject_save_files simple_salesforce

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst docs/user_guide docs/changes.rst docs/conf.py
%license LICENSE.txt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12.5-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Python Maint <python-maint@redhat.com> - 1.12.5-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 07 2023 Roman Inflianskas <rominf@aiven.io> - 1.12.5-1
- Update to 1.12.5 (fedora#2220501)
- Use version tag instead of commit hash to make updates easier.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Roman Inflianskas <rominf@aiven.io> - 1.12.4-1
- Update to 1.12.4
- Rebuilt for Python 3.12 (resolve rhbz#2220501)
- Simplify testing

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.11.5-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.11.5-2
- Rebuilt for Python 3.11

* Mon Feb 28 2022 Paul Wouters <paul.wouters@aiven.io> - 1.11.5-1
- Initial package
