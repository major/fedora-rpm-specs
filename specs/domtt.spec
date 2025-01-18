Name:          domtt
Version:       0.7.3
Release:       29%{?dist}
Summary:       DOM Tooltip (aka domTT) is a Javascript widget

License:       Apache-2.0
URL:           http://www.mojavelinux.com/projects/domtooltip/
Source0:       http://www.mojavelinux.com/cooker/download/index.php?file=domtooltip/%{name}-0.7.3.tar.gz
Source1:       %{name}.conf
BuildArch:     noarch


%description
DOM Tooltip (aka domTT) is a Javascript widget, released under the Apache 2.0
license, which allows developers to add customized tool-tips to their web sites. 


%prep
%setup -q -n domTT

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/html/en
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/js
install -m 0644 *.html $RPM_BUILD_ROOT%{_datadir}/%{name}/html/en
install -m 0644 *.js $RPM_BUILD_ROOT%{_datadir}/%{name}/js
cp -p %{SOURCE1} %{name}.conf


%files
%doc AUTHORS BUGS Changelog README TODO %{name}.conf
%{_datadir}/%{name}/html/en
%{_datadir}/%{name}/js


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 11 2024 Martin Gansser <linux4martin[at]gmx.de> - 0.7.3-28
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 14 2012 Martin Gansser <linux4martin[at]gmx.de> - 0.7.3-6
- added BuildArch noarch

* Thu Nov 9 2012 Martin Gansser <linux4martin[at]gmx.de> - 0.7.3-5
- rebuild

* Thu Nov 9 2012 Martin Gansser <linux4martin[at]gmx.de> - 0.7.3-4
- added apache conf file to doc section

* Thu Nov 8 2012 Martin Gansser <linux4martin[at]gmx.de> - 0.7.3-3
- Dropped BuildRequires and Requires because there is no build

* Wed Nov 7 2012 Martin Gansser <linux4martin[at]gmx.de> - 0.7.3-2
- added js files

* Mon Nov 5 2012 Martin Gansser <linux4martin[at]gmx.de> - 0.7.3-1
- initial Fedora version
