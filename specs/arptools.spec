Name:           arptools
Summary:        Collection of libnet and libpcap based ARP utilities
License:        GPL-2.0-or-later

%global git_commit_full 2cf523f6fe6760da1eb3f97963f1975f96f6f106
%global git_commit %(c="%{git_commit_full}"; echo "${c:0:7}")
%global git_date 20230218

Version:        1.0.2
Release:        26.%{git_date}git%{git_commit}%{?dist}

URL:            https://github.com/burghardt/arptools
Source0:        %{URL}/archive/%{git_commit_full}/%{name}-%{git_commit_full}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel


%description
ARP Tools is collection of libnet and libpcap based ARP utilities.
It currently contains ARP Discover (arpdiscover), an Ethernet scanner based on
ARP protocol; ARP Flood (arpflood), an ARP request flooder; and ARP Poison
(arppoison), for poisoning switches' MAC address tables.


%prep
%setup -q -n %{name}-%{git_commit_full}


%build
chmod +x autogen.sh # yes, really
NOCONFIGURE="yes" ./autogen.sh
%configure
%make_build


%install
%make_install


%files
%doc AUTHORS ChangeLog NEWS README.md TODO
%license COPYING
%{_sbindir}/arpdiscover
%{_sbindir}/arpflood
%{_sbindir}/arppoison


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-26.20230218git2cf523f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-25.20230218git2cf523f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-24.20230218git2cf523f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-23.20230218git2cf523f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-22.20230218git2cf523f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.2-21.20230218git2cf523f
- Update to latest git snapshot (2023-02-18)
- Fix installing README symlink instead of actual file

* Thu Feb 16 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.0.2-20.20230213git8be3f31
- Update to latest git snapshot (2023-02-13)
- Convert License tag to SPDX
- Add missing BuildRequires

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 30 2012 Jon Ciesla <limburgher@gmail.com> - 1.0.2-5
- libnet rebuild.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Feb 22 2009 Jakub Hrozek <jhrozek@redhat.com> 1.0.2-1
- initial packaging
