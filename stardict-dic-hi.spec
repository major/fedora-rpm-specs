Name:           stardict-dic-hi
Version:        3.0.1
Release:        30%{?dist}
Summary:        Hindi dictionary for stardict

License:        GPL-1.0-or-later
URL:            http://stardict.sourceforge.net/
# URL http://ltrc.iiit.net/downloads/shabdanjali-stardict/shabdanjali-fedora.tgz
# usage: source generate-tarball.sh <version> <org-source-tarball> <initial-name-of-new-tarball>
# usage example: source generate-tarball.sh 3.0.1 shabdanjali-fedora.tgz shabdanjali-fedora
Source0:        shabdanjali-fedora-3.0.1-nobinary.tar.gz
Source1:        generate-tarball.sh
Requires:       stardict
BuildArch:      noarch

%description
Hindi dictionary for stardict. The actual dictionary comes from
http://www.iiit.net/ltrc/Dictionaries/gen_eng_hin_hlp.html and Sriram
Chaudhry has converted it to a form usable by stardict.

%prep
%setup -q -n shabdanjali-fedora

%build
# Empty build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic
cp -p -rf shabdanjali* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/
chmod 644 README

%files
%doc README
%{_datadir}/stardict/dic/*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-28
- Update license tag to SPDX format

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Parag Nemade <pnemade AT redhat DOT com> - 3.0.1-15
- Add Supplements: for langpacks namimg guidelines
- Clean the specfile to follow current packaging guidelines

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 30 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-4
- Saving timestamp with -p.

* Thu Jan 30 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-3
- Added usage details for generate script

* Thu Jan 08 2009 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-2
- Fixed the actual source link. Removed the binary rpm of no use inside
- tarball. Fixed the URL also.

* Sat Dec 06 2008 Rakesh Pandit <rakesh@fedoraproject.org> 3.0.1-1
- Initial build
