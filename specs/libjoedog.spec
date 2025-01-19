%global _hardened_build 1
%global libname joedog
%global current 0

Name:           lib%{libname}
Version:        %{current}.1.2
Release:        27%{?dist}
Summary:        Repack of the common code base of fido and siege as shared library

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.%{libname}.org/
Source0:        https://github.com/rmohr/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: libjoedog-c99.patch

%{?el5:BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildRequires:  libtool
BuildRequires: make

%description
%{name} is a library containing the common code base of siege and fido by Jeff
Fulmer. It consists mostly of convenience wrapper functions and a hash table
implementation.


%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}


%prep
%autosetup -p1
# old autotools want m4-dir to be present
mkdir -p m4
autoreconf -fi


%build
%configure --disable-static
# dirty hack to force immediate binding with hardenend build having
# autocrap's libtool pass the needed ld-specs to the linker.
sed -i -e 's! \\\$compiler_flags !&%{?_hardening_ldflags} !' libtool
make %{?_smp_mflags}


%install
%if 0%{?el5}
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%else
%make_install
%endif

install -Dpm 0644 config.h %{buildroot}%{_includedir}/%{libname}
rm -f %{buildroot}%{_libdir}/%{name}.la



%ldconfig_scriptlets


%files
%doc README ChangeLog COPYING
%{_libdir}/%{name}.so.%{current}
%{_libdir}/%{name}.so.%{version}


%files devel
%{_includedir}/%{libname}
%{_libdir}/%{name}.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.2-26
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Florian Weimer <fweimer@redhat.com> - 0.1.2-21
- Port to C99

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Roman Mohr <roman@fenkhuber.at> - 0.1.2-1
- adding new macros for upstream siege 3.0.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.1-4
- changed %%_hardening_ldflags to %%{?_hardening_ldflags}
  Will now expand to {NULL} if not defined
- fixes build on rhel <= 6

* Thu Jun 27 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.1-3
- force libtool to pass %%_hardening_ldflags during linkage, only,
  instead of full ${C,LD}FLAGS

* Wed Jun 26 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.1-2
- install config.h in package, since it's needed for includes

* Wed Jun 26 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.1-1
- new upstream-version
- fixes build for el5
- force libtool to use all hardening-flags

* Mon Jun 24 2013 Roman Mohr <roman@fenkhuber.at> - 0.1.0-2
- fixed as proposed in bz #977367 comment 2
- enabled hardened build, trimmed BuildRequires, added Group for el5
- replaced hardcoded name with %%{name}, added %%{libname}
- some clean-ups and improvement of readabilty
- moving source to github

* Sun Jun 23 2013 Roman Mohr <roman@fenkhuber.at> - 0.1.0-1
- initial release
