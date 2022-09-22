%global libname pclzip

Name:      php-%{libname}
Version:   2.8.2
Release:   15%{?dist}
Summary:   Compression and extraction functions for Zip formatted archives

License:   LGPLv2
URL:       http://www.phpconcept.net/%{libname}
# %%{SOURCE0} gets set to "download.php?file=pclzip-2-8-2.tgz" (for example)
# so need to download the source file manually from
# http://www.phpconcept.net/pclzip/pclzip-downloads
#
# http://www.phpconcept.net/download.php?file=pclzip-VERSION_WTIH_DASHES_INSTEAD_OF_DOTS.tgz
Source0:   %{libname}-%(echo "%{version}" | sed 's/\./-/g').tgz

BuildArch: noarch

Requires:  php(language)
# phpcompatinfo (computed from version 2.8.2)
Requires:  php-date
Requires:  php-pcre
Requires:  php-zlib

%description
PclZip library offers compression and extraction functions for Zip formatted
archives (WinZip, PKZIP).

PclZip gives you the ability to manipulate zip formatted archives. You can
create an archive, list the content and extract all its content in the file
system.

PclZip defines an object class which represent a Zip Archive. This class
manages the archive properties and offers access method and actions on
the archive.


%prep
%setup -qc

# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' *.*


%build
# Empty build section, nothing required


%install
mkdir -p %{buildroot}/%{_datadir}/php/%{libname}
cp -p *.php %{buildroot}/%{_datadir}/php/%{libname}/


%check
# No upstream tests


%files
%doc *.txt
%{_datadir}/php/%{libname}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.2-2
- Conditional %%{?dist}

* Thu May 29 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.8.2-1
- Initial package
