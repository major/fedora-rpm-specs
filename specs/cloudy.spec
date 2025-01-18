Name: cloudy
Version: 17.03
Release: 11%{?dist}
Summary: Spectral synthesis code to simulate conditions in interstellar matter


License: Zlib
URL: http://www.nublado.org/
Source0: http://data.nublado.org/cloudy_releases/c17/c%{version}.tar.gz
Patch0: cloudy-make.patch

BuildRequires: gcc-c++
BuildRequires: perl-generators
BuildRequires: make

Requires: %{name}-data = %{version}-%{release}

%description
Most of the quantitative information we have about the cosmos comes from 
spectroscopy. In many cases the light we analyze was produced by atoms in 
the first generations of stars and galaxies.  The spectra are produced by 
dilute gas where such properties as the gas kinetic temperature, chemical 
state, level of ionization, and level populations, are determined by a 
host of microphysical processes rather than by a single temperature. 
Analytical solutions are seldom possible and computer solutions are 
needed to understand their physical properties. Numerical simulations make 
it possible to understand complex physical environments starting from 
first principles. Cloudy is designed to do exactly this.

%package data
Summary: data %{name}
BuildArch: noarch
 
%description data
This package contains the atomic data for %{name}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
 
%description doc
This package contains the usage documentation for %{name}.

%prep
%autosetup -n c%{version} -p1

%build
cd source
make %{?_smp_mflags} CXX="%{__cxx}" CXXFLAGS="%{optflags}" \
    CLOUDY_DATA_PATH=%{_datadir}/%{name}/data/

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/scripts
mkdir -p %{buildroot}/%{_datadir}/%{name}/grain
install -m 755 source/cloudy.exe %{buildroot}/%{_bindir}/cloudy
cp -a data/ %{buildroot}/%{_datadir}/%{name}/
rm -rf %{buildroot}/%{_datadir}/%{name}/data/cdms+jpl/convert_calpgm
rm -rf %{buildroot}/%{_datadir}/%{name}/data/cdms+jpl/convert_calpgm.cpp
rm -rf %{buildroot}/%{_datadir}/%{name}/data/cdms+jpl/.gitignore

%check
echo "test" > test.in
export CLOUDY_DATA_PATH="%{buildroot}/%{_datadir}/%{name}/data/"
%{buildroot}/%{_bindir}/cloudy -r test

%files
%license license.txt 
%doc readme.txt 
%{_bindir}/cloudy

%files data
%doc data/readme_data.htm data/readme_LineList_dat.txt
%{_datadir}/%{name}

%files doc
%license license.txt
%doc docs/* 

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 17.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 17.03-10
- Modify license after review, brom BSD to Zlib
- Fix incorrect changlog entry

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 17.03-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 17.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 17.03-2
- Fix compilation flags

* Tue Aug 23 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 17.03-1
- New upstream source (17.03)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 13.05-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 13.05-1
- New upstream source (13.05), fixes compilation errors

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 13.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Sergio Pascual <sergiopr@fedoraproject.org> - 13.04-1
- New upstream source (13.04), fixes GCC 6 build failure

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 13.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 13.03-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr  5 2014 Ville Ville Skyttä <ville.skytta@iki.fi> - 13.03-3
- Don't ship editor backup files

* Tue Feb 04 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 13.03-2
- Remove doxygen source and build requires

* Tue Feb 04 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 13.03-1
- New upstream version

* Wed Jan 22 2014 Sergio Pascual <sergiopr@fedoraproject.org> - 08.00-9
- Updated macros
- Fix bz #1037017, format security error

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 08.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 08.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 08.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 08.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 08.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 08.00-3
- Reorganized help docs

* Fri Jul 09 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 08.00-2
- Include license as %%doc in -doc subpackages

* Sun Apr 04 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 08.00-1
- New upstream source
- Devel documentations in its own subpackage devel-doc
- Program documentation in doc subpackage (bz #492431)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 07.02.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 07.02.01-7
- Noarch subpackage for docs

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 07.02.01-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Sergio Pascual <sergiopr at fedoraproject.org> - 07.02.01-5
- Directory not owned by package (bz #473639)

* Thu Mar 27 2008 Sergio Pascual <sergiopr at fedoraproject.org> - 07.02.01-4
- Timestamps in footer of doxygen docs removed (bz #436495)

* Thu Mar 27 2008 Sergio Pascual <sergiopr at fedoraproject.org> - 07.02.01-3
- Docs package is noarch (reverted)

* Sun Feb 24 2008 Sergio Pascual <sergiopr at fedoraproject.org> - 07.02.01-2
- Too much files in docs

* Thu Feb 14 2008 Sergio Pascual <sergiopr at fedoraproject.org> - 07.02.01-1
- Initial specfile
