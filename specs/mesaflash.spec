Name:            mesaflash
Version:         3.4.9

%global forgeurl https://github.com/LinuxCNC/%{name}
%global tag     release/%{version}
#%%global date     20200608
#%%global commit   946725c83c1cdef5b75e63b7aadcb20e1bf19eca

%forgemeta

Release:         6%{?dist}
Summary:         Configuration and diagnostic tool for Mesa Electronics boards
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later
Url:             %{forgeurl}
Source0:         %{forgesource}

BuildRequires:   make
BuildRequires:   /usr/bin/git
BuildRequires:   gcc
BuildRequires:   pkgconfig(libpci)
BuildRequires:   pkgconfig(libmd)


%description
Configuration and diagnostic tool for Mesa Electronics
PCI(E)/ETH/EPP/USB/SPI boards.


%prep
%forgeautosetup -S git
# Remove binary files
rm -rf *.dll *.sys libpci


%build
# Set the version string
CFLAGS='%{build_cflags} -DVERSION=\"%{version}-%{release}\"'
%set_build_flags
%ifarch i386 x86_64
  export USE_STUBS=0
%else
  export USE_STUBS=1
%endif
%{make_build} OWNERSHIP=""


%install
%ifarch i386 x86_64
  export USE_STUBS=0
%else
  export USE_STUBS=1
%endif
%{make_install} OWNERSHIP="" DESTDIR="%{buildroot}%{_prefix}"


%files
# The license is in the documentation file
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4.9-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 17 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.4.9-1
- Update to 3.4.9 (#2041264)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 08 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.4.0-0.3.20200608git946725c
- Update to the lastest available version
- Drop patches upstream merged

* Wed Apr 29 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.4.0-0.2
- Update to the lastest available version
- Add patch to set VERSION from spec file

* Tue Apr 28 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.4.0-0.1
- Update to the lastest available version

* Mon Apr 20 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.3.0-0.3
- Update upstream references to the patches.

* Mon Apr 20 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.3.0-0.2
- Add a patch to compile on platforms without <sys/io.h> header.

* Fri Apr 17 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 3.3.0-0.1
- Initial RPM release.
