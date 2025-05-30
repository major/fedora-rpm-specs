# Generated by go2rpm 1.15.0
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/oras-project/oras
%global goipath         oras.land/oras
%global forgeurl        https://github.com/oras-project/oras
Version:                1.2.2

%gometa -L -f

%global common_description %{expand:
Work with OCI registries, but for secure supply chain - managing content like
artifacts, images, SBOM.}

%global golicenses      LICENSE
%global godocs          docs CODE_OF_CONDUCT.md CONTRIBUTING.md\\\
                        MAINTAINERS.md OWNERS.md README.md SECURITY.md

Name:           golang-oras
Release:        %autorelease
Summary:        OCI registry client - managing content like artifacts, images, packages

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  golang(oras.land/oras-go/v2)

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

# Remove e2e tests
rm -rf test/e2e

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%if %{without bootstrap}
%files
%license LICENSE
%doc docs CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md OWNERS.md README.md
%doc SECURITY.md
%{_bindir}/oras
%endif

%gopkgfiles

%changelog
%autochangelog
