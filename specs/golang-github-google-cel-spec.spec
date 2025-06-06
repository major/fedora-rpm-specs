# Generated by go2rpm 1.7.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/google/cel-spec
%global goipath         github.com/google/cel-spec
Version:                0.7.0

%gometa

%global common_description %{expand:
The Common Expression Language (CEL) implements common semantics for expression
evaluation, enabling different applications to more easily interoperate.}

%global golicenses      LICENSE
%global godocs          doc CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md\\\
                        MAINTAINERS.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Common Expression Language, specification and binary representation

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck -d tests/envcheck -d tests/simple
%endif

%gopkgfiles

%changelog
%autochangelog
