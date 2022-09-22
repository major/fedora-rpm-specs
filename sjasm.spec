Name:           sjasm
Version:        0.39
Release:        0.32.g1%{?dist}
Summary:        A z80 cross assembler
License:        BSD
# Upstream no longer appears to exist
URL:            http://www.xl2s.tk
Source0:        %{name}39g1.zip
Patch0:         sjasm-0.39-fixmakefile.patch
Patch1:         sjasm-0.39-64bitfix.patch
BuildRequires: make
BuildRequires:  gcc-c++


%description
SjASM is a two pass macro Z80 cross assembler


%prep
%setup -qcn %{name}-%{version}
%patch0 -p0
%patch1 -p0
sed -i 's/\r//' %{name}.txt

# Convert to UTF8
iconv -f iso8859-1 %{name}.txt -t utf8 > %{name}.txt.conv \
    && /bin/mv -f %{name}.txt.conv %{name}.txt


%build
make -C sjasmsrc039g1 %{?_smp_mflags} CXXFLAGS="%{optflags} -DMAX_PATH=MAXPATHLEN"


%install
rm -rf %{buildroot}
make -C sjasmsrc039g1 install DESTDIR=%{buildroot}



%files
%{_bindir}/%{name}
%doc %{name}.txt


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.32.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.31.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.30.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.29.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.28.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.27.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.26.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.25.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.24.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.23.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.22.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.21.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.20.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-0.19.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.18.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.39-0.17.g1
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.16.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.15.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.14.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.13.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.12.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.11.g1
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.10.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.9.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.8.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-0.7.g1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.39-0.6.g1
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Ian Chapman <packages@amiga-hardware.com> 0.39-0.5.g1
- Release bump for F8 mass rebuild
- Converted sjasm.txt to UTF8
- Corrected license

* Mon Aug 28 2006 Ian Chapman <packages@amiga-hardware.com> 0.39-0.4.g1
- Release bump for FC6 mass rebuild

* Sun Aug 20 2006 Ian Chapman <packages@amiga-hardware.com> 0.39-0.3.g1
- Bump release in preparation for FE migration

* Sat Aug 12 2006 Ian Chapman <packages@amiga-hardware.com> 0.39-0.2.g1
- Added patch for compiling on 64bit systems

* Fri Aug 11 2006 Ian Chapman <packages@amiga-hardware.com> 0.39-0.1.g1
- Initial Release
