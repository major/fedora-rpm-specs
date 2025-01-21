%global __cmake_in_source_build 1

Name:		yubico-piv-tool
Version:	2.7.1
Release:	2%{?dist}
Summary:	Tool for interacting with the PIV applet on a YubiKey

License:	BSD-2-Clause
URL:		https://developers.yubico.com/yubico-piv-tool/
Source0:	https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz
Source1:	https://developers.yubico.com/yubico-piv-tool/Releases/yubico-piv-tool-%{version}.tar.gz.sig
Source2:	gpgkey-9588EA0F.gpg

BuildRequires:  make
BuildRequires:	pcsc-lite-devel
BuildRequires:  openssl-devel
BuildRequires:  chrpath
BuildRequires:	gnupg2 gengetopt help2man
BuildRequires:	check-devel
BuildRequires:	gcc gcc-c++
BuildRequires:	cmake3
BuildRequires:	zlib-devel
Requires:		pcsc-lite-ccid

%description
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.

With it you may generate keys on the device, importing keys and certificates,
and create certificate requests, and other operations. A shared library and
a command-line tool is included.

%package devel
Summary: Tool for interacting with the PIV applet on a YubiKey
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The Yubico PIV tool is used for interacting with the
Privilege and Identification Card (PIV) applet on a YubiKey.
This package includes development files.


%prep
gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q

%build
%cmake3 .
%make_build VERBOSE=1

%check
%ctest --output-on-failure

%install
%make_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/yubico-piv-tool
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libykcs11.so.*
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libykpiv.so.*
rm -f $RPM_BUILD_ROOT%{_libdir}/libykpiv.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/libykcs11.{la,a}


%ldconfig_scriptlets


%files
%license COPYING
%{_bindir}/yubico-piv-tool
%{_libdir}/libykpiv.so.2*
%{_libdir}/libykcs11.so.2*


%doc
%{_mandir}/man1/yubico-piv-tool.1.gz

%files devel
%{_libdir}/libykpiv.so
%{_libdir}/libykcs11.so
%attr(0644,root,root) %{_libdir}/pkgconfig/ykpiv.pc
%attr(0644,root,root) %{_libdir}/pkgconfig/ykcs11.pc
%dir %{_includedir}/ykpiv
%attr(0644,root,root) %{_includedir}/ykpiv/ykpiv.h
%attr(0644,root,root) %{_includedir}/ykpiv/ykpiv-config.h


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 Jakub Jelen <jjelen@redhat.com> - 2.7.1-1
- New upstream release fixing x390x build (#2333288)

* Thu Dec 19 2024 Jakub Jelen <jjelen@redhat.com> - 2.7.0-1
- New upstream release (#2333288)

* Thu Sep 12 2024 Jakub Jelen <jjelen@redhat.com> - 2.6.1-1
- New upstream release (#2311937)

* Thu Aug 22 2024 Jakub Jelen <jjelen@redhat.com> - 2.6.0-1
- New upstream release (#2306797)

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.2-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 07 2024 Jakub Jelen <jjelen@redhat.com> - 2.5.2-1
- New upstream release (#2279499)

* Wed Feb 14 2024 Jakub Jelen <jjelen@redhat.com> - 2.5.1-1
- New upstream release (#2264044)

* Thu Feb 01 2024 Jakub Jelen <jjelen@redhat.com> - 2.5.0-1
- New upstream release supporting larger RSA keys and ED25519 and X25519 (#2262179)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Jakub Jelen <jjelen@redhat.com> - 2.4.2-1
- New upstream release related to the previous issue (#2253499)

* Wed Dec 06 2023 Jakub Jelen <jjelen@redhat.com> - 2.4.1-1
- Fix the build for i686 architecture (#2252823)

* Tue Dec 05 2023 Jakub Jelen <jjelen@redhat.com> - 2.4.0-1
- New upstream release (#2252823)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Jakub Jelen <jjelen@redhat.com> - 2.3.1-1
- New upstream release (#2167694)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 04 2022 Veronika Hanulikova <vhanulik@redhat.com> - 2.3.0-1
- New upstream release (#2059540)
- Initialize maybe-uninitialized variables
- Fix usage of pointer after free
- Build against OpenSSL 3.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Orion Poplawski <orion@nwra.com> - 2.2.1-3
- Build with OpenSSL 1.1 until upstream fixes OpenSSL 3.0 compatibility

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.2.1-2
- Rebuilt with OpenSSL 3.0.0

* Wed Sep 08 2021 Jakub Jelen <jjelen@redhat.com> - 2.2.1-1
- New upstream release (#2001834)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jakub Jelen <jjelen@redhat.com> - 2.2.0-1
- New upstream release (#1918362)

* Thu Jul 30 2020 Jakub Jelen <jjelen@redhat.com> - 2.1.1-1
- New upstream release (#1859119)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Jakub Jelen <jjelen@redhat.com> - 2.1.0-1
- New upstream release (#1855024)

* Fri Feb  7 2020 Orion Poplawski <orion@nwra.com> - 2.0.0-1
- Update to 2.0.0 (#1796170)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Jakub Jelen <jjelen@redhat.com> - 1.7.0-1
- New upstream release (#1695650)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Jakub Jelen <jjelen@redhat.com> - 1.6.2-1
- New upstream release

* Tue Aug 21 2018 Jakub Jelen <jjelen@redhat.com> - 1.6.1-1
- New upstream bugfix release

* Wed Aug 08 2018 Jakub Jelen <jjelen@redhat.com> - 1.6.0-1
- New upstream release fixing YSA-2018-03 (#1613863)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Jakub Jelen <jjelen@redhat.com> - 1.5.0-1
- New upstream release (#1543947)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.4-2
- Escape macros in %%changelog

* Fri Oct 20 2017 Jakub Jelen <jjelen@redhat.com> - 1.4.4-1
- New upstream release (#1504462)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Jakub Jelen <jjelen@redhat.com> - 1.4.3-1
- New upstream release (#1443074)

* Thu Feb 23 2017 Jakub Jelen <jjelen@redhat.com> - 1.4.2-3
- Rebuild against OpenSSL 1.0.2 (#1424566)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 06 2016 Jakub Jelen <jjelen@redhat.com> - 1.4.2-1
- New upstream release (#1370850)

* Fri Aug 12 2016 Jakub Jelen <jjelen@redhat.com> - 1.4.1-1
- New upstream release (#1366435)

* Tue May 03 2016 Jakub Jelen <jjelen@redhat.com> - 1.4.0-1
- New upstream release
- Source tarball verification

* Fri Apr 29 2016 Jakub Jelen <jjelen@redhat.com> - 1.3.1-1
- New upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Jakub Jelen <jjelen@redhat.com> 1.2.2-1
- Update to 1.2.2

* Tue Dec 08 2015 Jakub Jelen <jjelen@redhat.com> 1.2.1-1
- Update to 1.2.1 (#1289091)

* Mon Nov 16 2015 Jakub Jelen <jjelen@redhat.com> 1.1.2-1
- Update to 1.1.2 (#1281987)

* Thu Nov 12 2015 Jakub Jelen <jjelen@redhat.com> 1.1.1-1
- Update to 1.1.1 (#1280522)

* Sun Nov 08 2015 Jessica Frazelle <jess@docker.com> 1.1.0-1
- Rebase to 1.1.0

* Fri Oct 02 2015 Jakub Jelen <jjelen@redhat.com> 1.0.3-1
- Rebase to 1.0.3

* Thu Jul 16 2015 Jakub Jelen <jjelen@redhat.com> 1.0.1-1
- Rebase to 1.0.1

* Mon Jul 13 2015 Jakub Jelen <jjelen@redhat.com> 1.0.0-3
- License is GPLv3+
- owner for %%{_includedir}/ykpiv
- remove hard-coded paths from ./configure
- make check is run unconditionally
- change RPATH handling to make check pass

* Thu Jul 09 2015 Jakub Jelen <jjelen@redhat.com> 1.0.0-2
- Fixed problems for Fedora Review

* Thu Jul 09 2015 Jakub Jelen <jjelen@redhat.com> 1.0.0-1
- Initial release

