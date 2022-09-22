%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%global pear_name %(echo %{name} | sed -e 's/^php-dropbox-php-//' -e 's/-/_/g')
%global channelname pear.dropbox-php.com

Name:           php-dropbox-php-Dropbox
Version:        1.0.0
Release:        20%{?dist}
Summary:        Library for integrating dropbox with PHP

License:        MIT
URL:            http://www.dropbox-php.com/
Source0:        http://%{channelname}/get/%{pear_name}-%{version}.tgz

BuildArch:      noarch

BuildRequires:  php-pear(PEAR)
BuildRequires:  php-channel(%{channelname})

Requires:       php-pear(PEAR)
Requires:       php-channel(%{channelname})
Requires(post): %{__pear}
Requires(postun): %{__pear}

Requires:       php-spl php-curl php-date php-hash
Requires:       php-json php-pcre

Requires:       php-pear(HTTP_OAuth)
Requires:       php-pecl(oauth)

Provides:       php-pear(%{channelname}/%{pear_name}) = %{version}

%description
This PHP library allows you to easily integrate dropbox with PHP.
The library makes use of OAuth.

Optional Dependencies:
Zend framework: Zend_{Oauth,Json,Uri} for OAuth/Zend back-end
Wordpress: WP_Http for OAuth/Wordpress back-end


%prep
%setup -q -c

mv package.xml %{pear_name}-%{version}/%{name}.xml


%build


%install
cd %{pear_name}-%{version}
rm -rf %{buildroot} docdir
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{channelname}/%{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/%{pear_name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.0.0-4
- require php-pecl(oauth) instead of php-oauth
- add note about optional dep to wordpress and zend

* Wed Mar 06 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.0.0-3
- require HTTP_OAuth
- get source from pear host http://pear.dropbox-php.com

* Wed Feb 27 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.0.0-2
- rename to php-dropbox-php-Dropbox

* Tue Feb 19 2013 Gregor Tätzner <brummbq@fedoraproject.org> - 1.0.0-1
- Initial package