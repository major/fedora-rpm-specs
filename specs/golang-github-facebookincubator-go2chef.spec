# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/facebookincubator/go2chef
%global goipath         github.com/facebookincubator/go2chef
Version:                1.0
%global tag             1.0

%gometa

%global common_description %{expand:
go2chef is a Go tool for bootstrapping Chef installations in a flexible and
self-contained way. With go2chef, our goal is to make bootstrapping any node
in a Chef deployment as simple as "get go2chef onto a machine and run it".}

%global golicenses      LICENSE
%global godocs          examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Tool to bootstrap a system from zero so that it's able to run Chef

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%package -n go2chef
Summary:        %{summary}

%description -n go2chef
%{common_description}

%gopkg

%prep
%goprep
# these examples aren't useful without the repository itself
rm -r examples/{custom_binary,plugins}
# fix permissions
chmod -x examples/bundles/{chefctl,chefrepo}/bundle.ps1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/go2chef %{goipath}/bin
%gobuild -o %{gobuilddir}/bin/go2chef-remote %{goipath}/scripts

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files -n go2chef
%license LICENSE
%doc examples CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
