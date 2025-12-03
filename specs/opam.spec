# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml/opam
%global testurl https://github.com/ocaml/opam-repository

Name:           opam
Version:        2.5.0
Release:        %autorelease
Summary:        Source-based package manager for OCaml

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://opam.ocaml.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/%{name}-full-%{version}.tar.gz
Source1:        %{giturl}/releases/download/%{version}/%{name}-full-%{version}.tar.gz.sig
Source2:        https://opam.ocaml.org/opam-dev-pubkey.pgp
# Files needed for testing.  See tests/reftests/dune.inc.
Source3:        %{testurl}/archive/0070613707.tar.gz
Source4:        %{testurl}/archive/009e00fa.tar.gz
Source5:        %{testurl}/archive/11ea1cb.tar.gz
Source6:        %{testurl}/archive/143dd2a2f59f5befbf3cb90bb2667f911737fbf8.tar.gz
Source7:        %{testurl}/archive/297366c.tar.gz
Source8:        %{testurl}/archive/3235916.tar.gz
Source9:        %{testurl}/archive/7090735c.tar.gz
Source10:       %{testurl}/archive/7371c1d9.tar.gz
Source11:       %{testurl}/archive/a5d7cdc0.tar.gz
Source12:       %{testurl}/archive/ad4dd344.tar.gz
Source13:       %{testurl}/archive/c1842d168d.tar.gz
Source14:       %{testurl}/archive/c1ba97dafe95c865d37ad4d88f6e57c9ffbe7f0a.tar.gz
Source15:       %{testurl}/archive/de897adf36c4230dfea812f40c98223b31c4521a.tar.gz
Source16:       %{testurl}/archive/f372039d.tar.gz
# Disable tests that:
# - access the Internet
# - use the git file protocol (removed in git 2.38)
Patch:          %{name}-disable-tests.patch

BuildRequires:  diffutils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-base64-devel >= 3.1.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-cudf-devel >= 0.7
BuildRequires:  ocaml-dose3-devel >= 6.1
BuildRequires:  ocaml-dune >= 2.8.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-jsonm-devel
BuildRequires:  ocaml-mccs-devel >= 1.1.17
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-opam-0install-cudf-devel >= 0.5.0
BuildRequires:  ocaml-opam-file-format-devel >= 2.1.4
BuildRequires:  ocaml-patch-devel >= 3.0.0~alpha1
BuildRequires:  ocaml-re-devel >= 1.10.0
BuildRequires:  ocaml-sha-devel >= 1.13
BuildRequires:  ocaml-spdx-licenses-devel >= 1.0.0
BuildRequires:  ocaml-swhid-core-devel
BuildRequires:  ocaml-uutf-devel
BuildRequires:  ocaml-z3-devel
BuildRequires:  openssl

# Testing dependencies
BuildRequires:  bubblewrap
BuildRequires:  bzip2
BuildRequires:  mercurial
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  rsync
BuildRequires:  unzip
BuildRequires:  xxd
BuildRequires:  xz

# Needed to install packages and run opam init.
Requires:       bubblewrap
Requires:       bzip2
Requires:       gcc
Requires:       gzip
Requires:       make
Requires:       tar
Requires:       unzip
Requires:       xz

Requires:       opam-installer%{?_isa} = %{version}-%{release}

# Common remote
Recommends:     git-core

# Less common remotes
Suggests:       darcs
Suggests:       mercurial
Suggests:       rsync

%description
Opam is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and
a Git-friendly development workflow.

%package installer
Summary:        Standalone script for opam install files

%description installer
Standalone script for working with opam .install files, see the opam
package for more information.

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -n %{name}-full-%{version} -p1
sed -e 's,%%SOURCE3%%,%{SOURCE3},' \
    -e 's,%%SOURCE4%%,%{SOURCE4},' \
    -e 's,%%SOURCE5%%,%{SOURCE5},' \
    -e 's,%%SOURCE6%%,%{SOURCE6},' \
    -e 's,%%SOURCE7%%,%{SOURCE7},' \
    -e 's,%%SOURCE8%%,%{SOURCE8},' \
    -e 's,%%SOURCE9%%,%{SOURCE9},' \
    -e 's,%%SOURCE10%%,%{SOURCE10},' \
    -e 's,%%SOURCE11%%,%{SOURCE11},' \
    -e 's,%%SOURCE12%%,%{SOURCE12},' \
    -e 's,%%SOURCE13%%,%{SOURCE13},' \
    -e 's,%%SOURCE14%%,%{SOURCE14},' \
    -e 's,%%SOURCE15%%,%{SOURCE15},' \
    -e 's,%%SOURCE16%%,%{SOURCE16},' \
    -i tests/reftests/dune.inc

%build
export DUNE_ARGS='--verbose'
export DUNE_PROFILE_ARG='release'

%configure
%make_build

%install
export DUNE_ARGS='--verbose'
export DUNE_PROFILE_ARG='release'
%make_install

# However it looks like some (extra) documentation gets
# installed in the wrong place so... delete it.
rm -rf %{buildroot}%{_prefix}/doc

%check
# Silence git warnings that lead to failed tests
git config --global init.defaultBranch main
git config --global user.email 'mockbuild@fedoraproject.org'
git config --global user.name 'Mock Builder'

export DUNE_ARGS='--verbose'
export DUNE_PROFILE_ARG='release'
make tests

%files
%license LICENSE
%{_bindir}/opam
%exclude %{_mandir}/man1/opam-installer.1*
%{_mandir}/man1/*.1*

%files installer
%license LICENSE
# Upstream puts this documentation under opam-installer, not opam.
# Since I have opam require opam-installer anyway, this seems reasonable.
# (And there are lots of man pages in the opam package, so it has docs).
%doc README.md CHANGES AUTHORS CONTRIBUTING.md
%{_bindir}/opam-installer
%{_mandir}/man1/opam-installer.1*

%changelog
%autochangelog
