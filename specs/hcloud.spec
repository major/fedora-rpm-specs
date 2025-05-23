# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/hetznercloud/cli
%global goipath         github.com/hetznercloud/cli
Version:                1.50.0

%gometa

%global common_description %{expand:
A command-line interface for Hetzner Cloud.}

%global golicenses      LICENSE
%global godocs          examples CHANGES.md README.md

Name:           hcloud
Release:        %autorelease
Summary:        A command-line interface for Hetzner Cloud

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

ExcludeArch:    %{ix86} ppc64le s390x

%description
%{common_description}

%gopkg

%prep
%goprep

# Upstream uses goreleaser to set the version, but we need to set it manually here.
sed 's/versionPrerelease = "dev"/versionPrerelease = ""/' -i internal/version/version.go

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

# Build shell completions.
for SHELL in bash fish zsh; do
    %{gobuilddir}/bin/%{name} completion $SHELL > %{name}.${SHELL}
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# Install shell completions.
install -Dp %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dp %{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dp %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}


%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc examples README.md
%{_bindir}/*
%{_datadir}/bash-completion/completions/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/zsh/site-functions/_%{name}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions

%gopkgfiles

%changelog
%autochangelog
