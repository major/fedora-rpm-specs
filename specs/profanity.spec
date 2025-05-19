Name:           profanity
Version:        0.15.0
Release:        1%{?dist}
Summary:        A console based XMPP client

License:        GPL-3.0-only
URL:            https://profanity-im.github.io/
Source0:        https://profanity-im.github.io/tarballs/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf-archive
BuildRequires:  libtool
# Base:
BuildRequires:  libstrophe-devel
BuildRequires:  ncurses-devel
BuildRequires:  glib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  python-unversioned-command
# Optional dependancies for support:
# Desktop notification support
BuildRequires:  libnotify-devel
# OTR support
BuildRequires:  libotr-devel
# PGP support
BuildRequires:  gpgme-devel
# OMEMO support
BuildRequires:  libsignal-protocol-c-devel
# OMEMO support (>= 1.7)
BuildRequires:  libgcrypt-devel
# Python plugin support
BuildRequires:  python3-devel
# Support for display OMEMO QR code
BuildRequires:  qrencode-devel
# For tests:
BuildRequires:  libcmocka-devel
# For docs:
BuildRequires:  doxygen
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  texinfo
BuildRequires:  tree

%description
Profanity is a console based XMPP client written in C using ncurses
and libstrophe, inspired by Irssi.



%package libs
Summary:       The shared libraries required for plugins of Profanity
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs
The %{name}-libs package provides the essential shared libraries for any
plugin of Profanity written in C.

See: https://profanity-im.github.io/plugins.html



%package        devel
Summary:        Development files for libraries used by plugins of Profanity
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing plugins written in C for Profanity.



%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains docbook documentation for developing
applications that use %{name}.



%prep
%autosetup
# Output docbook instead of HTML
sed -i "s/GENERATE_HTML          = YES/GENERATE_HTML          = NO/g" apidocs/c/c-prof.conf
sed -i "s/GENERATE_DOCBOOK       = NO/GENERATE_DOCBOOK       = YES/g" apidocs/c/c-prof.conf
sed -i "s/DOCBOOK_PROGRAMLISTING = NO/DOCBOOK_PROGRAMLISTING = YES/g" apidocs/c/c-prof.conf

%build
autoreconf -i -W all
%configure
%make_build

# Build HTML documentation
pushd apidocs/c/
doxygen c-prof.conf  # results are in apidocs/c/docbook/
tree
popd
pushd apidocs/python/
sphinx-apidoc -f -o . src
make texinfo  # results are in apidocs/python/_build/texinfo
pushd _build
pushd texinfo
makeinfo --docbook ProfanityPythonPluginsAPI.texi
tree
popd
popd
popd


%install
%make_install
# Remove libprofanity.la generated
rm -f %{buildroot}%{_libdir}/libprofanity.la

# Install docbook documentation for the doc subpackage
mkdir -p %{buildroot}%{_datadir}/help/en/profanity/
for file in apidocs/c/docbook/*.xml;
do
  install -m644 ${file} \
    %{buildroot}%{_datadir}/help/en/profanity
done
install -m644 apidocs/python/_build/texinfo/ProfanityPythonPluginsAPI.xml \
  %{buildroot}%{_datadir}/help/en/profanity

# Install example config file
cp -a profrc.example %{buildroot}%{_datadir}/%{name}/


%check
make check



%files
%license COPYING LICENSE.txt
%doc CHANGELOG README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%{_mandir}/man1/%{name}-*
%{_datadir}/%{name}/


%files libs
%{_libdir}/libprofanity.so.0*


%files devel
%{_libdir}/libprofanity.so
%{_includedir}/profapi.h


%files doc
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/profanity



%changelog
* Fri May 16 2025 Benson Muite <fed500@fedoraproject.org> - 0.15.0-1
- Update to latest release
- Use docbook

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14.0-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.14.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 3 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 0.14.0-1
- Update to 0.14.0
- Improve file ownership in doc subpackage
- Minor fix in the doc subpackage (no need to remove rst files)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.13.1-4
- Rebuilt for Python 3.12

* Thu Mar 2 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 0.13.1-3
- Enable displaying OMEMO QRcode support

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 12 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1
- Enable python plugin support

* Wed Sep 14 2022 Matthieu Saulnier <fantom@fedoraproject.org> - 0.13.0-1
- Update to 0.13.0
- Update SourceURL in spec file
- Remove python plugin support

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.11.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 12 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Wed Aug 25 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.11.0-2
- Package Review RHBZ#1995497:
  - Remove useless ldconfig scriptlets
  - Fix Requires tag of the doc subpackage
  - Fix summary and description of lib and devel subpackages
  - Reverse requirements between main package and libs subpackage
  - Move docfiles from libs subpackage to main package

* Mon Aug 09 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 0.11.0-1
- Package Review RHBZ#1995497:
  - Initial packaging
