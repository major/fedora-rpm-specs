%bcond_without check

# https://github.com/go-cmd/cmd
%global goipath         github.com/go-cmd/cmd
Version:                1.4.0

%gometa

%global common_description %{expand:
This package is a small but very useful wrapper around os/exec.Cmd for Linux
and macOS that makes it safe and simple to run external commands in highly
concurrent, asynchronous, real-time applications.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go library wrapper around os/exec.Cmd

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-test/deep)

%description %{common_description}

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
