# Generated by go2rpm
# Needs Firefox for testing
%bcond_with check
%global debug_package %{nil}


# https://github.com/skratchdot/open-golang
%global goipath         github.com/skratchdot/open-golang
%global commit          eef8423979666925a58eb77f9db583e54320d5a4

%gometa

%global common_description %{expand:
Open a file, directory, or URI using the OS's default application for
that object type. Optionally, you can specify an application to use.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Open a file, directory, or URI using the OS's default application

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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
