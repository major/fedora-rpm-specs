%bcond_without check

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/bazelbuild/rules_go/go/tools/coverdata\\)$


# https://github.com/google/gvisor
%global goipath         gvisor.dev/gvisor
%global forgeurl        https://github.com/google/gvisor
Version:                20211129.0
# taken from the "go" branch (as bazel is not available in fedora)
%global commit          9bd5098511159f089530db891c1fd4c770cccc62

%global go_arches       x86_64 aarch64

%gometa

%global common_description %{expand:
gVisor is an open-source, OCI-compatible sandbox runtime that provides
a virtualized container environment. It runs containers with a new
user-space kernel, delivering a low overhead container security
solution for high-density applications.

gVisor integrates with Docker, containerd and Kubernetes, making it
easier to improve the security isolation of your containers while
still using familiar tooling. Additionally, gVisor supports a variety
of underlying mechanisms for intercepting application calls, allowing
it to run in diverse host environments, including cloud-hosted virtual
machines.}

%global gosupfiles      ${vendor[@]}

%global golicenses      LICENSE
%global godocs          README.md AUTHORS

Name:           %{goname}
Release:        %autorelease
Summary:        A container sandbox runtime focused on security, efficiency, and ease of use

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        https://github.com/bazelbuild/rules_go/raw/master/go/tools/coverdata/coverdata.go

# Vendored
# BuildRequires:  golang(github.com/bazelbuild/rules_go/go/tools/coverdata)
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/cenkalti/backoff)
BuildRequires:  golang(github.com/containerd/cgroups)
BuildRequires:  golang(github.com/containerd/cgroups/stats/v1)
BuildRequires:  golang(github.com/containerd/cgroups/v2)
BuildRequires:  golang(github.com/containerd/console)
BuildRequires:  golang(github.com/containerd/containerd/api/events)
BuildRequires:  golang(github.com/containerd/containerd/api/types/task)
BuildRequires:  golang(github.com/containerd/containerd/errdefs)
BuildRequires:  golang(github.com/containerd/containerd/events)
BuildRequires:  golang(github.com/containerd/containerd/log)
BuildRequires:  golang(github.com/containerd/containerd/mount)
BuildRequires:  golang(github.com/containerd/containerd/namespaces)
BuildRequires:  golang(github.com/containerd/containerd/pkg/process)
BuildRequires:  golang(github.com/containerd/containerd/pkg/stdio)
BuildRequires:  golang(github.com/containerd/containerd/runtime)
BuildRequires:  golang(github.com/containerd/containerd/runtime/linux/runctypes)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v2/shim)
BuildRequires:  golang(github.com/containerd/containerd/runtime/v2/task)
BuildRequires:  golang(github.com/containerd/containerd/sys/reaper)
BuildRequires:  golang(github.com/containerd/fifo)
BuildRequires:  golang(github.com/containerd/go-runc)
BuildRequires:  golang(github.com/containerd/typeurl)
BuildRequires:  golang(github.com/gofrs/flock)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/google/btree)
BuildRequires:  golang(github.com/google/subcommands)
BuildRequires:  golang(github.com/kr/pty)
BuildRequires:  golang(github.com/mattbaird/jsonpatch)
BuildRequires:  golang(github.com/mohae/deepcopy)
BuildRequires:  golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/syndtr/gocapability/capability)
BuildRequires:  golang(github.com/vishvananda/netlink)
BuildRequires:  golang(golang.org/x/sync/errgroup)
BuildRequires:  golang(golang.org/x/sys/unix)
BuildRequires:  golang(golang.org/x/time/rate)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/encoding/prototext)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  golang(google.golang.org/protobuf/types/known/anypb)
BuildRequires:  golang(google.golang.org/protobuf/types/known/timestamppb)
BuildRequires:  golang(k8s.io/api/admission/v1beta1)
BuildRequires:  golang(k8s.io/api/admissionregistration/v1beta1)
BuildRequires:  golang(k8s.io/api/core/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/net)
BuildRequires:  golang(k8s.io/client-go/kubernetes)
BuildRequires:  golang(k8s.io/client-go/rest)

%description
%{common_description}

%gopkg

%prep
%goprep
mkdir -p vendor/github.com/bazelbuild/rules_go/go/tools/coverdata/
cp %{S:1} vendor/github.com/bazelbuild/rules_go/go/tools/coverdata/

%build
%gobuild -o %{gobuilddir}/bin/runsc %{goipath}/runsc

%install
mapfile -t vendor <<< $(find vendor -type f)
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
