# Generated from rest-client-1.3.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rest-client

# This enables to run full test suite, where network connection is available.
# However, it must be disabled for Koji build.
%bcond_with network
%bcond_without tests

Name: rubygem-%{gem_name}
Version: 2.1.0
Release: 12%{?dist}
Summary: Simple HTTP and REST client for Ruby
License: MIT
URL: https://github.com/rest-client/rest-client
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix test suite compatibility with Ruby 3+.
# https://github.com/jbox-web/rest-client/commit/49c96a6415cc241b02356d28b7a5a89d0e134bfa
Patch0: rubygem-rest-client-2.1.0-Fix-broken-tests-with-Ruby-3.x.patch
# Update certificates to correctly pass integration test suite with enabled
# networking.
# https://github.com/jbox-web/rest-client/commit/15b20206404f0e59417f1fc202726e5a694d7d76
Patch1: rubygem-rest-client-2.1.0-Fix-integration-tests-update-www.mozilla.org-CA-Cert.patch
# https://github.com/jbox-web/rest-client/pull/2
# ruby3.2 changes URI.parse behavior so that hostname returns
# empty string instead of nil
Patch2: rubygem-rest-client-2.1.0-ruby32-URL_parse-change-hostname.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{with tests}
BuildRequires: rubygem(http-cookie)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(netrc)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(http-accept)
%endif
BuildArch: noarch

%description
A simple HTTP and REST client for Ruby, inspired by the Sinatra microframework
style of specifying actions: get, put, post, delete.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

# Allow newer http-accept we have in Fedora
%gemspec_remove_dep -g http-accept
%gemspec_add_dep -g http-accept '< 3.0'

%patch0 -p1

%patch1 -p1
%gemspec_remove_file -t ["spec/integration/capath_digicert/3513523f.0", "spec/integration/capath_digicert/399e7759.0"]
%gemspec_remove_file ["spec/integration/capath_digicert/3513523f.0", "spec/integration/capath_digicert/399e7759.0"]
%gemspec_add_file ["spec/integration/capath_digicert/ce5e74ef.0"]

( cat %PATCH2 | sed -e 's|rest_client|restclient|' | patch -p1 )

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

%if %{with tests}
%check
pushd .%{gem_instdir}
%if %{without network}
mv spec/integration/httpbin_spec.rb{,.disable}
mv spec/integration/request_spec.rb{,.disable}
%endif

rspec spec
popd
%endif

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{_bindir}/restclient
%exclude %{gem_instdir}/.*
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/AUTHORS
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/history.md
%{gem_instdir}/rest-client.gemspec
%{gem_instdir}/rest-client.windows.gemspec
%{gem_instdir}/spec

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-11
- Replace Patch1 with the one upstream formally adopted

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-9
- Apply proposal patch for ruby3.2 URI.parse behavior change

* Mon Aug 08 2022 Vít Ondruch <vondruch@redhat.com> - 2.1.0-8
- Fix test suite compatibility with Ruby 3+.
  Resolves: rhbz#2113703
- Update certificates to fix integration test suite.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Pavel Valena <pvalena@redhat.com> - 2.1.0-2
- Allow newer http-accept gem.

* Fri Nov 15 2019 Pavel Valena <pvalena@redhat.com> - 2.1.0-1
- Update to rest-client 2.1.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Vít Ondruch <vondruch@redhat.com> - 2.0.0-2
- Fix compatibility with Ruby OpenSSL 2.x+.

* Thu Jul 14 2016 Jun Aruga <jaruga@redhat.com> - 2.0.0-1
- Update to rest-client 2.0.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 19 2015 Vít Ondruch <vondruch@redhat.com> - 1.8.0-1
- Update to rest-client 1.8.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Vít Ondruch <vondruch@redhat.com> - 1.6.7-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Sat Sep 22 2012 Tim Bielawa <tim@redhat.com> - 1.6.7-1
- Update to 1.6.7

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 1.6.1-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 1.6.1-1
- New version release

* Wed Mar 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.0-6
- New version release

* Wed Feb 17 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-5
- Added %%dir %%{geminstdir} into spec file

* Wed Feb 17 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-4
- Marked README.rdoc, history.md and spec/ as %%doc

* Tue Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-3
- Fixed licence (MIT)
- Fixed duplicated files in spec
- Replaced %%define with %%global

* Tue Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-2
- Fixed spec filename
- Added Ruby dependency

* Tue Feb 16 2010 Michal Fojtik <mfojtik@redhat.com> - 1.3.1-1
- Initial package
