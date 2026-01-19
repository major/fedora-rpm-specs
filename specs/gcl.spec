# Address randomization breaks gcl's memory management scheme
%undefine _hardened_build

# The package notes feature leads to failed builds for everything that depends
# on GCL.  Turn it off until somebody figures out how to make it work without
# polluting linker flags.
%undefine _package_note_file

# FASL file loads fail with an unexpected EOF error without this.  I do not yet
# know why.
%global __brp_strip_lto %{_bindir}/true

# Use of LTO leads to strange segfaults, reason as yet unknown.
%global _lto_cflags %{nil}

Name:           gcl
Version:        2.7.1
Release:        %autorelease
Summary:        GNU Common Lisp

# LGPL-2.0-or-later:
# - cmpnew
# - gcl-tk/guis.c
# - gcl-tk/tkinfo.lsp
# - gcl-tk/tkl.lsp
# - gmp4 (not used)
# - h
# - lsp (except as noted below)
# - o (except as noted below)
# GPL-1.0-or-later:
# - o/firstfile.c
# - o/lastfile.c
# - o/ntheap.h (not used on Linux)
# - o/unexec*
# - xgcl-2
# MIT-Modern-Variant:
# - gcl-tk/tkAppInit.c
# - gcl-tk/tkMain.c
# - gcl-tk/tkXAppInit.c
# - gcl-tk/tkXshell.c
# LOOP:
# - lsp/gcl_loop.lsp
License:        LGPL-2.0-or-later AND GPL-1.0-or-later AND MIT-Modern-Variant AND LOOP
URL:            https://www.gnu.org/software/gcl/
VCS:            git:https://git.savannah.gnu.org/git/gcl.git
Source0:        https://ftp.gnu.org/gnu/gcl/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gcl/%{name}-%{version}.tar.gz.sig
Source2:        https://ftp.gnu.org/gnu/gnu-keyring.gpg
Source3:        gcl.el

# Upstream builds point releases for Debian, and uploads the patches directly
# to the Debian Patch Tracker, but does not spin new tarballs.  These are the
# upstream patches from https://sources.debian.org/patches/gcl/.
%global patchdir %{version}-18
# Errata from a gcl mailing list post
Patch:          %{name}-2.7.1-errata.patch

### Fedora patches

# This patch was last sent upstream on 29 Dec 2008.  It updates one source file
# from LaTeX 2.09 to LaTeX 2e, thereby eliminating LaTeX warnings about running
# in compatibility mode.
Patch:          %{name}-2.6.11-latex.patch
# This patch was last sent upstream on 29 Dec 2008.  It adapts to texinfo 5.0.
Patch:          %{name}-2.7.1-texinfo.patch
# This patch was last sent upstream on 29 Dec 2008.  It fixes a large number of
# compile- and run-time problems with the Emacs interface code.
Patch:          %{name}-2.7.1-elisp.patch
# This patch was last sent upstream on 13 Oct 2009.  Add a format attribute.
Patch:          %{name}-2.7.1-format.patch
# Fix a clash with the system definition of bsearch.
Patch:          %{name}-2.7.1-bsearch.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  binutils-devel
BuildRequires:  bzip2
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  tex(latex)
BuildRequires:  tex-ec
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  emacs-nw

Requires:       gcc
Requires:       libtirpc-devel%{?_isa}
Requires:       util-linux%{?_isa}
Requires:       which%{?_isa}

%description
GCL is a Common Lisp currently compliant with the ANSI standard.  Lisp
compilation produces native code through the intermediary of the system's C
compiler, from which GCL derives efficient performance and easy portability.
The GUI currently uses TCL/Tk.


%package emacs
License:        GPL-1.0-or-later
Summary:        Emacs mode for interacting with GCL
Requires:       %{name} = %{version}-%{release}
Requires:       emacs(bin) %{?_emacs_version:>= %{_emacs_version}}
BuildArch:      noarch

%description emacs
Emacs mode for interacting with GCL


%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1


%conf
# Ensure the frame pointer doesn't get added back
sed -i 's/"-fomit-frame-pointer"/""/' configure

# Silence warnings about the obsolescence of egrep
sed -i 's/egrep/grep -E/' ltmain.sh

# Fix path to the saved images
sed -i 's,/lib/,/%{_lib}/,' bin/gcl.in

# Get a version of texinfo.tex that works with the installed version of texinfo
cp -p %{_texmf_main}/tex/texinfo/texinfo.tex info

# The archive is so full of spurious executable bits that we just remove them
# all here, then add back the ones that should exist
find . -type f -perm /0111 -exec chmod a-x {} +
chmod a+x ansi-tests/make-tar compile config.guess config.sub configure \
  depcomp gcl-tk/gcltksrv.in install-sh missing xbin/*

# Temporary workaround for problems detecting architecture.  Remove this on the
# next release.
%ifarch %{power64}
sed -i 's,output_mach=`.*`,output_mach=ppc64,' configure
%endif
%ifarch s390x
sed -i 's,output_mach=`.*`,output_mach=s390_64,' configure
%endif

%build
%configure \
  --disable-dependency-tracking \
  --enable-readline \
  --enable-tcltk \
  --enable-tclconfig=%{_libdir} \
  --enable-tkconfig=%{_libdir} \
  --enable-xdr \
  --enable-xgcl
# Parallel builds often lead to resource exhaustion
make

# Build gcl.info, which is needed for DESCRIBE to work properly
rm info/gcl.info
make -C info gcl.info

# dwdoc needs two extra LaTeX runs to resolve references
cd xgcl-2
pdflatex dwdoc.tex
pdflatex dwdoc.tex
cd -


%install
%make_install

# Get rid of the parts that we don't want
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/emacs
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/gcl-*/info

# Install the man page
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -pf man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

# Install and compile the Emacs code
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
cp -pfr elisp/* $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
rm -f $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl/makefile
rm -f $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl/readme
mkdir -p $RPM_BUILD_ROOT%{_emacs_sitestartdir}
sed -e "s|%LISP_DIR%|%{_emacs_sitelispdir}|" %{SOURCE3} > $RPM_BUILD_ROOT%{_emacs_sitestartdir}/gcl.el
pushd $RPM_BUILD_ROOT%{_emacs_sitelispdir}/gcl
%{_emacs_bytecompile} *.el
popd

# Help the debuginfo generator
ln -s ../h/cmpinclude.h cmpnew/cmpinclude.h
ln -s ../h/cmpinclude.h lsp/cmpinclude.h
ln -s ../h/cmpinclude.h xgcl-2/cmpinclude.h

# Fix permissions
chmod 0755 %{buildroot}%{_libdir}/gcl-%{version}/unixport/libboot.so

# The image has garbage strings containing RPM_BUILD_ROOT
export QA_SKIP_BUILD_ROOT=1


%clean
rm -f /tmp/gazonk_* /tmp/gcl_*


%files
%{_bindir}/gcl
%{_libdir}/gcl-%{version}/
%{_infodir}/*
%{_mandir}/man*/*
%doc ChangeLog README
%license COPYING

%files emacs
%doc elisp/readme
%{_emacs_sitelispdir}/gcl/
%{_emacs_sitestartdir}/*


%changelog
%autochangelog
