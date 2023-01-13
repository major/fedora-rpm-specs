# Older versions of subpackages that are disabled in these conditionals are
# Obsoleted in python3-opentelemetry-contrib-instrumentations; if changing or
# removing a conditional, be sure that those are updated as needed.

# A subpackage needs aio_pika ~= 7.2.0; python-aio-pika is not packaged
%bcond_with aio_pika

# A subpackage needs aiopg >=0.13.0,<1.3.0; F38 has 1.3.4
%bcond_with aiopg

# A subpackage needs confluent-kafka >= 1.8.2, < 2.0.0; F38 has 1.6.1
%bcond_with confluent_kafka

# Some tests need elasticsearch-dsl; python-elasticsearch-dsl is not packaged
%bcond_with elasticsearch_dsl

# A subpackage needs falcon >= 1.4.1, < 4.0.0; F38 has 4.0.0
%bcond_with falcon

# Some tests need moto ~= 2.0; but python-moto is not packaged
%bcond_with moto

# A subpackage needs protobuf ~= 4.21; F38 has 3.19.6
%bcond_with protobuf4

# A subpackage needs remoulade >= 0.50; python-remoulade is not packaged
%bcond_with remoulade

# A subpackage needs scikit-learn ~= 0.24.0; F38 has 1.1.2
%bcond_with sklearn

# A subpackage needs starlette ~= 0.13.0; F38 has 0.22.0
%bcond_with starlette

# A subpackage needs tortoise-orm >= 0.17.0; python-tortoise-orm is not
# packaged
%bcond_with tortoise_orm

# Some tests need werkzeug == 0.16.1, or at least < 2.2.0; F38 has 2.2.2
#
# We unpinned the werkzeug version in the pyramid instrumentation test
# dependencies (it was pinned to == 0.16.1), but it’s not immediately obvious
# how to update the tests to work with current versions of werkzeug.
#
# The class werkzeug.wrappers.BaseResponse was deprecated in 2.1.0
# (https://github.com/pallets/werkzeug/issues/1963) and removed in 2.2.0
# (https://github.com/pallets/werkzeug/pull/2276).
%bcond_with werkzeug

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-opentelemetry-contrib
# See eachdist.ini. Note that this package must have the same version as the
# ”prerel_version” (pre-release version) in the python-opentelemetry package,
# and the two packages. Currently, nothing in this package follows the
# OpenTelemetry “stable_version”, so the entire package is versioned with the
# beta/pre-release version,
%global prerel_version 0.36~b0
# …except a few subpackages that have their OWN versioning scheme:
%global aws_propagator_version 1.0.1
%global aws_sdk_version 2.0.1
Version:        %{prerel_version}
Release:        %autorelease
Summary:        OpenTelemetry instrumentation for Python modules

# Until we get clarification from upstream,
#   Applicability of BSD-3-Clause license?
#   https://github.com/open-telemetry/opentelemetry-python-contrib/issues/1531
# we assume that any of the files in the repository may contain code under
# LICENSE.BSD3, which is BSD-3-Clause, except for packages that carry their own
# LICENSE files.
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib
%global srcversion %(echo '%{prerel_version}' | tr -d '~^')
Source0:        %{url}/archive/v%{srcversion}/opentelemetry-python-contrib-%{srcversion}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       opentelemetry-bootstrap.1
Source11:       opentelemetry-instrument.1

BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# While this package is noarch, excluding i686 unblocks many dependent packages
# (some of which have already removed i686 support).
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

%global prerel_distinfo %(echo '%{prerel_version}' | tr -d '~^').dist-info
%global pkgdirs %{shrink:
    %{?with_protobuf4:exporter/opentelemetry-exporter-prometheus-remote-write}
    exporter/opentelemetry-exporter-richconsole
    opentelemetry-instrumentation
    opentelemetry-distro
    propagator/opentelemetry-propagator-aws-xray
    propagator/opentelemetry-propagator-ot-trace
    sdk-extension/opentelemetry-sdk-extension-aws
    util/opentelemetry-util-http
    instrumentation/opentelemetry-instrumentation-aiohttp-client
    %{?with_aiopg:instrumentation/opentelemetry-instrumentation-aiopg}
    %{?with_aio_pika:instrumentation/opentelemetry-instrumentation-aio-pika}
    instrumentation/opentelemetry-instrumentation-asgi
    instrumentation/opentelemetry-instrumentation-asyncpg
    instrumentation/opentelemetry-instrumentation-aws-lambda
    instrumentation/opentelemetry-instrumentation-boto
    instrumentation/opentelemetry-instrumentation-boto3sqs
    instrumentation/opentelemetry-instrumentation-botocore
    instrumentation/opentelemetry-instrumentation-celery
    %{?with_confluent_kafka:instrumentation/opentelemetry-instrumentation-confluent-kafka}
    instrumentation/opentelemetry-instrumentation-dbapi
    instrumentation/opentelemetry-instrumentation-django
    instrumentation/opentelemetry-instrumentation-elasticsearch
    %{?with_falcon:instrumentation/opentelemetry-instrumentation-falcon}
    instrumentation/opentelemetry-instrumentation-fastapi
    instrumentation/opentelemetry-instrumentation-flask
    instrumentation/opentelemetry-instrumentation-grpc
    instrumentation/opentelemetry-instrumentation-httpx
    instrumentation/opentelemetry-instrumentation-jinja2
    instrumentation/opentelemetry-instrumentation-kafka-python
    instrumentation/opentelemetry-instrumentation-logging
    instrumentation/opentelemetry-instrumentation-mysql
    instrumentation/opentelemetry-instrumentation-pika
    instrumentation/opentelemetry-instrumentation-psycopg2
    instrumentation/opentelemetry-instrumentation-pymemcache
    instrumentation/opentelemetry-instrumentation-pymongo
    instrumentation/opentelemetry-instrumentation-pymysql
    instrumentation/opentelemetry-instrumentation-pyramid
    instrumentation/opentelemetry-instrumentation-redis
    %{?with_remoulade:instrumentation/opentelemetry-instrumentation-remoulade}
    instrumentation/opentelemetry-instrumentation-requests
    %{?with_sklearn:instrumentation/opentelemetry-instrumentation-sklearn}
    instrumentation/opentelemetry-instrumentation-sqlalchemy
    instrumentation/opentelemetry-instrumentation-sqlite3
    %{?with_starlette:instrumentation/opentelemetry-instrumentation-starlette}
    instrumentation/opentelemetry-instrumentation-system-metrics
    instrumentation/opentelemetry-instrumentation-tornado
    %{?with_tortoise_orm:instrumentation/opentelemetry-instrumentation-tortoiseorm}
    instrumentation/opentelemetry-instrumentation-urllib
    instrumentation/opentelemetry-instrumentation-urllib3
    instrumentation/opentelemetry-instrumentation-wsgi
    opentelemetry-contrib-instrumentations
    %{nil}}

%description
OpenTelemetry instrumentation for Python modules.


%package doc
Summary:        Documentation for OpenTelemetry Python Contrib packages
Version:        %{prerel_version}

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description doc
This package provides documentation for OpenTelemetry Python Contrib packages.


%if %{with protobuf4}
%package -n python3-opentelemetry-exporter-prometheus-remote-write
Summary:        Prometheus Remote Write Metrics Exporter for OpenTelemetry
Version:        %{prerel_version}

%description -n python3-opentelemetry-exporter-prometheus-remote-write
This package contains an exporter to send metrics from the OpenTelemetry Python
SDK directly to a Prometheus Remote Write integrated backend (such as Cortex or
Thanos) without having to run an instance of the Prometheus server.
%endif


%package -n python3-opentelemetry-exporter-richconsole
Summary:        Rich Console Exporter for OpenTelemetry
Version:        %{prerel_version}

%description -n python3-opentelemetry-exporter-richconsole
This library is a console exporter using the Rich tree view. When used with a
batch span processor, the rich console exporter will show the trace as a tree
and all related spans as children within the tree, including properties.


%package -n python3-opentelemetry-instrumentation
Summary:        Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python
Version:        %{prerel_version}
License:        Apache-2.0

# From python-opentelemetry:
BuildRequires:  python3dist(opentelemetry-test-utils)
Recommends:     python3-opentelemetry-distro = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation
This package provides a couple of commands that help automatically instruments
a program.


%package -n python3-opentelemetry-distro
Summary:        OpenTelemetry Python Distro
Version:        %{prerel_version}

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-distro
This package provides entrypoints to configure OpenTelemetry.

%pyproject_extras_subpkg -n python3-opentelemetry-distro -i %{python3_sitelib}/opentelemetry_distro-%{prerel_distinfo} otlp


%package -n python3-opentelemetry-propagator-aws-xray
Summary:        AWS X-Ray Propagator for OpenTelemetry
Version:        %{aws_propagator_version}
License:        Apache-2.0

# Test dependency (covered upstream by dependencies in
# opentelemetry-instrumentation-fastapi and
# opentelemetry-exporter-prometheus-remote-write).
BuildRequires:  python3dist(requests)

%description -n python3-opentelemetry-propagator-aws-xray
This library provides the propagator necessary to inject or extract a tracing
context across AWS services.


%package -n python3-opentelemetry-propagator-ot-trace
Summary:        OT Trace Propagator for OpenTelemetry
Version:        %{prerel_version}

%description -n python3-opentelemetry-propagator-ot-trace
OpenTelemetry OT Trace Propagator.


%package -n python3-opentelemetry-sdk-extension-aws
Summary:        AWS SDK extension for OpenTelemetry
Version:        %{aws_sdk_version}
License:        Apache-2.0

%description -n python3-opentelemetry-sdk-extension-aws
This library provides components necessary to configure the OpenTelemetry SDK
for tracing with AWS X-Ray.


%package -n python3-opentelemetry-util-http
Summary:        Web util for OpenTelemetry
Version:        %{prerel_version}

%description -n python3-opentelemetry-util-http
This library provides ASGI, WSGI middleware and other HTTP-related
functionality that is common to instrumented web frameworks (such as Django,
Starlette, FastAPI, etc.) to track requests timing through OpenTelemetry.


%package -n python3-opentelemetry-instrumentation-aiohttp-client
Summary:        OpenTelemetry aiohttp client instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-aiohttp-client
This library allows tracing HTTP requests made by the aiohttp client library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-aiohttp-client -i %{python3_sitelib}/opentelemetry_instrumentation_aiohttp_client-%{prerel_distinfo} instruments


%if %{with aiopg}
%package -n python3-opentelemetry-instrumentation-aiopg
Summary:        OpenTelemetry aiopg instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-dbapi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-aiopg
OpenTelemetry aiopg instrumentation.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-aiopg -i %{python3_sitelib}/opentelemetry_instrumentation_aiopg-%{prerel_distinfo} instruments
%endif


%if %{with aio_pika}
%package -n python3-opentelemetry-instrumentation-aio-pika
Summary:        OpenTelemetry Aio-pika instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

%description -n python3-opentelemetry-instrumentation-aio-pika
This library allows tracing requests made by the Aio-pika library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-aio-pika -i %{python3_sitelib}/opentelemetry_instrumentation_aio_pika-%{prerel_distinfo} instruments
%endif


%package -n python3-opentelemetry-instrumentation-asgi
Summary:        ASGI instrumentation for OpenTelemetry
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-asgi
This library provides a ASGI middleware that can be used on any ASGI framework
(such as Django, Starlette, FastAPI or Quart) to track requests timing through
OpenTelemetry.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-asgi -i %{python3_sitelib}/opentelemetry_instrumentation_asgi-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-asyncpg
Summary:        OpenTelemetry instrumentation for AsyncPG
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-asyncpg
This library allows tracing PostgreSQL queries made by the asyncpg library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-asyncpg -i %{python3_sitelib}/opentelemetry_instrumentation_asyncpg-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-aws-lambda
Summary:        OpenTelemetry AWS Lambda instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-propagator-aws-xray = %{?epoch:%{epoch}:}%{aws_propagator_version}-%{release}

%description -n python3-opentelemetry-instrumentation-aws-lambda
This library provides an Instrumentor used to trace requests made by the Lambda
functions on the AWS Lambda service.

It also provides scripts used by AWS Lambda Layers to automatically initialize
the OpenTelemetry SDK. Learn more on the AWS Distro for OpenTelemetry (ADOT)
documentation for the Python Lambda Layer.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-aws-lambda -i %{python3_sitelib}/opentelemetry_instrumentation_aws_lambda-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-boto
Summary:        OpenTelemetry Boto instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-boto
This library allows tracing requests made by the Boto library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-boto -i %{python3_sitelib}/opentelemetry_instrumentation_boto-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-boto3sqs
Summary:        Boto3 SQS service tracing for OpenTelemetry
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-boto3sqs
This library allows tracing requests made by the Boto3 library to the SQS
service.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-boto3sqs -i %{python3_sitelib}/opentelemetry_instrumentation_boto3sqs-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-botocore
Summary:        OpenTelemetry Botocore instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-botocore
This library allows tracing requests made by the Botocore library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-botocore -i %{python3_sitelib}/opentelemetry_instrumentation_botocore-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-celery
Summary:        OpenTelemetry Celery Instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-celery
Instrumentation for Celery.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-celery -i %{python3_sitelib}/opentelemetry_instrumentation_celery-%{prerel_distinfo} instruments


%if %{with confluent_kafka}
%package -n python3-opentelemetry-instrumentation-confluent-kafka
Summary:        OpenTelemetry Confluent Kafka instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-confluent-kafka
This library allows tracing requests made by the confluent-kafka library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-confluent-kafka -i %{python3_sitelib}/opentelemetry_instrumentation_confluent_kafka-%{prerel_distinfo} instruments
%endif


%package -n python3-opentelemetry-instrumentation-dbapi
Summary:        OpenTelemetry Database API instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-dbapi
OpenTelemetry Database API instrumentation.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-dbapi -i %{python3_sitelib}/opentelemetry_instrumentation_dbapi-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-django
Summary:        OpenTelemetry Instrumentation for Django
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-wsgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-django
This library allows tracing requests for Django applications.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-django -i %{python3_sitelib}/opentelemetry_instrumentation_django-%{prerel_distinfo} instruments asgi


%package -n python3-opentelemetry-instrumentation-elasticsearch
Summary:        OpenTelemetry elasticsearch instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-elasticsearch
This library allows tracing elasticsearch made by the elasticsearch library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-elasticsearch -i %{python3_sitelib}/opentelemetry_instrumentation_elasticsearch-%{prerel_distinfo} instruments


%if %{with falcon}
%package -n python3-opentelemetry-instrumentation-falcon
Summary:        Falcon instrumentation for OpenTelemetry
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-wsgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-falcon
This library builds on the OpenTelemetry WSGI middleware to track web requests
in Falcon applications.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-falcon -i %{python3_sitelib}/opentelemetry_instrumentation_falcon-%{prerel_distinfo} instruments
%endif


%package -n python3-opentelemetry-instrumentation-fastapi
Summary:        OpenTelemetry FastAPI Instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-asgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-fastapi
This library provides automatic and manual instrumentation of FastAPI web
frameworks, instrumenting http requests served by applications utilizing the
framework.

auto-instrumentation using the opentelemetry-instrumentation package is also
supported.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-fastapi -i %{python3_sitelib}/opentelemetry_instrumentation_fastapi-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-flask
Summary:        Flask instrumentation for OpenTelemetry
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-wsgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-flask
This library builds on the OpenTelemetry WSGI middleware to track web requests
in Flask applications.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-flask -i %{python3_sitelib}/opentelemetry_instrumentation_flask-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-grpc
Summary:        OpenTelemetry gRPC instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-grpc
Client and server interceptors for gRPC Python.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-grpc -i %{python3_sitelib}/opentelemetry_instrumentation_grpc-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-httpx
Summary:        OpenTelemetry HTTPX Instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# This is in the top-level tox.ini, but only for an environment specific to a
# version of httpx that we don’t have.
BuildRequires:  python3dist(respx)

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-httpx
This library allows tracing HTTP requests made by the httpx library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-httpx -i %{python3_sitelib}/opentelemetry_instrumentation_httpx-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-jinja2
Summary:        OpenTelemetry jinja2 instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-jinja2
OpenTelemetry jinja2 integration.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-jinja2 -i %{python3_sitelib}/opentelemetry_instrumentation_jinja2-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-kafka-python
Summary:        OpenTelemetry Kafka-Python instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-kafka-python
OpenTelemetry kafka-python integration

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-kafka-python -i %{python3_sitelib}/opentelemetry_instrumentation_kafka_python-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-logging
Summary:        OpenTelemetry Logging instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-logging
OpenTelemetry logging integration.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-logging -i %{python3_sitelib}/opentelemetry_instrumentation_logging-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-mysql
Summary:        OpenTelemetry MySQL instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-dbapi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-mysql
Instrumentation with MySQL that supports the mysql-connector library and is
specified to trace_integration using ‘MySQL’.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-mysql -i %{python3_sitelib}/opentelemetry_instrumentation_mysql-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-pika
Summary:        OpenTelemetry pika instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

%description -n python3-opentelemetry-instrumentation-pika
This library allows tracing requests made by the pika library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-pika -i %{python3_sitelib}/opentelemetry_instrumentation_pika-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-psycopg2
Summary:        OpenTelemetry psycopg2 instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-dbapi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-psycopg2
OpenTelemetry Psycopg Instrumentation.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-psycopg2 -i %{python3_sitelib}/opentelemetry_instrumentation_psycopg2-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-pymemcache
Summary:        OpenTelemetry pymemcache instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-pymemcache
OpenTelemetry pymemcache Instrumentation

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-pymemcache -i %{python3_sitelib}/opentelemetry_instrumentation_pymemcache-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-pymongo
Summary:        OpenTelemetry pymongo instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-pymongo
OpenTelemetry pymongo Instrumentation

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-pymongo -i %{python3_sitelib}/opentelemetry_instrumentation_pymongo-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-pymysql
Summary:        OpenTelemetry PyMySQL instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-dbapi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-pymysql
OpenTelemetry PyMySQL Instrumentation

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-pymysql -i %{python3_sitelib}/opentelemetry_instrumentation_pymysql-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-pyramid
Summary:        OpenTelemetry Pyramid instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-wsgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-pyramid
OpenTelemetry Pyramid Instrumentation

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-pyramid -i %{python3_sitelib}/opentelemetry_instrumentation_pyramid-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-redis
Summary:        OpenTelemetry Redis instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-redis
This library allows tracing requests made by the Redis library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-redis -i %{python3_sitelib}/opentelemetry_instrumentation_redis-%{prerel_distinfo} instruments


%if %{with remoulade}
%package -n python3-opentelemetry-instrumentation-remoulade
Summary:        OpenTelemetry Remoulade instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-remoulade
This library allows tracing requests made by the Remoulade library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-remoulade -i %{python3_sitelib}/opentelemetry_instrumentation_remoulade-%{prerel_distinfo} instruments
%endif


%package -n python3-opentelemetry-instrumentation-requests
Summary:        OpenTelemetry requests instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-requests
This library allows tracing HTTP requests made by the requests library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-requests -i %{python3_sitelib}/opentelemetry_instrumentation_requests-%{prerel_distinfo} instruments


%if %{with sklearn}
%package -n python3-opentelemetry-instrumentation-sklearn
Summary:        OpenTelemetry sklearn instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-sklearn
This library allows tracing HTTP requests made by the scikit-learn library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-sklearn -i %{python3_sitelib}/opentelemetry_instrumentation_sklearn-%{prerel_distinfo} instruments
%endif


%package -n python3-opentelemetry-instrumentation-sqlalchemy
Summary:        OpenTelemetry SQLAlchemy instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# This is needed on s390x only, but it doesn’t hurt to have it on the other
# architectures.
BuildRequires:  python3dist(greenlet)

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-sqlalchemy
This library allows tracing requests made by the SQLAlchemy library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-sqlalchemy -i %{python3_sitelib}/opentelemetry_instrumentation_sqlalchemy-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-sqlite3
Summary:        OpenTelemetry SQLite3 instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-dbapi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-sqlite3
OpenTelemetry SQLite3 Instrumentation.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-sqlite3 -i %{python3_sitelib}/opentelemetry_instrumentation_sqlite3-%{prerel_distinfo} instruments


%if %{with starlette}
%package -n python3-opentelemetry-instrumentation-starlette
Summary:        OpenTelemetry Starlette Instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-asgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-starlette
This library provides automatic and manual instrumentation of Starlette web
frameworks, instrumenting http requests served by applications utilizing the
framework.

Auto-instrumentation using the opentelemetry-instrumentation package is also
supported.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-starlette -i %{python3_sitelib}/opentelemetry_instrumentation_starlette-%{prerel_distinfo} instruments
%endif


%package -n python3-opentelemetry-instrumentation-system-metrics
Summary:        OpenTelemetry System Metrics Instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

%description -n python3-opentelemetry-instrumentation-system-metrics
Instrumentation to collect system performance metrics.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-system-metrics -i %{python3_sitelib}/opentelemetry_instrumentation_system_metrics-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-tornado
Summary:        Tornado instrumentation for OpenTelemetry
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-tornado
This library builds on the OpenTelemetry WSGI middleware to track web requests
in Tornado applications.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-tornado -i %{python3_sitelib}/opentelemetry_instrumentation_tornado-%{prerel_distinfo} instruments


%if %{with tortoise_orm}
%package -n python3-opentelemetry-instrumentation-tortoiseorm
Summary:        OpenTelemetry Instrumentation for Tortoise ORM
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-tortoiseorm
This library allows tracing queries made by tortoise ORM backends, mysql,
postgres and sqlite.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-tortoiseorm -i %{python3_sitelib}/opentelemetry_instrumentation_tortoiseorm-%{prerel_distinfo} instruments
%endif


%package -n python3-opentelemetry-instrumentation-urllib
Summary:        OpenTelemetry urllib instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-urllib
This library allows tracing HTTP requests made by the urllib library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-urllib -i %{python3_sitelib}/opentelemetry_instrumentation_urllib-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-urllib3
Summary:        OpenTelemetry urllib3 instrumentation
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-urllib3
This library allows tracing HTTP requests made by the urllib3 library.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-urllib3 -i %{python3_sitelib}/opentelemetry_instrumentation_urllib3-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-instrumentation-wsgi
Summary:        WSGI Middleware for OpenTelemetry
Version:        %{prerel_version}
License:        Apache-2.0

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
Requires:       python3-opentelemetry-instrumentation = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-util-http = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-instrumentation-wsgi
This library provides a WSGI middleware that can be used on any WSGI framework
(such as Django / Flask) to track requests timing through OpenTelemetry.

%pyproject_extras_subpkg -n python3-opentelemetry-instrumentation-wsgi -i %{python3_sitelib}/opentelemetry_instrumentation_wsgi-%{prerel_distinfo} instruments


%package -n python3-opentelemetry-contrib-instrumentations
Summary:        OpenTelemetry Contrib Instrumentation Packages
Version:        %{prerel_version}
License:        Apache-2.0

# Removed upstream:
# https://github.com/open-telemetry/opentelemetry-python-contrib/pull/1366
Obsoletes:      python3-opentelemetry-exporter-datadog < 0.36~b0-1
Obsoletes:      python3-opentelemetry-exporter-datadog+instruments < 0.36~b0-1

# Ensure we have fully-versioned dependencies (to release) across subpackages
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_requiring_base_package
%if %{with aio_pika}
Requires:       python3-opentelemetry-instrumentation-aio-pika = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-aio-pika < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-aio-pika+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-aiohttp-client = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%if %{with aiopg}
Requires:       python3-opentelemetry-instrumentation-aiopg = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-aiopg < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-aiopg+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-asgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-asyncpg = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-aws-lambda = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-boto = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-boto3sqs = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-botocore = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-celery = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%if %{with confluent_kafka}
Requires:       python3-opentelemetry-instrumentation-confluent-kafka = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-confluent-kafka < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-confluent-kafka+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-dbapi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-django = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-elasticsearch = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%if %{with falcon}
Requires:       python3-opentelemetry-instrumentation-falcon = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-falcon < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-falcon+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-fastapi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-flask = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-grpc = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-httpx = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-jinja2 = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-kafka-python = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-logging = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-mysql = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-pika = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-psycopg2 = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-pymemcache = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-pymongo = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-pymysql = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-pyramid = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-redis = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%if %{with remoulade}
Requires:       python3-opentelemetry-instrumentation-remoulade = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-remoulade < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-remoulade+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-requests = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%if %{with sklearn}
Requires:       python3-opentelemetry-instrumentation-sklearn = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-sklearn < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-sklearn+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-sqlalchemy = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-sqlite3 = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%if %{with starlette}
Requires:       python3-opentelemetry-instrumentation-starlette = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-starlette < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-starlette+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-system-metrics = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-tornado = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%if %{with tortoise_orm}
Requires:       python3-opentelemetry-instrumentation-tortoiseorm = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
%else
Obsoletes:      python3-opentelemetry-instrumentation-tortoiseorm < 0.36~b0-1
Obsoletes:      python3-opentelemetry-instrumentation-tortoiseorm+instruments < 0.36~b0-1
%endif
Requires:       python3-opentelemetry-instrumentation-urllib = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-urllib3 = %{?epoch:%{epoch}:}%{prerel_version}-%{release}
Requires:       python3-opentelemetry-instrumentation-wsgi = %{?epoch:%{epoch}:}%{prerel_version}-%{release}

%description -n python3-opentelemetry-contrib-instrumentations
This package installs all instrumentation packages hosted by the OpenTelemetry
Python Contrib repository, except those with dependency version requirements
that could not be satisfied.


%prep
%autosetup -n opentelemetry-python-contrib-%{srcversion}

# Un-pin importlib-metadata test dependency; see:
#   Pin importlib-metadata version for celery test
#   https://github.com/open-telemetry/opentelemetry-python-contrib/pull/1374
sed -r -i 's/("importlib-metadata)[[:blank:]]*==[^"]+/\1/' \
    instrumentation/opentelemetry-instrumentation-celery/pyproject.toml

# Un-pin test dependencies that were pinned to exact versions but perhaps
# habitually rather than for some concrete reason.
#
# https://github.com/open-telemetry/opentelemetry-python-contrib/pull/1277
sed -r -i 's/("parameterized)[[:blank:]]*==[^"]+/\1/' \
    instrumentation/opentelemetry-instrumentation-falcon/pyproject.toml
# https://github.com/open-telemetry/opentelemetry-python-contrib/pull/1291
# Unpinning is not good enough; see the werkzeug build conditonal
sed -r -i 's/("werkzeug)[[:blank:]]*==[^"]+/\1/' \
    instrumentation/opentelemetry-instrumentation-pyramid/pyproject.toml

# Some tests, and the dev requirements, pin markupsafe==2.0.1. See:
#
#   Fixing build failures
#   https://github.com/open-telemetry/opentelemetry-python-contrib/pull/928
#     temporary fix. we should update the jinja, flask deps
#     See https://github.com/pallets/markupsafe/issues/282
#     breaking change introduced in markupsafe causes jinja, flask to break
#
# We can’t respect this, but we also don’t need to because we have
# appropriately updated versions of jinja and flask too.
#
# The find-then-modify pattern keeps us from discarding mtimes on any sources
# that do not need modification.
find . -type f \( -name '*.txt' -o -name '*.toml' \) -exec \
    gawk '/markupsafe[[:blank:]]*==/ { print FILENAME }' '{}' '+' |
  xargs -r -t sed -r -i 's/(markupsafe[[:blank:]]*)==/\1>=/'

# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find */src */*/src -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

# The python3-opentelemetry-contrib-instrumentations subpackage will depend on
# *all* instrumentation subpackages; patch out the dependencies on those that
# we were not able to build due to dependency issues.
for omit in \
    %{?!with_aiopg:aiopg} \
    %{?!with_aio_pika:aio-pika} \
    %{?!with_confluent_kafka:confluent-kafka} \
    %{?!with_falcon:falcon} \
    %{?!with_remoulade:remoulade} \
    %{?!with_sklearn:sklearn} \
    %{?!with_starlette:starlette} \
    %{?!with_tortoise_orm:tortoiseorm} \
    %{nil}
do
  sed -r -i \
      "s/^([[:blank:]]*)(\"opentelemetry-instrumentation-${omit}==)/\1# \2/" \
      opentelemetry-contrib-instrumentations/pyproject.toml
done

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

(
  # - We do not use formatters/linters/type-checkers/coverage.
  #
  # - Similarly, we do not run the “spellcheck” tox environment, so we do not
  #   need codespell.
  # - readme-renderer is needed only if we run
  #   scripts/check_for_valid_readme.py; this is also the reason for the
  #   version-pinned dependency on bleach, so we remove that too
  #
  # - we do not need any of the sphinx packages because we are not building the
  #   documentation
  # - grpcio-tools is not needed since we are not generating any proto bindings
  sed -r \
      -e '/\b(black|flake8|isort|mypy|mypy-protobuf|pylint|pytest-cov)\b/d' \
      -e '/\b(codespell|readme-renderer|bleach)\b/d' \
      -e '/\b(sphinx)/d' \
      -e '/\b(grpcio-tools)\b/d' \
      dev-requirements.txt | tee dev-requirements-prefiltered.txt

%if %{with doc_pdf}
  awk '
      /^[[:blank:]]*$/ { suppress = 0; print; next }
      # Un-pin indirect dependencies, especially those of our subpackages;
      # the versions of these will just end up overspecified.
      /^#[[:blank:]]+Required by ((opentelemetry-)?instrumentation)/ {
        suppress = 1
      }
      /^#[[:blank:]]+[Ii]ndirect/ { suppress = 1 }
      suppress { next }
      # No URIs, no relative paths
      /^(-e|\.\/)/ { next }
      {
        # Unpin exact-version dependencies, converting them to lower bounds
        sub(/==/, ">=")
        # Loosen the bound on sphinx-rtd-theme
        sub(/sphinx-rtd-theme~=/, "sphinx-rtd-theme>=")
        print
      }' docs-requirements.txt | tee docs-requirements-prefiltered.txt
%endif

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
    # Exclude coverage, linters, typecheckers, etc.
    excludes = {"coverage", "mypy"}
    # dev-requirements.txt handles pytest, and we do not want pytest-benchmark
    excludes.add("test")
    # We cannot test obsolete or future versions
    excludes.update({"django1", "django2", "django4"})
    excludes.update({"elasticsearch2", "elasticsearch5", "elasticsearch6"})
    excludes.update({"falcon1", "falcon2", "falcon3"})
    excludes.add("sqlalchemy11")
    excludes.add("pika0")
    excludes.update({"pymemcache135", "pymemcache200", "pymemcache300"})
    excludes.update({"pymemcache342"})
    excludes.update({"httpx18", "httpx21"})
    if any(what in command for what in excludes):
        continue
    print(dep)
' | tee tox-requirements-prefiltered.txt) |
  sed -r -e '/^#/d' |
  sort -u |
  tee all-requirements-filtered.txt


%generate_buildrequires
# We filter generated BR’s to avoid listing those that are provided by packages
# built in this spec file. For easier inspection, we also reorder and
# de-duplicate them.
(
  # Consolidated from dev-requirements.txt and tox.ini in %%prep, with quite a
  # bit of well-justified filtering and adjusting. We will tack it onto each
  # %%pyproject_buildrequires call.
  reqs="${PWD}/all-requirements-filtered.txt"

  for pkgdir in %{pkgdirs}
  do
    pushd "${pkgdir}" >/dev/null
    extras='test'
    if echo "${pkgdir}" | grep -E '^instrumentation/' >/dev/null
    then
      extras="${extras},instruments"
    fi
    case "${pkgdir}" in
%if %{without moto}
    instrumentation/opentelemetry-instrumentation-boto|instrumentation/opentelemetry-instrumentation-botocore)
      # Can’t run the tests
      extras='instruments'
      ;;
    instrumentation/opentelemetry-instrumentation-django)
      extras="${extras},asgi"
      ;;
%endif
%if %{without elasticsearch_dsl}
    instrumentation/opentelemetry-instrumentation-elasticsearch)
      # Can’t run the tests
      extras='instruments'
      ;;
%endif
%if %{without werkzeug}
    instrumentation/opentelemetry-instrumentation-pyramid)
      # Can’t run the tests
      extras='instruments'
      ;;
%endif
    esac
    %pyproject_buildrequires -x "${extras}" "${reqs}"
    popd >/dev/null
  done
) | sed -r \
    -e '/\bopentelemetry-instrumentation\b/d' \
    -e '/\bopentelemetry-propagator-aws-xray\b/d' \
    -e '/\bopentelemetry-util-http\b/d' \
  | sort -u


%build
for pkgdir in %{pkgdirs}
do
  pushd "${pkgdir}"
  %pyproject_wheel
  popd
done

%if %{with doc_pdf}
# As docs-requirements.txt notes:
#   Need to install the api/sdk in the venv for autodoc. Modifying sys.path
#   doesn't work for pkg_resources.
# The problem is that the opentelemetry namespace package is found both in the
# local paths (added to sys.path by docs/conf.py) and in the build
# environment’s global site-packages; modifying PYTHONPATH allows one or the
# other to be found, but does not ”overlay” them. For example, if an
# ”opentelemetry“ without “opentelemetry.instrumentation” is found first, then
# “opentelemetry.instrumentation” will not be found, even if it exists
# elsewhere in the Python path.
#
# Our workaround is to shove everything into one directory as it would be in
# the installed system.
OVERLAYDIR="${PWD}/docs/_overlay"
rm -vrf "${OVERLAYDIR}"
mkdir -p "${OVERLAYDIR}"
cp -rvp %{python3_sitelib}/opentelemetry* "${OVERLAYDIR}/"
# Actually installing the wheels would be more “proper,” but these packages
# don’t have generated code or compiled extensions, so simply copying the
# sources will work here.
for pkgdir in %{pkgdirs}
do
  cp -rvp "${pkgdir}/src/opentelemetry" "${OVERLAYDIR}/"
done

PYTHONPATH="${OVERLAYDIR}" \
    %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install

install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}'


%check
for pkgdir in %{pkgdirs}
do
  unset k
  unset ignore

  ignore="${ignore-} --ignore-glob=*benchmark*"

  case "${pkgdir}" in
  instrumentation/opentelemetry-instrumentation-aiohttp-client)
    # These tests require network access.
    k="${k-}${k+ and }not (TestAioHttpIntegration and test_credential_removal)"
    # This is some kind of metadata issue with
    # pkg_resources.iter_entry_points(). It is probably specific to the RPM
    # build environment. See also the similar test skips in
    # python-opentelemetry.
    k="${k-}${k+ and }not (TestLoadingAioHttpInstrumentor and test_loading_instrumentor)"
    ;;
%if %{without moto}
  # Can’t run the tests; do an import-only “smoke test” instead.
  instrumentation/opentelemetry-instrumentation-boto)
    %{py3_check_import opentelemetry.instrumentation.boto
      opentelemetry.instrumentation.boto.package
      opentelemetry.instrumentation.boto.version}
    continue
    ;;
  instrumentation/opentelemetry-instrumentation-botocore)
    %{py3_check_import opentelemetry.instrumentation.botocore
      opentelemetry.instrumentation.botocore.package
      opentelemetry.instrumentation.botocore.version
      opentelemetry.instrumentation.botocore.extensions
      opentelemetry.instrumentation.botocore.extensions.dynamodb
      opentelemetry.instrumentation.botocore.extensions.lmbd
      opentelemetry.instrumentation.botocore.extensions.sns
      opentelemetry.instrumentation.botocore.extensions.sqs
      opentelemetry.instrumentation.botocore.extensions.types}
    continue
    ;;
%endif
%if %{without elasticsearch_dsl}
  # Can’t run the tests; do an import-only “smoke test” instead.
  instrumentation/opentelemetry-instrumentation-elasticsearch)
    %{py3_check_import opentelemetry.instrumentation.elasticsearch
      opentelemetry.instrumentation.elasticsearch.package
      opentelemetry.instrumentation.elasticsearch.version}
    continue
    ;;
%endif
%if %{without werkzeug}
  # Can’t run the tests; do an import-only “smoke test” instead.
  instrumentation/opentelemetry-instrumentation-pyramid)
    %{py3_check_import opentelemetry.instrumentation.pyramid
      opentelemetry.instrumentation.pyramid.callbacks
      opentelemetry.instrumentation.pyramid.package
      opentelemetry.instrumentation.pyramid.version}
    continue
    ;;
%endif
  instrumentation/opentelemetry-instrumentation-tornado)
    # These tests require network access.
    k="${k-}${k+ and }not (TestTornadoInstrumentation and test_credential_removal)"
    ;;
  opentelemetry-contrib-instrumentations)
    # This package has no tests; it is effectively a metapackage, and it is not
    # importable due to a hyphen in the ”package“ directory name.
    continue
    ;;
  esac

  %pytest "${pkgdir}" ${ignore-} -k "${k-}"
done


%files doc
%license LICENSE LICENSE.Apache LICENSE.BSD3
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%if %{with doc_pdf}
%doc docs/_build/latex/opentelemetrypythoncontrib.pdf
%endif


%if %{with protobuf4}
%files -n python3-opentelemetry-exporter-prometheus-remote-write
%license LICENSE LICENSE.Apache LICENSE.BSD3
%doc exporter/opentelemetry-exporter-prometheus-remote-write/README.rst
%doc exporter/opentelemetry-exporter-prometheus-remote-write/example/

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,exporter/}

%{python3_sitelib}/opentelemetry/exporter/prometheus_remote_write/
%{python3_sitelib}/opentelemetry_exporter_prometheus_remote_write-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-exporter-richconsole
%license LICENSE LICENSE.Apache LICENSE.BSD3
%doc exporter/opentelemetry-exporter-richconsole/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,exporter/}

%{python3_sitelib}/opentelemetry/exporter/richconsole/
%{python3_sitelib}/opentelemetry_exporter_richconsole-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation
%license opentelemetry-instrumentation/LICENSE
%doc opentelemetry-instrumentation/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/py.typed
%dir %{python3_sitelib}/opentelemetry/instrumentation/__pycache__/
%pycached %{python3_sitelib}/opentelemetry/instrumentation/*.py
%{python3_sitelib}/opentelemetry/instrumentation/auto_instrumentation/
%{python3_sitelib}/opentelemetry_instrumentation-%{prerel_distinfo}/

%{_bindir}/opentelemetry-bootstrap
%{_bindir}/opentelemetry-instrument

%{_mandir}/man1/opentelemetry-bootstrap.1*
%{_mandir}/man1/opentelemetry-instrument.1*


%files -n python3-opentelemetry-distro
%license LICENSE LICENSE.Apache LICENSE.BSD3
%doc opentelemetry-distro/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/

%{python3_sitelib}/opentelemetry/distro/
%{python3_sitelib}/opentelemetry_distro-%{prerel_distinfo}/


%files -n python3-opentelemetry-propagator-aws-xray
%license propagator/opentelemetry-propagator-aws-xray/LICENSE
%doc propagator/opentelemetry-propagator-aws-xray/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,propagators/}

%{python3_sitelib}/opentelemetry/propagators/aws/
%global aws_propagator_distinfo %(echo '%{aws_propagator_version}' | tr -d '~^').dist-info
%{python3_sitelib}/opentelemetry_propagator_aws_xray-%{aws_propagator_distinfo}/


%files -n python3-opentelemetry-propagator-ot-trace
%license LICENSE LICENSE.Apache LICENSE.BSD3
%doc propagator/opentelemetry-propagator-ot-trace/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,propagators/}

%{python3_sitelib}/opentelemetry/propagators/ot_trace/
%{python3_sitelib}/opentelemetry_propagator_ot_trace-%{prerel_distinfo}/


%files -n python3-opentelemetry-sdk-extension-aws
%license sdk-extension/opentelemetry-sdk-extension-aws/LICENSE
%doc sdk-extension/opentelemetry-sdk-extension-aws/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,sdk/,sdk/extension/}

%{python3_sitelib}/opentelemetry/sdk/extension/aws/
%global aws_sdk_distinfo %(echo '%{aws_sdk_version}' | tr -d '~^').dist-info
%{python3_sitelib}/opentelemetry_sdk_extension_aws-%{aws_sdk_distinfo}/


%files -n python3-opentelemetry-util-http
%license LICENSE LICENSE.Apache LICENSE.BSD3
%doc util/opentelemetry-util-http/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,util/}

%{python3_sitelib}/opentelemetry/util/http/
%{python3_sitelib}/opentelemetry_util_http-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-aiohttp-client
%license instrumentation/opentelemetry-instrumentation-aiohttp-client/LICENSE
%doc instrumentation/opentelemetry-instrumentation-aiohttp-client/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/aiohttp_client/
%{python3_sitelib}/opentelemetry_instrumentation_aiohttp_client-%{prerel_distinfo}/


%if %{with aiopg}
%files -n python3-opentelemetry-instrumentation-aiopg
%license instrumentation/opentelemetry-instrumentation-aiopg/LICENSE
%doc instrumentation/opentelemetry-instrumentation-aiopg/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/aiopg/
%{python3_sitelib}/opentelemetry_instrumentation_aiopg-%{prerel_distinfo}/
%endif


%if %{with aio_pika}
%files -n python3-opentelemetry-instrumentation-aio-pika
%license instrumentation/opentelemetry-instrumentation-aio-pika/LICENSE
%doc instrumentation/opentelemetry-instrumentation-aio-pika/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/aio_pika/
%{python3_sitelib}/opentelemetry_instrumentation_aio_pika-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-instrumentation-asgi
%license instrumentation/opentelemetry-instrumentation-asgi/LICENSE
%doc instrumentation/opentelemetry-instrumentation-asgi/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/asgi/
%{python3_sitelib}/opentelemetry_instrumentation_asgi-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-asyncpg
%license instrumentation/opentelemetry-instrumentation-asyncpg/LICENSE
%doc instrumentation/opentelemetry-instrumentation-asyncpg/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/asyncpg/
%{python3_sitelib}/opentelemetry_instrumentation_asyncpg-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-aws-lambda
%license instrumentation/opentelemetry-instrumentation-aws-lambda/LICENSE
%doc instrumentation/opentelemetry-instrumentation-aws-lambda/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/aws_lambda/
%{python3_sitelib}/opentelemetry_instrumentation_aws_lambda-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-boto
%license instrumentation/opentelemetry-instrumentation-boto/LICENSE
%doc instrumentation/opentelemetry-instrumentation-boto/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/boto/
%{python3_sitelib}/opentelemetry_instrumentation_boto-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-boto3sqs
%license instrumentation/opentelemetry-instrumentation-boto3sqs/LICENSE
%doc instrumentation/opentelemetry-instrumentation-boto3sqs/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/boto3sqs/
%{python3_sitelib}/opentelemetry_instrumentation_boto3sqs-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-botocore
%license instrumentation/opentelemetry-instrumentation-botocore/LICENSE
%doc instrumentation/opentelemetry-instrumentation-botocore/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/botocore/
%{python3_sitelib}/opentelemetry_instrumentation_botocore-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-celery
%license instrumentation/opentelemetry-instrumentation-celery/LICENSE
%doc instrumentation/opentelemetry-instrumentation-celery/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/celery/
%{python3_sitelib}/opentelemetry_instrumentation_celery-%{prerel_distinfo}/


%if %{with confluent_kafka}
%files -n python3-opentelemetry-instrumentation-confluent-kafka
%license instrumentation/opentelemetry-instrumentation-confluent-kafka/LICENSE
%doc instrumentation/opentelemetry-instrumentation-confluent-kafka/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/confluent_kafka/
%{python3_sitelib}/opentelemetry_instrumentation_confluent_kafka-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-instrumentation-dbapi
%license instrumentation/opentelemetry-instrumentation-dbapi/LICENSE
%doc instrumentation/opentelemetry-instrumentation-dbapi/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/dbapi/
%{python3_sitelib}/opentelemetry_instrumentation_dbapi-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-django
%license instrumentation/opentelemetry-instrumentation-django/LICENSE
%doc instrumentation/opentelemetry-instrumentation-django/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/django/
%{python3_sitelib}/opentelemetry_instrumentation_django-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-elasticsearch
%license instrumentation/opentelemetry-instrumentation-elasticsearch/LICENSE
%doc instrumentation/opentelemetry-instrumentation-elasticsearch/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}


%{python3_sitelib}/opentelemetry/instrumentation/elasticsearch/
%{python3_sitelib}/opentelemetry_instrumentation_elasticsearch-%{prerel_distinfo}/


%if %{with falcon}
%files -n python3-opentelemetry-instrumentation-falcon
%license instrumentation/opentelemetry-instrumentation-falcon/LICENSE
%doc instrumentation/opentelemetry-instrumentation-falcon/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/falcon/
%{python3_sitelib}/opentelemetry_instrumentation_falcon-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-instrumentation-fastapi
%license instrumentation/opentelemetry-instrumentation-fastapi/LICENSE
%doc instrumentation/opentelemetry-instrumentation-fastapi/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/fastapi/
%{python3_sitelib}/opentelemetry_instrumentation_fastapi-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-flask
%license instrumentation/opentelemetry-instrumentation-flask/LICENSE
%doc instrumentation/opentelemetry-instrumentation-flask/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/flask/
%{python3_sitelib}/opentelemetry_instrumentation_flask-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-grpc
%license instrumentation/opentelemetry-instrumentation-grpc/LICENSE
%doc instrumentation/opentelemetry-instrumentation-grpc/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/grpc/
%{python3_sitelib}/opentelemetry_instrumentation_grpc-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-httpx
%license instrumentation/opentelemetry-instrumentation-httpx/LICENSE
%doc instrumentation/opentelemetry-instrumentation-httpx/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/httpx/
%{python3_sitelib}/opentelemetry_instrumentation_httpx-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-jinja2
%license instrumentation/opentelemetry-instrumentation-jinja2/LICENSE
%doc instrumentation/opentelemetry-instrumentation-jinja2/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/jinja2/
%{python3_sitelib}/opentelemetry_instrumentation_jinja2-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-kafka-python
%license instrumentation/opentelemetry-instrumentation-kafka-python/LICENSE
%doc instrumentation/opentelemetry-instrumentation-kafka-python/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/kafka/
%{python3_sitelib}/opentelemetry_instrumentation_kafka_python-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-logging
%license instrumentation/opentelemetry-instrumentation-logging/LICENSE
%doc instrumentation/opentelemetry-instrumentation-logging/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/logging/
%{python3_sitelib}/opentelemetry_instrumentation_logging-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-mysql
%license instrumentation/opentelemetry-instrumentation-mysql/LICENSE
%doc instrumentation/opentelemetry-instrumentation-mysql/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/mysql/
%{python3_sitelib}/opentelemetry_instrumentation_mysql-%{prerel_distinfo}/



%files -n python3-opentelemetry-instrumentation-pika
%license instrumentation/opentelemetry-instrumentation-pika/LICENSE
%doc instrumentation/opentelemetry-instrumentation-pika/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/pika/
%{python3_sitelib}/opentelemetry_instrumentation_pika-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-psycopg2
%license instrumentation/opentelemetry-instrumentation-psycopg2/LICENSE
%doc instrumentation/opentelemetry-instrumentation-psycopg2/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/psycopg2/
%{python3_sitelib}/opentelemetry_instrumentation_psycopg2-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-pymemcache
%license instrumentation/opentelemetry-instrumentation-pymemcache/LICENSE
%doc instrumentation/opentelemetry-instrumentation-pymemcache/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/pymemcache/
%{python3_sitelib}/opentelemetry_instrumentation_pymemcache-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-pymongo
%license instrumentation/opentelemetry-instrumentation-pymongo/LICENSE
%doc instrumentation/opentelemetry-instrumentation-pymongo/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/pymongo/
%{python3_sitelib}/opentelemetry_instrumentation_pymongo-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-pymysql
%license instrumentation/opentelemetry-instrumentation-pymysql/LICENSE
%doc instrumentation/opentelemetry-instrumentation-pymysql/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/pymysql/
%{python3_sitelib}/opentelemetry_instrumentation_pymysql-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-pyramid
%license instrumentation/opentelemetry-instrumentation-pyramid/LICENSE
%doc instrumentation/opentelemetry-instrumentation-pyramid/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/pyramid/
%{python3_sitelib}/opentelemetry_instrumentation_pyramid-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-redis
%license instrumentation/opentelemetry-instrumentation-redis/LICENSE
%doc instrumentation/opentelemetry-instrumentation-redis/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/redis/
%{python3_sitelib}/opentelemetry_instrumentation_redis-%{prerel_distinfo}/


%if %{with remoulade}
%files -n python3-opentelemetry-instrumentation-remoulade
%license instrumentation/opentelemetry-instrumentation-remoulade/LICENSE
%doc instrumentation/opentelemetry-instrumentation-remoulade/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/remoulade/
%{python3_sitelib}/opentelemetry_instrumentation_remoulade-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-instrumentation-requests
%license instrumentation/opentelemetry-instrumentation-requests/LICENSE
%doc instrumentation/opentelemetry-instrumentation-requests/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/requests/
%{python3_sitelib}/opentelemetry_instrumentation_requests-%{prerel_distinfo}/


%if %{with sklearn}
%files -n python3-opentelemetry-instrumentation-sklearn
%license instrumentation/opentelemetry-instrumentation-sklearn/LICENSE
%doc instrumentation/opentelemetry-instrumentation-sklearn/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/sklearn/
%{python3_sitelib}/opentelemetry_instrumentation_sklearn-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-instrumentation-sqlalchemy
%license instrumentation/opentelemetry-instrumentation-sqlalchemy/LICENSE
%doc instrumentation/opentelemetry-instrumentation-sqlalchemy/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/sqlalchemy/
%{python3_sitelib}/opentelemetry_instrumentation_sqlalchemy-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-sqlite3
%license instrumentation/opentelemetry-instrumentation-sqlite3/LICENSE
%doc instrumentation/opentelemetry-instrumentation-sqlite3/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/sqlite3/
%{python3_sitelib}/opentelemetry_instrumentation_sqlite3-%{prerel_distinfo}/


%if %{with starlette}
%files -n python3-opentelemetry-instrumentation-starlette
%license instrumentation/opentelemetry-instrumentation-starlette/LICENSE
%doc instrumentation/opentelemetry-instrumentation-starlette/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/starlette/
%{python3_sitelib}/opentelemetry_instrumentation_starlette-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-instrumentation-system-metrics
%license instrumentation/opentelemetry-instrumentation-system-metrics/LICENSE
%doc instrumentation/opentelemetry-instrumentation-system-metrics/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/system_metrics/
%{python3_sitelib}/opentelemetry_instrumentation_system_metrics-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-tornado
%license instrumentation/opentelemetry-instrumentation-tornado/LICENSE
%doc instrumentation/opentelemetry-instrumentation-tornado/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/tornado/
%{python3_sitelib}/opentelemetry_instrumentation_tornado-%{prerel_distinfo}/


%if %{with tortoise_orm}
%files -n python3-opentelemetry-instrumentation-tortoiseorm
%license instrumentation/opentelemetry-instrumentation-tortoiseorm/LICENSE
%doc instrumentation/opentelemetry-instrumentation-tortoiseorm/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/tortoiseorm/
%{python3_sitelib}/opentelemetry_instrumentation_tortoiseorm-%{prerel_distinfo}/
%endif


%files -n python3-opentelemetry-instrumentation-urllib
%license instrumentation/opentelemetry-instrumentation-urllib/LICENSE
%doc instrumentation/opentelemetry-instrumentation-urllib/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/urllib/
%{python3_sitelib}/opentelemetry_instrumentation_urllib-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-urllib3
%license instrumentation/opentelemetry-instrumentation-urllib3/LICENSE
%doc instrumentation/opentelemetry-instrumentation-urllib3/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/urllib3/
%{python3_sitelib}/opentelemetry_instrumentation_urllib3-%{prerel_distinfo}/


%files -n python3-opentelemetry-instrumentation-wsgi
%license instrumentation/opentelemetry-instrumentation-wsgi/LICENSE
%doc instrumentation/opentelemetry-instrumentation-wsgi/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/{,instrumentation/}

%{python3_sitelib}/opentelemetry/instrumentation/wsgi/
%{python3_sitelib}/opentelemetry_instrumentation_wsgi-%{prerel_distinfo}/


%files -n python3-opentelemetry-contrib-instrumentations
%license opentelemetry-contrib-instrumentations/LICENSE
%doc opentelemetry-contrib-instrumentations/README.rst

# Shared namespace directories
%dir %{python3_sitelib}/opentelemetry/

%{python3_sitelib}/opentelemetry/contrib-instrumentations/
%{python3_sitelib}/opentelemetry_contrib_instrumentations-%{prerel_distinfo}/


%changelog
%autochangelog
