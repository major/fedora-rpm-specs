%global gem_name puppet-lint

Name: rubygem-%{gem_name}
Version: 4.3.0
Release: %autorelease
Summary: Ensure your Puppet manifests conform with the Puppetlabs style guide
License: MIT
URL: https://github.com/puppetlabs/puppet-lint/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/puppetlabs/puppet-lint/issues/225
# Handle ruby3.4 backtrace formatting change
Patch0:  puppet-lint-issue225-ruby34-backtrace-formatting-change.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.7
BuildRequires: rubygem(rspec) >= 3.0
BuildRequires: rubygem(rspec-its) >= 1.0
BuildArch: noarch

%description
Checks your Puppet manifests against the Puppetlabs
style guide and alerts you to any discrepancies.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

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

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}

COVERAGE=no rspec spec/unit

popd

%files
%dir %{gem_instdir}
%{_bindir}/puppet-lint
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/rubocop_baseline.yml
%{gem_instdir}/spec

%changelog
%autochangelog
