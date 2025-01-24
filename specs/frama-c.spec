# Coq's plugin architecture requires cmxs files, so:
ExclusiveArch: %{ocaml_native_compiler}

# Without this, gcc flags are passed to frama-c in the test suite
%undefine _auto_set_build_flags

Name:           frama-c
Version:        30.0
Release:        %autorelease
Summary:        Framework for source code analysis of C software

%global pkgversion %{version}-Zinc

# Licensing breakdown in source file frama-c.licensing
License:        LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-2.0-only WITH OCaml-LGPL-linking-exception AND GPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-4.0 AND BSD-3-Clause AND QPL-1.0-INRIA-2004 WITH QPL-1.0-INRIA-2004-exception
URL:            https://frama-c.com/
VCS:            git:https://git.frama-c.com/pub/frama-c.git
Source0:        https://frama-c.com/download/%{name}-%{pkgversion}.tar.gz
Source1:        https://frama-c.com/download/%{name}-%{pkgversion}-api.tar.gz
Source2:        https://frama-c.com/download/%{name}-server-%{pkgversion}-api.tar.gz
Source3:        https://frama-c.com/download/user-manual-%{pkgversion}.pdf
Source4:        https://frama-c.com/download/plugin-development-guide-%{pkgversion}.pdf
Source5:        https://frama-c.com/download/acsl-implementation-%{pkgversion}.pdf
Source6:        https://frama-c.com/download/aorai-manual-%{pkgversion}.pdf
Source7:        https://frama-c.com/download/e-acsl/e-acsl-manual-%{pkgversion}.pdf
Source8:        https://frama-c.com/download/e-acsl/e-acsl-implementation-%{pkgversion}.pdf
Source9:        https://frama-c.com/download/eva-manual-%{pkgversion}.pdf
Source10:       https://frama-c.com/download/metrics-manual-%{pkgversion}.pdf
Source11:       https://frama-c.com/download/rte-manual-%{pkgversion}.pdf
Source12:       https://frama-c.com/download/wp-manual-%{pkgversion}.pdf
# Icons created with gimp from the official upstream icon
Source13:       %{name}-icons.tar.xz
Source14:       com.%{name}.%{name}-gui.desktop
Source15:       com.%{name}.%{name}-gui.metainfo.xml
Source16:       acsl.el
Source17:       frama-c.licensing

# Do not require the bytes library for OCaml 5.x
Patch:          %{name}-bytes.patch

# Expose use of math library symbols to RPM
Patch:          %{name}-mathlib.patch

# Adapt to changes in why3 1.8.0
Patch:          %{name}-why3.1.8.0.patch

# Adapt to changes in C23
Patch:          %{name}-c23.patch

BuildRequires:  alt-ergo
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  emacs-nw
BuildRequires:  fdupes
BuildRequires:  flamegraph
BuildRequires:  graphviz
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-apron-devel
BuildRequires:  ocaml-dune >= 3.13.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-dune-site-devel >= 3.13.0
BuildRequires:  ocaml-lablgtk3-devel >= 3.1.0
BuildRequires:  ocaml-lablgtk3-sourceview3-devel
BuildRequires:  ocaml-menhir >= 20181006
BuildRequires:  ocaml-mlmpfr-devel
BuildRequires:  ocaml-ocamlgraph-devel >= 2.1.0
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppx-deriving-yaml-devel >= 0.2.0
BuildRequires:  ocaml-ppx-deriving-yojson-devel
BuildRequires:  ocaml-unionfind-devel >= 20220107
BuildRequires:  ocaml-why3-devel >= 1.7.1
BuildRequires:  ocaml-yaml-devel >= 3.0.0
BuildRequires:  ocaml-yojson-devel >= 2.0.1
BuildRequires:  ocaml-zarith-devel >= 1.9
BuildRequires:  ocaml-zmq-devel
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  time
BuildRequires:  unix2dos
BuildRequires:  why3
BuildRequires:  yq
BuildRequires:  z3

Requires:       alt-ergo
Requires:       flamegraph
Requires:       gcc
Requires:       graphviz
Requires:       hicolor-icon-theme
Requires:       why3

Recommends:     bash-completion

Suggests:       z3

# Frama-C contains a forked version of ocaml-cil, with incompatible
# modifications from ocaml-cil upstream.
Provides:       bundled(ocaml-cil)

# Do not Require private ocaml interfaces that we don't Provide
%global __requires_exclude ocaml\\\(Driver_ast\\\)

%global _docdir_fmt %{name}

%description
Frama-C is a suite of tools dedicated to the analysis of the source
code of software written in C.

Frama-C gathers several static analysis techniques in a single
collaborative framework. The collaborative approach of Frama-C allows
static analyzers to build upon the results already computed by other
analyzers in the framework. Thanks to this approach, Frama-C provides
sophisticated tools, such as a slicer and dependency analysis.

%package doc
Summary:        Large documentation files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Large documentation files for %{name}.

%package emacs
Summary:        Emacs support file for ACSL markup
License:        LGPL-2.1-only
Requires:       %{name} = %{version}-%{release}
Requires:       emacs(bin)
BuildArch:      noarch

%description emacs
This package contains an Emacs support file for working with C source
files marked up with ACSL.

%prep
%autosetup -p1 -n %{name}-%{pkgversion}
%setup -q -T -D -a 1 -n %{name}-%{pkgversion}
%setup -q -T -D -a 2 -n %{name}-%{pkgversion}
%setup -q -T -D -a 13 -n %{name}-%{pkgversion}

%conf
# Copy in the manuals
mkdir doc/manuals
cp -p %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
   %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} doc/manuals

# Preserve timestamps when installing
sed -ri 's/^CP[[:blank:]]+=.*/& -p/' share/Makefile.common

# Do not use env
%py3_shebang_fix share/analysis-scripts
%py3_shebang_fix share/machdeps
%py3_shebang_fix src/plugins/e-acsl/examples/ensuresec/push-alerts
%py3_shebang_fix src/plugins/e-acsl/scripts
%py3_shebang_fix tests/compliance

%build
%dune_build

%install
%dune_install

# Two of the man pages are duplicates, so make one a link to the other.
cat > %{buildroot}%{_mandir}/man1/frama-c-gui.1 << EOF
.so man1/frama-c.1
EOF

# Install the desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE14}

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE15} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/com.%{name}.%{name}-gui.metainfo.xml

# Install the icons
mkdir -p %{buildroot}%{_datadir}/icons
cp -a icons %{buildroot}%{_datadir}/icons/hicolor

# Install the bash completion file
mkdir -p %{buildroot}%{bash_completions_dir}
cp -p share/autocomplete_frama-c %{buildroot}%{bash_completions_dir}/frama-c

# Install the zsh completion file
mkdir -p %{buildroot}%{zsh_completions_dir}
cp -p share/_frama-c %{buildroot}%{zsh_completions_dir}

# Install and bytecompile the Emacs file
mkdir -p %{buildroot}%{_emacs_sitelispdir}
mv %{buildroot}%{_datadir}/frama-c/share/emacs/*.el %{buildroot}%{_emacs_sitelispdir}
rmdir %{buildroot}%{_datadir}/frama-c/share/emacs
chmod a-x %{buildroot}%{_emacs_sitelispdir}/*.el
cd %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} *.el
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cp -p %{SOURCE16} %{buildroot}%{_emacs_sitestartdir}
cd -

# Remove files we don't actually want
rm -f %{buildroot}%{_datadir}/frama-c/share/{autocomplete,}_frama-c
find %{buildroot}%{_libdir} -name \*.cmo -o -name \*.cmx -o -name \*.o -delete
rm -fr %{buildroot}%{_docdir}/frama-c{,-{dive,e-acsl,instantiate,loop-analysis,markdown-report,nonterm}}
find %{buildroot}%{ocamldir} -name opam -empty -delete

# Rename documentation files so we can have them all
cp -p src/plugins/dive/README.md README.dive.md
cp -p src/plugins/e-acsl/README README.e-acsl
cp -p src/plugins/instantiate/README.md README.instantiate.md
cp -p src/plugins/loop_analysis/README.org README.loop-analysis.org
cp -p src/plugins/markdown-report/README.md README.markdown-report.md
cp -p src/plugins/nonterm/README.md README.nonterm.md

# Unbundle flamegraph
rm -f %{buildroot}%{ocamldir}/frama-c/lib/analysis-scripts/flamegraph.pl
ln -s %{_bindir}/flamegraph.pl \
   %{buildroot}%{ocamldir}/frama-c/lib/analysis-scripts

# Fix a path in e-acsl-gcc.sh
if [ "%{_lib}" != "lib" ]; then
    sed -i '/EACSL_LIB/s,/lib/,/%{_lib}/,' %{buildroot}%{_bindir}/e-acsl-gcc.sh
fi

# Link duplicate files
%fdupes %{buildroot}%{ocamldir}
%fdupes %{buildroot}%{_datadir}/frama-c
%fdupes frama-c-api

# FIXME: tests fail on ppc6le due to redefinition of bool
# FIXME: test issue-eacsl-40.1.exec.wtests fails on aarch64
# FIXME: C23 has wreaked havoc on the test suite
#%%ifarch x86_64
#%%check
#export PYTHONPATH=%%{buildroot}%%{ocamldir}/frama-c/lib/analysis-scripts
#why3 config detect
## Parallel testing sometimes fails
#make default-tests PTESTS_OPTS=-error-code
#%%endif

%files
%doc README.md VERSION
%license licenses/*
%{_bindir}/e-acsl-gcc.sh
%{_bindir}/frama-c*
%{ocamldir}/frama-c*
%{ocamldir}/qed/
%{ocamldir}/stublibs/dllframa_c_kernel_stubs.so
%{ocamldir}/stublibs/dllwp_stubs.so
%{bash_completions_dir}/frama-c
%{zsh_completions_dir}/_frama-c
%{_datadir}/frama-c/
%{_datadir}/frama-c-e-acsl/
%{_datadir}/applications/com.%{name}.%{name}-gui.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/com.%{name}.%{name}-gui.metainfo.xml
%{_mandir}/man1/e-acsl-gcc.sh.1*
%{_mandir}/man1/frama-c.1*
%{_mandir}/man1/frama-c-gui.1*

%files doc
%doc README.dive.md README.e-acsl README.instantiate.md
%doc README.loop-analysis.org README.markdown-report.md README.nonterm.md
%doc doc/manuals/acsl-implementation-%{pkgversion}.pdf
%doc doc/manuals/aorai-manual-%{pkgversion}.pdf
%doc doc/manuals/e-acsl-implementation-%{pkgversion}.pdf
%doc doc/manuals/e-acsl-manual-%{pkgversion}.pdf
%doc doc/manuals/eva-manual-%{pkgversion}.pdf
%doc doc/manuals/metrics-manual-%{pkgversion}.pdf
%doc doc/manuals/plugin-development-guide-%{pkgversion}.pdf
%doc doc/manuals/rte-manual-%{pkgversion}.pdf
%doc doc/manuals/user-manual-%{pkgversion}.pdf
%doc doc/manuals/wp-manual-%{pkgversion}.pdf
%doc frama-c-api
%doc frama-c-server-api

%files emacs
%{_emacs_sitelispdir}/*.el*
%{_emacs_sitestartdir}/acsl.el

%changelog
%autochangelog
