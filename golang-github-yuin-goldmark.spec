%bcond_without check

# https://github.com/yuin/goldmark
%global goipath         github.com/yuin/goldmark
Version:                1.5.6

%gometa

%global common_description %{expand:
A markdown parser written in Go. Easy to extend, standard(CommonMark)
compliant, well structured.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Markdown parser written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%install
%gopkginstall

%if %{with check}
%check
%ifarch aarch64 %{ix86}
export GOLDMARK_TEST_TIMEOUT_MULTIPLIER=6
%endif
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
