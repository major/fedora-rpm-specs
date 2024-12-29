# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/ocaml-omake/omake

Name:           ocaml-omake
Version:        0.10.7
Release:        1%{?dist}
Summary:        Build system with automated dependency analysis

# License breakdown:
# MIT
# - lib/*
#
# LGPLv2 with the OpenSSL and OCaml linking exceptions
# FIXME: This exception probably needs a new SPDX name
# - src/clib/fam_inotify.c
# - src/clib/fam_kqueue.c
# - src/clib/fam_pseudo.h
# - src/clib/fam_win32.c
# - src/clib/lm_channel.c
# - src/clib/lm_compat_win32.c
# - src/clib/lm_compat_win32.h
# - src/clib/lm_ctype.c
# - src/clib/lm_fs_case_sensitive.c
# - src/clib/lm_heap.c
# - src/clib/lm_heap.h
# - src/clib/lm_notify.c
# - src/clib/lm_uname_ext.c
# - src/clib/unixsupport.h
# - src/libmojave/*
#
# GPLv2 with the OCaml linking exception:
# - doc/src/omake-doc.tex
# - src/clib/omake_shell_sys.c
# - src/clib/readline.c
# - src/exec/omake_exec.mli
# - src/exec/omake_exec_notify.ml
# - src/exec/omake_exec_notify.mli
# - src/exec/omake_exec_print.ml
# - src/exec/omake_exec_print.mli
# - src/shell/omake_shell_parse.mly
# - src/shell/omake_shell_sys.mli
# - src/shell/omake_shell_sys_type.ml
#
# GPLv2+:
# - src/clib/lm_termsize.c
# - src/env/omake_exp_lex.mli
# - src/env/omake_exp_parse.mly
License:        MIT AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND GPL-2.0-only WITH OCaml-LGPL-linking-exception AND GPL-2.0-or-later

URL:            http://projects.camlcity.org/projects/omake.html
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/omake-%{version}.tar.gz

# omake can be used on non-OCaml projects (RHBZ#548536).
Provides:       omake

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-findlib
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  hevea


%description
OMake is a build system designed for scalability and portability. It
uses a syntax similar to make utilities you may have used, but it
features many additional enhancements, including the following.

 * Support for projects spanning several directories or directory
   hierarchies.

 * Fast, reliable, automated, scriptable dependency analysis using MD5
   digests, with full support for incremental builds.

 * Dependency analysis takes the command lines into account — whenever
   the command line used to build a target changes, the target is
   considered out-of-date.

 * Fully scriptable, includes a library that providing support for
   standard tasks in C, C++, OCaml, and LaTeX projects, or a mixture
   thereof.


%prep
%autosetup -n omake-omake-%{version}

# Look in the right place for hevea.sty
sed -i 's,\$(HEVEA_DIR)\(/hevea\.sty\),%{_texmf_main}/tex/latex/hevea\1,' doc/OMakefile

# Use the right libdir
if [ "%{_lib}" != "lib" ]; then
    sed -i '/public\.LIBDIR/s,lib,%{_lib},' mk/defaults
    sed -i 's,\(\$(PREFIX)/\)lib,\1%{_lib},g' mk/make_config
fi

# Use the right mandir
sed -i 's,\(\$(PREFIX)/\)man,\1share/man,g' mk/defaults mk/make_config

%ifarch %{ocaml_native_compiler}
# Skip a broken test for cmxs support
sed -i 's/ocamlopt -shared -o \.dummy\.cmxs/true/' lib/build/OCaml.om
%endif


%build
export LIBDIR=%{_libdir}
./configure -prefix %{_prefix}
make all
OMAKELIB=$PWD/lib ./src/main/omake doc pdf
OMAKELIB=$PWD/lib ./src/main/omake doc txt


%install
export LIBDIR=%{_libdir}
make install \
  INSTALL_ROOT=$RPM_BUILD_ROOT
# brp-strip is unable to strip the binary unless it's writable:
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/omake
# Fix other permissions
find $RPM_BUILD_ROOT%{_libdir}/omake -type f -exec chmod 0644 {} +
chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man1/omake.1


%files
%license LICENSE LICENSE.OMake
%doc CONTRIBUTORS.org README.md ChangeLog
%doc doc/txt/omake-doc.txt doc/ps/omake-doc.pdf
%{_libdir}/omake/
%{_bindir}/omake
%{_bindir}/osh
%{_mandir}/man1/omake.1*
%{_mandir}/man1/osh.1*


%changelog
* Thu Dec 26 2024 Jerry James <loganjerry@gmail.com> - 0.10.7-1
- Version 0.10.7
- Adapt to changed hevea path
- Work around a broken test for cmxs support

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-12
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-11
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-8
- Bump release and rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-7
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-6
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-5
- Bump release and rebuild

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-4
- OCaml 5.1 rebuild for Fedora 40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 0.10.6-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 0.10.6-1
- Version 0.10.6
- Convert the License tag to SPDX
- Use the %%license macro
- Build with debuginfo
- Fix hevea detection
- Install man pages
- Fix installation into libdir

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-39
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-36
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-35
- OCaml 4.13.1 rebuild to remove package notes

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-33
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 17:28:29 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-31
- OCaml 4.12.0 build
- Remove dependency on dead.package gamin-devel.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-29
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-28
- OCaml 4.11.0 rebuild

* Mon Aug 03 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-27
- Disable debuginfo.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-24
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-23
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-22
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-21
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-20
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-18
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan 09 2020 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-17
- OCaml 4.09.0 for riscv64

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-16
- OCaml 4.09.0 (final) rebuild.

* Fri Aug 16 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-15
- OCaml 4.08.1 (final) rebuild.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-14
- OCaml 4.08.1 (rc2) rebuild.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-12
- OCaml 4.08.0 (final) rebuild.

* Mon Apr 29 2019 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-11
- OCaml 4.08.0 (beta 3) rebuild.

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.3-10
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-7
- OCaml 4.07.0 (final) rebuild.

* Wed Jun 20 2018 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-6
- OCaml 4.07.0-rc1 rebuild.

* Thu May 17 2018 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-5
- Re-add the dist tag, dropped accidentally in 0.10.3 rebase.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 22 2017 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-3
- Abandon attempts to set LIBDIR, just use /usr/lib instead.

* Wed Nov 08 2017 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-2
- OCaml 4.06.0 rebuild.

* Tue Nov 07 2017 Richard W.M. Jones <rjones@redhat.com> - 0.10.3-1
- New upstream version 0.10.3.
- New upstream website (camlcity.org) and maintainer.
- Modernize the spec file.
- Remove old patches which no longer apply.
- Reenable hevea dependency.
- Remove "cvs_realclean".

* Mon Aug 07 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.29
- OCaml 4.05.0 rebuild.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.6-0.rc1.28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.6-0.rc1.27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.26
- OCaml 4.04.2 rebuild.

* Fri May 12 2017 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.25
- OCaml 4.04.1 rebuild.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.6-0.rc1.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.23
- Rebuild for OCaml 4.04.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8.6-0.rc1.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 05 2016 Richard Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.21
- Use global instead of define.

* Tue Jul 28 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.20
- OCaml 4.02.3 rebuild.

* Wed Jul 22 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.19
- s/390x: Disable stripping on bytecode-only platforms.

* Wed Jun 24 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.18
- ocaml-4.02.2 final rebuild.

* Wed Jun 17 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.17
- ocaml-4.02.2 rebuild.

* Mon Feb 16 2015 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.16
- ocaml-4.02.1 rebuild.

* Sat Aug 30 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.15
- ocaml-4.02.0 final rebuild.

* Sat Aug 23 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.14
- ocaml-4.02.0+rc1 rebuild.

* Mon Aug 18 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.13
- Kill -warn-error option that caused failure to build on OCaml 4.02.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-0.rc1.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Aug 09 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.11
- ocaml-4.02.0-0.8.git10e45753.fc22 rebuild.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.10
- OCaml 4.02.0 beta rebuild.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-0.rc1.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.8
- OCaml 4.01.0 rebuild.
- Modernize the spec file.
- Enable debuginfo.
- Add patch to remove more warnings.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-0.rc1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-0.rc1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.4
- Change Debian patch to disable all compile warnings.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-0.rc1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1.3
- Rebuild for OCaml 4.00.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-0.rc1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.6-0.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan  5 2011 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.6-0.rc1
- New upstream version 0.9.8.6-0.rc1.
- Remove patches - all are upstream.
- Add patch to disable new warning in OCaml 3.12 (by Stephane Glondu).
- No separate omake-ocamldep program.

* Tue Jan  5 2010 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-12
- Use upstream RPM 4.8 OCaml dependency generator.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-11
- Rebuild for OCaml 3.11.2.

* Thu Dec 17 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-10
- Add 'Provides: omake' (RHBZ#548536).
- Remove OCaml from the summary, since omake is not an OCaml-specific tool.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-8
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Tue Mar  3 2009 Caolán McNamara <caolanm@redhat.com> - 0.9.8.5-7
- patch src/libmojave-external/cutil/lm_printf.c rather than
  src/clib/lm_printf.c as the latter is created as a link of the
  former during the build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  6 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-5
- Patch for "attempt to free a non-heap object" (Jakub Jelinek).

* Fri Dec  5 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-4
- Rebuild for OCaml 3.11.0.

* Fri May 16 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-3
- Rebuild with OCaml 3.10.2-2 (fixes bz 445545).

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-2
- Added stdin/stdout fix patch from Debian.

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.8.5-1
- Initial RPM release.
