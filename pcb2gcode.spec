Name:		pcb2gcode
Version:	1.3.2
Release:	24%{?dist}
Summary:	Command-line software for the isolation, routing and drilling of PCBs

License:	GPLv3+
URL:		https://github.com/pcb2gcode/pcb2gcode/
Source0:	https://github.com/pcb2gcode/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Define-screen-symbol.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.8
BuildRequires:	pkgconfig(gdkmm-2.4) >= 2.8
BuildRequires:	pkgconfig(libgerbv) >= 2.1.0

%description
pcb2gcode is a command-line software for the isolation, routing and drilling of
PCBs. It takes Gerber files as input and it outputs gcode files, suitable for
the milling of PCBs. It also includes an Autoleveller, useful for the automatic
dynamic calibration of the milling depth.

%prep
%setup -q
%patch0 -p1


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%{_bindir}/pcb2gcode
%{_mandir}/man1/pcb2gcode.1*
%doc AUTHORS README.md
%license COPYING


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.3.2-23
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-21
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-18
- Rebuilt for Boost 1.75

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 1.3.2-17
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-15
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-11
- Rebuilt for Boost 1.69

* Wed Jan 09 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.3.2-10
- Hack to work with current gerbv

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-7
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Dec  4 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.2-1
- Initial packaging
