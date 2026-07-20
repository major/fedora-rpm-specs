Summary: imake source code configuration and build system
Name: imake
Version: 1.0.10
Release: %autorelease
License: MIT-open-group AND HPND
URL: http://www.x.org

Source0: https://www.x.org/pub/individual/util/imake-%{version}.tar.xz
Source1: https://www.x.org/pub/individual/util/makedepend-1.0.8.tar.xz
Source2: https://www.x.org/pub/individual/util/gccmakedep-1.0.3.tar.bz2
Source3: https://www.x.org/pub/individual/util/xorg-cf-files-1.0.8.tar.xz
Source4: https://www.x.org/pub/individual/util/lndir-1.0.4.tar.xz
Patch11: imake-1.0.2-abort.patch
Patch12: xorg-cf-files-1.0.8-DEFAULT_SOURCE.patch
ExcludeArch: %{ix86}

BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorg-x11-proto-devel
BuildRequires: gcc
BuildRequires: gcc-c++
# imake is not functional without cc
Requires:      gcc

Provides: ccmakedep cleanlinks gccmakedep lndir makedepend makeg
Provides: mergelib mkdirhier mkhtmlindex revpath xmkmf

%description
Imake is a deprecated source code configuration and build system which
has traditionally been supplied by and used to build the X Window System
in X11R6 and previous releases.  As of the X Window System X11R7 release,
the X Window system has switched to using GNU autotools as the primary
build system, and the Imake system is now deprecated, and should not be
used by new software projects.  Software developers are encouraged to
migrate software to the GNU autotools system.

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4

# imake patches
pushd %{name}-%{version}
%patch -P 11 -p1 -b .abort
popd
pushd xorg-cf-files-1.0.8
%patch -P 12 -p1 -b .defaultsource
popd

%build
# Build everything
{
   for pkg in imake makedepend gccmakedep lndir xorg-cf-files ; do
      pushd $pkg-*
      case $pkg in
         imake|xorg-cf-files)
            %configure --with-config-dir=%{_datadir}/X11/config
            ;;
         *)
            %configure
            ;;
      esac
      make
      popd
   done
}

%install
# Install everything
{
   for pkg in imake makedepend gccmakedep lndir xorg-cf-files ; do
      pushd $pkg-*
      make install DESTDIR=$RPM_BUILD_ROOT
      popd
   done
}

%files
%{_bindir}/ccmakedep
%{_bindir}/cleanlinks
%{_bindir}/gccmakedep
%{_bindir}/imake
%{_bindir}/lndir
%{_bindir}/makedepend
%{_bindir}/makeg
%{_bindir}/mergelib
%{_bindir}/mkdirhier
%{_bindir}/mkhtmlindex
%{_bindir}/revpath
%{_bindir}/xmkmf
%dir %{_datadir}/X11/config
%{_datadir}/X11/config/*.cf
%{_datadir}/X11/config/*.def
%{_datadir}/X11/config/*.rules
%{_datadir}/X11/config/*.tmpl
#%%dir %%{_mandir}/man1x
%{_mandir}/man1/ccmakedep.1*
%{_mandir}/man1/cleanlinks.1*
%{_mandir}/man1/gccmakedep.1*
%{_mandir}/man1/imake.1*
%{_mandir}/man1/lndir.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mergelib.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/mkhtmlindex.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/xmkmf.1*

%changelog
%autochangelog
