%global		postver	-r2
%global		postrpmver	%(echo "%postver" | sed -e 's|-|.|g' | sed -e 's|^\.||')

%global		mainver		1.5

%global		baserelease	10
%global		rpmrel		%{baserelease}%{?postver:.%postrpmver}

Name:		tideEditor
Version:	%{mainver}
Release:	%{rpmrel}%{?dist}
Summary:	Editor for Tide Constituent Database (TCD) files

# SPDX confirmed
License:	GPL-3.0-or-later
URL:		http://www.flaterco.com/xtide/
Source0:	ftp://ftp.flaterco.com/xtide/tideeditor-%{version}%{?postver}.tar.xz

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	qt4-devel
BuildRequires:	libtcd-devel
# Temporally
BuildRequires:	automake
Requires:	xtide-common

%description
tideEditor is an editor for Tide Constituent Database (TCD) files.  It
was written by Jan C. Depner but is now jointly maintained by David
Flater and Jan Depner.

%prep
%setup -q -n tideeditor-%{version}

sed -i.moc Makefile.in \
	-e '\@MOC@s|CPPFLAGS|CPPFLAGS_UNUSED|'

%build
export CPPFLAGS="$RPM_OPT_FLAGS"
for mod in \
	QtCore \
	QtGui \
	%{nil}
do
	export CPPFLAGS="${CPPFLAGS} $(pkg-config --cflags $mod)"
done	
export ac_cv_path_MOC=%{_bindir}/moc-qt4

%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS
%doc ChangeLog
%doc README
%license COPYING
%{_bindir}/tideEditor

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 27 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-7.r2
- SPDX migration

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-6.r2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5.r2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5.r2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5.r2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5.r2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5.r2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-5.r2
- 1.5 respin r2

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5-1
- 1.5

* Tue Feb  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.5-1
- 1.4.5

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.4-1
- 1.4.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.3-2
- F-17: rebuild against gcc47

* Mon Sep 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.3-1
- 1.4.3

* Tue Sep 13 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.4.2-1
- 1.4.2
- License change: GPLv2+ -> GPLv3+

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-5
- Rebuild for new libtcd

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-4
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-3
- F-11: Mass rebuild

* Tue Apr  1 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-2
- Fix BuildRequires wrt qt3 <-> qt4 name change

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-1.dist.3
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-1.dist.2
- License update

* Wed Apr 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4.1-1
- 1.4.1

* Fri Apr 13 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.4-1
- 1.4

* Tue Nov 28 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.12.0.2-1
- 1.3.12-r2.

* Mon Nov 27 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.12-3
- Remove unneeded BR

* Sun Nov 26 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.12-2
- Drop desktop file after discuss with David Flater (upstream) and
  Patrice Dumas (reviewer)

* Thu Nov 23 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.12-1
- 1.3.12 release
- Introduce a shell script for GNOME desktop usage.

* Mon Nov 20 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.3.12-0.1.dev1
- Split from xtide, repackaging (see bug 211626)
