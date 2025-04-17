%bcond_without check

%global debug_package %{nil}

# https://github.com/yuin/goldmark
%global goipath         github.com/yuin/goldmark
Version:                1.7.10

%gometa -L

%global common_description %{expand:
A markdown parser written in Go. Easy to extend, standard(CommonMark)
compliant, well structured.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-yuin-goldmark
Release:        %autorelease
Summary:        Markdown parser written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%install
%gopkginstall

%if %{with check}
%check
%ifarch aarch64 %{ix86} riscv64
export GOLDMARK_TEST_TIMEOUT_MULTIPLIER=10
%endif
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
