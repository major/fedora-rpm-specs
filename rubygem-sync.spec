# Generated from sync-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sync

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: %autorelease
Summary: A module that provides a two-phase lock with a counter
License: BSD-2-Clause
URL: https://github.com/ruby/sync

Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ruby/sync.git && cd sync
# git archive -o rubygem-sync-0.5.0-specs.tgz v0.5.0 test
Source1: %{name}-%{version}-specs.tgz
# https://github.com/ruby/sync/commit/8f2821d0819ee7c08506f204c7676f12c5ab1397
# Note that ruby3.3 drops RubyVM::MJIT in favor of RJIT
Patch0:  sync-8f2821d-guard-vm-jit.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
A module that provides a two-phase lock with a counter.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1
(
cd %{_builddir}/
%patch -P0 -p1
)
# Remove unneeded scripts
rm -rf bin
sed -i 's/"bin\/console".freeze, "bin\/setup".freeze, //' ../%{gem_name}-%{version}.gemspec 

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



%check
pushd .%{gem_instdir}
# Link the test suite into the right place in source tree.
ln -s %{_builddir}/test .
# Run tests
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/sync.gemspec

%changelog
%autochangelog
