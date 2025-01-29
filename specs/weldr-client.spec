# Pass --without tests to skip building composer-cli-tests
%bcond_without tests
# Pass --without signed to skip gpg signed tar.gz (DO NOT DO THAT IN PRODUCTION)
%bcond_without signed

%global goipath         github.com/osbuild/weldr-client/v2

Name:      weldr-client
Version:   35.14
Release:   3%{?dist}
# Upstream license specification: Apache-2.0
License:   Apache-2.0
Summary:   Command line utility to control osbuild-composer

%gometa
Url:       %{gourl}
Source0:   https://github.com/osbuild/weldr-client/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if %{with signed}
Source1:   https://github.com/osbuild/weldr-client/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:   https://keys.openpgp.org/vks/v1/by-fingerprint/117E8C168EFE3A7F#/gpg-117E8C168EFE3A7F.key
%endif

Patch0001: 0001-Fix-non-constant-log-strings.patch

Obsoletes: composer-cli < 35.0
Provides: composer-cli = %{version}-%{release}

Requires: diffutils

BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
%if 0%{?fedora}
BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/spf13/cobra)
# Required for tests and %check
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

BuildRequires: git-core
BuildRequires: make
BuildRequires: gnupg2


%description
Command line utility to control osbuild-composer

%prep
%if %{with signed}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%if 0%{?rhel}
%forgeautosetup -p1
%else
%goprep
%autopatch -p1
%endif

%build
export LDFLAGS="-X %{goipath}/cmd/composer-cli/root.Version=%{version} "

%if 0%{?rhel}
GO_BUILD_PATH=$PWD/_build
install -m 0755 -vd $(dirname $GO_BUILD_PATH/src/%{goipath})
ln -fs $PWD $GO_BUILD_PATH/src/%{goipath}
cd $GO_BUILD_PATH/src/%{goipath}
install -m 0755 -vd _bin
export PATH=$PWD/_bin${PATH:+:$PATH}
export GOPATH=$GO_BUILD_PATH:%{gopath}
export GOFLAGS=-mod=vendor
%else
export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"
export GO111MODULE=off
%endif
%gobuild -o composer-cli %{goipath}/cmd/composer-cli


## TODO
##make man

%if %{with tests} || 0%{?rhel}
export BUILDTAGS="integration"

# Build test binaries with `go test -c`, so that they can take advantage of
# golang's testing package. The RHEL golang rpm macros don't support building them
# directly. Thus, do it manually, taking care to also include a build id.
#
# On Fedora go modules have already been turned off, and the path set to the one into which
# the golang-* packages install source code.
export LDFLAGS="${LDFLAGS:-} -linkmode=external -compressdwarf=false -B 0x$(od -N 20 -An -tx1 -w100 /dev/urandom | tr -d ' ')"
go test -c -tags=integration -buildmode pie -compiler gc -ldflags="${LDFLAGS}" -o composer-cli-tests %{goipath}/weldr
%endif

%install
make DESTDIR=%{buildroot} install

%if %{with tests} || 0%{?rhel}
make DESTDIR=%{buildroot} install-tests
%endif

%check
%if 0%{?fedora}
export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"
export GO111MODULE=off
%endif

# Run the unit tests
export LDFLAGS="-X %{goipath}/cmd/composer-cli/root.Version=%{version} "
make test


%files
%license LICENSE
%doc examples HACKING.md README.md
%{_bindir}/composer-cli
%dir %{_sysconfdir}/bash_completion.d
%{_sysconfdir}/bash_completion.d/composer-cli
%{_mandir}/man1/composer-cli*

%if %{with tests} || 0%{?rhel}
%package tests
Summary:    Integration tests for composer-cli

Requires: createrepo_c

%description tests
Integration tests to be run on a pristine-dedicated system to test the
composer-cli package.

%files tests
%license LICENSE
%{_libexecdir}/tests/composer-cli/
%endif


%changelog
* Mon Jan 27 2025 Brian C. Lane <bcl@redhat.com> - 35.14-3
- Fix non-constant log strings
  Resolves: rhbz#2341535

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 35.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Brian C. Lane <bcl@redhat.com> - 35.14-1
- New release: 35.14 (bcl)
- tests: Remove openstack (bcl)
- readme: project links (lukas)
- Makefile: implement "fully source containers" HMS-3883 (florian.schueller)
- README: fix anchor typo (florian.schueller)
- README: fix compatibility with docusaurus (florian.schueller)
- go.mod: Use go 1.21 (bcl)
- workflows: Use go 1.21.x for govuln tests (bcl)
- build(deps): bump github.com/spf13/cobra from 1.8.0 to 1.8.1 (49699333+dependabot[bot])
- build(deps): bump github.com/BurntSushi/toml from 1.3.2 to 1.4.0 (49699333+dependabot[bot])
- Makefile: dnf5 builddep accepts .spec files without --spec (bcl)
- Containerfile: Install dnf5-plugins for builddep support (bcl)
- bash: Add status show to bash completion (bcl)
- go.mod: Use go 1.20 (bcl)
- bash: Add wait command to bash completion (bcl)
