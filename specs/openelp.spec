Name:           openelp
Version:        0.9.3
Release:        4%{?dist}
Summary:        Open Source EchoLink Proxy

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/cottsay/%{name}
Source0:        https://github.com/cottsay/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  systemd
Requires(pre):  shadow-utils
Requires(post): firewalld-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
OpenELP is an open source EchoLink proxy for Linux and Windows. It aims to be
efficient and maintain a small footprint, while still implementing all of the
features present in the official EchoLink proxy.

OpenELP also has the ability to bind to multiple network interfaces which are
routed to unique external IP addresses, and therefore is capable of accepting
connections from multiple clients simultaneously.


%package devel
Summary:        Development files for OpenELP
Requires:       %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains headers and other development files for building software
which utilizes OpenELP, and Open Source EchoLink Proxy.


%prep
%autosetup -p1

# Remove bundled md5, use OpenSSL instead
rm src/md5.c


%build
%cmake3 \
  -DOPENELP_USE_OPENSSL:BOOL=ON \
  %{nil}

%cmake3_build -- all doc


%install
%cmake3_install

# Run the service under a specific user
sed -i '/^\[Service\]$/a User=openelp' %{buildroot}%{_unitdir}/%{name}.service

# Extract the command line options to sysconfig
install -d %{buildroot}%{_sysconfdir}/sysconfig
grep ^ExecStart= %{buildroot}%{_unitdir}/%{name}.service | \
  sed 's|.*openelpd *\(.*\) %{_sysconfdir}/ELProxy.conf|\1|' | \
  sed 's|\(.*\)|# Options for openelpd\nOPTIONS="\1"|' > %{buildroot}%{_sysconfdir}/sysconfig/openelpd
sed -i '/^\[Service\]$/a EnvironmentFile=-%{_sysconfdir}/sysconfig/openelpd' %{buildroot}%{_unitdir}/%{name}.service
sed -i 's|\(ExecStart=.*openelpd\).*|\1 \$OPTIONS %{_sysconfdir}/ELProxy.conf|' %{buildroot}%{_unitdir}/%{name}.service

# Manually install the firewalld service
install -m0644 -p -D doc/%{name}.xml %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml


%check
%ctest3


%pre
getent group openelp >/dev/null || groupadd -r openelp
getent passwd openelp >/dev/null || \
    useradd -r -g openelp -d / -s /sbin/nologin \
    -c "EchoLink Proxy" openelp

%post
%{?ldconfig}
%firewalld_reload
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%{?ldconfig}
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%doc AUTHORS README.md TODO.md
%{_bindir}/%{name}d
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/openelpd.1.*
%{_prefix}/lib/firewalld/services/%{name}.xml
%attr(0640, openelp, root) %config(noreplace) %{_sysconfdir}/ELProxy.conf
%config(noreplace) %{_sysconfdir}/sysconfig/openelpd
%{_unitdir}/%{name}.service

%files devel
%doc %{?__cmake3_builddir}%{!?__cmake3_builddir:%{__cmake_builddir}}/doc/html
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.3-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 17 2024 Scott K Logan <logans@cottsay.net> - 0.9.3-1
- Update to 0.9.3

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.9.2-4
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.2-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sun Feb 07 2021 Scott K Logan <logans@cottsay.net> - 0.9.2-1
- Update to 0.9.2 (rhbz#1925917)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Scott K Logan <logans@cottsay.net> - 0.8.0-5
- Resolve build issues due to CMake out-of-source build changes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Scott K Logan <logans@cottsay.net> - 0.8.0-2
- Use macros for ldconfig and firewalld scriptlets
- Specifically remove bundled md5 implementation

* Thu Jun 18 2020 Scott K Logan <logans@cottsay.net> - 0.8.0-1
- Update to 0.8.0
- Add firewalld service
- Adjust ELProxy.conf permissions because it contains a password

* Sun Jun 07 2020 Scott K Logan <logans@cottsay.net> - 0.7.2-1
- Initial package (rhbz#1844794)
