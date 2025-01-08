Name:		unuran
Version:	1.11.0
Release:	1%{?dist}
Summary:	Universal Non-Uniform Random number generator

License:	GPL-2.0-or-later
URL:		http://statistik.wu-wien.ac.at/unuran
Source0:	http://statistik.wu-wien.ac.at/unuran/%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc-c++

%description
UNU.RAN is an ANSI C library licensed under GPL.
It contains universal (also called automatic or black-box) algorithms
that can generate random numbers from large classes of continuous or
discrete distributions, and also from practically all standard
distributions.

The library and an extensive online documentation are available at:

	  -------------------------------------------
	     http://statistik.wu-wien.ac.at/unuran/
	  -------------------------------------------

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Header and object files for unuran

%description devel
Header and object files for unuran, and pdf docs.

%prep
%autosetup -p1

%build
%configure --enable-shared --disable-static
%make_build

%install
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/libunuran.la
rm $RPM_BUILD_ROOT/%{_includedir}/unuran_tests.h
rm $RPM_BUILD_ROOT/%{_infodir}/unuran_win32*
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

# clean examples
rm -rf __dist_examples __clean_examples
cp -a examples __clean_examples
make -C __clean_examples distclean
rm __clean_examples/Makefile*
mkdir __dist_examples
mv __clean_examples __dist_examples/examples

%files
%doc AUTHORS README NEWS KNOWN-PROBLEMS THANKS UPGRADE
%license COPYING
%{_infodir}/unuran*
%{_libdir}/libunuran.so.*

%files devel
%{_includedir}/unuran*.h
%{_libdir}/libunuran.so
%doc doc/unuran.pdf __dist_examples/examples

%check # enable if you want - takes a long time
SEED=2742664 make check

%changelog
* Mon Jan 06 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.11.0-1
- Update to 1.11.0

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.9.0-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec  2 2022 Florian Weimer <fweimer@redhat.com> - 1.9.0-3
- Port configure script to C99 (#2150308)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 16 2022 Neal Becker <ndbecker2@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.8.1-7
- Add BuildRequires gcc-c++
- Adjust specfile for updated packaging guidelines

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.8.1-1
- Rebuilt for new upstream release 1.8.1, fixes rhbz #698168

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 1.8.0-11
- Spec clean up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 27 2010 Neal Becker <ndbecker2@gmail.com> - 1.8.0-1
- update to 1.8.0

* Tue Apr 27 2010 Neal Becker <ndbecker2@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Fri Apr 23 2010 Neal Becker <ndbecker2@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Fri Apr 23 2010 Neal Becker <ndbecker2@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Sat Oct 17 2009 Neal Becker <ndbecker2@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  9 2009 Neal Becker <ndbecker2@gmail.com> - 1.3.1-1
- Update to 1.3.1 final

* Thu Jan  8 2009 Neal Becker <ndbecker2@gmail.com> - 1.3-1.devel%{?dist}
- Update to 1.3.devel

* Thu Dec 18 2008 Neal Becker <ndbecker2@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Tue Apr 29 2008 Neal Becker <ndbecker2@gmail.com> - 1.2.4-p1-1
- Update to 1.2.4-p1 (remove failing test)

* Tue Apr 29 2008 Neal Becker <ndbecker2@gmail.com> - 1.2.4-1
- Update to 1.2.4 (fixes a roundoff problem in %%check on i386)

* Tue Apr 22 2008 Neal Becker <ndbecker2@gmail.com> - 1.2.2-1
- debug for make check

* Mon Apr 21 2008 Neal Becker <ndbecker2@gmail.com> - 1.2.2-1
- Update to 1.2.2

* Sun Mar 16 2008 Neal Becker <ndbecker2@gmail.com> - 1.2.1-2
- -fno-optimize-sibling-calls workaround for gcc-4.3

* Tue Feb 19 2008 Neal Becker <ndbecker2@gmail.com> - 1.2.1-1
- Update to 1.2.1

* Tue Feb 19 2008 Neal Becker <ndbecker2@gmail.com> - 1.2.0-1
- Update to 1.2.0
- Re-enable check

* Sat Feb  9 2008 Neal Becker <ndbecker2@gmail.com> - 1.1.0-6
- Patches from pertusus@free.fr

* Fri Jan 18 2008 Neal Becker <ndbecker2@gmail.com> - 1.1.0-5
- rm %%{_infodir}/dir

* Wed Jan  9 2008 Neal Becker <ndbecker2@gmail.com> - 1.1.0-4
- Add examples
- install -p
- Add check

* Tue Jan  8 2008 Neal Becker <ndbecker2@gmail.com> - 1.1.0-3
- Move devel stuff to devel package

* Wed Dec 26 2007 Neal Becker <ndbecker2@gmail.com> - 1.1.0-2
- Fix install-info stuff
- docdir *.spec

* Wed Dec 26 2007 Neal Becker <ndbecker2@gmail.com> - 1.1.0-1
- Update to 1.1.0
- 1nstall unuran.pdf
- disable-static
- install-info

* Fri May 12 2006 Neal Becker <ndbecker2@gmail.com> - 0.7.2-2
- rm unuran_tests.h
- Add post, postun
- Fix files

