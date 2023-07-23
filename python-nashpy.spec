%bcond_with docs
%bcond_without tests

%global pypi_name nashpy
%global pretty_name Nashpy

%global _description %{expand:
This library implements the following algorithms for Nash equilibria
on 2 player games: Support enumeration, Best response polytope vertex
enumeration, Lemke Howson algorithm.}

Name:           python-%{pypi_name}
Version:        0.0.37
Release:        2%{?dist}
Summary:        A library to compute equilibria of 2 player normal form games

License:        MIT
URL:            https://github.com/drvinceknight/%{pretty_name}
Source0:        %{url}/archive/v%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: %{py3_dist packaging}
BuildRequires: %{py3_dist pep517}	
BuildRequires: %{py3_dist flit}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(matplotlib)

# For documentation
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
#missing for now
#BuildRequires:  python3dist(sphinx-togglebutton)

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%if %{with docs}
%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.
%endif

%prep
%autosetup -n %{pretty_name}-%{version}

%generate_buildrequires	
%pyproject_buildrequires -r


%build
%pyproject_wheel

%if %{with docs}
# Generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files nashpy

%check	
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES.md CITATION.md paper paper.bib

%if %{with docs}
%files doc
%license LICENSE
%doc html/
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 6 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.37-1
- Update to 0.0.37

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.36-2
- Enable tests

* Thu Jan 12 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.36-1
- Update to 0.0.36

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.35-2
- Rename element in doc

* Thu Jun 23 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.35-1
- Update to 0.0.35

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.0.32-2
- Rebuilt for Python 3.11

* Wed Apr 13 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.32-1
- New upstream's release

* Sat Mar 19 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.31-1
- New upstream's release

* Tue Mar 1 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.30-1
- New upstream's release

* Mon Jan 24 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.28-4
- Remove dependency (pyproject-rpm-macros)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 27 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.28-2
- Disable tests for now

* Wed Oct 27 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.28-1
- New upstream's release

* Fri Sep 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.25-2
- Remove code checker

* Thu Aug 5 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.25-1
- Update to the latest version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.24-2
- Disable building docs (dependencies not satisfied)

* Fri Jul 9 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.24-1
- Update to the latest version

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.23-3
- Rebuilt for Python 3.10

* Tue May 4 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.23-2
- Enhance tests with 'interrogate'

* Tue May 4 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.23-1
- Update to the latest version
- Using pyprojet-rpm (upstream switched to flit)

* Mon Apr 5 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.21-1
- Add subpackage for docs

* Sun Apr 4 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.0.21-1
- Initial package
