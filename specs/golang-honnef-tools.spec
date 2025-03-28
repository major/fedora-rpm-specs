# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/dominikh/go-tools
%global goipath         honnef.co/go/tools
%global forgeurl        https://github.com/dominikh/go-tools
Version:                2023.1.3
%global commit          0e3cc2963b37ac5d3fb66a4d9cb9dcfadbd4e21d

%gometa

%global common_description %{expand:
Staticcheck - The advanced Go linter.}

%global golicenses      LICENSE-THIRD-PARTY LICENSE LICENSE-gcsizes\\\
                        LICENSE-ir
%global godocs          doc README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Staticcheck - The advanced Go linter

License:        BSD-3-Clause AND MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
mv go/gcsizes/LICENSE LICENSE-gcsizes
mv go/ir/LICENSE LICENSE-ir

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
%ifarch s390x
for test in "TestAll" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif

%files
%license LICENSE-THIRD-PARTY LICENSE LICENSE-gcsizes LICENSE-ir
%doc doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
