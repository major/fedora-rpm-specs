# disable the debug package since it produces nothing useful due to e3
# being written in assembly
%global debug_package	%{nil}

Name:		e3
Version:	2.82
Release:	21%{?dist}
Summary:	Text editor with key bindings similar to WordStar, Emacs, pico, nedit, or vi

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		https://sites.google.com/site/e3editor/
Source0:	https://sites.google.com/site/e3editor/Home/%{name}-%{version}.tgz

# mark the stack as non-executable and disable tiny/crippled elf on 32
# bit linux so that stack can be marked as non-executable on it too
# http://www.gentoo.org/proj/en/hardened/gnu-stack.xml
Patch0:		e3-gnu-stack.patch
BuildRequires:	nasm
BuildRequires: make
ExclusiveArch:	%{ix86} x86_64

%description
e3 is a full-screen, user-friendly text editor with an key bindings similar to
that of either WordStar, Emacs, pico, nedit, or vi.

%prep
%setup -q

# delete the included binaries
rm -rf bin

%patch -P0 -p1

%build
%ifarch x86_64
make PREFIX=%{_prefix} MANDIR=%{_mandir}/man1 EXMODE=SED 64
%else
make PREFIX=%{_prefix} MANDIR=%{_mandir}/man1 EXMODE=SED 32
%endif


%install
rm -rf %{buildroot}
# The Makefile does not have the feature to speciy a DESTDIR so we do this by
# hand
mkdir -p %{buildroot}%{_bindir}
install -m 755 e3 %{buildroot}%{_bindir}
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3ws
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3em
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3pi
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3vi
ln -sf %{_bindir}/e3 %{buildroot}%{_bindir}/e3ne

mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 e3.man %{buildroot}%{_mandir}/man1/e3.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3ws.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3em.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3pi.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3vi.1
ln -sf %{_mandir}/man1/e3.1 %{buildroot}%{_mandir}/man1/e3ne.1

%files
%doc COPYRIGHT COPYING.GPL README README.v2.7.1 ChangeLog e3.html
%{_bindir}/e3*
%{_mandir}/man1/e3*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.82-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 15 2016 Mark McKinstry <mmckinst@umich.edu> - 2.82-1
- upgrade to 2.82

* Mon Feb 29 2016 Mark McKinstry <mmckinst@umich.edu> - 2.81-1
- upgrade to 2.81

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Mark McKinstry <mmckinst@nexcess.net> - 2.8-3
- patch to mark the stack as non-executable

* Wed Dec  5 2012 Mark McKinstry <mmckinst@nexcess.net> - 2.8-2
- disable deubg package

* Tue Jan  3 2012 Mark McKinstry <mmckinst@nexcess.net> 2.8-1
- initial build
