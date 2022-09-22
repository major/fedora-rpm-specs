Name:		php-xmlseclibs
Version:	1.3.1
Release:	17%{?dist}
Summary:	PHP library for XML Security

License:	BSD
URL:		http://code.google.com/p/xmlseclibs/
Source0:	https://xmlseclibs.googlecode.com/files/xmlseclibs-%{version}.tar.gz

Requires:	php-mcrypt
Requires:	php-dom
Requires:	php-hash
Requires:	php-libxml
Requires:	php-openssl

BuildRequires:	php-pear
BuildRequires:	php-mcrypt
BuildRequires:	php-dom
BuildRequires:	php-hash
BuildRequires:	php-libxml
BuildRequires:	php-openssl

BuildArch:	noarch

%description
xmlseclibs is a library written in PHP for working with XML Encryption and 
Signatures. 

%prep
%setup -q -n xmlseclibs

%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/php/xmlseclibs
cp -pr xmlseclibs.php ${RPM_BUILD_ROOT}%{_datadir}/php/xmlseclibs/

%check
%{__pear} \
   run-tests \
   -i "-d include_path=%{buildroot}%{pear_phpdir}:%{pear_phpdir}" \
   tests | tee ../tests.log
# pear doesn't set return code
if grep -q "FAILED TESTS" ../tests.log; then
  for fic in tests/*.diff; do
    cat $fic; echo -e "\n"
  done
  exit 1
fi

%files
%doc CHANGELOG.txt LICENSE
%{_datadir}/php/xmlseclibs


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 F. Kooman <fkooman@tuxed.net> - 1.3.1-1
- update to 1.3.1 addressing all packaging issues

* Tue Jun 18 2013 F. Kooman <fkooman@tuxed.net> - 1.3.0-6
- add more dependencies listed by phpci output

* Tue Jun 18 2013 F. Kooman <fkooman@tuxed.net> - 1.3.0-5
- add mcrypt BuildRequires 

* Tue Jun 18 2013 F. Kooman <fkooman@tuxed.net> - 1.3.0-4
- add PEAR dependency to be able to run tests

* Tue Jun 18 2013 F. Kooman <fkooman@tuxed.net> - 1.3.0-3
- updates for package review 
- run tests

* Fri Jun 07 2013 F. Kooman <fkooman@tuxed.net> - 1.3.0-2
- add patch to support more signature methods, required by simplesamlphp 1.11.0

* Sat Feb 18 2012 F. Kooman <fkooman@tuxed.net> - 1.3.0-1
- initial package


