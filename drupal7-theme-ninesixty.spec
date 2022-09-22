%global drupalver 7
%{?rhel: %{expand: %%global drupal drupal%%{drupalver}}}
%if 0%{?fedora} >= 15
%global drupal drupal%{drupalver}
%endif
%{!?drupal: %{expand: %%global drupal drupal}}
%global drupaldir %{_datadir}/%{drupal}
%global modname ninesixty

Name:           drupal%{drupalver}-theme-%{modname}
Version:        1.0
Release:        20%{?dist}
Summary:        Ninesixty theme for Drupal %{drupalver}

License:        GPLv2+ and GPL+ or MIT
URL:            http://drupal.org/project/ninesixty
Source0:        http://ftp.drupal.org/files/projects/%{modname}-%{drupalver}.x-%{version}.tar.gz
Source1:        LICENSE.txt
BuildArch:      noarch
Requires:       %{drupal} >= 7.0

%description
This theme is based on the 960 Grid System by Nathan Smith.  NineSixty
is a base theme with all the files provided by the 960 Grid System.
From the sketch sheets to all the styles from the framework are
included. There are a few modifications so it better fits into
Drupal. All the details are inside the README.txt file.


%prep
%setup -qn %{modname}
find -size 0 | xargs rm -f


%build
cp %{SOURCE1} .


%install
rm -rf %{buildroot}
install -d %{buildroot}%{drupaldir}/modules/%{modname}
find . -type f -exec install -m 0644 -D '{}' %{buildroot}%{drupaldir}/modules/%{modname}/'{}' \;



%files
%doc LICENSE.txt README.txt
%exclude %{drupaldir}/modules/%{modname}/LICENSE.txt
%exclude %{drupaldir}/modules/%{modname}/README.txt
%{drupaldir}/modules/%{modname}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct  4 2011 Paul W. Frields <stickster@gmail.com> - 1.0-1
- Initial RPM package

