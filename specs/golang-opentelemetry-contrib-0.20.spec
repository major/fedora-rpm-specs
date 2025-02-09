# Generated by go2rpm 1.5.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/open-telemetry/opentelemetry-go-contrib
%global goipath         go.opentelemetry.io/contrib-0.20
%global forgeurl        https://github.com/open-telemetry/opentelemetry-go-contrib
Version:                0.20.0

%gometa

%global common_description %{expand:
Collection of extensions for OpenTelemetry-Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md RELEASING.md\\\
                        example

Name:           %{goname}
Release:        %autorelease
Summary:        Collection of extensions for OpenTelemetry-Go

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# Fix for Golang 1.18
Patch0:         0001-Fix-Errorf-variable-in-host_test.patch

BuildRequires:  golang(cloud.google.com/go/compute/metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/ec2metadata)
BuildRequires:  golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires:  golang(github.com/aws/smithy-go/middleware)
BuildRequires:  golang(github.com/aws/smithy-go/transport/http)
BuildRequires:  golang(github.com/bradfitz/gomemcache/memcache)
BuildRequires:  golang(github.com/DataDog/datadog-go/statsd)
BuildRequires:  golang(github.com/emicklei/go-restful/v3)
BuildRequires:  golang(github.com/felixge/httpsnoop)
BuildRequires:  golang(github.com/gin-gonic/gin)
BuildRequires:  golang(github.com/go-kit/kit/endpoint)
BuildRequires:  golang(github.com/go-kit/kit/sd/lb)
BuildRequires:  golang(github.com/gocql/gocql)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/golang/snappy)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/labstack/echo/v4)
BuildRequires:  golang(github.com/prometheus/prometheus/prompb)
BuildRequires:  golang(github.com/shirou/gopsutil/cpu)
BuildRequires:  golang(github.com/shirou/gopsutil/mem)
BuildRequires:  golang(github.com/shirou/gopsutil/net)
BuildRequires:  golang(github.com/shirou/gopsutil/process)
BuildRequires:  golang(github.com/Shopify/sarama)
BuildRequires:  golang(github.com/spf13/afero)
BuildRequires:  golang(github.com/spf13/viper)
BuildRequires:  golang(go.mongodb.org/mongo-driver/bson)
BuildRequires:  golang(go.mongodb.org/mongo-driver/event)
# BuildRequires:  golang(go.opencensus.io/examples/exporter)
# BuildRequires:  golang(go.opencensus.io/examples/grpc/proto)
BuildRequires:  golang(go.opencensus.io/plugin/ocgrpc)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opencensus.io/trace/propagation)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/attribute)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/baggage)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/bridge/opencensus/utils)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/codes)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/exporters/metric/prometheus)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/exporters/stdout)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/exporters/trace/zipkin)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/metric)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/metric/global)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/metric/number)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/propagation)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/export/metric)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/export/metric/aggregation)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/aggregator/histogram)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/controller/basic)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/processor/basic)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/selector/simple)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/resource)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/trace)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/semconv)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/trace)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/unit)
BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gopkg.in/macaron.v1)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/Shopify/sarama/mocks)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo)
BuildRequires:  golang(go.mongodb.org/mongo-driver/mongo/options)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/oteltest)
# BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/export/metric/metrictest)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/aggregator/aggregatortest)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/aggregator/lastvalue)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/aggregator/minmaxsumcount)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/metric/aggregator/sum)
BuildRequires:  golang(go.uber.org/goleak)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1
sed -i \
    -e 's|"go.opentelemetry.io/contrib|"go.opentelemetry.io/contrib-0.20|' \
    $(find . -name '*.go')
sed -i \
    -e 's|"go.opentelemetry.io/otel|"go.opentelemetry.io/otel-0.20|' \
    $(find . -name '*.go')
rm -rfv instrumentation/github.com/astaxie/beego/
rm -rfv instrumentation/github.com/aws/aws-sdk-go-v2/
# examples are not packaged
rm -rvf propagators/opencensus/examples

%install
%gopkginstall

%if %{with check}
%check
%gocheck -t exporters/metric
%endif

%gopkgfiles

%changelog
%autochangelog
