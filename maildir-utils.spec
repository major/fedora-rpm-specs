%define _legacy_common_support 1

Name:           maildir-utils
Version:        1.8.11
Release:        %autorelease
Summary:        A command-line mail organization utility

License:        GPLv3+
URL:            http://www.djcbsoftware.nl/code/mu/index.html
Source0:        https://github.com/djcb/mu/releases/download/v%{version}/mu-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++

# Needed for patching stuff
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  xapian-core
BuildRequires:  xapian-core-devel
BuildRequires:  xapian-core-libs
BuildRequires:  texinfo
BuildRequires:  libuuid-devel
BuildRequires:  dh-autoreconf
# Current version of mu4e supports emacs versions >= 24.4
BuildRequires:  emacs >= 24.4
Requires:       emacs-filesystem >= 24.4
Requires:       xapian-core

%description
Maildir-utils (mu) is a command-line utility for organizing and
searching email.

%package guile
Summary:        Guile bindings for mu (maildir-utils)
BuildRequires:  guile22-devel
Requires:       guile22
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-guile-devel < 1.8.10-1
%description guile
This package contains the Guile bindings for mu
(maildir-utils).

%prep
%autosetup -n mu-%{version}
# Makes sure that the docs are installed in the proper place
sed -i 's|${prefix}/share/doc/mu|${prefix}/share/doc/%{name}|' configure.ac

%build
# Because of the patch above, we have to regenerate the build files.
autoreconf --force --install --verbose || exit $?
# Disable the toy GTK GUI "mug".
%configure --disable-gtk --disable-webkit --disable-static --enable-shared
%make_build GUILE_SNARF=guile-snarf2.2


%install
%make_install

# We must remove the "mu"-documentation directory
# since all of those documents are under
# maildir-utils
rm -r %{buildroot}/%{_docdir}/mu

# Remove the dir that gets installed alongside the info-pages
# as it would conflict with other packages.
rm %{buildroot}/%{_infodir}/dir

# Remove libtool .la files
rm %{buildroot}/%{_libdir}/libguile-mu.la

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
%{_datadir}/mu/
%{_libdir}/libguile-mu.so.0*
%{_libdir}/libguile-mu.so
%{_datadir}/guile/site/2.2/mu.scm
%{_datadir}/guile/site/2.2/mu/

%changelog
%autochangelog
