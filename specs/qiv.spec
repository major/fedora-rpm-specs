Name:           qiv
Version:        2.3.3
Release:        %autorelease

Summary:        Quick Image Viewer

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://spiegl.de/qiv/
Source0:        http://spiegl.de/qiv/download/%{name}-%{version}.tgz

Patch0:         2.3.3-makefile-destdir.patch
Patch1:         2.3.3-fix-prototypes.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  imlib2-devel
BuildRequires:  file-devel
BuildRequires:  lcms2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libexif-devel
BuildRequires:  libtiff-devel

%description
qiv is a very small and pretty fast gdk2/Imlib2 image viewer.

%prep
%autosetup

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install PREFIX="%{_prefix}"
chmod 644 contrib/qiv-command.example

%files
%doc README Changelog README.TODO contrib/qiv-command.example
%license README.COPYING
%{_bindir}/qiv
%{_mandir}/man1/qiv.1*
%{_datadir}/applications/qiv.desktop
%{_datadir}/pixmaps/qiv.png

%changelog
%autochangelog
