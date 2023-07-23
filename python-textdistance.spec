
%global pypi_name textdistance

%global _description %{expand:
TextDistance - python library for comparing distance between two or more 
sequences by many algorithms.

Features:
- 30+ algorithms
- Pure python implementation
- Simple usage
- More than two sequences comparing
- Some algorithms have more than one implementation in one class.
- Optional numpy usage for maximum speed.
}

Name:           python-%{pypi_name}
Version:        4.2.0
Release:        12%{?dist}
Summary:        Compute distance between the two texts
License:        MIT
URL:            https://github.com/orsinium/textdistance
Source0:        %{pypi_source}
# numpy 1.24.x removes numpy.int and so on
Patch0:         https://github.com/life4/textdistance/pull/75.patch
# JaroWinkler boosting fix
Patch1:         https://github.com/life4/textdistance/pull/76.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# required for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(jellyfish)

%description
%_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%_description


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Fix bad executable permission
mkdir -p %{buildroot}%{_docdir}/python3-%{pypi_name}
cp -pr README.md %{buildroot}%{_docdir}/python3-%{pypi_name}
chmod 644 %{buildroot}%{_docdir}/python3-%{pypi_name}/README.md

%check
# disable tests that need abydos
%{__python3} -m pytest -v -k 'not test_list_of_numbers and not test_qval and not test_compare'

%files -n python3-%{pypi_name}
%license LICENSE
%{_docdir}/python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.0-11
- Backport upstream patch for numpy 1.24.x numpy.int removal
- Backport upstream patch for test_jaro_winkler test fix

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 4.2.0-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.2.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 25 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.0-2
- Fix directory ownership
- run tests

* Thu Dec 24 2020 Mukundan Ragavan <nonamedotc@gmail.com> - 4.2.0-1
- Initial package.
