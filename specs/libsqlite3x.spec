%global veryear 2007
%global vermon  10
%global verday  18
%global namesq3 libsq3
Name:           libsqlite3x
Version:        %{veryear}%{vermon}%{verday}
Release:        38%{?dist}
Summary:        A C++ Wrapper for the SQLite3 embeddable SQL database engine

# fix license tag: https://bugzilla.redhat.com/show_bug.cgi?id=491618
License:        zlib
URL:            http://www.wanderinghorse.net/computing/sqlite/
Source0:        http://www.wanderinghorse.net/computing/sqlite/%{name}-%{veryear}.%{vermon}.%{verday}.tar.gz
Source1:        libsqlite3x-autotools.tar.gz
Patch1:         libsqlite3x-prep.patch
Patch2:         libsqlite3x-includes.patch

BuildRequires:  sqlite-devel dos2unix automake libtool doxygen gcc-c++
BuildRequires: make

%description
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sqlite3x is a C++ wrapper API for working
with sqlite3 databases that uses exceptions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       sqlite-devel pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     %{namesq3}
Summary:        A C++ Wrapper for the SQLite3 embeddable SQL database engine
Requires:       %{namesq3} = %{version}-%{release}

%description -n %{namesq3}
sqlite3 is a slick embedded SQL server written in C. It's easy to use,
powerful, and quite fast. sq3 is a C++ wrapper API for working
with sqlite3 databases that does not use exceptions.

%package -n     %{namesq3}-devel
Summary:        Development files for %{name}
Requires:       %{namesq3} = %{version}-%{release}
Requires:       sqlite-devel pkgconfig

%description -n %{namesq3}-devel
The %{namesq3}-devel package contains libraries and header files for
developing applications that use %{namesq3}.

%prep
%setup -q -n %{name}-%{veryear}.%{vermon}.%{verday} -a 1
dos2unix *.hpp *.cpp
%patch -P1 -p0 -b .prep
%patch -P2 -p0 -b .incl

iconv -f iso8859-1 -t utf-8  <README >R && mv R README

%build
aclocal
libtoolize -f
autoheader
autoconf
automake -a -c
%configure --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make
make doc
make doc-sq3

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%ldconfig_scriptlets -n %{namesq3}

%files
%doc AUTHORS Doxygen-index.txt
%{_libdir}/libsqlite3x.so.*

%files devel
%doc README doc/html
%{_includedir}/sqlite3x
%{_libdir}/libsqlite3x.so
%{_libdir}/pkgconfig/libsqlite3x.pc

%files -n %{namesq3}
%doc AUTHORS Doxygen-index.txt
%{_libdir}/libsq3.so.*

%files -n %{namesq3}-devel
%doc README doc-sq3/html
%{_includedir}/sq3
%{_libdir}/libsq3.so
%{_libdir}/pkgconfig/libsq3.pc

%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-24
- rebuild
- add gcc-c++ BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20071018-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20071018-17
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-9
- conform to licensing guide update

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-7
- fix license tag

* Thu Apr 16 2009 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-6
- replace %%define with %%global

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-4
- separate sq3 and sqlite3x into separate binary packages
- add unused-direct-shlib-dependency build quirk
- add missing dependency

* Fri May 16 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-3
- add cstring includes for strlen prototypes

* Sat Mar 22 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-2
- add autotools based build system

* Sat Mar 22 2008 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20071018-1
- update

* Thu Aug  2 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20070214-1
- update

* Thu Jan  4 2007 Thomas Sailer <t.sailer@alumni.ethz.ch> - 20060929-1
- Initial build
