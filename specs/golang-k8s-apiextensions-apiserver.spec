# Generated by go2rpm
%bcond_without check

# https://github.com/kubernetes/apiextensions-apiserver
%global goipath         k8s.io/apiextensions-apiserver
%global forgeurl        https://github.com/kubernetes/apiextensions-apiserver
Version:                1.22.0
%global tag             kubernetes-1.22.0
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
API server for API extensions like CustomResourceDefinitions.}

%global golicenses      LICENSE
%global godocs          examples code-of-conduct.md CONTRIBUTING.md README.md

%global gosupfiles      "${examples[@]}"

Name:           %{goname}
Release:        %autorelease
Summary:        API server for API extensions like CustomResourceDefinitions

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  golang(github.com/emicklei/go-restful)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/spf13/cobra)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(go.etcd.io/etcd/client/pkg/v3/transport)
BuildRequires:  golang(go.etcd.io/etcd/client/v3)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(k8s.io/api/autoscaling/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta/table)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/validation/path)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/conversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/protobuf)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/versioning)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/uuid)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation/field)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/waitgroup)
BuildRequires:  golang(k8s.io/apimachinery/pkg/version)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/apiserver/pkg/admission)
BuildRequires:  golang(k8s.io/apiserver/pkg/authorization/authorizer)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints/discovery)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints/handlers)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints/handlers/fieldmanager)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints/handlers/responsewriters)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints/metrics)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints/openapi)
BuildRequires:  golang(k8s.io/apiserver/pkg/endpoints/request)
BuildRequires:  golang(k8s.io/apiserver/pkg/features)
BuildRequires:  golang(k8s.io/apiserver/pkg/registry/generic)
BuildRequires:  golang(k8s.io/apiserver/pkg/registry/generic/registry)
BuildRequires:  golang(k8s.io/apiserver/pkg/registry/rest)
BuildRequires:  golang(k8s.io/apiserver/pkg/server)
BuildRequires:  golang(k8s.io/apiserver/pkg/server/filters)
BuildRequires:  golang(k8s.io/apiserver/pkg/server/options)
BuildRequires:  golang(k8s.io/apiserver/pkg/server/storage)
BuildRequires:  golang(k8s.io/apiserver/pkg/storage)
BuildRequires:  golang(k8s.io/apiserver/pkg/storage/errors)
BuildRequires:  golang(k8s.io/apiserver/pkg/storage/names)
BuildRequires:  golang(k8s.io/apiserver/pkg/storage/storagebackend)
BuildRequires:  golang(k8s.io/apiserver/pkg/util/dryrun)
BuildRequires:  golang(k8s.io/apiserver/pkg/util/feature)
BuildRequires:  golang(k8s.io/apiserver/pkg/util/openapi)
BuildRequires:  golang(k8s.io/apiserver/pkg/util/proxy)
BuildRequires:  golang(k8s.io/apiserver/pkg/util/webhook)
BuildRequires:  golang(k8s.io/apiserver/pkg/warning)
BuildRequires:  golang(k8s.io/client-go/discovery)
BuildRequires:  golang(k8s.io/client-go/discovery/fake)
BuildRequires:  golang(k8s.io/client-go/dynamic)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/kubernetes/scheme)
BuildRequires:  golang(k8s.io/client-go/listers/core/v1)
BuildRequires:  golang(k8s.io/client-go/rest)
BuildRequires:  golang(k8s.io/client-go/restmapper)
BuildRequires:  golang(k8s.io/client-go/scale)
BuildRequires:  golang(k8s.io/client-go/scale/scheme/autoscalingv1)
BuildRequires:  golang(k8s.io/client-go/testing)
BuildRequires:  golang(k8s.io/client-go/tools/cache)
BuildRequires:  golang(k8s.io/client-go/util/flowcontrol)
BuildRequires:  golang(k8s.io/client-go/util/jsonpath)
BuildRequires:  golang(k8s.io/client-go/util/workqueue)
BuildRequires:  golang(k8s.io/component-base/featuregate)
BuildRequires:  golang(k8s.io/component-base/logs)
BuildRequires:  golang(k8s.io/component-base/metrics)
BuildRequires:  golang(k8s.io/component-base/metrics/legacyregistry)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/aggregator)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/builder)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/common)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/handler)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/util/proto)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/validation/errors)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/validation/spec)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/validation/strfmt)
BuildRequires:  golang(k8s.io/kube-openapi/pkg/validation/validate)
BuildRequires:  golang(k8s.io/utils/pointer)
BuildRequires:  golang(k8s.io/utils/trace)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/fieldpath)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/googleapis/gnostic/openapiv2)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/yaml.v2)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/fuzzer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/fuzzer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  golang(k8s.io/apiserver/pkg/storage/etcd3)
BuildRequires:  golang(k8s.io/apiserver/pkg/storage/etcd3/testing)
BuildRequires:  golang(k8s.io/client-go/util/retry)
BuildRequires:  golang(k8s.io/component-base/featuregate/testing)
BuildRequires:  golang(sigs.k8s.io/yaml)
%endif

%description %{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/apiextensions-apiserver %{goipath}

%install
mapfile -t examples <<< $(find examples -type f)
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
# test/integration: needs network
%gocheck -t test/integration -t pkg/controller/openapi -t pkg/apiserver/validation -t pkg/apiserver -d pkg/registry/customresource
%endif

%files
%license LICENSE
%doc examples code-of-conduct.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog