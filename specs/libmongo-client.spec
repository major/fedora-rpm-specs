Name:		libmongo-client
Version:	0.1.8
Release:	26%{?dist}
Summary:	Alternative C driver for MongoDB

License:	Apache-2.0
URL:		https://github.com/algernon/libmongo-client
Source0:	%{name}-%{version}.tar.gz
# wget https://github.com/algernon/libmongo-client/archive/libmongo-client-%{version}.tar.gz
# source obtained from https://github.com/algernon/libmongo-client/tags
# tar xfz libmongo-client-%{version}.tar.gz
# mv libmongo-client-libmongo-client-%{version} libmongo-client-%{version}
# tar czf libmongo-client-%{version}.tar.gz libmongo-client-%{version}

BuildRequires: libtool
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: glib2-devel

%package devel
Summary: Development files for libmongo-client
Requires: %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary: Documentation for libmongo-client
%{?fedora:BuildArch: noarch}
BuildRequires: graphviz
BuildRequires: doxygen
BuildRequires: make

%description
Alternative C driver for MongoDB. Libmongo-client is meant
to be a stable (API, ABI and quality alike), clean, well documented
and well tested shared library, that strives to make the most
common use cases as convenient as possible.

%description devel
Development files (libraries and include files) for libmongo-client

%description doc
Subpackage contains documentation for libmongo-client

%prep
%setup -q

%build
autoreconf -i
%configure --disable-static
make %{?_smp_mflags}
make doxygen


%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}/%{_libdir}/*.{a,la}


%ldconfig_scriptlets


%files
%doc LICENSE NEWS README.md
%{_libdir}/libmongo-client.so.*


%files devel
%{_libdir}/pkgconfig/libmongo-client.pc
%{_libdir}/libmongo-client.so
%{_includedir}/mongo-client

%files doc
%doc docs/html


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Attila Lakatos <alakatos@redhat.com> - 0.1.8-21
- Migrate to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.8-10
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Radovan Sroka <rsroka@redhat.com> - 0.1.8-5
- import srpm from f25
- this package was dead, but we need this for rsyslog mongodb module

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 31 2014 Peter Czanik <czanik@balabit.hu> - 0.1.8-1
- upadte to 0.1.8

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.7.1-1
- update to 0.1.7.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov  5 2012 Milan Bartos <mbartos@redhat.com> - 0.1.6.1-1
- update to 0.1.6.1

* Mon Oct  8 2012 Milan Bartos <mbartos@redhat.com> - 0.1.5-6
- includedir mongo-client owned by -devel subpackage

* Wed Oct  3 2012 Milan Bartos <mbartos@redhat.com> - 0.1.5-5
- added dependencies for autogen.sh

* Wed Oct  3 2012 Milan Bartos <mbartos@redhat.com> - 0.1.5-4
- changed documentation location as standalone subpackage

* Wed Oct  3 2012 Milan Bartos <mbartos@redhat.com> - 0.1.5-3
- added documentation to devel subpackage

* Tue Oct  2 2012 Milan Bartos <mbartos@redhat.com> - 0.1.5-2
- added %%{?_isa} to Requires for devel subpackage

* Wed Sep 26 2012 Milan Bartos <mbartos@redhat.com> - 0.1.5-1
- initial port

