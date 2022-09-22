%{?drupal7_find_provides_and_requires}

%global module fences

Name:          drupal7-%{module}
Version:       1.2
Release:       15%{?dist}
Summary:       Configurable field wrappers

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

Requires:      drupal7(field)

%description
Fences is a an easy-to-use tool to specify an HTML element for each field. This
element choice will propagate everywhere the field is used, such as teasers, RSS
feeds and Views. You don't have to keep re-configuring the same HTML element
over and over again every time you display the field.

Best of all, Fences provides leaner markup than Drupal 7 core! And can get rid
of the extraneous classes too!

This kind of tool is needed in order to create semantic HTML5 output from
Drupal. Without such a tool, you have to create custom field templates in your
theme for every field. :(

Similar projects include Semantic fields [1], Field Wrappers [2] and a tool
inside the Display Suite [3] extras.

This package provides the following Drupal module:
* %{module}

[1] http://drupal.org/project/semantic_fields
[2] http://drupal.org/project/field_wrappers
[3] http://drupal.org/project/ds


%prep
%setup -qn %{module}


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{?_licensedir:%license LICENSE.txt}
%doc *.txt
%{drupal7_modules}/%{module}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-10
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Shawn Iwinski <shawn.iwinski@gmail.com> - 1.2-1
- Updated to 1.2 (RHBZ #1265028)
- Removed RPM README b/c it only explained common Drupal workflow
- %%license usage
- Keep documentation where end-users expect it

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-2
- Updated for drupal7-rpmbuild 7.22-5

* Tue Apr 02 2013 Shawn Iwinski <shawn.iwinski@gmail.com> 1.0-1
- Initial package
