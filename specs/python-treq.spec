%global pypi_name treq

%global with_doc 1

Name:           python-%{pypi_name}
Version:        24.9.1
Release:        2%{?dist}
Summary:        A requests-like API built on top of twisted.web's Agent

License:        MIT
URL:            https://github.com/twisted/treq
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch


%if 0%{?with_doc}
BuildRequires:  python3-twisted
BuildRequires:  python3-sphinx
%endif
 
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-httpbin

%description
treq is an HTTP library inspired by requests but written on top of
Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests
when using Twisted.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
treq is an HTTP library inspired by requests but written on top of
Twisted’s Agents.
It provides a simple, higher level API for making HTTP requests
when using Twisted.

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        treq documentation
%description -n python-%{pypi_name}-doc
Documentation for treq
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if 0%{?with_doc}
# generate html docs
export PYTHONPATH=%{python2_sitelib}:%{python3_sitelib}:src
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files treq

%check
%pytest -v


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 20 2024 Yatin Karel <ykarel@redhat.com> - 24.9.1-1
- Update to 24.9.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Charalampos Stratakis <cstratak@redhat.com> - 23.11.0-3
- Eliminate cgi usage
Resolves: rhbz#2290560

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 23.11.0-2
- Rebuilt for Python 3.13

* Thu Feb 15 2024 Orion Poplawski <orion@nwra.com> - 23.11.0-1
- Update to 23.11.0
- Use pyproject macros

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 21.5.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 21.5.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.5.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.5.0-1
- 21.5.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.1.0-2
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Dan Callaghan <djc@djc.id.au> - 21.1.0-1
- Update to 21.1.0 (RHBZ#1813778, RHBZ#1953535)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 18.6.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Orion Poplawski <orion@nwra.com> - 18.6.0-1
- Update to 18.6.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 17.8.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 17.8.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 17.8.0-6
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 17.8.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Yatin Karel <ykarel@redhat.com> - 17.8.0-2
- Enabled Doc build, Fix BR Issues and some nit picks

* Fri Aug 11 2017 ykarel <ykarel@redhat.com> - 17.8.0-1
- Initial package.
