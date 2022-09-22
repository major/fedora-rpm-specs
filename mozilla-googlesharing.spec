%global moz_extensions %{_datadir}/mozilla/extensions

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global src_ext_id googlesharing@extension.thoughtcrime.org
%global inst_dir %{moz_extensions}/%{firefox_app_id}/%{src_ext_id}

%global seamonkey_app_dir \{googlesharing}
%global sym_link_dir %{moz_extensions}/%{seamonkey_app_dir} 

Name:           mozilla-googlesharing
Version:        0.18
Release:        23%{?dist}
Summary:        Anonymizing proxy service for Googlesharing system
License:        GPLv3+
URL:            http://www.googlesharing.net/
#source taken from mozilla's addon page,source not available at upstream download page
#see http://www.googlesharing.net/download.html
Source0:        http://releases.mozilla.org/pub/mozilla.org/addons/60333/googlesharing-0.18-fx.xpi
BuildArch:      noarch
Requires:       mozilla-filesystem


%description

This mozilla add-on aims to provide a level of anonymity from Google.
Prevents google from tracking your searches, movements,and websites you visit.
Leaves non-Google traffic completely untouched and unaffected.
Also makes this system,completely transparent to the end user.

%prep
%setup -q -c

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT

%{__install} -Dp -m 644 chrome.manifest $RPM_BUILD_ROOT/%{inst_dir}/chrome.manifest
%{__install} -Dp -m 644 certificate.pem $RPM_BUILD_ROOT%{inst_dir}/certificate.pem
%{__install} -Dp -m 644 install.rdf $RPM_BUILD_ROOT%{inst_dir}/install.rdf
%{__install} -Dpm 644 defaults/preferences/defaults.js $RPM_BUILD_ROOT%{inst_dir}/defaults/preferences/defaults.js

%{__mkdir_p} $RPM_BUILD_ROOT%{inst_dir}/chrome/content/images
%{__mkdir_p} $RPM_BUILD_ROOT%{inst_dir}/components  

pushd chrome/content/
%{__install} -Dpm 644 addEditProxy.js googlesharing.js options.js addEditProxy.xul googlesharing.xul options.css options.xul $RPM_BUILD_ROOT%{inst_dir}/chrome/content/
popd

pushd chrome/content/images/
%{__install} -Dpm 644 cbox-check.gif firemole.gif firemole-web.gif up.gif down.gif firemole-icon.gif googlesharing.png $RPM_BUILD_ROOT%{inst_dir}/chrome/content/images/
popd

pushd components/
%{__install} -Dpm 644 ConnectionManager.js Filter.js LocalProxy.js ProxyManager.js DataShuffler.js GoogleSharingManager.js Proxy.js $RPM_BUILD_ROOT%{inst_dir}/components/
popd

# symlink from seamonkey extension to firefox extension
mkdir -p %{buildroot}%{sym_link_dir}
ln -s %{inst_dir} %{buildroot}%{sym_link_dir}

%files
%doc COPYING
%{inst_dir}
%{sym_link_dir}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 03 2010 Mohammed Imran <imranceh@gmail.com> - 0.18-5
- Added SeaMonkey support

* Wed Apr 28 2010 Mohammed Imran <imranceh@gmail.com> - 0.18-4
- Replaced macro define with macro global

* Mon Apr 26 2010 Mohammed Imran <imranceh@gmail.com> - 0.18-3
- Used pushd popd instead of cd

* Fri Apr 23 2010 Mohammed Imran <imranceh@gmail.com> - 0.18-2
- Added missing images directory

* Fri Apr 23 2010 Mohammed Imran <imranceh@gmail.com> - 0.18-1
- Initial build
