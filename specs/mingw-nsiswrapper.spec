Name:           mingw-nsiswrapper
Version:        12
Release:        7%{?dist}
Summary:        Helper program for making NSIS Windows installers

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://fedoraproject.org/wiki/MinGW

Source0:        nsiswrapper.pl
Source1:        README
Source2:        COPYING

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-podlators


%description
NSISWrapper is a helper program for making Windows installers,
particularly when you are cross-compiling from Unix.

NSIS (a separate package) is a program for building Windows
installers.  This wrapper simply makes it easier to generate the
installer script that NSIS needs.


%package -n mingw32-nsiswrapper
Summary:        Helper program for making NSIS Windows installers
Requires:       mingw32-binutils
Requires:       mingw32-crt
Requires:       mingw32-nsis

%description -n mingw32-nsiswrapper
NSISWrapper is a helper program for making Windows installers,
particularly when you are cross-compiling from Unix.

NSIS (a separate package) is a program for building Windows
installers.  This wrapper simply makes it easier to generate the
installer script that NSIS needs.


%prep
# empty


%build
# empty


%check
perl -Tc %{SOURCE0}


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/nsiswrapper

# Install documentation (manually).
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
install -m 0644 %{SOURCE1} %{SOURCE2} \
  $RPM_BUILD_ROOT%{_docdir}/%{name}

# Build the manpage from the source.
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
pod2man -c "NSIS" -r "%{name}-%{version}" %{SOURCE0} \
  > $RPM_BUILD_ROOT%{_mandir}/man1/nsiswrapper.1


%files -n mingw32-nsiswrapper
%doc %{_docdir}/%{name}/COPYING
%doc %{_docdir}/%{name}/README
%{_bindir}/nsiswrapper
%{_mandir}/man1/nsiswrapper.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 12-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 25 2023 Richard W.M. Jones <rjones@redhat.com> - 12-1
- Use mingw*-crt to search for DLLs (RHBZ#2164360)
- Remove ancient Fedora conditional.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Richard W.M. Jones <rjones@redhat.com> - 11-1
- Pango modules are no longer required (RHBZ#1607041).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug  6 2013 Richard W.M. Jones <rjones@redhat.com> - 10-4
- Unversioned docdir in Fedora 20 (RHBZ#993912).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 10-2
- Perl 5.18 rebuild

* Sat Jul 13 2013 Richard W.M. Jones <rjones@redhat.com> - 10-1
- Generate the list of DLLs programmatically (RHBZ#856354).
- Remove 'Group' line, unnecessary for modern RPM.
- Add simple check section.

* Fri Feb 22 2013 Ivan Romanov <drizt@land.ru> - 9-6
- pod2man now is in perl-podlators (#914187)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 9-3
- Renamed the source package to mingw-nsiswrapper (#801007)

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 9-1
- Made the package compatible with the mingw-w64 toolchain
- Dropped unneeded RPM tags

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct  7 2011 Romanov Ivan <drizt@land.ru> - 8-1
- Use $PgrogramFiles as default install path (RHBZ#743002)

* Wed Sep 28 2011 Richard W.M. Jones <rjones@redhat.com> - 7-1
- Don't apply lowercase to Qt library names (thanks Ivan Romanov).

* Thu May 19 2011 Richard W.M. Jones <rjones@redhat.com> - 6-1
- Patched for new location of libgdk-pixbuf loaders (RHBZ#706219).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 21 2009 Richard W.M. Jones <rjones@redhat.com> - 5-1
- Add dnsapi.dll to list of system libraries (RHBZ#548965).

* Mon Oct 12 2009 Adam Tkac <atkac redhat com> - 4-4
- add version.dll to list of system libraries (#528467)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul  5 2009 Richard W.M. Jones <rjones@redhat.com> - 4-2
- Add runtime requires mingw32-binutils (RHBZ#509747).

* Tue Jun  9 2009 Richard W.M. Jones <rjones@redhat.com> - 4-1
- Add more system libraries to the script.

* Tue Apr 21 2009 Richard W.M. Jones <rjones@redhat.com> - 3-5
- Fix dependency problem with + in DLL name (Thomas Sailer).

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 3-3
- Rebuild for mingw32-gcc 4.4

* Thu Oct 16 2008 Richard W.M. Jones <rjones@redhat.com> - 3-2
- Initial RPM release.
