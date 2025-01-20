Name:           python-google-i18n-address
%global srcname %(echo %{name} | sed 's/^python-//')
%global pypi_name %(echo %{srcname} | sed 's/-/_/g')

Version:        3.1.0
Release:        7%{?dist}
Summary:        Address validation helpers for Google's i18n address database

# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            https://pypi.python.org/pypi/google-i18n-address/
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package contains a copy of Google’s i18n address metadata
repository that contains great data but comes with no uptime guarantees.

Contents of this package will allow you to programatically build address
forms that adhere to rules of a particular region or country, validate
local addresses and format them to produce a valid address label for
delivery.

The package also contains a Python interface for address validation.}

%description %_description

%package -n python3-%{srcname}
Summary: Address validation helpers for Google's i18n address database
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
# warns about obsolete testing, and then downloads files from the internet
#{__python3} setup.py test

%install
%pyproject_install
%pyproject_save_files i18naddress
# names used for test files are sure to cause clashses with other packages :/
rm -rf %{buildroot}/%{python3_sitelib}/tests
# 1. It requires `sudo`, since data files are saved in the code directory: `/usr/lib/python3.11/site-packages/i18naddress/data`
# 2. Even with `sudo` it crashes.
rm -rf %{buildroot}/%{_bindir}/update-validation-files

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.1.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Roman Inflianskas <rominf@aiven.io> - 3.1.0-1
- Update to 3.1.0 (resolve rhbz#2212266)
- Update package to use new Python macros.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.5.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 02 2022 Paul Wouters <paul.wouters@aiven.io - 2.5.2-1
- Resolves rhbz#2077524 python-google-i18n-address-2.5.2 is available

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 11:30:10 EDT 2020 Paul Wouters <pwouters@redhat.com> - 2.4.0-1
- Initial package
