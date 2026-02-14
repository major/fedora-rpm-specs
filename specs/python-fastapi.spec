# Breaks a circular dependency on fastapi-cli by omitting it from fastapi’s
# “standard”, “standard-no-fastapi-cloud-cli”, and “all” extras.
%bcond bootstrap 0

%bcond orjson 1
# Not yet packaged: https://pypi.org/project/pwdlib/
# (Used for a few tests.)
%bcond pwdlib 0
# Not yet packaged: https://pypi.org/project/PyJWT/
# (Only has very limited use in the tests.)
%bcond pyjwt 0
# Python 3.14 / Pydantic 3.12 / PEP 649 compat. issues; orphaned for F43
%bcond sqlmodel %[ %{without bootstrap} && 0 ]
# Not yet packaged: https://pypi.org/project/strawberry-graphql/
# (Only needed for integration examples in the documentation.)
%bcond strawberry_graphql 0
%bcond uvicorn 1

Name:           python-fastapi
Version:        0.129.0
Release:        %autorelease
Summary:        FastAPI framework

# SPDX
License:        MIT
URL:            https://github.com/fastapi/fastapi
Source:         %{url}/archive/%{version}/fastapi-%{version}.tar.gz

# Written for Fedora in groff_man(7) format based on --help output
Source10:       fastapi.1
Source11:       fastapi-dev.1
Source12:       fastapi-run.1
Source13:       fastapi-deploy.1
Source14:       fastapi-login.1

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x standard,standard-no-fastapi-cloud-cli,all
BuildOption(install):   -l fastapi

BuildArch:      noarch

# Downstream-only: run test_fastapi_cli without coverage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-run-test_fastapi_cli-without-coverag.patch

BuildRequires:  python3-devel

# Since dependency groups contain overly-strict version bounds and some
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# we just list the test dependencies we *do* want manually rather than trying
# to patch pyproject.toml. We preserve upstream’s lower bounds but remove upper
# bounds, as we must try to make do with what we have.
#
# docs-tests:
BuildRequires:  %{py3_dist httpx} >= 0.23
# (we don’t actually need ruff)
# tests:
BuildRequires:  %{py3_dist anyio[trio]} >= 3.2.1
BuildRequires:  %{py3_dist dirty-equals} >= 0.9
BuildRequires:  %{py3_dist flask} >= 1.1.2
BuildRequires:  %{py3_dist inline-snapshot} >= 0.21.1
%if %{with pwdlib}
BuildRequires:  %{py3_dist pwdlib[argon2]} >= 0.2.1
%endif
%if %{with pyjwt}
BuildRequires:  %{py3_dist pyjwt} >= 2.9
%endif
BuildRequires:  %{py3_dist pytest} >= 7.1.3
BuildRequires:  %{py3_dist pyyaml} >= 5.3.1
%if %{with sqlmodel}
BuildRequires:  %{py3_dist sqlmodel} >= 0.0.31
%endif
%if %{with strawberry_graphql}
BuildRequires:  %{py3_dist strawberry-graphql} >= 0.200
%endif
BuildRequires:  %{py3_dist a2wsgi} >= 1.9
# This is still needed in the tests even if we do not have sqlmodel to bring it
# in as an indirect dependency.
BuildRequires:  %{py3_dist sqlalchemy}

%global common_description %{expand:
FastAPI is a modern, fast (high-performance), web framework for building APIs
with Python based on standard Python type hints.

The key features are:

  • Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette
    and Pydantic). One of the fastest Python frameworks available.
  • Fast to code: Increase the speed to develop features by about 200% to
    300%. *
  • Fewer bugs: Reduce about 40% of human (developer) induced errors. *
  • Intuitive: Great editor support. Completion everywhere. Less time
    debugging.
  • Easy: Designed to be easy to use and learn. Less time reading docs.
  • Short: Minimize code duplication. Multiple features from each parameter
    declaration. Fewer bugs.
  • Robust: Get production-ready code. With automatic interactive
    documentation.
  • Standards-based: Based on (and fully compatible with) the open standards
    for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

* estimation based on tests on an internal development team, building
  production applications.}

%description %{common_description}


%package -n     python3-fastapi
Summary:        %{summary}

%if %{defined fc44} || %{defined fc45} || %{defined fc46}
# Removed in F44 after upstream deprecated fastapi-slim
Obsoletes:      python3-fastapi-slim < 0.128.8
%endif

%description -n python3-fastapi %{common_description}


%if %{defined fc44} || %{defined fc45} || %{defined fc46}
# We don’t use “%%pyproject_extras_subpkg -n python3-fastapi …” because we want
# to Obsolete the corresponding fastapi-slim extras.

%package -n python3-fastapi+standard
Summary: Metapackage for python3-fastapi: standard extras
Requires: python3-fastapi = %{version}-%{release}
Obsoletes: python3-fastapi-slim+standard < 0.128.8
%description -n python3-fastapi+standard
This is a metapackage bringing in standard extras requires for python3-fastapi.
It makes sure the dependencies are installed.

%files -n python3-fastapi+standard
%ghost %dir %{python3_sitelib}/*.dist-info

%package -n python3-fastapi+standard-no-fastapi-cloud-cli
Summary: Metapackage for python3-fastapi: standard-no-fastapi-cloud-cli extras
Requires: python3-fastapi = %{version}-%{release}
Obsoletes: python3-fastapi-slim+standard-no-fastapi-cloud-cli < 0.128.8
%description -n python3-fastapi+standard-no-fastapi-cloud-cli
This is a metapackage bringing in standard-no-fastapi-cloud-cli extras requires
for python3-fastapi. It makes sure the dependencies are installed.

%files -n python3-fastapi+standard-no-fastapi-cloud-cli
%ghost %dir %{python3_sitelib}/*.dist-info

%package -n python3-fastapi+all
Summary: Metapackage for python3-fastapi: all extras
Requires: python3-fastapi = %{version}-%{release}
Obsoletes: python3-fastapi-slim+all < 0.128.8
%description -n python3-fastapi+all
This is a metapackage bringing in all extras requires for python3-fastapi.
It makes sure the dependencies are installed.

%files -n python3-fastapi+all
%ghost %dir %{python3_sitelib}/*.dist-info
%else
%pyproject_extras_subpkg -n python3-fastapi standard standard-no-fastapi-cloud-cli all
%endif


%prep -a
%if %{with bootstrap}
# Break a dependency cycle with fastapi-cli by commenting out all dependencies
# on it. Note that this removes it from the “standard”,
# “standard-no-fastapi-cloud-cli”, and “all” extras metapackages.
sed -r -i 's/("fastapi-cli?\b.*",)/# \1/' pyproject.toml
%endif
%if %{without orjson}
# Comment out all dependencies on orjson (for ORJSONResponse). Note that this
# removes it from the “all” extra metapackage.
sed -r -i 's/("orjson\b.*",)/# \1/' pyproject.toml
%endif
%if %{without uvicorn}
# Comment out all dependencies on uvicorn. Note that this removes it from the
# “all” extra metapackage.
sed -r -i 's/("uvicorn\b.*",)/# \1/' pyproject.toml
%endif

# Remove bundled js-termynal 0.0.1; since we are not building documentation, we
# do this very bluntly:
rm -rvf docs/*/docs/js docs/*/docs/css


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}' '%{SOURCE14}'

%if %{without bootstrap}
install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/fastapi' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/fastapi'
'%{buildroot}%{_bindir}/fastapi' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_fastapi'
'%{buildroot}%{_bindir}/fastapi' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/fastapi.fish'
%endif


%check -a
%if %{with bootstrap}
ignore="${ignore-} --ignore=tests/test_fastapi_cli.py"
%endif

%if %{without orjson}
k="${k-}${k+ and }not test_orjson_non_str_keys"
ignore="${ignore-} --ignore=tests/test_default_response_class.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_custom_response/test_tutorial001.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_custom_response/test_tutorial001b.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_custom_response/test_tutorial009c.py"
%endif

%if %{without pyjwt}
ignore="${ignore-} --ignore=tests/test_tutorial/test_security/test_tutorial004.py"
ignore="${ignore-} --ignore=tests/test_tutorial/test_security/test_tutorial005.py"
%endif

%if %{without sqlmodel}
ignore="${ignore-} --ignore-glob=tests/test_tutorial/test_sql_databases/*"
%endif

%if %{without strawberry_graphql}
ignore="${ignore-} --ignore=tests/test_tutorial/test_graphql/test_tutorial001.py"
%endif

# We aren’t interested in running tests for the development scripts, and doing
# so has some PYTHONPATH issues (ModuleNotFoundError: No module named
# 'scripts') in this environment.
ignore="${ignore-} --ignore-glob=scripts/tests/*"

# Ignore all DeprecationWarning messages, as they pop up from various
# dependencies in practice. Upstream deals with this by tightly controlling
# dependency versions in CI.
warningsfilter="${warningsfilter-} -W ignore::DeprecationWarning"

%pytest ${warningsfilter-} -k "${k-}" ${ignore-}


%files -n python3-fastapi -f %{pyproject_files}
%doc CITATION.cff
%doc README.md

%{_bindir}/fastapi
%{_mandir}/man1/fastapi.1*
%{_mandir}/man1/fastapi-*.1*
%if %{without bootstrap}
%{bash_completions_dir}/fastapi
%{zsh_completions_dir}/_fastapi
%{fish_completions_dir}/fastapi.fish
%endif


%changelog
%autochangelog
