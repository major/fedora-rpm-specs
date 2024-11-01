# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/awslabs/aws-go-multi-module-repository-tools
%global goipath         github.com/awslabs/aws-go-multi-module-repository-tools
%global commit          b6ea8596afb401d42d28ccb2b8dadb20b4847fa7

%gometa -f

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE LICENSE.txt NOTICE
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        None

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

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
%license LICENSE LICENSE.txt NOTICE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
