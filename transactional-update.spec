Name:           transactional-update
Version:        3.6.2
Release:        4%{?dist}
Summary:        Transactional Updates with btrfs and snapshots

# transactional-update and tukit is GPLv2+ everything else is LGPLv2+ or GPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/openSUSE/transactional-update
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Backports from upstream
Patch0001:      0001-Fix-missing-cstring-include-for-strerror.patch

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3dist(lxml)
BuildRequires:  %{_bindir}/xmllint
BuildRequires:  %{_bindir}/xsltproc
BuildRequires:  %{_bindir}/w3m

%description
transactional-update is a tool to update a system in an atomic
way with btrfs and snapshots.

#--------------------------------------------------------------------

%package -n tukit
Summary:        Tool for doing transactional updates using Btrfs snapshots
License:        GPLv2+
Requires:       libtukit%{?_isa} = %{version}-%{release}

%description -n tukit
tukit is a simple tool to make changes to a system in an atomic way
with btrfs and snapshots.

%post -n tukit
%systemd_post create-dirs-from-rpmdb.service

%preun -n tukit
%systemd_preun create-dirs-from-rpmdb.service

%files -n tukit
%license COPYING gpl-2.0.txt
%doc README.md NEWS
%{_sbindir}/tukit
%{_sbindir}/create_dirs_from_rpmdb
%{_unitdir}/create-dirs-from-rpmdb.service

#--------------------------------------------------------------------

%package -n dracut-%{name}
Summary:        Dracut module for supporting transactional updates
License:        GPLv2+
Supplements:    (tukit and kernel)
Requires:       tukit = %{version}-%{release}
BuildArch:      noarch

%description -n dracut-%{name}
This package contains the dracut modules for handling early boot aspects
for transactional updates.

%files -n dracut-%{name}
%license COPYING gpl-2.0.txt
%doc README.md NEWS
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/modules.d/50transactional-update/

#--------------------------------------------------------------------

%package -n libtukit
Summary:        Library for doing transactional updates using Btrfs snapshots
License:        GPLv2+ or LGPLv2+
Obsoletes:      tukit-libs < 3.2.0-2
Provides:       tukit-libs = %{version}-%{release}
Provides:       tukit-libs%{?_isa} = %{version}-%{release}
Requires:       btrfs-progs
Requires:       lsof
Requires:       rsync
Requires:       snapper

%description -n libtukit
This package contains the libraries required for programs to do
transactional updates using btrfs snapshots.

%files -n libtukit
%license COPYING gpl-2.0.txt lgpl-2.1.txt
%{_libdir}/libtukit.so.*

#--------------------------------------------------------------------

%package -n tukit-devel
Summary:        Development files for tukit library
License:        GPLv2+ or LGPLv2+
Requires:       libtukit%{?_isa} = %{version}-%{release}

%description -n tukit-devel
This package contains the files required to develop programs to do
transactional updates using btrfs snapshots.

%files -n tukit-devel
%license COPYING gpl-2.0.txt lgpl-2.1.txt
%{_includedir}/tukit/
%{_libdir}/libtukit.so
%{_libdir}/pkgconfig/tukit.pc

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
autoreconf -fiv
%configure
%make_build


%install
%make_install

# Delete static archives and libtool cruft
rm -rf %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/*.la

# Delete transactional-update and associated files, as it's SUSE-specific
rm -rf %{buildroot}%{_sbindir}/transactional-update*
rm -rf %{buildroot}%{_sbindir}/tu-rebuild-kdump-initrd
rm -rf %{buildroot}%{_unitdir}/transactional-update*
rm -rf %{buildroot}%{_prefix}%{_sysconfdir}
rm -rf %{buildroot}%{_sysconfdir}
rm -rf %{buildroot}%{_mandir}
rm -rf %{buildroot}%{_docdir}


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Apr 17 2022 Neal Gompa <ngompa@fedoraproject.org> - 3.6.2-3
- Fix build with GCC 12 (RH#2047043)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Neal Gompa <ngompa@fedoraproject.org> - 3.6.2-1
- Update to 3.6.2 (RH#2025199)

* Sat Nov 13 2021 Neal Gompa <ngompa@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1 (RH#1989208)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Neal Gompa <ngompa13@gmail.com> - 3.4.0-1
- Update to 3.4.0 (RH#1937546)

* Fri Mar 26 2021 Neal Gompa <ngompa13@gmail.com> - 3.3.0-1
- Update to 3.3.0 (RH#1937546)

* Wed Mar 10 2021 Neal Gompa <ngompa13@gmail.com> - 3.2.1-1
- Update to 3.2.1 (RH#1937546)

* Sun Mar 07 2021 Neal Gompa <ngompa13@gmail.com> - 3.2.0-2
- Rename tukit-libs package to libtukit

* Sun Mar 07 2021 Neal Gompa <ngompa13@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Fri Feb 12 2021 Neal Gompa <ngompa13@gmail.com> - 3.1.2-0.1
- Update to 3.1.2
- Drop upstreamed patches

* Thu Feb 11 2021 Neal Gompa <ngompa13@gmail.com> - 3.1.1-0.1
- Update to 3.1.1
- Add patch to fix tukit within daemons
- Add patch to drop obsolete autotools macro for libtool

* Wed Feb 03 2021 Neal Gompa <ngompa13@gmail.com> - 3.1.0-0.1
- Update to 3.1.0
- Update license tags

* Wed Jan 27 2021 Neal Gompa <ngompa13@gmail.com> - 3.0.0-0.1
- Update to final 3.0 release

* Tue Dec 29 2020 Neal Gompa <ngompa13@gmail.com> - 3.0~git20201223.c43c678-0.2
- Package dracut module and create-dirs-from-rpmdb service

* Wed Dec 23 2020 Neal Gompa <ngompa13@gmail.com> - 3.0~git20201223.c43c678-0.1
- Update to new git snapshot
- Drop upstreamed patch
- Add missing runtime dependencies

* Wed Dec 23 2020 Neal Gompa <ngompa13@gmail.com> - 3.0~git20201214.373f611-0.1
- Initial packaging
