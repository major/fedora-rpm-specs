# Generated from yaml-lint-0.0.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yaml-lint
# This commit corresponds to the relase in github which is not tagged :-(
%global commit 8dfc583584e046c54617315734883c887768c6ca

Name:          rubygem-%{gem_name}
Version:       0.1.2
Release:       %autorelease
Summary:       Really simple YAML lint
License:       MIT
URL:           https://github.com/Pryz/yaml-lint
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:       https://github.com/Pryz/yaml-lint/archive/%{commit}/yaml-lint-%{commit}.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildArch:     noarch


%description
Check if your YAML files can be loaded.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# unpack only the spec and LICENSE from SOURCE1
tar zxf %{SOURCE1} --strip-components 1 \
                   yaml-lint-%{commit}/spec \
                   yaml-lint-%{commit}/LICENSE \
                   yaml-lint-%{commit}/README.md \

# Disable Coverals
sed -i "s/^require 'coveralls'$//" spec/spec_helper.rb
sed -i "s/^Coveralls.wear!//"      spec/spec_helper.rb


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
rspec -I%{gem_instdir} spec


%files
%dir %{gem_instdir}
%{_bindir}/yaml-lint
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license LICENSE
%doc README.md


%files doc
%doc %{gem_docdir}


%changelog
%autochangelog
