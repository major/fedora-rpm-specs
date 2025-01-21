Summary: test VT100-type terminal

%define AppPatched 20241204

Name: vttest
Version: 2.7.%{AppPatched}
Release: 7%{?dist}
License: MIT
URL: https://invisible-island.net/%{name}/
Source0: https://invisible-island.net/archives/%{name}/%{name}-%{AppPatched}.tgz
BuildRequires: gcc
BuildRequires: make

%description
Vttest is a program designed to test the functionality of a VT100
terminal (or emulator thereof).  It tests both display (escape sequence
handling) and keyboard.

The program is menu-driven and contains full on-line operating
instructions.  To run a given menu-item, you must enter its number.  You
can run all menu-items (for a given level) by entering an asterisk, i.e,
`*'.

%prep

%autosetup -p1 -n %{name}-%{AppPatched}

%build

%configure

%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
%doc CHANGES MANIFEST README
%license COPYING

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.20241204-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Thomas E. Dickey <dickey@his.com> - 2.7.20241204-1
- update to 2.7.20241204 (RHBZ #2321688)

* Thu Oct 31 2024 Thomas E. Dickey <dickey@his.com> - 2.7.20241031-1
- update to 2.7.20241031 (RHBZ #2321688)

* Sun Oct 27 2024 Thomas E. Dickey <dickey@his.com> - 2.7.20241024-1
- update to 2.7.20241024 (RHBZ #2321688)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.20240708-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Thomas E. Dickey <dickey@his.com> - 2.7.20240708-1
- update to 2.7.20240708 (RHBZ #2296534)

* Sun Feb 25 2024 Thomas E. Dickey <dickey@his.com> - 2.7.20240218-1
- update to 2.7.20240218 (RHBZ #2264796)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.20231230-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Thomas E. Dickey <dickey@his.com> - 2.7.20230201-1
- update to 2.7.20231230 (RHBZ #2240499)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.20230201-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Thomas E. Dickey <dickey@his.com> - 2.7.20230201-1
- update to 2.7.20230201 (RHBZ #2167192)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.20221229-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Thomas E. Dickey <dickey@his.com> - 2.7.20221229-1
- update to 2.7.20221229 (RHBZ #2143489)

* Tue Dec  6 2022 Florian Weimer <fweimer@redhat.com> - 2.7.20220827-2
- Fix glitch in configure script in FIONREAD detection (#2151353)

* Sun Aug 28 2022 Thomas E. Dickey <dickey@his.com> - 2.7.20220827-1
- update to 2.7.20220827 (RHBZ #2055158)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.20220215-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 17 2022 Thomas E. Dickey <dickey@his.com> - 2.7.20220215-1
- update to 2.7.20220215 (RHBZ #2055158)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.20210210-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Thomas E. Dickey <dickey@his.com> - 2.7.20210210-1
- address review-comments
- install doc, license files used in previous Fedora package
