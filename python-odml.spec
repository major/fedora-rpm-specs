%bcond_without tests

%global pypi_name odml

%global _description %{expand:
odML (open metadata Markup Language) is a file format for storing 
arbitrary metadata. The underlying data model offers a way to 
store metadata in a structured human- and machine-readable way.
Well organized metadata management is a key component to 
guarantee reproducibility of experiments and to track provenance
of performed analyses.

python-odml is the python library for reading and writing odml
metadata files. It is a registered research resource with the
RRID:SCR_001376.}

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        5%{?dist}
Summary:        File-format to store metadata in an organized way

License:        BSD
URL:            https://g-node.github.io/python-odml/
Source0:        https://github.com/G-Node/python-%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist lxml}
BuildRequires:  %{py3_dist pyyaml}
BuildRequires:  %{py3_dist rdflib}
BuildRequires:  %{py3_dist docopt}
# Cannot use the py3_dist macro as it changes owl_rl to owl-rl
BuildRequires:  python3-owl_rl
%endif

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}
BuildRequires:	%{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}

%description doc %_description

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'
# Remove pathlib from install_requires from setup.py
sed -i -e 's/, "pathlib"//g' setup.py

%build
%py3_build

# Build documentation
PYTHONPATH=. sphinx-build-3 doc html
rm -rvf html/.buildinfo
rm -rvf html/.doctrees

# Add examples to a common folder
mkdir examples
cp -prv doc/example* examples

%install
%py3_install

%check
%if %{with tests}
# test_version_converter needs an internet connection, therefore disabled
PYTHONPATH=. pytest-%{python3_version} --deselect test/test_version_converter.py
%endif

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/odML-%{version}-py%{python3_version}.egg-info/
%{_bindir}/odmlconversion
%{_bindir}/odmlconvert
%{_bindir}/odmltordf
%{_bindir}/odmlview

%files doc
%license LICENSE
%doc html examples

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.1-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 1.5.1-1
- Updated to v1.5.1
- Removed auto-dep generator

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.4-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.4.4-3
- Added setuptools to BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.4-2
- Rebuilt for Python 3.9

* Mon Jan 27 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 1.4.4-1
- Initial build
