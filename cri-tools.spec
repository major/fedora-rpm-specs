%global with_bundled 1
%global with_check 0

%if 0%{?fedora} > 28
%global with_debug 0
%else
%global with_debug 1
%endif

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

# It is only necessary to override %%gobuild to include the buildtags on RHEL 8 and below
# or where %%gobuild is otherwise undefined
%if ! 0%{?gobuild:1} || (%{defined rhel} && 0%{?rhel} <= 8)
%define gobuild(o:) go build -tags="$BUILDTAGS" -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%endif

%global provider github
%global provider_tld com
%global project kubernetes-sigs
%global repo %{name}
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}

Name: cri-tools
Version: 1.29.0
Release: 1%{?dist}
Summary: CLI and validation tools for Container Runtime Interface
License: ASL 2.0
URL: https://%{provider_prefix}
Source0: https://%{provider_prefix}/archive/v%{version}/%{name}-%{version}.tar.gz
# no ppc64
ExclusiveArch: %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: glibc-static
BuildRequires: go-md2man
Provides: crictl = %{version}-%{release}

# vendored libraries
# fedpkg prep
# ./vendor2provides.py cri-tools-%%{version}/vendor/modules.txt
Provides:       bundled(golang(github.com/Azure/go-ansiterm)) = d185dfc
Provides:       bundled(golang(github.com/Microsoft/go-winio)) = 0.6.0
Provides:       bundled(golang(github.com/beorn7/perks)) = 1.0.1
Provides:       bundled(golang(github.com/blang/semver/v4)) = 4.0.0
Provides:       bundled(golang(github.com/cenkalti/backoff/v4)) = 4.2.1
Provides:       bundled(golang(github.com/cespare/xxhash/v2)) = 2.2.0
Provides:       bundled(golang(github.com/cpuguy83/go-md2man/v2)) = 2.0.2
Provides:       bundled(golang(github.com/cyphar/filepath-securejoin)) = 0.2.4
Provides:       bundled(golang(github.com/davecgh/go-spew)) = 1.1.1
Provides:       bundled(golang(github.com/distribution/reference)) = 0.5.0
Provides:       bundled(golang(github.com/docker/docker)) = 24.0.7+incompatible
Provides:       bundled(golang(github.com/docker/go-units)) = 0.5.0
Provides:       bundled(golang(github.com/emicklei/go-restful/v3)) = 3.11.0
Provides:       bundled(golang(github.com/felixge/httpsnoop)) = 1.0.3
Provides:       bundled(golang(github.com/fsnotify/fsnotify)) = 1.7.0
Provides:       bundled(golang(github.com/go-logr/logr)) = 1.3.0
Provides:       bundled(golang(github.com/go-logr/stdr)) = 1.2.2
Provides:       bundled(golang(github.com/go-openapi/jsonpointer)) = 0.19.6
Provides:       bundled(golang(github.com/go-openapi/jsonreference)) = 0.20.2
Provides:       bundled(golang(github.com/go-openapi/swag)) = 0.22.3
Provides:       bundled(golang(github.com/go-task/slim-sprig)) = 52ccab3
Provides:       bundled(golang(github.com/gogo/protobuf)) = 1.3.2
Provides:       bundled(golang(github.com/golang/protobuf)) = 1.5.3
Provides:       bundled(golang(github.com/google/gnostic-models)) = 0.6.8
Provides:       bundled(golang(github.com/google/go-cmp)) = 0.6.0
Provides:       bundled(golang(github.com/google/gofuzz)) = 1.2.0
Provides:       bundled(golang(github.com/google/pprof)) = 4bb14d4
Provides:       bundled(golang(github.com/google/uuid)) = 1.4.0
Provides:       bundled(golang(github.com/gorilla/websocket)) = 1.5.0
Provides:       bundled(golang(github.com/grpc-ecosystem/grpc-gateway/v2)) = 2.16.0
Provides:       bundled(golang(github.com/josharian/intern)) = 1.0.0
Provides:       bundled(golang(github.com/json-iterator/go)) = 1.1.12
Provides:       bundled(golang(github.com/liggitt/tabwriter)) = 89fcab3
Provides:       bundled(golang(github.com/mailru/easyjson)) = 0.7.7
Provides:       bundled(golang(github.com/matttproud/golang_protobuf_extensions)) = 1.0.4
Provides:       bundled(golang(github.com/mitchellh/go-wordwrap)) = 1.0.1
Provides:       bundled(golang(github.com/moby/spdystream)) = 0.2.0
Provides:       bundled(golang(github.com/moby/term)) = 0.5.0
Provides:       bundled(golang(github.com/modern-go/concurrent)) = bacd9c7
Provides:       bundled(golang(github.com/modern-go/reflect2)) = 1.0.2
Provides:       bundled(golang(github.com/munnerz/goautoneg)) = a7dc8b6
Provides:       bundled(golang(github.com/mxk/go-flowrate)) = cca7078
Provides:       bundled(golang(github.com/onsi/ginkgo/v2)) = 2.13.2
Provides:       bundled(golang(github.com/onsi/gomega)) = 1.30.0
Provides:       bundled(golang(github.com/opencontainers/go-digest)) = 1.0.0
Provides:       bundled(golang(github.com/opencontainers/runc)) = 1.1.10
Provides:       bundled(golang(github.com/opencontainers/selinux)) = 1.11.0
Provides:       bundled(golang(github.com/prometheus/client_golang)) = 1.16.0
Provides:       bundled(golang(github.com/prometheus/client_model)) = 0.4.0
Provides:       bundled(golang(github.com/prometheus/common)) = 0.44.0
Provides:       bundled(golang(github.com/prometheus/procfs)) = 0.10.1
Provides:       bundled(golang(github.com/russross/blackfriday/v2)) = 2.1.0
Provides:       bundled(golang(github.com/sirupsen/logrus)) = 1.9.3
Provides:       bundled(golang(github.com/spf13/pflag)) = 1.0.5
Provides:       bundled(golang(github.com/urfave/cli/v2)) = 2.26.0
Provides:       bundled(golang(github.com/xrash/smetrics)) = 039620a
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)) = 0.42.0
Provides:       bundled(golang(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)) = 0.44.0
Provides:       bundled(golang(go.opentelemetry.io/otel)) = 1.19.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace)) = 1.19.0
Provides:       bundled(golang(go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc)) = 1.19.0
Provides:       bundled(golang(go.opentelemetry.io/otel/metric)) = 1.19.0
Provides:       bundled(golang(go.opentelemetry.io/otel/sdk)) = 1.19.0
Provides:       bundled(golang(go.opentelemetry.io/otel/trace)) = 1.19.0
Provides:       bundled(golang(go.opentelemetry.io/proto/otlp)) = 1.0.0
Provides:       bundled(golang(golang.org/x/mod)) = 0.13.0
Provides:       bundled(golang(golang.org/x/net)) = 0.19.0
Provides:       bundled(golang(golang.org/x/oauth2)) = 0.10.0
Provides:       bundled(golang(golang.org/x/sys)) = 0.15.0
Provides:       bundled(golang(golang.org/x/term)) = 0.15.0
Provides:       bundled(golang(golang.org/x/text)) = 0.14.0
Provides:       bundled(golang(golang.org/x/time)) = 0.3.0
Provides:       bundled(golang(golang.org/x/tools)) = 0.14.0
Provides:       bundled(golang(google.golang.org/appengine)) = 1.6.7
Provides:       bundled(golang(google.golang.org/genproto/googleapis/api)) = 23370e0
Provides:       bundled(golang(google.golang.org/genproto/googleapis/rpc)) = b8732ec
Provides:       bundled(golang(google.golang.org/grpc)) = 1.58.3
Provides:       bundled(golang(google.golang.org/protobuf)) = 1.31.0
Provides:       bundled(golang(gopkg.in/inf.v0)) = 0.9.1
Provides:       bundled(golang(gopkg.in/yaml.v2)) = 2.4.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = 3.0.1
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/api)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/apiextensions-apiserver)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/apimachinery)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/apiserver)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/cli-runtime)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/client-go)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/component-base)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/cri-api)) = e4636d0
Provides:       bundled(golang(k8s.io/klog/v2)) = 2.110.1
Provides:       bundled(golang(k8s.io/kube-openapi)) = 2dd684a
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kubectl)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kubelet)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes)) = 1.29.0-rc.2
Provides:       bundled(golang(k8s.io/utils)) = 3b25d92
Provides:       bundled(golang(sigs.k8s.io/json)) = bc3834c
Provides:       bundled(golang(sigs.k8s.io/structured-merge-diff/v4)) = 4.4.1
Provides:       bundled(golang(sigs.k8s.io/yaml)) = 1.4.0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/api)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/apiextensions-apiserver)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/apimachinery)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/apiserver)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/cli-runtime)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/client-go)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/cloud-provider)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/cluster-bootstrap)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/code-generator)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/component-base)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/component-helpers)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/controller-manager)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/cri-api)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/csi-translation-lib)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/dynamic-resource-allocation)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/endpointslice)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kms)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kube-aggregator)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kube-controller-manager)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kube-proxy)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kube-scheduler)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kubectl)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/kubelet)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes)) = 1.29.0-rc.2
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/legacy-cloud-providers)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/metrics)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/mount-utils)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/pod-security-admission)) = e4636d0
Provides:       bundled(golang(k8s.io/kubernetes/staging/src/k8s.io/sample-apiserver)) = e4636d0

%description
%{summary}.

%prep
%autosetup -p1

%build
%global gomodulesmode GO111MODULE=on
# Exporting %%{gomodulesmode} is only necessary on RHEL 8 and below
export %{gomodulesmode}
export GOFLAGS="-mod=vendor"
export BUILDTAGS="selinux seccomp"

%gobuild -o bin/crictl %{import_path}/cmd/crictl
go-md2man -in docs/crictl.md -out docs/crictl.1

%install
# install binaries
install -dp %{buildroot}%{_bindir}
install -p -m 755 ./bin/crictl %{buildroot}%{_bindir}

# install manpage
install -dp %{buildroot}%{_mandir}/man1
install -p -m 644 docs/crictl.1 %{buildroot}%{_mandir}/man1

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md OWNERS README.md RELEASE.md code-of-conduct.md
%doc docs/{benchmark.md,roadmap.md,validation.md}
%{_bindir}/crictl
%{_mandir}/man1/crictl*.1*

%changelog
* Thu Jan 25 2024 Bradley G Smith <bradley.g.smith@gmail.com> - 1.29.0-1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Maxwell G <gotmax@e.email> - 1.24.2-1
- Update to 1.24.2.
- Fix FTBFS
- Fix incorrect overriding of %%gobuild.
- Update to new upstream URL
- Handle new go.mod vendoring

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-9.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-8.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-7.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-6.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-5.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-4.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-3.dev.git19b7255
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.11.0-2.dev.git19b7255
- autobuilt 19b7255

* Tue Jul 17 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.11.0-1.dev.gitf95ba2f
- bump to v1.11.0
- built f95ba2f

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - version.Versionversion.Version-2.git41d6c4a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - version.Versionversion.Version-1.git41d6c4a1
- bump to version.Version
- autobuilt 41d6c4a

* Fri Jun 29 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - crictlVersion-3.git3bf77bf
- autobuilt 3bf77bf

* Wed Jun 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - crictlVersion-2.git012eea1
- autobuilt 012eea1

* Tue Jun 19 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - crictlVersion-1.git78ec590
- bump to crictlVersion
- autobuilt 78ec590

* Sat Jun 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-26.git9c667f5
- autobuilt 9c667f5

* Fri Jun 15 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-25.gitc38159e
- autobuilt c38159e

* Fri Jun 08 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-24.git9da2549
- autobuilt 9da2549

* Sun May 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-23.giteae53b2
- autobuilt eae53b2

* Fri May 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-22.gitc58160c
- autobuilt c58160c

* Fri May 18 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-21.gitb2cb253
- autobuilt b2cb253

* Wed May 09 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-20.git6ae7b25
- autobuilt 6ae7b25

* Tue May 08 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-19.gited19775
- autobuilt ed19775

* Fri May 04 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-18.git585e558
- autobuilt 585e558

* Wed May 02 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-17.git49847ed
- autobuilt commit 49847ed

* Fri Apr 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-16.git34ce008
- autobuilt commit 34ce008

* Tue Apr 24 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-15.git0dca09b
- autobuilt commit 0dca09b

* Sat Apr 21 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-14.gitf37a5a1
- autobuilt commit f37a5a1

* Thu Apr 19 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-13.gitdb53d78
- autobuilt commit db53d78

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-12.gitf6ed14e
- autobuilt commit f6ed14e

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-11.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-10.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-9.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-8.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-7.gitf6ed14e
- autobuilt commit f6ed14e

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 1.0.0-6.gitf6ed14e
- autobuilt commit f6ed14e

* Fri Apr 06 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-5.gitf6ed14e
- built commit f6ed14e

* Mon Mar 26 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-4.git207e773
- built commit 207e773

* Mon Mar 26 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-3.git653cc8c
- disable critest cause PITA to build

* Wed Feb 07 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-2.alpha.0.git653cc8c
- include critest binary

* Wed Feb 07 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1.0.0-1.alpha.0.gitf1a58d6
- First package for Fedora

