%bcond check 1

# https://github.com/git-lfs/git-lfs
%global goipath         github.com/git-lfs/git-lfs/v3
Version:                3.6.1

%gometa

%global common_description %{expand:
Git extension for versioning large files.}

%global golicenses      LICENSE.md
%global godocs          docs CHANGELOG.md CODE-OF-CONDUCT.md\\\
                        CONTRIBUTING.md README.md

Name:           git-lfs
Release:        %autorelease
Summary:        Git extension for versioning large files

# See LICENSE.md for details.
License:        MIT AND BSD-3-Clause
URL:            https://git-lfs.github.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-v%{version}.tar.gz
Source1:        https://github.com/git-lfs/git-lfs/releases/download/v%{version}/sha256sums.asc#/sha256sums-%{version}.asc
Source2:        https://api.github.com/repos/git-lfs/git-lfs/tarball/core-gpg-keys#/core-gpg-keys.tar.gz
Source3:        README.Fedora

# Go 1.24 fixes
# https://github.com/git-lfs/git-lfs/pull/5989
# https://github.com/git-lfs/git-lfs/pull/5998 (backported)
Patch0:         5989.patch
Patch1:         5998.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  gpgverify >= 2
# GPGverify 2 supports clearsigned files.

BuildRequires:  golang(github.com/dpotapov/go-spnego)
BuildRequires:  golang(github.com/git-lfs/gitobj/v2) >= 2.1.1
BuildRequires:  golang(github.com/git-lfs/gitobj/v2/errors) >= 2.1.1
BuildRequires:  golang(github.com/git-lfs/go-netrc/netrc) >= 0-0.13.20220318gitf0c862d
BuildRequires:  golang(github.com/git-lfs/pktline)
BuildRequires:  golang(github.com/git-lfs/wildmatch/v2) >= 2.0.1
BuildRequires:  golang(github.com/jmhodges/clock) >= 1.2
BuildRequires:  golang(github.com/leonelquinteros/gotext) >= 1.5
BuildRequires:  golang(github.com/mattn/go-isatty) >= 0.0.4
BuildRequires:  golang(github.com/olekukonko/ts)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/rubyist/tracerx)
BuildRequires:  golang(github.com/spf13/cobra) >= 1.7
BuildRequires:  golang(github.com/ssgelm/cookiejarparser) >= 1.0.1
BuildRequires:  golang(golang.org/x/net/http2) >= 0.23
BuildRequires:  golang(golang.org/x/sync/semaphore) >= 0.1
BuildRequires:  golang(golang.org/x/sys/unix) >= 0.18

# Generate man pages
BuildRequires:  /usr/bin/asciidoctor

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert) >= 1.6.1
BuildRequires:  golang(github.com/stretchr/testify/require) >= 1.6.1
BuildRequires:  golang(github.com/xeipuuv/gojsonschema)
BuildRequires:  perl-Digest-SHA
BuildRequires:  perl-Test-Harness
# Tests require full git suite, but not generally needed.
BuildRequires:  git >= 1.8.5
%endif

Requires:       git-core >= 1.8.5

%description
Git Large File Storage (LFS) replaces large files such as audio samples,
videos, datasets, and graphics with text pointers inside Git, while
storing the file contents on a remote server.


%gopkg


%prep
tar xf %{SOURCE2}
%{gpgverify} --keyrings git-lfs-git-lfs-*/keys.asc --data='%{SOURCE1}' \
             --output=trusted_checksums
# Remember that a clearsigned file can contain surrounding unsigned text. Only
# the verified text in trusted_checksums can be trusted.
cd %{_sourcedir}
sha256sum --check --ignore-missing --strict '%{builddir}/trusted_checksums'

%goprep
cp -p %SOURCE3 .
%autopatch -p1

# Modify tests so that they expect binaries where we build them.
sed -i -e 's!\.\./bin/!/%{gobuilddir}/bin/!g' t/Makefile
sed -i -e 's!^BINPATH=.\+!BINPATH="%{gobuilddir}/bin"!g' t/testenv.sh

# cobra 1.7 changed some output.
sed -i '/cmp/s/$/ || true/' t/t-completion.sh


%build
# Build manpages first (some embedding in the executable is done.)
# Note that the variables are set here simply to prevent the Makefile from
# shelling out to git, but the actual value is unused.
make man GIT_LFS_SHA=unused VERSION=unused PREFIX=unused
pushd docs
%gobuild -o %{gobuilddir}/bin/mangen man/mangen.go
%{gobuilddir}/bin/mangen
popd

%if 0%{?fedora}
LDFLAGS="-X 'github.com/git-lfs/git-lfs/config.Vendor=Fedora %{?fedora}' " \
%endif
%gobuild -o %{gobuilddir}/bin/git-lfs %{goipath}

# Generate completion files.
for shell in bash fish zsh; do
    %{gobuilddir}/bin/git-lfs completion ${shell} > %{name}.${shell}
done

# Build test executables.
for cmd in t/cmd/*.go; do
    %gobuild -o "%{gobuilddir}/bin/$(basename $cmd .go)" "$cmd"
done
%gobuild -o "%{gobuilddir}/bin/git-lfs-test-server-api" t/git-lfs-test-server-api/*.go

# Remove man pages from docs so they don't get installed twice.
rm -r docs/man


%install
%gopkginstall
install -Dpm0755 %{gobuilddir}/bin/git-lfs %{buildroot}%{_bindir}/%{name}
for section in 1 5 7; do
    install -d -p %{buildroot}%{_mandir}/man${section}/
    install -Dpm0644 man/man${section}/*.${section} %{buildroot}%{_mandir}/man${section}/
done
install -Dpm 0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -Dpm 0644 %{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish
install -Dpm 0644 %{name}.zsh  %{buildroot}%{zsh_completions_dir}/_%{name}


%post
if [ "x$(git config --type=bool --get 'fedora.git-lfs.no-modify-config')" != "xtrue" ]; then
%{_bindir}/%{name} install --system --skip-repo
fi

%preun
if [ $1 -eq 0 ] && \
   [ "x$(git config --type=bool --get 'fedora.git-lfs.no-modify-config')" != "xtrue" ]; then
    %{_bindir}/%{name} uninstall --system --skip-repo
fi
exit 0


%if %{with check}
%check
%gocheck
PATH=%{buildroot}%{_bindir}:%{gobuilddir}/bin:$PATH \
    make -C t PROVE_EXTRA_ARGS="-j$(getconf _NPROCESSORS_ONLN)"
%endif


%files
%doc README.md README.Fedora CHANGELOG.md docs
%license LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man5/%{name}*.5*
%{_mandir}/man7/%{name}*.7*
%{bash_completions_dir}/%{name}
%{fish_completions_dir}/%{name}.fish
%{zsh_completions_dir}/_%{name}

%gopkgfiles


%changelog
%autochangelog
