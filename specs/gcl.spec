# Address randomization breaks gcl's memory management scheme
%undefine _hardened_build

# The package notes feature leads to failed builds for everything that depends
# on GCL.  Turn it off until somebody figures out how to make it work without
# polluting linker flags.
%undefine _package_note_file

# GCL wants to read uncompressed info files.  Turn off automatic compression.
%global __brp_compress %{_bindir}/true

# FASL file loads fail with an unexpected EOF error without this.  I do not yet
# know why.
%global __brp_strip_lto %{_bindir}/true

# Use of LTO leads to strange segfaults, reason as yet unknown.
%global _lto_cflags %{nil}

Name:           gcl
Version:        2.6.14
Release:        10%{?dist}
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
%global patchdir %{version}-11
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre1
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre2
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre3
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre4
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre5
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre6
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre7
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre8
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre9
Patch:          https://sources.debian.org/data/main/g/gcl/%{patchdir}/debian/patches/Version_2_6_15pre10

### Fedora patches

# This patch was last sent upstream on 29 Dec 2008.  It updates one source file
# from LaTeX 2.09 to LaTeX 2e, thereby eliminating LaTeX warnings about running
# in compatibility mode.
Patch:          %{name}-2.6.11-latex.patch
# This patch was last sent upstream on 29 Dec 2008.  It adapts to texinfo 5.0.
Patch:          %{name}-2.6.11-texinfo.patch
# This patch was last sent upstream on 29 Dec 2008.  It fixes a large number of
# compile- and run-time problems with the Emacs interface code.
Patch:          %{name}-2.6.11-elisp.patch
# This is a Fedora-specific patch.  Do not delete C files produced from D files
# so they can be pulled into the debuginfo package.
Patch:          %{name}-2.6.11-debuginfo.patch
# This patch was last sent upstream on 13 Oct 2009.  It fixes two bugs in the
# reading of PLT information.
Patch:          %{name}-2.6.11-plt.patch
# This patch was last sent upstream on 13 Oct 2009.  It fixes several malformed
# function prototypes involving an ellipsis.
Patch:          %{name}-2.6.11-ellipsis.patch
# Turn address randomization off early.  GCL is linked with libtirpc, which is
# linked with libselinux, which has a static initializer that calls malloc()
# and free() on systems that do not have /sys/fs/selinux or /selinux mounted,
# or have them mounted read-only.
Patch:          %{name}-2.6.12-libselinux.patch
# This patch was last sent upstream on 29 Dec 2008.  It updates the autoconf
# and libtool files to newer versions.  By itself, this patch accomplishes
# little of interest.  However, some of the later patches change configure.in.
# Without this patch, autoconf appears to run successfully, but generates a
# configure script that contains invalid shell script syntax.
Patch:          %{name}-2.6.12-infrastructure.patch
# This patch was last sent upstream on 29 Dec 2008.  It rationalizes the
# handling of system extensions.  For example, on glibc-based systems, some
# functionality is available only when _GNU_SOURCE is defined.
Patch:          %{name}-2.6.12-extension.patch
# Force building in C17 mode; the code is not ready for C23
Patch:          %{name}-2.6.14-c17.patch

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
compilation produces native code through the intermediary of the
system's C compiler, from which GCL derives efficient performance and
easy portability.  The GUI currently uses TCL/Tk.


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
# The binary MUST be run with address randomization off.  The main() function
# has code to accomplish that, but it does not run early enough.  Ensure that
# randomization is off before GCL even starts.
sed -i 's,echo exec,& %{_bindir}/setarch -R,' makefile

# Ensure the frame pointer doesn't get added back
sed -i 's/"-fomit-frame-pointer"/""/' configure

# Fix a path in the launch script
sed -i 's|/usr/lib/tk|%{_datadir}/tk|' debian/gcl.sh

# Silence warnings about the obsolescence of egrep and fgrep
sed -i 's/egrep/grep -E/' o/egrep-def
sed -i 's/fgrep/grep -F/' configure.in configure mp/makefile o/unexec.c \
    o/unexec-19.29.c xbin/notify

# Get a version of texinfo.tex that works with the installed version of texinfo
cp -p %{_texmf_main}/tex/texinfo/texinfo.tex info

# The archive is so full of spurious executable bits that we just remove them
# all here, then add back the ones that should exist
find . -type f -perm /0111 -exec chmod a-x {} +
chmod a+x add-defs add-defs1 config.guess config.sub configure install.sh
chmod a+x bin/info bin/info1 gcl-tk/gcltksrv.in gcl-tk/ngcltksrv mp/gcclab
chmod a+x o/egrep-def utils/replace xbin/*

%build
# The code is not ready for C23
export CFLAGS='%{build_cflags} -std=gnu17'
%configure --enable-readline --enable-ansi --enable-dynsysgmp --enable-xgcl \
  --enable-tclconfig=%{_libdir} --enable-tkconfig=%{_libdir}
# FIXME: %%{?_smp_mflags} breaks the build
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

# Install the HTML documentation
mkdir -p html
cp -pfr info/gcl-si info/gcl-tk html

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

# The image has garbage strings containing RPM_BUILD_ROOT
export QA_SKIP_BUILD_ROOT=1

# Since we disabled brp-compress, manually compress the man page
gzip -9v $RPM_BUILD_ROOT%{_mandir}/man1/gcl.1


%clean
rm -f /tmp/gazonk_* /tmp/gcl_*


%files
%{_bindir}/gcl
%{_prefix}/lib/gcl*
%{_infodir}/*
%{_mandir}/man*/*
%doc readme readme.xgcl RELEASE* ChangeLog* faq doc
%doc gcl*.jpg gcl.ico gcl.png
%doc html/gcl-si html/gcl-tk
%license COPYING*

%files emacs
%doc elisp/readme
%{_emacs_sitelispdir}/gcl/
%{_emacs_sitestartdir}/*


%changelog
* Tue Jan 21 2025 Jerry James <loganjerry@gmail.com> - 2.6.14-10
- Build in C17 mode

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Jerry James <loganjerry@gmail.com> - 2.6.14-9
- Update to 2.6.15pre10 with fixes for riscv64

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 29 2024 Jerry James <loganjerry@gmail.com> - 2.6.14-7
- Update to 2.6.15pre8
- Build for s390x again
- Require libtirpc-devel at runtime

* Tue Feb 27 2024 Jerry James <loganjerry@gmail.com> - 2.6.14-6
- Update to 2.6.15pre5

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar  6 2023 Jerry James <loganjerry@gmail.com> - 2.6.14-2
- Update to 2.6.15pre3
- Drop upstreamed -unrandomize patch

* Sat Jan 21 2023 Jerry James <loganjerry@gmail.com> - 2.6.14-1
- Update to 2.6.14
- Verify the tarball
- Drop upstreamed modern C patch
- The -fwrapv compiler flag is no longer needed
- Add -unrandomize patch to fix compilation with glibc 2.36.9000
- Do not build for s390x until a compiler issue can be resolved

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Jerry James <loganjerry@gmail.com> - 2.6.13-1
- Update to 2.6.13 final
- Drop upstreamed -fd-leak patch
- Drop obsolete -arm patch

* Wed Nov 23 2022 Jerry James <loganjerry@gmail.com> - 2.6.13-0.129
- Update to 2.6.13pre129
- Add patch for https://fedoraproject.org/wiki/Changes/PortingToModernC
- Silence warnings about the obsolescence of egrep and fgrep

* Wed Nov  9 2022 Jerry James <loganjerry@gmail.com> - 2.6.13-0.126
- Update to 2.6.13pre126
- Convert License tag to SPDX

* Mon Aug  8 2022 Jerry James <loganjerry@gmail.com> - 2.6.13-0.119
- Update to 2.6.13pre119

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.117.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb  4 2022 Jerry James <loganjerry@gmail.com> - 2.6.13-0.117
- Update to 2.6.13pre117

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.112.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Jerry James <loganjerry@gmail.com> - 2.6.13-0.112
- Update to 2.6.13pre112

* Tue Nov  9 2021 Jerry James <loganjerry@gmail.com> - 2.6.13-0.102
- Update to 2.6.13pre102
- Drop upstreamed patches: -unrandomize, -asm-signal-h, -massert
- Drop XEmacs support

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.99.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb  2 2021 Jerry James <loganjerry@gmail.com> - 2.6.13-0.99
- Update to 2.6.13pre99

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.95.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Jerry James <loganjerry@gmail.com> - 2.6.13-0.95
- Add -massert patch to fix FTBFS with recent glibc

* Wed Jan  6 2021 Jerry James <loganjerry@gmail.com> - 2.6.13-0.95
- Update to 2.6.13pre95

* Tue Nov  3 2020 Jerry James <loganjerry@gmail.com> - 2.6.13-0.93
- Update to 2.6.13pre93

* Mon Aug 24 2020 Jerry James <loganjerry@gmail.com> - 2.6.13-0.92
- Update to 2.6.13pre92

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.90.1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.90.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul  7 2020 Jerry James <loganjerry@gmail.com> - 2.6.13-0.90.1
- Do not compress the info files, breaks DESCRIBE
- Do not strip the FASL files; GCL cannot load them afterwards
- Modify the launcher script instead of using the gcl/gcl-binary split

* Mon Feb 24 2020 Jerry James <loganjerry@gmail.com> - 2.6.13-0.90
- Update to 2.6.13pre90
- Drop -tail-recursion-check patch, obsoleted by this update
- Drop -fcommon from build flags, fixed upstream

* Fri Jan 31 2020 Jerry James <loganjerry@gmail.com> - 2.6.13-0.89
- Update to 2.6.13pre89
- Add -tail-recursion-check patch to work around a segfaulting test
- Add -fcommon to build flags to work around FTBFS with GCC 10
- Drop -mno-pltseq on ppc64le, fixed upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.84.3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  2 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.84.3
- Update the path to texinfo.tex

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.13-0.84.2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.84.2
- Make gcl a wrapper script for gcl-binary to fix address randomization issues

* Sat Jun 29 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.84.1
- Update to 2.6.13pre84 (bz 1674924)
- Drop the -selinux patch and subpackage, no longer needed
- Build with -fwrapv
- Add the -libselinux patch to fix FTBFS if selinuxfs is mounted read-only
- Build with -mno-pltseq on ppc64le to handle relocation issues

* Sat Mar 23 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.79.2
- Merge -(x)emacs-el subpackages into -(x)emacs

* Sun Feb 17 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.79.2
- Drop the -largefile patch, causing crashes

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.13-0.79.1.1
- Rebuild for readline 8.0

* Fri Feb 15 2019 Jerry James <loganjerry@gmail.com> - 2.6.13-0.79.1
- Update to 2.6.13pre79, fixes FTBFS (bz 1674924)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 2.6.12-11
- The SELinux package is noarch, so drop isa from dependencies

* Wed Feb 21 2018 Jerry James <loganjerry@gmail.com> - 2.6.12-10
- Comply with the draft SELinux packaging policy
- A new method of modifying the CFLAGS is needed
- Add ppc64le patch to fix a link problem

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.6.12-6
- Rebuild for readline 7.x

* Sat Mar  5 2016 Jerry James <loganjerry@gmail.com> - 2.6.12-5
- Add -sincos patch to fix maxima build failure

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 23 2015 Jerry James <loganjerry@gmail.com> - 2.6.12-3
- Fix gcl-selinux post script (bz 1246002)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Jerry James <loganjerry@gmail.com> - 2.6.12-1
- New upstream release
- Drop upstreamed reloc patches

* Fri Oct 10 2014 Jerry James <loganjerry@gmail.com> - 2.6.11-3
- Add -aarch64 patch to fix build on aarch64
- Update -ppc64 patch to match upstream's version

* Tue Sep 23 2014 Jerry James <loganjerry@gmail.com> - 2.6.11-2
- Add -ppc64 patch to fix build on ppc64/ppc64le (bz 1145521)

* Mon Sep  8 2014 Jerry James <loganjerry@gmail.com> - 2.6.11-1
- New upstream release (bz 1138998)
- Drop upstreamed patches
- Drop -fstack-protector workaround; fixed upstream
- GCL now builds on ppc64 (bz 480519)
- GCL now builds on aarch64 (bz 1099534)
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.6.10-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Tue May 20 2014 Jerry James <loganjerry@gmail.com> - 2.6.10-4
- ExcludeArch aarch64 (bz 1099534)

* Mon May 19 2014 Jerry James <loganjerry@gmail.com> - 2.6.10-3
- Add temporary fix for FTBFS with gmp 6

* Wed Feb  5 2014 Jerry James <loganjerry@gmail.com> - 2.6.10-2
- Add -tcl8 patch to prepare for TCL 8.6

* Fri Nov 15 2013 Jerry James <loganjerry@gmail.com> - 2.6.10-1
- New upstream release
- Drop upstreamed patches
- Help the debuginfo generator find more sources

* Wed Nov 13 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-3
- Rebuild to fix SELinux policy breakage

* Tue Oct  8 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-2
- Add -print-double patch from upstream to fix maxima 5.31.2 or later build.

* Mon Aug 26 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-1
- Final 2.6.8 release
- Build with -fno-omit-frame-pointer on all arches; SGC needs it
- Fix bug in selinux post script
- Add -tcl patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.18.20130521cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.17.20130521cvs
- Update to 20130521 snapshot for bug fixes
- Rebase patches

* Mon May 13 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.16.20130511cvs
- Update to 20130511 snapshot for bug fixes
- Add -largefile patch

* Fri Mar 22 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.15.20130126cvs
- Really fix FTBFS on i386 with -fno-omit-frame-pointer
- Update the -texinfo patch for texinfo 5.x
- Update texinfo.tex so we have a version that works with texinfo 5.x

* Thu Feb 14 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.15.20130126cvs
- Update to 20130126 snapshot to fix FTBFS
- Drop upstreamed -s390-reloc patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.15.20130121cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 23 2013 Dan Horák <dan[at]danny.cz> - 2.6.8-0.14.20130121cvs
- fix build on s390
- successful build requires kernel newer than what's in RHEL-6

* Mon Jan 21 2013 Jerry James <loganjerry@gmail.com> - 2.6.8-0.13.20130121cvs
- Update to 20130121 snapshot, fixes bz 838068
- Rebuild for bz 886934
- Add tex-ec BR for TeXLive 2012
- Fix texinfo sources
- Workaround error from passing --parent to %%doc

* Tue Oct 30 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.12.20121008cvs
- Update to 20121008 snapshot
- Add patch to identify unknown relocs instead of just exiting

* Thu Jul 26 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.11.20120705cvs
- Update to 20120705 snapshot
- Change SELinux BR to match recent changes in Rawhide

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.11.20120323cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.10.20120323cvs
- Update to 20120323 snapshot

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 2.6.8-0.10.20120109cvs
- Update to 20120109 snapshot

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.8-0.9.20110516cvs.2
- rebuild with new gmp without compat lib

* Tue Oct 11 2011 Peter Schiffer <pschiffe@redhat.com> - 2.6.8-0.9.20110516cvs.1
- rebuild with new gmp

* Thu Jun 16 2011 Jerry James <loganjerry@gmail.com> - 2.6.8-0.9.20110516cvs
- Rebuild due to bz 712251
- Use explicitly versioned Requires on gcl-selinux
- Drop defattr

* Wed Jun  1 2011 Jerry James <loganjerry@gmail.com> - 2.6.8-0.8.20110516cvs
- Update to 20110516 CVS snapshot for more bug fixes
- Fix SELinux policy for maxima (bz 650279)
- Drop upstreamed volatile patch

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.8.20101115cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Jerry James <loganjerry@gmail.com> - 2.6.8-0.7.20101115cvs
- Update to 20101115 CVS snapshot for more bug fixes
- Drop upstreamed loginname patch
- Add man page patch
- Add license file to -selinux package
- Don't force dynamic BFD so we can use custreloc instead

* Tue Mar 23 2010 Jerry James <loganjerry@gmail.com> - 2.6.8-0.7.20100201cvs
- Update to 20100201 CVS snapshot for multiple bug fixes including, I hope,
  bz 573534
- Drop upstreamed sigprocmask-linux patch
- Work around binutils-devel/binutils-static brokenness in F-13+.

* Mon Nov 30 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.7.20090701cvs
- Fix scripts to reflect actual installation order (bz 541050)
- Update PLT patch for GNU ld >= 2.19 (bz 542004)
- Use (X)Emacs macros to simplify the spec file

* Tue Oct 20 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.6.20090701cvs
- Update SELinux policy for confined users (bz 529757)

* Tue Oct  6 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.5.20090701cvs
- Update SELinux files to give compiled maxima files the right context
- Drop SELinux compatibility kludge for early F-11 selinux-policy packages

* Tue Aug 11 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.4.20090701cvs
- Update to 20090701 CVS snapshot, fixes bz 511483
- Break fix for <asm/signal.h> out into a separate patch and do it right
- Add -plt patch to fix reading of PLT info
- Add -ellipsis patch to eliminate nondeterministic behavior
- Use xz payloads instead of bz2
- Minor spec file cleanups

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.4.20090303cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.3.20090303cvs
- Update to 20090303 CVS snapshot
- Drop upstreamed BFD patch
- Make separate -selinux subpackage

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-0.3.20080902cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 21 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.2.20080902cvs
- Add -fno-strict-aliasing to fix build problems in Rawhide.
- Fix the broken version number scheme I used on the last two releases.

* Mon Jan 26 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.1.20080902cvs.2
- Add missing files required to build gcl.info, which is needed for the
  DESCRIBE function to work properly.
- Specify the info entries explicitly, else a mangled version is written.

* Sat Jan 17 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.1.20080902cvs.1
- ExcludeArch ppc64 for now until I can figure out why it doesn't build

* Fri Jan  9 2009 Jerry James <loganjerry@gmail.com> - 2.6.8-0.1.20080902cvs
- Update from CVS to fix many build problems
- Fix SELinux and BFD problems that blocked the build
- Add patches to address various build and runtime problems
- Drop old patches that are obsoleted by the update from CVS
- Split out emacs and xemacs subpackages

* Mon Jul 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6.7-19
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6.7-18
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-17
- exclude arch x86_64 for now

* Thu Jan 03 2008 Alex Lancaster <alexlan at fedoraproject.org> - 2.6.7-16
- Rebuild for new Tcl (8.5)

* Tue Aug 14 2007 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-15
- Fix post-install script path on x64_64

* Wed Dec 27 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-14
- added req ncurses-devel

* Thu Dec 21 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-13
- Fix for compiling with readline library

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-12
- Rebuild for FE6

* Sat May  6 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-11
- fixed summary text (CLtL1 -> ANSI)
- configure: readine -> readline

* Fri Apr 14 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-10
- added changes to SELinux policy

* Wed Mar  8 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-7
- Patch gcl-bash.patch for configure

* Sat Feb 18 2006 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-6
- Rebuild for Fedora Extras 5

* Fri Sep  9 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.6.7-1
- New Version 2.6.7

* Sun Apr 17 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.6.6-2
- Added buildreq tetex and texinfo

* Wed Apr  6 2005 Gerard Milmeister <gemi@bluewin.ch> - 2.6.6-1
- New Version 2.6.6

* Fri Feb 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:2.6.5-1
- First Fedora release
