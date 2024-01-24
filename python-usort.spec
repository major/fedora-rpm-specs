%bcond_without docs

# Created by pyp2rpm-3.3.5
%global pypi_name usort

%global common_description %{expand:
μsort is a safe, minimal import sorter. Its primary goal is to make no
"dangerous" changes to code, and to make no changes on code style. This is
achieved by detecting distinct "blocks" of imports that are the most likely to
be safely interchangeable, and only reordering imports within these blocks
without altering formatting. Code style is left as an exercise for linters and
formatters.}

Name:           python-%{pypi_name}
Version:        0.6.3
Release:        11%{?dist}
Summary:        A small, safe import sorter

License:        MIT
URL:            https://github.com/facebookexperimental/usort
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  sed
BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(libcst)
BuildRequires:  python3dist(m2r)
BuildRequires:  python3dist(moreorless)
BuildRequires:  python3dist(setuptools) >= 38.3
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(stdlib-list)
BuildRequires:  python3dist(toml)
%if %{with docs}
BuildRequires:  python3-docs
BuildRequires:  python-stdlib-list-doc
BuildRequires:  python3dist(sphinx)
%endif

%description
%{common_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} == 32
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
%{common_description}

%if %{with docs}
%package doc
Summary:        Documentation for %{name}
Requires:       python3-docs

%description doc
Documentation for %{name}.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
sed -e 's/python/python3/g' -i Makefile
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%if %{with docs}
# Use local intersphinx inventory
sed -r \
    -e 's|https://docs.python.org/3|%{_docdir}/python3-docs/html|' \
    -e 's|https://python-stdlib-list.readthedocs.io/en/latest|%{_docdir}/python-stdlib-list-doc/html|' \
    -i docs/conf.py
%endif

%build
%py3_build
%if %{with docs}
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%{__make} test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/usort
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%if %{with docs}
%files doc
%doc html
%license LICENSE
%endif

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Python Maint <python-maint@redhat.com> - 0.6.3-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.6.3-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.3-3
- Rebuilt for Python 3.10

* Wed Mar 17 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.6.3-2
- Build docs by default

* Sun Mar 07 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 0.6.3-1
- Initial package.
