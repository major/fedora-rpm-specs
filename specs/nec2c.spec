Name:           nec2c
Version:        1.3.2
Release:        3%{?dist}
Summary:        Translation of NEC2 antenna modeling tool from FORTRAN to C

License:        GPL-3.0-only
URL:            https://github.com/KJ7LNW/nec2c
Source0:        https://github.com/KJ7LNW/nec2c/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        nec2c.1

BuildRequires:  autoconf automake make
BuildRequires:  gcc
# Should not be required but configure checks for it.
BuildRequires:  gcc-c++
%if ! 0%{?rhel}
BuildRequires:  help2man
%endif

%description
nec2c is a translation of the Numerical Electromagnetics Code (NEC2)
from FORTRAN to C. 

Operationally nec2c differs from NEC2 by being a command line
non-interactive program, taking as arguments the input file name
and optionally the output file name.


%prep
%autosetup


%build
autoreconf -fi
%configure
%make_install CFLAGS="%{optflags}"


%install
#skip make install and do manual install, it's just one file
install -D -m 0755 nec2c %{buildroot}%{_bindir}/nec2c

mkdir -p %{buildroot}%{_mandir}/man1
%if 0%{?rhel}
    install -pm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1
%else
    help2man -o %{buildroot}%{_mandir}/man1/%{name}.1 -h -h -v -v --no-discard-stderr -N %{buildroot}%{_bindir}/%{name}
%endif


%files
%doc AUTHORS README NEC2-bug.txt
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 02 2024 Richard Shaw <hobbes1069@gmail.com> - 1.3.2-1
- Update to 1.3.2.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Richard Shaw <hobbes1069@gmail.com> - 1.3-1
- Update to latest upstream release.

* Mon Aug 26 2013 Richard Shaw <hobbes1069@gmail.com> - 1.1-1
- Update to latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 19 2013 Richard Shaw <hobbes1069@gmail.com> - 0.9-1
- Update to latest upstream release.
- Add man page for nec2c.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 11 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 0.8-1
- New upstream release
- Fix some permissions to silent rpmlint

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.7-3
- Fix Patch0:/%%patch mismatch.

* Tue Jul 1 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.7-2
- Patch for ppc build

* Tue Jul 1 2008 Jef Spaleta <jspaleta AT fedoraproject DOT org> - 0.7-1
- new release 

* Thu Feb 14 2008 Steve Conklin <sconklin@redhat.com> - 0.6-3
- Rebuild for gcc4.3

* Sat Jan 26 2008 Robert 'Bob' Jensen <bob@bobjensen.com> - 0.6-2
- CFLAGS tweak per review

* Tue Dec 11 2007 Sindre Pedersen Bjørdal - 0.6-1
- Initial build
