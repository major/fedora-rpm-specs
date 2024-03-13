Name:           maildir-utils
Version:        1.12.1
Release:        %autorelease
Summary:        A command-line mail organization utility

License:        GPL-3.0-or-later
URL:            http://www.djcbsoftware.nl/code/mu/index.html
Source0:        https://github.com/djcb/mu/releases/download/v%{version}/mu-%{version}.tar.xz
Patch0:         1.12.1-mu4e-docs-directory.patch
Patch1:         1.12.1-mu-docs-directory.patch
Patch2:         1.12.1-mu-guile-scripts-directory.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++

# Needed for patching stuff
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  xapian-core
BuildRequires:  xapian-core-devel
BuildRequires:  xapian-core-libs
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  libuuid-devel
BuildRequires:  dh-autoreconf
BuildRequires:  git-core
# FIXME: Make sure cld2 also works in s390x
#BuildRequires:  cld2-devel
# Current version of mu4e supports emacs versions >= 26.3
BuildRequires:  emacs >= 26.3
Requires:       emacs-filesystem >= 26.3
Requires:       xapian-core

%description
Maildir-utils (mu) is a command-line utility for organizing and
searching email.

%package guile
Summary:        Guile bindings for mu (maildir-utils)
BuildRequires:  guile30-devel
Requires:       guile30
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-guile-devel < 1.8.10-1
%description guile
This package contains the Guile bindings for mu
(maildir-utils).

%prep
%autosetup -n mu-%{version} -S git

%build
# FIXME: Make sure cld2 also works in s390x
%meson \
    -Dguile=enabled \
    -Dcld2=disabled \
    -Dreadline=enabled
%meson_build


%install
%meson_install

%files
%license COPYING
%doc NEWS.org mu4e/mu4e-about.org
%{_bindir}/mu
%{_emacs_sitelispdir}/mu4e
%{_infodir}/mu4e.info.gz
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files guile
%{_infodir}/mu-guile.info.gz
%{_datadir}/maildir-utils/
%{_libdir}/guile/3.0/extensions/libguile-mu.so
%{_datadir}/guile/site/3.0/mu/
%{_datadir}/guile/site/3.0/mu.scm

%changelog
%autochangelog
