%global prerel pre1
%global xfceversion 4.20

Name:           xfce4-dev-tools
Version:        4.20.0
Release:        %autorelease
Summary:        Xfce developer tools

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/xfce/xfce4-dev-tools/start
#VCS git:https://gitlab.xfce.org/xfce/xfce4-dev-tools.git
Source0:        http://archive.xfce.org/xfce/%{xfceversion}/src/%{name}-%{version}.tar.bz2

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  glib2-devel
BuildRequires:  libxslt-devel
BuildRequires:  meson
Requires:       autoconf
Requires:       automake
Requires:       gawk
Requires:       git
Requires:       glib2-devel
Requires:       grep
Requires:       intltool

%description
This package contains common tools required by Xfce developers and people
that want to build Xfce from Git.

%prep
%autosetup

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
%{_bindir}/xdt-check-abi
%{_bindir}/xdt-csource
%{_bindir}/xdt-gen-visibility
%{_datadir}/aclocal/*
%{_mandir}/man1/xdt-csource.1.gz

%changelog
%autochangelog
