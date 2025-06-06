# Generated by go2rpm 1.9.0
%bcond_without check
%bcond_with bootstrap
%global debug_package %{nil}


%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/kubernetes/apiserver
%global goipath         k8s.io/apiserver
%global forgeurl        https://github.com/kubernetes/apiserver
Version:                1.22.0
%global tag             kubernetes-1.22.0
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
This library contains code to create Kubernetes aggregation server complete with
delegated authentication and authorization, kubectl compatible discovery
information, optional admission chain, and versioned types. It's first consumers
are k8s.io/kubernetes, k8s.io/kube-aggregator, and
github.com/kubernetes-incubator/service-catalog.}

%global golicenses      LICENSE
%global godocs          code-of-conduct.md CONTRIBUTING.md README.md

%global gosupfiles      ${example[@]}

Name:           %{goname}
Release:        %autorelease
Summary:        Library for writing a Kubernetes-style API server

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%if %{without bootstrap}
BuildRequires:  golang(bitbucket.org/ww/goautoneg)
BuildRequires:  golang(github.com/coreos/go-oidc/v3/oidc)
BuildRequires:  golang(github.com/coreos/go-systemd/v22/daemon)
BuildRequires:  golang(github.com/emicklei/go-restful)
BuildRequires:  golang(github.com/evanphx/json-patch)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/googleapis/gnostic/openapiv2)
BuildRequires:  golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/mvccpb)
BuildRequires:  golang(go.etcd.io/etcd/api/v3/v3rpc/rpctypes)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/transport)
BuildRequires:  golang(go.etcd.io/etcd/client/v3)
BuildRequires:  golang(go.etcd.io/etcd/server/v3/embed)
BuildRequires:  golang(go.opentelemetry.io/contrib-0.20/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  golang(go.opentelemetry.io/contrib-0.20/instrumentation/net/http/otelhttp)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/exporters/otlp/otlpgrpc)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/resource)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/sdk/trace)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/semconv)
BuildRequires:  golang(go.opentelemetry.io/otel-0.20/trace)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(go.uber.org/zap/zaptest)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte)
BuildRequires:  golang(golang.org/x/crypto/nacl/secretbox)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/websocket)
BuildRequires:  golang(golang.org/x/sync/singleflight)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/grpclog)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires:  golang(k8s.io/api/admission/v1)
BuildRequires:  golang(k8s.io/api/admission/v1beta1)
BuildRequires:  golang(k8s.io/api/admissionregistration/v1)
BuildRequires:  golang(k8s.io/api/apiserverinternal/v1alpha1)
BuildRequires:  golang(k8s.io/api/authentication/v1)
BuildRequires:  golang(k8s.io/api/authentication/v1beta1)
BuildRequires:  golang(k8s.io/api/authorization/v1)
BuildRequires:  golang(k8s.io/api/authorization/v1beta1)
BuildRequires:  golang(k8s.io/api/coordination/v1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/api/flowcontrol/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/fuzzer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/validation/path)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1beta1/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/conversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/recognizer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/cache)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/clock)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/mergepatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/net)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/rand)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/uuid)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/waitgroup)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  golang(k8s.io/apimachinery/pkg/version)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/client-go/informers)
BuildRequires:  golang(k8s.io/client-go/informers/core/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/fake)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/authentication/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/authorization/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires:  golang(k8s.io/client-go/kubernetes/typed/flowcontrol/v1beta1)
BuildRequires:  golang(k8s.io/client-go/listers/admissionregistration/v1)
BuildRequires:  golang(k8s.io/client-go/listers/core/v1)
BuildRequires:  golang(k8s.io/client-go/listers/flowcontrol/v1beta1)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api)
BuildRequires:  golang(k8s.io/client-go/tools/events)
BuildRequires:  golang(k8s.io/client-go/transport)
BuildRequires:  golang(k8s.io/client-go/util/cert)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)
BuildRequires:  golang(k8s.io/client-go/util/keyutil)
BuildRequires:  golang(k8s.io/client-go/util/workqueue)
BuildRequires:  golang(k8s.io/component-base/cli/flag)
BuildRequires:  golang(k8s.io/component-base/featuregate)
BuildRequires:  golang(k8s.io/component-base/logs)
BuildRequires:  golang(k8s.io/component-base/metrics)
BuildRequires:  golang(k8s.io/component-base/metrics/legacyregistry)
BuildRequires:  golang(k8s.io/component-base/metrics/prometheus/workqueue)
BuildRequires:  golang(k8s.io/component-base/metrics/testutil)
BuildRequires:  golang(k8s.io/component-base/traces)
BuildRequires:  golang(k8s.io/component-base/version)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/builder)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/common)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/handler)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/schemaconv)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util/proto)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/validation/spec)
BuildRequires:  golang(k8s.io/utils/lru)
BuildRequires:  golang(k8s.io/utils/net)
BuildRequires:  golang(k8s.io/utils/path)
BuildRequires:  golang(k8s.io/utils/pointer)
BuildRequires:  golang(k8s.io/utils/trace)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/fieldpath)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/merge)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/typed)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/value)
BuildRequires:  golang(sigs.k8s.io/yaml)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/square/go-jose.v2)
BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/batch/v1)
BuildRequires:  golang(k8s.io/api/extensions/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/testapigroup/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/selection)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/dynamic)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/clientcmd/api/v1)
BuildRequires:  golang(k8s.io/component-base/featuregate/testing)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util/proto/testing)
%endif
%endif

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

sed -i "s|github.com/munnerz/goautoneg|bitbucket.org/ww/goautoneg|" $(find . -name "*.go")
sed -i "s|github.com/coreos/go-oidc|github.com/coreos/go-oidc/v3/oidc|" $(find . -name "*.go")
sed -i \
    -e 's|"go.opentelemetry.io/otel|"go.opentelemetry.io/otel-0.20|' \
    $(find . -name '*.go')
sed -i \
    -e 's|"go.opentelemetry.io/contrib|"go.opentelemetry.io/contrib-0.20|' \
    $(find . -name '*.go')

%install
mapfile -t example <<< $(find pkg/apis/example* -type f)
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck -d pkg/endpoints/handlers/fieldmanager -d pkg/util/webhook \
         -d pkg/registry/generic/registry -d pkg/server/filters \
         -d pkg/storage/storagebackend/factory -d pkg/util/flowcontrol/metrics
%endif
%endif

%gopkgfiles

%changelog
%autochangelog
