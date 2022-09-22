# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Created by pyp2rpm-3.3.2
%global pypi_name pytest-flake8

%global desc \
%{name} is a plugin for pytest to leverage flake8 to automatically\
and efficiently checking for PEP8 compliance of a project.

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Plugin for pytest to check PEP8 compliance with Flake8

License:        BSD
URL:            https://github.com/tholo/pytest-flake8
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description %{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{desc}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_flake8


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
# license file included in %%pyproject_files
%doc README.rst

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.6-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.6-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-1
- Update to 1.0.6 (#1827518) to fix compatibility with flake8 3.8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Dan Radez <dradez@redhat.com> - 1.0.4-1
- update to 1.0.4

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Subpackage python2-pytest-flake8 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 11 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.1-1
- Initial package
