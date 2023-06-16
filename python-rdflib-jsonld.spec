%bcond_without tests

%global pypi_name rdflib-jsonld

%global _description %{expand:
This is an implementation of JSON-LD for RDFLib. JSON-LD is a lightweight
Linked Data format. It is easy for humans to read and write. It is based on
the already successful JSON format and provides a way to help JSON data
inter operate at Web-scale.

This implementation will:
- Read in an JSON-LD formatted document and create an RDF graph
- Serialize an RDF graph to JSON-LD formatted output}

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        8%{?dist}
Summary:        Python rdflib extension adding JSON-LD parser and serializer

License:        BSD
URL:            https://github.com/RDFLib/rdflib-jsonld
Source0:        %{pypi_source}

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist rdflib}

# v6.0.0 of rdflib provides rdflib-jsonld itself. This package would not
# be compatible with future releases of rdflib
Conflicts:      python3-rdflib >= 6.0.0

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}
BuildRequires:	%{py3_dist sphinx}

%description doc %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

# Build documentation
PYTHONPATH=. sphinx-build-%{python3_version} docs html
rm -rvf html/.buildinfo
rm -rvf html/.doctrees

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=. pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/rdflib_jsonld/
%{python3_sitelib}/rdflib_jsonld-%{version}-py%{python3_version}.egg-info/

%files doc
%license LICENSE.md
%doc html

%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.6.0-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.6.0-3
- Drop spurious or obsolete flake8 BR

* Sat Sep 11 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 0.6.0-2
- Add conflicts for python3-rdflib-6.0.0

* Sat Sep 11 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 0.6.0-1
- Version bump to v0.6.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.5.0-1
- Initial build
