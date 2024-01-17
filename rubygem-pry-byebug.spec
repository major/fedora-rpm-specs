# Generated from pry-byebug-3.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pry-byebug

Name: rubygem-%{gem_name}
Version: 3.10.1
Release: %autorelease
Summary: Fast debugging with Pry
License: MIT
URL: https://github.com/deivid-rodriguez/pry-byebug
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.0
BuildArch: noarch

%description
Combine 'pry' with 'byebug'. Adds 'step', 'next', 'finish',
'continue' and 'break' commands to control execution.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n  %{gem_name}-%{version}

%build
# https://github.com/deivid-rodriguez/pry-byebug/commit/036f94c67bb3eff36cda54400d9833062d9002dc
# Allow byebug 11.0 and above
sed -i ../%{gem_name}-%{version}.gemspec \
	-e '\@byebug@s|10\.0|11.0|' \
	%{nil}

gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
