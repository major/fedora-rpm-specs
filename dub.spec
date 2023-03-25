%ifarch aarch64 armv7hl ppc64le
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           dub
Version:        1.31.1
Release:        %autorelease
Summary:        Package and build management system for D

License:        MIT
URL:            https://github.com/dlang/dub
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:  %{ldc_arches}

BuildRequires:  curl-devel
BuildRequires:  ldc

%description
DUB is a package and build manager for D applications and libraries.

%prep
%autosetup

%build
ldmd2 -run build.d %{_d_optflags}
./bin/dub scripts/man/gen_man.d

%install
install -Dpm0755 -t %{buildroot}%{_bindir} bin/dub
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 scripts/man/dub*.1
install -Dpm0644 scripts/bash-completion/dub.bash %{buildroot}%{_datadir}/bash-completion/completions/dub
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/completions scripts/fish-completion/dub.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions scripts/zsh-completion/_dub

%if %{with tests}
%check
# Compiler to use for the test suite
export DC=ldmd2
# Path to dub binary
export DUB="%{buildroot}%{_bindir}/dub"
# Some tests require dub in the system path
export PATH="%{buildroot}%{_bindir}:$PATH"
dub test
pushd test
# Neuter the test suite for now, as it depends on a lot of unpackaged modules
./run-unittest.sh || true
%endif

%files
%license LICENSE
%doc ARCHITECTURE.md CONTRIBUTING.md README.md
%doc architecture.png architecture.graphmlz
%doc examples
%{_bindir}/dub
%{_mandir}/man1/dub*.1*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/dub
%dir %{_datadir}/fish
%dir %{_datadir}/fish/completions
%{_datadir}/fish/completions/dub.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_dub

%changelog
%autochangelog
