# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Frama-C contains a forked version of ocaml-cil.  We cannot use the Fedora
# ocaml-cil package as a replacement, because Frama-C upstream has modified
# their version in incompatible ways.

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# Without this, gcc flags are passed to frama-c in the test suite
%undefine _auto_set_build_flags

Name:           frama-c
Version:        27.0
Release:        1%{?dist}
Summary:        Framework for source code analysis of C software

%global pkgversion %{version}-Cobalt

# Licensing breakdown in source file frama-c.licensing
License:        LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-2.0-only WITH OCaml-LGPL-linking-exception AND GPL-2.0-or-later AND CC0-1.0 AND CC-BY-SA-4.0 AND BSD-3-Clause AND QPL-1.0-INRIA-2004 WITH QPL-1.0-INRIA-2004-exception
URL:            https://frama-c.com/
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

# why3 is unavailable on i686.  We could build without why3 support, but
# choose to forego i686 support entirely.
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExclusiveArch:  %{java_arches}

BuildRequires:  alt-ergo
BuildRequires:  appstream
BuildRequires:  clang
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  emacs-nox
BuildRequires:  flamegraph
BuildRequires:  graphviz
BuildRequires:  libgnomecanvas-devel
BuildRequires:  make
BuildRequires:  ocaml >= 4.11.1
BuildRequires:  ocaml-apron-devel
BuildRequires:  ocaml-dune >= 3.2.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-dune-site-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-lablgtk3-devel >= 3.1.0
BuildRequires:  ocaml-lablgtk3-sourceview3-devel
BuildRequires:  ocaml-menhir >= 20181006
BuildRequires:  ocaml-mlmpfr-devel
BuildRequires:  ocaml-ocamlgraph-devel >= 1.8.8
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-ppx-deriving-yaml-devel >= 0.2.0
BuildRequires:  ocaml-ppx-deriving-yojson-devel
BuildRequires:  ocaml-ppx-import-devel
BuildRequires:  ocaml-why3-devel >= 1.6.0
BuildRequires:  ocaml-yaml-devel >= 3.0.0
BuildRequires:  ocaml-yojson-devel >= 2.0.1
BuildRequires:  ocaml-zarith-devel >= 1.5
BuildRequires:  ocaml-zmq-devel
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  time
BuildRequires:  unix2dos
BuildRequires:  why3
BuildRequires:  z3

Requires:       alt-ergo
Requires:       flamegraph
Requires:       gcc
Requires:       graphviz
Requires:       hicolor-icon-theme
Requires:       ocaml-ppx-import
Requires:       why3

Recommends:     bash-completion

Suggests:       z3

# Do not Require private ocaml interfaces that we don't Provide
%global __requires_exclude ocaml\\\(Driver_ast\\\)

# This can be removed when Fedora 38 reaches EOL
Obsoletes:      frama-c-xemacs < 23.1-2

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
%autosetup -n %{name}-%{pkgversion}
%setup -q -T -D -a 1 -n %{name}-%{pkgversion}
%setup -q -T -D -a 2 -n %{name}-%{pkgversion}
%setup -q -T -D -a 13 -n %{name}-%{pkgversion}

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
%make_build RELEASE=yes DUNE_DISPLAY=verbose VERBOSEMAKE=yes

%install
# Upstream's installation method leaves the buildroot path in many installed
# files.  Substitute our preferred installation method.
sed -i 's|\(dune install\) --root.*|\1 --destdir=%{buildroot} --verbose --release %{_smp_mflags}|' share/Makefile.installation

# Install
%make_install PREFIX=%{_prefix} MANDIR=%{_mandir} RELEASE=yes \
  DUNE_DISPLAY=verbose VERBOSEMAKE=yes

# Move the doc directory to the right place
mv %{buildroot}%{_prefix}/doc %{buildroot}%{_datadir}

# Move the OCaml directories to the right place
mkdir -p %{buildroot}%{ocamldir}
mv %{buildroot}%{_prefix}/lib/{frama,qed,stublibs}* %{buildroot}%{ocamldir}

# Two of the man pages are duplicates, so make one a link to the other.
cat > %{buildroot}%{_mandir}/man1/frama-c-gui.1 << EOF
.so man1/frama-c.1
EOF

# Install the desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE14}

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE15} %{buildroot}%{_metainfodir}
appstreamcli validate --no-net \
  %{buildroot}%{_metainfodir}/com.%{name}.%{name}-gui.metainfo.xml

# Install the icons
mkdir -p %{buildroot}%{_datadir}/icons
cp -a icons %{buildroot}%{_datadir}/icons/hicolor

# Install the bash completion file
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp -p share/autocomplete_frama-c \
   %{buildroot}%{_datadir}/bash-completion/completions/frama-c

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
rm -f %{buildroot}%{_datadir}/frama-c/share/autocomplete_frama-c
find %{buildroot}%{_libdir} -name \*.cmo -o -name \*.cmx -o -name \*.o -delete
rm -fr %{buildroot}%{_docdir}/frama-c{,-{dive,e-acsl,instantiate,loop-analysis,markdown-report,nonterm}}

# Rename documentation files so we can have them all
cp -p src/plugins/dive/README.md README.dive.md
cp -p src/plugins/e-acsl/README README.e-acsl
cp -p src/plugins/instantiate/README.md README.instantiate.md
cp -p src/plugins/loop_analysis/README.org README.loop-analysis.org
cp -p src/plugins/markdown-report/README.md README.markdown-report.md
cp -p src/plugins/nonterm/README.md README.nonterm.md

# We can't ship ivette until Fedora can support Electron apps
rm %{buildroot}%{_bindir}/ivette %{buildroot}%{ocamldir}/frama-c/ivette.tgz

# Unbundle flamegraph
rm -f %{buildroot}%{ocamldir}/frama-c/lib/analysis-scripts/flamegraph.pl
ln -s %{_bindir}/flamegraph.pl \
   %{buildroot}%{ocamldir}/frama-c/lib/analysis-scripts

# Fix a path in e-acsl-gcc.sh
if [ "%{_lib}" != "lib" ]; then
    sed -i '/EACSL_LIB/s,/lib/,/%{_lib}/,' %{buildroot}%{_bindir}/e-acsl-gcc.sh
fi

# FIXME: tests fail on ppc6le due to redefinition of bool
%ifnarch ppc64le
%check
export PYTHONPATH=%{buildroot}%{ocamldir}/frama-c/lib/analysis-scripts
why3 config detect
# Parallel testing sometimes fails
make default-tests PTESTS_OPTS=-error-code
%endif

%files
%doc README.md VERSION
%license licenses/*
%{_bindir}/e-acsl-gcc.sh
%{_bindir}/frama-c*
%{ocamldir}/frama-c*
%{ocamldir}/qed/
%{ocamldir}/stublibs/dllframa_c_kernel_stubs.so
%{_datadir}/frama-c/
%{_datadir}/frama-c-e-acsl/
%{_datadir}/applications/com.%{name}.%{name}-gui.desktop
%{_datadir}/bash-completion/completions/frama-c
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
* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 27.0-1
- Version 27.0

* Sat Jun 10 2023 Jerry James <loganjerry@gmail.com> - 26.1-2
- Rebuild for ocaml-dune-site 3.8.1

* Wed Feb 15 2023 Jerry James <loganjerry@gmail.com> - 26.1-1
- Version 26.1

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 26.0-5
- Bump release and rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 26.0-4
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Jerry James <loganjerry@gmail.com> - 26.0-2
- Rebuild to fix ocaml-dune-site dependency

* Sat Nov 26 2022 Jerry James <loganjerry@gmail.com> - 26.0-1
- Version 26.0
- Add Requires on ppx_import (bz 2148391)

* Tue Nov  1 2022 Jerry James <loganjerry@gmail.com> - 25.0-7
- Rebuild for ocaml-ppxlib 0.28.0

* Sat Oct 29 2022 Jerry James <loganjerry@gmail.com> - 25.0-6
- Fix a path in e-acsl-gcc.sh (bz 2137875)

* Tue Oct 18 2022 Jerry James <loganjerry@gmail.com> - 25.0-5
- Rebuild for ocaml-stdint 0.7.1

* Fri Sep 16 2022 Jerry James <loganjerry@gmail.com> - 25.0-4
- Rebuild for why3 1.5.1

* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 25.0-3
- Rebuild for ocaml-ppx-deriving-yojson 3.7.0
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 25.0-1
- Remove i686 support

* Thu Jul  7 2022 Jerry James <loganjerry@gmail.com> - 25.0-1
- Version 25.0
- Drop coq 8.14 compatibility patch
- Drop coq BR; coq is now invoked via why3

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 24.0-7
- OCaml 4.14.0 rebuild

* Fri Mar 25 2022 Jerry James <loganjerry@gmail.com> - 24.0-6
- Rebuild for coq 8.15.1 and ocaml-zmq 5.1.5

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 24.0-5
- Rebuild for coq 8.15.0 and why3 1.4.1

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 24.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 24.0-2
- Rebuild for ocaml-ppxlib 0.24.0

* Tue Dec  7 2021 Jerry James <loganjerry@gmail.com> - 24.0-1
- Version 24.0
- Drop upstreamed fix for OCaml 4.13

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 23.1-5
- Rebuild for coq 8.14.1 and ocaml-sexplib0 0.15.0

* Thu Oct 21 2021 Jerry James <loganjerry@gmail.com> - 23.1-4
- Rebuild for coq 8.14.0 and ocaml-zmq 5.1.4
- Add -coq8.14 patch
- Drop XEmacs support

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 23.1-3
- OCaml 4.13.1 build

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 23.1-2
- Try to build on s390x with OCaml 4.13

* Wed Aug 11 2021 Jerry James <loganjerry@gmail.com> - 23.1-1
- Version 23.1

* Fri Jul 30 2021 Jerry James <loganjerry@gmail.com> - 23.0-3
- Rebuild for changed ocamlx(Dynlink)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Jerry James <loganjerry@gmail.com> - 23.0-1
- Update to Vanadium 23.0

* Tue Jun  8 2021 Jerry James <loganjerry@gmail.com> - 22.0-11
- Rebuild for ocaml-ocamlgraph 2.0.0

* Mon Mar 15 2021 Richard W.M. Jones <rjones@redhat.com> - 22.0-10
- Bump and rebuild for updated ocaml-findlib.

* Wed Mar  3 2021 Jerry James <loganjerry@gmail.com> - 22.0-9
- Rebuild for coq 8.13.1 and ocaml-zarith 1.12

* Tue Mar  2 11:40:01 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 22.0-8
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 22.0-7
- Rebuild for coq 8.13.0
- Update metainfo and install in metainfodir

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  2 2021 Jerry James <loganjerry@gmail.com> - 22.0-5
- Rebuild for flocq 3.4.0

* Wed Dec 23 2020 Jerry James <loganjerry@gmail.com> - 22.0-4
- Rebuild for coq 8.12.2

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 22.0-3
- Rebuild for ocaml-ppx-deriving-yojson 3.6.1

* Wed Dec  2 2020 Jerry James <loganjerry@gmail.com> - 22.0-2
- Rebuild for coq 8.12.1

* Fri Nov 20 2020 Jerry James <loganjerry@gmail.com> - 22.0-1
- Update to Titanium 22.0
- Add %%check script

* Mon Nov 16 2020 Jerry James <loganjerry@gmail.com> - 21.1-7
- Rebuild for ocaml-zarith 1.11

* Fri Sep 25 2020 Jerry James <loganjerry@gmail.com> - 21.1-6
- Rebuild for apron 0.9.13 and why3 1.3.3

* Wed Sep 02 2020 Richard W.M. Jones <rjones@redhat.com> - 21.1-5
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020 Jerry James <loganjerry@gmail.com> - 21.1-4
- Rebuild for coq 8.12.0

* Mon Aug 24 2020 Richard W.M. Jones <rjones@redhat.com> - 21.1-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jerry James <loganjerry@gmail.com> - 21.1-1
- Update to Scandium 21.1

* Mon Jun 15 2020 Jerry James <loganjerry@gmail.com> - 21.0-2
- Rebuild for coq 8.11.2

* Sat Jun 13 2020 Jerry James <loganjerry@gmail.com> - 21.0-1
- Update to Scandium 21.0
- Drop upstreamed -why3 patch

* Wed May 20 2020 Jerry James <loganjerry@gmail.com> - 20.0-4
- Rebuild for coq 8.11.1

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 20.0-3
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Sun Apr 05 2020 Richard W.M. Jones <rjones@redhat.com> - 20.0-2
- Update all OCaml dependencies for RPM 4.16.

* Wed Mar 25 2020 Jerry James <loganjerry@gmail.com> - 20.0-1
- Update to Calcium 20.0

* Thu Jan 23 2020 Jerry James <loganjerry@gmail.com> - 19.1-5
- Rebuild for apron 0.9.12

* Mon Dec  9 2019 Jerry James <loganjerry@gmail.com> - 19.1-4
- OCaml 4.09.0 (final) rebuild.

* Tue Oct 29 2019 Jerry James <loganjerry@gmail.com> - 19.1-3
- Rebuild for why3 1.2.1

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 19.1-2
- Rebuild for ocaml-menhir 20190924

* Mon Sep 23 2019 Jerry James <loganjerry@gmail.com> - 19.1-1
- Update to Potassium 19.1

* Fri Sep  6 2019 Jerry James <loganjerry@gmail.com> - 19.0-3
- Unbundle flamegraph
- Install bash completions in the right place

* Fri Aug  2 2019 Jerry James <loganjerry@gmail.com> - 19.0-2
- Fix list of filtered requires

* Tue Jul 30 2019 Jerry James <loganjerry@gmail.com> - 19.0-1
- Update to Potassium version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 18.0-1
- Update to Argon version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 17.0-1
- Update to Chlorine version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 16.0-1
- Update to Sulfur version
- Drop upstreamed -safe-string patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 15.0-7
- Remove obsolete scriptlets

* Sat Dec  9 2017 Jerry James <loganjerry@gmail.com> - 15.0-6
- Rebuild for why3 0.88.2

* Mon Dec  4 2017 Jerry James <loganjerry@gmail.com> - 15.0-5
- Rebuild for mlgmpidl

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 15.0-4
- OCaml 4.06.0 rebuild.

* Sat Oct  7 2017 Jerry James <loganjerry@gmail.com> - 15.0-3
- Rebuild for why3 0.88.0

* Tue Sep 12 2017 Jerry James <loganjerry@gmail.com> - 15.0-2
- More excludes so that provides match requires

* Thu Sep  7 2017 Jerry James <loganjerry@gmail.com> - 15.0-1
- Update to Phosphorus version
- Switch to new upstream version numbering scheme
- Install the bash completion file

* Wed Sep 06 2017 Richard W.M. Jones <rjones@redhat.com> - 1.14-6
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.14-3
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.14-2
- OCaml 4.04.1 rebuild.

* Fri Mar 24 2017 Jerry James <loganjerry@gmail.com> - 1.14-1
- Update to Silicon version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jerry James <loganjerry@gmail.com> - 1.13-7
- Rebuild for coq 8.6

* Wed Nov 30 2016 Jerry James <loganjerry@gmail.com> - 1.13-6
- Rebuild for alt-ergo 1.30

* Mon Nov 07 2016 Richard W.M. Jones <rjones@redhat.com> - 1.13-5
- Rebuild for OCaml 4.04.0.
- Add small fixes for OCaml 4.04.0.

* Fri Oct 28 2016 Jerry James <loganjerry@gmail.com> - 1.13-4
- Rebuild for coq 8.5pl3
- Remove obsolete scriptlets

* Thu Sep  1 2016 Jerry James <loganjerry@gmail.com> - 1.13-3
- Rebuild for why3 0.87.2

* Wed Jul 13 2016 Jerry James <loganjerry@gmail.com> - 1.13-2
- Rebuild for coq 8.5pl2
- Require ocaml-findlib (bz 1354515)

* Wed Jun  1 2016 Jerry James <loganjerry@gmail.com> - 1.13-1
- Update to Aluminium version

* Fri Apr 22 2016 Jerry James <loganjerry@gmail.com> - 1.12-4
- Rebuild for coq 8.5pl1

* Sat Apr 16 2016 Jerry James <loganjerry@gmail.com> - 1.12-3
- Rebuild for ocaml-ocamlgraph 1.8.7

* Fri Mar 18 2016 Jerry James <loganjerry@gmail.com> - 1.12-2
- Rebuild for why3 0.87.0

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 1.12-1
- Update to Magnesium version
- Drop unneeded -why patch

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Jerry James <loganjerry@gmail.com> - 1.11-9
- Rebuild for ocaml-zarith 1.4.1

* Thu Jul 30 2015 Richard W.M. Jones <rjones@redhat.com> - 1.11-8
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.11-7
- ocaml-4.02.2 final rebuild.

* Mon Jun 22 2015 Jerry James <loganjerry@gmail.com> - 1.11-6
- Rebuild for why3 0.86.1

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.11-5
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jerry James <loganjerry@gmail.com> - 1.11-3
- Rebuild for why3 0.86

* Sat Apr 11 2015 Jerry James <loganjerry@gmail.com> - 1.11-2
- Rebuild for coq 8.4pl6

* Wed Mar 18 2015 Jerry James <loganjerry@gmail.com> - 1.11-1
- Update to Sodium version
- Drop all patches; all have been upstreamed
- Add -why patch to fix the why build

* Wed Feb 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.10-21
- ocaml-4.02.1 rebuild.

* Thu Oct 30 2014 Jerry James <loganjerry@gmail.com> - 1.10-20
- Rebuild for coq 8.4pl5

* Tue Oct 14 2014 Jerry James <loganjerry@gmail.com> - 1.10-19
- Rebuild for ocaml-zarith 1.3

* Thu Sep 18 2014 Jerry James <loganjerry@gmail.com> - 1.10-18
- Bump release and rebuild

* Thu Sep 18 2014 Jerry James <loganjerry@gmail.com> - 1.10-17
- Rebuild for why3 0.85

* Thu Sep  4 2014 Jerry James <loganjerry@gmail.com> - 1.10-16
- Adapt to why3 0.84

* Tue Sep  2 2014 Jerry James <loganjerry@gmail.com> - 1.10-15
- Rebuild for final ocaml 4.02.0 release
- Fix license handling

* Mon Aug 25 2014 Jerry James <loganjerry@gmail.com> - 1.10-14
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Richard W.M. Jones <rjones@redhat.com> - 1.10-12
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Aug  4 2014 Jerry James <loganjerry@gmail.com> - 1.10-11
- BR emacs instead of emacs-nox, which has gone away

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 1.10-11
- Bump release and rebuild.

* Fri Aug 01 2014 Richard W.M. Jones <rjones@redhat.com> - 1.10-10
- Bump release and rebuild.

* Fri Jul 25 2014 Richard W.M. Jones <rjones@redhat.com> - 1.10-9
- Rebuild for OCaml 4.02.0 beta.

* Mon Jul 21 2014 Jerry James <loganjerry@gmail.com> - 1.10-8
- Add comment to desktop file

* Thu Jun 26 2014 Jerry James <loganjerry@gmail.com> - 1.10-7
- Set LDFLAGS in a less destructive way (bz 1105265)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Jerry James <loganjerry@gmail.com> - 1.10-5
- Rebuild for coq 8.4pl4

* Mon Apr 21 2014 Jerry James <loganjerry@gmail.com> - 1.10-4
- Rebuild for ocamlgraph 1.8.5; add -ocamlgraph patch to adapt

* Tue Apr 15 2014 Richard W.M. Jones <rjones@redhat.com> - 1.10-3
- Remove ocaml_arches macro (RHBZ#1087794).

* Mon Mar 24 2014 Jerry James <loganjerry@gmail.com> - 1.10-2
- Fix the icon name in the desktop file
- Install icons
- Drop unnecessary gmp-devel BR (pulled in by ocaml-zarith-devel)
- Fix permissions later, else they get reset to the bad values

* Mon Mar 17 2014 Jerry James <loganjerry@gmail.com> - 1.10-1
- Update to Neon version
- All patches have been upstreamed; drop them
- The manuals are no longer included in the source distribution; add as Sources
- BR ocaml-findlib instead of ocaml-findlib-devel
- BR why3 to get coq + why3 support in the wp plugin

* Wed Feb 26 2014 Jerry James <loganjerry@gmail.com> - 1.9-9
- Rebuild for ocaml-ocamlgraph 1.8.4; add -ocamlgraph patch to adapt.
- Add an Appdata file.

* Wed Oct 02 2013 Richard W.M. Jones <rjones@redhat.com> - 1.9-8
- Rebuild for ocaml-lablgtk 2.18.

* Mon Sep 16 2013 Jerry James <loganjerry@gmail.com> - 1.9-7
- Rebuild for OCaml 4.01.0
- Enable debuginfo

* Fri Aug  9 2013 Jerry James <loganjerry@gmail.com> - 1.9-6
- Update -fixes patch to fix startup failures on ARM

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Jerry James <loganjerry@gmail.com> - 1.9-4
- Update to 20130601 bugfix Fluorine release

* Mon Jun  3 2013 Jerry James <loganjerry@gmail.com> - 1.9-3
- Add -fixes patch to fix code generation for inductive definitions

* Thu May 23 2013 Jerry James <loganjerry@gmail.com> - 1.9-2
- Update to bugfix Fluorine release

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 1.9-1
- Update to Fluorine version
- Merge -devel into the main package (bz 888865)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Jerry James <loganjerry@gmail.com> - 1.8-5
- Rebuild for coq 8.4pl1 and alt-ergo 0.95

* Mon Nov  5 2012 Jerry James <loganjerry@gmail.com> - 1.8-4
- Build with zarith support

* Mon Oct 22 2012 Jerry James <loganjerry@gmail.com> - 1.8-3
- Update the Requires filter even more for Oxygen

* Mon Oct 22 2012 Jerry James <loganjerry@gmail.com> - 1.8-2
- Update the Requires filter for Oxygen

* Fri Oct 19 2012 Jerry James <loganjerry@gmail.com> - 1.8-1
- Update to Oxygen version

* Tue Sep 11 2012 Jerry James <loganjerry@gmail.com> - 1.7-9
- Disable dangerous code in src/type/type.ml that leads to segfaults.

* Mon Aug 27 2012 Jerry James <loganjerry@gmail.com> - 1.7-8
- Use a vastly simpler patch for OCaml 4 that fixes the native build.

* Fri Aug  3 2012 Jerry James <loganjerry@gmail.com> - 1.7-7
- Shipping the bytecode version works better if it isn't stripped.

* Fri Aug  3 2012 Jerry James <loganjerry@gmail.com> - 1.7-6
- Use upstream's version of the ocamlgraph patch.
- Ship the bytecode binaries until the native breakage is diagnosed.

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.7-5
- Rebuild for OCaml 4.00.0 official.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 1.7-3
- Rebuild for OCaml 3.12.1

* Tue Nov  8 2011 Jerry James <loganjerry@gmail.com> - 1.7-2
- Rebuild to eliminate libpng dependency

* Tue Oct 25 2011 Jerry James <loganjerry@gmail.com> - 1.7-1
- Update to Nitrogen version

* Mon Jul 11 2011 Jerry James <loganjerry@gmail.com> - 1.6-1
- Update to Carbon version
- Removed unnecessary spec file elements (BuildRoot, etc.)
- Update approach to filtering provides and requires
- Do not filter as much; why should Require some of the filtered names
- Add (X)Emacs support packages
- Add doc subpackage to hold large manual PDFs
- Support for gtksourceview 1.x has been dropped

* Wed Apr 13 2011 Karsten Hopp <karsten@redhat.com> 1.5-3.1
- add ppc64 to archs with ocaml

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Dan Horák <dan[at]danny.cz> - 1.5-2
- updated the supported arch list

* Sat Jul 17 2010 Mark Rader <msrader@gmail.com> 1.5-1
- Upgraded Frama C to Boron version and added ltl2ba dependencies.

* Mon Jul 05 2010 Mark Rader <msrader@gmail.com> 1.4-4
- Modified spec file to add new OCAML dependency structure for FC-13

* Sun Jun 06 2010 Mark Rader <msrader@gmail.com> 1.4-3
- Added documentation to explain the various licensing entries.
- Added .desktop file

* Wed May 26 2010 Mark Rader <msrader@gmail.com> 1.4-2
- Add SELinux context settings.

* Wed Feb 10 2010 Alan Dunn <amdunn@gmail.com> 1.4-1
- Initial Fedora RPM
