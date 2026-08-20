# To break dependency loops, including:
#   - httpx2 → starlette → httpx
#   - httpx2 → uvicorn → a2wsgi → starlette → httpx2
# … we disable tests when bootstrapping a new Python version.
%bcond bootstrap 0
%bcond tests %{without bootstrap}

Name:           python-httpx2
Version:        2.12.0
Release:        %autorelease
Summary:        A next-generation HTTP client for Python

# Note: httpx2 and httpcore2 are developed together in one uv workspace in the
# same git repository. They are released synchronously with the same version
# numbers, and they share a test suite. Therefore, this source RPM produces
# both python3-httpx2 and python3-httpcore2.

# The entire source is BSD-3-Clause, except:
#
# MIT:
#   - src/httpx2/httpx2/websockets/ (httpx2.websockets), derived from httpx-ws
#   - src/httpx2/httpx2/_sse.py (httpx2._sse), derived from httpx-sse
#
# Since these are only in the python3-httpx2 subpackage (not python3-httpcore2
# or any of the extras metapackages), we only include the MIT term in that
# subpackage’s License field and in SourceLicense.
License:        BSD-3-Clause
SourceLicense:  %{license} AND MIT
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
BuildRequires:  %{py3_dist starlette}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist trustme}
BuildRequires:  %{py3_dist uvicorn}
BuildRequires:  %{py3_dist websockets}
BuildRequires:  %{py3_dist werkzeug}
%endif

%global common_description %{expand:
HTTPX2 is a fully featured HTTP client library for Python. It includes an
integrated command line client, has support for both HTTP/1.1 and HTTP/2, and
provides both sync and async APIs.}

%description %{common_description}


%package -n python3-httpx2
Summary:        %{summary}
# See notes above the base package’s License field.
License:       %{license} AND MIT

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-httpcore2 = %{version}-%{release}

# A version of httpx-ws was vendored into httpx2 as httpx2.websockets in
# https://github.com/pydantic/httpx2/pull/1042. It was rebased on httpx-ws
# 0.9.0 in https://github.com/pydantic/httpx2/pull/1067.
#
# Mandatory upstream unbundling query, per
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#bundling:
# https://github.com/pydantic/httpx2/pull/1042#issuecomment-5087946615
# (Upstream confirmed there is no path to using an external dependency.)
Provides:       bundled(python3dist(httpx-ws)) = 0.9
# Similarly for httpx-sse, which was vendored as httpx2._sse in
# https://github.com/pydantic/httpx2/pull/1046. We believe that this was based
# on the latest release of httpx-sse at the time, 0.4.3.
Provides:       bundled(python3dist(httpx-sse)) = 0.4.3

%description -n python3-httpx2 %{common_description}


%{pyproject_extras_subpkg -n python3-httpx2 --dist-name httpx2 %{shrink:
    brotli http2 socks ws zstd}}

# Ship the command-line tool in the cli extras package (which would otherwise
# be a metapackage), since the extra is required for the tool to function.
%pyproject_extras_subpkg -n python3-httpx2 --dist-name httpx2 cli
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


%{pyproject_extras_subpkg -n python3-httpcore2 --dist-name httpcore2 %{shrink:
    http2 socks trio asyncio}}


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

# Temporarily permit an older uv-dynamic-versioning. This dependency was
# updated by dependabot in https://github.com/pydantic/httpx2/pull/1103, but it
# doesn’t seem anything from the newer version is really required. We can drop
# this after python-uv-dynamic-versioning is updated to at least 0.14.0,
# https://src.fedoraproject.org/rpms/python-uv-dynamic-versioning/pull-request/1,
# https://bugzilla.redhat.com/show_bug.cgi?id=2513025.
%pyproject_patch_dependency uv-dynamic-versioning:set_lower:0.12.0

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
    --extras brotli,cli,http2,socks,ws,zstd
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
%pyproject_save_files --assert-license --dist-name httpcore2 httpcore2
%pyproject_save_files --assert-license --dist-name httpx2 httpx2

install --directory '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man \
    --no-discard-stderr \
    --no-info \
    --name='A next-generation HTTP client for Python' \
    --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/httpx2.1' \
    httpx2


%check
%pyproject_check_import --dist-name httpcore2
%pyproject_check_import --dist-name httpx2

%if %{with tests}
# We are not interested in running the benchmarks.
ignore="${ignore-} --ignore=tests/test_benchmark.py"
ignore="${ignore-} --ignore=tests/test_benchmark_memory.py"

%pytest -m 'not network' -rs --verbose ${ignore-}
%endif


%files -n python3-httpcore2 -f %{pyproject_files --dist-name httpcore2}
%doc src/httpcore2/CHANGELOG.md
%doc src/httpcore2/README.md


%files -n python3-httpx2 -f %{pyproject_files --dist-name httpx2}
%doc src/httpx2/CHANGELOG.md
%doc README.md


%changelog
%autochangelog
