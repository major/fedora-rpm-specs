%bcond_without check

# https://github.com/yuin/goldmark
%global goipath         github.com/yuin/goldmark
Version:                1.4.14

%gometa

%global common_description %{expand:
A markdown parser written in Go. Easy to extend, standard(CommonMark)
compliant, well structured.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Markdown parser written in Go
Patch0001:      0001-Increase-timeout-for-32-bit-builds.patch

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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
