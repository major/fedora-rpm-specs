# Generated from sassc-rails-2.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sassc-rails

# Because of circular dependency with sass-rails
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 2.1.2
Release: 13%{?dist}
Summary: Integrate SassC-Ruby into Rails
# SIL license found in
# test/dummy/app/assets/stylesheets/erb_render_with_context.css.erb
# https://github.com/sass/sassc-rails/issues/155
# Automatically converted from old format: MIT and OFL - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-OFL
URL: https://github.com/sass/sassc-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix test suite compatibility with Rails 7+.
# https://github.com/sass/sassc-rails/pull/178
Patch0: rubygem-sassc-rails-2.1.2-Fix-test-suite-for-Rails-7.patch
# Fix compatibility with Minitest 5.19+.
# https://github.com/sass/sassc-rails/pull/179
Patch1: rubygem-sassc-tails-2.1.2-Fix-compatibility-with-Minitest-5.19.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
%if %{without bootstrap}
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(sass-rails)
BuildRequires: rubygem(sassc)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(tilt)
%endif
BuildArch: noarch

%description
Integrate SassC-Ruby into Rails.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch -P0 -p1
%patch -P1 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%if %{without bootstrap}
%check
pushd .%{gem_instdir}

# Copy in .gemspec and use the sass-rails sources
cp %{buildroot}%{gem_spec} sassc-rails.gemspec

# Avoid unnecessary dependency
sed -i -e '/require .pry./ s/^/#/' test/test_helper.rb
sed -i -e '/dependency.*pry./ s/^/#/' \
       -e '/dependency.*rake./ s/^/#/' \
    sassc-rails.gemspec

sed -i -e '/Bundler\.require/ s/^/#/' \
       -e '/require .bundler./ s/^/#/' \
    test/test_helper.rb

# The test is unstalbe and passes just occasionally.
sed -i '/def test_globbed_imports_work_when_globbed_file_is_added$/a \
    skip' test/sassc_rails_test.rb

ruby -Ilib:test -rsass-rails -rsprockets/railtie \
  -e 'Dir.glob "./test/**/*.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/sassc-rails.gemspec
%{gem_instdir}/test
%{gem_instdir}/gemfiles
%doc %{gem_instdir}/CODE_OF_CONDUCT.md

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Vít Ondruch <vondruch@redhat.com> - 2.1.2-9
- Fix FTBFS due to incompatibility with Minitest 5.19+.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 27 2023 Vít Ondruch <vondruch@redhat.com> - 2.1.2-7
- Fix FTBFS caused by RoR 7+.
  Resolves: rhbz#2113707

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Pavel Valena <pvalena@redhat.com> - 2.1.2-1
- Initial package.
