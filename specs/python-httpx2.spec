# To break a dependency loop between httpx2 -> uvicorn -> a2wsgi -> starlette -> httpx2,
# we disable tests when bootstrapping new Python version.
%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-httpx2
Version:        2.5.0
Release:        %autorelease
Summary:        A next-generation HTTP client for Python

# Note: httpx2 and httpcore2 are developed together in one uv workspace in the
# same git repository. They are released synchronously with the same version
# numbers, and they share a test suite. Therefore, this source RPM produces
# both python3-httpx2 and python3-httpcore2.

License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
Source:         %{url}/archive/v%{version}/httpx2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  tomcli

%if %{with tests}
# Test dependencies; see the part of the workspace’s “dev” dependency group
# after the “Tests” comment. It’s possible to generate dependencies from this
# group, like:
#   %%pyproject_buildrequires --no-use-build-system --dependency-groups dev
# However, the dependency group isn’t usable as-is.
#   - It contains test, linting, and packaging dependencies, with only comments
#     indicating which is which. We *could* ask upstream to split these out
#     into separate dependency groups.
#   - Even the test dependencies still include benchmarking and
#     coverage-analysis dependencies that we would need to patch out. We
#     *could* use %%pyproject_patch_dependency for this, or ask upstream for
#     even more fine-grained dependency groups.
#   - Almost all of the dependencies are pinned to exact versions. This is the
#     real deal-breaker; by the time we patch out all of the version pins, it’s
#     just as easy to list the dependencies manually.
BuildRequires:  %{py3_dist chardet}
BuildRequires:  %{py3_dist cryptography}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-httpbin}
BuildRequires:  %{py3_dist pytest-trio}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist trustme}
BuildRequires:  %{py3_dist uvicorn}
BuildRequires:  %{py3_dist werkzeug}
%endif

%global common_description %{expand:
HTTPX2 is a fully featured HTTP client library for Python. It includes an
integrated command line client, has support for both HTTP/1.1 and HTTP/2, and
provides both sync and async APIs.}

%description %{common_description}


%package -n python3-httpx2
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-httpcore2 = %{version}-%{release}

%description -n python3-httpx2 %{common_description}


# TODO: Avoid the -i option once better multi-package support is available,
# https://src.fedoraproject.org/rpms/pyproject-rpm-macros/pull-request/612
%{pyproject_extras_subpkg %{shrink:
    -i %{python3_sitelib}/httpx2-%{version}.dist-info
    -n python3-httpx2
    brotli http2 socks zstd
    }}

# Ship the command-line tool in the cli extras package (which would otherwise
# be a metapackage), since the extra is required for the tool to function.
%{pyproject_extras_subpkg %{shrink:
    -i %{python3_sitelib}/httpx2-%{version}.dist-info
    -n python3-httpx2
    cli
    }}
%{_bindir}/httpx2
%{_mandir}/man1/httpx2.1*


%package -n python3-httpcore2
Summary:        A minimal low-level HTTP client

%description -n python3-httpcore2
The HTTP Core package provides a minimal low-level HTTP client, which does one
thing only. Sending HTTP requests.

It does not provide any high level model abstractions over the API, does not
handle redirects, multipart uploads, building authentication headers,
transparent HTTP caching, URL parsing, session cookie handling, content or
charset decoding, handling JSON, environment based configuration defaults, or
any of that Jazz.


# TODO: Avoid the -i option once better multi-package support is available,
# https://src.fedoraproject.org/rpms/pyproject-rpm-macros/pull-request/612
%{pyproject_extras_subpkg %{shrink:
    -i %{python3_sitelib}/httpcore2-%{version}.dist-info
    -n python3-httpcore2
    http2 socks trio asyncio
    }}


%prep
%autosetup -p1 -C

# This is too strict for downstream packaging, since warnings may bubble up
# from any dependency. Upstream has strictly pinned test dependency versions.
tomcli set pyproject.toml lists delitem \
    tool.pytest.ini_options.filterwarnings error

# Since uv-dynamic-versioning does not support an environment variable override
# similar to SETUPTOOLS_SCM_PRETEND_VERSION, the simplest thing we can do is to
# set the fallback-version in each pyproject.toml. The alternative would be to
# add a BuildRequires on git-core, BuildOption(prep): -S git, and then make a
# git tag named v%%{version} in %%prep. The following is simpler and
# lighter-weight, especially since we already depend on tomcli anyway.
tomcli set src/httpcore2/pyproject.toml str \
    tool.uv-dynamic-versioning.fallback-version '%{version}'
tomcli set src/httpx2/pyproject.toml str \
    tool.uv-dynamic-versioning.fallback-version '%{version}'

# Do not generate BuildRequires on workspace packages.
%pyproject_patch_dependency httpcore2:ignore:br_only
%pyproject_patch_dependency httpx2:ignore:br_only

# Imitate the effect of the [tool.hatch.build.targets.sdist.force-include]
# section in src/httpx2/pyproject.toml on upstream’s release process, ensuring
# that these files appear in wheels; particularly, this ensures that LICENSE.md
# appears in the dist-info metadata for the httpx2 package.
cp --preserve --update=none-fail README.md LICENSE.md src/httpx2/


%generate_buildrequires
%{pyproject_buildrequires %{shrink:
    --directory src/httpx2
    --extras brotli,cli,http2,socks,zstd
    }}
%{pyproject_buildrequires %{shrink:
    --directory src/httpcore2
    --extras http2,socks,trio,asyncio
    }}


%build
%pyproject_wheel --directory src/httpcore2
%pyproject_wheel --directory src/httpx2


%install
%pyproject_install
# TODO: Use %%pyproject_save_files and %%{pyproject_files} once better
# multi-package support is available,
# https://src.fedoraproject.org/rpms/pyproject-rpm-macros/pull-request/612

install --directory '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man \
    --no-discard-stderr \
    --no-info \
    --name='A next-generation HTTP client for Python' \
    --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/httpx2.1' \
    httpx2


%check
# TODO: Use %%pyproject_check_import once better multi-package support is available,
# https://src.fedoraproject.org/rpms/pyproject-rpm-macros/pull-request/612
%py3_check_import httpx2 httpcore2
%if %{with tests}
%pytest -m 'not network' -rs --verbose --ignore=tests/test_benchmark.py
%endif


%files -n python3-httpcore2
# This results in a harmless “file listed twice” warning from fedora-review; we
# can easily avoid this once better multi-package support is available,
# https://src.fedoraproject.org/rpms/pyproject-rpm-macros/pull-request/612
%license %{python3_sitelib}/httpcore2-%{version}.dist-info/licenses/LICENSE.md

%doc src/httpcore2/CHANGELOG.md
%doc src/httpcore2/README.md

%{python3_sitelib}/httpcore2/
%{python3_sitelib}/httpcore2-%{version}.dist-info/


%files -n python3-httpx2
# This results in a harmless “file listed twice” warning from fedora-review; we
# can easily avoid this once better multi-package support is available,
# https://src.fedoraproject.org/rpms/pyproject-rpm-macros/pull-request/612
%license %{python3_sitelib}/httpx2-%{version}.dist-info/licenses/LICENSE.md

%doc src/httpx2/CHANGELOG.md
%doc README.md

%{python3_sitelib}/httpx2/
%{python3_sitelib}/httpx2-%{version}.dist-info/


%changelog
%autochangelog
