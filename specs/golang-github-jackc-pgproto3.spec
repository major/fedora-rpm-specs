# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/jackc/pgproto3
%global goipath         github.com/jackc/pgproto3
Version:                2.3.2

%gometa

%global goaltipaths     github.com/jackc/pgproto3/v2

%global common_description %{expand:
Package pgproto3 is a encoder and decoder of the PostgreSQL wire protocol
version 3.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Eencoder and decoder of the PostgreSQL wire protocol

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

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
