%global github_owner    natxet
%global github_name     CssMin
%global github_version  3.0.6
%global github_commit   d5d9f4c3e5cedb1ae96a95a21731f8790e38f1dd

%global packagist_owner natxet
%global packagist_name  cssmin

# phpcompatinfo
%global php_min_ver    5.1.2

Name:           php-%{packagist_owner}-%{packagist_name}
Version:        %{github_version}
Release:        9%{?github_date:.%{github_date}git%{shortcommit}}%{?dist}
Summary:        Configurable CSS parser and minifier

Group:          Development/Libraries
# License text is included in the sole code file
License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source0:        %{url}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  php-cli >= %{php_min_ver}
BuildRequires:  php-pcre
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

Requires:       php(language) >= %{php_min_ver}
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

Provides:       php-composer(%{packagist_owner}/%{packagist_name}) = %{version}
# Legacy
Provides:       php-composer(%{packagist_owner}/CssMin) = %{version}



%description
CssMin is a css parser and minifier. It minifies css by removing
unneeded whitespace characters, comments, empty blocks and empty
declarations. In addition declaration values can get rewritten to
shorter notation if available. The minification is configurable.

Autoloader: %{_datadir}/php/%{packagist_owner}/CssMin/autoload.php


%prep
%setup -qn %{github_name}-%{github_commit}


%build
: Create autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src/

: Legacy symlink
ln -s . src/src


%install
mkdir -p %{buildroot}%{_datadir}/php/%{packagist_owner}
cp -pr src %{buildroot}%{_datadir}/php/%{packagist_owner}/CssMin


# https://docs.fedoraproject.org/en-US/packaging-guidelines/Directory_Replacement/#_working_around_it_with_scriptlets
%pretrans -p <lua>
path = "%{_datadir}/php/%{packagist_owner}/CssMin/src"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end


%check
# Minimal test for our autoloader
php -r '
  require "%{buildroot}%{_datadir}/php/%{packagist_owner}/CssMin/autoload.php";
  exit(class_exists("CssMin") ? 0 : 1);
'


%files
%doc README composer.json
%dir %{_datadir}/php/%{packagist_owner}
     %{_datadir}/php/%{packagist_owner}/CssMin
# NOTE: %%attr is required for EPEL6 (dist-6E-epel)
%ghost %attr(644, root, root) %{_datadir}/php/%{packagist_owner}/CssMin/src.rpmmoved
%ghost %attr(644, root, root) %{_datadir}/php/%{packagist_owner}/CssMin/src.rpmmoved/CssMin.php


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 06 2020 Shawn Iwinski <shawn@iwin.ski> - 3.0.6-5
- Fix composer provides (php-composer(natxet/cssmin); and still provide previous
  php-composer(natxet/CssMin))
- Fix install (remove "src" dir)
- Use Fedora Autoloader
- Fix directory ownership

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Remi Collet <remi@remirepo.net> - 3.0.6-1
- update to 3.0.6
- add minimal test for our autoloader

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 25 2016 James Hogarth <james.hogarth@gmail.com> - 3.0.4-1
- new release 3.0.4
- Add simple classmap autoloader

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Adam Williamson <awilliam@redhat.com> - 3.0.3-1
- new release 3.0.3

* Mon Feb 23 2015 Adam Williamson <awilliam@redhat.com> - 3.0.2-2.20141229git8883d28
- change layout to match upstream's (with the /src sub-directory)

* Mon Dec 29 2014 Adam Williamson <awilliam@redhat.com> - 3.0.2-1.20141229git8883d28
- initial package
