# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/kubernetes/api
%global goipath         k8s.io/api
%global forgeurl        https://github.com/kubernetes/api
Version:                1.22.0
%global tag             kubernetes-1.22.0
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
Schema of the external API types that are served by the Kubernetes API server.}

%global golicenses      LICENSE
%global godocs          code-of-conduct.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Canonical location of the Kubernetes API definition

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(k8s.io/apimachinery/pkg/api/resource)
BuildRequires:  golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires:  golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires:  golang(k8s.io/apimachinery/pkg/types)
BuildRequires:  golang(k8s.io/apimachinery/pkg/util/intstr)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
