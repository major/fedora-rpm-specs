%global apiversion 0.17

%if 0%{?rhel}

# build conversion tools
%bcond_with convtools
# build python3 bindings
%bcond_with python

%else
# build conversion tools
%bcond_without convtools
# build python3 bindings
%bcond_without python

%endif

Name: liborcus
Version: 0.17.2
Release: 4%{?dist}
Summary: Standalone file import filter library for spreadsheet documents

License: MPLv2.0
URL: https://gitlab.com/orcus/orcus
Source0: https://kohei.us/files/orcus/src/%{name}-%{version}.tar.xz
Patch0:  liborcus-noexamples.patch

BuildRequires: make
BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: automake
%if %{with convtools}
BuildRequires: help2man
BuildRequires: pkgconfig(libixion-0.17)
%endif
BuildRequires: pkgconfig(mdds-2.0)
%if %{with python}
BuildRequires: pkgconfig(python3)
%if 0%{?rhel}
BuildRequires: python3
%endif
%endif
BuildRequires: pkgconfig(zlib)

%description
%{name} is a standalone file import filter library for spreadsheet
documents. Currently under development are ODS, XLSX and CSV import
filters.

%if %{with convtools}
%package model
Summary: Spreadsheet model for %{name} conversion tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description model
The %{name}-model package contains a spreadsheet model used by the
conversion tools.
%endif

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tools for working with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Helper tools for %{name} and converters of various file formats to HTML
and text.

%if %{with python}
%package python3
Summary: Python 3 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description python3
Python 3 bindings for %{name}.
%endif

%package doc
Summary: API documentation for %{name}
BuildArch: noarch

%description doc
API documentation for %{name}.

%prep
%autosetup -p1

%if %{without convtools}
%global condopts %{?condopts} --disable-spreadsheet-model
%endif
%if %{without python}
%global condopts %{?condopts} --disable-python
%endif

%build
autoreconf
%configure --disable-debug --disable-silent-rules --disable-static \
    --disable-werror --with-pic %{?condopts}
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{python3_sitearch}/*.la

%if %{with convtools}
# create and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -S '%{name} %{version}' -n 'convert a CSV file' -o orcus-csv.1 %{buildroot}%{_bindir}/orcus-csv
help2man -N -S '%{name} %{version}' -n 'convert a Gnumeric file' -o orcus-gnumeric.1 %{buildroot}%{_bindir}/orcus-gnumeric
help2man -N -S '%{name} %{version}' -n 'convert an ODF spreadsheet' -o orcus-ods.1 %{buildroot}%{_bindir}/orcus-ods
help2man -N -S '%{name} %{version}' -n 'transform an XML file' -o orcus-xls-xml.1 %{buildroot}%{_bindir}/orcus-xls-xml
help2man -N -S '%{name} %{version}' -n 'convert a OpenXML spreadsheet' -o orcus-xlsx.1 %{buildroot}%{_bindir}/orcus-xlsx
help2man -N -S '%{name} %{version}' -n 'convert an XML file' -o orcus-xml.1 %{buildroot}%{_bindir}/orcus-xml
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -p -m 0644 orcus-*.1 %{buildroot}/%{_mandir}/man1
%endif

# build documentation
make doc-doxygen

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make check %{?_smp_mflags}

%ldconfig_scriptlets

%if %{with convtools}
%ldconfig_scriptlets model
%endif

%files
%doc AUTHORS CHANGELOG
%license LICENSE
%{_libdir}/%{name}-%{apiversion}.so.*
%{_libdir}/%{name}-mso-%{apiversion}.so.*
%{_libdir}/%{name}-parser-%{apiversion}.so.*

%if %{with convtools}
%files model
%{_libdir}/%{name}-spreadsheet-model-%{apiversion}.so.*
%endif

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/%{name}-mso-%{apiversion}.so
%{_libdir}/%{name}-parser-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc
%if %{with convtools}
%{_libdir}/%{name}-spreadsheet-model-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-spreadsheet-model-%{apiversion}.pc
%endif

%files tools
%{_bindir}/orcus-css-dump
%{_bindir}/orcus-detect
%{_bindir}/orcus-json
%{_bindir}/orcus-mso-encryption
%{_bindir}/orcus-zip-dump
%{_bindir}/orcus-yaml
%if %{with convtools}
%{_bindir}/orcus-csv
%{_bindir}/orcus-gnumeric
%{_bindir}/orcus-ods
%{_bindir}/orcus-styles-ods
%{_bindir}/orcus-xls-xml
%{_bindir}/orcus-xlsx
%{_bindir}/orcus-xml
%{_mandir}/man1/orcus-csv.1*
%{_mandir}/man1/orcus-gnumeric.1*
%{_mandir}/man1/orcus-ods.1*
%{_mandir}/man1/orcus-xls-xml.1*
%{_mandir}/man1/orcus-xlsx.1*
%{_mandir}/man1/orcus-xml.1*
%endif

%if %{with python}
%files python3
%{python3_sitearch}/_orcus.so
%{python3_sitearch}/_orcus_json.so
%{python3_sitelib}/orcus
%endif

%files doc
%license LICENSE
%doc doc/_doxygen/html

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.17.2-3
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.17.2-2
- Rebuilt for Boost 1.78

* Wed Feb 02 2022 Caolán McNamara <caolanm@redhat.com> - 0.17.2-1
- Resolves: rhbz#2018620 Update to 0.17.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.16.1-9
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.16.1-7
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.16.1-5
- Rebuilt for Boost 1.75

* Tue Dec 08 2020 Caolán McNamara <caolanm@redhat.com> - 0.16.1-4
- fix build without libixion under rhel

* Wed Dec 02 2020 Caolán McNamara <caolanm@redhat.com> - 0.16.1-3
- build without libixion under rhel

* Mon Oct 19 2020 Jeff Law <law@redhat.com> - 0.16.1-2
- Fix missing headers for gcc-11

* Tue Sep 29 2020 Caolán McNamara <caolanm@redhat.com> - 0.16.1-1
- latest release

* Fri Sep 25 2020 Caolán McNamara <caolanm@redhat.com> - 0.16.0-3
- reenable make check

* Fri Sep 25 2020 Caolán McNamara <caolanm@redhat.com> - 0.16.0-2
- replace -DSIZEOF_VOID_P=4 with upstream solution

* Thu Sep 24 2020 Caolán McNamara <caolanm@redhat.com> - 0.16.0-1
- latest release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 0.15.3-5
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.15.3-4
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.3-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 02 2019 David Tardon <dtardon@redhat.com> - 0.15.3-1
- new upstream release

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.15.2-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Caolán McNamara <caolanm@redhat.com> - 0.15.2-1
- new upstream release

* Tue Aug 20 2019 Caolán McNamara <caolanm@redhat.com> - 0.15.0-1
- new upstream release

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 Stephan Bergmann <sbergman@redhat.com> - 0.14.1-4
- Replace hard-coded /usr/bin with _bindir macro for flatpak build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.14.1-2
- Rebuilt for Boost 1.69

* Fri Oct 26 2018 David Tardon <dtardon@redhat.com> - 0.14.1-1
- new upstream release

* Sun Sep 02 2018 David Tardon <dtardon@redhat.com> - 0.14.0-1
- new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13.4-2
- Rebuilt for Python 3.7

* Wed Feb 28 2018 David Tardon <dtardon@redhat.com> - 0.13.4-1
- new upstream release

* Sat Feb 17 2018 David Tardon <dtardon@redhat.com> - 0.13.3-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 David Tardon <dtardon@redhat.com> - 0.13.2-1
- new upstream release

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.13.1-2
- Rebuilt for Boost 1.66

* Mon Nov 20 2017 David Tardon <dtardon@redhat.com> - 0.13.1-1
- new upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.12.1-5
- Rebuilt for Boost 1.64

* Wed Feb 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.12.1-4
- Rebuild for brp-python-bytecompile

* Tue Feb 07 2017 Björn Esser <besser82@fedoraproject.org> - 0.12.1-3
- Rebuilt for Boost 1.63
- Fix build and directory ownership

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.12.1-2
- Rebuild for Python 3.6

* Thu Sep 29 2016 David Tardon <dtardon@redhat.com> - 0.12.1-1
- new upstream release

* Wed Jul 20 2016 David Tardon <dtardon@redhat.com> - 0.11.2-2
- rebuild for libixion 0.12

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar 14 2016 David Tardon <dtardon@redhat.com> - 0.11.1-1
- new upstream release

* Tue Mar 08 2016 David Tardon <dtardon@redhat.com> - 0.11.0-1
- new upstream release

* Sun Feb 14 2016 David Tardon <dtardon@redhat.com> - 0.9.2-4
- switch to new mdds and libixion

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.9.2-2
- Rebuilt for Boost 1.60

* Mon Oct 19 2015 David Tardon <dtardon@redhat.com> - 0.9.2-1
- rebase to the 0.9.x line

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Fri Jul 24 2015 Adam Williamson <awilliam@redhat.com> - 0.7.1-5
- rebuild for Boost 1.58 (for f23, for real this time)

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.7.1-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 David Tardon <dtardon@redhat.com> - 0.7.1-2
- rebuild for yet another C++ ABI break

* Wed Feb 25 2015 David Tardon <dtardon@redhat.com> - 0.7.1-1
- new upstream release

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.7.0-7
- include <iostream> in string_pool_test (liborcus-0.7.0-iostream.patch)

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.7.0-6
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 David Tardon <dtardon@redhat.com> - 0.7.0-3
- enable conversion tools

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.7.0-2
- Rebuild for boost 1.55.0

* Thu May 22 2014 David Tardon <dtardon@redhat.com> - 0.7.0-1
- new upstream release

* Mon May 05 2014 Jaromir Capik <jcapik@redhat.com> - 0.5.1-7
- add support for ppc64le

* Wed Jan 22 2014 David Tardon <dtardon@redhat.com> - 0.5.1-6
- add support for aarch64

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.5.1-4
- Rebuild for boost 1.54.0

* Mon Jun 10 2013 David Tardon <dtardon@redhat.com> - 0.5.1-3
- trivial changes

* Tue May 28 2013 David Tardon <dtardon@redhat.com> - 0.5.1-2
- build orcus-zip-dump too

* Mon May 06 2013 David Tardon <dtardon@redhat.com> - 0.5.1-1
- new release

* Fri Feb 15 2013 Stephan Bergmannn <sbergman@redhat.com> - 0.3.0-5
- missing boost include

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.3.0-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.3.0-3
- Rebuild for Boost-1.53.0

* Sat Dec 08 2012 David Tardon <dtardon@redhat.com> - 0.3.0-2
- a pointless release bump

* Fri Dec 07 2012 David Tardon <dtardon@redhat.com> - 0.3.0-1
- new release

* Sun Sep 09 2012 David Tardon <dtardon@redhat.com> - 0.1.0-1
- initial import
