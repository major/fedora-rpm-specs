# Generated from addressable-2.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name addressable

Name: rubygem-%{gem_name}
Version: 2.9.2
Release: %autorelease
Summary: URI Implementation
License: Apache-2.0
URL: https://github.com/sporkmonger/addressable
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/sporkmonger/%{gem_name}/archive/%{gem_name}-%{version}/%{gem_name}-%{gem_name}-%{version}.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(public_suffix)
BuildRequires: rubygem(rspec-its)
BuildArch: noarch

%description
Addressable is an alternative implementation to the URI implementation that is
part of Ruby's standard library. It is flexible, offers heuristic parsing, and
additionally provides extensive support for IRIs and URI templates.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
tar zxf %{SOURCE1} %{gem_name}-%{gem_name}-%{version}/spec --strip-components 1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
# Drop Bundler dependency.
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb

# Remove tests failing because of missing internet connection.
mv spec/addressable/net_http_compat_spec.rb{,.disabled}

LC_ALL=C.UTF-8 rspec spec/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
