Summary: Symbolic Computation Program
Name:    maxima
Version: 5.47.0

Release: 6%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     http://maxima.sourceforge.net/
Source:  http://downloads.sourceforge.net/sourceforge/maxima/maxima-%{version}%{?beta}.tar.gz
%if 0%{?fedora}
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc sparcv9
%endif
%if 0%{?rhel}
ExclusiveArch: %{ix86} x86_64 ppc sparcv9
%endif

## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=837142
# https://sourceforge.net/tracker/?func=detail&aid=3539587&group_id=4933&atid=104933
Patch50: maxima-5.37.1-clisp-noreadline.patch

# Build the fasl while building the executable to avoid double initialization
# https://github.com/sagemath/sage/blob/develop/build/pkgs/maxima/patches/maxima.system.patch
Patch51: maxima-5.30.0-build-fasl.patch

# handle multiple ldflags in ecl build
Patch52: maxima-ecl_ldflags.patch

# fix matrix exponentiation
# https://gitlab.archlinux.org/archlinux/packaging/packages/maxima/-/raw/main/matrixexp.patch
Patch53: matrixexp.patch

# Use GMP arithmetic with sbcl (Void Linux)
# https://gitlab.archlinux.org/archlinux/packaging/packages/maxima/-/raw/main/maxima-sbcl-gmp.patch
Patch54: maxima-sbcl-gmp.patch

%define maxima_ver %{version}%{?beta}
BuildRequires: make
BuildRequires: emacs
Requires: emacs-filesystem >= %{_emacs_version}
%define texmf %{_datadir}/texmf

%ifarch %{ix86} x86_64
%define default_lisp sbcl
%define _enable_sbcl --enable-sbcl-exec
%if 0%{?fedora} && !0%{?flatpak}
%define _enable_clisp --enable-clisp-exec
#define _enable_ecl --enable-ecl
%define _enable_gcl --enable-gcl
%endif
%endif

%ifarch aarch64
%define default_lisp sbcl
%define _enable_sbcl --enable-sbcl-exec
%if 0%{?fedora} && !0%{?flatpak}
%define _enable_gcl --enable-gcl
#define _enable_ecl --enable-ecl
%endif
%endif

%ifarch %{arm}
%define default_lisp sbcl
%define _enable_sbcl --enable-sbcl-exec
%if 0%{?fedora} && !0%{?flatpak}
#define _enable_gcl --enable-gcl
#define _enable_ecl --enable-ecl
%endif
%endif

%ifarch ppc
%define default_lisp sbcl
%define _enable_sbcl --enable-sbcl-exec
%if 0%{?fedora} && !0%{?flatpak}
# clisp: http://bugzilla.redhat.com/166347 (resolved) - clisp/ppc (still) awol.
#define _enable_clisp --enable-clisp
%define _enable_gcl --enable-gcl
%endif
%endif

%ifarch sparcv9
%define default_lisp sbcl
%define _enable_sbcl --enable-sbcl-exec
%endif

%if "x%{?_enable_cmucl}" == "x%{nil}"
Obsoletes: %{name}-runtime-cmucl < %{version}-%{release}
%endif
%if "x%{?_enable_gcl}" == "x%{nil}"
Obsoletes: %{name}-runtime-gcl < %{version}-%{release}
%endif
%if "x%{?_enable_sbcl}" == "x%{nil}"
Obsoletes: %{name}-runtime-sbcl < %{version}-%{release}
%endif
%if "x%{?_enable_ecl}" == "x%{nil}"
Obsoletes: %{name}-runtime-ecl < %{version}-%{release}
%endif

Source1: maxima.png
Source6: maxima-modes.el

## Other maxima reference docs
Source10: http://starship.python.net/crew/mike/TixMaxima/macref.pdf
Source11: http://maxima.sourceforge.net/docs/maximabook/maximabook-19-Sept-2004.pdf

# Inhibit automatic compressing of info files.
# Compressed info files break maxima's internal help.
%global __spec_install_post %{nil}
# debuginfo.list ends up empty/blank anyway. disable
%global debug_package   %{nil}
# workaround debug-id conflicts (with sbcl)
%global _build_id_links none

# upstream langpack upgrades, +Provides too? -- Rex
Obsoletes: %{name}-lang-es < %{version}-%{release}
Obsoletes: %{name}-lang-es-utf8 < %{version}-%{release}
Obsoletes: %{name}-lang-pt < %{version}-%{release}
Obsoletes: %{name}-lang-pt-utf8 < %{version}-%{release}
Obsoletes: %{name}-lang-pt_BR < %{version}-%{release}
Obsoletes: %{name}-lang-pt_BR-utf8 < %{version}-%{release}

BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(bash-completion)
%global bash_completionsdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo '/etc/bash_completion.d')
BuildRequires: perl-interpreter
BuildRequires: perl(Getopt::Long)
BuildRequires: python3
BuildRequires: %{py3_dist vtk}
BuildRequires: recode
# texi2dvi
BuildRequires: texinfo-tex
BuildRequires: tex(latex)
%if 0%{?fedora}
BuildRequires: tex(fullpage.sty)
%endif
# /usr/bin/wish
BuildRequires: tk
# Needed for the sbcl tests
BuildRequires: gnuplot

Requires: %{name}-runtime%{?default_lisp:-%{default_lisp}} = %{version}-%{release}
Requires: gnuplot
Requires: rlwrap

%description
Maxima is a full symbolic computation program.  It is full featured
doing symbolic manipulation of polynomials, matrices, rational
functions, integration, Todd-coxeter, graphing, bigfloats.  It has a
symbolic debugger source level debugger for maxima code.  Maxima is
based on the original Macsyma developed at MIT in the 1970's.

%package gui
Summary: Tcl/Tk GUI interface for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-xmaxima < %{version}-%{release}
Requires: tk
Requires: xdg-utils
%description gui
Tcl/Tk GUI interface for %{name}

%package src
Summary: %{name} lisp source code
Requires: %{name} = %{version}-%{release}
%description src
%{name} lisp source code.

%if "x%{?_enable_clisp:1}" == "x1"
# to workaround mysterious(?) "cpio: MD5 sum mismatch" errors when installing this subpkg
%define __prelink_undo_cmd %{nil}
#define _with_clisp_runtime --with-clisp-runtime=%%{_libdir}/clisp/base/lisp.run
%package runtime-clisp
Summary: Maxima compiled with clisp
BuildRequires: clisp-devel
%if "%{?_enable_clisp}" != "--enable-clisp-exec"
Requires: clisp
%endif
Requires: %{name} = %{version}-%{release}
Obsoletes: maxima-exec-clisp < %{version}-%{release}
Provides: %{name}-runtime = %{version}-%{release}
%description runtime-clisp
Maxima compiled with Common Lisp (clisp)
%endif

%if "x%{?_enable_cmucl:1}" == "x1"
%define _with_cmucl_runtime --with-cmucl-runtime=%{_prefix}/lib/cmucl/bin/lisp
%package runtime-cmucl
Summary: Maxima compiled with CMUCL
BuildRequires: cmucl
# needed dep somewhere around cmucl-20a -- Rex
Requires: cmucl
Requires:  %{name} = %{version}-%{release}
Obsoletes: maxima-exec-cmucl < %{version}-%{release}
Provides:  %{name}-runtime = %{version}-%{release}
%description runtime-cmucl
Maxima compiled with CMU Common Lisp (cmucl)
%endif

%if "x%{?_enable_gcl:1}" == "x1"
%package runtime-gcl
Summary: Maxima compiled with GCL
BuildRequires: gcl
BuildRequires: gcl-emacs
Requires:  %{name} = %{version}-%{release}
Obsoletes: maxima-exec-gcl < %{version}-%{release}
Provides:  %{name}-runtime = %{version}-%{release}
%description runtime-gcl
Maxima compiled with Gnu Common Lisp (gcl)
%endif

%if "x%{?_enable_sbcl:1}" == "x1"
%package runtime-sbcl
Summary: Maxima compiled with SBCL
BuildRequires: sbcl
BuildRequires: gmp-devel
%if "%{?_enable_sbcl}" != "--enable-sbcl-exec"
# requires the same sbcl it was built against
%global sbcl_vr %(sbcl --version 2>/dev/null | cut -d' ' -f2)
%if "x%{?sbcl_vr}" != "x%{nil}"
Requires: sbcl = %{sbcl_vr}
%else
Requires: sbcl
%endif
%endif
Requires: %{name} = %{version}-%{release}
Obsoletes: maxima-exec-sbcl < %{version}-%{release}
Provides: %{name}-runtime = %{version}-%{release}
%description runtime-sbcl
Maxima compiled with Steel Bank Common Lisp (sbcl).
%endif

%if "x%{?_enable_ecl:1}" == "x1"
%package runtime-ecl
Summary: Maxima compiled with ECL
BuildRequires: ecl
%global ecllib %(ecl -eval "(princ (SI:GET-LIBRARY-PATHNAME))" -eval "(quit)" 2>/dev/null)
Requires: ecl
Requires: %{name} = %{version}-%{release}
Obsoletes: maxima-exec-ecl < %{version}-%{release}
Provides: %{name}-runtime = %{version}-%{release}
%description runtime-ecl
Maxima compiled with Embeddable Common-Lisp (ecl).
%endif

%prep
%autosetup -n %{name}%{!?cvs:-%{version}%{?beta}} -p1

# Extra docs
install -p -m644 %{SOURCE10} .
install -D -p -m644 %{SOURCE11} doc/maximabook/maxima.pdf

sed -i -e 's|@ARCH@|%{_target_cpu}|' src/maxima.in

sed -i -e 's:/usr/local/info:/usr/share/info:' \
  interfaces/emacs/emaxima/maxima.el
sed -i -e \
  's/(defcustom\s+maxima-info-index-file\s+)(\S+)/$1\"maxima.info-16\"/' \
  interfaces/emacs/emaxima/maxima.el

# Avoid obsolescence warnings
sed -i 's/egrep -v/grep -Ev/' configure admin/make_share_list share/Makefile.in


%build
%configure \
  %{?default_lisp:--with-default-lisp=%{default_lisp} } \
  %{?_enable_clisp} %{!?_enable_clisp: --disable-clisp } %{?_with_clisp_runtime} \
  %{?_enable_cmucl} %{!?_enable_cmucl: --disable-cmucl } %{?_with_cmucl_runtime} \
  %{?_enable_gcl}   %{!?_enable_gcl:   --disable-gcl } \
  %{?_enable_sbcl}  %{!?_enable_sbcl:  --disable-sbcl } \
  %{?_enable_ecl}   %{!?_enable_ecl:   --disable-ecl } \
  --enable-lang-es --enable-lang-es-utf8 \
  --enable-lang-pt --enable-lang-pt-utf8 \
  --enable-lang-pt_BR --enable-lang-pt_BR-utf8

# help avoid (re)running makeinfo/tex
touch doc/info/maxima.info \
      share/contrib/maxima-odesolve/kovacicODE.info

%make_build


%install
%make_install bashcompletiondir=%{bash_completionsdir}

%if "x%{?_enable_ecl:1}" == "x1"
install -D -m755 src/binary-ecl/maxima.fas $RPM_BUILD_ROOT%{ecllib}/maxima.fas
%endif

# app icon
install -p -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/maxima.png

install -D -m644 -p %{SOURCE6} $RPM_BUILD_ROOT%{_emacs_sitelispdir}/site_start.d/maxima-modes.el

for file in $RPM_BUILD_ROOT%{_emacs_sitelispdir}/{,site_start.d/}*.el ; do
  %{_emacs_bytecompile} ${file} ||:
done

# emaxima LaTeX style (%%ghost)
install -d $RPM_BUILD_ROOT%{texmf}/tex/latex/
ln -sf  %{_datadir}/maxima/%{maxima_ver}/emacs \
        $RPM_BUILD_ROOT%{texmf}/tex/latex/emaxima

## unwanted/unpackaged files
rm -fv $RPM_BUILD_ROOT%{_infodir}/dir
# docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/maxima/%{maxima_ver}/doc/{contributors,implementation,misc,maximabook,EMaximaIntro.ps}

# _enable_gcl: debuginfo (sometimes?) fails to get auto-created, so we'll help out
touch debugfiles.list


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/net.sourceforge.maxima.xmaxima.desktop
%ifnarch %{ix86}
make -k check ||:
%endif

%triggerin -- tetex-latex,texlive-latex
if [ -d %{texmf}/tex/latex ]; then
  rm -rf %{texmf}/tex/latex/emaxima ||:
  ln -sf %{_datadir}/maxima/%{maxima_ver}/emacs %{texmf}/tex/latex/emaxima ||:
  %{_bindir}/texhash 2> /dev/null ||:
fi

%triggerun -- tetex-latex,texlive-latex
if [ $2 -eq 0 ]; then
  rm -f %{texmf}/tex/latex/emaxima ||:
fi

%files
%license COPYING
%doc AUTHORS ChangeLog README README-lisps.md
%doc doc/implementation/
%doc doc/maximabook/maxima.pdf
%{_bindir}/maxima
%{_bindir}/rmaxima
%dir %{_datadir}/maxima
%dir %{_datadir}/maxima/%{maxima_ver}
%{_datadir}/maxima/%{maxima_ver}/[a-c,f-r,t-w,y-z,A-Z]*
%{_datadir}/maxima/%{maxima_ver}/demo/
%dir %{_datadir}/maxima/%{maxima_ver}/doc/
%dir %{_datadir}/maxima/%{maxima_ver}/doc/html/
%{_datadir}/maxima/%{maxima_ver}/doc/html/figures/
%doc %lang(en) %{_datadir}/maxima/%{maxima_ver}/doc/html/*.h*
%doc %lang(en) %{_datadir}/maxima/%{maxima_ver}/doc/share/
%doc %lang(es) %{_datadir}/maxima/%{maxima_ver}/doc/html/es/
%doc %lang(pt) %{_datadir}/maxima/%{maxima_ver}/doc/html/pt/
%doc %lang(pt_BR) %{_datadir}/maxima/%{maxima_ver}/doc/html/pt_BR/
%{_datadir}/maxima/%{maxima_ver}/share/
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/mime/packages/x-maxima-out.xml
%{bash_completionsdir}/*maxima
# FIXME, copy/move to %%_datadir/icons/hicolor/
%{_datadir}/pixmaps/*maxima*
%dir %{_libdir}/maxima/
%dir %{_libdir}/maxima/%{maxima_ver}/
%{_libexecdir}/maxima
%{_infodir}/imaxima*
%{_infodir}/maxima*
%{_infodir}/abs_integrate.info*
%{_infodir}/drawutils.info*
%{_infodir}/kovacicODE.info*
%{_infodir}/logic.info*
%{_infodir}/nelder_mead.info
%{_infodir}/symplectic_ode.info
%lang(es) %{_infodir}/es*
%lang(pt) %{_infodir}/pt/
%lang(pt_BR) %{_infodir}/pt_BR*
%{_mandir}/man1/maxima.*
%{_mandir}/*/man1/maxima.*
%ghost %{texmf}/tex/latex/emaxima
%{_emacs_sitelispdir}/*
%exclude %{_emacs_sitelispdir}/site_start.d/
%{_emacs_sitelispdir}/site_start.d/*.el*


%files src
%{_datadir}/maxima/%{maxima_ver}/src/

%files gui
%{_bindir}/xmaxima
%{_datadir}/maxima/%{maxima_ver}/xmaxima/
%{_datadir}/applications/net.sourceforge.maxima.xmaxima.desktop
%{_metainfodir}/net.sourceforge.maxima.xmaxima.appdata.xml
%{_datadir}/icons/hicolor/*/*/*
%{_infodir}/xmaxima*

%if "x%{?_enable_clisp:1}" == "x1"
%files runtime-clisp
%{_libdir}/maxima/%{maxima_ver}/binary-clisp
%endif

%if "x%{?_enable_cmucl:1}" == "x1"
%files runtime-cmucl
%{_libdir}/maxima/%{maxima_ver}/binary-cmucl
%endif

%if "x%{?_enable_gcl:1}" == "x1"
%files runtime-gcl
%{_libdir}/maxima/%{maxima_ver}/binary-gcl
%endif

%if "x%{?_enable_sbcl:1}" == "x1"
%files runtime-sbcl
%{_libdir}/maxima/%{maxima_ver}/binary-sbcl
%endif

%if "x%{?_enable_ecl:1}" == "x1"
%files runtime-ecl
%{_libdir}/maxima/%{version}/binary-ecl
%{ecllib}/maxima*.fas
%endif


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.47.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 5.47.0-5
- Disable ECL runtime

* Mon Jul  29 2024 Miroslav Suchý <msuchy@redhat.com> - 5.47.0-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.47.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon May 20 2024 Jerry James <loganjerry@gmail.com> - 5.47.0-2
- Rebuild for ecl 24.5.10

* Tue Feb  6 2024 José Matos <jamatos@fedoraproject.org> - 5.47.0-1
- Update to 5.47.0
- Clean spec a bit
- Add patch to fix matrix exponentiation and GMP arithmetic with sbcl (thanks to Ilia Gradina)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.45.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.45.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 22 2023 Jerry James <loganjerry@gmail.com> - 5.45.1-6
- Rebuild for ecl 23.9.9
- Update deprecated %%patchN usage
- Avoid obsolescence warnings from egrep

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.45.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.45.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.45.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar  7 2022 Jerry James <loganjerry@gmail.com> - 5.45.1-2
- Tweak the previous change to get a valid ECL FASL

* Sat Feb  5 2022 Jerry James <loganjerry@gmail.com> - 5.45.1-1
- Bring back maxima-ecl_ldflags.patch and install maxima.fas again

* Thu Feb  3 2022 José Matos <jamatos@fedoraproject.org> - 5.45.1-1
- update to 5.45.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.43.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Orion Poplawski <orion@nwra.com> - 5.43.2-6
- Rebuild for vtk 9.1.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.43.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.43.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.43.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 5.43.2-2
- Rebuild for ecl 20.4.24
- Add python3 and ecl patches
- BR gcl-emacs to fix emacs byte-compilation error
- Bring texinfo support back

* Wed Apr 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.43.2-1
- 5.43.2

* Fri Feb 28 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.43.0-3
- rebuild (sbcl)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.43.0-1
- maxima-5.43.0
- use %%make_build %%make_install
- update for emacs packaging guidelines

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.42.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Jerry James <loganjerry@gmail.com> - 5.42.1-9
- Rebuild for gcl 2.6.13pre84
- Fix mixed use of spaces and tabs

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.42.1-8
- Rebuild for readline 8.0

* Fri Feb 15 2019 Jerry James <loganjerry@gmail.com> - 5.42.1-7
- Rebuild for gcl 2.6.13pre79
- Drop obsolete post and postun scripts

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.42.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Björn Esser <besser82@fedoraproject.org> - 5.42.1-5
- Rebuilt for libcrypt.so.2 again, the linked libcrypt inherits from clisp

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 5.42.1-4
- Rebuilt for libcrypt.so.2 (#1666033)

* Wed Jan 02 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.42.1-3
- rebuild (sbcl)

* Fri Oct 26 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.1-2
- Fix/enable -ecl support (#1643328)

* Sat Oct 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.1-1
- 5.42.1

* Fri Sep 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.0-1
- 5.42.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.41.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Rex Dieter <rdieter@fedoraproject.org> 5.41.0-7
- rebuild (sbcl), disable gcl f28+

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.41.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 5.41.0-5
- Rebuilt for switch to libxcrypt

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.41.0-4
- Remove obsolete scriptlets

* Fri Dec 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-3
- ignore errors from 'install-info maxima.info' (#1526608)

* Fri Oct 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-2
- rebuild (sbcl)

* Thu Oct 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-1
- 5.41.0

* Fri Sep 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-8
- rebuild (sbcl)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.40.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.40.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-5
- rebuild (sbcl)

* Mon Jun 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-4
- rebuild (sbcl)

* Sun Jun 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-3
- workaround sbcl conflicts: _build_id_links none (#1458416#c2)

* Fri Jun 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-2
- rebuild (sbcl)

* Thu Jun 01 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-1
- 5.40.0

* Wed Mar 29 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-7
- drop desktop vendor hacks
- aarch64: support sbcl (default), gcl for < f26

* Mon Mar 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-6
- rebuild (sbcl)

* Thu Mar 23 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-5
- aarch64: drop gcl (#1435395), use ecl default
- drop BR: time (unused)

* Fri Feb 24 2017 Jerry James <loganjerry@gmail.com> - 5.39.0-4
- rebuild (ecl and clisp)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.39.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 5.39.0-2
- Rebuild for readline 7.x

* Sun Dec 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-1
- maxima-5.39.0

* Wed Sep 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-4
- rebuild (aarch64)

* Tue Aug 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-3
- rebuild (sbcl)

* Fri Apr 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-2
- rebuild (sbcl)

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-1
- maxima-5.38.0

* Wed Mar  9 2016 Jerry James <loganjerry@gmail.com> - 5.37.3-8
- rebuild (ecl)

* Mon Mar 07 2016 Rex Dieter <rdieter@fedoraproject.org> 5.37.3-7
- rebuild (sbcl)

* Sat Mar  5 2016 Jerry James <loganjerry@gmail.com> - 5.37.3-6
- reenable ecl, the problem was with gcl, now fixed

* Sat Mar 05 2016 Rex Dieter <rdieter@fedoraproject.org> 5.37.3-6
- rebuild (sbcl), disable ecl (currently FTBFS) f24+

* Fri Mar  4 2016 Jerry James <loganjerry@gmail.com> - 5.37.3-5
- Rebuild for ecl 16.1.2

* Sat Feb 13 2016 Rex Dieter <rdieter@fedoraproject.org> 5.37.3-4
- xmaxima listed under "Development", not "Science" or "Education" (#1306882)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.37.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 5.37.3-2
- rebuild(sbcl), .spec cosmetics

* Sat Nov 14 2015 Rex Dieter <rdieter@fedoraproject.org> 5.37.3-1
- 5.37.3

* Wed Nov 11 2015 Rex Dieter <rdieter@fedoraproject.org> 5.37.2-4
- rebuild (sbcl)

* Sat Oct  3 2015 Jerry James <loganjerry@gmail.com>  - 5.37.2-3
- Rebuild for ecl 16.0.0

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> 5.37.2-2
- rebuild (sbcl)

* Tue Sep 22 2015 Rex Dieter <rdieter@fedoraproject.org> 5.37.2-1
- 5.37.2 (fixes 'make check')

* Mon Sep 14 2015 Rex Dieter <rdieter@fedoraproject.org> 5.37.1-2
- aarch64: default_lisp gcl

* Mon Sep 14 2015 Rex Dieter <rdieter@fedoraproject.org> 5.37.1-1
- 5.37.1 (#1259886)
- support aarch64 (gcl,ecl) (#926122)
- bump maxima.png icon to 64x64 (#1157589)
- use --enable-clisp-exec,--enable-sbcl-exec

* Mon Jun 22 2015 Rex Dieter <rdieter@fedoraproject.org> 5.36.1-3
- rebuild (sbcl)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.36.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Rex Dieter <rdieter@fedoraproject.org> 5.36.1-2
- uninstallation refers to files that do not exist (#1222229)

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 5.36.1-1
- 5.36.1 (#1217814)

* Thu Apr 30 2015 Rex Dieter <rdieter@fedoraproject.org> 5.35.1-5
- rebuild (sbcl)

* Sat Feb 21 2015 Rex Dieter <rdieter@fedoraproject.org> 5.35.1-4
- ecl fixed, re-enable (#1193134)

* Fri Feb 13 2015 Rex Dieter <rdieter@fedoraproject.org> 5.35.1-3
- rebuild (sbcl)
- %%ix86,x86_64: disable ecl f23+ (#1193134)

* Sat Jan 03 2015 Rex Dieter <rdieter@fedoraproject.org> 5.35.1-2
- rebuild (sbcl)

* Tue Dec 16 2014 Rex Dieter <rdieter@fedoraproject.org> 5.35.1-1
- 5.35.1

* Thu Oct 09 2014 Rex Dieter <rdieter@fedoraproject.org> 5.34.1-2
- rebuild (sbcl)

* Thu Oct 09 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 5.34.1-1
- 5.34.1

* Wed Sep 03 2014 Rex Dieter <rdieter@fedoraproject.org> 5.34.0-1
- 5.34.0

* Thu Aug 21 2014 Rex Dieter <rdieter@fedoraproject.org> 5.33.0-9
- rebuild (sbcl)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.33.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 28 2014 Rex Dieter <rdieter@fedoraproject.org> 5.33.0-7
- rebuild (sbcl)

* Thu Jun 12 2014 Rex Dieter <rdieter@fedoraproject.org> 5.33.0-6
- rebuild (sbcl), arm support/use-by-default sbcl (like other archs)

* Tue Jun 10 2014 Rex Dieter <rdieter@fedoraproject.org> 5.33.0-5
- (re)enable gcl support

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.33.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Rex Dieter <rdieter@fedoraproject.org> 5.33.0-3
- (re)enable ecl support

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 5.33.0-2
- rebuild (sbcl)
- disable gcl/ecl support (rawhide busted atm)

* Tue Apr 08 2014 Rex Dieter <rdieter@fedoraproject.org> 5.33.0-1
- 5.33.0

* Fri Mar 07 2014 Rex Dieter <rdieter@fedoraproject.org> 5.32.1-3
- rebuild (sbcl)

* Wed Jan 29 2014 Rex Dieter <rdieter@fedoraproject.org> 5.32.1-2
- rebuild (sbcl)

* Fri Jan 03 2014 Rex Dieter <rdieter@fedoraproject.org> 5.32.1-1
- 5.32.1

* Thu Dec 26 2013 Rex Dieter <rdieter@fedoraproject.org> 5.32.0-1
- 5.32.0

* Tue Dec 03 2013 Rex Dieter <rdieter@fedoraproject.org> 5.31.3-3
- rebuild (sbcl)

* Fri Nov 01 2013 Rex Dieter <rdieter@fedoraproject.org> 5.31.3-2
- rebuild (sbcl)

* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 5.31.3-1
- 5.31.3

* Sat Oct 05 2013 Rex Dieter <rdieter@fedoraproject.org> 5.31.2-1
- 5.31.2

* Mon Sep 30 2013 Rex Dieter <rdieter@fedoraproject.org> 5.31.1-2
- rebuild (sbcl)

* Fri Sep 27 2013 Rex Dieter <rdieter@fedoraproject.org> 5.31.1-1
- 5.31.1

* Sat Sep 07 2013 Rex Dieter <rdieter@fedoraproject.org> 5.31.0-1
- 5.31.0

* Sat Aug 10 2013 Rex Dieter <rdieter@fedoraproject.org> 5.30.0-8
- build for %%arm too (gcl/ecl support)

* Fri Aug 09 2013 Rex Dieter <rdieter@fedoraproject.org> 5.30.0-7
- rebuild (sbcl)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.30.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Jerry James <loganjerry@gmail.com> - 5.30.0-5
- rebuild (ecl)

* Tue Jun 04 2013 Rex Dieter <rdieter@fedoraproject.org> 5.30.0-4
- rebuild (sbcl)

* Sun Jun 02 2013 Rex Dieter <rdieter@fedoraproject.org> 5.30.0-3
- rebuild (sbcl)

* Mon Apr 29 2013 Rex Dieter <rdieter@fedoraproject.org> 5.30.0-2
- rebuild (sbcl)

* Sat Apr 06 2013 Rex Dieter <rdieter@fedoraproject.org> 5.30.0-1
- 5.3.30

* Wed Feb 27 2013 Rex Dieter <rdieter@fedoraproject.org> 5.29.1-6
- cleaner/simpler workaround to avoid (re)running makeinfo/tex

* Tue Feb 26 2013 Rex Dieter <rdieter@fedoraproject.org> 5.29.1-5
- avoid texinfo on f19+ (#913274)

* Wed Feb 20 2013 Rex Dieter <rdieter@fedoraproject.org> 5.29.1-4
- rebuild (sbcl)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.29.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 5.29.1-2
- rebuild (sbcl)

* Thu Dec 13 2012 Rex Dieter <rdieter@fedoraproject.org> 5.29.1-1
- maxima-5.29.1

* Sat Dec 08 2012 Rex Dieter <rdieter@fedoraproject.org> 5.29.0-3
- wxmaxima_compat patch

* Sat Dec 08 2012 Rex Dieter <rdieter@fedoraproject.org> 5.29.0-2
- rebuild (sbcl)

* Sat Dec 08 2012 Rex Dieter <rdieter@fedoraproject.org> 5.29.0-1
- maxima-5.29.0

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 5.28.0-3
- rebuild (sbcl)

* Sat Oct 27 2012 Rex Dieter <rdieter@fedoraproject.org> 5.28.0-2
- rebuild (sbcl)

* Fri Aug 17 2012 Rex Dieter <rdieter@fedoraproject.org> 5.28.0-1
- maxima-5.28.0

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-11
- rebuild (ecl)

* Tue Aug 07 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-10
- rebuild (sbcl)

* Mon Jul 23 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-9
- rebuild (sbcl)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.27.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-7
- RFE: Add patch to allow disabling readline in maxima-runtime-clisp (#837142)

* Mon Jul 02 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-6
- BR: libffi-devel (workaround ecl bug #837102)

* Mon Jul 02 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-5.1
- enable (only) ecl to highlight ftbfs

* Sun Jul 01 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-5
- disable cmucl (orphaned) support

* Sun Jul 1 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 5.27.0-4
- Enable ecl support.
- Build ecl interface to maxima required by sagemath.

* Tue May 29 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-3
- rebuild (sbcl)

* Thu Apr 12 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-2
- rebuild (sbcl)

* Thu Apr 05 2012 Rex Dieter <rdieter@fedoraproject.org> 5.27.0-1
- 5.27.0

* Wed Jan 18 2012 Rex Dieter <rdieter@fedoraproject.org> 5.26.0-1
- 5.26.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.25.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Rex Dieter <rdieter@fedoraproject.org> 5.25.1-3
- rebuild (sbcl)

* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 5.25.1-2.1
- rebuild with new gmp without compat lib

* Sat Oct 15 2011 Rex Dieter <rdieter@fedoraproject.org> 5.25.1-2
- rebuild (sbcl)

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 5.25.1-1.1
- rebuild with new gmp

* Tue Sep 06 2011 Rex Dieter <rdieter@fedoraproject.org> 5.25.1-1
- maxima-5.25.1

* Mon Aug 22 2011 Rex Dieter <rdieter@fedoraproject.org> 5.25.0-3
- fix sbcl_vr macro usage

* Sun Aug 21 2011 Rex Dieter <rdieter@fedoraproject.org> 5.25.0-1
- maxima-5.25.0

* Fri Jul 15 2011 Rex Dieter <rdieter@fedoraproject.org> 5.24.0-1
- maxima-5.24.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Rex Dieter <rdieter@fedoraproject.org> - 5.23.2-1
- maxima-5.23.2

* Fri Dec 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.23.0-1
- maxima-5.23.0

* Mon Nov 29 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.22.1-6
- rebuild (clisp, libsigsegv)

* Mon Oct 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.22.1-5
- maxima-runtime-cmucl: missing cmucl dependency (#646186)
- tighten -runtime-related deps
- add dep on default runtime
- enable gcl runtime (#496124)

* Thu Sep 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.22.1-4
- rebuild (sbcl)

* Wed Sep 29 2010 jkeating - 5.22.1-3
- Rebuilt for gcc bug 634757

* Sat Sep 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.22.1-2
- rebuild (sbcl)

* Mon Aug 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.22.1-1
- maxima-5.22.1

* Sat Jul 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.21.1-3
- rebuild (sbcl)

* Fri May 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.21.1-2
- rebuild (sbcl)

* Sun Apr 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.21.1-1
- maxima-5.21.1

* Mon Apr 12 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-1
- maxima-5.21.0

* Fri Apr 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.20.1-4
- rebuild (sbcl)

* Tue Feb 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 5.20.1-3
- rebuild (sbcl)

* Wed Dec 16 2009 Stephen Beahm <stephenbeahm@comcast.net> - 5.20.1-2
- enable rmaxima (#551910)

* Tue Dec 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 5.20.1-1
- maxima-5.20.1 (#547012)

* Thu Dec 10 2009 Rex Dieter <rdieter@fedoraproject.org> - 5.20.0-1
- maxima-5.20.0
