Name:		libzdnn
Version:	1.0.1
Release:	6%{?dist}
Summary:	Driver library for the IBM Z Neural Network Processing Assist Facility

License:	Apache-2.0
Url:		https://github.com/IBM/zDNN
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:	s390x
BuildRequires:	gcc
BuildRequires:	g++
BuildRequires:	make
BuildRequires:	gawk
BuildRequires:	automake
BuildRequires:	autoconf
	
# Be explicit about the soversion in order to avoid unintentional changes.
%global soversion 0

%description
The zDNN library provide a user space API for exploitation of the
Neural Network Processing Assist Facility.  All application which
intend to use that facility on IBM Z are supposed to do this via this
library.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package	static
Summary:	Static library version %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description    static
The %{name}-static package contains the static library of %{name}.


%prep
%autosetup -p1 -n zDNN-%{version}
autoreconf -i

%build
# libzdnn needs to be built with z14 support so override the distro wide options to append -march=z14.
# cflags for the init routines in e.g. zdnn_init.c should just use the distro options.
# export CFLAGS_INIT explicitely since it is not handled by configure
CFLAGS_INIT="%{build_cflags}"; export CFLAGS_INIT; CFLAGS="%{build_cflags} -march=z14 -mtune=z14" CXXFLAGS="%{build_cxxflags} -march=z14 -mtune=z14" %configure
%make_build build

%install
%make_install
mv $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{soversion} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version}
ln -s -r $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{soversion}

rm -f $RPM_BUILD_ROOT%{_libdir}/libzdnn.so
ln -s -r $RPM_BUILD_ROOT%{_libdir}/libzdnn.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libzdnn.so


%files
%{_libdir}/libzdnn.so.%{version}
%{_libdir}/libzdnn.so.%{soversion}
%doc README.md
%license LICENSE

%files devel
%{_includedir}/zdnn.h
%{_libdir}/*.so

%files static
%{_libdir}/libzdnn.a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 1 2023 Andreas Krebbel <krebbel@linux.ibm.com> - 1.0.1-1
- New release.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Andreas Krebbel <krebbel@linux.ibm.com> - 0.4.0-1
- New release.
- Remove: libzdnn-cflags_init.patch
- Remove: libzdnn-symbol_check.patch
- Remove: libzdnn-makedeps_fix.patch

* Fri Oct 29 2021 Andreas Krebbel <krebbel@linux.ibm.com> - 0.3.1-6
- Include libzdnn-makedeps_fix.patch.

* Thu Oct 21 2021 Andreas Krebbel <krebbel@linux.ibm.com> - 0.3.1-5
- Include libzdnn-symbol_check.patch.

* Tue Oct 19 2021 Andreas Krebbel <krebbel@linux.ibm.com> - 0.3.1-4
- Add missing blank in the description of the static package.
- Add build dependency for g++ for the initializer.cpp file.
- Make devel dependency on the main package arched.
- Change the dependency in the static package to devel and make it arched.

* Thu Oct 7 2021 Andreas Krebbel <krebbel@linux.ibm.com> - 0.3.1-3
- Add -mtune=z14 to override flags.
- Fix changelog formatting

* Sat Oct 2 2021 Andreas Krebbel <krebbel@linux.ibm.com> - 0.3.1-2
- Add proper source path.
- Add -n parameter to autosetup to deal with the different top-level
  dirname in the github created tarballs.
- Mention zdnn.h explicitely in the files section
- Include libzdnn-cflags_init.patch and pass CFLAGS_INIT to configure.

* Fri Sep 24 2021 Andreas Krebbel <krebbel@linux.ibm.com> - 0.3.1-1
- Initial version based on an IBM internal version provided by Stefan
  Liebler <stli@linux.ibm.com>
