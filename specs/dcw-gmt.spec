Name:           dcw-gmt
Version:        2.2.0
Release:        4%{?dist}
Summary:        Digital Chart of the World (DCW) for GMT

License:        LGPL-3.0-or-later
URL:            https://github.com/GenericMappingTools/dcw-gmt
Source0:        https://github.com/GenericMappingTools/dcw-gmt/releases/download/%{version}/dcw-gmt-%{version}.tar.gz
BuildArch:      noarch


%description
DCW-GMT is an enhancement to the original 1:1,000,000 scale vector basemap of
the world available from the Princeton University Digital Map and Geospatial
Information Center and from GeoCommunity at
http://data.geocomm.com/readme/dcw/dcw.html.  To read and process the data you
should install GMT, the Generic Mapping Tools.


%prep
%setup -q

# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a *.nc *.txt %{buildroot}/%{_datadir}/%{name}/


%files
%license LICENSE
%doc README.md
%{_datadir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0-2
- convert license to SPDX

* Fri Jul 12 2024 Orion Poplawski <orion@nwra.com> - 2.2.0-1
- Update to 2.2.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 13 2023 Orion Poplawski <orion@nwra.com> - 2.1.2-1
- Update to 2.1.2

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 19 2022 Orion Poplawski <orion@nwra.com> - 2.1.1-1
- Update to 2.1.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Orion Poplawski <orion@nwra.com> - 2.1.0-1
- Update to 2.1.0

* Sat Nov 20 2021 Orion Poplawski <orion@nwra.com> - 2.0.1-1
- Update to 2.0.1

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 09 2021 Orion Poplawski <orion@nwra.com> - 2.0.0-1
- Update to 2.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Orion Poplawski <orion@nwra.com> - 1.1.4-1
- Update to 1.1.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 2 2014 Orion Poplawski <orion@cora.nwra.com> 1.1.1-1
- Update to 1.1.1

* Mon Nov 11 2013 Orion Poplawski <orion@cora.nwra.com> 1.1.0-2
- Fix URL and Source0
- Use buildroot macro

* Mon Nov 11 2013 Orion Poplawski <orion@cora.nwra.com> 1.1.0-1
- Initial package
