%global docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

Name:		QuantLib
Version:	1.29
Release:	8%{?dist}
Summary:	A software framework for quantitative finance
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.quantlib.org
Source0:	https://dl.bintray.com/quantlib/releases/QuantLib-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc, gcc-c++
BuildRequires:	boost-devel >= 1.43, texlive-latex, texlive-dvips, emacs

%description
QuantLib is a free/open-source library for modeling, trading, and 
risk management in real-life.

%package devel
Summary:	QuantLib development files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Static libraries and headers for QuantLib.

%package test
Summary:	The test-suite to check the setup of QuantLib
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description test
The QuantLib-test-suite will validate the compiled code against 
pre-constructed test cases, and helps in validating the library.

%package doc
Summary:	The documentation for QuantLib
Requires:	%{name} = %{version}
BuildRequires:	doxygen >= 1.3, graphviz

%description doc
This package contains documentation files generated from the source code of
QuantLib.

%prep
%setup -q

%build
%configure --enable-intraday CFLAGS="$RPM_OPT_FLAGS -fpermissive" CPPFLAGS="$RPM_OPT_FLAGS -fpermissive"
# Get rid of RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
# pdf and ps file creation process breaks tetex
# make pdf-local ps-local

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{docdir}
#cp -p Docs/latex/refman.pdf %{buildroot}%{docdir}/QuantLib-%{version}-docs-refman.pdf
#cp -p Docs/latex/refman.ps %{buildroot}%{docdir}/QuantLib-%{version}-docs-refman.ps
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p man/*.1 %{buildroot}%{_mandir}/man1/
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/*.a
# So many of the names in the Quantlib manpages are generic, so we rename them to avoid conflicts.
%if 0
for i in history format gamma manips engines rate floor group license todo error deprecated attachment description domain.hpp method next value end y0 Constraint length; do
	if [ -f %{buildroot}%{_mandir}/man3/$i.3 ]; then
		mv %{buildroot}%{_mandir}/man3/$i.3 %{buildroot}%{_mandir}/man3/ql-$i.3
	else
		echo "$i.3 not found in %{buildroot}%{_mandir}/man3/"
	fi
done

# Get rid of spaces in man page names
mv "%{buildroot}%{_mandir}/man3/Singleton_ ExchangeRateManager _.3" %{buildroot}/%{_mandir}/man3/Singleton_ExchangeRateManager.3
# mv "%%{buildroot}%%{_mandir}/man3/Singleton_ IndexManager _.3" %%{buildroot}/%%{_mandir}/man3/Singleton_IndexManager.3
mv "%{buildroot}%{_mandir}/man3/operator Leg.3" %{buildroot}/%{_mandir}/man3/operator_Leg.3
mv "%{buildroot}%{_mandir}/man3/Singleton_ CommoditySettings _.3" %{buildroot}/%{_mandir}/man3/Singleton_CommoditySettings.3
mv "%{buildroot}%{_mandir}/man3/Singleton_ UnitOfMeasureConversionManager _.3" %{buildroot}/%{_mandir}/man3/Singleton_UnitOfMeasureConversionManager.3
# Fix file encoding
recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        mv -f "${1}_" "$1"
}
recode %{buildroot}%{_mandir}/man3/QuantLib_DKKCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_SEKCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_NOKCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_FIMCurrency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/QuantLib_Currency.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/ql-group.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/ql-history.3 iso-8859-1
recode %{buildroot}%{_mandir}/man3/ql-license.3 iso-8859-1
%endif

# Fix multilib conflicts
touch -r News.md %{buildroot}%{_bindir}/quantlib-config
touch -r News.md %{buildroot}%{_datadir}/emacs/site-lisp/quantlib.elc

%ldconfig_scriptlets

%files
%doc LICENSE.TXT
%{_libdir}/libQuantLib.so.*

%files devel
%{_includedir}/ql/
%{_libdir}/libQuantLib.so
%{_libdir}/pkgconfig/quantlib.pc
%{_bindir}/quantlib-config
%{_mandir}/man1/quantlib-config.*
%{_mandir}/man1/quantlib-benchmark.*
%{_datadir}/aclocal/quantlib.m4
%{_datadir}/emacs/site-lisp/*

%files test
%{_bindir}/quantlib-test-suite
%{_mandir}/man1/quantlib-test-suite.*

%files doc
%doc Contributors.txt ChangeLog.txt README.md News.md
%if 0
%{_mandir}/man3/*
%endif
%{_mandir}/man1/BasketLosses.*
%{_mandir}/man1/Bonds.*
%{_mandir}/man1/BermudanSwaption.*
%{_mandir}/man1/CallableBonds.*
%{_mandir}/man1/CDS.*
%{_mandir}/man1/ConvertibleBonds.*
%{_mandir}/man1/CVAIRS.*
%{_mandir}/man1/DiscreteHedging.*
%{_mandir}/man1/EquityOption.*
%{_mandir}/man1/FittedBondCurve.*
%{_mandir}/man1/FRA.*
%{_mandir}/man1/Gaussian1dModels.*
%{_mandir}/man1/GlobalOptimizer.*
%{_mandir}/man1/LatentModel.*
%{_mandir}/man1/MarketModels.*
%{_mandir}/man1/MulticurveBootstrapping.*
%{_mandir}/man1/MultidimIntegral.*
%{_mandir}/man1/Replication.*
%{_mandir}/man1/Repo.*
#%%{docdir}/QuantLib-%%{version}-docs-refman.pdf
#%%{docdir}/QuantLib-%%{version}-docs-refman.ps

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.29-7
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.29-3
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 27 2023 Tom Callaway <spot@fedoraproject.org> - 1.29-1
- update to 1.29

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.16-10
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.16-8
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.16-5
- Rebuilt for Boost 1.75

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.16-3
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Tom Callaway <spot@fedoraproject.org> - 1.16-1
- update to 1.16

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.13-2
- Rebuilt for Boost 1.69

* Wed Jul 25 2018 Tom Callaway <spot@fedoraproject.org> - 1.13-1
- update to 1.13
- add BuildRequires: gcc, gcc-c++
- man3 files are gone

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Tom Callaway <spot@fedoraproject.org> - 1.12.1-1
- update to 1.12.1
- rename "length" man page to avoid conflict

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 1.10.1-2
- Rebuilt for Boost 1.66

* Thu Aug 31 2017 Tom Callaway <spot@fedoraproject.org> - 1.10.1-1
- update to 1.10.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Tom Callaway <spot@fedoraproject.org> - 1.10-3
- enable --enable-intraday option

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.10-2
- Rebuilt for Boost 1.64

* Thu Jun  1 2017 Tom Callaway <spot@fedoraproject.org> - 1.10-1
- update to 1.10

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.9.1-2
- Rebuilt for Boost 1.63

* Mon Jan 16 2017 Tom Callaway <spot@fedoraproject.org> - 1.9.1-1
- update to 1.9.1

* Fri Sep 23 2016 Tom Callaway <spot@fedoraproject.org> - 1.8.1-1
- update to 1.8.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 1.7.1-2
- fix define to be global

* Mon Jan 18 2016 Tom Callaway <spot@fedoraproject.org> - 1.7.1-1
- update to 1.7.1

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.7-2
- Rebuilt for Boost 1.60

* Tue Nov  3 2015 Tom Callaway <spot@fedoraproject.org> - 1.7-1
- update to 1.7

* Wed Sep  9 2015 Tom Callaway <spot@fedoraproject.org> - 1.6.2-1
- update to 1.6.2

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-3
- Rebuilt for Boost 1.59

* Thu Aug 13 2015 Tom Callaway <spot@fedoraproject.org> - 1.6.1-2
- build again to dodge boost override

* Thu Aug  6 2015 Tom Callaway <spot@fedoraproject.org> - 1.6.1-1
- update to 1.6.1

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.6-3
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun  5 2015 Tom Callaway <spot@fedoraproject.org> - 1.6-1
- update to 1.6

* Mon May 04 2015 Tom Callaway <spot@fedoraproject.org> - 1.5-1
- update to 1.5

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-8
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.4-7
- Rebuild for boost 1.57.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.4-4
- Rebuild for boost 1.55.0

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.4-3
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.4-2
- rebuild for boost 1.55.0

* Thu Feb 27 2014 Tom Callaway <spot@fedoraproject.org> - 1.4-1
- update to 1.4

* Mon Dec  2 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.2.1-7
- Unversioned doc dir tweaks (#993925).

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.2.1-5
- Rebuild for boost 1.54.0

* Fri Mar  1 2013 Tom Callaway <spot@fedoraproject.org> - 1.2.1-4
- rename conflicting man pages (bz 915125)

* Sat Feb 23 2013 Kevin Fenzi <kevin@scrye.com> - 1.2.1-3
- Rebuild for broken deps in rawhide
- Drop texlive-utils as it no longer exists or is needed. 

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.2.1-2
- Rebuild for Boost-1.53.0

* Tue Sep 11 2012 Tom Callaway <spot@fedoraproject.org> - 1.2.1-1
- update to 1.2.1

* Fri Aug  3 2012 Tom Callaway <spot@fedoraproject.org> - 1.2-3
- fix build issues 

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr  3 2012 Tom Callaway <spot@fedoraproject.org> - 1.2-1
- update to 1.2

* Mon Apr  2 2012 Tom Callaway <spot@fedoraproject.org> - 1.1-6
- fix more manpage conflicts

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.1-3
- rebuild for new boost

* Fri Aug  5 2011 Tom Callaway <spot@fedoraproject.org> - 1.1-2
- rebuild for new boost

* Sat May 28 2011 Tom Callaway <spot@fedoraproject.org> - 1.1-1
- update to 1.1

* Fri Apr 15 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.1-7
- rebuild for new boost

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 06 2011 Thomas Spura <tomspur@fedoraproject.org> - 1.0.1-5
- rebuild for new boost

* Wed Aug  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-4
- rebuild for new boost

* Fri Apr 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-3
- have doc package own new MarketModels manpage

* Fri Apr 23 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-2
- fix files listing, shared libs are now sanely versioned!

* Tue Apr 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.1-1
- update to 1.0.1

* Mon Mar  1 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-1
- update to 1.0

* Wed Jan 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.9-1
- update to 0.9.9
- don't package static libs (resolves 556035)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Benjamin Kosnik  <bkoz@redhat.com> - 0.9.7-4
- Rebuild for boost-1.37.0.

* Mon Nov 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.7-3
- rename conflicting man pages (bz 472615)

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.7-2
- missing man pages

* Thu Nov 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.7-1
- update to 0.9.7

* Mon Mar 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-5
- no operator _.3 man page in 0.9.0

* Mon Mar 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-4
- fix file conflicts with poorly named manpages (bz 437616)

* Wed Feb 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-3
- FittedBondCurve manpage

* Wed Feb 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-2
- build fixes

* Wed Feb 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.0-1
- bump to 0.9.0

* Mon Oct 29 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.1-4
- fix more conflicting manpages (bz 322201)
- fix multilib conflict (bz 343041)

* Thu Sep 20 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.1-3
- another conflicting man page (resolves bugzilla 297161)

* Sun Aug 26 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.1-2
- rebuild for BuildID

* Mon Aug  6 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.1-1.1
- rebuild for new boost in rawhide

* Tue Jul 10 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.1-1
- bump to 0.8.1

* Thu Jan 18 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.14-2
- namespace conflicts resolved (210206)

* Fri Jan  5 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.14-1
- bump to 0.3.14
- patch0 is obsolete
- fix more namespace conflicts

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.13-4
- adjust for new man pages

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.13-3
- fix missing sources

* Fri Sep 15 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.13-2
- fc6 bump

* Tue Aug 22 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.13-1
- bump to 0.3.13

* Thu Apr  6 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.12-1
- bump to 0.3.12, resolve bz 182228, bz 181867

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-4
- bump for FC-5

* Fri Nov 18 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-3
- use -fpermissive to deal with icky c++ code

* Thu Nov 17 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-2
- fix patch

* Wed Nov 16 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-1
- bump for new release

* Fri Jul 29 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.10-1
- Bump for new release

* Sat Jun 25 2005 Colin Charles <colin@fedoraproject.org> 0.3.9-2
- Fix download URL

* Fri Jun  3 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.9-1
- cleanup spec
- add emacs,xemacs BuildRequires
- bump to 0.3.9

* Tue May 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-7
- fix QuantLib-0.3.8-installdatahookfix.patch

* Sat Apr 16 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-6
- add tetex BuildRequires

* Fri Apr 15 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-5
- minor spec cleanups

* Thu Apr 14 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-4
- bump number because of cvs issues

* Mon Apr 11 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-3
- Cleanup docs handling

* Sat Apr  2 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-2
- add $(DESTDIR) to make install-data-hook
- rename two man pages due to generic name conflicts

* Fri Apr  1 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-1
- inital package for Fedora Extras
