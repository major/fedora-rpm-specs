%global pypi_name pytest-sugar

%global _description %{expand:
pytest-sugar is a plugin for pytest that shows failures and errors instantly
and shows a progress bar.}

Name:           python-%{pypi_name}
Version:        0.9.4
Release:        4%{?dist}
Summary:        Change the default look and feel of pytest

License:        BSD
URL:            https://pypi.org/project/%{pypi_name}
Source0:        %pypi_source

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

BuildRequires:  %{py3_dist packaging}
BuildRequires:  %{py3_dist termcolor}
BuildRequires:  %{py3_dist pytest}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=. %{pytest}

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/pytest_sugar-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/pytest_sugar.py
%dir %{python3_sitelib}/__pycache__
%{python3_sitelib}/__pycache__/pytest_sugar*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.4-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 27 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.4-1
- Update to latest release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.3-1
- Update to 0.9.3
- Enable tests: failures with pytest5 were fixed in this release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.2-1
- Correct macro usage
- Temporarily disable tests

* Fri Jul 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.2-1
- Initial build
