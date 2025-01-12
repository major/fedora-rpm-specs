# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

# NOTE: Upstream has said that the Frama-C support is still experimental, and
# less functional than the corresponding support in why2.  They recommend not
# enabling it for now.  We abide by their wishes.  Revisit this decision each
# release.

Name:           why3
Version:        1.8.0
Release:        %autorelease
Summary:        Software verification platform

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://www.why3.org/
VCS:            git:https://gitlab.inria.fr/why3/why3.git
Source0:        https://why3.gitlabpages.inria.fr/releases/%{name}-%{version}.tar.gz
# Desktop file written by Jerry James
Source1:        fr.lri.%{name}.desktop
# AppData file written by Jerry James
Source2:        fr.lri.%{name}.metainfo.xml
# Fix a link order issue
Patch:          %{name}-link-order.patch

BuildRequires:  coq
BuildRequires:  emacs-nw
BuildRequires:  emacs-proofgeneral
BuildRequires:  flocq
BuildRequires:  graphviz
BuildRequires:  java-devel
BuildRequires:  latexmk
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-apron-devel
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk3-sourceview3-devel
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-mlmpfr-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppx-sexp-conv-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-sexplib-devel
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(comment.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(tgtermes.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  tex-urlbst

Requires:       gtksourceview3%{?_isa}
Requires:       hicolor-icon-theme
Requires:       texlive-base%{?_isa}
Requires:       vim-filesystem

Recommends:     bash-completion
Recommends:     flocq

Provides:       bundled(js-jquery)

# The corresponding Provides is not generated, so filter this out
%global __requires_exclude ocaml\\\(Driver_ast\\\)

%description
Why3 is the next generation of the Why software verification platform.
Why3 clearly separates the purely logical specification part from
generation of verification conditions for programs.  It features a rich
library of proof task transformations that can be chained to produce a
suitable input for a large set of theorem provers, including SMT
solvers, TPTP provers, as well as interactive proof assistants.

%package examples
Summary:        Example inputs
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description examples
Example source code with why3 annotations.

%package emacs
Summary:        Emacs support file for %{name} files
Requires:       %{name} = %{version}-%{release}
Requires:       emacs(bin)
BuildArch:      noarch

%description emacs
This package contains an Emacs support file for working with %{name} files.

%package all
Summary:        Complete Why3 software verification platform suite
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       alt-ergo coq cvc5 E gappa yices-tools z3 zenon

%description all
This package provides a complete software verification platform suite
based on Why3, including various automated and interactive provers.

%package -n ocaml-%{name}
Summary:        Software verification library for ocaml
Requires:       ocaml-zip-devel%{?_isa}

%description -n ocaml-%{name}
This package contains an ocaml library that exposes the functionality
of why3 to applications.

%package -n ocaml-%{name}-devel
Summary:        Development files for using the ocaml-%{name} library
Requires:       ocaml-%{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-menhir%{?_isa}
Requires:       ocaml-num-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-sexplib-devel%{?_isa}
Requires:       ocaml-zip-devel%{?_isa}

%description -n ocaml-%{name}-devel
This package contains development files needed to build applications
that use the ocaml-%{name} library.

%package proofgeneral
Summary:        Why3 integration with ProofGeneral
Requires:       %{name} = %{version}-%{release}
Requires:       emacs-proofgeneral
BuildArch:      noarch

%description proofgeneral
This package provides a why3 plugin for ProofGeneral.

%prep
%autosetup -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

# Use the correct compiler flags, keep timestamps, and harden the build due to
# network use.  Link the binaries with runtime compiled with -fPIC.
# This avoids many link-time errors.
sed -e 's|-Wall|%{build_cflags} %{build_ldflags}|;s/ -O -g//' \
    -e 's/cp /cp -p /' \
    -e 's|^OLINKFLAGS =.*|& -runtime-variant _pic -ccopt "%{build_ldflags}"|' \
    -i Makefile.in

# Update the ProofGeneral integration instructions
sed -i.orig 's,(MY_PATH_TO_WHY3)/share/whyitp,%{_emacs_sitelispdir},' share/whyitp/README
fixtimestamp share/whyitp/README

# Fix a configure script typo
sed -i 's/\$(OCAMLC/$(ocamlc/' configure

%build
%configure --enable-verbose-make --enable-bddinfer
# Work around a Makefile bug in version 1.8.0
ln -s why3.opt bin/why3
# FIXME: Parallel make sometimes fails
make
# The documentation build is broken in the 1.8.0 release
# make doc
rm -f doc/html/.buildinfo examples/use_api/.merlin.in

%install
%make_install
make install-lib DESTDIR=%{?buildroot} INSTALL="%{__install} -p"

%ifarch %{ocaml_native_compiler}
# Install the native coq files
cd lib/coq
for dir in $(find . -name .coq-native); do
  cp -a $dir %{buildroot}%{_libdir}/%{name}/coq/$dir
done
cd -
%endif

# Install the bash completion file
mkdir -p %{buildroot}%{bash_completions_dir}
cp -p share/bash/%{name} %{buildroot}%{bash_completions_dir}

# Install the zsh completion file
mkdir -p %{buildroot}%{zsh_completions_dir}
cp -p share/zsh/_why3 %{buildroot}%{zsh_completions_dir}

# Install the LaTeX style
mkdir -p %{buildroot}%{_texmf}/tex/latex/why3
cp -p share/latex/why3lang.sty %{buildroot}%{_texmf}/tex/latex/why3

# Move the gtksourceview language file to the right place
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0
mv %{buildroot}%{_datadir}/%{name}/lang \
   %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs

# Install the desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p share/images/src/logo-kim.svg \
      %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Install the AppStream metadata
mkdir -p %{buildroot}%{_metainfodir}
cp -p %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/fr.lri.%{name}.metainfo.xml

# Move the vim file to the right place
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles
mv %{buildroot}%{_datadir}/%{name}/vim/ftdetect \
   %{buildroot}%{_datadir}/%{name}/vim/syntax \
   %{buildroot}%{_datadir}/vim/vimfiles

# Byte compile the Emacs support files
cp -p share/whyitp/whyitp.el %{buildroot}%{_emacs_sitelispdir}
cd %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} %{name}.el whyitp.el
cd -

# Remove misplaced documentation
rm -fr %{buildroot}%{_datadir}/doc

# Fix permissions
chmod 0755 %{buildroot}%{_bindir}/* \
           %{buildroot}%{_libdir}/%{name}/commands/* \
           %{buildroot}%{_libdir}/%{name}/plugins/*.cmxs \
           %{buildroot}%{ocamldir}/%{name}/*.cmxs

%files
%doc AUTHORS CHANGES.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/isabelle_client
%{bash_completions_dir}/why3
%{zsh_completions_dir}/_why3
%{_datadir}/%{name}/
%{_datadir}/applications/fr.lri.%{name}.desktop
%{_datadir}/gtksourceview-3.0/language-specs/coma.lang
%{_datadir}/gtksourceview-3.0/language-specs/%{name}.lang
%{_datadir}/gtksourceview-3.0/language-specs/%{name}c.lang
%{_datadir}/gtksourceview-3.0/language-specs/%{name}py.lang
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/vim/vimfiles/ftdetect/%{name}.vim
%{_datadir}/vim/vimfiles/syntax/%{name}.vim
%{_texmf}/tex/latex/why3/
%{_libdir}/%{name}/
%{_metainfodir}/fr.lri.%{name}.metainfo.xml

%files -n ocaml-%{name}
%dir %{ocamldir}/%{name}/
%{ocamldir}/%{name}/META
%{ocamldir}/%{name}/*.cmi
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}/*.cmxs
%endif

%files -n ocaml-%{name}-devel
%ifarch %{ocaml_native_compiler}
%{ocamldir}/%{name}/*.a
%{ocamldir}/%{name}/*.cmx
%{ocamldir}/%{name}/*.cmxa
%else
%{ocamldir}/%{name}/*.cma
%endif
%{ocamldir}/%{name}/*.cmt

%files examples
%doc examples

%files emacs
%{_emacs_sitelispdir}/%{name}.el*

%files proofgeneral
%doc share/whyitp/README
%{_emacs_sitelispdir}/whyitp.el*

# "why3-all" is a meta-package; it just depends on other packages, so that
# it's easier to install a useful suite of tools.  Thus, it has no files:
%files all

%changelog
%autochangelog
