
## global prerelease	201412181500

Summary:	Free, simple and portable asynchronous resolver library
Name:		libasr
Version:	1.0.4
Release:	8%{?prerelease:.%{prerelease}}%{?dist}

License:	BSD
URL:		https://github.com/OpenSMTPD/libasr

%if 0%{?prerelease}
Source0:	http://www.opensmtpd.org/archives/%{name}-%{prerelease}.tar.gz
%else
Source0:	http://www.opensmtpd.org/archives/%{name}-%{version}.tar.gz
%endif

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libevent-devel
%if 0%{?el7}
BuildRequires:	openssl11-devel
%else
BuildRequires:	openssl-devel
%endif

%description
Libasr allows to run DNS queries and perform hostname resolutions in a fully
asynchronous fashion. The implementation is thread-less, fork-less, and does not
make use of signals or other "tricks" that might get in the developer's way.
The API was initially developed for the OpenBSD operating system, where it is
natively supported.

This library is intended to bring this interface to other systems. It is
originally provided as a support library for the portable version of the
OpenSMTPD daemon, but it can be used in any other contexts.


%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and libraries for developing
with %{name}.


%prep
%setup -q %{?prerelease: -n %{name}-%{prerelease}}

%build
%configure \
	--enable-shared \
	--disable-static \
	--with-mantype=man

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
chmod 0755 %{buildroot}%{_libdir}/libasr.so.*
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets


%files
%doc ChangeLog README.md
%license LICENCE
%{_libdir}/libasr.so.*


%files devel
%{_includedir}/asr.h
%{_libdir}/libasr.so


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 17 2020 Denis Fateyev <denis@fateyev.com> - 1.0.4-4
- Rebuild for libevent soname change

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Denis Fateyev <denis@fateyev.com> - 1.0.4-2
- Rebuilt for epel7 compatibility

* Thu Jan 30 2020 Denis Fateyev <denis@fateyev.com> - 1.0.4-1
- Update to 1.0.4 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Denis Fateyev <denis@fateyev.com> - 1.0.2-11
- Spec cleanup from deprecated items

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Denis Fateyev <denis@fateyev.com> - 1.0.2-1
- Update to 1.0.2 release

* Mon Feb 02 2015 Denis Fateyev <denis@fateyev.com> - 1.0.1-1
- Update to 1.0.1 release

* Sun Dec 21 2014 Denis Fateyev <denis@fateyev.com> - 1.0.0-1
- Initial Fedora RPM release
