# Enable the automatic Python dependency generator
%{?python_enable_dependency_generator}

# Tests do not work without vagrant + virtualbox in the environment
%bcond_with tests

%global pypi_name vagrantpy

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        12%{?dist}
Summary:        Python bindings for interacting with Vagrant virtual machines

License:        MIT
URL:            https://github.com/vagrantpy/vagrantpy
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%if %{with tests}
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(rednose)
BuildRequires:  vagrant
BuildRequires:  virtualbox
%endif

%description
VagrantPy is a python module that provides a _thin_ wrapper
around the vagrant command line executable, allowing programmatic control of
Vagrant virtual machines (boxes).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
VagrantPy is a python module that provides a _thin_ wrapper
around the vagrant command line executable, allowing programmatic control of
Vagrant virtual machines (boxes).

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
nosetests --immediate --stop -vv --rednose
%endif

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/vagrant
%{python3_sitelib}/vagrantpy-%{version}-*

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.0-12
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.0-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 David McCheyne <davidmccheyne@gmail.com> - 0.6.0-1
- Packaging for Fedora

* Wed Jan 15 2020 Neal Gompa <ngompa13@gmail.com>
- Initial packaging
