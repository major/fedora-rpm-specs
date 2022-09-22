%global apiversion 0.1

Name: libe-book
Version: 0.1.3
Release: 21%{?dist}
Summary: A library for import of reflowable e-book formats

License: MPLv2.0
URL: https://sourceforge.net/projects/libebook/
Source: http://downloads.sourceforge.net/libebook/%{name}-%{version}.tar.xz

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: help2man
BuildRequires: make
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(liblangtag)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(zlib)

Patch0: 0001-fix-build-with-ICU-68.patch

%description
%{name} is a library for import of reflowable e-book formats.
Currently supported are PalmDoc, TealDoc, Plucker eBook, eReader eBook,
FictionBook v.2, TCR, zTXT and Broad Band eBook (LRF).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary: Tools to transform e-books into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform e-books into other formats.
Currently supported: XHTML, raw, text.

%prep
%autosetup -p1

%build
%configure --disable-silent-rules --disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in ebook2html ebook2raw ebook2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 ebook2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%make_build check

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING
%doc docs/doxygen/html

%files tools
%{_bindir}/ebook2raw
%{_bindir}/ebook2text
%{_bindir}/ebook2html
%{_mandir}/man1/ebook2html.1*
%{_mandir}/man1/ebook2raw.1*
%{_mandir}/man1/ebook2text.1*

%changelog
* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.1.3-21
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 0.1.3-17
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 0.1.3-14
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Sat May 16 2020 Pete Walter <pwalter@fedoraproject.org> - 0.1.3-13
- Rebuild for ICU 67

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 0.1.3-11
- Rebuild for ICU 65

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.1.3-8
- Rebuilt for Boost 1.69

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 0.1.3-7
- Rebuild for ICU 63

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 0.1.3-5
- Rebuild for ICU 62

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 0.1.3-4
- Rebuild for ICU 61.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.1.3-2
- Rebuilt for Boost 1.66

* Tue Jan 02 2018 David Tardon <dtardon@redhat.com> - 0.1.3-1
- new upstream release

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 0.1.2-19
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-16
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-14
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-13
- Rebuilt for Boost 1.63

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.1.2-12
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.1.2-10
- Rebuilt for Boost 1.60

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 0.1.2-9
- rebuild for ICU 56.1

* Sun Aug 30 2015 Jonathan Wakely <jwakely@redhat.com> 0.1.2-8
- Rebuilt for Boost 1.59

* Sun Aug 30 2015 David Tardon <dtardon@redhat.com> - 0.1.2-7
- fix build with boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.1.2-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.1.2-2
- Rebuild for boost 1.57.0

* Mon Jan 05 2015 David Tardon <dtardon@redhat.com> - 0.1.2-1
- new upstream release

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 0.1.1-4
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 David Tardon <dtardon@redhat.com> - 0.1.1-1
- new upstream release

* Thu May 29 2014 David Tardon <dtardon@redhat.com> - 0.1.0-2
- detect and parse zipped FictionBook 2 files again

* Mon May 26 2014 David Tardon <dtardon@redhat.com> - 0.1.0-1
- new upstream release 0.1.0

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.0.3-4
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.0.3-3
- rebuild for boost 1.55.0

* Thu Feb 13 2014 David Tardon <dtardon@redhat.com> - 0.0.3-2
- rebuild for new ICU

* Mon Feb 10 2014 David Tardon <dtardon@redhat.com> - 0.0.3-1
- new upstream release 0.0.3
- generate man pages for the conversion tools

* Sat Nov 16 2013 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new release

* Mon Nov 11 2013 David Tardon <dtardon@redhat.com> - 0.0.1-2
- install all public headers
- fix library name in .pc

* Sun Nov 10 2013 David Tardon <dtardon@redhat.com> - 0.0.1-1
- initial import
