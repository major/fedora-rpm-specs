%global _hardened_build 1
%global __provides_exclude ^sstp-pppd-plugin\\.so$
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo bad)
%global commonname sstpc

Name:           sstp-client
Version:        1.0.18
Release:        9%{?dist}
Summary:        Secure Socket Tunneling Protocol(SSTP) Client
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            https://gitlab.com/eivnaes/sstp-client
Source0:        https://gitlab.com/eivnaes/%{name}/-/releases/%{version}/downloads/dist-gzip/%{name}-%{version}.tar.gz
Patch0:         0001-pppd-plugin-workaround-broken-pppd.h-header-for-memc.patch
Patch1:         0001-Adding-support-for-compiling-against-pppd-version-2..patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  ppp
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel >= 2.5.0
# ppp 2.5.0 patches require autoreconf, drop this when a new version
# is released and those patches are dropped
BuildRequires:  autoconf automake libtool
Requires(pre):  shadow-utils
# PPP bumps location of the libraries with every new release.
Requires:       ppp = %{ppp_version}

Recommends:     (NetworkManager-sstp if NetworkManager)
Recommends:     (NetworkManager-sstp-gnome if (NetworkManager-sstp and gnome-shell))

%description
This is a client for the Secure Socket Tunneling Protocol (SSTP). It can be 
used to establish a SSTP connection to a Windows 2008 Server.

Features:
* Establish a SSTP connection to a remote Windows 2k8 server.
* Async PPP support (most distributions provide this).
* Similar command line handling as pptp-client for easy integration.
* IPv6 support
* Basic HTTP Proxy support
* Certficate handling and verification
* SSTP plugin integration with NetworkManager v0.9 (available as separate package)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ppp-devel%{?_isa} = %{ppp_version}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
# for ppp 2.5.0 patches
autoreconf -fi
%configure --disable-static                                          \
           --disable-silent-rules                                    \
           --with-libevent=2                                         \
           --with-pppd-plugin-dir="%{_libdir}/pppd/%{ppp_version}"   \
           --with-runtime-dir="%{_localstatedir}/run/%{commonname}"  \
           --enable-user=yes                                         \
           --enable-group=yes
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

# Use %%doc to handle documentation.
rm -frv %{buildroot}%{_docdir}

find %{buildroot} -name '*.la' -delete -print

%check
make check

%pre
getent group %{commonname} >/dev/null || groupadd -r %{commonname}
getent passwd %{commonname} >/dev/null || \
    useradd -r -g %{commonname} \
    -d %{_localstatedir}/run/%{commonname} \
    -s /sbin/nologin \
    -c "Secure Socket Tunneling Protocol(SSTP) Client" %{commonname}
exit 0

%ldconfig_post

%postun
%{?ldconfig}
rm -rf %{_localstatedir}/run/%{commonname}

%files
%doc AUTHORS README ChangeLog TODO USING DEVELOPERS *.example
%license COPYING
%{_sbindir}/sstpc
%{_libdir}/libsstp_api-0.so
%{_libdir}/pppd/%{ppp_version}/sstp-pppd-plugin.so
%{_mandir}/man8/sstpc.8*

%files devel
%doc DEVELOPERS
%{_includedir}/sstp-client/
%{_libdir}/libsstp_api.so
%{_libdir}/pkgconfig/sstp-client-1.0.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Adam Williamson <awilliam@redhat.com> - 1.0.18-8
- Rebuild for ppp 2.5.1

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.18-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 18 2023 Adam Williamson <awilliam@redhat.com> - 1.0.18-3
- Rebuild for new ppp

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 07 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.18-1
- Update to 1.0.18 (#2125003)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 23 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.17-2
- Conditionally recommend NetworkManager-sstp and NetworkManager-sstp-gnome

* Wed Apr 06 2022 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.17-1
- Update to 1.0.17
- Switch URL and Source to new page on GitLab.com

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.15-21
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 13 2021 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.15-1
- Update to 1.0.15

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  8 12:47:45 CET 2021 Tomas Hrcka <thrcka@redhat.com> - 1.0.11-18
- rebuilt with new version of ppp

* Tue Sep 29 20:45:27 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.11-17
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.11-15
- Rebuild for new ppp

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Kevin Fenzi <kevin@scrye.com> - 1.0.11-10
- Rebuild for new libevent

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.0.11-8
- Rebuilt for new ppp
- Drop the superfluous dependency on a particular ppp release

* Tue Aug 22 2017 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.11-7
- Rebuild against (another) new ppp package version

* Fri Aug 18 2017 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.11-6
- Rebuild against new ppp package version - bug 1482840

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Tomas Hozza <thozza@redhat.com> - 1.0.11-3
- Rebuild against new ppp package version

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 1.0.11-2
- Rebuilt for new ppp

* Wed Dec 14 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.11-1
- Update to 1.0.11 which is compatible with OpenSSL 1.1.0c

* Wed Dec 14 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.10-6
- Fix ldconfig call in postun - #1404802

* Thu Jul 21 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.10-5
- Workaround for problem with Rpath

* Fri Feb 19 2016 Tomas Hozza <thozza@redhat.com> - 1.0.10-4
- Rebuild against new ppp package version

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Christopher Meng <i@cicku.me> - 1.0.10-2
- Correct ppp dependency.

* Sat Jun 20 2015 Christopher Meng <rpm@cicku.me> - 1.0.10-1
- Update to 1.0.10

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Christopher Meng <rpm@cicku.me> - 1.0.9-6
- Rebuild against new ppp.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 01 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-4
- Fix library issue.

* Fri Jul 26 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-3
- Filter out the private library.

* Tue Jul 23 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-2
- Remove Rpath.

* Sun Feb 03 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-1
- Initial Package.
