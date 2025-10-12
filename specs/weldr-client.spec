# Pass --without tests to skip building composer-cli-tests
%bcond_without tests
# Pass --without signed to skip gpg signed tar.gz (DO NOT DO THAT IN PRODUCTION)
%bcond_without signed

%global goipath         github.com/osbuild/weldr-client/v2

Name:      weldr-client
Version:   36.0
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

Patch0001: 0001-tests-Skip-checking-arch-when-testing-sent-body.patch

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
* Fri Oct 10 2025 Alejandro Sáez <asm@redhat.com> - 36.0-3
- rebuild

* Fri Aug 15 2025 Maxwell G <maxwell@gtmx.me> - 36.0-2
- Rebuild for golang-1.25.0

* Thu Aug 14 2025 Brian C. Lane <bcl@redhat.com> - 36.0-1
- tests: Skip checking arch when testing sent body
- New release: 36.0 (bcl)
- golangci: Disable linting for a few things (bcl)
- test: Remove unneeded fmt.Sprintf (bcl)
- lint: Clean up lint errcheck errors (bcl)
- workflows: Update to golangci-lint 2.3.0 (bcl)
- workflows: Update to use go 1.23 and drop 1.21 and 1.22 (bcl)
- GHA: enable the stale action to delete its saved state (thozza)
- composer-cli: Add cloudapi support to delete command (bcl)
- cloud: Add DeleteCompose function and tests (bcl)
- cloud: Add DeleteRaw function and tests (bcl)
- tests: Fix TestComposeInfoCloud (bcl)
- cloud: Handle unexpected status codes (bcl)
- composer-cli: Add cloudapi support to compose image command (bcl)
- cloud: Add ComposeImagePath function (bcl)
- cloud: Add GetFilePath function to download an image file (bcl)
- common: Move part of GetFilePath into common.SaveResponseBodyToFile (bcl)
- composer-cli: Add size to the compose status cloud command (bcl)
- composer-cli: Add support for more cloudapi detail to compose list (bcl)
- composer-cli: Add cloudapi support to the compose info command (bcl)
- apischema: Add UploadTypes function to ComposeMetadataV1 (bcl)
- cloud: Add GetComposeMetadata function (bcl)
- common: Move blueprint struct to common (bcl)
- cloud: Move status mapping into a function (bcl)
- apischema: Move ComposeResponseV1 to apischema (bcl)
- apischema: Move Status to apischema (bcl)
- apischema: Move PackageDetails to apischema (bcl)
- apischema: Move ComposeInfo to apischema (bcl)
- apischema: Add a common location to define cloudapi structs (bcl)
- build(deps): bump github.com/BurntSushi/toml from 1.4.0 to 1.5.0 (49699333+dependabot[bot])
- compose: Add listing cloud composes to the status command (bcl)
- compose: Add listing cloud composes to the list command (bcl)
- cloud: Add test for ListComposes (bcl)
- cloud: Implement ListComposes to return cloudapi compose info (bcl)
- projects: Add cloudapi support to depsolve command (bcl)
- blueprints: Add cloudapi support for depsolving local blueprint files (bcl)
- cloud: Add DepsolveBlueprint function (bcl)
- depsolve: Move parsing of weldr response into apischema (bcl)
- depsolve: Use common.PackageNEVRA (bcl)
- README.md: align with image-builder-cli (florian.schueller)
- projects: Add cloudapi support to the list command (bcl)
- projects: Add cloudapi support for project info command (bcl)
- cloud: Add SearchPackages function (bcl)
- composer-cli: Add a --weldr-only flag (bcl)
- tests: OSTree does not support the qcow2 image type (bcl)
- compose: Add cloudapi support to the compose types command (bcl)
- cloud: Add ComposeTypes function to return image types (bcl)
- common: Add SortedMapKeys helper (bcl)
- distros: Add cloudapi support to the list command (bcl)
- cloud: Add test for ListDistros (bcl)
- cloud: Add ListDistros function to return distro names (bcl)
- github/workflows/pr_best_practices: initial version (florian.schueller)
- common: PackageNEVRA JSON epoch field can be string or int (bcl)
- common: Move PackageNEVRA to common (bcl)
- common: Move GetHostDistroName to common (bcl)
- common: Refactor GetContentFilename (bcl)
- common: Refactor cloud common to use internal common functions (bcl)
- common: Create a common package to share functions (bcl)
- weldr: Function to check APIResponse for an error ID (bcl)
- build(deps): bump github.com/spf13/cobra from 1.8.1 to 1.9.1 (49699333+dependabot[bot])
- cloud: Make the test bool private (bcl)
- compose: Return an error when opening a file (bcl)
- cloud: Add tests for ComposeWait function (bcl)
- compose: Add cloud API --wait to start command (bcl)
- compose: Add support for cloud API UUIDs to compose wait (bcl)
- cloud: Add ComposeWait function (bcl)
- cloud: Add test for ComposeInfo (bcl)
- cloud: Add ComposeInfo function (bcl)
- compose: Remove redundant 'Error' from error strings in start (bcl)
- compose: Add upload handling for cloud (bcl)
- cloud: Add support for passing upload options (bcl)
- compose: Add ability to use a local blueprint to start a compose (bcl)
- cloud: Add StartCompose function (bcl)
- cloud: Add ServerStatus function (bcl)
- status: Add cloudapi status to show command (bcl)
- Makefile: Pass VERSION into build container (bcl)
- cmd: Add cloudapi client (bcl)
- cloud: Add basic Client functions for cloud api (bcl)
- go.mod: Upgrade modules to current versions (bcl)
- go.mod: Bump go version to 1.22.6 (bcl)
- tools: Use go toolbox in prepare-source.sh (bcl)
- Fix non-constant log strings (bcl)
- Bump testify version to 1.10.0 (bcl)
