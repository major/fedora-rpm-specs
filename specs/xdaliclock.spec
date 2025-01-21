Summary: A clock for the X Window System
Name: xdaliclock
Version: 2.43
Release: 22%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://www.jwz.org/xdaliclock/
Source0: http://www.jwz.org/xdaliclock/xdaliclock-%{version}.tar.gz
Source1: xdaliclock.desktop
Patch0: xdaliclock-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: desktop-file-utils
BuildRequires: libICE-devel, libXmu-devel, libSM-devel, xorg-x11-proto-devel
BuildRequires: libXext-devel, libXaw-devel, libXt-devel
BuildRequires: redhat-rpm-config

%description
XDaliClock is a large digital clock for the X Window System, with digits
that "melt" into their new shapes when the time changes. XDaliClock
supports 12 and 24 hour modes, and displays the date when you hold a mouse
button down over it. It also can be configured to do colormap cycling, and
for window transparency.

%prep
%autosetup -p1

%build
# easier than patching configure to read those files from own directory
cp /usr/lib/rpm/redhat/config.{guess,sub} .

cd X11
%configure
make %{?_smp_mflags}

%install
cd X11

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults

install -p -m 0755 xdaliclock $RPM_BUILD_ROOT%{_bindir}
install -p -m 0644 xdaliclock.man \
	$RPM_BUILD_ROOT%{_mandir}/man1/xdaliclock.1
install -p -m 0644 XDaliClock.ad \
	$RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/XDaliClock

desktop-file-install  \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	--add-category "X-Fedora" \
	--add-category "Graphics" \
	%{SOURCE1}

%files
%doc README
%{_bindir}/xdaliclock
%{_mandir}/man1/xdaliclock.1*
%{_datadir}/X11/app-defaults/XDaliClock
%{_datadir}/applications/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.43-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 2.43-16
- Port configure scripts to C99

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Adam Jackson <ajax@redhat.com> 2.43-1
- xdaliclock 2.43

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Paul Wouters <pwouters@redhat.com> - 2.42-1
- Update to 2.42 (#1124300)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Paul Wouters <pwouters@redhat.com> - 2.25-11
- Resolves rhbz#926760 Does not support aarch64 in f19 and rawhide

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.25-8
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 12 2011 Paul Wouters <paul@xelerance.com> - 2.25-5
- Build for rawhide
- Remove execute bit from man page

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 16 2008 Chris Ricker <kaboom@oobleck.net> 2.25-1
- New upstream release
- Fix desktop file installation

* Mon Sep 11 2006 Chris Ricker <kaboom@oobleck.net> 2.23-3
- Bump and rebuild

* Wed Feb 15 2006 Chris Ricker <kaboom@oobleck.net> 2.23-2
- Really update for modular X

* Wed Feb 15 2006 Chris Ricker <kaboom@oobleck.net> 2.23-1
- New release
- Update for modular X

* Mon May 09 2005 Chris Ricker <kaboom@oobleck.net> 2.20-2%{?dist}
- Add dist tag

* Sat Apr 23 2005 Chris Ricker <kaboom@oobleck.net> 2.20-1
- Initial package for Fedora Extras
