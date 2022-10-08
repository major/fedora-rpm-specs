%bcond_without check

# https://github.com/vultr/vultr-cli
%global goipath         github.com/vultr/vultr-cli
Version:                2.15.0

%gometa

%global common_description %{expand:
Official command line tool for Vultr services.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md CONTRIBUTING.md README.md

Name:           vultr-cli
Release:        %autorelease
Summary:        Official command line tool for Vultr services
# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  go-rpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/vultr-cli %{goipath}

# Build shell completions.
for SHELL in bash fish zsh; do
    VULTR_API_KEY=null %{gobuilddir}/bin/%{name} completion $SHELL > %{name}.${SHELL}
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
%license %{golicenses}
%doc %{godocs}
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
