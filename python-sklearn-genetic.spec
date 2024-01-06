%bcond tests 1

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

%global pypi_name sklearn-genetic

%global _description %{expand:
sklearn-genetic is a genetic feature selection module for scikit-learn.
Genetic algorithms mimic the process of natural selection to search
for optimal values of a function.}

# Package a snapshot to support modern versions of sklearn and numpy. We do
# this rather than applying a patch because the other changes since 0.5.1 are
# trivial and desirable:
# https://github.com/manuel-calzolari/sklearn-genetic/compare/0.5.1...12ee9b2e591ec379793bcff1966095b43dac10c6
%global commit 12ee9b2e591ec379793bcff1966095b43dac10c6
%global snapdate 20230819

Name:           python-%{pypi_name}
Version:        0.5.1%{?commit:^%{snapdate}git%(c='%{commit}'; echo "${c:0:7}")}
Release:        1%{?dist}
Summary:        A genetic feature selection module for scikit-learn

License:        LGPL-3.0-only
URL:            https://github.com/manuel-calzolari/%{pypi_name}
%global srcversion %{expr:%{defined commit}?"%{?commit}":"%{version}"}
Source:         %{url}/archive/%{srcversion}/%{pypi_name}-%{srcversion}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{srcversion}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files -l genetic_selection

%check
%if %{with tests}
%pytest
%endif

%files -n python3-sklearn-genetic -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE.txt
%if %{with doc_pdf}
%doc docs/build/latex/%{pypi_name}.pdf
%endif

%changelog
* Wed Aug 23 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.5.1^20230819git12ee9b2-1
- Fix compatibility with numpy 1.20 and later and with modern scikit-learn
- Convert License to SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Python Maint <python-maint@redhat.com> - 0.5.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 05 2022 Python Maint <python-maint@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.11

* Sun Apr 10 2022 Iztok Fister Jr. <iztokf AT fedoraproject DOT org> - 0.5.1-1
- Initial package
