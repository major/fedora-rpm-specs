%global xfceversion 4.18

Name:           xfce4-dev-tools
Version:        4.18.0
Release:        %autorelease
Summary:        Xfce developer tools

License:        GPLv2+
URL:            http://xfce.org/~benny/projects/xfce4-dev-tools/
#VCS git:git://git.xfce.org/xfce/xfce4-dev-tools
Source0:        http://archive.xfce.org/src/xfce/xfce4-dev-tools/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  glib2-devel
Requires:       autoconf
Requires:       automake
Requires:       gawk
Requires:       git
Requires:       glib2-devel
Requires:       grep
Requires:       gtk-doc
Requires:       intltool

%description
This package contains common tools required by Xfce developers and people
that want to build Xfce from SVN.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install


%files
%license COPYING
%doc AUTHORS ChangeLog HACKING NEWS
%{_bindir}/xfce-build
%{_bindir}/xfce-do-release
%{_bindir}/xfce-get-release-notes
%{_bindir}/xfce-get-translations
%{_bindir}/xfce-update-news
%{_bindir}/xdt-autogen
%{_bindir}/xdt-csource
%{_datadir}/aclocal/*
%{_mandir}/man1/xdt-csource.1.gz

%changelog
%autochangelog
