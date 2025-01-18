%define mainversion 2.0
%define extra 0.2.0

Name:           PySolFC-cardsets
Version:        3.0
Release:        3%{?dist}
Summary:        Various cardsets for PySolFC
License:        GPL-2.0-or-later
URL:            https://pysolfc.sourceforge.io/
Source0:        https://github.com/shlomif/PySolFC-Cardsets/archive/%{version}/PySolFC-Cardsets-%{version}.tar.gz
Source1:        https://github.com/shlomif/PySol-Extra-Mahjongg-Cardsets/archive/%{extra}/PySol-Extra-Mahjongg-Cardsets-%{extra}.tar.gz
BuildArch:      noarch

Requires:       PySolFC >= %{mainversion}

%description
This package contains extras cardsets for PySolFC.

%prep
%setup -q -n PySolFC-Cardsets-%{version} -a1

%build

%install
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/PySolFC
# remove cardsets included in PySolFC package (PySolFC-Cardsets--Minimal-3.0.0)
rm -rf cardset-2000 cardset-blaren-7x7 cardset-crystal-mahjongg cardset-dashavatara-ganjifa \
       cardset-dashavatara-ganjifa-xl cardset-dojouji-3x3 \ cardset-dondorf \
       cardset-gnome-mahjongg-1 cardset-hanafuda-200-years cardset-hexadeck \ cardset-hokusai-6x6 \
       cardset-knave-of-hearts-4x4 cardset-louie-mantia-hanafuda cardset-matching \
       cardset-matching-xl cardset-matrix cardset-mid-winter-eve-8x8 cardset-mughal-ganjifa \
       cardset-mughal-ganjifa-xl cardset-neo cardset-neo-hex cardset-neo-tarock \
       cardset-next-matrix cardset-oxymoron cardset-players-trumps-10x10 cardset-simple-ishido \
       cardset-simple-ishido-xl cardset-standard cardset-the-card-players-9x9 cardset-tuxedo \
       cardset-uni-mahjongg cardset-victoria-falls-5x5 cardset-vienna-2k

cp -a cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC
cp -a PySol-Extra-Mahjongg-Cardsets-0.2.0/Lost-Mahjongg-Cardsets/cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC


find $RPM_BUILD_ROOT%{_datadir}/PySolFC -type f -name 'COPYRIGHT' -exec chmod 0644 '{}' \;

%files
%{_datadir}/PySolFC/cardset-*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Adam Williamson <awilliam@redhat.com> - 3.0-1
- Update to 3.0 (#2272345), update list of removals for minimal-3.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 19 2023 Sérgio Basto <sergio@serjux.com> - 2.2-2
- Updated the remove of cardsets already included in PySolFC package (PySolFC-Cardsets--Minimal-2.2.0)
- Convert to SPDX License

* Mon Feb 27 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.2-1
- Update to 2.2 (#2173477)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Sérgio Basto <sergio@serjux.com> - 2.0-18
- Add Lost-Mahjongg-Cardsets

* Mon May 06 2019 Sérgio Basto <sergio@serjux.com> - 2.0-17
- Use new github sources

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-3
- Change requirement on main version to >= 2.0, not = 1.1

* Mon Feb 8 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-2
- Add dist tag since manual copying is not done anymore (see releng #3335)

* Sat Jan 30 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-1
- Update to 2.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 25 2007 Stewart Adam <s.adam@diffingo.com> 1.1-3
- Remove BR python-devel
- Add dot to %%description
- Remove preinstalled cardsets
- Use a dir PySolFC actually recognizes

* Wed Oct 24 2007 Stewart Adam <s.adam@diffingo.com> 1.1-2
- Own dirs we create
- Remove %%{?dist} tag
- Fix URL, description and summary
- Don't place any executable files in the RPM

* Sat Sep 29 2007 Stewart Adam <s.adam@diffingo.com> 1.1-1
- Initial release
