# Generated by go2rpm 1.10.0
%bcond_without check

# https://github.com/uber/athenadriver
%global goipath         github.com/uber/athenadriver
Version:                1.1.15

%gometa -L -f

%global common_description %{expand:
A fully-featured AWS Athena database driver.}

%global golicenses      LICENSE
%global godocs          examples ChangeLog.txt README.md

Name:           golang-github-uber-athenadriver
Release:        %autorelease
Summary:        A fully-featured AWS Athena database driver

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/athenareader %{goipath}/athenareader

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/athenareader %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc examples ChangeLog.txt README.md
%{_bindir}/athenareader

%gopkgfiles

%changelog
%autochangelog
