Summary:	Library for national and language-specific issues
Name:		libnatspec
Version:	0.2.6
Release:	25%{?dist}

License:	LGPLv2
Url:		http://sourceforge.net/projects/natspec
Source:		https://downloads.sourceforge.net/project/natspec/natspec/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	popt-devel
BuildRequires:	autoconf, automake, libtool
BuildRequires: make


%description
Library for national and language-specific issues.
This library provides userful functions for
mount, submount, mkisofs, multimedia players.
This library try to help resolve charset hell (encoding problem)
in a various programs depends on locale and messages.


%package	devel
Summary:	Development package of library for national and language-specific issues
Requires:	%{name}%{?_isa} = %{version}-%{release}
# All examples use GPLGv2+ else unzip and zip which uses BSD
License:	GPLv2+ and BSD

%description devel
The %{name}-devel package contains libraries and header files for
developing extensions for %{name}.


%prep
%setup -q

# Fix permissions
chmod 644 profile/*
find examples -type f -exec chmod 644 {} \;

pushd examples
iconv -f KOI8-R catpkt-1.0-alt-natspec.patch -t UTF-8 > catpkt-1.0-alt-natspec.patch.new
mv catpkt-1.0-alt-natspec.patch.new catpkt-1.0-alt-natspec.patch
popd

iconv -f KOI8-R -t UTF-8 ChangeLog > ChangeLog.new
mv ChangeLog.new ChangeLog

%build
autoreconf -fiv
%configure --with-i18n-file=/etc/locale.conf
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc AUTHORS README ChangeLog NEWS TODO README-ru.html
%{_libdir}/*.so.*
%{_bindir}/*
%{_mandir}/man1/*


%files devel
%doc examples profile
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec  1 2012  <drizt@land.ru> - 0.2.6-6
- migration i18n
- fixed license for examples

* Mon Oct 29 2012 Ivan Romanov <drizt@land.ru> - 0.2.6-5
- dropped %%defattr
- corrected description

* Sat Oct 27 2012 Ivan Romanov <drizt@land.ru> - 0.2.6-4
- Fedora package
- Dropped unusual %%clean stage and rm in %%install stage
- Dropped BuildRoot
- Fixed make install
- Uses %%{_isa}
- profile and examplese moved to -devel subpackage
- Fixed group for main package
- added dos2unix to BR

* Sat Mar 19 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.6-2
- rebuilt

* Sat Feb  6 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.6-1
- initial build for Fedora
