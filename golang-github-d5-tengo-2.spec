%bcond_without check

# https://github.com/d5/tengo
%global goipath         github.com/d5/tengo/v2
Version:                2.10.1

%gometa

%global common_description %{expand:
A fast script language for Go.}

%global golicenses      LICENSE
%global godocs          docs examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Fast script language for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/tengo %{goipath}/cmd/tengo

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc docs examples README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog

