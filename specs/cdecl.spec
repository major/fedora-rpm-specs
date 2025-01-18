Name: cdecl
Summary: Translator for C gibberish

# The original cdecl has been released in May 1988, into the public domain.
# The fork used in this package re-licenses the code under GPLv3.
# It also includes some code taken from Gnulib, licensed under the LGPL.
#
# Check the discussion on the legal mailing list regarding suitability for Fedora:
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/QBYRCIMQDXAD2ZKUWKKYSTDB6T6GW2SO/
License: GPL-3.0-or-later AND LGPL-2.1-or-later AND LicenseRef-Fedora-PublicDomain

Version: 18.4.1
Release: 2%{?dist}

URL: https://github.com/paul-j-lucas/cdecl/
Source0: %{URL}releases/download/cdecl-%{version}/cdecl-%{version}.tar.gz

# cdecl tries a couple of different methods of getting terminal information.
# One of them involves getting the terminal path via ctermid(3) and then
# opening the file. This works in a regular user session and seems to
# work in upstream's CI environment. However, in mock & koji, the file
# is not accessible, causing the relevant test to fail.
Patch0: cterm-no-such-dev.patch

BuildRequires: diffutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses
BuildRequires: readline-devel


%description
Cdecl is a program which will turn English-like phrases such as "declare
foo as array 5 of pointer to function returning int" into C declarations
such as "int (*foo[5])()". It can also do the opposite, translating C
into the pseudo-English. And it handles typecasts, too. Plus C++.
This version also has command line editing and history.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install


%check
make -C test/ check || { cat test/test-suite.log; exit 1; }


%files
%doc AUTHORS README.md README-2.5.txt
%license COPYING
%{_bindir}/cdecl
%{_bindir}/c++decl
%{_mandir}/man1/cdecl.1*
%{_mandir}/man1/c++decl.1*

%{_datadir}/bash-completions/
# bash-completions/completions/_cdecl
%{_datadir}/zsh/
# zsh/site-functions/_cdecl


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 18.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 09 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 18.4.1-1
- Update to v18.4.1

* Tue Sep 03 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 18.4-1
- Update to v18.4

* Thu Aug 15 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 18.3-1
- Update to v18.3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 22 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 17.0.1-1
- Update to v17.0.1

* Thu Jun 13 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 17.0-1
- Update to v17.0

* Tue May 28 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.4.1-1
- Update to v16.4.1
- Drop Patch0 (wrong file install paths - fixed upstream)

* Sat May 25 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.4-1
- Update to v16.4

* Tue Apr 16 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.3-1
- Update to v16.3

* Sat Mar 02 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.2.2-1
- Update to v16.2.2

* Tue Feb 20 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.2.1-1
- Update to v16.2.1

* Tue Jan 30 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.2-1
- Update to v16.2

* Mon Jan 15 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.1-1
- Update to v16.1

* Fri Jan 05 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 16.0-1
- Update to v16.0
- Add a note regarding licensing and suitability for Fedora

* Mon Oct 02 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 15.0-1
- Update to v15.0

* Sat Sep 16 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 14.4-1
- Update to v14.4

* Thu Aug 31 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 14.3-1
- Update to v14.3
- Extract sources into two copies to further separate the "install" and "test" builds

* Fri Jul 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 14.2-1
- Build from a different fork - jump to v14.2

* Thu Jul 20 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2.5-1
- Initial packaging
