Name:           mate-common
Summary:        mate common build files
Version:        1.28.0
Release:        %autorelease
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.28/mate-common-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  automake autoconf

Requires:       automake
Requires:       autoconf
Requires:       autoconf-archive 
Requires:       gettext
Requires:       intltool
Requires:       libtool
Requires:       glib2-devel
Requires:       gtk-doc
Requires:       itstool
Requires:       yelp-tools

%description
binaries for building all MATE desktop sub components

%prep
%autosetup -p1

%build
%configure

make %{?_smp_mflags} V=1


%install
%{make_install}


%files
%{_bindir}/mate-*
%{_datadir}/aclocal/mate-*.m4
%{_datadir}/mate-common
%{_mandir}/man1/*

%changelog
%autochangelog
