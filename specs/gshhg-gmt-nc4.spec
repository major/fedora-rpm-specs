Name:           gshhg-gmt-nc4
Version:        2.3.7
Release:        13%{?dist}
Summary:        Global Self-consistent Hierarchical High-resolution Geography (GSHHG)

License:        LGPL-3.0-or-later
URL:            https://github.com/GenericMappingTools/gshhg-gmt
# seems to be derived at least from 2 Public Domain datasets, 
# CIA World DataBank II and World Vector Shoreline (already in fedora),
# then modified.
Source0:        https://github.com/GenericMappingTools/gshhg-gmt/releases/download/%{version}/gshhg-gmt-%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      GMT-coastlines < 2.2.4-2
Provides:       GMT-coastlines = %{version}-%{release}
Provides:       gshhg-gmt = %{version}-%{release}


%description
GSHHG is a high-resolution shoreline data set amalgamated from two databases:
Global Self-consistent Hierarchical High-resolution Shorelines (GSHHS) and
CIA World Data Bank II (WDBII).  GSHHG contains vector descriptions at five
different resolutions of land outlines, lakes, rivers, and political
boundaries.  This data for use by GMT, the Generic Mapping Tools.

This package contains the crude, low, and intermediate resolution data.
Install the -all, -full, or -high sub-packages to get full, high, or all of
the resolution data respectively. 


%package        full
Summary:        GSHHG - full resolution
Requires:       %{name}
Obsoletes:      GMT-coastlines-full < 2.2.4-2
Provides:       GMT-coastlines-full = %{version}-%{release}
Provides:       gshhg-gmt-full = %{version}-%{release}

%description    full
%{summary}.


%package        high
Summary:        GSHHG - high resolution
Requires:       %{name}
Obsoletes:      GMT-coastlines-high < 2.2.4-2
Provides:       GMT-coastlines-high = %{version}-%{release}
Provides:       gshhg-gmt-high = %{version}-%{release}

%description    high
%{summary}.


%package        all
Summary:        GSHHG - all resolutions
Requires:       %{name}
Requires:       %{name}-full
Requires:       %{name}-high
Obsoletes:      GMT-coastlines-all < 2.2.4-2
Provides:       GMT-coastlines-all = %{version}-%{release}
Provides:       gshhg-gmt-all = %{version}-%{release}

%description    all
%{summary}.


%prep
%setup -q -n gshhg-gmt-%{version} 

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a *.nc %{buildroot}/%{_datadir}/%{name}


%files
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT README.TXT
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*_[cil].nc

%files full
%{_datadir}/%{name}/*_f.nc

%files high
%{_datadir}/%{name}/*_h.nc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.7-11
- convert license to SPDX

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Orion Poplawski <orion@nwra.com> - 2.3.7-1
- Update to 2.3.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 7 2014 Orion Poplawski <orion@cora.nwra.com> 2.3.3-1
- Update to 2.3.3

* Thu Oct 2 2014 Orion Poplawski <orion@cora.nwra.com> 2.3.2-1
- Update to 2.3.2

* Thu Jul 10 2014 Orion Poplawski <orion@cora.nwra.com> 2.3.1-1
- Update to 2.3.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 7 2014 Orion Poplawski <orion@cora.nwra.com> 2.3.0-2
- Fix obsoletes (bug #1095424)

* Mon Mar 3 2014 Orion Poplawski <orion@cora.nwra.com> 2.3.0-1
- Update to 2.3.0

* Mon Nov 11 2013 Orion Poplawski <orion@cora.nwra.com> 2.2.4-1
- Rename from GMT-coastlines
