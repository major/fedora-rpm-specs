%define		majorver	5.1
%define		date		20070304

# The data in MeCab dic are compiled by arch-dependent binaries
# and the created data are arch-dependent.
# However, this package does not contain any executable binaries
# so debuginfo rpm is not created.
%define		debug_package	%{nil}

Name:		mecab-jumandic
Version:	%{majorver}.%{date}
Release:	33%{?dist}
Summary:	JUMAN dictorionary for MeCab

# SPDX confirmed
License:	BSD-3-Clause
URL:		http://mecab.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mecab/%{name}-%{majorver}-%{date}.tar.gz

BuildRequires: make
BuildRequires:	mecab-devel
Requires:	mecab

%description
MeCab JUMAN is a dictionary for MeCab using CRF estimation
based on Kyoto corpus.
This dictionary is for UTF-8 use.

%package 	EUCJP
Summary:	JUMAN dictionary for Mecab with encoded by EUC-JP
Requires:	mecab

%description EUCJP

MeCab JUMAN is a dictionary for MeCab using CRF estimation
based on Kyoto corpus.
This dictionary is for EUC-JP use.

%prep
%setup -q -n %{name}-%{majorver}-%{date}

%build
# First build on UTF-8
%configure \
	--with-mecab-config=%{_bindir}/mecab-config \
	--with-charset=utf8
%{__make} %{?_smp_mflags}
# Preserve them
%{__mkdir} UTF-8
%{__cp} -p \
	*.bin *.dic *.def dicrc \
	UTF-8/

# Next build on EUC-JP
# This is the default, however Fedora uses UTF-8 so
# for Fedora this must be the option.
%{__make} clean
%configure \
	--with-mecab-config=%{_bindir}/mecab-config
%{__make} %{?_smp_mflags}


%install
# First install EUC-JP
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__mv} $RPM_BUILD_ROOT%{_libdir}/mecab/dic/jumandic \
	$RPM_BUILD_ROOT%{_libdir}/mecab/dic/jumandic-EUCJP

# Next install UTF-8
%{__mv} -f UTF-8/* .
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
# Note: post should be okay. mecab-dic expects that
# mecab is installed in advance.
if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/jumandic|' \
		%{_sysconfdir}/mecabrc || :
fi

%post EUCJP
# Note: post should be okay. mecab-dic expects that
# mecab is installed in advance.
if test -f %{_sysconfdir}/mecabrc ; then
	%{__sed} -i -e 's|^dicdir.*|dicdir = %{_libdir}/mecab/dic/jumandic-EUCJP|' \
		%{_sysconfdir}/mecabrc || :
fi

%files
%doc AUTHORS
%license COPYING
%{_libdir}/mecab/dic/jumandic/

%files EUCJP
%doc AUTHORS
%license COPYING
%{_libdir}/mecab/dic/jumandic-EUCJP/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 10 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.20070304-31
- SPDX migration

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.20070304-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20070304-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.20070304-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 5.1.20070304-4
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 5.1.20070304-3
- F-11: Mass rebuild

* Fri Jun 13 2008 Jon Stanley <jonstanley@gmail.com> - 5.1-20070304-2
- Rebuild

* Thu Mar  8 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 5.1.20070304-1
- 5.1 date 20070304

* Sun Mar  4 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 5.1.20051121-4
- Add missing defattr and make sed script safer.

* Sat Mar  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 5.1.20051121-3
- Change default to UTF-8 and make EUC-JP charset package.

* Tue Feb 27 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 5.1.20051121-2
- Package requirement deps reconstruct

* Fri Feb 23 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 5.1.20051121-1
- Initial packaging for Fedora.
