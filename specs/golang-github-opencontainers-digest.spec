# Generated by go2rpm 1.8.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/opencontainers/go-digest
%global goipath         github.com/opencontainers/go-digest
Version:                1.0.0
%global commit          bde1400a84bededaf764144a72cbd007a633196e

%gometa

%global common_description %{expand:
Package Digest provides a generalized type to opaquely represent message digests
and their operations within the registry. The Digest type is designed to serve
as a flexible identifier in a content-addressable system. More importantly, it
provides tools and wrappers to work with hash.Hash-based digests with little
effort.}

%global golicenses      LICENSE.docs LICENSE.code
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Common digest package used across the container ecosystem

License:        Apache-2.0 and CC-BY-SA-4.0
URL:            %{gourl}
Source:         %{gosource}

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