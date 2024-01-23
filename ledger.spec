%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:             ledger
Version:          3.2.1
Release:          15%{?dist}
Summary:          A powerful command-line double-entry accounting system
License:          BSD
URL:              http://ledger-cli.org/
Source0:          https://github.com/ledger/ledger/archive/v%{version}.tar.gz
# https://github.com/ledger/ledger/pull/2036
Patch0:           ledger-boost176.patch

BuildRequires:    boost-devel
BuildRequires:    cmake
BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    gettext-devel
BuildRequires:    gmp-devel
BuildRequires:    libedit-devel
BuildRequires:    mpfr-devel
BuildRequires:    utf8cpp-devel

# For building documentation.
BuildRequires:    doxygen
BuildRequires:    graphviz
BuildRequires:    man2html
BuildRequires:    texinfo
BuildRequires:    texlive-cm-super
BuildRequires:    texlive-ec
BuildRequires:    texlive-eurosym
BuildRequires:    texinfo-tex

# Obsolete the python2-ledger subpackage rhbz#1629493
Obsoletes:        python2-ledger < 3.1.1-22

%description
Ledger is a powerful, double-entry accounting system that is accessed
from the UNIX command-line. This may put off some users — as there is
no flashy UI — but for those who want unparalleled reporting access to
their data, there really is no alternative.

%package devel
Summary: Libraries and header files for %{name} development
Requires: %{name} = %{version}-%{release}
%description devel
Libraries and header files for %{name} development.

%prep
%autosetup -n %{name}-%{version} -p 1
# Avoid texinfo errors on EL7.
%if 0%{?rhel} == 7
sed -i -e 's#FIXME:UNDOCUMENTED#FIXMEUNDOCUMENTED#g' doc/ledger3.texi
%endif
rm -r lib/utfcpp


%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_SKIP_RPATH:BOOL=ON \
       -DUSE_PYTHON:BOOL=OFF \
       -DUSE_DOXYGEN:BOOL=ON \
       -DBUILD_WEB_DOCS:BOOL=ON

%cmake_build
%cmake_build -t doc

%install
%cmake_install

# Bash completion
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -p -m0644 contrib/ledger-completion.bash \
    %{buildroot}%{_sysconfdir}/bash_completion.d/ledger

# Install documentation manually to a convenient directory layout
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_infodir}/*

# Info files
cp -p %{__cmake_builddir}/doc/ledger3.info* %{buildroot}%{_infodir}

# Contrib scripts
mkdir -p %{buildroot}%{_pkgdocdir}/contrib
for i in bal bal-huquq compilation-ledger.el entry getquote.pl getquote-uk.py ledger-du README repl.sh report tc ti to trend; do
    install -p -m0644 contrib/${i} %{buildroot}%{_pkgdocdir}/contrib/${i}
done

# Input samples
mkdir -p %{buildroot}%{_pkgdocdir}/samples
for i in demo.ledger divzero.dat drewr3.dat drewr.dat sample.dat standard.dat transfer.dat wow.dat; do
    install -p -m0644 test/input/${i} %{buildroot}%{_pkgdocdir}/samples/${i}
done

# Tests are disabled for the time being since they seem to require Python 2
#%%check
# Tests all fail when removing rpath.
#LD_LIBRARY_PATH=$PWD %%ctest

%files
%doc README.md doc/GLOSSARY.md doc/NEWS.md
%doc %{__cmake_builddir}/doc/ledger3.html
%doc %{__cmake_builddir}/doc/ledger3.pdf
# https://bugzilla.redhat.com/show_bug.cgi?id=728959
# These must be explicitly listed.
%doc %{_pkgdocdir}/contrib
%doc %{_pkgdocdir}/samples
%{_bindir}/ledger
%{_infodir}/ledger3.info*
%{_libdir}/libledger.so.3
%{_mandir}/man1/ledger.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/ledger
%license LICENSE.md

%files devel
%{_includedir}/ledger
%{_libdir}/libledger.so


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 3.2.1-14
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 3.2.1-12
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 3.2.1-9
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 09 2021 Jonathan Wakely <jwakely@redhat.com> - 3.2.1-7
- Patched and rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 3.2.1-4
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 3.2.1-2
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 3.2.1-1
- Update to newest stable upstream version
- Fix build on Rawhide

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-6.20191030git2ca3d69
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-5.20191030git2ca3d69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 3.1.3-4.20191030git2ca3d69
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3.20191030git2ca3d69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 3.1.3-2.20191030git2ca3d69
- Rebuild for ICU 65

* Wed Oct 30 2019 Jani Juhani Sinervo <jani@sinervo.fi> - 3.1.3-1.20191030git2ca3d69
- Update docs
- Remove python 2 dependence
- Disable tests because of their dependence on python 2

* Fri Oct 25 2019 Jani Juhani Sinervo <jani@sinervo.fi> - 3.1.3-1.20191025git49b07a1
- Update to version 3.1.3
- emacs-ledger and emacs-ledger-el have been separated from the main tree
- Enable tests

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 3.1.1-24
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.1.1-22
- Obsolete the python2-ledger subpackage rhbz#1629493

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 3.1.1-19
- Rebuild for ICU 62

* Wed May 02 2018 Pete Walter <pwalter@fedoraproject.org> - 3.1.1-18
- Rebuild for ICU 61.1

* Tue May 01 2018 Jonathan Wakely <jwakely@redhat.com> - 3.1.1-17
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 3.1.1-16
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.1-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 3.1.1-13
- Rebuild for ICU 60.1

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.1-12
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.1-11
- Python 2 binary package renamed to python2-ledger
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 10 2017 Iliana Weller <ilianaw@buttslol.net> - 3.1.1-10
- Rebuilt after F27 rebuild stabilization

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Iliana Weller <ilianaw@buttslol.net> - 3.1.1-8
- Apply patch to fix builds on boost 1.61+ (#1423835)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 3.1.1-6
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 3.1.1-3
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.1.1-1
- update to upstream release 3.1.1

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 3.1-10
- Rebuilt for Boost 1.60

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 3.1-9
- rebuild for ICU 56.1

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.1-8
- Rebuilt for Boost 1.59

* Mon Jul 27 2015 Adam Williamson <awilliam@redhat.com> - 3.1-7
- add patches from jwakely to fix build with Boost 1.58
- fix pkgdocdir usage

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com>
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 3.1-4
- Rebuild for boost 1.57.0

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 3.1-3
- rebuild for ICU 54.1

* Tue Dec 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.1-2
- add conditional macro for _pkgdocdir

* Tue Nov 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.1-1
- update to upstream release 3.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 3.0.2-10
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.0.2-7
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 3.0.2-6
- rebuild for boost 1.55.0

* Sun May 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.0.2-5
- include useful scripts from contrib/
- include more sample files
- include example python script (demo.py)
- add bash completion

* Sun May 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.0.2-4
- add ledger-python subpackage with Python bindings
- remove BR: doxygen for now (until jQuery is packaged)

* Sun May 04 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.0.2-3
- revert upstream commit aa2ff2b5 which caused a regression

* Sun Apr 27 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.0.2-2
- fix @node pointer errors in Info files resulting in broken navigation

* Sun Apr 27 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.0.2-1
- update to upstream release 3.0.2
- remove EL6 related macros
- update URL
- use specific commit hash to obtain sources from GitHub
- update BuildRequires and build using CMake
- build HTML/PDF documentation
- revert a patch from upstream that requires boost 1.55 (not yet available
  on Fedora)
- libamounts now known as libledger
- use man page that is now built by upstream

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 2.6.3-6.2
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.6.3-4.2
- rebuild with new gmp without compat lib

* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 2.6.3-4.1
- rebuild with new gmp

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 2.6.3-3
- Rebuilt for gcc bug 634757

* Tue Jul  6 2010 Jim Radford <radford@blackbean.org> - 2.6.3-2
- Only support emacs until someone tests xemacs

* Tue Jul  6 2010 Jim Radford <radford@blackbean.org> - 2.6.3-1
- Upgrade to 2.6.2

* Thu Jan  1 2009 Jim Radford <radford@blackbean.org> - 2.6.1-1
- Initial release
