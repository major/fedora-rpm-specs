# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

# Not yet packaged (python-aiobotocore)
%bcond aiobotocore 0
# Not yet packaged (python-django-fake-model)
%bcond django 0
# Only compatibile with python-pg8000 < 1.20
%bcond pg8000 0
# Only compatibile with python-flask-sqlalchemy <= 2.5.1
%bcond flask_sqlalchemy %{expr:%{defined fc37} || %{defined fc38}}

# All of the tests for the following extensions require network access. (A few
# may succeed without it, but this is because they expected a failure, and a
# slightly different failure occurred instead.)
#
# We considered sending a PR upstream to add a “network” pytest mark so we
# could deselect these all at once with “-m 'not network',” but pytest would
# exit nonzero (failure) for any tox environments for which all tests were
# deselected, and that is quite annoying to work around; see
# https://github.com/pytest-dev/pytest/issues/5689. Instead we simply do not
# consider these environments.
%bcond httplib 0
%bcond httpx 0
%bcond pynamodb 0
%bcond requests 0

# The situation here is the same except that there are middleware tests that
# *do* all succeed, so we do not need to disable the entire environment.
# Instead, the module containing the client tests is ignored with a pytest
# flag.
%bcond aiohttp 1

Name:           python-aws-xray-sdk
Summary:        AWS X-Ray SDK for the Python programming language
Version:        2.12.1
Release:        %autorelease

# The entire source is Apache-2.0, except that sample-apps/ (packaged in the
# -doc subpackage) is MIT-0.
License:        Apache-2.0
URL:            https://github.com/aws/aws-xray-sdk-python
# We use the GitHub tarball instead of the PyPI sdist to get documentation
# and tests.
Source:         %{url}/archive/%{version}/aws-xray-sdk-python-%{version}.tar.gz

# Fix passing multiple values in testenv.passenv in tox.ini
# https://github.com/aws/aws-xray-sdk-python/pull/399
Patch:          %{url}/pull/399.patch
# Enable testing on Python 3.12
# https://github.com/aws/aws-xray-sdk-python/pull/400
# Rebased on top of PR#399, above.
Patch:          python-aws-xray-sdk-2.12.0-python3.12.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%if %{without django}
# Not brought in via tox environments, but needed for documentation:
BuildRequires:  python3dist(django)
%endif
%endif

BuildRequires:  postgresql-server

%global common_description %{expand:
The AWS X-Ray SDK for Python (the SDK) enables Python developers to record and
emit information from within their applications to the AWS X-Ray service.}

%description %{common_description}


%package -n     python3-aws-xray-sdk
Summary:        %{summary}

%description -n python3-aws-xray-sdk %{common_description}


%package        doc
Summary:        Documentation and examples for aws-xray-sdk
License:        Apache-2.0 AND MIT-0

%description doc %{common_description}


%prep
%autosetup -n aws-xray-sdk-python-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i \
    -e 's/coverage run.*-m //' \
    -e 's/^([[:blank:]]*)(coverage|codecov)\b/\1; \2/' \
    tox.ini

cp -p sample-apps/LICENSE LICENSE.sample-apps


%generate_buildrequires
%{pyproject_buildrequires -e \
%{toxenv}-core,\
%{?with_aiobotocore:%{toxenv}-ext-aiobotocore,}\
%{?with_aiohttp:%{toxenv}-ext-aiohttp,}\
%{toxenv}-ext-botocore,\
%{toxenv}-ext-bottle,\
%{?with_django:%{toxenv}-ext-django-4,}\
%{toxenv}-ext-flask,\
%{?with_flask_sqlalchemy:%{toxenv}-ext-flask_sqlalchemy,}\
%{?with_httplib:%{toxenv}-ext-httplib,}\
%{?with_httpx:%{toxenv}-ext-httpx},\
%{?with_pg8000:%{toxenv}-ext-pg8000,}\
%{toxenv}-ext-psycopg2,\
%{?with_pynamodb:%{toxenv}-ext-pynamodb,}\
%{?with_requests:%{toxenv}-ext-requests,}\
%{toxenv}-ext-sqlalchemy,\
%{toxenv}-ext-sqlalchemy_core,\
%{toxenv}-ext-sqlite3}


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex \
    SPHINXBUILD='sphinx-build' SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l aws_xray_sdk

install -t '%{buildroot}%{_pkgdocdir}' -p -m 0644 -D \
    %{?with_doc_pdf:docs/_build/latex/aws-xray-sdk.pdf} \
    CHANGELOG.rst README.md
cp -vpr sample-apps/ '%{buildroot}%{_pkgdocdir}'


%check
# See tox-distributioncheck.ini:
%pytest tests/distributioncheck

# Tests for the pymysql extension require a running mysql/mariadb server. We
# used to do this, using rubygem-mysql2 as an example, but it has become
# impractical to keep this working.

%if %{with aiohttp}
# See the note above the aiohttp bcond
ignore="${ignore-} --ignore=tests/ext/aiohttp/test_client.py"
%endif

# This will automatically run all the environments for which we generated
# dependencies in %%generate_buildrequires.
%tox -- -- -v --asyncio-mode=auto ${ignore-}


%files -n python3-aws-xray-sdk -f %{pyproject_files}


%files doc
%license LICENSE NOTICE

%doc %dir %{_pkgdocdir}/
%doc %{_pkgdocdir}/CHANGELOG.rst
%doc %{_pkgdocdir}/README.md
%if %{with doc_pdf}
%doc %{_pkgdocdir}/aws-xray-sdk.pdf
%endif

%doc %dir %{_pkgdocdir}/sample-apps/
%doc %{_pkgdocdir}/sample-apps/*/
%license %{_pkgdocdir}/sample-apps/LICENSE



%changelog
%autochangelog
