# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

# ANTLR is unavailable on i686
# See https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
#
# This is commented for out now because ocaml_native_compiler is
# narrower, and apparently if you have two ExclusiveArch lines in a
# spec file, RPM ignores the first one and uses the second one!
# ExclusiveArch: %%{java_arches}

%ifarch %{ocaml_native_compiler}
%global camlsuffix opt
%else
%global camlsuffix byte
%endif

# .coqide-gtk2rc produces an rpmlint warning due to its name,
# however, this name is proper as per the Coq documentation

# Coq installs python files into nonstandard places
%global _python_bytecompile_extra 0

# The documentation package cannot be built with ocaml-dune 3.8.2.  Check later
# releases of both coq and dune to see if the issues have been resolved.
%bcond doc 0

%global giturl  https://github.com/coq/coq

Name:           coq
Version:        8.20.1
Release:        %autorelease
Summary:        Proof management system

# The project as a whole is LGPL-2.1-only.  Exceptions:
# - clib/diff2.ml is MIT
# - gramlib is BSD-3-Clause
License:        LGPL-2.1-only AND MIT AND BSD-3-Clause
URL:            https://coq.inria.fr/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/V%{version}/%{name}-%{version}.tar.gz
Source1:        fr.inria.coqide.desktop
Source2:        coq.xml
Source3:        fr.inria.coqide.metainfo.xml
# Expose a dependency on the math library so rpm can see it
Patch:          %{name}-mathlib.patch

BuildRequires:  ocaml >= 4.09.0
BuildRequires:  ocaml-cairo-devel >= 0.6.4
BuildRequires:  ocaml-dune >= 3.6.1
BuildRequires:  ocaml-findlib-devel >= 1.8.1
BuildRequires:  ocaml-lablgtk3-sourceview3-devel >= 3.1.2
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-zarith-devel >= 1.11
BuildRequires:  adwaita-icon-theme
BuildRequires:  antlr4 >= 4.7.1
BuildRequires:  libappstream-glib
BuildRequires:  csdp-tools
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  git-core
BuildRequires:  java
BuildRequires:  libicns-utils
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist antlr4-python3-runtime}
BuildRequires:  rsync
BuildRequires:  time

%if %{with doc}
# For documentation
BuildRequires:  hevea
BuildRequires:  %{py3_dist beautifulsoup4}
BuildRequires:  %{py3_dist pexpect}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinxcontrib-bibtex}
BuildRequires:  %{py3_dist sphinx-rtd-theme}
BuildRequires:  tex(latex)
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(comment.sty)
BuildRequires:  tex(epic.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(framed.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(moreverb.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(stmaryrd.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(upquote.sty)
BuildRequires:  tex(utf8x.def)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  tex(FreeSerif.otf)
BuildRequires:  tex-cm-super
BuildRequires:  tex-courier
BuildRequires:  tex-ec
BuildRequires:  tex-helvetic
BuildRequires:  tex-symbol
BuildRequires:  tex-times
BuildRequires:  tex-xindy
BuildRequires:  tex-zapfchan
BuildRequires:  tex-zapfding
%else
BuildRequires:  texlive-base
%endif

Requires:       %{name}-core%{_isa} = %{version}-%{release}
Requires:       csdp-tools
Requires:       ocaml-findlib
Requires:       texlive-base

Recommends:     emacs-proofgeneral

# This can be removed when F41 reaches EOL
Obsoletes:      coq-doc < 8.16.0-2

%global _desc %{expand:
Coq is a formal proof management system.  It provides a formal language
to write mathematical definitions, executable algorithms and theorems
together with an environment for semi-interactive development of
machine-checked proofs.}

%description %_desc

Typical applications include the certification of properties of
programming languages (e.g. the CompCert compiler certification project,
or the Bedrock verified low-level programming library), the formalization
of mathematics (e.g. the full formalization of the Feit-Thompson theorem
or homotopy type theory) and teaching.

%package core
Summary:        Core components of the coq proof management system
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description core %_desc

This package includes the Coq core binaries, plugins, and tools, but not
the vernacular standard library.

%package coqide-server
Summary:        The coqidetop language server
Requires:       %{name}-core%{?_isa} = %{version}-%{release}

%description coqide-server %_desc

This package provides the coqidetop language server, an implementation of
Coq's XML protocol which allows clients, such as CoqIDE, to interact with
Coq in a structured way.

%package coqide
Summary:        Coqide IDE for Coq proof management system
Requires:       %{name}-coqide-server%{?_isa} = %{version}-%{release}
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
Requires:       xdg-utils

%description coqide %_desc

This package provides CoqIDE, a graphical user interface for the
development of interactive proofs.

%if %{with doc}
%package doc
Summary:        Documentation for Coq proof management system
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

%description doc %_desc

This package provides documentation and tutorials for the system.  The
main documentation comes in two parts: the main Library documentation,
which describes all Coq.* modules, and the Reference Manual, which
gives a more complete description of the whole system. Included are
also HTML versions of both. Furthermore, there are two tutorials, the
main one, and one specifically on recursive types. The example code
for the latter is also included.
%endif

%prep
%autosetup -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Use Fedora flags
sed -e 's|-Wall.*-O2|%{build_cflags} %{build_ldflags} -Wno-unused|' \
    -e 's| -march=native||' \
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
%global coqdocdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/coq-%{version}}

# Regenerate ANTLR files
cd doc/tools/coqrst/notations
antlr4 -Dlanguage=Python3 -visitor -no-listener TacticNotations.g
cd -

# Set our configuration options
./configure -prefix %{_prefix}                       \
            -libdir %{ocamldir}/coq                  \
            -configdir %{_sysconfdir}/xdg/%{name}    \
            -mandir %{_mandir}                       \
            -docdir %{coqdocdir}                     \
%ifarch %{ocaml_natdynlink}
            -natdynlink yes                          \
%else
            -natdynlink no                           \
%endif
            -browser "xdg-open %s"                   \
            -bytecode-compiler yes                   \
            -native-compiler no
# As of coq 8.17.0, the native compiler cannot be build with OCaml 5.x
#%%ifarch %%{ocaml_native_compiler}
#            -native-compiler yes
#%%else
#            -native-compiler no
#%%endif

# Build the binary artifacts
export SPHINXWARNOPT="-w$PWD/sphinx-warn.log"
make dunestrap VERBOSE=1 DUNEOPT="--verbose --profile=release"
%dune_build %{!?with_doc:-p coq-core,coq-stdlib,coq,coqide-server,coqide}

%install
%dune_install %{!?with_doc:coq-core coq-stdlib coq coqide-server coqide}

# Install the LaTeX style file
mkdir -p %{buildroot}%{_texmf_main}/tex/latex/misc
mv %{buildroot}%{_datadir}/texmf/tex/latex/misc/coqdoc.sty \
   %{buildroot}%{_texmf_main}/tex/latex/misc
rm -fr %{buildroot}%{_datadir}/texmf

# FIXME: dune ignores the configdir argument to configure
mkdir -p %{buildroot}%{_sysconfdir}/xdg/%{name}

%if %{with doc}
# Prepare the documentation for installation
find doc/sphinx/_build/html -name .buildinfo -delete
%endif

# Install desktop and file type icons
pushd ide/coqide/MacOS
icns2png -x coqide.icns
for sz in 16 32 256 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  mv coqide_${sz}x${sz}x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/coq.png
done
icns2png -x coqfile.icns
for sz in 16 32 128 256 512; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes
  mv coqfile_${sz}x${sz}x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/mimetypes/coqfile.png
done
popd

# Make a MIME type for .v files
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p %{SOURCE2} %{buildroot}%{_datadir}/mime/packages

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE3} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/fr.inria.coqide.metainfo.xml

# Install the language bindings
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
for fil in coq.lang coq-ssreflect.lang; do
  ln -s ../../coq/$fil %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
done

# Install the style file
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/styles
ln -s ../../coq/coq_style.xml %{buildroot}%{_datadir}/gtksourceview-3.0/styles

# Byte compile the tools
%py_byte_compile %{python3} %{buildroot}%{ocamldir}/coq-core/tools

%files
%{ocamldir}/coq/
%{ocamldir}/coq-stdlib/

%files core
%doc README.md
%license LICENSE
%{ocamldir}/coq-core/
%{ocamldir}/stublibs/dllcoqperf_stubs.so
%{ocamldir}/stublibs/dllcoqrun_stubs.so
%{_bindir}/coqc*
%{_bindir}/coqdep
%{_bindir}/coqdoc
%{_bindir}/coq_makefile
%{_bindir}/coqnative
%{_bindir}/coqpp
%{_bindir}/coq-tex
%{_bindir}/coqtimelog2html
%{_bindir}/coqtop*
%{_bindir}/coqwc
%{_bindir}/coqworker.%{camlsuffix}
%{_bindir}/coqworkmgr
%{_bindir}/csdpcert
%{_bindir}/ocamllibdep
%{_bindir}/votour
%{_mandir}/man1/coqc.1*
%{_mandir}/man1/coqchk.1*
%{_mandir}/man1/coqdep.1*
%{_mandir}/man1/coqdoc.1*
%{_mandir}/man1/coq_makefile.1*
%{_mandir}/man1/coqnative.1*
%{_mandir}/man1/coq-tex.1*
%{_mandir}/man1/coqtop.1*
%{_mandir}/man1/coqtop.byte.1*
%{_mandir}/man1/coqwc.1*
%{_texmf_main}/tex/latex/misc/
%if %{with doc}
# This should really go in the doc subpackage, but because it is installed in
# an arch-specific path, it cannot be part of a noarch package.
%{ocamldir}/coq-doc/
%endif

%files coqide-server
%{_bindir}/coqidetop*
%{ocamldir}/coqide-server/

%files coqide
%doc ide/coqide/FAQ
%{_bindir}/coqide
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/16x16/apps/coq.png
%{_datadir}/icons/hicolor/16x16/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/32x32/apps/coq.png
%{_datadir}/icons/hicolor/32x32/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/128x128/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/256x256/apps/coq.png
%{_datadir}/icons/hicolor/256x256/mimetypes/coqfile.png
%{_datadir}/icons/hicolor/512x512/apps/coq.png
%{_datadir}/icons/hicolor/512x512/mimetypes/coqfile.png
%{_mandir}/man1/coqide.1*
%{ocamldir}/coqide/
%{_metainfodir}/fr.inria.coqide.metainfo.xml
%{_datadir}/applications/fr.inria.coqide.desktop
%{_datadir}/gtksourceview-3.0/language-specs/coq*.lang
%{_datadir}/gtksourceview-3.0/styles/coq_style.xml
%{_datadir}/mime/packages/coq.xml
%{_sysconfdir}/xdg/coq/

%if %{with doc}
%files doc
%license doc/LICENSE
%{coqdocdir}
%endif

%changelog
%autochangelog
