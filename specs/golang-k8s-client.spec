# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/kubernetes/client-go
%global goipath         k8s.io/client-go
%global forgeurl        https://github.com/kubernetes/client-go
Version:                1.22.0
%global tag             kubernetes-1.22.0
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Go clients for talking to a Kubernetes cluster.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md code-of-conduct.md\\\
                        CONTRIBUTING.md INSTALL.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go client for Kubernetes

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/Azure/go-autorest/autorest)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/adal)
BuildRequires:  golang(github.com/Azure/go-autorest/autorest/azure)
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/evanphx/json-patch)
BuildRequires:  golang(github.com/golang/groupcache/lru)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/googleapis/gnostic/openapiv2)
BuildRequires:  golang(github.com/gregjones/httpcache)
BuildRequires:  golang(github.com/gregjones/httpcache/diskcache)
BuildRequires:  golang(github.com/imdario/mergo)
BuildRequires:  golang(github.com/peterbourgon/diskv)
BuildRequires:  golang(github.com/spf13/pflag)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  golang(golang.org/x/oauth2/google)
BuildRequires:  golang(golang.org/x/term)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(k8s.io/api/admissionregistration/v1)
BuildRequires:  golang(k8s.io/api/admissionregistration/v1beta1)
BuildRequires:  golang(k8s.io/api/apiserverinternal/v1alpha1)
BuildRequires:  golang(k8s.io/api/apps/v1)
BuildRequires:  golang(k8s.io/api/apps/v1beta1)
BuildRequires:  golang(k8s.io/api/apps/v1beta2)
BuildRequires:  golang(k8s.io/api/authentication/v1)
BuildRequires:  golang(k8s.io/api/authentication/v1beta1)
BuildRequires:  golang(k8s.io/api/authorization/v1)
BuildRequires:  golang(k8s.io/api/authorization/v1beta1)
BuildRequires:  golang(k8s.io/api/autoscaling/v1)
BuildRequires:  golang(k8s.io/api/autoscaling/v2beta1)
BuildRequires:  golang(k8s.io/api/autoscaling/v2beta2)
BuildRequires:  golang(k8s.io/api/batch/v1)
BuildRequires:  golang(k8s.io/api/batch/v1beta1)
BuildRequires:  golang(k8s.io/api/certificates/v1)
BuildRequires:  golang(k8s.io/api/certificates/v1beta1)
BuildRequires:  golang(k8s.io/api/coordination/v1)
BuildRequires:  golang(k8s.io/api/coordination/v1beta1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/api/discovery/v1)
BuildRequires:  golang(k8s.io/api/discovery/v1beta1)
BuildRequires:  golang(k8s.io/api/events/v1)
BuildRequires:  golang(k8s.io/api/events/v1beta1)
BuildRequires:  golang(k8s.io/api/extensions/v1beta1)
BuildRequires:  golang(k8s.io/api/flowcontrol/v1alpha1)
BuildRequires:  golang(k8s.io/api/flowcontrol/v1beta1)
BuildRequires:  golang(k8s.io/api/imagepolicy/v1alpha1)
BuildRequires:  golang(k8s.io/api/networking/v1)
BuildRequires:  golang(k8s.io/api/networking/v1beta1)
BuildRequires:  golang(k8s.io/api/node/v1)
BuildRequires:  golang(k8s.io/api/node/v1alpha1)
BuildRequires:  golang(k8s.io/api/node/v1beta1)
BuildRequires:  golang(k8s.io/api/policy/v1)
BuildRequires:  golang(k8s.io/api/policy/v1beta1)
BuildRequires:  golang(k8s.io/api/rbac/v1)
BuildRequires:  golang(k8s.io/api/rbac/v1alpha1)
BuildRequires:  golang(k8s.io/api/rbac/v1beta1)
BuildRequires:  golang(k8s.io/api/scheduling/v1)
BuildRequires:  golang(k8s.io/api/scheduling/v1alpha1)
BuildRequires:  golang(k8s.io/api/scheduling/v1beta1)
BuildRequires:  golang(k8s.io/api/storage/v1)
BuildRequires:  golang(k8s.io/api/storage/v1alpha1)
BuildRequires:  golang(k8s.io/api/storage/v1beta1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/internalversion/scheme)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1/unstructured)
BuildRequires:  golang(k8s.io/apimachinery/pkg/conversion)
BuildRequires:  golang(k8s.io/apimachinery/pkg/fields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/labels)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/streaming)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/serializer/versioning)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/cache)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/clock)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/diff)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/httpstream)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/httpstream/spdy)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/json)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/managedfields)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/naming)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/net)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/remotecommand)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/sets)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires:  golang(k8s.io/apimachinery/pkg/version)
BuildRequires:  golang(k8s.io/apimachinery/pkg/watch)
BuildRequires:  golang(k8s.io/klog/v2)
BuildRequires:  golang(k8s.io/utils/buffer)
BuildRequires:  golang(k8s.io/utils/integer)
BuildRequires:  golang(k8s.io/utils/pointer)
BuildRequires:  golang(k8s.io/utils/trace)
BuildRequires:  golang(sigs.k8s.io/structured-merge-diff/v4/typed)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/gofuzz)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/apitesting/roundtrip)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1beta1)
BuildRequires:  golang(sigs.k8s.io/yaml)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d tools/clientcmd -d util/flowcontrol
%endif

%gopkgfiles

%changelog
%autochangelog
