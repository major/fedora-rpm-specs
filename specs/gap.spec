%global gaparchdir %{_libdir}/gap
%global gaplibdir %{_datadir}/gap
%global icondir %{_datadir}/icons/hicolor
%global giturl  https://github.com/gap-system/gap

# Files installed in nearly every package by GAPDoc
%global GAPDoc_files chooser.html lefttoc.css manual.css manual.js nocolorprompt.css ragged.css rainbow.js times.css toggless.css toggless.js

# When bootstrapping a new architecture, there are no GAPDoc, gap-pkg-primgrp,
# gap-pkg-smallgrp, or gap-pkg-transgrp packages yet, but the gap binary
# refuses to run unless all four are present.  Therefore, build as follows:
# 1. Build this package in bootstrap mode.
# 2. Build GAPDoc in bootstrap mode.
# 3. Build gap-pkg-autodoc in bootstrap mode.
# 4. Build gap-pkg-io
# 5. Build GAPDoc in non-bootstrap mode.
# 6. Build gap-pkg-autodoc in non-bootstrap mode.
# 7. Build gap-pkg-primgrp and gap-pkg-smallgrp.
# 8. Build gap-pkg-transgrp.
# 9. Build this package in non-bootstrap mode.
%bcond bootstrap 0

Name:           gap
Version:        4.14.0
Release:        %autorelease
Summary:        Computational discrete algebra

%global majver %(cut -d. -f1-2 <<< %{version})

License:        GPL-2.0-or-later
URL:            https://www.gap-system.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        gap-README.fedora
Source2:        update-gap-workspace
Source3:        gap.xml
Source4:        org.gap-system.gap.desktop
Source5:        org.gap-system.gap.metainfo.xml
Source6:        gap.1.in
Source7:        gac.1.in
Source8:        update-gap-workspace.1
Source9:        gap.vim
Source10:       gapicon.bmp
# This patch applies a change from Debian to allow help files to be in gzip
# compressed DVI files, and also adds support for viewing with xdg-open.
Patch:          %{name}-help.patch
# Avoid the popcount instruction on systems that do not support it
Patch:          %{name}-popcount.patch
# Use zlib-ng directly instead of via the compatibility layer
Patch:          %{name}-zlib-ng.patch
# Work around for build errors with C23
# https://github.com/gap-system/gap/issues/5857
Patch:          %{name}-c23.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
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
BuildRequires:  pkgconfig(zlib-ng)
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

%conf
# Get the README
cp -p %{SOURCE1} README.fedora

# Regenerate the configure script
autoreconf -fi .

%build
# -Wl,-z,now breaks use of RTLD_LAZY
export LDFLAGS='%{build_ldflags} -Wl,-z,lazy'
export STRIP=%{_bindir}/true
%configure --disable-maintainer-mode

%make_build V=1

# Rebuild the manuals from source
export GAP_DIR=$PWD
make doc

# Build gapmacrodoc.pdf
cd doc
pdftex gapmacrodoc.tex
pdftex gapmacrodoc.tex
cd -

# Remove build paths
sed -i "s|$PWD|%{gapdir}|g" sysinfo.gap gac doc/make_doc

# Don't link every package shared object with libpthread
sed -i 's/[[:blank:]]*-pthread[[:blank:]]*//' sysinfo.gap

# Create an RPM macro file for GAP packages
cat > macros.%{name} << EOF
%%gap_version %{version}
%%gap_archdir %{gaparchdir}
%%gap_libdir %{gaplibdir}

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

# Add executable bits to the library
chmod 0755 %{buildroot}%{_libdir}/libgap.so.*

# Link, rather than copy, identical binaries
rm %{buildroot}%{gaparchdir}/gap
ln %{buildroot}%{_bindir}/gap %{buildroot}%{gaparchdir}/gap

# Remove files we do not want or install elsewhere
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
bmptopnm %{SOURCE10} > gapicon.pnm
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
sed 's|@VERSION@|%{version}|' %{SOURCE6} > %{buildroot}%{_mandir}/man1/gap.1
sed 's|@VERSION@|%{version}|' %{SOURCE7} > %{buildroot}%{_mandir}/man1/gac.1
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
%{_libdir}/libgap.so.9
%{_libdir}/libgap.so
%{_libdir}/pkgconfig/libgap.pc

%changelog
%autochangelog
