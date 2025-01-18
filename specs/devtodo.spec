Name:		devtodo
Version:	0.1.20
Summary:	Manage a prioritised list of todo items organized by directory
Release:	39%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://swapoff.org/DevTodo
Source0:	http://swapoff.org/files/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-0.1.20-buildfixes.patch
Patch1:     %{name}-aarch64.patch

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:	compat-readline5-devel
BuildRequires: make

%description
Todo is a program to display and manage a hierarchical, prioritised list of 
outstanding work, or just reminders.

The program itself is assisted by a few shell scripts that override default
builtins. Specifically, cd, pushd and popd are overridden so that when using
one of these commands to enter a directory, the todo will display any 
outstanding items in that directory.

For much more complete information please refer to the man page (devtodo(1)).


%prep
%setup -q
%patch -P0 -p1 -b .bfix
%patch -P1 -p1

%build
export CPPFLAGS="-I%{_includedir}/readline5" LDFLAGS="-L%{_libdir}/readline5"
%configure

make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
%{__install} -p -m 644 doc/scripts.sh %{buildroot}/%{_sysconfdir}/profile.d/devtodo.sh
%{__install} -p -m 644 doc/scripts.tcsh %{buildroot}/%{_sysconfdir}/profile.d/devtodo.tcsh



%files
%config(noreplace) %{_sysconfdir}/todorc
%config(noreplace) %{_sysconfdir}/profile.d/devtodo.sh
%config(noreplace) %{_sysconfdir}/profile.d/devtodo.tcsh
%{_bindir}/devtodo
%{_bindir}/todo
%{_bindir}/tda
%{_bindir}/tdr
%{_bindir}/tde
%{_bindir}/tdd
%{_bindir}/tdl
%{_mandir}/man?/*
%doc AUTHORS README COPYING NEWS QuickStart doc/todorc.example ChangeLog


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.20-38
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.1.20-24
- Rebuild with fixed binutils

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 02 2017 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.1.20-21
- Bump to rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.20-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.20-15
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.1.20-11
- Apply a patch to get it building on AArch64

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 0.1.20-8
- Applied the patch suggested by Miroslav Lichvar <mlichvar@redhat.com> to link with compat-readline5 (RHBZ #511306)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-7
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> - 0.1.20-3
- More fixes reported by reviewer

* Tue Dec 19 2008 Bernie Innocenti <bernie@codewiz.org> - 0.1.20-2
- Fix Summary and License tags as requested by reviewer

* Tue Dec 10 2008 Bernie Innocenti <bernie@codewiz.org> - 0.1.20-1
- Upstream version 0.1.20.
- Comply with Fedora packaging guidelines

* Sat Dec 14 2002 Alec Thomas <alec@korn.ch>
- Added tdl stuff

* Thu Nov  8 2001 Alec Thomas <alec@korn.ch>
- Now include example scripts for sh/tcsh and gzip man pages due to extreme bizarreness of rpm.

* Wed Jul 11 2001 Alec Thomas <alec@korn.ch>
- Removed aclocal/autoheader/autoconf/automake use.

* Mon May 14 2001 Alec Thomas <alec@korn.ch>
- Initial RPMage.
