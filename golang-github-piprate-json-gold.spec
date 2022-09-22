%bcond_with check

# https://github.com/piprate/json-gold
%global goipath         github.com/piprate/json-gold
Version:                0.4.1

%gometa

%global common_description %{expand:
A JSON-LD processor for Go.}

%global golicenses      LICENSE
%global godocs          examples CONTRIBUTORS.md README.md CHANGELOG.md

Name:           %{goname}
Release:        %autorelease
Summary:        JSON-LD processor

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/pquerna/cachecontrol)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog


