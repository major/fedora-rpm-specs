# Generated by go2rpm 1.8.0
%bcond_without check

# https://gitlab.com/cznic/golex
%global goipath         modernc.org/golex
%global forgeurl        https://gitlab.com/cznic/golex
Version:                1.0.1
%global tag             v1.0.1

%gometa

%global common_description %{expand:
A lex/flex like (not fully POSIX lex compatible) utility.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS CONTRIBUTORS README

Name:           %{goname}
Release:        %autorelease
Summary:        A lex/flex like (not fully POSIX lex compatible) utility

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/golex %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
rm -rfv lex/example_test.go
%gocheck
%endif

%files
%license LICENSE
%doc examples AUTHORS CONTRIBUTORS README
%{_bindir}/golex

%gopkgfiles

%changelog
%autochangelog