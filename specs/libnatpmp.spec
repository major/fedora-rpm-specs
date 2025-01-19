Name:           libnatpmp
Version:        20230423
Release:        7%{?dist}
Summary:        Library of The NAT Port Mapping Protocol (NAT-PMP)
License:        LGPL-2.0-or-later
URL:            http://miniupnp.free.fr/libnatpmp.html
Source0:        http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: make
%description
libnatpmp is an attempt to make a portable and fully compliant implementation
of the protocol for the client side. It is based on non blocking sockets and
all calls of the API are asynchronous. It is therefore very easy to integrate
the NAT-PMP code to any event driven code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%make_build CFLAGS="-fPIC -Wall -DENABLE_STRNATPMPERR %{optflags}" EXTRA_LD="%{?__global_ldflags}"

%install
make install INSTALL="install -p" PREFIX=%{buildroot} \
     INSTALLDIRLIB="%{buildroot}%{_libdir}" \
     INSTALLDIRINC="%{buildroot}%{_includedir}" \
     INSTALLDIRBIN="%{buildroot}%{_bindir}"

install -m 0644 -p natpmp_declspec.h %{buildroot}%{_includedir}/

find %{buildroot} -name '*.a' -delete -print
find %{buildroot} -name '*.so' -exec chmod 755 {} ";" -print

%check
make testgetgateway
./testgetgateway

%ldconfig_scriptlets

%files
%license LICENSE
%{_bindir}/natpmpc
%{_libdir}/*.so.*

%files devel
%doc Changelog.txt README
%{_libdir}/*.so
%{_includedir}/natpmp.h
%{_includedir}/natpmp_declspec.h

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20230423-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230423-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230423-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230423-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230423-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 22 2023 Gwyn Ciesla <gwync@protonmail.com> - 20230423-2
- Include natpmp_declspec.h

* Mon Apr 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 20230423-1
- 20230423

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 20150609-18
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug  9 2018 Owen Taylor <otaylor@redhat.com> - 20150609-8
- Fix to properly install into %{_bindir} / %{_includedir}

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150609-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 22 2015 Christopher Meng <rpm@cicku.me> - 20150609-1
- Update to 20150609

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140401-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140401-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Christopher Meng <rpm@cicku.me> - 20140401-1
- Update to 20140401

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131126-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Christopher Meng <rpm@cicku.me> - 20131126-2
- Correct the permissions to get useful debuginfo packages.

* Thu Jan 02 2014 Christopher Meng <rpm@cicku.me> - 20131126-1
- Update to 20131126
- Append proper CFLAGS to make.

* Wed Sep 11 2013 Christopher Meng <rpm@cicku.me> - 20130911-1
- Update to 20130911

* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 20120821-1
- Initial Package.
