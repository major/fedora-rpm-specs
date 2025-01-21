#%%global _hardened_build 1

Name:           slock
Version:        1.5
Release:        6%{?dist}
Summary:        Simple X display locker
License:        MIT
URL:            http://tools.suckless.org/%{name}
Source0:        http://dl.suckless.org/tools/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.4-libxcrypt.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  xorg-x11-proto-devel

%description
This is the simplest X screen locker we are aware of.  It is stable and
quite a lot people in this community are using it every day when they
are out with friends or fetching some food from the local pub.

%prep
%setup -q
%patch -P0 -p1
sed -e 's/^CFLAGS =/CFLAGS +=/g' -e 's/^LDFLAGS = -s/LDFLAGS +=/g' -i config.mk
sed -e 's/explicit_bzero\.c//' -i config.mk && rm -f explicit_bzero.c
sed -e 's/^\t@/\t/' -i Makefile
sed -e 's/nogroup/nobody/' config.def.h > config.h

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%license LICENSE
%doc README
%attr(4755, root, root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
# There is no freedesktop.org .desktop file because slock is basically a helper
# binary for light windowmanagers, and it shouldn't appear in applications menu

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Petr Šabata <contyk@redhat.com> - 1.5-1
- 1.5 bump
- SPDX migration

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.4-10
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Petr Šabata <contyk@redhat.com> - 1.4-8
- Fixing a segfault crash (rhbz#1563587)
- Use glibc's explicit_bzero() (rhbz#1422436)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.4-6
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Petr Šabata <contyk@redhat.com> - 1.4-2
- Reference nobody rather than nogroup which doesn't exist on Fedora

* Mon Nov 21 2016 Petr Šabata <contyk@redhat.com> - 1.4-1
- 1.4 bump

* Wed Aug 31 2016 Petr Pisar <ppisar@redhat.com> - 1.3-2
- Fix CVE-2016-6866 (segmentation fault on crypt() failure) (bug #1368370)

* Mon Feb 15 2016 Petr Šabata <contyk@redhat.com> - 1.3-1
- 1.3 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Petr Šabata <contyk@redhat.com> - 1.2-3
- Correct the dep list

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Petr Šabata <contyk@redhat.com> - 1.2-1
- 1.2 bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Petr Šabata <contyk@redhat.com> - 1.1-5
- Use %%attr to set setuid properly

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Petr Šabata <contyk@redhat.com> - 1.1-3
- Use a different approach to config patching (#965482)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Petr Šabata <contyk@redhat.com> - 1.1-1
- 1.1 bump; this means just patches cleanup

* Fri Aug 03 2012 Petr Šabata <contyk@redhat.com> - 1.0-4
- Prevent multiple instances of slock (859881ad3471)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Petr Šabata <contyk@redhat.com> - 1.0-2
- Make hardened builds; this is done in the config patch
- Apply 0eade055cef0 (dualcolor patch) and patch it to use Fedora light blue

* Mon Feb 13 2012 Petr Šabata <contyk@redhat.com> - 1.0-1
- 1.0 bump
- Update to new upstream description
- Drop defattr

* Mon Jan 23 2012 Petr Šabata <contyk@redhat.com> - 0.9-11
- Add a dummy error handler to prevent X from terminating slock (079717422185)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Petr Sabata <psabata@redhat.com> - 0.9-9
- Include upstream bugfixes for last three years; this includes better
  multiheaded and DPMS support, as well as check for password availability

* Tue Mar 01 2011 Petr Sabata <psabata@redhat.com> - 0.9-8
- Spec cleanup -- buildroot garbage removed, URL and Source corrected

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 27 2009 Pavel "Stalwart" Shevchuk <stlwrt@gmail.com> - 0.9-5
- Added comment about unneeded .desktop file

* Mon Mar 23 2009 Pavel "Stalwart" Shevchuk <stlwrt@gmail.com> - 0.9-4
- Replaced sed expressions with a patch

* Sun Mar 15 2009 Pavel "Stalwart" Shevchuk <stlwrt@gmail.com> - 0.9-3
- Fixed debuginfo generation

* Sun Mar 08 2009 Pavel "Stalwart" Shevchuk <stlwrt@gmail.com> - 0.9-2
- Set fedora generic compiler flags

* Fri Feb 27 2009 Pavel "Stalwart" Shevchuk <stlwrt@gmail.com> - 0.9-1
- Initial specfile for slock
