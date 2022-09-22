# Generated from jquery-rails-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-rails

# Unfortunately, lib/jquery/rails/version.rb specifies exact versions of
# bundled jquery, so be specific with the require to keep this relieable.
%global jquery1_version 1.12.4
#%%global jquery1_system_version 1.12.4
%global jquery2_version 2.2.4
#%%global jquery2_system_version 2.2.4
%global jquery3_version 3.5.1
%global jquery3_system_version 3.6.0

# In case bundled jQuery should be used, comment out appropriate line.
# jQuery {1,2}.x were dropped from Fedora.
#%%global unbundle_jquery1 1
#%%global unbundle_jquery2 1
# jQuery 3.x is in older version in Fedora.
#%%global unbundle_jquery3 1

Name: rubygem-%{gem_name}
Version: 4.4.0
Release: 3%{?dist}
Summary: Use jQuery with Rails 4+
License: MIT
URL: https://github.com/rails/jquery-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
%{?unbundle_jquery1:Requires: jquery = %{jquery1_version}}
%{?unbundle_jquery2:Requires: jquery = %{jquery2_version}}
%{?unbundle_jquery3:Requires: jquery = %{jquery3_version}}
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: web-assets-devel
# BR system version of jQuery even though we bundle. This makes the package
# FTBFS as soon as the version changes and will make somebody to notice and
# possibly unbundle sooner.
%{?unbundle_jquery1:BuildRequires: jquery = %{jquery1_version}}
#%%{!?unbundle_jquery1:BuildRequires: jquery = %{jquery1_system_version}}
%{?unbundle_jquery2:BuildRequires: jquery = %{jquery2_version}}
#%%{!?unbundle_jquery2:BuildRequires: jquery = %{jquery2_system_version}}
%{?unbundle_jquery3:BuildRequires: jquery = %{jquery3_version}}
%{!?unbundle_jquery3:BuildRequires: jquery = %{jquery3_system_version}}
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(rails-dom-testing)
# jquery-ujs is not yet in Fedora.
Provides: bundled(jquery-usj) = 1.2.2
%{!?unbundle_jquery1:Provides: bundled(js-jquery) = %{jquery1_version}}
%{!?unbundle_jquery2:Provides: bundled(js-jquery) = %{jquery2_version}}
%{!?unbundle_jquery3:Provides: bundled(js-jquery) = %{jquery3_version}}
BuildArch: noarch

%description
This gem provides jQuery and the jQuery-ujs driver for your Rails 4+
application.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if 0%{?unbundle_jquery1}
for file in %{_jsdir}/jquery/1/*; do
  rm %{buildroot}%{gem_instdir}/vendor/assets/javascripts/jquery.*
  ln -s -f $file -t %{buildroot}%{gem_instdir}/vendor/assets/javascripts/
done
%endif

%if 0%{?unbundle_jquery2}
for file in %{_jsdir}/jquery/2/*; do
  rm %{buildroot}%{gem_instdir}/vendor/assets/javascripts/jquery2.*
  ln -s -f $file %{buildroot}%{gem_instdir}/vendor/assets/javascripts/$(basename $file | sed 's/jquery/jquery2/')
done
%endif

%if 0%{?unbundle_jquery3}
for file in %{_jsdir}/jquery/3/*; do
  rm %{buildroot}%{gem_instdir}/vendor/assets/javascripts/jquery3.*
  ln -s -f $file %{buildroot}%{gem_instdir}/vendor/assets/javascripts/$(basename $file | sed 's/jquery/jquery3/')
done
%endif

%check
pushd .%{gem_instdir}
# Check that rpm version dependencies match the versions expected by the
# gem package.
ruby -Ilib -rjquery/rails/version -e '
exit \
  Jquery::Rails::JQUERY_VERSION == "%{jquery1_version}" && \
  Jquery::Rails::JQUERY_2_VERSION == "%{jquery2_version}" && \
  Jquery::Rails::JQUERY_3_VERSION == "%{jquery3_version}"
'

ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/VERSIONS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/jquery-rails.gemspec
%{gem_instdir}/test

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Vít Ondruch <vondruch@redhat.com> - 4.4.0-1
- Update to jquery-rails 4.4.0.
  Resolves: rhbz#1434635

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Vít Ondruch <vondruch@redhat.com> - 4.2.2-10
- jQuery {1,2}.x were dropped from Fedora while jQuery 3.x available in
  more recent version.
  Related: rhbz#1863662
  Related: rhbz#1863663

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Vít Ondruch <vondruch@redhat.com> - 4.2.2-1
- Update to jquery-rails 4.2.2.

* Wed Dec 21 2016 Vít Ondruch <vondruch@redhat.com> - 4.2.1-2
- Use system version of jQuery 2.x.

* Fri Dec 02 2016 Vít Ondruch <vondruch@redhat.com> - 4.2.1-1
- Update to jquery-rails 4.2.1.

* Fri Jul 22 2016 Vít Ondruch <vondruch@redhat.com> - 4.0.4-3
- Relax the rails-dom-testing dependency.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Vít Ondruch <vondruch@redhat.com> - 4.0.4-1
- Update to jquery-rails 4.0.4.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Josef Stribny <jstribny@redhat.com> - 3.1.0-1
- Update to jquery-rails 3.1.0

* Thu Feb 06 2014 Josef Stribny <jstribny@redhat.com> - 3.0.4-2
- Fix license to MIT only

* Wed Oct 23 2013 Josef Stribny <jstribny@redhat.com> - 3.0.4-1
- Update to jquery-rails 3.0.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.2-1
- Initial package
