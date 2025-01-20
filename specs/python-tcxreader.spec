%bcond_without tests

%global pypi_name tcxreader
%global fullversion 0.4.10

%global _description %{expand:
This is a simple TCX parser / reader which can read Garmin TCX file
extension files. The following data is currently parsed:
longitude, latitude, elevation, time, distance, hr_value, cadence,
watts, TPX_speed (extension). It also works well with missing data!}

Name:           python-%{pypi_name}
Version:        %{?fullversion}
Release:        3%{?dist}
Summary:        tcxreader is a parser/reader for Garmin's TCX file format

# SPDX
License:        MIT
URL:            https://github.com/alenrajsp/tcxreader
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%if %{with tests}
cd tcxreader
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc examples/ example_data/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.10-1
- Update to 0.4.10

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.9-2
- Rebuilt for Python 3.13

* Fri Feb 9 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.9-1
- Update to 0.4.9

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 30 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.6-1
- Update to 0.4.6

* Fri Nov 24 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.5-1
- Update to 0.4.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.4-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.4-1
- New release

* Thu Oct 6 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.2-1
- New release

* Tue Aug 9 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.4.1-1
- New release

* Mon Aug 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.15-1
- New release

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.14-2
- Rebuilt for Python 3.11

* Sat May 7 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.14-1
- New release

* Mon Apr 18 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.13-4
- Do not package the tests (new patch)

* Mon Apr 18 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.13-3
- Remove several dependencies

* Sat Apr 16 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.13-2
- Switch to (python) rpm macros

* Mon Mar 28 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.13-1
- New release

* Wed Mar 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.9-1
- New release

* Sat Feb 12 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.8-7
- Update description

* Thu Jan 27 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.8-6
- Correct Source0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 1 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.8-4
- Use pytest macro

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.8-2
- Rebuilt for Python 3.10

* Mon Apr 26 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.8-1
- Update to the latest release -- 0.3.8
- Add LICENSE

* Thu Apr 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.6-3
- Install examples and datasets to docs

* Tue Apr 13 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.6-2
- Editing dependencies (problems with F32 and F33)

* Tue Mar 30 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.6-1
- New version - 0.3.6
- Enable tests

* Mon Mar 22 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.3-2
- Removing cosmetic macro

* Sun Mar 14 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.3-1
- New version - 0.3.3

* Fri Mar 05 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.3.2-1
- Initial package
