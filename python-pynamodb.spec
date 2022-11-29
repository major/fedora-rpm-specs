# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-pynamodb
Summary:        A pythonic interface to Amazon’s DynamoDB
Version:        5.3.3
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/pynamodb/PynamoDB
# We use the GitHub tarball instead of the PyPI tarball to get documentation
# and tests.
Source0:        %{url}/archive/%{version}/PynamoDB-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
%{summary}.

DynamoDB is a great NoSQL service provided by Amazon, but the API is verbose.
PynamoDB presents you with a simple, elegant API.}

%description %{common_description}


%package -n     python3-pynamodb
Summary:        %{summary}

%description -n python3-pynamodb %{common_description}


%pyproject_extras_subpkg -n python3-pynamodb signals


%package        doc
Summary:        Documentation and examples for PynamoDB

%description doc %{common_description}


%prep
%autosetup -n PynamoDB-%{version} -p1

{
%if %{with doc_pdf}
  # Un-pin exact versions in doc dependencies
  sed -r 's/==/>=/' docs/requirements.txt
%endif
  # Get non-CI dev dependencies (no coverage/linting)
  awk '/^# only used in CI/ {ci=1}; !ci' requirements-dev.txt
} | tee requirements-filtered.txt
# Don’t generate (unfiltered) dev dependencies for tox:
sed -r -i 's/[-]rrequirements-dev\.txt//' tox.ini


%generate_buildrequires
%pyproject_buildrequires -t requirements-filtered.txt


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs SPHINXOPTS='%{?_smp_mflags}' latex
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files pynamodb


%check
%tox


%files -n python3-pynamodb -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE; verify with “rpm -qL -p …”
%doc README.rst


%files doc
%license LICENSE
%doc README.rst
%doc examples
%if %{with doc_pdf}
%doc docs/_build/latex/PynamoDB.pdf
%endif


%changelog
%autochangelog
