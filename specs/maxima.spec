%bcond tests 1

Summary: Symbolic Computation Program
Name:    maxima
Version: 5.50.0
Release: %autorelease
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://maxima.sourceforge.io/
Source:  https://downloads.sourceforge.net/sourceforge/maxima/maxima-%{version}%{?beta}.tar.gz

## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=837142
# https://sourceforge.net/tracker/?func=detail&aid=3539587&group_id=4933&atid=104933
Patch50: maxima-5.37.1-clisp-noreadline.patch

# Build the fasl while building the executable to avoid double initialization
# https://github.com/sagemath/sage/blob/develop/build/pkgs/maxima/patches/maxima.system.patch
Patch51: maxima-5.30.0-build-fasl.patch

# handle multiple ldflags in ecl build
# https://gitlab.archlinux.org/archlinux/packaging/packages/maxima/-/blob/main/0001-ECL-Fix-autoconf-options-on-whitespace.patch
Patch52: maxima-ecl_ldflags.patch

# Use GMP arithmetic with sbcl (Void Linux)
# https://gitlab.archlinux.org/archlinux/packaging/packages/maxima/-/raw/main/maxima-sbcl-gmp.patch
Patch54: maxima-sbcl-gmp.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

%define maxima_ver %{version}%{?beta}
BuildRequires: make
BuildRequires: emacs
Requires: emacs-filesystem >= %{_emacs_version}
%define texmf %{_datadir}/texmf

# overridden below for some arches
%define default_lisp gcl
# available on all arches
%define _enable_gcl --enable-gcl

# not available for s390x
%ifarch x86_64 aarch64 ppc64le riscv64
%define default_lisp sbcl
%define _enable_sbcl --enable-sbcl-exec
%endif

# not available for riscv64
%ifarch x86_64 aarch64 ppc64le s390x
%define _enable_clisp --enable-clisp-exec
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

BuildRequires: desktop-file-utils
BuildRequires: ImageMagick
BuildRequires: pkgconfig(bash-completion)
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
# tcl9.patch makes this incompatible with 8.6
BuildRequires: tk >= 1:9.0
# Needed for the sbcl tests
BuildRequires: gnuplot

Requires: %{name}-runtime = %{version}-%{release}
Suggests: %{name}-runtime%{?default_lisp:-%{default_lisp}} = %{version}-%{release}

Requires: gnuplot
Requires: rlwrap
Requires: hicolor-icon-theme

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
# tcl9.patch makes this incompatible with 8.6
Requires: tk >= 1:9.0
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
%make_install bashcompletiondir=%{bash_completions_dir}

%if "x%{?_enable_ecl:1}" == "x1"
install -D -m755 src/binary-ecl/maxima.fas $RPM_BUILD_ROOT%{ecllib}/maxima.fas
%endif

# app icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/{apps,mimetypes}
mv $RPM_BUILD_ROOT%{_datadir}/icons/text-x-maxima*.svg \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/mimetypes/
mv $RPM_BUILD_ROOT%{_datadir}/icons/xmaxima.svg \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/

# icon is nonstandard size (135x135)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
convert -resize 128x128 $RPM_BUILD_ROOT%{_datadir}/icons/xmaxima.png \
       $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/xmaxima.png
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/xmaxima.png

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
desktop-file-validate %{buildroot}%{_datadir}/applications/Xmaxima.desktop
%if %{with tests}
make -k check || cat tests/test-suite.log
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
%doc %lang(en) %{_datadir}/maxima/%{maxima_ver}/doc/html/manual.css
%doc %lang(en) %{_datadir}/maxima/%{maxima_ver}/doc/share/
%doc %lang(es) %{_datadir}/maxima/%{maxima_ver}/doc/html/es/
%doc %lang(pt) %{_datadir}/maxima/%{maxima_ver}/doc/html/pt/
%doc %lang(pt_BR) %{_datadir}/maxima/%{maxima_ver}/doc/html/pt_BR/
%{_datadir}/maxima/%{maxima_ver}/share/
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/mime/packages/x-maxima-out.xml
%{bash_completions_dir}/*maxima
%{_datadir}/icons/hicolor/scalable/mimetypes/*
%dir %{_libdir}/maxima/
%dir %{_libdir}/maxima/%{maxima_ver}/
%{_infodir}/imaxima*
%{_infodir}/maxima*
%{_infodir}/abs_integrate.info*
%{_infodir}/drawutils.info*
%{_infodir}/guess.info*
%{_infodir}/kovacicODE.info*
%{_infodir}/logic.info*
%{_infodir}/mathml.info*
%{_infodir}/nelder_mead.info
%{_infodir}/raddenest.info*
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
%{_datadir}/applications/Xmaxima.desktop
%{_metainfodir}/net.sourceforge.maxima.xmaxima.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*
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
%autochangelog
