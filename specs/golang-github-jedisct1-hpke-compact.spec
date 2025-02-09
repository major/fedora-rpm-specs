# Generated by go2rpm 1.5.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/jedisct1/go-hpke-compact
%global goipath         github.com/jedisct1/go-hpke-compact
Version:                0.9.0
%global tag             0.9.0

%gometa

%global common_description %{expand:
A small and easy to use HPKE implementation in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Small and easy to use HPKE implementation in Go

License:        ISC
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/chacha20poly1305)
BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/crypto/hkdf)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/powerman/check)
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
