Name:        vsqlite++
Version:    0.3.13
Release:    31%{?dist}
Summary:    Well designed C++ sqlite 3.x wrapper library

License:    BSD
URL:        http://vsqlite.virtuosic-bytes.com
Source0:    http://evilissimo.fedorapeople.org/releases/vsqlite--/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  boost-devel
BuildRequires:  sqlite-devel
BuildRequires:  libtool
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%package doc
BuildArch:      noarch
Summary:        Development documentation for %{name}

%description doc
This package contains development documentation files for %{name}.

%prep
%setup -q

%build
%configure
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
make %{?_smp_mflags}
doxygen Doxyfile

%install
# devel & base
install -p -m 755 -d %{buildroot}%{_libdir}
# devel only
install -p -m 755 -d %{buildroot}%{_includedir}/sqlite/ext
install -m 644 include/sqlite/*.hpp %{buildroot}%{_includedir}/sqlite
install -m 644 include/sqlite/ext/*.hpp %{buildroot}%{_includedir}/sqlite/ext
# docs
install -p -m 755 -d %{buildroot}%{_docdir}

# build for all
make DESTDIR=%{buildroot} install

%ldconfig_scriptlets

%files doc
%doc ChangeLog README COPYING examples/sqlite_wrapper.cpp html/*

%files devel
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite
# Don't add .la/.a to the package
%exclude %{_libdir}/libvsqlitepp.la
%exclude %{_libdir}/libvsqlitepp.a

%files
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so.*

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.13-21
- Added gcc-c++ and gcc build requires

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.13-16
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.13-15
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 0.3.13-13
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.3.13-12
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.3.13-10
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.13-8
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.3.13-7
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.13-4
- Changed the URL to the new project website

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.3.13-3
- Rebuild for boost 1.55.0

* Mon May 19 2014 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.13-2
- Removal of premake in BuildRequires

* Thu Apr 24 2014 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.13-1
- Update to upstream release vsqlite++-0.3.13

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.3.11-3
- Rebuild for boost 1.54.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.11-1
- Upstream version 0.3.11

* Fri Sep 28 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.9-3
- Documentation subpackage now noarch

* Wed Sep 26 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.9-2
- Removed comment with macro - Not needed anymore

* Tue Sep 25 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.9-1
- Updated to upstream vsqlite++-0.3.9
- Removing now obsolete ./autogen.sh call in prep
- Remove of unnecessary BuildRequires automake and autoconf
- Upstream renamed Changelog to ChangeLog - reflected changes
- Upstream renamed LICENSE to COPYING - reflected changes

* Tue Sep 25 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.7-2
- Fix for %%description spelling 'ibrary' => 'library'
- Fix for unused libm dependency
- Include Changelog, README and LICENSE to devel
- Removed TODO, VERSION
- Removed duplicated lines in the install sectin
- New doc sub package for the html documentation and code example
- Removed static package
- Removed unnecessary ldconfig call on devel package
- One BuildRequires entry per line

* Tue Sep 25 2012 Vinzenz Feenstra <evilissimo@gmail.com> - 0.3.7-1
- Initial package

