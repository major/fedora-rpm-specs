%global __provides_exclude_from ^%{_libdir}/groonga/plugins/normalizers/mysql\\.so$

Name:		groonga-normalizer-mysql
Version:	1.1.3
Release:	9%{?dist}
Summary:	MySQL compatible normalizer plugin for Groonga

License:	LGPLv2
URL:		http://groonga.org/
Source0:	http://packages.groonga.org/source/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	groonga-devel >= 8.0.4
BuildRequires: make
Requires:	groonga-libs >= 8.0.4

%description
This package provides MySQL compatible normalizer plugin.
You can use NormalizerMySQLGeneralCI and NormalizerMySQLUnicodeCI as normalizer.

%package devel
Summary:        Development files for groonga-normalizer-mysql
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides development files for groonga-normalizer-mysql.

%prep
%setup -q

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_libdir}/groonga/plugins/*/*.la

%files
%dir %{_libdir}/groonga
%dir %{_libdir}/groonga/plugins/
%dir %{_libdir}/groonga/plugins/normalizers
%{_libdir}/groonga/plugins/normalizers/mysql.so
%{_docdir}/%{name}/*

%files devel
%{_libdir}/pkgconfig/groonga-normalizer-mysql.pc

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Kentaro Hayashi <kenhys@gmail.com> - 1.1.3-1
- New upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Kentaro Hayashi <hayashi@clear-code.com> - 1.1.1-1
- new upstream release.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Masafumi Yokoyama <yokoyama@clear-code.com> - 1.1.0-1
- new upstream release.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.9-2
- Drop ExclusiveArch, atomic primitives now supported on all arches

* Sat Apr 4 2015 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.9-1
- new upstream release.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.6-1
- new upstream release.

* Wed Aug 7 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.5-4
- install unlisted doc files explicitly.
- add comment about ExclusiveArch

* Tue Jul 30 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.5-3
- remove needless directory ownership about plugin directory.
- use fully versioned dependency to base package.

* Mon Jul 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.5-2
- remove needless continuous line from configure section.

* Sat Jun 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.5-1
- new upstream release.

* Wed May 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.4-1
- new upstream release.

* Mon Apr 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.3-1
- new upstream release.
- Reduce required packages. groonga-libs is only required.
- Require groonga 3.0.3 or later.
- Split development files into -devel package.

* Fri Mar 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.2-0
- new upstream release.

* Thu Feb 28 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.1-1
- new upstream release

* Tue Jan 29 2013 HAYASHI Kentaro <hayashi@clear-code.com> - 1.0.0-1
- initial packaging for Fedora
