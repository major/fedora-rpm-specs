# Generated from tins-1.29.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name tins

Name: rubygem-%{gem_name}
Version: 1.38.0
Release: %autorelease
Summary: Useful tools library in Ruby
License: MIT
URL: https://github.com/flori/tins
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
BuildRequires: rubygem(irb)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0
BuildRequires: rubygem(sync)
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(simplecov)
BuildArch: noarch

%description
All the stuff that isn't good/big enough for a real library.


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


%check
pushd .%{gem_instdir}
ruby -rtest-unit -e 'exit Test::Unit::AutoRunner.run(true)' -Ilib tests/
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/CHANGES.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/tests
%{gem_instdir}/tins.gemspec

%changelog
%autochangelog
