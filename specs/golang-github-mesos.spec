# Generated by go2rpm
# flaky tests, only try on one arch
%ifarch x86_64
%global debug_package %{nil}

%bcond_without check
%endif

# https://github.com/mesos/mesos-go
%global goipath         github.com/mesos/mesos-go
Version:                0.0.11

%gometa

%global common_description %{expand:
Pure Go language bindings for Apache Mesos, under development. As with other
pure implementations, mesos-go uses the HTTP wire protocol to communicate
directly with a running Mesos master and its slave instances. One of the
objectives of this project is to provide an idiomatic Go API that makes it super
easy to create Mesos frameworks using Go.}

%global golicenses      LICENSE NOTICE
%global godocs          CONTRIBUTING.md DESIGN.md README.md CHANGELOG\\\
                        examples

Name:           %{goname}
Release:        %autorelease
Summary:        Go language bindings for Apache Mesos

# Upstream license specification: BSD-3-Clause and Apache-2.0 and MIT
# Automatically converted from old format: BSD and ASL 2.0 and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Apache-2.0 AND LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gogo/protobuf/gogoproto)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/gogo/protobuf/sortkeys)
BuildRequires:  golang(github.com/gogo/protobuf/types)
BuildRequires:  golang(github.com/golang/glog)
BuildRequires:  golang(github.com/pborman/uuid)
BuildRequires:  golang(github.com/pquerna/ffjson/fflib/v1)
BuildRequires:  golang(github.com/prometheus/client_golang/prometheus)
BuildRequires:  golang(github.com/samuel/go-zookeeper/zk)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/mock)
BuildRequires:  golang(golang.org/x/net/context)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/gogo/protobuf/jsonpb)
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
%gocheck -d api/v0/upid
%endif

%gopkgfiles

%changelog
%autochangelog