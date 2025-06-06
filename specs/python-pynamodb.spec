# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-pynamodb
Summary:        A pythonic interface to Amazon’s DynamoDB
Version:        6.1.0
Release:        %autorelease

# SPDX
License:        MIT
URL:            https://github.com/pynamodb/PynamoDB
# We use the GitHub tarball instead of the PyPI tarball to get documentation
# and tests.
Source:         %{url}/archive/%{version}/PynamoDB-%{version}.tar.gz

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x signals requirements-filtered.txt
BuildOption(install):   -l pynamodb

BuildArch:      noarch

%if %{with doc_pdf}
BuildRequires:  make
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


%prep -a
{
%if %{with doc_pdf}
  # Un-pin exact versions in doc dependencies.
  #
  # We can’t handle self-referential dependencies like .[signals]; we use the
  # -x argument to %%pyproject_buildrequires instead
  sed -r -e 's/==/>=/' -e 's/^\.\[/# &/' docs/requirements.txt
%endif
  # Get non-CI dev dependencies (no coverage/linting)
  awk '/^# only used in CI/ {ci=1}; !ci' requirements-dev.txt
} | tee requirements-filtered.txt


%build -a
%if %{with doc_pdf}
%make_build -C docs SPHINXOPTS='-j%{?_smp_build_ncpus}' latex
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%check -a
# The integration tests need to connect to a local copy of DynamoDB; see the
# “Run dynamodb_local” step in .github/workflows.test.yaml. We can’t use a
# pre-compiled Java application for testing, and only a negligible number of
# integration tests can work without it, so we skip the integration tests.
ignore="${ignore-} --ignore-glob=tests/integration/*"

# Regression in test_connection_make_api_call__binary_attributes due to
# JMESPathTypeError since botocore 1.37.12
# https://github.com/pynamodb/PynamoDB/issues/1265
k="${k-}${k+ and }not test_connection_make_api_call__binary_attributes"

%pytest ${ignore-} -k "${k-}" -v


%files -n python3-pynamodb -f %{pyproject_files}
%doc README.rst


%files doc
%license LICENSE
%doc README.rst
%doc examples/
%if %{with doc_pdf}
%doc docs/_build/latex/PynamoDB.pdf
%endif


%changelog
%autochangelog
