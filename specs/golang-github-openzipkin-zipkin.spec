# Generated by go2rpm
# Needs network
%bcond_with check
%global debug_package %{nil}


# https://github.com/openzipkin/zipkin-go
%global goipath         github.com/openzipkin/zipkin-go
Version:                0.2.5

%gometa

%global common_description %{expand:
Zipkin Go is the official Go Tracer implementation for Zipkin, supported by the
OpenZipkin community.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Zipkin tracer library for Go

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/Shopify/sarama)
BuildRequires:  golang(github.com/streadway/amqp)
BuildRequires:  golang(google.golang.org/grpc)
BuildRequires:  golang(google.golang.org/grpc/codes)
BuildRequires:  golang(google.golang.org/grpc/metadata)
BuildRequires:  golang(google.golang.org/grpc/peer)
BuildRequires:  golang(google.golang.org/grpc/stats)
BuildRequires:  golang(google.golang.org/grpc/status)
BuildRequires:  golang(google.golang.org/protobuf/proto)
BuildRequires:  golang(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  golang(google.golang.org/protobuf/runtime/protoimpl)

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
