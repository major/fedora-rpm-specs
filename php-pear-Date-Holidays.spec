%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name Date_Holidays

Name:           php-pear-Date-Holidays
Version:        0.21.8
Release:        18%{?dist}
Summary:        Driver based class to calculate holidays

License:        PHP
URL:            http://pear.php.net/package/Date_Holidays
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  php-pear(PEAR) >= 1.6.0

Requires(post): %{__pear}
Requires(postun): %{__pear}
Requires:       php-calendar
Requires:       php-date
Requires:       php-pcre
Requires:       php-simplexml
Requires:       php-pear(PEAR)
Requires:       php-pear(Date)
Requires:       php-pear(XML_Serializer)
Requires:       php-pear(Console_Getargs)
# Optional drivers available in repo
Requires:       php-pear(Date_Holidays_USA)


Provides:       php-pear(%{pear_name}) = %{version}

%description
Date_Holidays helps you calculating the dates and titles of holidays and
other special celebrations. The calculation is driver-based so it is easy
to add new drivers that calculate a country's holidays. The methods of the
class can be used to get a holiday's date and title in various languages.


%prep
%setup -qc

cd %{pear_name}-%{version}
# Package is V2
mv ../package.xml %{name}.xml


%build
cd %{pear_name}-%{version}
# Empty build section, most likely nothing required.


%install
rm -rf %{buildroot}
cd %{pear_name}-%{version}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
install -d %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}



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
%{_bindir}/pear-dh-*
%{pear_xmldir}/%{name}.xml
%{pear_testdir}/%{pear_name}
%{pear_datadir}/%{pear_name}
%{pear_phpdir}/Date/Holidays*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Remi Collet <remi@fedoraproject.org> - 0.21.8-1
- Version 0.21.8 (alpha) - API 0.17.2 (alpha)
- add optional dep, Date_Holidays_USA

* Sun Nov 25 2012 Remi Collet <remi@fedoraproject.org> - 0.21.7-1
- Version 0.21.7 (alpha) - API 0.17.2 (alpha)
- add all phpci detected dependencies

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 0.21.6-4
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 0.21.6-3
- rebuilt for new pear_testdir

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Remi Collet <Fedora@FamilleCollet.com> 0.21.6-1
- Version 0.21.6 (alpha) - API 0.17.2 (alpha)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Remi Collet <Fedora@FamilleCollet.com> 0.21.5-1
- Version 0.21.5 (alpha) - API 0.17.2 (alpha)

* Wed Apr 13 2011 Remi Collet <Fedora@FamilleCollet.com> 0.21.4-4
- doc in /usr/share/doc/pear

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 15 2010 Remi Collet <Fedora@FamilleCollet.com> - 0.21.4-2
- remove LICENSE file (not provided by upstream)
- rename Date_Holidays to php-pear-Date-Holidays.xml
- fix shebang
- set date.timezone during build

* Sun Aug 30 2009 Christopher Stone <chris.stone@gmail.com> 0.21.4-1.1
- Upstream sync

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Sep 12 2008 Christopher Stone <chris.stone@gmail.com> 0.20.1-1
- Upstream sync

* Thu May 22 2008 Christopher Stone <chris.stone@gmail.com> 0.19.1-1
- Upstream sync

* Thu Feb 07 2008 Christopher Stone <chris.stone@gmail.com> 0.17.4-1
- Upstream sync

* Mon Jul 02 2007 Christopher Stone <chris.stone@gmail.com> 0.17.1-2
- Add files to %%{_bindir}

* Mon Jul 02 2007 Christopher Stone <chris.stone@gmail.com> 0.17.1-1
- Upstream Sync
- Update license file

* Sun Jan 14 2007 Christopher Stone <chris.stone@gmail.com> 0.17.0-1
- Upstream sync
- Remove %%{_bindir} files from %%files

* Sun Jan 14 2007 Christopher Stone <chris.stone@gmail.com> 0.16.1-2
- Add LICENSE

* Sat Oct 14 2006 Christopher Stone <chris.stone@gmail.com> 0.16.1-1
- Initial release
