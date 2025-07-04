# Generated by go2rpm 1.11.1
%bcond_without check

# https://github.com/goccy/go-yaml
%global goipath         github.com/goccy/go-yaml
Version:                1.18.0

%gometa -L -f

%global common_description %{expand:
Go package similar to github.com/go-yaml/yaml with some additional
features.}

%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md

Name:           golang-github-goccy-yaml
Release:        %autorelease
Summary:        YAML support for the Go language

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
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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
%doc README.md CHANGELOG.md
%{_bindir}/ycat

%gopkgfiles

%changelog
%autochangelog
