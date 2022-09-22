%define _legacy_common_support 1

Name:           maildir-utils
Version:        1.8.9
Release:        1%{?dist}
Summary:        A command-line mail organization utility

License:        GPLv3+
URL:            http://www.djcbsoftware.nl/code/mu/index.html
Source0:        https://github.com/djcb/mu/releases/download/v%{version}/mu-%{version}.tar.xz

BuildRequires: make
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
%description guile
This package contains the Guile bindings for mu
(maildir-utils).

%package guile-devel
Summary:        Mu-Guile development files
Requires:       %{name}-guile%{?_isa} = %{version}-%{release}
%description guile-devel
This package contains the Guile development files for mu
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
%{_datadir}/guile/site/2.2/mu.scm
%{_datadir}/guile/site/2.2/mu/

%files guile-devel
%{_libdir}/libguile-mu.so


%changelog
* Thu Sep 01 2022 Jani Juhani Sinervo <jani@sinervo.fi> - 1.8.9-1
- Update to 1.8.9

* Thu Sep 01 2022 Jakub Kadlcik <frostyx@email.cz> - 1.8.5-1
- Update to a new upstream version

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 01 2021 Jani Juhani Sinervo <jani@sinervo.fi> - 1.6.6-1
- Update to latest upstream version

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 30 2021 Jani Juhani Sinervo <jani@sinervo.fi> - 1.4.15
- Update to latest upstream version

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 19 2020 Maximiliano Sandoval <msandova@protonmail.com> - 1.4.10-1
- Update to 1.4.10

* Thu Apr 23 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 1.4.1-1
- Update to 1.4.1
- Fix replying to mail (rhbz 1823325)

* Sun Mar 01 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 1.3.9-1.20200229git17f38dc
- Update to 1.3.9
- Fix build issue on rawhide

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Maximiliano Sandoval <msandova@protonmail.com> - 1.3.3-1
- Update to 1.3.3, removed patch merged upstream

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 2019 Omair Majid <omajid@redhat.com> - 1.3.1-2
- Fix mu4e-news by fixing mu4e's documentation root path

* Wed Jun 19 2019 Jani Juhani Sinervo <jani@sinervo.fi> - 1.3.1-1
- Initial spec
