# Generated by go2rpm 1.12.0
# https://github.com/kubernetes-sigs/yaml/issues/23
# https://github.com/kubernetes-sigs/yaml/issues/34
%ifnarch i686
%bcond_without check
%endif
%global debug_package %{nil}

# https://github.com/kubernetes-sigs/yaml
%global goipath         sigs.k8s.io/yaml
%global forgeurl        https://github.com/kubernetes-sigs/yaml
Version:                1.4.0

%gometa -L

%global common_description %{expand:
A wrapper around go-yaml designed to enable a better way of handling YAML when
marshaling to and from structs.

In short, this library first converts YAML to JSON using go-yaml and then uses
json.Marshal and json.Unmarshal to convert to or from the struct. This means
that it effectively reuses the JSON struct tags as well as the custom JSON
methods MarshalJSON and UnmarshalJSON unlike go-yaml.}

%global golicenses      LICENSE goyaml.v2-LICENSE goyaml.v2-LICENSE.libyaml\\\
                        goyaml.v2-NOTICE goyaml.v3-LICENSE goyaml.v3-NOTICE
%global godocs          CONTRIBUTING.md README.md RELEASE.md

Name:           golang-sigs-k8s-yaml
Release:        %autorelease
Summary:        Marshal and unmarshal YAML in Go

License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

mv goyaml.v2/LICENSE goyaml.v2-LICENSE
mv goyaml.v2/LICENSE.libyaml goyaml.v2-LICENSE.libyaml
mv goyaml.v2/NOTICE goyaml.v2-NOTICE
mv goyaml.v3/LICENSE goyaml.v3-LICENSE
mv goyaml.v3/NOTICE goyaml.v3-NOTICE

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog