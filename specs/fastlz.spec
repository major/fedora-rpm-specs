# spec file for fastlz
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#

%global abi    0

Name:      fastlz
Summary:   Portable real-time compression library
Version:   0.5.0
Release:   2%{?dist}
License:   MIT
URL:       http://fastlz.org/

Source0:   https://github.com/ariya/FastLZ/archive/refs/tags/0.5.0.tar.gz

BuildRequires: gcc


%description
FastLZ is a lossless data compression library designed for real-time
compression and decompression. It favors speed over compression ratio.
Decompression requires no memory. Decompression algorithm is very simple,
and thus extremely fast.


%package devel
Summary:    Header files and development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}.


%prep
%setup -q -n FastLZ-%{version}


%build
# Build the shared library
gcc %optflags -fPIC -c fastlz.c  -o fastlz.o
gcc %optflags -fPIC -shared \
   -Wl,-soname -Wl,lib%{name}.so.%{abi} \
   -o lib%{name}.so.%{abi} fastlz.o
ln -s lib%{name}.so.%{abi} lib%{name}.so

# Build the commands for test
cd examples
gcc %optflags -fPIC 6pack.c   -I.. -L.. -l%{name} -o 6pack
gcc %optflags -fPIC 6unpack.c -I.. -L.. -l%{name} -o 6unpack


%install
install -D -m 0755 lib%{name}.so.%{abi} %{buildroot}%{_libdir}/lib%{name}.so.%{abi}
ln -s lib%{name}.so.%{abi} %{buildroot}%{_libdir}/lib%{name}.so
install -D -pm 0644 %{name}.h           %{buildroot}%{_includedir}/%{name}.h

# Don't install the commands, as we obviously don't need more compression tools


%check
export LD_LIBRARY_PATH=$PWD

cd examples
cp ../%{name}.c tmpin
./6pack -v
./6unpack -v

: Compress
./6pack -1 tmpin tmpout1
./6pack -2 tmpin tmpout2

: Uncompress 1
rm tmpin
./6unpack tmpout1
diff ../%{name}.c tmpin

: Uncompress 2
rm tmpin
./6unpack tmpout2
diff ../%{name}.c tmpin



%files
%license LICENSE.MIT
%{_libdir}/lib%{name}.so.%{abi}

%files devel
%doc README.md
%doc ChangeLog
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 16 2024 Remi Collet <remi@remirepo.net> - 0.5.0-1
- update to 0.5.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.23.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.22.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.21.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.20.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.19.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.18.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.17.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.16.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.15.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.14.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.13.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.12.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.11.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.10.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Remi Collet <remi@remirepo.net> - 0.1.0-0.9.20070619svnrev12
- missing BR on gcc

* Thu Feb 15 2018 Remi Collet <remi@remirepo.net> - 0.1.0-0.8.20070619svnrev12
- drop ldconfig scriptlets

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.7.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.6.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.5.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.4.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.3.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-0.2.20070619svnrev12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep  5 2014 Remi Collet <remi@fedoraproject.org> - 0.1-0.1.20070619svnrev12
- Initial RPM
