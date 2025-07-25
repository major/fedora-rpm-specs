Summary:        Very fast network log-on cracker
Name:           hydra
Version:        9.5
Release:        9%{?dist}
License:        AGPL-3.0-only
URL:            https://github.com/vanhauser-thc/thc-hydra
VCS:            git:https://github.com/vanhauser-thc/thc-hydra
# Old URL       https://www.thc.org/thc-hydra/

Source0:        https://github.com/vanhauser-thc/thc-hydra/archive/v%{version}/%{name}-%{version}.tar.gz
# Sent upstream via email 20120518
Patch0:         hydra-use-system-libpq-fe.patch
Patch1:         hydra-fix-dpl4hydra-dir.patch

BuildRequires:  afpfs-ng-devel
BuildRequires:  apr-devel
BuildRequires:  desktop-file-utils
BuildRequires:  firebird-devel
BuildRequires:  freerdp2-devel
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libbson-devel
BuildRequires:  libfbclient2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  libmemcached-devel
BuildRequires:  libpq-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel
BuildRequires:  libwinpr2-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  memcached-devel
BuildRequires:  mongo-c-driver-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  subversion-devel

%description
Hydra is a parallelized log-in cracker which supports numerous protocols to
attack. New modules are easy to add, beside that, it is flexible and very fast.

This tool gives researchers and security consultants the possibility to show
how easy it would be to gain unauthorized access from remote to a system.

%package frontend
Summary: The GTK+ front end for hydra
Requires: hydra = %{version}-%{release}
%description frontend
This package includes xhydra, a GTK+ front end for hydra. 

%prep
%autosetup -p 1 -n thc-hydra-%{version}

%build
%configure --nostrip
%make_build

%install
%make_install \
    PREFIX="" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}/man1" \
    DATADIR="%{_datadir}/%{name}" \
    PIXDIR="%{_datadir}/pixmaps" \
    APPDIR="%{_datadir}/applications"

# Fix dpl4hydra.sh (w/o buildroot prefix)
sed -i 's|^INSTALLDIR=.*|INSTALLDIR=/usr|' %{buildroot}/%{_bindir}/dpl4hydra.sh

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/xhydra.desktop

%files
%doc CHANGES README
%license LICENSE
%{_bindir}/dpl4hydra.sh
%{_bindir}/hydra
%{_bindir}/hydra-wizard.sh
%{_bindir}/pw-inspector
%{_datadir}/%{name}
%{_mandir}/man1/hydra.1*
%{_mandir}/man1/pw-inspector.1*

%files frontend
%{_bindir}/xhydra
%{_datadir}/pixmaps/xhydra.png
%{_datadir}/applications/xhydra.desktop
%{_mandir}/man1/xhydra.1*

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Simone Caronni <negativo17@gmail.com> - 9.5-6
- Clean up SPEC file.
- Adjust build requirements:
  * Use FreeRDP 2, FreeRDP 3 does not build.
  * Remove exceptions for s390x.
  * Drop MongoDB build requirement, it does no longer exist.
- Use upstream desktop and icon file, they are the same.
- Clean up repository of unused files.
- Trim changelog.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 29 2023 Michal Ambroz <rebus _at seznam.cz>  9.5-3
- merge #PR1 - add missing libsmbclient dependency

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Michal Ambroz <rebus _at seznam.cz>  9.5-1
- bump to new release 9.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Florian Weimer <fweimer@redhat.com> - 9.4-2
- C99 compatibility fixes

* Sun Oct 16 2022 Othman Madjoudj <athmane@fedoraproject.org> - 9.4-1
- Update to 9.4 (rhbz #2125386)
- Switch to PCRE2 (rhbz #2128308)

* Tue Aug 16 2022 Simone Caronni <negativo17@gmail.com> - 9.3-1
- Update to 9.3, fix build with recent updated libraries.

* Mon Aug 15 2022 Simone Caronni <negativo17@gmail.com> - 9.2-9
- Rebuild for updated FreeRDP.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Than Ngo <than@redhat.com> - 9.2-7
- fixed bz#2022029, FTBFS with OpenSSL 3.0.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 9.2-5
- Rebuilt with OpenSSL 3.0.0

* Mon Aug 02 2021 Othman Madjoudj <athmane@fedoraproject.org> - 9.2-4
- Disable Firebird support on s390x since it's not available anymore (RHBZ #1987570)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 9.2-2
- Rebuild for updated FreeRDP.

* Tue Mar 23 2021 Michal Ambroz <rebus _at seznam.cz>  9.2-1
- bump to new release 9.2

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 9.0-7
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
