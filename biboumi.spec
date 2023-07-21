Name: biboumi
Version: 9.0
Release: 4%{?dist}
Summary: An XMPP gateway that connects to IRC servers

License: zlib
URL: https://lab.louiz.org/louiz/biboumi
Source0: %{url}/-/archive/%{version}/%{name}-%{version}.tar.xz
Patch0: Don-t-download-catch-during-build.patch

BuildRequires: gcc-c++
BuildRequires: cmake >= 3.0
BuildRequires: catch-devel
BuildRequires: libuuid-devel
BuildRequires: expat-devel
BuildRequires: libidn-devel
BuildRequires: systemd-devel
BuildRequires: botan2-devel
BuildRequires: sqlite-devel
BuildRequires: udns-devel
BuildRequires: libpq-devel
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: systemd-rpm-macros
%{?systemd_ordering}

%description
Biboumi is an XMPP gateway that connects to IRC servers and translates
between the two protocols. It can be used to access IRC channels using any
XMPP client as if these channels were XMPP MUCs.


%prep
%autosetup


%build
%cmake \
    -DCMAKE_BUILD_TYPE=release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DPOLLER=EPOLL \
    -DWITH_BOTAN=1 \
    -DWITH_SYSTEMD=1 \
    -DWITH_LIBIDN=1 \
    -DWITH_SQLITE3=1 \
    -DWITH_POSTGRESQL=1
%cmake_build

%cmake_build --target doc

%install
%cmake_install

%check
%cmake_build --target test_suite

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license COPYING
%doc README.rst doc/*.rst
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_sysconfdir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%{_bindir}/%{name}


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 11 2022 Michael Scherer <misc@fedoraproject.org> - 9.0-1
- Update to 9.0
- unretire and rebuild for rawhide
- add various changes proposed by Petr Menšík on bz#2025155

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 8.5-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 8.5-6
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Florent Le Coz <louiz@louiz.org> - 8.5-3
- Use cmake_build/install, see https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds#Migration

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Jeremy Cline <jcline@redhat.com> - 8.5-1
- Update to v8.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 2019 Jeremy Cline <jcline@redhat.com> - 8.3-2
- Add systemd scriptlets
- Own the /etc/biboumi directory

* Sun Apr 14 2019 Jeremy Cline <jeremy@jcline.org> - 8.3-1
- Initial package
