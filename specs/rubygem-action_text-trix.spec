# Generated from action_text-trix-2.1.16.gem by gem2rpm -*- rpm-spec -*-
%global gem_name action_text-trix

%global dompurify_version 3.4.2

# Circular dependency with rubygem-actiontext.
%bcond_with bootstrap

# TODO: Re-enable recompilation if possible. Currently, we don't have rollup.js
# in Fedora and therefore it requires network access. Still good for checking
# the results
%bcond_with js_recompilation

Name: rubygem-%{gem_name}
Version: 2.1.19
Release: 1%{?dist}
Summary: A rich text editor for everyday writing
# MIT: Trix
# (MPL-2.0 OR Apache-2.0): DOMPurify embedded into Trix
License: MIT AND (MPL-2.0 OR Apache-2.0)
URL: https://github.com/basecamp/trix
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/basecamp/trix.git && cd trix/action_text-trix
# git archive -v -o action_text-trix-2.1.19-tests.tar.gz v2.1.19 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.tar.gz
# Source code of pregenerated JS files.
# git clone https://github.com/basecamp/trix.git && cd trix
# git archive -v -o trix-2.1.19.tar.gz v2.1.19 src rollup.config.js package.json
Source2: trix-%{version}%{?prerelease}.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if %{without bootstrap}
BuildRequires: rubygem(actiontext)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(activestorage)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(importmap-rails)
BuildRequires: rubygem(propshaft)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(railties)
BuildRequires: rubygem(selenium-webdriver)
BuildRequires: rubygem(sqlite3)
BuildRequires: ruby
BuildRequires: chromedriver chromium chromium-headless
# Chromium availability is limited:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_800
# and chrome-headless even more:
# https://src.fedoraproject.org/rpms/chromium/blob/0d9761748509bb12051ab149d28c1052cd834f87/f/chromium.spec#_46-48
ExclusiveArch: x86_64 aarch64 noarch
%endif
%{?with_js_recompilation:BuildRequires: %{_bindir}/npm}
BuildArch: noarch
Provides: bundled(js-trix) = %{version}
Provides: bundled(js-dompurify) = %{dompurify_version}

%description
A rich text editor for everyday writing.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1 -b 2

%build
%if %{with js_recompilation}
# Recompile the embedded JS files from sources.
#
# This is practice suggested by packaging guidelines:
# https://fedoraproject.org/wiki/Packaging:Guidelines#Use_of_pregenerated_code

find app/assets/ -type f -exec sha512sum {} \;

mkdir %{builddir}/trix
( cd %{builddir}/trix

ln -s %{builddir}/src .
cp -a %{builddir}/{package.json,rollup.config.js} .

# TODO: This requires network access. Use Fedora rollup.js if it becomes
# available eventually
npm install
npx rollup --config rollup.config.js

# For comparison with the orginal checksum above.
find action_text-trix/app/assets/ -type f -exec sha512sum {} \;
)
%endif

# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%if %{without bootstrap}
%check
( cd .%{gem_instdir}

# Check DOMPurify version.
grep "DOMPurify %{dompurify_version}" app/assets/javascripts/trix.js

ln -s %{builddir}/test .

export BUNDLE_GEMFILE=${PWD}/../Gemfile

# The `Gemfiles` is unavoidable, otherwise `importmap-rails` are not properly
# loaded (although they could be added into `config/application.rb`).
touch ../Gemfile
echo 'gem "actiontext"' >> ../Gemfile
echo 'gem "activerecord"' >> ../Gemfile
echo 'gem "activestorage"' >> ../Gemfile
echo 'gem "capybara"' >> ../Gemfile
echo 'gem "importmap-rails"' >> ../Gemfile
echo 'gem "propshaft"' >> ../Gemfile
echo 'gem "puma"' >> ../Gemfile
echo 'gem "railties"' >> ../Gemfile
echo 'gem "selenium-webdriver"' >> ../Gemfile
echo 'gem "sqlite3"' >> ../Gemfile

# We don't have cuprite, but have selenium which appears to do the job.
sed -i '/driven_by/ s/cuprite/selenium/' test/application_system_test_case.rb
sed -i '/driven_by/ s/:chrome/:headless_chrome/' test/application_system_test_case.rb
sed -i '/js_errors:/ s/^/#/' test/application_system_test_case.rb
sed -i '/headless:/ s/^/#/' test/application_system_test_case.rb

ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
)
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Fri Mar 06 2026 Vít Ondruch <vondruch@redhat.com> - 2.1.19-1
- Initial package
