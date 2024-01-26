# The module loader does not work with PIE
%undefine _hardened_build

%global gaparchdir %{_libdir}/gap
%global gaplibdir %{_datadir}/gap
%global icondir %{_datadir}/icons/hicolor
%global gapbits default%{__isa_bits}

%ifarch ppc64le
%global gapcpu powerpc64le-redhat-linux-gnu
%else
%global gapcpu %{_build}
%endif
%global gaparch %{gapcpu}-%{gapbits}-kv8

# Files installed in nearly every package by GAPDoc
%global GAPDoc_files chooser.html lefttoc.css manual.css manual.js nocolorprompt.css ragged.css rainbow.js times.css toggless.css toggless.js

# When bootstrapping a new architecture, there are no GAPDoc, gap-pkg-primgrp,
# gap-pkg-smallgrp, or gap-pkg-transgrp packages yet, but the gap binary
# refuses to run unless all four are present.  Therefore, build as follows:
# 1. Build this package in bootstrap mode.
# 2. Build GAPDoc in bootstrap mode.
# 3. Build gap-pkg-transgrp.
# 4. Build gap-pkg-autodoc in bootstrap mode.
# 5. Build gap-pkg-io
# 6. Build GAPDoc in non-bootstrap mode.
# 7. Build gap-pkg-autodoc in non-bootstrap mode.
# 8. Build gap-pkg-primgrp and gap-pkg-smallgrp.
# 9. Build this package in non-bootstrap mode.
%bcond_with bootstrap

Name:           gap
Version:        4.12.2
Release:        7%{?dist}
Summary:        Computational discrete algebra

%global majver %(cut -d. -f1-2 <<< %{version})

License:        GPL-2.0-or-later
URL:            https://www.gap-system.org/
Source0:        https://github.com/gap-system/gap/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        gap-README.fedora
Source2:        update-gap-workspace
Source3:        gap.xml
Source4:        org.gap-system.gap.desktop
Source5:        org.gap-system.gap.metainfo.xml
Source6:        gap.1.in
Source7:        gac.1.in
Source8:        update-gap-workspace.1
Source9:        gap.vim
# ATLAS data used during the tests
Source10:       gap-testdata.tar.xz
# This patch applies a change from Debian to allow help files to be in gzip
# compressed DVI files, and also adds support for viewing with xdg-open.
Patch0:         %{name}-help.patch
# Avoid the popcount instruction on systems that do not support it
Patch1:         %{name}-popcount.patch

ExclusiveArch:  %{gap_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  parallel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(english.ldf)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(pslatex.sty)
BuildRequires:  tex(psnfss.map)
BuildRequires:  tex(tex)
BuildRequires:  tex-cm-super
BuildRequires:  tex-ec
BuildRequires:  tex-helvetic
BuildRequires:  tex-latex-bin
BuildRequires:  tex-rsfs
BuildRequires:  tex-symbol
BuildRequires:  tex-times

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-online-help = %{version}-%{release}
Requires:       hicolor-icon-theme

%description
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory.  GAP provides a programming
language, a library of thousands of functions implementing algebraic
algorithms written in the GAP language as well as large data libraries
of algebraic objects.  GAP is used in research and teaching for studying
groups and their representations, rings, vector spaces, algebras,
combinatorial structures, and more.

This package contains the command line application.

%package libs
Summary:        Essential GAP libraries
BuildArch:      noarch

%description libs
This package contains the essential GAP libraries: lib and grp.

%package core
Summary:        GAP core components
Requires:       %{name}-libs = %{version}-%{release}
%if %{without bootstrap}
Requires:       GAPDoc
Requires:       gap-pkg-primgrp
Requires:       gap-pkg-smallgrp
Requires:       gap-pkg-transgrp
%endif

Suggests:       catdoc

%description core
This package contains the core GAP system.

%package online-help
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
# RSFS: LicenseRef-Rsfs
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Online help for GAP
Requires:       %{name}-core = %{version}-%{release}
BuildArch:      noarch

%description online-help
This package contains the documentation in TeX format needed for GAP's
online help system.

%package rpm-macros
Summary:        RPM macros for GAP packages

%description rpm-macros
This package contains RPM macros for GAP packages.

%package devel
Summary:        GAP compiler and development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-rpm-macros%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description devel
This package contains the GAP compiler (gac) and the header files necessary
for developing GAP programs.

%package vim
Summary:        Edit GAP files with VIM
Requires:       %{name}-core = %{version}-%{release}
Requires:       vim-filesystem
BuildArch:      noarch

%description vim
This package provides VIM add-on files to support editing GAP sources.
Both syntax highlighting and indentation are supported.

# We used to have a separate libgap-devel package.  That has been removed
# because:
# - it only contained libgap.so;
# - sagemath, the only consumer of libgap, requires libgap.so in addition to
#   to the contents of the libgap package, so both had to be installed anyway

%package -n libgap
Summary:        Library containing core GAP logic
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
# The code executes gunzip
Requires:       gzip

# The packages that GAP itself considers default
Recommends:     gap-pkg-autpgrp
Recommends:     gap-pkg-alnuth
Recommends:     gap-pkg-crisp
Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-factint
Recommends:     gap-pkg-fga
Recommends:     gap-pkg-irredsol
Recommends:     gap-pkg-laguna
Recommends:     gap-pkg-polenta
Recommends:     gap-pkg-polycyclic
Recommends:     gap-pkg-resclasses
Recommends:     gap-pkg-sophus
Recommends:     gap-pkg-tomlib

%description -n libgap
Library containing core GAP logic

%prep
%autosetup -p0

# Get the README
cp -p %{SOURCE1} README.fedora

# Compile default package path into the executable
sed 's,^GAP_CPPFLAGS =,& -DSYS_DEFAULT_PATHS="\\"%{gaplibdir}:%{gaparchdir}\\"",' \
    -i Makefile.rules

%build
# -Wl,-z,now breaks use of RTLD_LAZY
# Even though the GAP kernel is single-threaded, it must be linked with pthreads
# or packages cannot successfully load and run multithreaded shared objects.
export LDFLAGS="-lpthread -Wl,-z,relro -Wl,--as-needed"
export STRIP=%{_bindir}/true
export LC_ALL=C.UTF-8
%configure

# Get rid of undesirable hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build V=1

# Rebuild the manuals from source
export GAP_DIR=$PWD
make manuals

# Build gapmacrodoc.pdf
cd doc
pdftex gapmacrodoc.tex
pdftex gapmacrodoc.tex
cd -

# Remove build paths
#sed -i "s|$PWD|%%{gapdir}|g" sysinfo.gap bin/gap.sh gac doc/make_doc

# Don't link every package shared object with libpthread
sed -i "s/[[:blank:]]*-lpthread[[:blank:]]*//" sysinfo.gap

# Fix mangled paths in gap.sh
sed -i "s|^\(GAP_EXE=\).*|\1%{_bindir}|;/  GAP_EXE=/d" bin/gap.sh

# Create an RPM macro file for GAP packages
cat > macros.%{name} << EOF
%%gap_version %{version}
%%gap_archdir %{gaparchdir}
%%gap_libdir %{gaplibdir}
%%gap_arch %{gaparch}

# Files installed by GAPDoc
%%gapdoc_files %{GAPDoc_files}

# Install documentation files of interest.  In particular, we do not install
# intermediate files produced by (La)TeX as it runs.  GAPDoc style files are
# linked instead of copied.
# -d DIR: Copy files to directory DIR under the package directory (instead of
#         "doc", which is the default)
# -n NAME: name of the package, defaults to %%%%{pkgname}
%%gap_copy_docs(d:n:) \\
  subdir=%%{-d:%%{-d*}}%%{!-d:doc} \\
  if [ "%%_target_cpu" = "noarch" ]; then \\
    path=%%{buildroot}%%{gap_libdir}/pkg/%%{-n:%%{-n*}}%%{!-n:%%{pkgname}}/\$subdir \\
  else \\
    path=%%{buildroot}%%{gap_archdir}/pkg/%%{-n:%%{-n*}}%%{!-n:%%{pkgname}}/\$subdir \\
  fi \\
  for ext in bib css gif html jpeg jpg js lab pdf png six txt; do \\
    cp -p \$subdir/*.\$ext \$path 2>/dev/null || : \\
  done \\
  for fil in %%{gapdoc_files}; do \\
    if [ -e "\$path/\$fil" ]; then \\
      rm \$path/\$fil \\
      if [ "%%_target_cpu" = "noarch" ]; then \\
        ln -s ../..\$(sed 's|/|/..|' <<< "\${subdir//[^\\\\/]}")/GAPDoc/styles/\$fil \$path/\$fil \\
      else \\
        ln -s %%{gap_libdir}/pkg/GAPDoc/styles/\$fil \$path/\$fil \\
      fi \\
    fi \\
  done
EOF

%install
%make_install

# Link, rather than copy, identical binaries
rm %{buildroot}%{gaparchdir}/gap
ln %{buildroot}%{_bindir}/gap %{buildroot}%{gaparchdir}/gap

# Remove files we do not want or install elsewhere
rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{gaplibdir}/{*.md,COPYRIGHT,LICENSE}
rm -fr %{buildroot}%{gaplibdir}/etc/vim

# Install the workspace helper
install -p -m755 %{SOURCE2} %{buildroot}%{_bindir}

# Install documentation builders
cp -p doc/{gapmacro.tex,manualindex,versiondata,*.{bib,lab,pdf,six,xml}} \
      %{buildroot}%{gaplibdir}/doc

# Make an empty directory for archful packages
mkdir -p %{buildroot}%{gaparchdir}/pkg

# Unbundle GAPDoc files from the manuals
for book in hpc ref tut; do
    rm %{buildroot}%{gaplibdir}/doc/$book/{*.css,*.js,chooser.html}
    for fil in %{GAPDoc_files}; do
        ln -s ../../pkg/GAPDoc/styles/$fil %{buildroot}%{gaplibdir}/doc/$book
    done
done

# Install VIM support where the rest of the system expects to find it
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/indent
cp -p etc/vim/gap_indent.vim %{buildroot}%{_datadir}/vim/vimfiles/indent
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/syntax
cp -p etc/vim/gap.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax
mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
cp -p %{SOURCE9} %{buildroot}%{_datadir}/vim/vimfiles/ftdetect

# Create the system workspace, initially empty
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
touch %{buildroot}%{_localstatedir}/lib/%{name}/workspace.gz

# Install the icon; the original is 1024x1024
bmptopnm cnf/cygwin/gapicon.bmp > gapicon.pnm
for size in 16 22 24 32 36 48 64 72 96 128 192 256 512; do
  mkdir -p %{buildroot}%{icondir}/${size}x${size}/apps
  pamscale -xsize=$size -ysize=$size gapicon.pnm | pnmtopng -compression=9 \
    > %{buildroot}%{icondir}/${size}x${size}/apps/%{name}.png
done

# Install the MIME type
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p %{SOURCE3} %{buildroot}%{_datadir}/mime/packages

# Install the desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --mode=644 --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE4}

# Install the AppData file
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE5} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gap-system.gap.metainfo.xml

# Install the RPM macro file
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cp -p macros.%{name} %{buildroot}%{_rpmconfigdir}/macros.d

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
sed "s|@VERSION@|%{version}|" %{SOURCE6} > %{buildroot}%{_mandir}/man1/gap.1
sed "s|@VERSION@|%{version}|" %{SOURCE7} > %{buildroot}%{_mandir}/man1/gac.1
cp -p %{SOURCE8} %{buildroot}%{_mandir}/man1

%preun
if [ $1 -eq 0 ]; then
  %{_bindir}/update-gap-workspace delete &> /dev/null || :
fi

%transfiletriggerin -- %{gaplibdir}/pkg %{gaparchdir}/pkg
%{_bindir}/update-gap-workspace > /dev/null || :

%transfiletriggerpostun -- %{gaplibdir}/pkg %{gaparchdir}/pkg
%{_bindir}/update-gap-workspace > /dev/null || :

%if %{without bootstrap}
%check
export LC_ALL=C.UTF-8
sed -e "s|GAP_DIR=.*|GAP_DIR=$PWD|" \
    -e "s|GAP_EXE=.*|GAP_EXE=$PWD|" \
    -i bin/gap.sh
sed -i "s|80 -r|& -l $PWD|" Makefile.rules

# Unpack the test data
tar -C pkg -xf %{SOURCE10}

make check
%endif

%files
%doc README.md README.fedora
%{_bindir}/gap
%{gaparchdir}/gap
%{_mandir}/man1/gap.1*
%{_metainfodir}/org.gap-system.gap.metainfo.xml
%{_datadir}/applications/org.gap-system.gap.desktop
%{_datadir}/mime/packages/gap.xml
%{icondir}/16x16/apps/gap.png
%{icondir}/22x22/apps/gap.png
%{icondir}/24x24/apps/gap.png
%{icondir}/32x32/apps/gap.png
%{icondir}/36x36/apps/gap.png
%{icondir}/48x48/apps/gap.png
%{icondir}/64x64/apps/gap.png
%{icondir}/72x72/apps/gap.png
%{icondir}/96x96/apps/gap.png
%{icondir}/128x128/apps/gap.png
%{icondir}/192x192/apps/gap.png
%{icondir}/256x256/apps/gap.png
%{icondir}/512x512/apps/gap.png

%files libs
%license COPYRIGHT LICENSE
%dir %{gaplibdir}
%{gaplibdir}/CITATION
%{gaplibdir}/grp/
%{gaplibdir}/hpcgap/
%{gaplibdir}/lib/

%files core
%{_bindir}/update-gap-workspace
%dir %{gaparchdir}
%{gaparchdir}/sysinfo.gap
%{gaparchdir}/pkg/
%{gaplibdir}/pkg/
%{_mandir}/man1/update-gap-workspace.1*
%dir %{_localstatedir}/lib/%{name}/
%verify(user group mode) %{_localstatedir}/lib/%{name}/workspace.gz

%files online-help
%{gaplibdir}/doc/

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.%{name}

%files devel
%{_bindir}/gac
%{gaplibdir}/etc/
%{_includedir}/gap/
%{_mandir}/man1/gac.1*

%files vim
%doc etc/vim/debug.vim etc/vim/debugvim.txt etc/vim/README.vim-utils
%{_datadir}/vim/vimfiles/ftdetect/gap.vim
%{_datadir}/vim/vimfiles/indent/gap_indent.vim
%{_datadir}/vim/vimfiles/syntax/gap.vim

%files -n libgap
%{_libdir}/libgap.so.8
%{_libdir}/libgap.so.8.*
%{_libdir}/libgap.so

%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 10 2023 Jerry James <loganjerry@gmail.com> - 4.12.2-5
- Use a more reliable way of detecting CPU features

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jerry James <loganjerry@gmail.com> - 4.12.2-3
- Validate metainfo with appstream-util

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 4.12.2-2
- Conform more closely to upstream's preferred file layout
- Remove %%gap_arches from the RPM macro file

* Sun Dec 18 2022 Jerry James <loganjerry@gmail.com> - 4.12.2-1
- Version 4.12.2
- Drop upstreamed unused patch

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 4.12.1-1
- Version 4.12.1
- Drop builtin-mul-overflow patch
- Drop post-4.12.0 bug fix patches
- Switch to upstream's method of bootstrapping

* Mon Oct 17 2022 Jerry James <loganjerry@gmail.com> - 4.12.0-2
- Add rpm-macros subpackage
- Clarify license of the online-help subpackage
- Don't ship config.h or make_doc at upstream's request

* Mon Sep 26 2022 Jerry James <loganjerry@gmail.com> - 4.12.0-1
- Version 4.12.0
- Remove ix86 support
- Drop obsolete -gac, -bagheader, and -ref patches
- Add -popcount patch to avoid illegal CPU instruction errors
- Add -unused patch to trim unused functions
- Add upstream post-release bug fix patches
- Add ATLAS data needed for the tests
- Rearrange %%install to ease future transition to "make install"

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 4.11.1-5
- Convert License tag to SPDX

* Thu Jul 21 2022 Jerry James <loganjerry@gmail.com> - 4.11.1-5
- Change s390x binary name to match updated config

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Jerry James <loganjerry@gmail.com> - 4.11.1-3
- Add -bagheader patch to work around package build failures on i386

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 17 2021 Jerry James <loganjerry@gmail.com> - 4.11.1-1
- Version 4.11.1
- Drop upstreamed -aarch64 patch
- Install into the metainfo dir instead of the appdata dir
- Do not force every package shared object to be linked with libpthread
- Fix typo in the preun script
- Drop workaround for s390x tests, fixed upstream

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Jerry James <loganjerry@gmail.com> - 4.11.0-6
- Force the binary to be linked with pthreads

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jerry James <loganjerry@gmail.com> - 4.11.0-4
- Incorporate upstream changes and cleanups
- Drop the libgap-devel subpackage; it is not useful

* Thu Apr  2 2020 Jerry James <loganjerry@gmail.com> - 4.11.0-3
- Reenable inlining on aarch64 on all but 1 function

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 4.11.0-2
- Turn off all inlining on aarch64 to work around possible GCC bug

* Fri Mar 13 2020 Jerry James <loganjerry@gmail.com> - 4.11.0-1
- Version 4.11.0
- Drop upstreamed -immutable patch
- Drop libtool Requires from the -devel subpackage
- Add -aarch64 patch to fix FTBFS on aarch64

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Jerry James <loganjerry@gmail.com> - 4.10.2-1
- Drop -stat patch, no longer needed after gap-pkg-io update
- Drop -doc patch: it is not the right solution to the problem

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 4.10.2-1
- New upstream release
- Make the main package own the GAP bin directory

* Wed Mar 20 2019 Jerry James <loganjerry@gmail.com> - 4.10.1-1
- New upstream release
- Drop upstreamed sagemath patches

* Sun Feb 17 2019 Jerry James <loganjerry@gmail.com> - 4.10.0-2
- Build in non-bootstrap mode

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.10.0-1
- Rebuild for readline 8.0

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 4.10.0-0
- New upstream release
- Drop upstreamed -paths patch
- Add -bootstrap patch to break circular build dependencies
- Add -escape, -ref, -doc, -gac, and -immutable patches
- Add -terminal, -erroroutput, and -enterleave patches from sagemath
- Add libgap and libgap-devel subpackages
- Move the commandline application into the main package
- Change BRs and Rs due to recent TeXLive packaging changes
- Create all of the icon sizes supported by hicolor-icon-theme
- Fix update-gap-workspace on initial build with empty workspace
- Disable hardened build, which breaks RTLD_LAZY in the module loader
- Build in bootstrap mode

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar  3 2018 Jerry James <loganjerry@gmail.com> - 4.8.8-3
- Move the icons to the apps directory

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Jerry James <loganjerry@gmail.com> - 4.8.8-1
- Remove obsolete scriptlets

* Wed Sep  6 2017 Jerry James <loganjerry@gmail.com> - 4.8.8-1
- New upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Jerry James <loganjerry@gmail.com> - 4.8.7-2
- Bring back the -stat patch, still needed by gap-pkg-io

* Fri Mar 31 2017 Jerry James <loganjerry@gmail.com> - 4.8.7-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.8.6-2
- Rebuild for readline 7.x

* Mon Nov 14 2016 Jerry James <loganjerry@gmail.com> - 4.8.6-1
- New upstream release
- Adjust BRs for the latest texlive release

* Wed Sep 28 2016 Jerry James <loganjerry@gmail.com> - 4.8.5-1
- New upstream release

* Wed Jun 15 2016 Jerry James <loganjerry@gmail.com> - 4.8.4-1
- New upstream release

* Thu May  5 2016 Jerry James <loganjerry@gmail.com> - 4.8.3-2
- Fix PowerPC64 build failure (bz 1330108)

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 4.8.3-1
- New upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  2 2015 Jerry James <loganjerry@gmail.com> - 4.7.9-1
- New upstream release

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 4.7.8-3
- Use file triggers
- Rebuild documentation from source
- Compress files in parallel
- Unpack the tools archive

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jerry James <loganjerry@gmail.com> - 4.7.8-1
- New upstream release

* Wed May 20 2015 Jerry James <loganjerry@gmail.com> - 4.7.7-2
- Fix gac compiler flags for dynamic objects
- Update appdata

* Mon Feb 16 2015 Jerry James <loganjerry@gmail.com> - 4.7.7-1
- New upstream release

* Fri Jan 23 2015 Jerry James <loganjerry@gmail.com> - 4.7.6-3
- Fix scriptlets so they don't complain when uninstalling
- Drop obsolete Group tags

* Thu Jan 15 2015 Jerry James <loganjerry@gmail.com> - 4.7.6-2
- Fix crash with nameless TTYs, such as in mock shell environments

* Wed Dec 10 2014 Jerry James <loganjerry@gmail.com> - 4.7.6-1
- New upstream release
- Fix license handling
- Install more icon sizes

* Sat Aug 16 2014 Rex Dieter <rdieter@fedoraproject.org> 4.7.5-3
- update scriplets

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Jerry James <loganjerry@gmail.com> - 4.7.5-1
- New upstream release
- Fix ownership of workspace.gz

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Jerry James <loganjerry@gmail.com> - 4.7.4-1
- New upstream release

* Wed Feb  5 2014 Jerry James <loganjerry@gmail.com> - 4.7.2-2
- Update location of rpm macro file for rpm >= 4.11
- Add an AppData file

* Tue Jan 14 2014 Jerry James <loganjerry@gmail.com> - 4.7.2-1
- New upstream release
- Upstream no longer distributes an (X)Emacs interface

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 4.6.5-1
- New upstream release

* Wed May 22 2013 Jerry James <loganjerry@gmail.com> - 4.6.4-2
- Update -stat patch to provide large integer conversion (for, e.g., loff_t)
- Drop meataxe Requirement as it has been replaced with internal routines

* Thu May 16 2013 Jerry James <loganjerry@gmail.com> - 4.6.4-1
- New upstream release

* Thu Mar 28 2013 Jerry James <loganjerry@gmail.com> - 4.6.3-1
- New upstream release

* Sat Mar 09 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 4.6.2-2
- Remove %%config from %%{_sysconfdir}/rpm/macros.*
  (https://fedorahosted.org/fpc/ticket/259).

* Wed Feb 20 2013 Jerry James <loganjerry@gmail.com> - 4.6.2-1
- New upstream release
- Move update-gap-workspace call to posttrans (bz 912067)
- Add -stat patch and -D_FILE_OFFSET_BITS=64 to CPPFLAGS to use 64-bit
  stat interface on 32-bit systems

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Rex Dieter <rdieter@fedoraproject.org> 4.5.7-2
- optimize/update icon scriptlets

* Mon Dec 17 2012 Jerry James <loganjerry@gmail.com> - 4.5.7-1
- New upstream release

* Mon Oct 22 2012 Jerry James <loganjerry@gmail.com> - 4.5.6-3
- Further fixes for the -m32/-m64 issue
- Many packages need the primitive, small, or transitive groups; collapse them
  all into the -libs subpackage so they are always available
- Provide sysinfo-default[32|64], as required by some packages
- Provide symbolic links to gac and gap from the bin directory, as required by
  some packages

* Sat Oct 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 4.5.6-2
- -m32/-m64 should come from RPM_OPT_FLAGS. Fix build issues on non x86 arches

* Mon Sep 24 2012 Jerry James <loganjerry@gmail.com> - 4.5.6-1
- New upstream release
- Remove unused patches from git

* Thu Sep 13 2012 Jerry James <loganjerry@gmail.com> - 4.5.5-1
- New upstream release
- Drop upstreamed patches
- Sources are now UTF-8; no conversion necessary

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Jerry James <loganjerry@gmail.com> - 4.4.12-4
- Add an RPM macro file for GAP packages
- Fix the location of config.h

* Wed Jan 11 2012 Jerry James <loganjerry@gmail.com> - 4.4.12-3
- Fix problems found on review

* Tue Jan  3 2012 Jerry James <loganjerry@gmail.com> - 4.4.12-2
- Mimic Debian's subpackage structure

* Wed Oct 12 2011 Jerry James <loganjerry@gmail.com> - 4.4.12-1
- Initial RPM
