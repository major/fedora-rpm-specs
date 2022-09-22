%bcond_without check

# https://github.com/graph-gophers/graphql-go
%global goipath         github.com/graph-gophers/graphql-go
Version:                1.3.0

%gometa

%global common_description %{expand:
GraphQL server with a focus on ease of use.}

%global golicenses      LICENSE
%global godocs          docs example CONTRIBUTING.md README.md CHANGELOG.md

Name:           %{goname}
Release:        %autorelease
Summary:        GraphQL server with a focus on ease of use

# Upstream license specification: BSD-3-Clause and BSD-2-Clause
License:        BSD and BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/opentracing/opentracing-go)
BuildRequires:  golang(github.com/opentracing/opentracing-go/ext)
BuildRequires:  golang(github.com/opentracing/opentracing-go/log)

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

