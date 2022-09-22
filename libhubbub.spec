Name: libhubbub
Version: 0.3.7
Release: 6%{?dist}
Summary: An HTML5 compliant parsing library

License: MIT
URL: http://www.netsurf-browser.org/projects/hubbub/
Source: http://download.netsurf-browser.org/libs/releases/%{name}-%{version}-src.tar.gz

BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: netsurf-buildsystem
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(libparserutils)
BuildRequires: make

Patch0: 0001-do-not-use-deprecated-is_error.patch

%description
Hubbub is an HTML5 compliant parsing library, written in C. It was
developed as part of the NetSurf project.

The HTML5 specification defines a parsing algorithm, based on the
behavior of mainstream browsers, which provides instructions for how to
parse all markup, both valid and invalid. As a result, Hubbub parses web
content well.

Features:
* Parses HTML, good and bad
* Simple C API
* Fast
* Character encoding detection
* Well-tested (~90% test coverage)
* Portable

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

%global make_vars COMPONENT_TYPE=lib-shared PREFIX=/usr LIBDIR=%{_lib} Q=
%global build_vars OPTCFLAGS='%{optflags}' OPTLDFLAGS="$RPM_LD_FLAGS"

%prep
%autosetup -n %{name}-%{version} -p1

sed -i -e s@-Werror@@ Makefile

%build
make %{?_smp_mflags} %{make_vars} %{build_vars}
make %{?_smp_mflags} docs %{make_vars}

%install
make install DESTDIR=%{buildroot} %{make_vars}

%check
make %{?_smp_mflags} test %{make_vars} %{build_vars}

%files
%doc README
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/hubbub
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license COPYING
%doc docs/Architecture docs/Macros docs/Todo docs/Treebuilder docs/Updated
%doc docs/html

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 David Tardon <dtardon@redhat.com> - 0.3.7-1
- new upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 David Tardon <dtardon@redhat.com> - 0.3.6-1
- new upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 David Tardon <dtardon@redhat.com> - 0.3.4-1
- new upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 18 2016 David Tardon <dtardon@redhat.com> - 0.3.3-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 David Tardon <dtardon@redhat.com> - 0.3.1-1
- new upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 27 2014 David Tardon <dtardon@redhat.com> - 0.3.0-1
- new upstream release

* Mon Jan 13 2014 David Tardon <dtardon@redhat.com> - 0.2.0-3
- fix libhubbub.pc

* Wed Jan 08 2014 David Tardon <dtardon@redhat.com> - 0.2.0-2
- build with correct flags

* Wed Dec 25 2013 David Tardon <dtardon@redhat.com> - 0.2.0-1
- initial import
