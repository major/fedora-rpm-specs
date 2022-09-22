%global pypi_name stdlib-list

%global desc %{expand: \
Python Standard Library List -This package includes lists of all of the
standard libraries for Python, along with the code for scraping the official
Python docs to get said lists.Listing the modules in the standard library?
Wait, why on Earth would you care about that?! Because knowing whether or
not a module is part of the standard library will come in}

Name:       python-%{pypi_name}
Version:    0.8.0
Release:    6%{?dist}
Summary:    A list of Python Standard Libraries

License:    MIT
URL:        https://github.com/jackmaney/python-stdlib-list
# pypi is missing docs, so use the github tarball instead
Source0:    %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:  noarch

%{?python_enable_dependency_generator}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:    %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

# The require not picked up by the dep generator
Requires:   python3dist(sphinx)
Requires:   python3dist(sphinx-rtd-theme)

%description -n python3-%{pypi_name}
%{desc}

%package doc
Summary:   %{name} documentation

%description doc
Documentation for %{name}

%prep
%autosetup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/stdlib_list
%{python3_sitelib}/stdlib_list-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%doc html

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.10

* Mon Mar 15 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Sun Mar 07 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.6.0-8
- Build docs
- Use GitHub tarball instead of PyPI

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-5
- Update patch to include lists required by other packages

* Sat Jun 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-4
- Update for python 3.9
- TODO: enable tests added in next release

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.6.0-1
- New upstream version

* Mon Nov 11 2019 Ankur Sinha <ankursinha@fedoraproject.org> - 0.5.0-5
- Fix requires
- https://bugzilla.redhat.com/show_bug.cgi?id=1770852

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.5.0-2
- Fix comments BZ 1741623

* Thu Aug 15 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.5.0-1
- Initial package.
