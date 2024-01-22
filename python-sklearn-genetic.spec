%bcond tests 1

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

%global _description %{expand:
sklearn-genetic is a genetic feature selection module for scikit-learn.
Genetic algorithms mimic the process of natural selection to search
for optimal values of a function.}

Name:           python-sklearn-genetic
Version:        0.6.0
Release:        %autorelease
Summary:        A genetic feature selection module for scikit-learn

License:        LGPL-3.0-only
URL:            https://github.com/manuel-calzolari/sklearn-genetic
Source:         %{url}/archive/%{version}/sklearn-genetic-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-sklearn-genetic
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n python3-sklearn-genetic %_description

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
%autosetup -n sklearn-genetic-%{version}

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
%doc docs/build/latex/sklearn-genetic.pdf
%endif

%changelog
%autochangelog
