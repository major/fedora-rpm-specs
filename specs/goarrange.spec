# Generated by go2rpm 1.10.0
%bcond_without check

# https://github.com/jdeflander/goarrange
%global goipath         github.com/jdeflander/goarrange
Version:                1.0.0

%gometa -L -f

%global common_description %{expand:
Automatic arrangement of Go source code.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           goarrange
Release:        %autorelease
Summary:        Automatic arrangement of Go source code

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
%gobuild -o %{gobuilddir}/bin/goarrange %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
