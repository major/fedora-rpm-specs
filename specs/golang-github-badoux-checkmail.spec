# Generated by go2rpm 1.3
%bcond_without check
%bcond_with network
%global debug_package %{nil}


# https://github.com/badoux/checkmail
%global goipath         github.com/badoux/checkmail
Version:                1.2.1

%gometa

%global common_description %{expand:
Golang package for email validation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Golang package for email validation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%if %{without network}
%global gotestflags %{?gotestflags} -run TestValidateFormat
%endif
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
