# We keep track manually of the library version
%global liblongver 0.0.0
%global libshortver 0

Name:           cmpfit
Version:        1.5
Release:        7%{?dist}
Summary:        A MINPACK-1 Least Squares Fitting Library in C

License:        BSD-2-Clause-FreeBSD
URL:            http://cow.physics.wisc.edu/~craigm/idl/cmpfit.html
Source0:        http://cow.physics.wisc.edu/~craigm/idl/down/%{name}-%{version}.tar.gz

BuildRequires:  gcc

%description
CMPFIT uses the Levenberg-Marquardt technique to solve the least-squares 
problem. In its typical use, CMPFIT will be used to fit a user-supplied 
function (the "model") to user-supplied data points (the "data") by adjusting 
a set of parameters. CMPFIT is based upon MINPACK-1 (LMDIF.F) by More' and 
collaborators. 

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release} 

%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%prep
%setup -q

%build
# Manual build, makefile only does static library
gcc %{optflags} -fpic -c -o mpfit.o mpfit.c
gcc -shared -Wl,-soname,libmpfit.so.%{libshortver} -o libmpfit.so.%{liblongver} mpfit.o -lm

%install
mkdir -p  %{buildroot}/%{_includedir}
mkdir -p  %{buildroot}/%{_libdir}

cp mpfit.h %{buildroot}/%{_includedir}
cp libmpfit.so.%{liblongver} %{buildroot}/%{_libdir}
pushd %{buildroot}/%{_libdir}
ln -s libmpfit.so.%{liblongver} libmpfit.so.%{libshortver}
ln -s libmpfit.so.%{liblongver} libmpfit.so
popd

%files
%doc README DISCLAIMER
%{_libdir}/libmpfit.so.%{liblongver}
%{_libdir}/libmpfit.so.%{libshortver}

%files devel
%{_includedir}/mpfit.h
%{_libdir}/libmpfit.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.5-1
- Update to version 1.5
- Switch to SPDX license identifier

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.4-1
- Update to version 1.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3a-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3a-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 10 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3a-1
- Update to version 1.3a

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2-5
- Reverted patch

* Thu Jun 05 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2-4
- Correct patch added

* Thu Jun 05 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2-3
- Updating package to version available from fityk github repo
- update obtained via email from original author of mpfit by fityk devel
- Added patch from Marcin Wojdyr (fityk github repo)

* Fri Mar 07 2014 Sergio Pascual <sergiopr at fedoraproject.org> - 1.2-2
- Add license in DISCLAIMER
- Update requires in cmpfit-devel

* Fri Aug 16 2013 Sergio Pascual <sergiopr at fedoraproject.org> - 1.2-1
- Initial spec
