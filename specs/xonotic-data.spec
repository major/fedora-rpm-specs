%global datadate 20230620

Summary: Game data for the Xonotic first person shooter
Name: xonotic-data
Version: 0.8.6
Release: 5%{?dist}
License: GPL-2.0-or-later
URL: http://www.xonotic.org/
# Source is custom, obtained with :
# wget http://dl.xonotic.org/xonotic-%{version}.zip
# unzip xonotic-%{version}.zip
# mkdir xonotic-data-%{version}/
# mv Xonotic/data/ Xonotic/Docs/* \
#    Xonotic/GPL* Xonotic/COPYING Xonotic/key_0.d0pk xonotic-data-%{version}/
# tar -cJf xonotic-data-%{version}.tar.xz xonotic-data-%{version}/
Source0: %{name}-%{version}.tar.xz
BuildArch: noarch

%description
Xonotic is a fast-paced, chaotic, and intense multiplayer first person shooter, 
focused on providing basic, old style deathmatches.

Data (textures, maps, sounds and models) required to play xonotic.

%prep
%setup -q

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-data.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-maps.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-music.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/xonotic-%{datadate}-nexcompat.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/font-xolonium-%{datadate}.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p data/font-unifont-%{datadate}.pk3 %{buildroot}%{_datadir}/xonotic/data/
install -p key_0.d0pk %{buildroot}%{_datadir}/xonotic/

%files
%doc GPL* COPYING
%{_datadir}/xonotic/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.6-1
- 0.8.6

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.8.5-3
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 29 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.8.5-1
- 0.8.5

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.8.2-6
- Install font pk3.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Kalev Lember <klember@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 04 2015 Kalev Lember <klember@redhat.com> - 0.8.1-1
- Update to 0.8.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 17 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- 0.8.0 (RHBZ #1183203)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.0-3
- Fix incorrect url in spec (rhbz #978022)

* Wed Jun 19 2013 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.0-2
- update spec: in custom build info use version macros instead of specific version

* Thu Jun 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.7.0-1
- 0.7.0, BZ 974029.

* Fri Feb 22 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-4
- Fixed Obsoletes.

* Wed Feb 20 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-3
- Fixed Provides.

* Fri Feb 08 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.0-2
- Changed define to global.
- De-macroized many commands.

* Mon Mar 12 2012 Jon Ciesla <limburgher@gmail.com> - 0.6.0-1
- New upstream.

* Thu Jan 26 2012 Jon Ciesla <limburgher@gmail.com> - 0.5.0-1
- Initial version, based on nexuiz-data 2.5.2 package.
