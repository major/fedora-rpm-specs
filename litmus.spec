Name:		litmus
Version:	0.14
Release:	1%{?dist}
Summary:	WebDAV server compliance test suite
License:	GPLv2+
URL:		https://notroj.github.io/litmus/
Source0:	https://notroj.github.io/litmus/litmus-0.14.tar.gz
BuildRequires:  gcc, automake, make
BuildRequires:	neon-devel

%description
litmus is a WebDAV server test suite, which aims to test whether a server is 
compliant with the WebDAV protocol as specified in RFC2518.

%prep
%setup -q -n %{name}-%{version}

# Making sure we use system libs, not bundled ones
find neon/src -name '*.c' -o -name '*.h' | xargs rm -rf

%build
%configure --with-neon=%{_prefix}

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

%files
%{_bindir}/litmus
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%doc COPYING FAQ README.md THANKS TODO

%changelog
* Mon Jan 30 2023 Joe Orton <jorton@redhat.com> - 0.14-1
- update to 0.14

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Joe Orton <jorton@redhat.com> - 0.13-28
- update for neon 0.32 (#2046709)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Joe Orton <jorton@redhat.com> - 0.13-22
- update for neon 0.31

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 30 2013 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 0.13-9
- Patched litmus to build with Neon 0.30
- Run autogen.sh to re-generate the configure scripts
- Fixes https://bugzilla.redhat.com/show_bug.cgi?id=992143

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.13-4
- Removed data dir cleanup, files are needed at runtime (bug #800477)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.13-3
- Fixed prefix usage in configure
- Drop bundled libraries to make sure we use the system ones

* Tue Dec 13 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.13-2
- Proper use of configure macro
- Added comment on i18n patch
- Consistent use of buildroot macro

* Fri Dec 09 2011 Ricardo Rocha <ricardo.rocha@cern.ch> - 0.13-1
- Initial build
