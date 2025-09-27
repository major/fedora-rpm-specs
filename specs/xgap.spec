%global gap_pkgname xgap
%global giturl      https://github.com/gap-packages/xgap

Name:           %{gap_pkgname}
Version:        4.33
Release:        %autorelease
Summary:        GUI for GAP

# The project as a whole is GPL-2.0-or-later.
# src.x11/selfile.{c,h} is HPND.
License:        GPL-2.0-or-later AND HPND
URL:            https://gap-packages.github.io/xgap/
VCS :           git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Created by Jerry James <loganjerry@gmail.com>
Source1:        %{name}.desktop
# Created by Paulo César Pereira de Andrade
# <paulo.cesar.pereira.de.andrade@gmail.com>
Source2:        XGap
# This patch quiets a compiler warning.
Patch:          %{name}-warning.patch
# Fix FTBFS due to an incompatible pointer type
Patch:          %{name}-incompatible-pointer.patch
# Adapt to a change in the gap binary location in gap 4.15.0
Patch:          %{name}-gap-path.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    gap
BuildOption(install): bin examples htm lib tst
BuildOption(check): tst/testall.g

BuildRequires:  desktop-file-utils
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-smallgrp-doc
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  tth

Requires:       gap%{?_isa}

Provides:       gap-pkg-%{gap_pkgname} = %{version}-%{release}

%description
An X Windows GUI for GAP.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# Nimbus: AGPL-3.0-only
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND AGPL-3.0-only
Summary:        XGap documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-smallgrp-doc

%description doc
This package contains documentation for %{gap_pkgname}.

%prep
%autosetup -p0

%build
export CFLAGS='%{build_cflags} -D_GNU_SOURCE'
%configure --with-gaproot=%{gap_archdir}
%make_build

# Fix a path in the shell wrapper
sed -i "s,$PWD,\$GAP_DIR/pkg/%{name}-%{version}," bin/xgap.sh

# Link to main GAP documentation
ln -s %{gap_libdir}/etc ../../etc
ln -s %{gap_libdir}/doc ../../doc
ln -s %{gap_libdir}/pkg/smallgrp ..
ln -s %{name}-%{version} ../%{name}
cd doc
./make_doc
cd -
rm -f ../%{name} ../smallgrp ../../{doc,etc}

%install -a
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{gap_archdir}/pkg/%{name}/bin/xgap.sh %{buildroot}%{_bindir}/xgap
rm %{buildroot}%{gap_archdir}/pkg/%{name}/bin/*/{Makefile,config*,*.o}

# Install the desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --mode=644 --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install the X resource file
mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
cp -p %{SOURCE2} %{buildroot}%{_datadir}/X11/app-defaults

%check -p
# Temporarily modify the test runner to add the necessary -l argument
sed -i.orig 's|"-p"|"-l","%{buildroot}%{gap_archdir};",&|' \
   %{buildroot}%{gap_archdir}/pkg/%{name}/tst/xgap_test.g

%check -a
mv %{buildroot}%{gap_archdir}/pkg/%{name}/tst/xgap_test.g.orig \
   %{buildroot}%{gap_archdir}/pkg/%{name}/tst/xgap_test.g

%files
%doc CHANGES README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/X11/app-defaults/XGap
%dir %{gap_archdir}/pkg/%{name}/
%{gap_archdir}/pkg/%{name}/*.g
%{gap_archdir}/pkg/%{name}/bin/
%{gap_archdir}/pkg/%{name}/lib/
%{gap_archdir}/pkg/%{name}/tst/

%files doc
%docdir %{gap_archdir}/pkg/%{name}/doc/
%docdir %{gap_archdir}/pkg/%{name}/examples/
%docdir %{gap_archdir}/pkg/%{name}/htm/
%{gap_archdir}/pkg/%{name}/doc/
%{gap_archdir}/pkg/%{name}/examples/
%{gap_archdir}/pkg/%{name}/htm/

%changelog
%autochangelog
