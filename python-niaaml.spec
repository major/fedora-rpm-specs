%bcond tests 1
# It’s nice to be able to run the examples as additional tests, but we normally
# choose not to do so since some examples take as much as several hours to run.
%bcond test_examples 0
# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

%global pypi_name niaaml
%global pretty_name NiaAML

%global _description %{expand:
NiaAML is a framework for Automated Machine Learning based on nature-inspired
algorithms for optimization. The framework is written fully in Python. The
name NiaAML comes from the Automated Machine Learning method of the same name.
Its goal is to compose the best possible classification pipeline for the given
task efficiently using components on the input. The components are divided
into three groups: feature selection algorithms, feature transformation
algorithms and classifiers. The framework uses nature-inspired algorithms
for optimization to choose the best set of components for the
classification pipeline, and optimize their hyperparameters.}

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        %autorelease
Summary:        Python automated machine learning framework

License:        MIT
URL:            https://github.com/lukapecnik/%{pretty_name}
Source:         %{url}/archive/%{version}/%{pretty_name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%package doc
Summary:        %{summary}

BuildRequires:  dos2unix
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
%endif

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{pretty_name}-%{version}
rm -fv poetry.lock

# Make deps consistent with Fedora deps
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

# Ensure the Python interpreter path is correct in the example runner script:
sed -r -i 's|\bpython3\b|%{python3}|' examples/run_all.sh

# Fix CRNL (DOS-style) line endings
dos2unix --keepdate paper/paper.bib

%generate_buildrequires
# There exists a docs/requirements.txt, but it seems to be inaccurate, with a
# large number of unnecessary dependencies, so we do not use it to generate
# BR’s.
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files niaaml

%check
%if %{with tests}
%pytest
%endif
%if %{with test_examples}
# See also: examples/run_all.sh
find examples -type f -name '*.py' |
  env %{py3_test_envvars} xargs -r -n 1 -t -P %{_smp_build_ncpus} -I '{}' \
      '%{python3}' '{}'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md COMPONENTS.md CITATION.md

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc docs/_build/latex/%{pypi_name}.pdf
%endif
%doc examples/
%doc paper/
%doc docs/paper/10.21105.joss.02949.pdf
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md CITATION.md

%changelog
%autochangelog
