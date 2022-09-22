%global __strip %{mingw32_strip}
%global __objdump %{mingw32_objdump}

%global shortname sigar

Name:		mingw-%{shortname}
Version:	1.6.5
Release:	0.28.git58097d9%{?dist}
Summary:	MinGW Windows sigar library

%global sigar_suffix  0-g4b67f57
%global sigar_hash    58097d9

License:	ASL 2.0
URL:		http://sigar.hyperic.com/

# Once 1.6.5 is released, we can use tarballs from GitHub:
#    Source0:	http://download.github.com/hyperic-sigar-{name}-{version}-{sigar_suffix}.tar.gz
#
# Until then the tarball can be re-generated with:
#    git clone git://github.com/hyperic/sigar.git
#    cd sigar
#    git archive --prefix=sigar-1.6.5/ 833ca18 | bzip2 > sigar-1.6.5-833ca18.tbz2
#
# The diff from 1.6.4 is too huge to contemplate cherrypicking from
Source0:	%{shortname}-%{version}-%{sigar_hash}.tbz2

BuildRequires:	mingw32-gcc cmake
BuildRequires:	redhat-rpm-config make
BuildRequires:	mingw32-filesystem

BuildArch:      noarch

%description
The Sigar API provides a portable interface for gathering system
information such as:
- System memory, swap, CPU, load average, uptime, logins
- Per-process memory, CPU, credential info, state, arguments,
  environment, open files
- File system detection and metrics
- Network interface detection, configuration info and metrics
- Network route and connection tables

This information is available in most operating systems, but each OS
has their own way(s) providing it. SIGAR provides developers with one
API to access this information regardless of the underlying platform.

#The core API is implemented in pure C with bindings currently
#implemented for Java, Perl and C#.


%package -n mingw32-%{shortname}
Summary:	MinGW Windows sigar library

%description -n mingw32-%{shortname}
The Sigar API provides a portable interface for gathering system
information such as:
- System memory, swap, CPU, load average, uptime, logins
- Per-process memory, CPU, credential info, state, arguments,
  environment, open files
- File system detection and metrics
- Network interface detection, configuration info and metrics
- Network route and connection tables

This information is available in most operating systems, but each OS
has their own way(s) providing it. SIGAR provides developers with one
API to access this information regardless of the underlying platform.

#The core API is implemented in pure C with bindings currently
#implemented for Java, Perl and C#.


%prep
# When using the GitHub tarballs, use:
# setup -q -n hyperic-{shortname}-{sigar_hash}
%setup -q -n %{shortname}-%{version}

%build
PATH=%{mingw32_bindir}:$PATH

mkdir build
pushd build
%{mingw32_cmake} ..
make %{?_smp_mflags}
popd

%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

%files -n mingw32-%{shortname}
%doc ChangeLog README LICENSE NOTICE AUTHORS
%{mingw32_bindir}/libsigar.dll
%{mingw32_libdir}/libsigar.dll.a
%{mingw32_includedir}/sigar*.h

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.28.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.27.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.26.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.25.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.24.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.23.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.6.5-0.22.git58097d9
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.21.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.20.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.19.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.18.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.17.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.16.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-0.15.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-0.14.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-0.13.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 30 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.5-0.12.git58097d9
- Rebuild against latest mingw-crt to fix Windows XP compatibility issue

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-0.11.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-0.10.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-0.9.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.6.5-0.8.git58097d9
- Renamed the source package to mingw-sigar (#801029)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.6.5-0.7.git58097d9
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-0.6.git58097d9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Adam Stokes <astokes@fedoraproject.org> - 1.6.5-0.5.git58097d9
- New upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-0.4.git833ca18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 21 2010 Andrew Beekhof <andrew@beekhof.net> - 1.6.5-0.3.git833ca18
- Minor tweaks before import: summary and use of spaces

* Wed Dec 21 2010 Andrew Beekhof <andrew@beekhof.net> - 1.6.5-0.2.git833ca18
- Incorporate review feedback, include dependencies generator macro

* Wed Dec 1 2010 Andrew Beekhof <andrew@beekhof.net> - 1.6.5-0.1.git833ca18
- Initial checkin
