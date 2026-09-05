%global gem_name factory_bot

Name: rubygem-%{gem_name}
Version: 6.6.0
Release: %autorelease
Summary: Framework and DSL for defining and using model instance factories
License: MIT
URL: https://github.com/thoughtbot/factory_bot
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/thoughtbot/factory_bot.git
# git -C factory_bot archive -v -o factory_bot-6.6.0-specs.txz v6.6.0 spec/
Source1: %{gem_name}-%{version}-specs.txz
# git clone --no-checkout https://github.com/thoughtbot/factory_bot.git
# git -C factory_bot archive -v -o factory_bot-6.6.0-features.txz v6.6.0 features/
Source2: %{gem_name}-%{version}-features.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-its)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(sqlite3)
BuildRequires: %{_bindir}/cucumber
BuildRequires: rubygem(aruba)
BuildArch: noarch
# Gem was renamed.
# https://github.com/thoughtbot/factory_bot/commit/e083f4a904ae30d170872385d4be3b37d44276e5
Obsoletes: rubygem-factory_girl < 4.10.0

%description
Framework and DSL for defining and using factories - less error-prone,
more explicit, and all-around easier to work with than fixtures.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
# Unpack Source1 and Source2
%setup -q -n %{gem_name}-%{version} -b 1 -b 2

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Symlinks don't work for this test suite
cp -a %{_builddir}/spec .

# We don't care about coverage.
sed -i "/simplecov/ s/^/#/" spec/spec_helper.rb

rspec -rspec_helper spec

ln -s %{_builddir}/features .
sed -i "/simplecov/ s/^/#/" features/support/env.rb

cucumber
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/GETTING_STARTED.md
%doc %{gem_instdir}/NAME.md
%doc %{gem_instdir}/NEWS.md

%changelog
%autochangelog
