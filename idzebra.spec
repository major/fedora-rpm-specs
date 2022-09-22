Name:    idzebra
Version: 2.1.4
Release: 18%{?dist}
Summary: High performance structured text indexing and retrieval engine

License: GPLv2+
URL:     http://www.indexdata.dk/zebra/
Source0: http://ftp.indexdata.dk/pub/zebra/%{name}-%{version}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: expat-devel
BuildRequires: gcc
BuildRequires: libicu-devel
BuildRequires: libxslt-devel
BuildRequires: libyaz-devel
BuildRequires: perl-generators
BuildRequires: tcl
BuildRequires: zlib-devel
BuildRequires: make

Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
Zebra is a high-performance, general-purpose structured text indexing
and retrieval engine. It reads structured records in a variety of input
formats (such as email, XML, and MARC) and allows access to them through
exact Boolean search expressions and relevance-ranked free-text queries.


%package -n lib%{name}
Summary: Zebra libraries

%description -n lib%{name}
Libraries for the Zebra search engine.


%package -n lib%{name}-modules
Summary: Zebra modules
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-modules
Modules for the Zebra search engine


%package -n lib%{name}-devel
Summary: Zebra development libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
Development libraries for the Zebra search engine.


%prep
%autosetup -p 1


%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
rm  %{buildroot}%{_libdir}/*.la \
    %{buildroot}%{_libdir}/%{name}-2.0/modules/*.la


%ldconfig_scriptlets lib%{name}


%files
%doc ChangeLog NEWS README.md TODO
%license LICENSE.zebra
%{_datadir}/%{name}-2.0/tab
%{_bindir}/zebrasrv*
%{_bindir}/zebraidx*
%{_bindir}/idzebra-abs2dom
%{_defaultdocdir}/%{name}-2.0
%{_mandir}/*/%{name}*
%{_mandir}/*/zebra*
%{_datadir}/%{name}-2.0-examples


%files -n lib%{name}
%doc ChangeLog NEWS README.md TODO
%license LICENSE.zebra
%{_libdir}/*.so.*


%files -n lib%{name}-modules
%{_libdir}/%{name}-2.0/modules/*.so


%files -n lib%{name}-devel
%{_bindir}/idzebra-config-*
%{_includedir}/%{name}-2.0/*
%{_libdir}/*.so
%{_mandir}/*/idzebra-config-*
%{_datadir}/aclocal/*.m4


%changelog
* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.1.4-18
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Kevin Fenzi <kevin@scrye.com> - 2.1.4-15
- Rebuild for hiredis 1.0.2

* Tue Nov 02 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.4-14
- Rebuild for new yaz

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 2.1.4-12
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 2.1.4-11
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 2.1.4-8
- Rebuild for ICU 67

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 2.1.4-6
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 2.1.4-3
- Rebuild for ICU 63

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.1.4-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jan 03 2019 Björn Esser <besser82@fedoraproject.org> - 2.1.4-1
- Update to 2.1.4 (#1080827)
- Fix FTBFS (#1604358)
- Modernize spec-file

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.62-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.62-9
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.62-8
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.62-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.0.62-6
- Rebuilt for switch to libxcrypt

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 2.0.62-5
- Rebuild for ICU 60.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.62-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.62-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 2.0.62-1
- New upstream release

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 2.0.58-9
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.58-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 2.0.58-7
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 2.0.58-5
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.0.58-4
- rebuild for ICU 53.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 3 2014 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 2.0.58-1
- Update to latest upstream release
- Rebuild for new yaz

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 2.0.52-6
- rebuild for new ICU

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0.52-4
- Perl 5.18 rebuild

* Fri Feb 01 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.0.52-3
- Rebuild for icu 50

* Wed Oct 31 2012 Nicholas van Oudtshoorn <vanoudt at gmail.com> 2.0.52-2
- Minor spec file fixes
* Mon Oct 29 2012 Nicholas van Oudtshoorn <vanoudt at gmail.com> 2.0.52-1
- New version
- Spec file fixes
* Wed Apr 27 2011 Nicholas van Oudtshoorn <vanoudt at gmail.com> 2.0.46-1
- Initial spec file for Fedora
