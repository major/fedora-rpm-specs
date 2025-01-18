%define __cmake_in_source_build 1
%global __soversion 2.0

Name:		biblesync
Version:	2.1.0
Release:	13%{?dist}
Summary:	A Cross-platform library for sharing Bible navigation

License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.xiphos.org
Source0:	https://github.com/karlkleinpaste/biblesync/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	libuuid-devel
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires: make

%description
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libuuid-devel%{?_isa}

%description devel
This package contains libraries and header files for developing applications
that use %{name}.

%prep
%setup -q


%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC"
mkdir build
pushd build
%cmake -DLIBDIR=%{_libdir} .. -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" -DBIBLESYNC_SOVERSION=%{__soversion}
make %{?_smp_mflags}
popd


%install
pushd build
make install DESTDIR=%{buildroot}
popd

%files
%doc LICENSE
%{_libdir}/libbiblesync.so.%{__soversion}

%files devel
%doc AUTHORS COPYING ChangeLog README.md WIRESHARK
%{_includedir}/biblesync
%{_libdir}/pkgconfig/biblesync.pc
%{_libdir}/libbiblesync.so
%{_mandir}/man7/biblesync.7*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Oct 12 2020 Jeff Law <law@redhat.com> - 2.1.0-4
- Use __cmake_in_source_build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Greg Hellings <greg.hellings@gmail.com> - 2.1.0-1
- Upstream version 2.1.0
- Remove pkgconfig file patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Greg Hellings <greg.hellings@gmail.com> - 2.0.1-3
- Patching pkgconfig file

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Gregory Hellings <greg.hellings@gmail.com> - 2.0.1-1
- Upstream version 2.0.1
- Update Source URL to github location

* Sun Feb 18 2018 Gregory Hellings <greg.hellings@gmail.com> - 1.1.2-11
- Removed post/postun scriptlets per F28+ change

* Sun Feb 18 2018 Gregory Hellings <greg.hellings@gmail.com> - 1.1.2-10
- Added gcc/g++ deps for new dependency rules

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Greg Hellings <greg.hellings@gmail.com> - 1.1.2-5
- Adapted patch from Ville Skyttä <ville.skytta@iki.fi>
- Don't discard $RPM_OPT_FLAGS when adding fPIC

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Greg Hellings <greg.hellings@gmail.com> - 1.1.2-2
- Added fPIC

* Tue Dec 9 2014 Greg Hellings <greg.hellings@gmail.com> - 1.1.2-1
- New upstream version
- API incompatible with 1.0 series

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 04 2014 Greg Hellings <greg.hellings@gmail.com> - 1.0.2-4
- Final import form

* Sat Jul 19 2014 Greg Hellings <greg.hellings@gmail.com> - 1.0.2-3
- Package review feedback

* Mon Jul 07 2014 Greg Hellings <greg.hellings@gmail.com> - 1.0.2-2
- Initial build
