Name:		msktutil
Version:	1.2
Release:	9%{?dist}
Summary:	Program for interoperability with Active Directory 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://github.com/msktutil/msktutil
Source0:	https://github.com/msktutil/msktutil/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	openldap-devel
BuildRequires:	krb5-devel
Requires:	cyrus-sasl-gssapi

%description
Msktutil is a program for interoperability with Active Directory that can
create a computer account in Active Directory, create a system Kerberos keytab,
add and remove principals to and from that keytab, and change the computer
account's password.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%license LICENSE
%doc README ChangeLog
%{_mandir}/man1/*
%{_bindir}/%{name}
%{_sbindir}/%{name}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Michael Cronenworth <mike@cchtml.com> - 1.2-1
- Update to 1.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Michael Cronenworth <mike@cchtml.com> - 1.1-1
- Update to 1.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.0-1
- Update to 1.0
- Drop EL5 compatibility

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 17 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.5.1-5
- Use SourceForge.net URL for homepage

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.5.1-2
- Use SourceForge.net URL for Source0 instead of Google Code.

* Sun Oct 27 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.5.1-1
- Update to 0.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 01 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.5-1
- Update to 0.5 final

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.2-1
- Update to 0.4.2 final

* Mon Nov 19 2012 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.4.2-0.1
- Update to 0.4.2
- Remove CPPFLAGS and PATH_KRB5_CONFIG hacks

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4.1-1
- Update to 0.4.1
- Remove all upstreamed patches
- No need to regenerate configure with autoconf
- New upstream URL

* Sat Dec 3 2011 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4-7
- Adjust conditionals for setting CPPFLAGS and KRB5_CONFIG
- Use PATH_KRB5_CONFIG instead of KRB5_CONFIG when running configure,
  since the latter is used by the Kerberos libraries to specify an
  alternative path to krb5.conf. Thanks again Russ Allbery.

* Mon Oct 3 2011 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4-6
- Adjust regex in krb5-config patch. Thanks Russ Allbery.

* Sat Oct 1 2011 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4-5
- Use patches from upstream git, instead of my own from -4
- Patch Makefile to use $LIBS
- Patch to use krb5-config to automatically determine build flags
- Bump Fedora version to F16 for /usr/include/et
- Regenerate configure with autoconf

* Thu Jul 21 2011 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4-4
- Patch LDAP debug code to correctly report get/set operations

* Sun Jul 10 2011 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4-3
- Reformat BRs, include ChangeLog, explicitly name binary.
- Patch Makefile to be verbose.

* Tue Jul 5 2011 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4-2
- Don't package INSTALL and un-mark manpages as doc

* Tue May 10 2011 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4-1
- Initial package
