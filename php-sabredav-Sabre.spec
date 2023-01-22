%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear:       %global __pear       %{_bindir}/pear}
%global pear_name %(echo %{name} | sed -e 's/^php-sabredav-//' -e 's/-/_/g')
%global channelname pear.sabredav.org

Name:           php-sabredav-Sabre
Version:        1.0.0
Release:        28%{?dist}
Summary:        Base for Sabre_DAV packages

License:        BSD
URL:            http://code.google.com/p/sabredav
Source0:        http://pear.sabredav.org/get/%{pear_name}-%{version}.tgz

# Fix autoload to allow namespace for VObject
Patch0:         %{name}.patch

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)
Requires:       php-pear(PEAR)
Requires:       php-common >= 5.1
Requires:       php-pdo
Requires:       php-xml
Requires:       php-mbstring
BuildRequires:  php-channel(%{channelname})

Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:       php-pear(%{pear_name}) = %{version}
Requires:       php-channel(%{channelname})
Provides:       php-pear(%{channelname}/%{pear_name}) = %{version}

%description
The Base SabreDAV package provides some functionality used by all packages.

%prep
%setup -q -c
cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml

# Fix autoload to use namespace and force version
%patch0 -p1 -b .orig


%build
# Empty build section, most likely nothing required.

%install
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot $RPM_BUILD_ROOT %{name}.xml

# Clean up unnecessary files
rm -rf $RPM_BUILD_ROOT%{pear_metadir}/.??*

# Install XML package description
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{name}.xml $RPM_BUILD_ROOT%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/%{pear_name}


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-12
- fix pear_metadir macro

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-11
- fix autoload as VObject 2.1 use namespace
- rename Sabre.xml to php-sabredav-Sabre.xml

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 02 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 1.0.0-9
- create if-else to fix clean up issue with f19 and rhel
* Sat Mar 02 2013 Joseph Marrero <jmarrero@fedoraproject.org> - 1.0.0-8
- change pear_phpdir to pear_metadir to correctly build on f19
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Wed Oct 31 2012 Joseph Marrero <jmarrero@fedoraproject.org> - 1.0.0-6
- Added the requirements deps asked by phpci
* Sun Oct 14 2012 Joseph Marrero <jmarrero@fedoraproject.org> - 1.0.0-5
- Fixed Description
* Sun Oct 14 2012 Joseph Marrero <jmarrero@fedoraproject.org> - 1.0.0-4
- Fixed Documentation directory
- Added phpci pointed requirements wich are all in php-common
- Dependencies Clean up
* Wed Oct 03 2012 Joseph Marrero <jmarrero@fedoraproject.org> - 1.0.0-3
- removed uneaded remove of %%BUILDROOT 
- changed %%define for global
- removed extra changes of directory
* Wed Oct 03 2012 Joseph Marrero <jmarrero@fedoraproject.org> - 1.0.0-2
- Change Description to be more specific to diferenciate from Sabre_DAV package
* Fri Apr 06 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.0.0-1
- initial package
