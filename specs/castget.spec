
Name:           castget
Version:        2.0.1
Release:        %autorelease
Summary:        A command-line podcast downloader

License:        LGPL-2.1-or-later
URL:            https://castget.johndal.com/
Source0:        https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.bz2
# https://github.com/mlj/castget/issues/65
Patch0:		stdlib.patch

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  id3lib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires: make

%description
castget is a simple, command-line based RSS enclosure downloader. It is
primarily intended for automatic, unattended downloading of podcasts.


%prep
%autosetup -p 1


%build
# Workaround for C23 incompatibility in id3lib
# https://bugzilla.redhat.com/show_bug.cgi?id=2342124
# https://sourceforge.net/p/id3lib/bugs/215/
CFLAGS+=-std=gnu17
%configure LDFLAGS=-Wl,--copy-dt-needed-entries
%make_build


%install
%make_install


%files
%license COPYING.LIB
%doc AUTHORS CHANGES.md ChangeLog.old INSTALL castgetrc.example
%{_bindir}/%{name}
%{_mandir}/man?/*


%changelog
%autochangelog
