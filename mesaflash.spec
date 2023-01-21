Name:            mesaflash
Version:         3.4.0

%global forgeurl https://github.com/micges/%{name}
%global date     20200608
%global commit   946725c83c1cdef5b75e63b7aadcb20e1bf19eca

%forgemeta

Release:         0.9%{?dist}
Summary:         Configuration and diagnostic tool for Mesa Electronics boards
License:         GPLv2+
Url:             %{forgeurl}
Source0:         %{forgesource}

BuildRequires: make
BuildRequires:   /usr/bin/git
BuildRequires:   gcc
BuildRequires:   pkgconfig(libpci)


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
