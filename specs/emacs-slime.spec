%global pkg slime

Name:            emacs-%{pkg}
Epoch:           2
Version:         2.28
Release:         6%{?dist}
Summary:         The superior lisp interaction mode for emacs        

#Public domain: Mentioned in README file
#LLGPL: Mentioned in swank-ccl.lisp
#GPLv2+: slime.el,slime-autoloads.el
#GPLv3+: Many files in contrib are GPLv3+
License:         LicenseRef-Fedora-Public-Domain AND GPL-3.0-or-later AND GPL-2.0-or-later AND LLGPL
URL:             http://common-lisp.net/project/slime/
Source0:         https://github.com/slime/slime/archive/v%{version}.tar.gz#/%{pkg}-%{version}.tar.gz

BuildRequires:   emacs texinfo common-lisp-controller
# for testing
BuildRequires:   sbcl
BuildRequires: make

Requires:        emacs(bin) >= %{_emacs_version} common-lisp-controller

Requires(post):  common-lisp-controller
Requires(preun): common-lisp-controller

Provides:        %{name}-el = %{epoch}:%{version}-%{release}
Obsoletes:       %{name}-el < 1:2.19-5

BuildArch:      noarch
# taken from sbcl.spec since we use it for testing
ExclusiveArch:  %{arm} %{ix86} x86_64 ppc sparcv9 aarch64

%description
SLIME is a Emacs mode for common Lisp development.

%prep
%autosetup -n %{pkg}-%{version} -p1

%build
#{_emacs_bytecompile} *.el
make
cd doc/
make slime.info

%install
install -pm 755 -d %{buildroot}%{_emacs_sitestartdir}
install -pm 644 *.el  %{buildroot}%{_emacs_sitestartdir}

install -pm 755 -d %{buildroot}%{_infodir}
install -pm 644 doc/%{pkg}.info %{buildroot}%{_infodir}/

install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/contrib
install -pm 755 -d %{buildroot}%{_emacs_sitelispdir}/%{pkg}/lib
install -pm 644 *.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 644 lib/*.el* %{buildroot}%{_emacs_sitelispdir}/%{pkg}/lib/


install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/lib
install -pm 755 -d %{buildroot}%{_datadir}/common-lisp/source/slime/swank
install -pm 644 *.lisp %{buildroot}%{_datadir}/common-lisp/source/slime
install -pm 644 contrib/*.lisp %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 contrib/*.el %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 contrib/README.md %{buildroot}%{_datadir}/common-lisp/source/slime/contrib
install -pm 644 lib/*.el %{buildroot}%{_datadir}/common-lisp/source/slime/lib
install -pm 644 swank/*.lisp %{buildroot}%{_datadir}/common-lisp/source/slime/swank
install -pm 644 *.asd %{buildroot}%{_datadir}/common-lisp/source/slime

mv contrib/README.md contrib/contrib-README.md

%check
make check

%post
/usr/sbin/register-common-lisp-source swank

%preun
/usr/sbin/unregister-common-lisp-source swank 

%files
%doc NEWS PROBLEMS README.md doc/slime-small.pdf doc/slime-refcard.pdf contrib/contrib-README.md
%doc CONTRIBUTING.md

%dir %{_emacs_sitestartdir}
%{_emacs_sitestartdir}/*.el

%dir %{_emacs_sitelispdir}/%{pkg}
%dir %{_emacs_sitelispdir}/%{pkg}/contrib
%dir %{_emacs_sitelispdir}/%{pkg}/lib
%{_emacs_sitelispdir}/%{pkg}/*.el
%{_emacs_sitelispdir}/%{pkg}/*.elc
%{_emacs_sitelispdir}/%{pkg}/lib/*.el
%{_emacs_sitelispdir}/%{pkg}/lib/*.elc

%dir %{_datadir}/common-lisp/source/slime
%dir %{_datadir}/common-lisp/source/slime/contrib
%dir %{_datadir}/common-lisp/source/slime/lib
%{_datadir}/common-lisp/source/slime/*.lisp
%{_datadir}/common-lisp/source/slime/contrib/*.lisp
%{_datadir}/common-lisp/source/slime/contrib/*.el
%{_datadir}/common-lisp/source/slime/lib/*.el
%{_datadir}/common-lisp/source/slime/swank/*.lisp
%{_datadir}/common-lisp/source/slime/contrib/README.md
%{_datadir}/common-lisp/source/slime/*.asd
%{_infodir}/%{pkg}.info.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Filipe Rosset <rosset.filipe@gmail.com> - 2:2.28-1
- Update to 2.28, fixes FTBFS rhbz#2164770

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 03 2022 Bhavin Gandhi <bhavin192@fedoraproject.org> - 2:2.27-1
- Update to 2.27, fixes rhbz#2113203 rhbz#1908571

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2:2.26-1
- Update to 2.26

* Mon Aug 17 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2:2.25-3
- Reenable tests but gate to architectures with sbcl

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2:2.25-1
- Update to 2.25
- Disable tests on Koji since not all builders have sbcl

* Tue Apr 28 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 2:2.24-1
- Update to 2.24
- Remove obsolete requirements on info

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Benjamin Kreuter <ben.kreuter@gmail.com> - 1:2.23-1
- Updated to v2.23

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1:2.19-7
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Tim Landscheidt <tim@tim-landscheidt.de> - 1:2.19-5
- Obsolete -el subpackage (#1234534)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Benjamin Kreuter <ben.kreuter@gmail.com> - 1:2.19-3
- Patched to fix failing tests

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 24 2017 Benjamin Kreuter <ben.kreuter@gmail.com> - 1:2.19-1
Updated to v2.19:
- Removed old patch
- Added new patches to fix test failures
- Updated sources to use new SHA512 hash format

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Benjamin Kreuter <ben.kreuter@gmail.com> - 1:2.12-4
- Fixed spec file to install swank.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 19 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1:2.12-2
- Add Epoch to subpackage's dependency

* Mon Feb 16 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1:2.12-1
- Update to latest stable release
- Spec clean-ups

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.10.20120525cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.9.20120525cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.8.20120525cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 3.0-0.7.20120525cvs
- Hardcode location of slime-backend
- Renamed patches
- Removed known_implementations.patch. Otherwise inferior-lisp-program variable is not used by slime.

* Mon Jul 23 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 3.0-0.6.20120525cvs
- All .el files go into -el package except for those under contrib. They go into common-lisp/source/slime
- Copy readme and changelog into contrib folder. Gives an idea of how to load the definitions into emacs.
- Rename readme and changelog under contrib and put them into doc folder as well.

* Mon Jul 23 2012 Lakshmi Narasimhan T V <lakshminaras2002@gmail.com> - 3.0-0.5.20120525cvs
- Apply patches to fix slime load error.
- Copy contrib directory in both base and el packages.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.4.20101113cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.3.20101113cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.2.20101113cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 14 2010 Arun SAG <sagarun at gmail dot com> - 3.0-0.1.20101113cvs
- Fixed the version information
- Fixed the license information
- Removed the buildroot tag as it is obsolete

* Sat Sep 11 2010 Arun SAG <sagarun at gmail dot com> - 1.2-1
- Initial release
