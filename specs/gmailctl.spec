# Generated by go2rpm 1.6.0
%bcond_without check

%global goname          gmailctl

# https://github.com/mbrt/gmailctl
%global goipath         github.com/mbrt/gmailctl
Version:                0.11.0

%gometa

%global common_description %{expand:
Declarative configuration for Gmail filters.}

%global golicenses      LICENSE
%global godocs          docs README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Declarative configuration for Gmail filters, stored locally

# Upstream license specification: BSD-3-Clause and MIT
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

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
%license LICENSE
%doc docs README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog
