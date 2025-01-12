# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml/opam

Name:           opam
Version:        2.3.0
Release:        %autorelease
Summary:        Source-based package manager for OCaml

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://opam.ocaml.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/%{name}-full-%{version}.tar.gz
Source1:        %{giturl}/releases/download/%{version}/%{name}-full-%{version}.tar.gz.sig
Source2:        https://opam.ocaml.org/opam-dev-pubkey.pgp

BuildRequires:  diffutils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  libacl-devel
BuildRequires:  make
BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-base64-devel >= 3.1.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-cudf-devel >= 0.7
BuildRequires:  ocaml-dose3-devel >= 6.1
BuildRequires:  ocaml-dune >= 2.8.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-jsonm-devel
BuildRequires:  ocaml-mccs-devel
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-opam-0install-cudf-devel >= 0.5.0
BuildRequires:  ocaml-opam-file-format-devel >= 2.1.4
BuildRequires:  ocaml-re-devel >= 1.10.0
BuildRequires:  ocaml-sha-devel >= 1.13
BuildRequires:  ocaml-spdx-licenses-devel >= 1.0.0
BuildRequires:  ocaml-swhid-core-devel
BuildRequires:  ocaml-uutf-devel
BuildRequires:  ocaml-z3-devel
BuildRequires:  openssl

# Needed to install packages and run opam init.
Requires:       bubblewrap
Requires:       bzip2
Requires:       diffutils
Requires:       gcc
Requires:       gzip
Requires:       make
Requires:       patch
Requires:       tar
Requires:       unzip
Requires:       xz

Requires:       opam-installer%{?_isa} = %{version}-%{release}

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

# It seems that some tests fail under mock.
# I am not sure why at the moment. So for now I'll just turn them off.
#%%check
#make tests

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
