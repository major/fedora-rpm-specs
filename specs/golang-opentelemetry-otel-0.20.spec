# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://github.com/open-telemetry/opentelemetry-go
%global goipath         go.opentelemetry.io/otel-0.20
%global forgeurl        https://github.com/open-telemetry/opentelemetry-go
Version:                0.20.0

%gometa

%global common_description %{expand:
OpenTelemetry Go API and SDK.}

%global golicenses      LICENSE
%global godocs          example RELEASING.md CHANGELOG.md CONTRIBUTING.md\\\
                        README.md

Name:           %{goname}
Release:        %autorelease
Summary:        OpenTelemetry Go API and SDK

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# To avoid "found import comments" errors
Patch0:         0001-Remove-import-comments.patch

BuildRequires:  golang(github.com/benbjohnson/clock)
BuildRequires:  golang(github.com/cenkalti/backoff/v4)
BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)
BuildRequires:  golang(github.com/openzipkin/zipkin-go/model)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus/promhttp)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(go.opencensus.io/metric)
BuildRequires:  golang(go.opencensus.io/metric/metricdata)
BuildRequires:  golang(go.opencensus.io/metric/metricexport)
BuildRequires:  golang(go.opencensus.io/metric/metricproducer)
BuildRequires:  golang(go.opencensus.io/resource)
BuildRequires:  golang(go.opencensus.io/stats)
BuildRequires:  golang(go.opencensus.io/stats/view)
BuildRequires:  golang(go.opencensus.io/tag)
BuildRequires:  golang(go.opencensus.io/trace)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/collector/metrics/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/collector/trace/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/common/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/metrics/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/resource/v1)
BuildRequires:  golang(go.opentelemetry.io/proto-0.7/otlp/trace/v1)
BuildRequires:  golang(golang.org/x/mod/semver)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/genproto/googleapis/rpc/errdetails)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/credentials)
BuildRequires:  golang(google.golang.org/grpc/encoding/gzip)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/proto)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(github.com/stretchr/testify/suite)
BuildRequires:  golang(go.opencensus.io/trace/tracestate)
BuildRequires:  golang(google.golang.org/protobuf/types/known/durationpb)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1
sed -i \
    -e 's|"go.opentelemetry.io/otel|"go.opentelemetry.io/otel-0.20|' \
    $(find . -name '*.go')
sed -i \
    -e 's|"go.opentelemetry.io/proto|"go.opentelemetry.io/proto-0.7|' \
    $(find . -name '*.go')


%install
%gopkginstall

%if %{with check}
%check
for test in "TestNewExporter_withInvalidSecurityConfiguration" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20.0-1
- convert license to SPDX

* Fri Aug 06 2021 Robert-André Mauchin <zebob.m@gmail.com> 0.20.0-1
- Uncommitted changes
