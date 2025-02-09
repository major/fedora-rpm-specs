# Generated by go2rpm 1.8.1
%if 0%{?__isa_bits} != 32
%bcond_without check
%endif
%global debug_package %{nil}

# https://github.com/go-yaml/yaml
%global goipath         gopkg.in/yaml.v3
%global forgeurl        https://github.com/go-yaml/yaml
Version:                3.0.1

%gometa

%global common_description %{expand:
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within Canonical as part of the juju project, and is
based on a pure Go port of the well-known libyaml C library to parse and
generate YAML data quickly and reliably.

The yaml package supports most of YAML 1.2, but preserves some behavior from 1.1
for backwards compatibility.

Specifically, as of v3 of the yaml package:

 - YAML 1.1 bools (yes/no, on/off) are supported as long as they are being
   decoded into a typed bool value. Otherwise they behave as a string. Booleans
   in YAML 1.2 are true/false only.
 - Octals encode and decode as 0777 per YAML 1.1, rather than 0o777 as specified
   in YAML 1.2, because most parsers still use the old format. Octals in the
   0o777 format are supported though, so new files work.
 - Does not support base-60 floats. These are gone from YAML 1.2, and were
   actually never supported by this package as it's clearly a poor choice.

and offers backwards compatibility with YAML 1.1 in some cases. 1.2, including
support for anchors, tags, map merging, etc. Multi-document unmarshalling is not
yet implemented, and base-60 floats from YAML 1.1 are purposefully not supported
since they're a poor design and are gone in YAML 1.2.}

%global golicenses      LICENSE NOTICE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        YAML support for the Go language

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  golang(gopkg.in/check.v1)

%description %{common_description}

%gopkg

%prep
%goprep

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
