Name:           python-aws-sam-translator
Summary:        Transform SAM templates into AWS CloudFormation templates
Version:        1.95.0
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/aws/serverless-application-model
# We use the GitHub tarball instead of the PyPI tarball to get documentation
# and tests.
Source:         %{url}/archive/v%{version}/serverless-application-model-%{version}.tar.gz

# Downstream-only: omit coverage arguments for pytest
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          python-aws-sam-translator-1.73.0-no-coverage.patch

# Failing tests on warnings makes sense for upstream CI, but is too strict for
# distribution packaging, where warnings may arise at any time from updated
# dependencies.
Patch:          python-aws-sam-translator-1.73.0-no-warning-error.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# Because most of the dependencies in the “dev” extra (from
# requirements/dev.txt) are unwanted or have version bounds that need to be
# loosened, we list them manually rather than generating BuildRequires from the
# “dev” extra.
# ----------
# Omitted dependencies in the following group are due to:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# coverage>=5.3,<8
# pytest-cov>=2.10,<5
# pytest-xdist>=2.5,<4
BuildRequires:  %{py3_dist pytest-xdist} >= 2.5
# pytest-env>=0.6,<1
BuildRequires:  %{py3_dist pytest-env} >= 0.6
# pytest-rerunfailures>=9.1,<12
BuildRequires:  %{py3_dist pytest-rerunfailures} >= 9.1
# pyyaml~=6.0
BuildRequires:  %{py3_dist pyyaml} >= 6
# ruff~=0.1.0
# ----------
# Test requirements
# pytest>=6.2,<8
BuildRequires:  %{py3_dist pytest} >= 6.2
# parameterized~=0.7
BuildRequires:  %{py3_dist parameterized} >= 0.7
# ----------
# We cannot run the integration tests because they interact with AWS.
#
# Integration tests
# dateparser~=1.1
# boto3>=1.23,<2
# tenacity~=8.0
# ----------
# The description in requirements/dev.txt is not quite correct; requests is
# actually another integration test dependency (see above).
#
# Requirements for examples
# requests~=2.28
# ----------
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# formatter
# black==23.10.1
# ruamel.yaml==0.17.21  # It can parse yaml while perserving comments
# ----------
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# type check
# mypy~=1.3.0
# ----------
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# types
# boto3-stubs[appconfig,serverlessrepo]>=1.19.5,==1.*
# types-PyYAML~=6.0
# types-jsonschema~=3.2

%global common_description %{expand:
%{summary}.

AWS Serverless Application Model (SAM) is an open-source framework for building
serverless applications.}

%description %{common_description}


%package -n     python3-aws-sam-translator
Summary:        %{summary}

# The bundled version is quite close to upstream. It has some “ignore” type
# annotations added, some if statements were reordered (apparently to put this
# library’s common case first for performance), and an LRU cache layer was
# added.
#
# When the type annotations were the only difference, we unbundled this as a
# downstream patch. Now we bundle again, but we have asked upstream about a
# path to unbundling—a request which was mandated by
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling:
#
#   Path to using upstream py27hash as a dependency?
#   https://github.com/aws/serverless-application-model/issues/2815
#
# Upstream refused: “Unfortunately due to how the SAM transform is consumed
# this would be a little tricky, so unless there's customer impact, it's not
# something we're looking to change at this time.”
Provides:       bundled(python3dist(py27hash)) = 1.0.2

Obsoletes:      python-aws-sam-translator-doc < 1.54.0-1

%description -n python3-aws-sam-translator %{common_description}


%prep
%autosetup -n serverless-application-model-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files samtranslator
# Bug: Source directory bin/ is installed into site-packages
# https://github.com/aws/serverless-application-model/issues/2588
rm -rvf '%{buildroot}%{python3_sitelib}/bin'


%check
# See Makefile target “test”. We cannot run the integration tests because they
# interact with AWS.
AWS_DEFAULT_REGION=us-east-1 PYTHONPATH="${PWD}" %pytest -k "${k-}" -n auto


%files -n python3-aws-sam-translator -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE/NOTICE/THIRD_PARTY_LICENSES; verify with
# “rpm -qL -p …”
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc DESIGN.md
%doc HOWTO.md
%doc README.md
# Contains a handful of reStructuredText files:
%doc docs/


%changelog
%autochangelog
