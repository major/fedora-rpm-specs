# TESTING NOTE: The tests require rocq-stdlib, thus introducing a circular
# dependency.  Use this conditional to control testing.
#
# The tests don't work anyway, because we have to have an installed version of
# rocq with rocq-devtools, which we don't otherwise want to build or install.
%bcond test 0

%global giturl  https://github.com/rocq-prover/rocq

Name:           rocq
Version:        9.1.1
Release:        %autorelease
Summary:        Proof management system

# The project as a whole is LGPL-2.1-only.  Exceptions:
# - clib/diff2.ml is MIT
# - gramlib is BSD-3-Clause except:
# - gramlib/stream.ml* is LGPL-2.1-only WITH OCaml-LGPL-linking-exception
License:        LGPL-2.1-only AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND MIT AND BSD-3-Clause
URL:            https://rocq-prover.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/V%{version}/%{name}-%{version}.tar.gz
Source1:        org.rocq-prover.rocqide.desktop
Source2:        org.rocq-prover.rocqide.metainfo.xml
Source3:        rocq.xml
# Expose a dependency on the math library so rpm can see it
Patch:          %{name}-mathlib.patch
# [Backport] Fix documentation build (upstream commit 17e4fb9)
Patch:          %{name}-no-generated-readme.patch

# Rocq's plugin architecture requires cmxs files.  In addition, neither Java
# nor OCaml is available on i386, but since i386 is not in
# ocaml_native_compiler, we do not need to exclude it explicitly.
ExclusiveArch:  %{ocaml_native_compiler}

BuildRequires:  adwaita-icon-theme
BuildRequires:  csdp-tools
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-cairo-devel >= 0.6.4
BuildRequires:  ocaml-dune >= 3.8
BuildRequires:  ocaml-findlib-devel >= 1.9.1
BuildRequires:  ocaml-lablgtk3-sourceview3-devel >= 3.1.2
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-zarith-devel >= 1.11
BuildRequires:  python3-devel

%if %{with test}
BuildRequires:  ocaml-ounit2-devel
BuildRequires:  ocaml-yojson-devel >= 2.0
BuildRequires:  ocaml-zip-devel
BuildRequires:  rocq-stdlib
BuildRequires:  rsync
BuildRequires:  time
%endif

# For documentation
BuildRequires:  antlr4 >= 4.7.1
BuildRequires:  %{py3_dist antlr4-python3-runtime}
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist pexpect}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  python3-sphinx-latex
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(array.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(ifpdf.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(microtype.sty)
BuildRequires:  tex(polyglossia.sty)
BuildRequires:  tex(unicode-math.sty)
BuildRequires:  tex(verbatim.sty)
BuildRequires:  tex(xr.sty)

Requires:       %{name}-runtime%{_isa} = %{version}-%{release}
Requires:       %{name}-core%{_isa} = %{version}-%{release}
Requires:       csdp-tools
Requires:       ocaml-findlib

Recommends:     emacs-proofgeneral
Recommends:     rocq-stdlib
Recommends:     texlive-collection-latex

# This can be removed when F48 reaches EOL
Provides:       coq = %{version}-%{release}
Obsoletes:      coq < 9.1.1

%global _desc %{expand:Rocq is a formal proof management system.  It provides a formal language to
write mathematical definitions, executable algorithms and theorems together
with an environment for semi-interactive development of machine-checked proofs.}

%description
%_desc

Typical applications include the certification of properties of programming
languages (e.g., the CompCert compiler certification project, or the Bedrock
verified low-level programming library), the formalization of mathematics
(e.g., the full formalization of the Feit-Thompson theorem or homotopy type
theory) and teaching.

%package        runtime
Summary:        Core binaries and tools of the Rocq proof management system
Requires:       %{name}%{?_isa} = %{version}-%{release}
# This can be removed when F48 reaches EOL
Provides:       coq-core = %{version}-%{release}
Obsoletes:      coq-core < 9.1.1

%description    runtime
%_desc

This package includes the Rocq prover core binaries, plugins, and tools, but
not the vernacular standard library.

%package        runtime-devel
Summary:        Development files for %{name}-runtime
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}

%description    runtime-devel
%_desc

The %{name}-runtime-devel package contains libraries and signature files
for developing applications that use %{name}-runtime.

%package        core
Summary:        The Rocq Prelude, and the Corelib and Ltac2 modules
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}
# This can be removed when F48 reaches EOL
Provides:       coq = %{version}-%{release}
Obsoletes:      coq < 9.1.1

%description    core
%_desc

This package includes the Rocq prelude, that is loaded automatically
by Rocq in every .v file, as well as other modules bound to the
Corelib.* and Ltac2.* namespaces.

%package        core-source
Summary:        Source files of the Rocq Prelude, and the Corelib and Ltac2 modules
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description    core-source
%_desc

This package contains the source Rocq files for the Rocq Prelude, and the
Corelib and Ltac2 modules.  These files are not needed to use the Rocq Prelude,
and the Corelib and Ltac2 modules.  They are made available for informational
purposes.

%package     -n coq-core-compat
Summary:        Compatibility binaries for Coq after the Rocq renaming
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
# This can be removed when F48 reaches EOL
Provides:       coq-core = %{version}-%{release}
Obsoletes:      coq-core < 9.1.1

%description -n coq-core-compat
%_desc

This package includes compatibility binaries to call Rocq
through previous Coq commands like coqc coqtop,...

%package        coqide-server
Summary:        The coqidetop language server
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
# This can be removed when F48 reaches EOL
Provides:       coq-coqide-server = %{version}-%{release}
Obsoletes:      coq-coqide-server < 9.1.1

%description    coqide-server
%_desc

This package provides the coqidetop language server, an implementation of
Rocq's XML protocol which allows clients, such as RocqIDE, to interact with
Rocq in a structured way.

%package        coqide-server-devel
Summary:        Development files for %{name}-coqide-server
Requires:       %{name}-coqide-server%{?_isa} = %{version}-%{release}

%description    coqide-server-devel
%_desc

The %{name}-coqide-server-devel package contains libraries and signature files
for developing applications that use %{name}-coqide-server.

%package        rocqide
# The project as a whole is LGPL-2.1-only.
# LGPL-2.1-or-later: ide/rocqide/protocol/xml_{lexer,parser}*
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Summary:        RocqIDE for the Rocq proof management system
Requires:       %{name}-coqide-server%{?_isa} = %{version}-%{release}
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
Requires:       xdg-utils
# This can be removed when F48 reaches EOL
Provides:       coq-coqide = %{version}-%{release}
Obsoletes:      coq-coqide < 9.1.1

Provides:       bundled(ocaml-xml-light)

%description    rocqide
%_desc

This package provides RocqIDE, a graphical user interface for the
development of interactive proofs.

%package        doc
Summary:        Documentation for the Rocq proof management system
# The documentation as a whole is OPUBL-1.0.
# Some sphinx-installed files are LGPL-2.1-only.
# Some sphinx-installed files are MIT.
#
# The OPUBL-1.0 license is not allowed for Fedora, but carries this usage note
# (https://gitlab.com/fedora/legal/fedora-license-data/-/blob/main/data/OPUBL-1.0.toml):
# "Allowed-for documentation if the copyright holder does not exercise any of
# the “LICENSE OPTIONS” listed in Section VI".
#
# doc/LICENSE contains this note: "Options A and B are *not* elected."
#
# Therefore, this package falls under the Fedora exception.
License:        OPUBL-1.0 AND LGPL-2.1-only AND MIT
BuildArch:      noarch
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
# This can be removed when F48 reaches EOL
Provides:       coq-doc = %{version}-%{release}
Obsoletes:      coq-doc < 9.1.1

%description    doc
%_desc

This package provides documentation and tutorials for the system.  The
main documentation comes in two parts: the main Library documentation,
which describes all Corelib.* modules, and the Reference Manual, which
gives a more complete description of the whole system. Included are
HTML versions of both and a PDF version of the Reference Manual.

%prep
%autosetup -p1

%conf
fixtimestamp() {
    touch -r $1.orig $1
    rm -f $1.orig
}

# Use Fedora flags
sed -e 's|-Wall.*-O2|%{build_cflags} %{build_ldflags} -Wno-unused|' \
    -i tools/configure/configure.ml

# Make sure debuginfo is generated
sed -i 's,-shared,& -g,g' tools/CoqMakefile.in

# Do not invoke env
for f in doc/tools/coqrst/notations/fontsupport.py;
do
  sed -i.orig 's,/usr/bin/env python2,%{python3},' $f
  fixtimestamp $f
done
for f in $(grep -Frl '%{_bindir}/env'); do
  sed -r -i.orig 's,(%{_bindir}/)env[[:blank:]]+([[:alnum:]]+),\1\2,g' $f
  fixtimestamp $f
done

%build
%global rocqdocdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/rocq-%{version}}

# Regenerate ANTLR files
cd doc/tools/coqrst/notations
antlr4 -Dlanguage=Python3 -visitor -no-listener TacticNotations.g
cd -

# Set our configuration options
# NOTE: Must still be installed in a dir named `coq'
./configure -prefix %{_prefix}                       \
            -libdir %{ocamldir}/coq                  \
            -configdir %{_sysconfdir}/xdg/%{name}    \
            -mandir %{_mandir}                       \
            -docdir %{rocqdocdir}                    \
%ifarch %{ocaml_natdynlink}
            -natdynlink yes                          \
%else
            -natdynlink no                           \
%endif
            -browser "xdg-open %s"                   \
            -bytecode-compiler yes                   \
            -native-compiler no
# As of coq 8.17.0, the native compiler cannot be built with OCaml 5.x
#%%ifarch %%{ocaml_native_compiler}
#            -native-compiler yes
#%%else
#            -native-compiler no
#%%endif

# Build the binary artifacts
make dunestrap VERBOSE=1 DUNEOPT="--verbose --profile=release"
%dune_build %{!?_with_test:-p rocq-runtime,rocq-core,coq-core,coqide-server,rocqide}

# Build the documentation
export ROCQLIB=${PWD}/_build/install/default/lib/coq
export SPHINXWARNOPT="-w$PWD/sphinx-warn.log"
%dune_build @refman-html @refman-pdf @corelib-html

%install
%dune_install %{!?_with_test:rocq-runtime rocq-core coq-core coqide-server rocqide}

# Install the LaTeX style file
mkdir -p %{buildroot}%{_texmf_main}/tex/latex/misc
mv %{buildroot}%{_datadir}/texmf/tex/latex/misc/coqdoc.sty \
   %{buildroot}%{_texmf_main}/tex/latex/misc
rm -fr %{buildroot}%{_datadir}/texmf

# FIXME: dune ignores the configdir argument to configure
mkdir -p %{buildroot}%{_sysconfdir}/xdg/%{name}

# Prepare the documentation for installation
find _build/default/doc -name .buildinfo -delete

# Install the documentation
rm -fr _build/default/doc/refman-html/.doctrees
mkdir -p %{buildroot}%{rocqdocdir}/refman-pdf
mv _build/default/doc/refman-pdf/rocq*.pdf %{buildroot}%{rocqdocdir}/refman-pdf/
mv _build/default/doc/refman-html %{buildroot}%{rocqdocdir}/refman-html
mv _build/default/doc/corelib/html %{buildroot}%{rocqdocdir}/corelib
mv _build/default/doc/corelib/_index.html %{buildroot}%{rocqdocdir}/corelib/

# Install desktop and file type icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/mimetypes
cp --preserve=timestamps ide/rocqide/coq.png \
   %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/rocq.png
cp --preserve=timestamps ide/rocqide/coq.png \
   %{buildroot}%{_datadir}/icons/hicolor/256x256/mimetypes/rocqfile.png

# Make a MIME type for .v files
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p %{SOURCE3} %{buildroot}%{_datadir}/mime/packages

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.rocq-prover.rocqide.metainfo.xml

# Install the language bindings
# NOTE: Must still be installed in a dir named `coq'
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
for fil in coq.lang coq-ssreflect.lang; do
  ln -s ../../coq/$fil %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
done

# Install the style file
# NOTE: Must still be installed in a dir named `coq'
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/styles
ln -s ../../coq/coq_style.xml %{buildroot}%{_datadir}/gtksourceview-3.0/styles

# Byte compile the tools
%py_byte_compile %{python3} %{buildroot}%{ocamldir}/coq-core/tools

# Generate file lists
%ocaml_files -s

%if %{with test}
%check
%dune_check
%endif

%files
# Empty metapackage

%files runtime -f .ofiles-rocq-runtime
%doc README.md
%license LICENSE
%{_texmf_main}/tex/latex/misc/

%files runtime-devel -f .ofiles-rocq-runtime-devel

%files core
%{ocamldir}/rocq-core/
%{ocamldir}/coq
%exclude %{ocamldir}/coq/theories/*/*.v
%exclude %{ocamldir}/coq/user-contrib/Ltac2/*/*.v

%files core-source
%{ocamldir}/coq/theories/*/*.v
%{ocamldir}/coq/user-contrib/Ltac2/*/*.v

%files -n coq-core-compat -f .ofiles-coq-core -f .ofiles-coq-core-devel

%files coqide-server -f .ofiles-coqide-server

%files coqide-server-devel -f .ofiles-coqide-server-devel

%files rocqide -f .ofiles-rocqide -f .ofiles-rocqide-devel
%doc ide/rocqide/FAQ
%{_datadir}/icons/hicolor/256x256/apps/rocq.png
%{_datadir}/icons/hicolor/256x256/mimetypes/rocqfile.png
%{_metainfodir}/org.rocq-prover.rocqide.metainfo.xml
%{_datadir}/applications/org.rocq-prover.rocqide.desktop
%{_datadir}/gtksourceview-3.0/language-specs/coq*.lang
%{_datadir}/gtksourceview-3.0/styles/coq_style.xml
%{_datadir}/mime/packages/rocq.xml
%{_sysconfdir}/xdg/rocq/

%files doc
%license doc/LICENSE
%{rocqdocdir}

%changelog
%autochangelog
