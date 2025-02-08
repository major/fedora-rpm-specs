Name:           rsync-bpc
Version:        3.1.3.0
Release:        14%{?dist}
Summary:        A customized fork of rsync that is used as part of BackupPC

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/backuppc/rsync-bpc
Source0:        https://github.com/backuppc/rsync-bpc/releases/download/%{version}/%{name}-%{version}.tar.gz

# Fix for building on CentOS 6 in COPR
Patch0:         rsync-bpc-rsync_h.patch
Patch1:         rsync-bpc-configure-c99.patch
Patch2:         rsync-bpc-gcc_15.patch

BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  perl

Provides:       bundled(rsync) = 3.1.3


%description
Rsync-bpc is a customized version of rsync that is used as part of
BackupPC, an open source backup system.

The main change to rsync is adding a shim layer (in the subdirectory
backuppc, and in bpc_sysCalls.c) that emulates the system calls for
accessing the file system so that rsync can directly read/write files
in BackupPC's format.

Rsync-bpc is fully line-compatible with vanilla rsync, so it can talk
to rsync servers and clients.

Rsync-bpc serves no purpose outside of BackupPC.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc NEWS README
%{_bindir}/rsync_bpc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1.3.0-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Florian Weimer <fweimer@redhat.com> - 3.1.3.0-9
- Update C99 compatibility patch

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Florian Weimer <fweimer@redhat.com> - 3.1.3.0-7
- Port configure script to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 12 2020 Richard Shaw <hobbes1069@gmail.com> - 3.1.3.0-1
- Update to 3.1.3.0.

* Fri Aug 07 2020 Richard Shaw <hobbes1069@gmail.com> - 3.1.2.2-1
- Upgrade to 3.1.2.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Richard Shaw <hobbes1069@gmail.com> - 3.1.2.0-1
- Update to 3.1.2.0.

* Tue Nov 27 2018 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.13-1
- Update to 3.0.9.13.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.12-1
- Update to 3.0.9.12.

* Sun Dec 17 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.11-1
- Update to latest upstream release, 3.0.9.11.

* Mon Dec  4 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.9-1
- Update to latest upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.8-1
- Update to latest upstream release.

* Sun May 28 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.7-1
- Update to latest upstream release.

* Sat Mar 25 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.6-1
- Update to latest upstream release.

* Sat Mar 18 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.5-1
- Several spec file updates.

* Mon Mar 13 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0.9.5-1
- Initial packaging.
