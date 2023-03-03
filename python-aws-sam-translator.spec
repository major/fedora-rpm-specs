Name:           python-aws-sam-translator
Summary:        Transform SAM templates into AWS CloudFormation templates
Version:        1.60.1
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/aws/serverless-application-model
# We use the GitHub tarball instead of the PyPI tarball to get documentation
# and tests.
Source0:        %{url}/archive/v%{version}/serverless-application-model-%{version}.tar.gz

# chore: Loose typing_extensions version requirement
# https://github.com/aws/serverless-application-model/pull/2916
Patch:          %{url}/pull/2916.patch
# Do not install “schema_source” to site-packages
# https://github.com/aws/serverless-application-model/pull/2973
Patch:          %{url}/pull/2973.patch

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

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

# Comment out a few dev dependencies that we will not use. Then, loosen
# selected semver-pinned dev dependencies, allowing newer versions.
sed -r -i \
    -e 's/^(black|flake8|pylint|ruff)\b/#\1/' \
    -e 's/^(coverage|pytest-cov|tox)\b/#\1/' \
    -e 's/^(mypy|boto3-stubs|types-.*)\b/#\1/' \
    -e 's/^(click|parameterized|pytest(-(rerunfailures|xdist))?)~=/\1>=/' \
    -e 's/^(pyyaml|requests|tenacity)~=/\1>=/' \
    requirements/dev.txt
# Finish patching out coverage
sed -r -i '/^addopts[[:blank:]]*=/d' pytest.ini


%generate_buildrequires
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files samtranslator
# Bug: Source directory bin/ is installed into site-packages
# https://github.com/aws/serverless-application-model/issues/2588
rm -rvf '%{buildroot}%{python3_sitelib}/bin'


%check
# See Makefile target “test”. We cannot run the interaction tests because they
# interact with AWS.
AWS_DEFAULT_REGION=us-east-1 %pytest -k "${k-}" -n auto


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
