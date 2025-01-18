Name:           fcgi
Version:        2.4.0
Release:        51%{?dist}
Summary:        FastCGI development kit

License:        OML
URL:            http://www.fastcgi.com/#TheDevKit
Source0:        http://fastcgi.com/dist/fcgi-%{version}.tar.gz

Patch1:         fcgi-2.4.0-autotools.patch
Patch2:         fcgi-2.4.0-gcc44_fixes.patch
# CVE-2012-6687
Patch3:         fcgi-2.4.0-poll.patch
Patch4:         fcgi-configure-exit.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  sed
BuildRequires:  coreutils
BuildRequires: make

%description
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific APIs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p 1

# remove DOS End Of Line Encoding
sed -i 's/\r//' doc/fastcgi-prog-guide/ch2c.htm

# fix file permissions
chmod a-x include/fcgios.h libfcgi/os_unix.c LICENSE.TERMS doc/fastcgi-prog-guide/*

%build
%configure
# fix bz1987468
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build -j1

%install
%make_install

rm %{buildroot}%{_libdir}/libfcgi{++,}.{l,}a

install -p -m 0644 -D doc/cgi-fcgi.1 %{buildroot}%{_mandir}/man1/cgi-fcgi.1

for manpage in doc/*.3
do
install -p -m 0644 -D $manpage %{buildroot}%{_mandir}/man3/$(basename $manpage)
done

rm -f -- doc/*.1
rm -f -- doc/*.3

%files
%{_bindir}/cgi-fcgi
%{_libdir}/libfcgi.so.*
%{_libdir}/libfcgi++.so.*
%{_mandir}/man1/*
%license LICENSE.TERMS
%doc LICENSE.TERMS

%files devel
%{_includedir}/*
%{_libdir}/libfcgi.so
%{_libdir}/libfcgi++.so
%{_mandir}/man3/*
%doc doc/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Florian Weimer <fweimer@redhat.com> - 2.4.0-45
- Fix another implicit declaration of exit (#2143591)

* Thu Nov 17 2022 Florian Weimer <fweimer@redhat.com> - 2.4.0-44
- Avoid implicit declaration of exit in configure (#2143591)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Andrew Bauer <zonexpertconsulting@outlook.com> - 2.4.0-41
- Disable rpath bz1987468

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 2.4.0-38
- Modernize specfile

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.4.0-27
- Rebuilt for GCC 5 C++11 ABI change

* Fri Feb 06 2015 Till Maas <opensource@till.name> - 2.4.0-26
- Use %%license

* Fri Feb 06 2015 Till Maas <opensource@till.name> - 2.4.0-25
- Fix crash when too many connections are used (CVE-2012-6687)
- Make gcc build dependencies obvious for local builds

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 03 2014 Till Maas <opensource@till.name> - 2.4.0-22
- Harden build

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 09 2011 Iain Arnell <iarnell@gmail.com> 2.4.0-17
- drop perl sub-package; it's been replaced by perl-FCGI (rhbz#736612)

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.4.0-16
- Perl mass rebuild & clean spec & clean Makefile.PL

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.4.0-14
- Mass rebuild with perl-5.12.0

* Sun May 16 2010 Till Maas <opensource@till.name> - 2.4.0-13
- Fix license tag. It's OML instead of BSD

* Mon Jan 18 2010 Chris Weyl <cweyl@alumni.drew.edu> - 2.4.0-12
- drop perl .so provides filtering, as it may have multiarch rpm implications

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.4.0-11
- rebuild against perl 5.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Chris Weyl <cweyl@alumni.drew.edu> - 2.4.0-9
- Stripping bad provides of private Perl extension libs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Till Maas <opensource@till.name> - 2.4.0-7
- Add missing #include <cstdio> to make it compile with gcc 4.4

* Tue Oct 14 2008 Chris Weyl <cweyl@alumni.drew.edu> - 2.4.0-6
- package up the perl bindings in their own subpackage

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.4.0-5
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Till Maas <opensource till name> - 2.4.0-4
- bump release for rebuild

* Wed Jul 11 2007 Till Maas <opensource till name> - 2.4.0-3
- remove parallel make flags

* Tue Apr 17 2007 Till Maas <opensource till name> - 2.4.0-2
- add some documentation
- add mkdir ${RPM_BUILD_ROOT} to %%install
- install man-pages

* Mon Mar 5 2007 Till Maas <opensource till name> - 2.4.0-1
- Initial spec for fedora
