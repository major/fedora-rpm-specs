%global major 3
%global minor 4
%global patchlevel 1

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# Notified upstream of incorrect FSF address on 23-NOV-2013.

Name:           d52
URL:            http://www.brouhaha.com/~eric/software/d52/
Version:        %{major}.%{minor}.%{patchlevel}
Release:        27%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Summary:        Disassemblers for 8051, 8048, and Z80 families
Source:         http://www.brouhaha.com/~eric/software/d52/%{name}v%{major}%{minor}%{patchlevel}.zip
Patch0:         d52v341-nostrip.patch
Patch1:         d52v341-format-security.patch
BuildRequires:  gcc
BuildRequires:  dos2unix
BuildRequires: make

%description
D52 is collection of disassemblers for the 8051, 8048, and Z80
families of microcontrollers and microprocessors.

%prep
%setup -q -n d52v%{major}%{minor}%{patchlevel}

for f in Makefile README *.{h,c,ctl,html} cyclefiles/*.{a51,cyc,ctl,d52,HEX,LST,rtf}
do
    dos2unix -k $f
done

# Fedora-specific patch to avoid stripping the executables in the build
# process, as that interferes with creation of a debuginfo RPM.
%patch -P0 -p1 -b .nostrip
%patch -P1 -p1 -b .format-security

%build
make %{_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 d52 %{buildroot}%{_bindir}
install -p -m0755 d48 %{buildroot}%{_bindir}
install -p -m0755 dz80 %{buildroot}%{_bindir}

install -d -m0755 %{buildroot}%{_datadir}/%{name}/cyclefiles
install -p -m0644 cyclefiles/*.cyc %{buildroot}%{_datadir}/%{name}/cyclefiles

install -d -m0755 %{buildroot}%{_datadir}/%{name}/examples
install -p -m0644 cyclefiles/*.{a51,d52,bin,ctl,HEX,LST,z80} %{buildroot}%{_datadir}/%{name}/examples

%files
%{_bindir}/d52
%{_bindir}/d48
%{_bindir}/dz80
%{_datadir}/%{name}
%doc COPYING README d52manual.html dz80-d48addendum.html
%doc cyclefiles/cycle_counting.{doc,htm,rtf}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.4.1-26
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 3.4.1-4
- Fix FTBFS with -Werror=format-security (#1106116)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 15 2013 Eric Smith <eric@brouhaha.com> 3.4.1-2
- Add comment for patch0.

* Sat Nov 23 2013 Eric Smith <eric@brouhaha.com> 3.4.1-1
- Initial version.
