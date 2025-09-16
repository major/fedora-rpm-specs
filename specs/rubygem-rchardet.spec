# Generated from rchardet-1.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rchardet

Name: rubygem-%{gem_name}
Version: 1.10.0
Release: %autorelease
Summary: Character encoding auto-detection in Ruby
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
URL: https://github.com/jmhodges/rchardet
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Upstream tar ball to grab LICENSE file and tests only
Source1: https://github.com/jmhodges/rchardet/archive/v%{version}/rchardet-%{version}.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Character encoding auto-detection in Ruby. As smart as your browser.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

tar zxf %{SOURCE1} rchardet-%{version}/test rchardet-%{version}/LGPL-LICENSE.txt rchardet-%{version}/Readme.md --strip-components 1
# Remove +x bit on license.
chmod 0644 LGPL-LICENSE.txt

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/LGPL-LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license LGPL-LICENSE.txt
%doc Readme.md

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
