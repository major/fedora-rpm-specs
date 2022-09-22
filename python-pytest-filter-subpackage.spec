%global srcname pytest-filter-subpackage
%global pythonicname pytest_filter_subpackage
%global sum Pytest plugin for filtering based on sub-packages


Name:           python-%{srcname}
Version:        0.1.1
Release:        8%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
This package contains a simple plugin for the pytest framework that provides
a shortcut to testing all code and documentation for a given sub-package.}

%description %_description


%package -n python3-%{srcname}
Summary:        %{sum}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%py_provides python3-%{srcname}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}

# Remove egg files from source
rm -r %{pythonicname}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst CHANGES.rst
%{python3_sitelib}/%{pythonicname}/
%{python3_sitelib}/*.egg-info/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Mattia Verga <mattia.verga@protonmail.com> - 0.1.1-2
- Correct Provides - fixes rhbz#1902785

* Sun Nov 15 2020 Mattia Verga <mattia.verga@protonmail.com> - 0.1.1-1
- Initial packaging
