Name:           pcb
Version:        4.3.0
Release:        %autorelease
Summary:        An interactive printed circuit board editor

License:        GPL-2.0-or-later
URL:            http://pcb.geda-project.org/index.html
Source0:        http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz

# Upstream http://git.geda-project.org/pcb/commit/?id=9dea9f5a3801d612f78c738fe7efccefa5745000
Patch1:         pcb-fedora-c99.patch

BuildRequires:  bison
BuildRequires:  cups
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  gettext-devel
BuildRequires:  gtkglext-devel
BuildRequires:  gtk2-devel
BuildRequires:  ImageMagick
BuildRequires:  intltool
BuildRequires:  libICE-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  perl-generators
BuildRequires:  tcl
BuildRequires:  tetex-latex
BuildRequires:  tk
BuildRequires:  unzip

Requires:       m4
Requires:       electronics-menu

%description
PCB is an interactive printed circuit board editor.
PCB includes a rats nest feature, design rule checking, and can provide
industry standard RS-274-X (Gerber), NC drill, and centroid data (X-Y data)
output for use in the board fabrication and assembly process. PCB offers
high end features such as an auto-router and trace optimizer which can
tremendously reduce layout time.

%package doc
Summary:        Documentation for PCB, an interactive printed circuit board editor
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains the documentation of PCB, an interactive printed circuit
board editor.

%prep
%autosetup -p1

# Convert ChangeLog to UTF-8
iconv -f iso-8859-1 -t utf-8 ChangeLog -o ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog

sed -i \
   's|examplesdir = $(pkgdatadir)/examples|examplesdir = @docdir@/examples|' \
   example/libraries/Makefile.*

sed -i \
   's|tutdir = $(pkgdatadir)/tutorial|tutdir = @docdir@/tutorial|' \
   tutorial/Makefile.*

touch aclocal.m4 Makefile.in

%build
export WISH=%{_bindir}/wish

%configure \
    --enable-dbus \
    --enable-toporouter \
    --disable-update-mime-database \
    --disable-update-desktop-database \
    --docdir=%{_pkgdocdir}

%make_build
pushd doc
make -t pcb.pdf pcb.info pcb.html
popd

%install
%make_install

# in /usr/share/pcb/newlib/ folder, sockets is an empty folder

desktop-file-install --vendor ""               \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

#
# Additional Examples
#
set +x
dest=%{buildroot}%{_pkgdocdir}/examples
for d in thermal pad puller ; do
   echo -n -e "... Fixing path of $d  \t"
   mkdir -p $dest/$d
   mv $dest/../$d.* $dest/$d
   install -pm 0644 doc/$d.{pcb,pdf} $dest/$d
   sed -i "s|$d.png|examples/$d/$d.png|" $dest/../%{name}.html
   echo "done"
done
set -x

## --- pcb supports for acpcircuits
# http://www.apcircuits.com/resources/links/pcb_unix.html
unzip tools/apctools.zip
install -p -m 755 apc*.pl  %{buildroot}%{_datadir}/%{name}/tools

# Removes duplicates
rm -f %{buildroot}%{_datadir}/%{name}/tools/apctools.zip

## ---

# Old versions of PCB don't support auto-route, pcb2ncap convert
# pcb format to ncap format used for mucspcb to auto-route the circuit.
# In newer versions of PCB, auto-route is included and pcb2ncap and mucspcb
# are no more needed.
rm -f %{buildroot}%{_datadir}/%{name}/tools/pcb2ncap.tgz

chmod 755 %{buildroot}%{_datadir}/%{name}/tools/{PCB2HPGL,pcbdiff,tgo2pcb.tcl,Merge*}

# remove unnecessary file
rm -f %{buildroot}%{_datadir}/%{name}/tools/gerbertotk.c

rm -rf %{buildroot}%{_datadir}/info/dir

mv %{buildroot}%{_pkgdocdir}/refcard.pdf %{buildroot}%{_pkgdocdir}/pcb-reference-card.pdf

# remove duplicates
rm -f %{buildroot}%{_bindir}/Merge*

# L#854396 0.20110918 needlessly installs gts static library & header file
rm -f %{buildroot}%{_libdir}/libgts.a %{buildroot}%{_includedir}/gts.h

# locale's
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Documentation sub-package
%files doc
%{_infodir}/%{name}*
%doc %{_pkgdocdir}/

# Main package
%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README

%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/pcb.xml
%{_datadir}/gEDA/scheme/gnet-pcbfwd.scm

%changelog
%autochangelog
