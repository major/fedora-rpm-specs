Name:           qiv
Version:        3.0.4
Release:        %autorelease

Summary:        Quick Image Viewer

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://spiegl.de/qiv/
Source0:        https://codeberg.org/ciberandy/qiv/archive/v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  file-devel
BuildRequires:  lcms2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libexif-devel
BuildRequires:  libtiff-devel

%description
qiv is a very small and pretty fast gdk3 image viewer.

%prep
%autosetup -n %{name}

%build
%make_build

%install
%make_install PREFIX="%{buildroot}%{_prefix}" STRIP_FLAG=""
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
