%global commit b82360a98f49ea6cefbd6c08ede6f16231bd6522
%global shortcommit %(c=%{commit}; echo ${c:0:12}) 

Name:           dataquay
Version:        0.9.1
Release:        11.20190227git%{shortcommit}%{?dist}
Summary:        Simple RDF for C++ and Qt applications

# README says BSD but this is more similar to MIT text
License:        MIT
URL:            https://www.breakfastquay.com/dataquay/
Source0:        https://bitbucket.org/breakfastquay/dataquay/get/%{commit}.tar.bz2#/%{name}-%{shortcommit}.tar.bz2

BuildRequires:  qt-devel
BuildRequires:  redland-devel
BuildRequires:  Xvfb xauth
BuildRequires: make
#Requires:       

%description
Dataquay is a free open source library that provides a friendly C++
interface to an RDF datastore using Qt4 classes and
containers. Supported datastores are the popular and feature-complete
Redland and the lightweight Sord.

Dataquay is simple to use and easy to integrate. It is principally
aimed at Qt-based applications that would like to use an RDF datastore
as backing for in-memory project data, to avoid having to invent file
formats or XML schemas and to make it easy to augment the data with
descriptive metadata pulled in from external sources. It's also useful
for applications with ad-hoc needs for metadata management using RDF
sources.

Dataquay does not use a separate database, instead using in-memory
storage with separate file import and export facilities. Although it
offers a choice of datastore implementations, the choice is made at
compile time: there is no runtime module system to take into account
when deploying your application.

The Fedora package is configured to use Redland, as recommended by the
developers for general use.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       redland-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n breakfastquay-dataquay-%{shortcommit}
# patch for multilib
%{__sed} -i.multilib 's|$${PREFIX}/lib|$${PREFIX}/%{_lib}|' lib.pro
%{__sed} -i.multilib 's|${exec_prefix}/lib|${exec_prefix}/%{_lib}|' \
         deploy/dataquay.pc.in


%build
%{qmake_qt4} dataquay.pro PREFIX=%{_prefix}
xvfb-run -a -w 1 make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}
# actually copy .pc file
%{__cp} -p deploy/dataquay.pc %{buildroot}%{_libdir}/pkgconfig/
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%doc CHANGELOG README.txt
%{_libdir}/*.so.*

%files devel
%doc examples
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2.20190227gitb82360a98f49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Michel Alexandre Salim <michel@lumiere.local> - 0.9.1-1.20190227gitb82360a98f49
- Update to 0.9.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul  4 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.9-12
- Explicitly use GNU++98 standard
- Use license macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9-10
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9-8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  2 2012 Michel Salim <salimma@fedoraproject.org> - 0.9-3
- Make -devel subpackage pull in pkgconfig(redland) as well

* Tue Oct  9 2012 Michel Salim <salimma@fedoraproject.org> - 0.9-2
- Add note with workaround for building in mock for bug #857709

* Sun Sep 16 2012 Michel Salim <salimma@fedoraproject.org> - 0.9-1
- Initial package

