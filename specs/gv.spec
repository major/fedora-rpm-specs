Summary: A X front-end for the Ghostscript PostScript(TM) interpreter
Name: gv
Version: 3.7.4
Release: %autorelease
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
# X11 built into ghostscript starting with 10.0
%if 0%{?fedora} || 0%{?rhel} >= 10
Requires: ghostscript
%else
Requires: ghostscript-x11
%endif
URL: http://www.gnu.org/software/gv/
Source0: ftp://ftp.gnu.org/gnu/gv/gv-%{version}.tar.gz
#Source0: ftp://alpha.gnu.org/gnu/gv/gv-%{version}.tar.gz
Source1: gv.png
# Check for null pointers in resource requests
# https://savannah.gnu.org/bugs/?38727
Patch0:  gv-resource.patch
# Change tab to space in gv_user_res.dat
# http://savannah.gnu.org/patch/?7998
Patch1:  gv-dat.patch
# Support aarch64
Patch2:  gv-aarch64.patch
# Fix bounding box recognition
Patch3:  gv-bounding-box.patch
# Fix NULL access segfault
# https://bugzilla.redhat.com/show_bug.cgi?id=1071238
Patch4:  gv-bug1071238.patch
# Fix PDF printing
# https://bugzilla.redhat.com/show_bug.cgi?id=1536211
Patch5:  gv-bz1536211.patch
# Fix buffer overflows in resource.c
# https://savannah.gnu.org/patch/?10096
Patch6:  gv-overflow.patch
BuildRequires:  gcc
BuildRequires: /usr/bin/makeinfo
BuildRequires: Xaw3d-devel
BuildRequires: libXinerama-devel
BuildRequires: zlib-devel, bzip2-devel
BuildRequires: desktop-file-utils
BuildRequires: make
ExcludeArch:   %{ix86}

%description
GNU gv is a user interface for the Ghostscript PostScript(TM) interpreter.
Gv can display PostScript and PDF documents on an X Window System.


%prep
%setup -q
%patch -P0 -p1 -b .resource
%patch -P1 -p1 -b .resdat
%patch -P2 -p1 -b .aarch64
%patch -P3 -p2 -b .bounding-box
%patch -P4 -p1 -b .bug1071238
%patch -P5 -p1 -b .bz1536211
%patch -P6 -p2 -b .overflow


%build
%configure
%make_build


%install
%make_install

#Still provide link
ln $RPM_BUILD_ROOT%{_bindir}/gv $RPM_BUILD_ROOT%{_bindir}/ghostview

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

cat > gv.desktop <<EOF
[Desktop Entry]
Name=GNU GV PostScript/PDF Viewer
GenericName=PostScript/PDF Viewer
Comment="View PostScript and PDF files"
Type=Application
Icon=gv
MimeType=application/postscript;application/pdf;
StartupWMClass=GV
Exec=gv %f
EOF

desktop-file-install \
       --add-category=Applications\
       --add-category=Graphics \
       --dir %{buildroot}%{_datadir}/applications/ \
       gv.desktop

#Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -p %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/pixmaps

# Remove info dir file
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/ghostview
%{_bindir}/gv
%{_bindir}/gv-update-userconfig
%{_datadir}/gv/
%{_datadir}/applications/gv.desktop
%{_datadir}/info/gv.info.gz
%{_datadir}/pixmaps/gv.png
%{_mandir}/man1/gv.*
%{_mandir}/man1/gv-update-userconfig.*


%changelog
%autochangelog
