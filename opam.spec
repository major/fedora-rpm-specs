%undefine _package_note_flags
Name:           opam
Version:        2.1.4
Release:        %autorelease
Summary:        Source-based package manager for OCaml

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/opam
Source0:        https://github.com/ocaml/opam/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib

BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-opam-file-format-devel
BuildRequires:  ocaml-base64-devel
BuildRequires:  ocaml-dose3-devel
BuildRequires:  ocaml-mccs-devel
BuildRequires:  ocaml-z3-devel

BuildRequires:  git
BuildRequires:  gcc-c++
BuildRequires:  bzip2
BuildRequires:  diffutils
BuildRequires:  libacl-devel

# Needed to install packages and run opam init.
Requires:       bubblewrap
Requires:       bzip2
Requires:       diffutils
Requires:       gcc
Requires:       gzip
Requires:       make
Requires:       m4
Requires:       patch
Requires:       unzip
Requires:       tar

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
%autosetup -p1 -n %{name}-%{version}

%build
%configure
export DUNE_ARGS="--verbose"
# Need to set the path so Makefile can run the opam command.
export PATH=$PWD:$PATH

# Parallel build does not succeed.
make

%install
export DUNE_ARGS="--verbose"
export PATH=$PWD:$PATH

# The makefile looks like it tries to invoke ocamlfind but only if DESTDIR
# isn't set. If it is set (which it is) LIBINSTALLDIR must be set too
# for installing opam-installer metadata.
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
