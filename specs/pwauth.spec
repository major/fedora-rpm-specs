%global _hardened_build 1

Name:           pwauth
Version:        2.3.10
Release:        33%{?dist}
Summary:        External plugin for mod_authnz_external authenticator

# Automatically converted from old format: BSD - review is highly recommended.
License:        BSD-3-Clause
URL:            https://github.com/phokz/pwauth/
Source0:        https://github.com/phokz/pwauth/archive/%{name}-%{version}.tar.gz
Source1:        pwauth.pam
Patch1:         pwauth-make.patch
Patch2:         pwauth-strchr.patch
Patch3:         pwauth-cleanup.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pam-devel

Requires:       httpd

%description
Pwauth is an authenticator designed to be used with mod_auth_external
or mod_authnz_external and the Apache HTTP daemon to support reasonably
secure web authentication out of the system password database on most
versions of Unix.


%prep
%setup -q

%patch -P1 -p1 -b .make
%patch -P2 -p1 -b .strchr
%patch -P3 -p1 -b .cleanup

%build
export CFLAGS="${RPM_OPT_FLAGS}"
export LDFLAGS="${RPM_LD_FLAGS}"

%make_build CFLAGS="${CFLAGS} -Wno-comment" LDFLAGS="${LDFLAGS}"


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/pam.d

install -p -m 4750 -t %{buildroot}%{_bindir} pwauth
install -p -m 0750 -t %{buildroot}%{_bindir} unixgroup
install -p -T %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/pwauth


%files
%attr(4750,-,apache) %{_bindir}/pwauth
%attr(0750,-,apache) %{_bindir}/unixgroup
%attr(644,-,-) %{_sysconfdir}/pam.d/pwauth
%doc CHANGES INSTALL README


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.10-32
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Philip Prindeville <philipp@fedoraproject.org> - 2.3.10-18
- Update spec to reflect rehoming of project

* Mon Jul 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.3.10-17
- BR: gcc (#1605529)
- use %%make_build

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.3.10-11
- Requires: httpd (#1319087)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-5
- Fix for bz#965461
- Get rid of some of the more worrisome compiler warnings.
- Use patch instead of sed to modify Makefile.

* Fri Mar 22 2013 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-4
- Fix for bz#924881

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-1
- Initial checkin after Fedora packaging review.

* Tue Apr 17 2012 Philip Prindeville <philipp@fedoraproject.org> 2.3.10-0
- Initial RPM packaging.
