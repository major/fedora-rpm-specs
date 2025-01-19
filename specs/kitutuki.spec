Name:		kitutuki
Version:	0.9.6
Release:	37%{?dist}
Summary:	Shell script language
Summary(ja):	シェルスクリプティング言語 

# SPDX confirmed
License:	GPL-1.0-or-later
URL:		http://ab25cq.web.fc2.com/
Source0:	http://ab25cq.web.fc2.com/%{name}-%{version}.tgz
## Not sent to the upstream, must do later
##
# Misc fixes for Makefile
Patch0:		kitutuki-0.9.5-makefile-misc-fix.patch
# Patch for kitutuki_help
Patch1:		kitutuki-0.9.1-kitutuki_help.patch
# Patch for configure, need autoconf
Patch2:		kitutuki-0.9.3-configure-migemo.patch
# Patch to compile with gcc10 -fno-common
Patch3:		kitutuki-0.9.6-gcc10-fno-common.patch

BuildRequires:  gcc
BuildRequires:	cmigemo-devel
BuildRequires:	ncurses-devel
BuildRequires:	oniguruma-devel
BuildRequires:	readline-devel

# Patch2
BuildRequires:	autoconf
BuildRequires:	make

%description
Kitutuki is a shell script language.

%description	-l ja
Kitutukiはシェルスクリプト言語です

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
%{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

# Makefile
%patch -P0 -p1 -b .mk
sed -i.strip -e '/install/s| -s | |' Makefile.in
sed -i.stamp -e 's|\([ \t][ \t]*install \)|\1 -p |' Makefile.in

# Other patches
%patch -P1 -p1 -b .help
%patch -P3 -p1 -b .gcc10

# configure
%patch -P2 -p1 -b .cf
autoconf
sed -i.cflags -e '/CFLAGS=/s|-fPIC|-fPIC %{optflags}|' configure

# Miscs
iconv -f EUC-JP -t UTF-8 README.ja.txt > README.ja.txt.utf8
touch -r README.ja.txt{,.utf8}
mv -f README.ja.txt{.utf8,}

%build
%configure \
	--sysconfdir=%{_libdir}/%{name} \
	--includedir=%{_includedir}/%{name} \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo \
	%{nil}

make %{?_smp_mflags} \
	docdir=%{_defaultdocdir}/%{name}/


%install
rm -rf %{buildroot}
# make install DESTDIR=%%{buildroot}
# Above does not work...
rm -rf ./Trash
%makeinstall \
	sysconfdir=%{buildroot}%{_libdir}/%{name}/ \
	includedir=%{buildroot}%{_includedir}/%{name}/ \
	docdir=$(pwd)/Trash/ \
	%{nil}

# Move kitutuki.ksh to %%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mv %{buildroot}%{_libdir}/%{name}/kitutuki.ksh \
	%{buildroot}%{_sysconfdir}/%{name}
ln -sf ../../../%{_sysconfdir}/%{name}/kitutuki.ksh \
	%{buildroot}%{_libdir}/%{name}/

%ldconfig_scriptlets

%files
%doc	AUTHORS
%license	GPL
%lang(ja)	%doc	README.ja.txt
%doc	usage.en.txt
%lang(ja)	%doc	usage.ja.txt

%dir %{_sysconfdir}/%{name}
# In case that kitutuki.ksh changes much as this is quite a
# new package, rather mark this as no-noreplace
%config	%{_sysconfdir}/%{name}/kitutuki.ksh
%{_bindir}/%{name}
%{_libdir}/libkitutuki.so.1{,.*}
%{_libdir}/%{name}/

%files	devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-35
- SPDX migration

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-24
- Fix for gcc10 -fno-common

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.6-22
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 01 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-19
- Rebuild against oniguruma 6.8.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.9.6-14
- Rebuild for readline 7.x

* Sun Oct 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-13
- Rebuild for oniguruma 6.1.1

* Mon Jul 18 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-12
- Rebuild for oniguruma 6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-7
- F-20: adjust for feature: UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.6-1
- Update to 0.9.6

* Tue Feb 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.5-2.respin1
- 0.9.5 respun

* Tue Feb 23 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.5-1
- Update to 0.9.5

* Sat Feb 20 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.3-1
- Update to 0.9.3

* Wed Feb 17 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.1-2
- Add Japanese summary / description
- Add more comments about kitutuki.ksh
- Fix kitutuki.ksh for kitutuki_help

* Tue Feb 16 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.1-1
- Initial packaging
