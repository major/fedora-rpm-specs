# Avoid installing arch-independent data into arch-dependent directory
# MUST for Erlang packages.
%global debug_package %{nil}

Name:           tsung
Version:        1.8.0
Release:        6%{?dist}
Summary:        A distributed multi-protocol load testing tool
License:        GPL-2.0-only
URL:            http://tsung.erlang-projects.org/
Source0:        http://tsung.erlang-projects.org/dist/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  erlang
BuildRequires:  perl-generators
# Just for expanding %%{__python3} macro
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
%else
BuildRequires:  python2-devel
BuildRequires:  python2-sphinx
%endif
BuildRequires:  doxygen-latex
BuildRequires:  latexmk
BuildRequires:  texlive-titlesec
BuildRequires:  texlive-framed
BuildRequires:  texlive-threeparttable
BuildRequires:  texlive-wrapfig
BuildRequires:  texlive-fncychap
Requires:       erlang
Requires:       gnuplot
Requires:       perl-Template-Toolkit

%description
tsung is a distributed load testing tool. It is protocol-independent and can 
currently be used to stress and benchmark HTTP, Jabber/XMPP, PostgreSQL, 
MySQL and LDAP servers.

It simulates user behavior using an XML description file, reports many 
measurements in real time (statistics can be customized with transactions, 
and graphics generated using GnuPlot).

For HTTP, it supports 1.0 and 1.1, has a proxy mode to record sessions, 
supports GET and POST methods, Cookies, and Basic WWW-authentication.
 
It also has support for SSL.

%package doc
BuildArch:      noarch
Summary:        Documentation files for tsung

%description doc
Documentation files for tsung

%prep
%setup -qn %{name}-%{version}

# Fix bogus shebangs.
sed -i 's|/usr/bin/env bash|/bin/bash|' *.sh.in
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i 's|/usr/bin/env python|/usr/bin/python|' src/tsung-plotter/tsplot.py.in
%else
sed -i 's|/usr/bin/env python|/usr/bin/python|' src/tsung-plotter/tsplot.py.in
%endif
sed -i '/SPHINXBUILD/ s|sphinx-build|sphinx-build-3|' docs/Makefile
sed -i 's|/usr/bin/env perl|/usr/bin/perl|' src/log2tsung.pl.in
# Switch to UTF-8
for file in LISEZMOI
do
    iconv -f ISO-8859-1 -t UTF-8 $file > $file.utf8
    touch -r $file $file.utf8
    mv -f $file.utf8 $file
done

%build
%configure --prefix=/usr
%make_build
cd docs
for target in html dirhtml singlehtml pickle json htmlhelp qthelp devhelp \
              epub latex latexpdf text man texinfo info gettext changes
do
    make $target ||:
done

%install
%make_install

for i in `ls %{buildroot}%{_libdir}/%{name}/bin | grep .pl$ | cut -d"." -f1`
do
  ln -sf ../%{_lib}/%{name}/bin/$i.pl %{buildroot}%{_bindir}/$i
done

# Fix versioned/unversioned docdir
rm -frv %{buildroot}%{_docdir}
rm -frv examples/*.xml.in

# Fix bogus shebang again
%if 0%{?fedora} || 0%{?rhel} >= 8
sed -i 's|python33|python3|' %{buildroot}%{_bindir}/tsplot
%else
sed -i 's|python27|python2|' %{buildroot}%{_bindir}/tsplot
%endif

%files
%doc CHANGELOG.md CONTRIBUTORS COPYING LISEZMOI README.md TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-rrd
%{_bindir}/%{name}_percentile
%{_bindir}/%{name}_stats
%{_bindir}/%{name}-recorder
%{_bindir}/log2%{name}
%{_bindir}/tsplot
%{_datadir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-recorder.1*
%{_mandir}/man1/tsplot.1*

%files doc
%doc docs examples

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 04 2023 Didier Fabert <didier.fabert@gmail.com> - 1.8.0-3
- migrated to SPDX license

* Wed Aug 02 2023 Didier Fabert <didier.fabert@gmail.com> - 1.8.0-2
- Fix python and perl shebangs https://bugzilla.redhat.com/show_bug.cgi?id=2224873

* Sat Jul 22 2023 Didier Fabert <didier.fabert@gmail.com> - 1.8.0-1
- Update to 1.8.0 (#2174608)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-19
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-16
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-13
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Didier Fabert <didier.fabert@gmail.com> - 1.7.0-10
- Conditionnal patch (not for el7)

* Mon Jun 03 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-9
- Perl 5.30 re-rebuild updated packages

* Sun Jun 02 2019 Didier Fabert <didier.fabert@gmail.com> - 1.7.0-8
- Patch to support python3 (submit to upstream)
- Create doc subpackage

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-7
- Perl 5.30 rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.0-4
- Perl 5.28 rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.7.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Didier Fabert <didier.fabert@gmail.com> - 1.7.0-1
- Update to 1.7.0 (#1486744)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-2
- Perl 5.24 rebuild

* Wed Apr 13 2016 Didier Fabert <didier.fabert@gmail.com> - 1.6.0-1
- Update to 1.6.0 (#1244745)
- Fix #1227478

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.1-5
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.5.1-4
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Christopher Meng <rpm@cicku.me> - 1.5.1-2
- Include example config files
- Better user experience for perl scripts

* Thu Jul 10 2014 Christopher Meng <rpm@cicku.me> - 1.5.1-1
- Update to 1.5.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.5.0-3
- Fix versioned/unversioned docdir

* Fri Aug 02 2013 Christopher Meng <rpm@cicku.me> - 1.5.0-2
- Fix wrong syntaxs of files.

* Sat May 25 2013 Christopher Meng <rpm@cicku.me> - 1.5.0-1
- Initial Package.
