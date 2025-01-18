Name:           cpdup
Version:        1.18
Release:        20%{?dist}
Summary:        Filesystem mirroring utility

%if 0%{?el5}
%endif
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://apollo.backplane.com/FreeSrc/
Source0:        http://apollo.backplane.com/FreeSrc/cpdup-%{version}.tgz
Source1:        Makefile.linux
Patch0:         cpdup-c99.patch

BuildRequires:  gcc
BuildRequires: make

%description
The cpdup utility makes an exact mirror copy of the source in the
destination, creating and deleting files and directories as necessary.
UTimes, hardlinks, softlinks, devices, permissions, and flags are
mirrored.  By default, cpdup asks for confirmation if any file or
directory needs to be removed from the destination and does not copy
files which it believes to have already been synchronized (by
observing that the source and destination file’s size and mtimes
match).  cpdup does not cross mount points in either the source or the
destination.  As a safety measure, cpdup refuses to replace a
destination directory with a file.


%prep
%autosetup -p1 -n %{name}
# we don't want this to get compiled
mv md5.c{,.off}
# make scripts non-executable for cleanliness
chmod -x scripts/*



%build
make %{?_smp_mflags} CFLAGS="${RPM_OPT_FLAGS}" -f %{SOURCE1}


%install
make install DESTDIR=$RPM_BUILD_ROOT -f %{SOURCE1}


%files
%doc BACKUPS PORTING scripts
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.18-19
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Florian Weimer <fweimer@redhat.com> - 1.18-13
- Add missing declaration of strlcpy for C99 compatibility (#2151452)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar  3 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.18-1
- Update to 1.18

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  2 2010 Michel Salim <salimma@fedoraproject.org> - 1.17-1
- Update to 1.17

* Sat Aug 22 2009 Michel Salim <salimma@fedoraproject.org> - 1.14-1
- Update to 1.14

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 11 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11-2
- Fix build problems with GLIBC on 64-bit archs

* Thu Jun  5 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11-1
- Update to 1.11

* Thu Feb 28 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.07-1
- Initial Fedora package

