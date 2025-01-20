%bcond_without tests
%bcond_without docs
%global pypi_name interrogate

%global _description %{expand:
interrogate checks your code base for missing docstrings.
Documentation should be as important as code itself. And it should 
live within code. Python standardized docstrings, allowing for developers 
to navigate libraries as simply as calling help() on objects, and with 
powerful tools like Sphinx, pydoc, and Docutils to automatically generate 
HTML, LaTeX, PDFs, etc.}

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        3%{?dist}
Summary:        Interrogate a codebase for docstring coverage

License:        MIT
URL:            https://github.com/econchick/interrogate
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
%endif

%if %{with docs}
BuildRequires:  python3dist(sphinx)
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n python-%{pypi_name}-doc
Summary:  %{summary}

%description -n python-%{pypi_name}-doc
Documentation for interrogate

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest tests/

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/interrogate

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.7.0-1
- Update to 1.7.0

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.6.0-2
- Rebuilt for Python 3.13

* Sun Apr 7 2024 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.6.0-1
- Update to 1.6.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.5.0-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.5.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 12 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.5.0-1
- Update to the latest upstream's release

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.10

* Sat May 15 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.4.0-1
- Update to the latest upstream's release

* Wed Apr 7 2021 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 1.3.2-1
- Initial package
