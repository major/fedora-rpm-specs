# Generated by go2rpm
# Need Elasticsearch serve
%bcond_with check
%global debug_package %{nil}


# https://github.com/olivere/elastic
%global goipath         gopkg.in/olivere/elastic.v2
%global forgeurl        https://github.com/olivere/elastic
Version:                2.0.61

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-olivere-elastic-devel < 2.0.12-0.12
}

%global common_description %{expand:
Package Elastic provides an interface to the Elasticsearch server.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS\\\
                        ISSUE_TEMPLATE.md README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        %autorelease
Summary:        Elasticsearch client for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%if %{with check}
# Tests
BuildRequires:  golang(github.com/fortytw2/leaktest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
