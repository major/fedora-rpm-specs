# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global forgeurl https://github.com/coccinelle/coccinelle
%global tag 1.3
#global commit 0afff7fab0dde3d100f078ce8fd9688693ec3237
#global date   20230624
Version:       1.3
%forgemeta

# Build the documentation on Fedora only.
%if 0%{?rhel}
%bcond_with doc
%else
%bcond_without doc
%endif

%ifnarch %{ocaml_native_compiler}
# Stripping the binary removes its bytecode payload
%global __strip %{_bindir}/true
%global debug_package %{nil}
%endif

Name:           coccinelle
Release:        1%{?dist}
Summary:        Semantic patching for Linux (spatch)

License:        GPL-2.0-only

URL:            https://coccinelle.lip6.fr/
Source0:        %{forgesource}

# Used for running Python tests.
Source1:        test.c
Source2:        testpy.cocci

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  python3-devel
BuildRequires:  bash-completion
BuildRequires:  make
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-parmap-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ocaml-menhir
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-pyml-devel
BuildRequires:  ocaml-stdcompat-devel
%if %{with doc}
BuildRequires:  latexmk
BuildRequires:  texlive-boxedminipage
BuildRequires:  texlive-comment
BuildRequires:  texlive-endnotes
BuildRequires:  texlive-ifsym
BuildRequires:  texlive-latex
BuildRequires:  texlive-listings
BuildRequires:  texlive-moreverb
BuildRequires:  texlive-multirow
BuildRequires:  texlive-preprint
BuildRequires:  texlive-subfigure
BuildRequires:  texlive-wrapfig
BuildRequires:  texlive-xypic
BuildRequires:  hevea
%endif

# This stops the automatic dependency generator adding some bogus
# OCaml dependencies.  Unfortunately we have to keep adding modules to
# this list every time there is some change in coccinelle.  There
# should be a better way, but I don't know what.
%{lua:
  modules = {
    'Control_flow_c',
    'Cpp_token_c',
    'Danger',
    'Data',
    'Flag_parsing_cocci',
    'Includes',
    'Includes_cache',
    'Lexer_parser',
    'Ograph_extended',
    'Parsing_consistency_c',
    'Parsing_hacks',
    'Parsing_recovery_c',
    'Parsing_stat',
    'Regexp_pcre',
    'Semantic_c',
    'Token_annot',
    'Token_helpers',
    'Token_views_c',
    'Type_annoter_c',
  }
  local arg = "__ocaml_requires_opts"
  for i, m in ipairs(modules) do
    arg = arg .. " -i " .. m .. " -x " .. m
  end
  rpm.define(arg)
}

# RHBZ#725415.
Requires:       ocaml-findlib


%description
Coccinelle is a tool to utilize semantic patches for manipulating C
code.  It was originally designed to ease maintenance of device
drivers in the Linux kernel.


%package bash-completion
Summary:        Bash tab-completion for %{name}
BuildArch:      noarch
Requires:       bash-completion > 2.0
Requires:       %{name} = %{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.


%if %{with doc}
%package doc
Summary:        Documentation for %{name}
License:        GFDL-1.3-no-invariants-only
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}


%description doc
The %{name}-doc package contains documentation for %{name}.
%endif


%package examples
Summary:        Examples for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}


%description examples
The %{name}-examples package contains examples for %{name}.



%prep
%forgeautosetup

# Replace /usr/bin/env shebang with /usr/bin/python3
sed -i '1s_^#!/usr/bin/env python$_#!%{python3}_' tools/pycocci

# Remove .gitignore files.
find -name .gitignore -delete

# Convert a few files to UTF-8 encoding.
for f in demos/demo_rule9/sym53c8xx.res demos/demo_rule9/sym53c8xx.c; do
  mv $f $f.orig
  iconv -f iso-8859-1 -t utf-8 < $f.orig > $f
  rm $f.orig
done

# replace tabs with spaces
find . -iname '*.py' | xargs -I {} sh -exc 'expand -t8 {} > tempfile && mv tempfile {}'

# Properly rebuild Menhir generated files.
rm -f parsing_cocci/parser_cocci_menhir.ml parsing_cocci/parser_cocci_menhir.mli


%build
autoreconf -i
./autogen

%configure \
    --with-python=%{_bindir}/python3 \
    --with-menhir=%{_bindir}/menhir

%{__sed} -i \
  -e 's,LIBDIR=.*,LIBDIR=%{_libdir},' \
  -e 's,MANDIR=.*,MANDIR=%{_mandir},' \
  -e 's,SHAREDIR=.*,SHAREDIR=%{_libdir}/%{name},' \
  -e 's,DYNLINKDIR=.*,DYNLINKDIR=%{_libdir}/ocaml,' \
  -e 's,BASH_COMPLETION_DIR=.*,BASH_COMPLETION_DIR=%{bash_completions_dir},' \
  Makefile.config

# Pass -g option everywhere.
echo '
EXTRA_OCAML_FLAGS = -g
EXTRACFLAGS = $(EXTRA_OCAML_FLAGS)
' > Makefile.local

%ifarch %{ocaml_native_compiler}
target=all-release
%else
target="all-dev docs"
%endif

# NOTE: Do not use smp_mflags!  It breaks the build.
unset MAKEFLAGS

make $target VERBOSE=yes

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python/coccilib
%make_install

# Remove these (they are just wrapper scripts).
rm -f $RPM_BUILD_ROOT%{_bindir}/spatch.byte
rm -f $RPM_BUILD_ROOT%{_bindir}/spatch.opt

# Move the libdir stuff into a subdirectory.
pushd $RPM_BUILD_ROOT%{_libdir}
mkdir coccinelle
mkdir coccinelle/ocaml
for f in standard.h standard.iso spatch spatch.byte spatch.opt ocaml/*; do
  if [ -f $f ]; then
    mv $f coccinelle/$f
  fi
done
popd

# Move Python libraries to python sitelib directory.
mkdir -p $RPM_BUILD_ROOT%{python3_sitelib}
mv $RPM_BUILD_ROOT%{_libdir}/python/coccilib \
  $RPM_BUILD_ROOT%{python3_sitelib}

rmdir $RPM_BUILD_ROOT%{_libdir}/python

mv $RPM_BUILD_ROOT%{_bindir}/spatch $RPM_BUILD_ROOT%{_libdir}/coccinelle

cp -p tools/pycocci $RPM_BUILD_ROOT%{_bindir}/

# wrapper script, sets up env variables
cp -p scripts/spatch.sh $RPM_BUILD_ROOT%{_bindir}/spatch
chmod a+x $RPM_BUILD_ROOT%{_bindir}/spatch


%check
# Run the tests using the non-script version of spatch so that these
# environment variables have effect, since spatch.sh (installed as
# %%{_bindir}/spatch) overwrites them.
export COCCINELLE_HOME=$RPM_BUILD_ROOT%{_libdir}/coccinelle
spatch=$COCCINELLE_HOME/spatch
export LD_LIBRARY_PATH=.
export PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitelib}:$PYTHONPATH

# Run --help to check the command works in general.
$spatch --help

# run the test recommended by the README
$spatch -sp_file demos/simple.cocci demos/simple.c

# test python support is working
# on previously broken builds, spatch exits with 255
$spatch --sp-file %{SOURCE2} %{SOURCE1}


%files
%license license.txt copyright.txt
%doc authors.txt bugs.txt changes.txt
%doc credits.txt install.txt readme.txt
%{_bindir}/pycocci
%{_bindir}/spatch
%{_bindir}/spgen
%{_libdir}/%{name}/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{python3_sitelib}/coccilib/


%files bash-completion
%license license.txt copyright.txt
%dir %{bash_completions_dir}
%{bash_completions_dir}/spatch


%if %{with doc}
%files doc
%doc docs
%endif


%files examples
%doc demos


%changelog
* Fri Dec 27 2024 Jerry James <loganjerry@gmail.com> - 1.3-1
- Build verbosely

* Wed Nov 13 2024 Richard W.M. Jones <rjones@redhat.com> - 1.3-1
- Update to 1.3 (RHBZ#2326000)

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 1.2-8
- Rebuild for ocaml-menhir 20240715

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2-6
- OCaml 5.2.0 ppc64le fix

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2-5
- Rebuilt for Python 3.13

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2-4
- OCaml 5.2.0 for Fedora 41

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2-3
- Revert: Pass -Oclassic to ocamlopt to avoid compilation blow-up

* Mon May 06 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2-2
- Pass -Oclassic to ocamlopt to avoid compilation blow-up

* Thu May 02 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2-1
- Update to 1.2 (RHBZ#2272154)

* Mon Mar 25 2024 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-31
- Use %%{bash_completions_dir} macro

* Mon Jan 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-30
- Bump and rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan  2 2024 Jerry James <loganjerry@gmail.com> - 1.1.1-27
- Rebuild for ocaml-num

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-26
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-25
- OCaml 5.1.1 rebuild for Fedora 40

* Mon Nov  6 2023 Jerry James <loganjerry@gmail.com> - 1.1.1-24.20230624git0afff7f
- Rebuild for ocaml-pyml 20231101

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-23
- OCaml 5.1 rebuild for Fedora 40

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-21
- Bump release and rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-20
- OCaml 5.0 rebuild for Fedora 39

* Thu Jun 29 2023 Jerry James <loganjerry@gmail.com> - 1.1.1-19.20230624git0afff7f
- Update to git HEAD for OCaml 5.0 compatibility
- New project URL
- Drop unneeded workaround for 32-bit ARM

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1.1-18
- Rebuilt for Python 3.12

* Wed Feb 15 2023 Jerry James <loganjerry@gmail.com> - 1.1.1-17
- Rebuild for ocaml-pyml 20220905
- Convert License tags to SPDX

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-16
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 03 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-14
- Switch to using forge macros

* Mon Aug  1 2022 Jerry James <loganjerry@gmail.com> - 1.1.1-13
- Rebuild for ocaml-pyml fixed for python 3.11

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-11
- Rebuild for OCaml 4.14.0 because of Python conflict

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 1.1.1-10
- Rebuilt for Python 3.11

* Sun Jun 19 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-9
- OCaml 4.14.0 rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.1-8
- Rebuilt for Python 3.11

* Fri Mar  4 2022 Jerry James <loganjerry@gmail.com> - 1.1.1-7
- Unbundle stdcompat and pyml
- Change doc and examples to noarch

* Wed Feb 23 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-6
- Build the documentation subpackage on Fedora only.

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-5
- OCaml 4.13.1 rebuild to remove package notes

* Wed Jan 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-4
- Rebuild to pick up new ocaml dependency

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Jerry James <loganjerry@gmail.com> - 1.1.1-2
- Rebuild for ocaml-pcre 7.5.0
- Fetch the official 1.1.1 release tarball
- New URLs
- Drop unused BRs: ocaml-extlib-devel, chrpath
- Add ocaml-parmap-devel BR
- Trim the list of filtered modules
- Mark ocaml-stdcompat as bundled
- Minor spec file cleanups

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.1-1
- New upstream version 1.1.1
- OCaml 4.13.1 build

* Tue Jul 27 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-5
- Rebuild for changed ocamlx(Dynlink)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.10

* Tue Mar  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-2
- New upstream version 1.1.0.
- Add patch to fix OCaml 4.12 issues.
- Fix unwanted dependency (RHBZ#1934137).

* Tue Mar  2 11:16:25 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.18.gitd0fd4c7d
- OCaml 4.12.0 build

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.17.gitd0fd4c7d
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-0.16.gitd0fd4c7d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.15.gitd0fd4c7d
- Fix for Python 3.10 (RHBZ#1896393).

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.14.gitd0fd4c7d
- OCaml 4.11.1 rebuild

* Sat Aug 22 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.13.gitd0fd4c7d
- OCaml 4.11.0 rebuild

* Mon Aug 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.12.gitd0fd4c7d
- Bump and rebuild to fix Dynlink dependency.

* Tue Jul 28 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.11
- Move to git d0fd4c7dfa70763870914eedee7022fa35f700e2.
- Includes the Python 3.9 patches already, so remove those.
- Rewrite BASH_COMPLETION_DIR in configuration.
- Properly rebuild menhir-generated files.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-0.10.6718331f8b574fa4100c7aa82ee4c833a6652ac0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.9.6718331f8b574fa4100c7aa82ee4c833a6652ac0
- Rebuild for updated ocaml-extlib (RHBZ#1837823).

* Sat May 30 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.8.6718331f
- Add fix for Python 3.9.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.9-0.7.111d328fee1303f14a5b9def835301d849e41331
- Rebuilt for Python 3.9

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.6.111d328fee1303f14a5b9def835301d849e41331
- Ignore ocamlx dependencies too.

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.5.111d328fee1303f14a5b9def835301d849e41331
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Wed Apr 22 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.4.111d328fee1303f14a5b9def835301d849e41331
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.3.111d328fee1303f14a5b9def835301d849e41331
- Update all OCaml dependencies for RPM 4.16.

* Wed Mar 25 2020 Jerry James <loganjerry@gmail.com> - 1.0.9-0.2
- Rebuild for ocaml-menhir 20200211

* Wed Mar 25 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.9-0.1
- Package pre-release version which supports OCaml 4.10 (RHBZ#1817182).

* Wed Jan 29 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.8-5
- Remove -unsafe-string.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.8-3
- OCaml 4.10.0+beta1 rebuild.

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.8-2
- OCaml 4.09.0 (final) rebuild.

* Mon Oct 14 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.8-1
- Official 1.0.8 release.

* Tue Sep 24 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.8-0.1
- Add upstream patches so coccinelle builds against OCaml 4.08 (RHBZ#1734855).

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-8
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-6
- Bump and rebuild to fix broken deps.
- Remove camlp4 dependency.
- Remove sexplib dependency.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-4
- Set PYTHONPATH before testing for python support.

* Thu Nov 08 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-3
- Use autogen script and remove redundent autoreconf.
- Eliminate unsupported --enable-release flag for configure, using
  targets instead (all-release when ocamlopt is available).
- Include %%check for python support.
- Run tests against non-script spatch so environment variables have effect.
- Thanks: John Friend.

* Thu Nov 08 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-2
- Second attempt at packaging 1.0.7.
- Different way to rebuild autotools.
- Move spatch binary to %%_libdir/coccinelle and use spatch wrapper script.
- Package spgen.

* Thu Jul 12 2018 Dominique Martinet <asmadeus@codewreck.org> - 1.0.7-1
- Upgrade to new upstream version 1.0.7
- Add -f to the 'remove generated menhir files' because their presence depend
  on the source
- Add another hack to generate a first dummy pyml_stubs lib to make the build
  system happy
- RWMJ: Run autoreconf.
- RWMJ: Add and fix bash-completion subpackage.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-19
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-18
- OCaml 4.07.0-rc1 rebuild.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-17
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-15
- OCaml 4.06.0 rebuild.
- Temporarily enable -unsafe-string.
- Pass -g to all instances of the compiler.

* Wed Aug 09 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-14
- Bump release and rebuild.

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-13
- OCaml 4.05.0 rebuild.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-10
- Bump release and rebuild.

* Tue Jun 27 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-9
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-8
- OCaml 4.04.1 rebuild.

* Wed Feb 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.6-7
- Rebuild for brp-python-bytecompile

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.6-5
- Rebuild for Python 3.6

* Wed Nov 09 2016 Dan Horák <dan@danny.cz> - 1.0.6-4
- remove ExcludeArch

* Tue Nov 08 2016 Richard W.M. Jones <rjones@redhat.com> - 1.0.6-3
- Rebuild for OCaml 4.04.0.
- Hide Get_constants2 internal symbol.

* Mon Oct 31 2016 Richard Jones <rjones@redhat.com> - 1.0.6-1
- New upstream version 1.0.6 (RHBZ#1380000).

* Mon Sep 19 2016 Richard Jones <rjones@redhat.com> - 1.0.5-2
- Install OCaml *.cmi files to get scripting support.

* Tue Jul 19 2016 Richard Jones <rjones@redhat.com> - 1.0.5-1
- New upstream version 1.0.5 (RHBZ#1342701).
- Remove upstream patch.
- Don't use parallel builds.
- Don't package spgen.
- Add BR various texlive-* packages.
- Force configure to use python3.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 02 2016 Tomas Orsava <torsava@redhat.com> - 1.0.4-6
- Fixed shebang pointing to Python instead of Python 3

* Fri Apr 15 2016 Dominika Krejci <dkrejci@redhat.com> - 1.0.4.-5
- Ported for Python 3 (#1313932)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Richard Jones <rjones@redhat.com> - 1.0.4-3
- Apply patch to fix ppc64le builds (thanks Julia Lawall) (RHBZ#1297855).
  See also: https://systeme.lip6.fr/pipermail/cocci/2016-January/thread.html#2742

* Wed Jan 06 2016 Richard Jones <rjones@redhat.com> - 1.0.4-2
- Remove bogus python_sitelib definition.

* Tue Nov  3 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.4-1
- New upstream version 1.0.4.
- Remove the spgen program as it is not meant to be packaged.
- Do not need to delete menhir files.
- Do not install OCaml *.cmi files.

* Tue Oct 27 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-1
- New upstream version 1.0.3.
- Set DYNLINKDIR.
- Unbundle ocaml-menhir, regenerate intermediate parser files.
- Declare that pycaml and parmap are bundled.
- Use 'make world' install of 'make all opt' (see install.txt).
- Add spgen to package.  It's broken at the moment - reported upstream.
- Various BRs required to build the documentation.

* Tue Sep 01 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-1
- New upstream version 1.0.2.
- Use standard configure macro instead of ./configure.
- Various fixes to configuration.
- Package OCaml bindings.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-5
- OCaml 4.02.3 rebuild.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-4
- ocaml-4.02.2 final rebuild.

* Tue Jun 23 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-3
- Put coccinelle data into libdir (instead of /usr/share) since it
  contains the binaries.
- Remove all the code which moved the binaries around.
- Fix the spatch wrapper script to contain the correct directory (RHBZ#1234812)

* Thu Jun 18 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-1
- New upstream version 1.0.1 (RHBZ#1233198).

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-4
- ocaml-4.02.2 rebuild.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-2
- Ignore some more internal module names when generating dependencies.

* Thu Apr 23 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-1
- Version 1.0.0(!)

* Tue Feb 17 2015 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.5
- ocaml-4.02.1 rebuild.

* Sun Aug 31 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.4
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.3
- ocaml-4.02.0+rc1 rebuild.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc21.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 02 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1.1
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc21.1
- New upstream version 1.0.0-rc21.
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc20.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc20.1
- New upstream version 1.0.0-rc20.

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc18.1
- New upstream version 1.0.0-rc18.
- OCaml 4.01.0 rebuild.
- Enable debuginfo.
- Remove strip & prelink hacks.
- Enable test.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc17.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 27 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc17.2
- Ignore a lot more symbols leaked by the library.

* Fri Apr 26 2013 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc17.1
- New upstream version 1.0.0-rc17.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc14.6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Bruno Wolff III <bruno@wolff.to> - 1.0.0-0.rc14.6
- Rebuild for ocaml 4.0.1.

* Tue Jul 31 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc14.5
- Remove sexplib patch which is no longer required by upstream.
- Enable parallel building.

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc14.3
- Confirmed with upstream that *.so files are no longer required.
- Re-enable move of python libs to python library dir.

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc14.2
- New upstream version 1.0.0-rc14.
- +BR ocaml-camlp4-devel

* Mon Jul 30 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc12.3
- New upstream version 1.0.0-rc12.
- Rebuild for OCaml 4.00.0.
- Remove buildroot, defattr, clean for modern RPM.
- Includes bundled extlib.  Disable this by adding BR ocaml-extlib-devel.
- Remove bytecode binary (spatch.byte).
- Fix check rule so it sets COCCINELLE_HOME.
- NB: TEST DISABLED.  UNLIKELY THAT SPATCH FUNCTIONS CORRECTLY.
  + Disable _libdir/*.so stripping.  Why is it not installed?
  + Disable Python stuff.  Why is it not installed?

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.rc9.6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 1.0.0-0.rc9.6.1
- Rebuild against PCRE 8.30

* Wed Feb  1 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc9.6
- Update to 1.0.0-rc9 (requested by Julia Lawall).

* Thu Jan 12 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc8.5
- Ignore Regexp (internal module).

* Sat Jan  7 2012 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc8.3
- Update to 1.0.0-rc8.
- Rebuild for OCaml 3.12.1.
- Use Fedora ocaml-sexplib, ocaml-pcre instead of forked embedded one.

* Mon Jul 25 2011 Richard W.M. Jones <rjones@redhat.com> - 1.0.0-0.rc4.2
- Update to 1.0.0-rc4.
- Requires ocaml-findlib (RHBZ#725415).
- Non-upstream patch to remove use of a couple of functions from the
  forked ocaml sexpr project, so we can use the Fedora one instead.
  See: http://lists.diku.dk/pipermail/cocci/2011-January/001439.html
- Include a new manpage in section 3.

* Wed Mar 30 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc9.1
- Update to 0.2.5-rc9.
- Ignore a bunch more false dependencies.

* Sat Mar  5 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc4.3
- Bump and rebuild to try to fix dependency issue.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-0.rc4.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb  3 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc4.2
- New upstream version 0.2.5-rc4.

* Mon Jan 10 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc1.2
- Bump and rebuild.

* Fri Jan  7 2011 Richard W.M. Jones <rjones@redhat.com> - 0.2.5-0.rc1.1
- New upstream version 0.2.5-rc1.
- Remove upstream patch for Python 2.7.
- Rebuild for OCaml 3.12.0.

* Wed Jul 28 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.2.3-0.rc6.3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 24 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.3-0.rc6.2
- Ignore some bogus generated requires.

* Fri Jul 23 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.3-0.rc6.1
- Fix for Python 2.7.

* Fri Jul 23 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.3-0.rc6
- New upstream version 0.2.3rc6.

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.2.0-0.rc1.2.1
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jan 12 2010 Richard W.M. Jones <rjones@redhat.com> - 0.2.0-0.rc1.2
- New upstream version 0.2.0rc1.

* Thu Nov  5 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-2
- Upstream URL and Source0 changed.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.10-1
- New upstream version 0.1.10.
- Removed patch, since fix to CVE-2009-1753 (RHBZ#502174) is now upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.8-4
- New upstream version 0.1.8.
- Include patch from Debian to fix CVE-2009-1753 (RHBZ#502174).
- Segfaults on PPC64, so added to ExcludeArch.

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Mar 17 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.5-3
- Make the documentation subpackage "-doc" not "-docs".
- Comment about patch0 and send upstream.

* Mon Mar 16 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.5-2
- BR python-devel.

* Mon Mar 16 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.5-1
- New upstream version 0.1.5.
- Use the correct method to get Python sitelib (Michal Schmidt).

* Wed Jan 28 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-8
- Remove useless Makefiles from python/coccilib.
- License is GPLv2 (not GPLv2+).
- Include documentation and demos in subpackages.
- Move python library to a more sensible path.
- Add a check section.

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-6
- Install the shared library in _libdir.
- Install the native code version if we have the optimizing compiler.

* Wed Jan 21 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-3
- Patch for Python 2.6.

* Wed Jan 21 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1.4-2
- Initial RPM release.
