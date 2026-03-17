Name: cdw
Version: 0.8.1
Release: %autorelease
Summary: Front-end for tools used for burning data CD/DVD
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later 
URL:            https://cdw.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         0001-add-formatstring.patch

BuildRequires:  gcc
BuildRequires:  libburn-devel
BuildRequires:  libcdio-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# It does not make sense to install cdw without the packages below:
Requires:       dvd+rw-tools
Requires:       genisoimage
Requires:       wodim
Requires:       xorriso

%description
cdw is a ncurses based front-end for some command-line tools used for burning
data CD and DVD discs and for related tasks. The tools are: cdrecord/wodim,
mkisofs/genisoimage, growisofs, dvd+rw-mediainfo, dvd+rw-format, xorriso.
cdw is able to rip tracks from your audio CD to raw audio files.
Limited support for copying content of data CD and DVD discs to image files
is also provided. cdw can verify correctness of writing ISO9660 image to
CD or DVD disc using md5sum or some of  programs that verifies SHA hashes.

%prep
%autosetup -p1

%build
%configure LIBS="-lm"
%make_build

%install
%make_install

%check
%make_build check LIBS="-lm"

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
