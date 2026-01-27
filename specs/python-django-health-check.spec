Name:           python-django-health-check
Version:        3.20.8
Release:        1%{?dist}
Summary:        Monitor the health of your Django app and its connected services

License:        MIT
URL:            https://github.com/codingjoe/django-health-check
Source:         %{url}/archive/%{version}/django-health-check-%{version}.tar.gz

# Downstream-only: patch out coverage-analysis (pytest-cov) options for pytest
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          django-health-check-3.20.8-pytest-no-coverage.patch

BuildArch:      noarch

BuildRequires:  tomcli

%global _description %{expand:
Pluggable health checks for Django applications. This project checks for
various conditions and provides reports when anomalous behavior is detected.}

%description %_description

%package -n python3-django-health-check
Summary:        %summary

# The -doc subpackage previously contained only the README and license file.
# Now we ship the Markdown sources because they are useful on their own. (We
# could build them with mkdocs, but there are missing extensions, and the
# resulting HTML would have license and bundling difficulties similar to those
# noted in RHBZ#2006555.) Since these sources are small in size and not
# numerous, we don’t need to split them out into a -doc subpackage.
Provides:       python-django-health-check-doc = %{version}-%{release}
Obsoletes:      python-django-health-check-doc < 3.20.8

%description -n python3-django-health-check %_description

%prep
%autosetup -n django-health-check-%{version}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem dependency-groups.test 'pytest-cov\b.*'

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -g test

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l health_check

%check
PYTHONPATH="${PWD}" %pytest

%files -n python3-django-health-check -f %{pyproject_files}
%doc README.md
# Markdown sources and associated images
%doc docs/

%changelog
* Sun Jan 18 2026 Benjamin A. Beasley <code@musicinmybrain.net> - 3.20.8-1
- Update to 3.20.8
- Port to pyproject-rpm-macros (fix RHBZ#2377644)

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 3.16.5-15
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 3.16.5-14
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 3.16.5-12
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.16.5-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.16.5-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.16.5-2
- Rebuilt for Python 3.11

* Wed Apr 6 2022 David Moreau-Simard - 3.16.5-1
- Update to latest upstream release
- Includes fix for django 4.x (https://github.com/KristianOellegaard/django-health-check/commit/93e9cdd1e881f255166df2d1189fcae838a077a9)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.11.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.11.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 David Moreau Simard <dmsimard@redhat.com> - 3.11.0-1
- First version of the package
