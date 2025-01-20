%bcond_without tests
# we do not build docs since current docs are immature


%bcond_without doc_pdf

%global pypi_name succulent

%global _description %{expand:
Sending sensor measurements, data, or GPS positions from embedded devices,
microcontrollers, and smartwatches to the central server is sometimes
complicated and tricky. Setting up the primary data collection scripts
can be time-consuming (selecting a protocol, framework, API, testing it, etc.).
Usually, scripts are written for a specific task; thus, they are not easily
adaptive to other tasks. succulent is a pure Python framework that simplifies
the configuration, management, collection, and preprocessing of data collected
via POST requests. }

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        2%{?dist}
Summary:        Collect POST requests

License:        MIT
URL:            https://github.com/firefly-cpp/%{pypi_name}
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3-toml-adapt
BuildRequires:  python3-pytest

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
%endif

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        Documentation and examples for %{name}

%description doc
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# optional step but let's ensure that there is no problems with python, pandas and Flask versions
toml-adapt -path pyproject.toml -a change -dep python -ver X
toml-adapt -path pyproject.toml -a change -dep flask -ver X
toml-adapt -path pyproject.toml -a change -dep pandas -ver X
toml-adapt -path pyproject.toml -a change -dep lxml -ver X
toml-adapt -path pyproject.toml -a change -dep numpy -ver X

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files succulent

%check
%if %{with tests}
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md CITATION.cff

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/succulent.pdf
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 6 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.4.0-1
- Update to 0.4.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.3.2-3
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.3.2-1
- Update to 0.3.2

* Sun Dec 17 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.3.0-1
- Update to 0.3.0

* Fri Dec 8 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.2.7-1
- Update to 0.2.7

* Thu Nov 16 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.2.6-1
- Update to 0.2.6

* Fri Aug 18 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.2.5-2
- Add subpackage for docs

* Thu Aug 17 2023 Iztok Fister Jr. <iztok@iztok-jr-fister.eu> - 0.2.5-1
- Update to 0.2.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.4-1
- Update to 0.2.4

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.2.3-2
- Rebuilt for Python 3.12

* Tue Jun 20 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.3-1
- Update to 0.2.3

* Mon Jun 5 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.2-1
- Update to 0.2.2

* Fri Jun 2 2023 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.2.1-1
- Initial package
