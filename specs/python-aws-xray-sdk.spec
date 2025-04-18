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
# Only compatibile with python-flask-sqlalchemy <= 2.5.1 and flask < 3.0.0
%bcond flask_sqlalchemy 0

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
# Only compatible with pynamodb < 6.0.0
%bcond pynamodb 0
%bcond requests 0

# The situation here is the same except that there are middleware tests that
# *do* all succeed, so we do not need to disable the entire environment.
# Instead, the module containing the client tests is ignored with a pytest
# flag.
%bcond aiohttp 1

Name:           python-aws-xray-sdk
Summary:        AWS X-Ray SDK for the Python programming language
Version:        2.14.0
Release:        %autorelease

# The entire source is Apache-2.0, except that sample-apps/ (packaged in the
# -doc subpackage) is MIT-0.
%global sample_apps_license MIT-0
License:        Apache-2.0
SourceLicense:  %{license} AND %{sample_apps_license}
URL:            https://github.com/aws/aws-xray-sdk-python
# We use the GitHub tarball instead of the PyPI sdist to get documentation
# and tests.
Source:         %{url}/archive/%{version}/aws-xray-sdk-python-%{version}.tar.gz

# Adjust intersphinx_mapping for Sphinx 8 compatibility
# https://github.com/aws/aws-xray-sdk-python/pull/449
Patch:          %{url}/pull/449.patch

# Modernize event loop handling in aiohttp tests
# https://github.com/aws/aws-xray-sdk-python/pull/455
# Fixes compatibility with python-pytest-aiohttp-1.1.0
Patch:          %{url}/pull/455.patch

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
License:        %{license} AND %{sample_apps_license}

%description doc %{common_description}


%prep
%autosetup -n aws-xray-sdk-python-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# Remove the version bound on pytest-asyncio: we cannot respect an
# exact-version pin, and currently we can’t even satisfy it as a lower-bound.
sed -r -i \
    -e 's/coverage run.*-m //' \
    -e 's/^([[:blank:]]*)(coverage|codecov)\b/\1; \2/' \
    -e 's/(pytest-asyncio) == [[:digit:].]+/\1/' \
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

# Tests for the pymysql extension require a running mysql/mariadb server. So
# does the following test. We used to do this, using rubygem-mysql2 as an
# example, but it has become impractical to keep this working.
k="${k-}${k+ and }not test_db_url_with_special_char"

%if %{with aiohttp}
# See the note above the aiohttp bcond
ignore="${ignore-} --ignore=tests/ext/aiohttp/test_client.py"
%endif

%{tox -e \
%{default_toxenv}-core,\
%{?with_aiobotocore:%{default_toxenv}-ext-aiobotocore,}\
%{?with_aiohttp:%{default_toxenv}-ext-aiohttp,}\
%{default_toxenv}-ext-botocore,\
%{default_toxenv}-ext-bottle,\
%{?with_django:%{default_toxenv}-ext-django-4,}\
%{default_toxenv}-ext-flask,\
%{?with_flask_sqlalchemy:%{default_toxenv}-ext-flask_sqlalchemy,}\
%{?with_httplib:%{default_toxenv}-ext-httplib,}\
%{?with_httpx:%{default_toxenv}-ext-httpx},\
%{?with_pg8000:%{default_toxenv}-ext-pg8000,}\
%{default_toxenv}-ext-psycopg2,\
%{?with_pynamodb:%{default_toxenv}-ext-pynamodb,}\
%{?with_requests:%{default_toxenv}-ext-requests,}\
%{default_toxenv}-ext-sqlalchemy,\
%{default_toxenv}-ext-sqlalchemy_core,\
%{default_toxenv}-ext-sqlite3\
    -- -- -v --asyncio-mode=auto ${ignore-} -k "${k-}"}


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
