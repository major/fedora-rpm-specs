Name:           glimmer
Version:        3.02b
Release:        29%{?dist}
Summary:        System for finding genes in microbial DNA

# Automatically converted from old format: Artistic clarified - review is highly recommended.
License:        ClArtistic
URL:            http://www.cbcb.umd.edu/software/glimmer
Source0:        http://www.cbcb.umd.edu/software/glimmer/glimmer302b.tar.gz
BuildRequires:  gcc-c++
BuildRequires: make
Requires:       elph

%description
Glimmer is a system for finding genes in microbial DNA, especially the genomes
of bacteria, archaea, and viruses. Glimmer (Gene Locator and Interpolated
Markov ModelER) uses interpolated Markov models (IMMs) to identify the coding
regions and distinguish them from noncoding DNA.


%prep
%setup -q -n glimmer3.02
rm -f sample-run/g3-*
sed -i "s+/fs/szgenefinding/Glimmer3/bin+%{_libexecdir}/glimmer3+" scripts/g3-*
sed -i "s+/fs/szgenefinding/Glimmer3/scripts+%{_datadir}/glimmer3+" scripts/g3-*
sed -i "s+/nfshomes/adelcher/bin/elph+%{_bindir}/elph+" scripts/g3-*
sed -i "s/@ if/if/" src/c_make.gen


%build
make -C src %{?_smp_mflags} CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"


%check


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/glimmer3
mkdir -p $RPM_BUILD_ROOT%{_datadir}/glimmer3
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 scripts/g3-* $RPM_BUILD_ROOT/%{_bindir}
install -m 755 bin/[a-su-z]* $RPM_BUILD_ROOT%{_libexecdir}/glimmer3
install -m 755 scripts/*.awk $RPM_BUILD_ROOT%{_datadir}/glimmer3
ln -s ../libexec/glimmer3/glimmer3 $RPM_BUILD_ROOT/%{_bindir}/glimmer3



%files
%doc LICENSE glim302notes.pdf sample-run
%{_bindir}/*
%{_datadir}/glimmer3/
%{_libexecdir}/glimmer3/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 3.02b-28
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 3.02b-17
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Christian Iseli <Christian.Iseli@unil.ch> - 3.02b-12
- Fix FTBFS due to missing BuildRequires gcc-c++ (bz 1606906)
- Fix rpmlint warning for bogus date in changelog

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.02b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.02b-5
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02b-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Christian Iseli <Christian.Iseli@unil.ch> - 3.02b-1
- Updated upstream, which has integrated the necessary gcc build patch
- Remove patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-9
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Christian Iseli <Christian.Iseli@licr.org> - 3.02-5
- Update patch for gcc-4.4

* Mon Feb 23 2009 Christian Iseli <Christian.Iseli@licr.org> - 3.02-4
- Rebuild for F-11

* Wed Jan 16 2008 Christian Iseli <Christian.Iseli@licr.org> - 3.02-3
- Add patch to port to gcc-4.3.

* Wed Aug 22 2007 Christian Iseli <Christian.Iseli@licr.org> - 3.02-2
- Fix License tag.

* Thu Feb 22 2007 Christian Iseli <Christian.Iseli@licr.org> - 3.02-1
- Import in Fedora devel.

* Fri Feb  9 2007 Christian Iseli <Christian.Iseli@licr.org> - 3.02-0
- Create spec file.
