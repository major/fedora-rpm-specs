# See eachdist.ini:
%global stable_version 1.18.0
%global prerel_version 0.39~b0
# WARNING: Because python-opentelemetry-contrib has some exact-version
# dependencies on subpackages of this package, it must be updated
# simultaneously with this package, preferably using a side tag, such that its
# stable_version and prerel_version always match those above.

# Contents of python3-opentelemetry-proto are generated from proto files in a
# separate repository with a separate version number. We treat these as
# generated sources: we aren’t required by the guidelines to re-generate them
# (although we *may*) but we must include the original sources.
#
# See PROTO_REPO_BRANCH_OR_COMMIT in scripts/proto_codegen.sh for the correct
# version number.
%global proto_version 0.17.0

# Unfortunately, we cannot disable the prerelease packages without breaking
# almost all of the stable packages, because opentelemetry-sdk depends on the
# prerelease package opentelementry-semantic-conventions.
%bcond prerelease 1

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

# The python-opencensus package was retired, so we cannot supply the
# python3-opentelemetry-opencensus-shim subpackage.
%bcond opencensus 0

Name:           python-opentelemetry
Version:        %{stable_version}
Release:        %autorelease
Summary:        OpenTelemetry Python API and SDK

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python
Source0:        %{url}/archive/v%{version}/opentelemetry-python-%{version}.tar.gz
# Note that we do not currently use this source, but it contains the original
# .proto files for python3-opentelemetry-proto, so we must include it.
%global proto_url https://github.com/open-telemetry/opentelemetry-proto
Source1:        %{proto_url}/archive/v%{proto_version}/opentelemetry-proto-%{proto_version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global stable_distinfo %(echo '%{stable_version}' | tr -d '~^').dist-info
# See eachdist.ini:
%global stable_pkgdirs %{shrink:
      opentelemetry-api
      opentelemetry-sdk
      opentelemetry-proto
      propagator/opentelemetry-propagator-jaeger
      propagator/opentelemetry-propagator-b3
      exporter/opentelemetry-exporter-zipkin-proto-http
      exporter/opentelemetry-exporter-zipkin-json
      exporter/opentelemetry-exporter-zipkin
      exporter/opentelemetry-exporter-prometheus
      exporter/opentelemetry-exporter-otlp
      exporter/opentelemetry-exporter-otlp-proto-common
      exporter/opentelemetry-exporter-otlp-proto-grpc
      exporter/opentelemetry-exporter-otlp-proto-http
      exporter/opentelemetry-exporter-jaeger-thrift
      exporter/opentelemetry-exporter-jaeger-proto-grpc
      exporter/opentelemetry-exporter-jaeger}
%global prerel_distinfo %(echo '%{prerel_version}' | tr -d '~^').dist-info
# See eachdist.ini:
%global prerel_pkgdirs %{shrink:
      tests/opentelemetry-test-utils
      exporter/opentelemetry-exporter-opencensus
      %{?with_opencensus:shim/opentelemetry-opencensus-shim}
      shim/opentelemetry-opentracing-shim
      opentelemetry-semantic-conventions}

%global common_description %{expand:
OpenTelemetry Python API and SDK.}

%description
%{common_description}


%package -n python3-opentelemetry-exporter-jaeger-proto-grpc
Summary:        Jaeger Protobuf Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

# All Jaeger exporters were deprecated upstream in 1.16.0/0.37b0.
Provides:       deprecated()

%description -n python3-opentelemetry-exporter-jaeger-proto-grpc
This library allows to export tracing data to Jaeger
(https://www.jaegertracing.io/).

Warning: Since v1.35, the Jaeger supports OTLP natively. Please use the OTLP
exporter instead. Upstream support for this exporter will end July 2023.


%package -n python3-opentelemetry-exporter-jaeger-thrift
Summary:        Jaeger Thrift Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

# All Jaeger exporters were deprecated upstream in 1.16.0/0.37b0.
Provides:       deprecated()

%description -n python3-opentelemetry-exporter-jaeger-thrift
This library allows to export tracing data to Jaeger
(https://www.jaegertracing.io/) using Thrift.

Warning: Since v1.35, the Jaeger supports OTLP natively. Please use the OTLP
exporter instead. Upstream support for this exporter will end July 2023.


%package -n python3-opentelemetry-exporter-jaeger
Summary:        Jaeger Exporters for OpenTelemetry
Version:        %{stable_version}

Obsoletes:      python3-opentelemetry-ext-jaeger < 1.0

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-exporter-jaeger-proto-grpc = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-jaeger-thrift = %{stable_version}-%{release}

# All Jaeger exporters were deprecated upstream in 1.16.0/0.37b0.
Provides:       deprecated()

%description -n python3-opentelemetry-exporter-jaeger
This library is provided as a convenience to install all supported Jaeger
Exporters. Currently it installs:
  • opentelemetry-exporter-jaeger-proto-grpc
  • opentelemetry-exporter-jaeger-thrift

To avoid unnecessary dependencies, users should install the specific package
once they’ve determined their preferred serialization method.

Warning: Since v1.35, the Jaeger supports OTLP natively. Please use the OTLP
exporter instead. Upstream support for this exporter will end July 2023.



%if %{with prerelease}
%package -n python3-opentelemetry-exporter-opencensus
Summary:        OpenCensus Exporter
Version:        %{prerel_version}

Obsoletes:      python3-opentelemetry-ext-opencensusexporter < 1.0

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-opencensus
This library allows to export traces using OpenCensus.
%endif


%package -n python3-opentelemetry-exporter-otlp-proto-common
Summary:        OpenTelemetry Protobuf Encoding
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-proto = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-otlp-proto-common
This library is provided as a convenience to encode to Protobuf. Currently used
by:

  • opentelemetry-exporter-otlp-proto-grpc
  • opentelemetry-exporter-otlp-proto-http


%package -n python3-opentelemetry-exporter-otlp-proto-grpc
Summary:        OpenTelemetry Collector Protobuf over gRPC Exporter
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}
Requires:       python3-opentelemetry-proto = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-otlp-proto-common = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-otlp-proto-grpc
This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over gRPC.


%package -n python3-opentelemetry-exporter-otlp-proto-http
Summary:        OpenTelemetry Collector Protobuf over HTTP Exporter
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}
Requires:       python3-opentelemetry-proto = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-otlp-proto-common = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-otlp-proto-http
This library allows to export data to the OpenTelemetry Collector using the
OpenTelemetry Protocol using Protobuf over HTTP.


%package -n python3-opentelemetry-exporter-otlp
Summary:        OpenTelemetry Collector Exporters
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-exporter-otlp-proto-grpc = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-otlp-proto-http = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-otlp
This library is provided as a convenience to install all supported
OpenTelemetry Collector Exporters. Currently it installs:

  • opentelemetry-exporter-otlp-proto-grpc
  • opentelemetry-exporter-otlp-proto-http

In the future, additional packages will be available:

  • opentelemetry-exporter-otlp-json-http

To avoid unnecessary dependencies, users should install the specific package
once they’ve determined their preferred serialization and protocol method.


%package -n python3-opentelemetry-exporter-prometheus
Summary:        OpenTelemetry Prometheus Exporter
Version:        %{prerel_version}

Obsoletes:      python3-opentelemetry-ext-prometheus < 1.0

Requires:       ((%{py3_dist prometheus_client} >= 0.5) with (%{py3_dist prometheus_client} < 1))
# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-prometheus
This library allows to export metrics data to Prometheus
(https://prometheus.io).


%package -n python3-opentelemetry-exporter-zipkin-json
Summary:        Zipkin Span JSON Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-zipkin-json
This library allows export of tracing data to Zipkin (https://zipkin.io/) using
JSON for serialization.


%package -n python3-opentelemetry-exporter-zipkin-proto-http
Summary:        Zipkin Span Protobuf Exporter for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-zipkin-json = %{stable_version}-%{release}

%description -n python3-opentelemetry-exporter-zipkin-proto-http
This library allows export of tracing data to Zipkin (https://zipkin.io/) using
Protobuf for serialization.


%package -n python3-opentelemetry-exporter-zipkin
Summary:        Zipkin Span Exporters for OpenTelemetry
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-exporter-zipkin-json = %{stable_version}-%{release}
Requires:       python3-opentelemetry-exporter-zipkin-proto-http = %{stable_version}-%{release}

Obsoletes:      python3-opentelemetry-ext-wsgi < 1.0

%description -n python3-opentelemetry-exporter-zipkin
This library is provided as a convenience to install all supported
OpenTelemetry Zipkin Exporters. Currently it installs:
  • opentelemetry-exporter-zipkin-json
  • opentelemetry-exporter-zipkin-proto-http

In the future, additional packages may be available:
  • opentelemetry-exporter-zipkin-thrift

To avoid unnecessary dependencies, users should install the specific package
once they've determined their preferred serialization method.


%package -n python3-opentelemetry-api
Summary:        OpenTelemetry Python API
Version:        %{stable_version}

# Note that the huge number of instrumentation packages are released in
# https://github.com/open-telemetry/opentelemetry-python-contrib and are
# packaged (where possible based on available dependencies) in
# https://src.fedoraproject.org/rpms/python-opentelemetry-contrib.
#
# The base opentelemetry-instrumentation package was also moved to “contrib” in
# release 1.6.1/0.25~b1. We therefore obsolete it…
Obsoletes:      python3-opentelemetry-instrumentation < 0.25~b1.1
# …and its pre-1.0 name…
Obsoletes:      python3-opentelemetry-auto-instrumentation < 1.0
# …and the pre-1.0 packages it was obsoleting. (Most of these are
# instrumentation extensions.)

# These have all been renamed and are now part of opentelemetry-python-contrib.
# They have a prerelease version number, which is less than the version number
# of the old packages, so obsoleting by version number alone is insufficient.
# It is fortunate, then, that they also have new names, and it is unlikely the
# old names will ever come back in any form.
#
# Any renamed pre-1.0 packages that remain in this repository are instead
# obsoleted by the corresponding new packages.

#   • opentelemetry-instrumentation-aiohttp-client
Obsoletes:      python3-opentelemetry-ext-aiohttp-client < 1.0
#   • opentelemetry-instrumentation-asgi
Obsoletes:      python3-opentelemetry-ext-asgi < 1.0
#   • opentelemetry-instrumentation-dbapi
Obsoletes:      python3-opentelemetry-ext-dbapi < 1.0
#   • opentelemetry-instrumentation-django
Obsoletes:      python3-opentelemetry-ext-django < 1.0
#   • opentelemetry-instrumentation-flask
Obsoletes:      python3-opentelemetry-ext-flask < 1.0
#   • opentelemetry-instrumentation-grpc
Obsoletes:      python3-opentelemetry-ext-grpc < 1.0
#   • opentelemetry-instrumentation-jinja2
Obsoletes:      python3-opentelemetry-ext-jinja2 < 1.0
#   • opentelemetry-instrumentation-mysql
Obsoletes:      python3-opentelemetry-ext-mysql < 1.0
#   • opentelemetry-instrumentation-psycopg2
Obsoletes:      python3-opentelemetry-ext-psycopg2 < 1.0
#   • opentelemetry-instrumentation-pymongo
Obsoletes:      python3-opentelemetry-ext-pymongo < 1.0
#   • opentelemetry-instrumentation-pymysql
Obsoletes:      python3-opentelemetry-ext-pymysql < 1.0
#   • opentelemetry-instrumentation-redis
Obsoletes:      python3-opentelemetry-ext-redis < 1.0
#   • opentelemetry-instrumentation-requests
Obsoletes:      python3-opentelemetry-ext-requests < 1.0
#   • opentelemetry-instrumentation-sqlalchemy
Obsoletes:      python3-opentelemetry-ext-sqlalchemy < 1.0
#   • opentelemetry-instrumentation-sqlite3
Obsoletes:      python3-opentelemetry-ext-sqlite3 < 1.0
#   • opentelemetry-instrumentation-wsgi
Obsoletes:      python3-opentelemetry-ext-wsgi < 1.0

#   • opentelemetry-exporter-datadog
Obsoletes:      python3-opentelemetry-ext-datadog < 1.0

# The opentelemetry-distro package was moved to “contrib” in release
# 1.6.1/0.25~b1.
Obsoletes:      python3-opentelemetry-distro < 0.25~b1.1
Obsoletes:      python3-opentelemetry-distro+otlp < 0.25~b1.1

%description -n python3-opentelemetry-api
%{summary}.


%package -n python3-opentelemetry-proto
Summary:        OpenTelemetry Python Proto
Version:        %{stable_version}

%description -n python3-opentelemetry-proto
%{summary}.


%package -n python3-opentelemetry-sdk
Summary:        OpenTelemetry Python SDK
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-semantic-conventions = %{prerel_version}-%{release}

%description -n python3-opentelemetry-sdk
%{summary}.


%if %{with prerelease}
%package -n python3-opentelemetry-semantic-conventions
Summary:        OpenTelemetry Python Semantic Conventions
Version:        %{prerel_version}

%description -n python3-opentelemetry-semantic-conventions
This library contains generated code for the semantic conventions defined by
the OpenTelemetry specification.
%endif


%package -n python3-opentelemetry-propagator-b3
Summary:        OpenTelemetry B3 Propagator
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}

%description -n python3-opentelemetry-propagator-b3
This library provides a propagator for the B3 format.


%package -n python3-opentelemetry-propagator-jaeger
Summary:        OpenTelemetry Jaeger Propagator
Version:        %{stable_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}

%description -n python3-opentelemetry-propagator-jaeger
This library provides a propagator for the Jaeger format.


%if %{with prerelease}
%if %{with opencensus}
%package -n python3-opentelemetry-opencensus-shim
Summary:        OpenCensus Shim for OpenTelemetry
Version:        %{prerel_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}

%description -n python3-opentelemetry-opencensus-shim
%{summary}.
%endif


%package -n python3-opentelemetry-opentracing-shim
Summary:        OpenTracing Shim for OpenTelemetry
Version:        %{prerel_version}

Obsoletes:      python3-opentelemetry-ext-opentracing-shim < 1.0

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}

%description -n python3-opentelemetry-opentracing-shim
%{summary}.
%endif


%if %{with prerelease}
%package -n python3-opentelemetry-test-utils
Summary:        OpenTracing Test Utilities
Version:        %{prerel_version}

# Dependencies across subpackages should be fully-versioned.
Requires:       python3-opentelemetry-api = %{stable_version}-%{release}
Requires:       python3-opentelemetry-sdk = %{stable_version}-%{release}

# Subpackage was renamed upstream
Obsoletes:      python3-opentelemetry-test < 0.26~b1-1

%description -n python3-opentelemetry-test-utils
This package provides internal testing utilities for the OpenTelemetry Python
project and provides no stability or quality guarantees. Please do not use it
for anything other than writing or running tests for the OpenTelemetry Python
project (github.com/open-telemetry/opentelemetry-python).
%endif


%package doc
Summary:        Documentation for python-opentelemetry
Version:        %{stable_version}

%description doc
This package provides documentation for python-opentelemetry.


%prep
%autosetup -n opentelemetry-python-%{stable_version}

# In “Pin googleapis-common-protos version”,
# https://github.com/open-telemetry/opentelemetry-python/pull/2777, upstream
# pinned “googleapis-common-protos ~= 1.52, < 1.56.3” to work around some test
# failures. However, we must deal with the system-wide versions of all
# dependencies, so we will have to skip any failing tests until and unless
# upstream is able to fix them properly.
sed -r -i 's/("googleapis-common-protos.*), <[^"]*/\1/' \
    exporter/opentelemetry-exporter-jaeger-proto-grpc/pyproject.toml
# In “Bug fix: detect and adapt to backoff package version”,
# https://github.com/open-telemetry/opentelemetry-python/pull/2980, upstream
# pinned test dependency “responses == 0.22.0”. While this matches the packaged
# version in Rawhide as of this writing, we won’t be able to respect this
# requirement in the long term, so we loosen it preemptively.
sed -r -i 's/(responses )== /\1>= /' \
    exporter/opentelemetry-exporter-otlp-proto-http/pyproject.toml
# In “Use importlib-metadata regardless of Python version (#3217)”,
# https://github.com/open-telemetry/opentelemetry-python/pull/3217, upstream
# pinned importlib-metadata ~= 6.0.0, which is very strict. We loosen it to
# allow at least the expected major version.  See:
# https://github.com/open-telemetry/opentelemetry-python/commit/6379c1cbe6432afaaac81f524a331a7819eaecc5#r105601318
sed -r -i 's/(importlib-metadata ~= 6\.0)\.0/\1/' \
    opentelemetry-api/pyproject.toml

%py3_shebang_fix .
# These are not installed with executable permissions, so shebangs are not
# useful:
thriftgen='exporter/opentelemetry-exporter-jaeger-thrift/src'
thriftgen="${thriftgen}/opentelemetry/exporter/jaeger/thrift/gen"
sed -r -i '1{/^#!/d}' \
    "${thriftgen}/agent/Agent-remote" \
    "${thriftgen}/jaeger/Collector-remote" \
    "${thriftgen}/zipkincore/ZipkinCollector-remote"

# Fix a test that shells out to the unversioned Python command. This is OK
# upstream, but not in Fedora.
sed -r -i 's|shutil\.which\("python"\)|"%{python3}"|' \
    opentelemetry-sdk/tests/trace/test_trace.py

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

(
  # - We do not use formatters/linters/type-checkers/coverage.
  #
  # - Similarly, we do not run the “spellcheck” tox environment, so we do not
  #   need codespell.
  #
  # - ddtrace is mentioned in a README but does not seem to actually be used
  #   anywhere
  # - we do not need sphinx_rtd_theme because we are not building the
  #   documentation as HTML
  # - we do not need sphinx-jekyll-builder because we will not build website
  #   docs
  # - now that instrumentation is moved to contrib, wrapt is no longer used
  #   directly; it is a dependency for some examples, and is in the intersphinx
  #   mapping, which we don’t use since the build is offline
  # - grpcio-tools is needed only if we run scripts/proto_codegen.sh
  # - httpretty does not seem to actually be used anywhere; it may be an
  #   optional dependency for output from some linter
  # - readme-renderer is needed only if we run
  #   scripts/check_for_valid_readme.py; this is also the reason for the
  #   version-pinned dependency on bleach, so we remove that too
  #
  # - we must allow Flask 2.x, as in opentelemetry-test-utils
  #
  # - we must allow Sphinx 3.6+ and 4.x
  # - we must allow sphinx-autodoc-typehints 1.17
  # - we must allow opentracing 2.3.x and 2.4.x
  # - we must allow protobuf 3.19.x; furthermore, we are not generating the
  #   bindings from the proto files, so we don’t have to respect the version
  #   specification in dev-requirements.txt, only the ones in individual
  #   packages
  #
  # - upstream pins markupsafe==2.0.1:
  #     temporary fix. we should update the jinja, flask deps
  #     See https://github.com/pallets/markupsafe/issues/282
  #     breaking change introduced in markupsafe causes jinja, flask to break
  #   but we have no such luxury
  # - we must allow pytest 7.2+ (upstream pins pytest==7.1.3)
  # - if we are not running the script to update the contrib repo SHA from
  #   branch, we do not need requests or ruamel.yaml; if we did need them, we
  #   would need to un-pin their versions; so we do both, unpinning and then
  #   removing
  #
  # - if we are not building the documentation, then we should ignore
  #   documentation dependencies duplicated in dev-requirements.txt
  # - if we are not building the documentation, we do not need Django
  sed -r \
      -e '/\b(black|flake8|isort|mypy|mypy-protobuf|pylint|pytest-cov)\b/d' \
      -e '/\b(codespell)\b/d' \
      -e '/\b(ddtrace|sphinx-(rtd-theme|jekyll-builder)|wrapt)\b/d' \
      -e '/\b(grpcio-tools|httpretty|readme-renderer|bleach)\b/d' \
      -e 's/\b(flask~=)1\.[[:digit:]]\b/\12\.0/' \
      -e 's/\b(sphinx(-autodoc-typehints)?|opentracing)~=/\1>=/' \
      -e 's/\b(protobuf)[>~]=.*/\1/' \
      -e 's/\b(markupsafe|pytest|requests|ruamel\.yaml)==.*/\1/' \
      -e '/\b(requests|ruamel\.yaml)\b/d' \
      %{?!with_doc_pdf:-e '/\b(sphinx|django)\b/d'} \
      dev-requirements.txt %{?with_doc_pdf:docs-requirements.txt}

  # We can’t easily use %%pyproject_buildrequires -t to read tox.ini, since
  # it’s not associated with a particular package in the source archive, but we
  # can read out the relevant dependencies and dump them into the requirements
  # file for processing.
  '%{python3}' -c '
from configparser import ConfigParser

toxfile = "tox.ini"
cfg = ConfigParser()
if toxfile not in cfg.read(toxfile):
    raise SystemExit(f"Could not load {toxfile}")
for dep in cfg.get("testenv", "deps").splitlines():
    parts = dep.rstrip("\r\n").split(None, 2)
    if not parts or parts[0].startswith("-"):
        continue
    elif not parts[0].endswith(":"):
        raise ValueError(f"Confusing dependency: {dep!r}")
    command = parts[0][:-1]
    dep = parts[1]
    if any(what in command for what in ("cov", "mypy", "proto4")):
        continue
    print(dep)
' ) | sed -r -e '/^#/d' -e '/^(.*\/)?opentelemetry-/d' | sort -u |
  tee requirements-filtered.txt

# Loosen any dependency versions that are pinned too tightly in subpackages.
# The find-then-modify pattern keeps us from discarding mtimes on sources that
# do not need modification.
#
# - we must allow opentracing 2.3.x and 2.4.x
for dep in 'opentracing'
do
  find . -type f -name 'pyproject.toml' -exec gawk \
      "/${dep}[[:blank:]]*~=/ { print FILENAME; nextfile }" '{}' '+' |
    xargs -r -t sed -r -i "s/\b(${DEP}[[:blank:]]*)~=/\\1>=/"
done


%generate_buildrequires
# We filter generated BR’s to avoid listing those that are provided by packages
# built in this spec file. For easier inspection, we also reorder and
# de-duplicate them.
(
  # Consolidated from dev-requirements.txt and docs-requirements.txt in %%prep,
  # with quite a bit of well-justified filtering and adjusting. We will tack it
  # onto each %%pyproject_buildrequires call.
  reqs="${PWD}/requirements-filtered.txt"

  for pkgdir in %{?with_prerelease:%{prerel_pkgdirs}} %{stable_pkgdirs}
  do
    pushd "${pkgdir}" >/dev/null
    if [[ "${pkgdir}" = 'exporter/opentelemetry-exporter-otlp' ]]
    then
      # No “test” extra:
      %pyproject_buildrequires
    else
      # Typical subpackage:
      %pyproject_buildrequires -x test "${reqs}"
    fi
    popd >/dev/null
  done
) | grep -vE '\bopentelemetry-' | sort -u


%build
for pkgdir in %{?with_prerelease:%{prerel_pkgdirs}} %{stable_pkgdirs}
do
  pushd "${pkgdir}"
  %pyproject_wheel
  popd
done

# Build documentation
%if %{with doc_pdf}
PYTHONPATH="${PWD}/build/lib" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install


%check
for pkgdir in %{?with_prerelease:%{prerel_pkgdirs}} %{stable_pkgdirs}
do
  # Note we do not attempt to run tests for opentelemetry-test-utils, i.e.
  # tests/opentelemetry-test-utils; there are none in practice, and pytest would
  # indicate failure.
  if [[ "${pkgdir}" = 'tests/opentelemetry-test-utils' ]]
  then
    continue
  fi
  unset k
  case "${pkgdir}" in
  opentelemetry-api)
    # This is some kind of metadata issue with
    # pkg_resources.iter_entry_points(). It is probably specific to the RPM
    # build environment. The entry points are found just fine if we set
    # PYTHONPATH='%%{buildroot}%%{python3_sitelib}' and run a Python snippet
    # like:
    #   from pkg_resources import iter_entry_points
    #   print(list(iter_entry_points("opentelemetry_propagator", "tracecontext")))
    # without using pytest.
    #
    # _ ERROR collecting opentelemetry-api/tests/propagators/test_global_httptextformat.py _
    # opentelemetry-api/tests/propagators/test_global_httptextformat.py:20: in <module>
    #     from opentelemetry.propagate import extract, inject
    # ../../BUILDROOT/python-opentelemetry-1.13.0-2.fc38.x86_64/usr/lib/python3.11/site-packages/opentelemetry/propagate/__init__.py:136: in <module>
    #     next(  # type: ignore
    # E   StopIteration
    echo "Skipping tests for ${pkgdir}; see spec file comments." 1>&2
    continue
    ;;
  opentelemetry-sdk)
    # Still more entry point issues
    k="${k-}${k+ and }not (TestGlobals and test_sdk_log_emitter_provider)"
    k="${k-}${k+ and }not (TestGlobals and test_sdk_logger_provider)"
    k="${k-}${k+ and }not (TestImportExporters and test_console_exporters)"
    k="${k-}${k+ and }not (TestLoggingInit and test_initialize_components_resource)"
    k="${k-}${k+ and }not (TestLoggingInit and test_logging_init_disable_default)"
    k="${k-}${k+ and }not (TestLoggingInit and test_logging_init_enable_env)"
    # Test failure in opentelemetry-sdk on Python 3.12
    # https://github.com/open-telemetry/opentelemetry-python/issues/3370
    k="${k-}${k+ and }not (TestLoggingHandler and test_log_record_user_attributes)"
    ;;
  esac

  %pytest "${pkgdir}" ${ignore-} -k "${k-}"
done


%files -n python3-opentelemetry-exporter-jaeger-proto-grpc
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-jaeger-proto-grpc/LICENSE
%doc exporter/opentelemetry-exporter-jaeger-proto-grpc/README.rst
%doc exporter/opentelemetry-exporter-jaeger-proto-grpc/examples

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/
%dir %{python3_sitelib}/opentelemetry/exporter/jaeger/
%{python3_sitelib}/opentelemetry/exporter/jaeger/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/jaeger/proto/

%{python3_sitelib}/opentelemetry/exporter/jaeger/proto/grpc/
%{python3_sitelib}/opentelemetry_exporter_jaeger_proto_grpc-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-jaeger-thrift
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-jaeger-thrift/LICENSE
%doc exporter/opentelemetry-exporter-jaeger-thrift/README.rst
%doc exporter/opentelemetry-exporter-jaeger-thrift/examples/

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/
%dir %{python3_sitelib}/opentelemetry/exporter/jaeger/
%{python3_sitelib}/opentelemetry/exporter/jaeger/py.typed

%{python3_sitelib}/opentelemetry/exporter/jaeger/thrift/
%{python3_sitelib}/opentelemetry_exporter_jaeger_thrift-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-jaeger
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-jaeger/LICENSE
%doc exporter/opentelemetry-exporter-jaeger/README.rst

# Shared namespace directories are already (co)-owned by the implementation
# subpackages (-proto-grpc, -thrift) upon which this subpackage depends.

%dir %{python3_sitelib}/opentelemetry/exporter/jaeger/__pycache__/
%pycached %{python3_sitelib}/opentelemetry/exporter/jaeger/version.py
%{python3_sitelib}/opentelemetry_exporter_jaeger-%{stable_distinfo}/


%if %{with prerelease}
%files -n python3-opentelemetry-exporter-opencensus
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-opencensus/LICENSE
%doc exporter/opentelemetry-exporter-opencensus/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/

%{python3_sitelib}/opentelemetry/exporter/opencensus/
%{python3_sitelib}/opentelemetry_exporter_opencensus-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-exporter-otlp-proto-common
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-otlp-proto-common/LICENSE
%doc exporter/opentelemetry-exporter-otlp-proto-common/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/
%{python3_sitelib}/opentelemetry/exporter/otlp/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/proto/

%{python3_sitelib}/opentelemetry/exporter/otlp/proto/common/
%{python3_sitelib}/opentelemetry_exporter_otlp_proto_common-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-otlp-proto-grpc
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-otlp-proto-grpc/LICENSE
%doc exporter/opentelemetry-exporter-otlp-proto-grpc/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/
%{python3_sitelib}/opentelemetry/exporter/otlp/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/proto/

%{python3_sitelib}/opentelemetry/exporter/otlp/proto/grpc/
%{python3_sitelib}/opentelemetry_exporter_otlp_proto_grpc-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-otlp-proto-http
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-otlp-proto-http/LICENSE
%doc exporter/opentelemetry-exporter-otlp-proto-http/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/
%dir %{python3_sitelib}/opentelemetry/exporter/otlp/proto/
%{python3_sitelib}/opentelemetry/exporter/otlp/py.typed

%{python3_sitelib}/opentelemetry/exporter/otlp/proto/http/
%{python3_sitelib}/opentelemetry_exporter_otlp_proto_http-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-otlp
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-otlp/LICENSE
%doc exporter/opentelemetry-exporter-otlp/README.rst

# Shared namespace directories are already (co)-owned by the implementation
# subpackages (-proto-grpc, -proto-http) upon which this subpackage depends.

%dir %{python3_sitelib}/opentelemetry/exporter/otlp/__pycache__/
%pycached %{python3_sitelib}/opentelemetry/exporter/otlp/version.py
%{python3_sitelib}/opentelemetry_exporter_otlp-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-prometheus
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-prometheus/LICENSE
%doc exporter/opentelemetry-exporter-prometheus/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/

%{python3_sitelib}/opentelemetry/exporter/prometheus/
%{python3_sitelib}/opentelemetry_exporter_prometheus-%{prerel_distinfo}/


%files -n python3-opentelemetry-exporter-zipkin-json
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-zipkin-json/LICENSE
# Not packaged since it is a zero-length file:
#doc exporter/opentelemetry-exporter-zipkin-json/CHANGELOG.md
%doc exporter/opentelemetry-exporter-zipkin-json/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/
%dir %{python3_sitelib}/opentelemetry/exporter/zipkin/
%{python3_sitelib}/opentelemetry/exporter/zipkin/py.typed

%{python3_sitelib}/opentelemetry/exporter/zipkin/encoder/
%{python3_sitelib}/opentelemetry/exporter/zipkin/json/
%pycached %{python3_sitelib}/opentelemetry/exporter/zipkin/node_endpoint.py
%{python3_sitelib}/opentelemetry_exporter_zipkin_json-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-zipkin-proto-http
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-zipkin-proto-http/LICENSE
# Not packaged since it is a zero-length file:
#doc exporter/opentelemetry-exporter-zipkin-proto-http/CHANGELOG.md
%doc exporter/opentelemetry-exporter-zipkin-proto-http/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/
%dir %{python3_sitelib}/opentelemetry/exporter/zipkin/
%{python3_sitelib}/opentelemetry/exporter/zipkin/py.typed
%dir %{python3_sitelib}/opentelemetry/exporter/zipkin/proto/

%{python3_sitelib}/opentelemetry/exporter/zipkin/proto/http/
%{python3_sitelib}/opentelemetry_exporter_zipkin_proto_http-%{stable_distinfo}/


%files -n python3-opentelemetry-exporter-zipkin
# Note that the contents are identical to the top-level LICENSE file.
%license exporter/opentelemetry-exporter-zipkin/LICENSE
%doc exporter/opentelemetry-exporter-zipkin/README.rst

# Shared namespace directories are already (co)-owned by the implementation
# subpackages (-json, -proto-http) upon which this subpackage depends.

%dir %{python3_sitelib}/opentelemetry/exporter/zipkin/__pycache__/
%pycached %{python3_sitelib}/opentelemetry/exporter/zipkin/version.py
%{python3_sitelib}/opentelemetry_exporter_zipkin-%{stable_distinfo}/


%files -n python3-opentelemetry-api
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-api/LICENSE
%doc opentelemetry-api/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/propagators/

%{python3_sitelib}/opentelemetry/_logs/
%{python3_sitelib}/opentelemetry/attributes/
%{python3_sitelib}/opentelemetry/baggage/
%{python3_sitelib}/opentelemetry/context/
%{python3_sitelib}/opentelemetry/metrics/
%{python3_sitelib}/opentelemetry/propagate/
%dir %{python3_sitelib}/opentelemetry/propagators/__pycache__/
%pycached %{python3_sitelib}/opentelemetry/propagators/composite.py
%pycached %{python3_sitelib}/opentelemetry/propagators/textmap.py
%{python3_sitelib}/opentelemetry/trace/
%{python3_sitelib}/opentelemetry/util/
%dir %{python3_sitelib}/opentelemetry/__pycache__/
%pycached %{python3_sitelib}/opentelemetry/environment_variables.py
%pycached %{python3_sitelib}/opentelemetry/version.py
%{python3_sitelib}/opentelemetry_api-%{stable_distinfo}/


%files -n python3-opentelemetry-proto
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-proto/LICENSE
%doc opentelemetry-proto/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/proto/
%{python3_sitelib}/opentelemetry_proto-%{stable_distinfo}/


%files -n python3-opentelemetry-sdk
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-sdk/LICENSE
%doc opentelemetry-sdk/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/sdk/
%{python3_sitelib}/opentelemetry_sdk-%{stable_distinfo}/


%if %{with prerelease}
%files -n python3-opentelemetry-semantic-conventions
# Note that the contents are identical to the top-level LICENSE file.
%license opentelemetry-sdk/LICENSE
%doc opentelemetry-sdk/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/semconv/
%{python3_sitelib}/opentelemetry_semantic_conventions-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-propagator-b3
# Note that the contents are identical to the top-level LICENSE file.
%license propagator/opentelemetry-propagator-b3/LICENSE
%doc propagator/opentelemetry-propagator-b3/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/propagators/

%{python3_sitelib}/opentelemetry/propagators/b3/
%{python3_sitelib}/opentelemetry_propagator_b3-%{stable_distinfo}/


%files -n python3-opentelemetry-propagator-jaeger
# Note that the contents are identical to the top-level LICENSE file.
%license propagator/opentelemetry-propagator-jaeger/LICENSE
%doc propagator/opentelemetry-propagator-jaeger/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/propagators/

%{python3_sitelib}/opentelemetry/propagators/jaeger/
%{python3_sitelib}/opentelemetry_propagator_jaeger-%{stable_distinfo}/


%if %{with prerelease}
%if %{with opencensus}
%files -n python3-opentelemetry-opencensus-shim
# Note that the contents are identical to the top-level LICENSE file.
%license shim/opentelemetry-opencensus-shim/LICENSE
%doc shim/opentelemetry-opencensus-shim/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/shim/

%{python3_sitelib}/opentelemetry/shim/opencensus_shim/
%{python3_sitelib}/opentelemetry_opencensus_shim-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-opentracing-shim
# Note that the contents are identical to the top-level LICENSE file.
%license shim/opentelemetry-opentracing-shim/LICENSE
%doc shim/opentelemetry-opentracing-shim/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed
%dir %{python3_sitelib}/opentelemetry/shim/

%{python3_sitelib}/opentelemetry/shim/opentracing_shim/
%{python3_sitelib}/opentelemetry_opentracing_shim-%{prerel_distinfo}/
%endif


%if %{with prerelease}
%files -n python3-opentelemetry-test-utils
%license LICENSE
%doc tests/opentelemetry-test-utils/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/
%{python3_sitelib}/opentelemetry/py.typed

%{python3_sitelib}/opentelemetry/test/
%{python3_sitelib}/opentelemetry_test_utils-%{prerel_distinfo}/
%endif


%files doc
%license LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc rationale.md
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/opentelemetrypython.pdf
%endif


%changelog
%autochangelog
