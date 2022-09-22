# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-aws-sam-translator
Summary:        Transform SAM templates into AWS CloudFormation templates
Version:        1.51.0
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/aws/serverless-application-model
# We use the GitHub tarball instead of the PyPI tarball to get documentation
# and tests.
Source0:        %{url}/archive/v%{version}/serverless-application-model-%{version}.tar.gz

# The base package is arched because we conditionalize tests; the binary
# packages are all noarch, and there is no compiled code.
%global debug_package %{nil}

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
%{summary}.

AWS Serverless Application Model (SAM) is an open-source framework for building
serverless applications.}

%description %{common_description}


%package -n     python3-aws-sam-translator
Summary:        %{summary}

BuildArch:      noarch

%description -n python3-aws-sam-translator %{common_description}


%package        doc
Summary:        Documentation for aws-sam-translator

BuildArch:      noarch

%description doc %{common_description}


%prep
%autosetup -n serverless-application-model-%{version} -p1

# Unbundle bundled “third-party” dependencies
rm -rvf THIRD_PARTY_LICENSES samtranslator/third_party
sed -r -i '/^[[:blank:]]*"THIRD_PARTY_LICENSES",[[:blank:]]*$/d' setup.py
sed -r -i '/^[[:blank:]]*THIRD_PARTY_LICENSES[[:blank:]]*$/d' setup.cfg
sed -r -i 's/samtranslator\.third_party\.(py27hash)/\1/g' \
    samtranslator/utils/py27hash_fix.py
echo 'py27hash >= 1.0.2' >> requirements/base.txt

# Comment out a few dev dependencies that we will not use. Then, loosen
# selected semver-pinned dev dependencies, allowing newer versions.
sed -r -i \
    -e 's/^(black|coverage|flake8|pylint|pytest-cov|tox)\b/#\1/' \
    -e 's/^(mypy|boto3-stubs|types-.*)\b/#\1/' \
    -e 's/^(click|parameterized|pytest|pyyaml|requests|tenacity)~=/\1>=/' \
    requirements/dev.txt
sed -r -i -e 's/^(jsonschema)~=/\1>=/' requirements/base.txt
# Patch out coverage
sed -r -i '/^addopts[[:blank:]]*=/d' pytest.ini


%generate_buildrequires
%pyproject_buildrequires -x dev


%build
%pyproject_wheel

%if %{with doc_pdf}
sphinx-build -b latex %{?_smp_mflags} docs %{_vpath_builddir}/_latex
%make_build -C %{_vpath_builddir}/_latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files samtranslator


%check
%if 0%{?__isa_bits} == 32
# This test only has an expected value for 64-bit platforms. Since we no longer
# need to support 32-bit platforms, we don’t bother trying to fix it:
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# https://fedoraproject.org/wiki/Changes/RetireARMv7
k="${k-}${k+ and }not (TestPy27UniStr and test_py27_hash)"
%endif
# Feature request: Support jsonschema 4.x
# https://github.com/aws/serverless-application-model/issues/2426
#
# This test fails because it asserts the exact number of validation errors;
# this seems to mean the test is too strict, rather than that it is revealing a
# real problem.
k="${k-}${k+ and }not (TestValidatorApi and test_errors_13_error_definitionuri)"
# See Makefile target “test”. We cannot run the interaction tests because they
# interact with AWS.
%pytest -k "${k-}" -n %{_smp_build_ncpus}


%files -n python3-aws-sam-translator -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE; verify with “rpm -qL -p …”
%doc README.md


%files doc
%license LICENSE NOTICE
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc DESIGN.md
%doc DEVELOPMENT_GUIDE.md
%doc HOWTO.md
%doc INTEGRATION_TESTS.md
%doc README.md
%if %{with doc_pdf}
%doc %{_vpath_builddir}/_latex/SAM.pdf
%endif


%changelog
%autochangelog
