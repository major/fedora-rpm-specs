# Generated from ansi-1.4.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ansi

# Disable checks since dependencies not
# available and some of them depend on this.
%global enable_checks 0

Name: rubygem-%{gem_name}
Version: 1.6.0
Release: %autorelease
Summary: ANSI at your fingertips!
License: BSD-2-Clause
URL: http://rubyworks.github.com/ansi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel 
BuildRequires: ruby 

%if 0%{?enable_checks}
BuildRequires: rubygem(detroit) 
BuildRequires: rubygem(qed) 
BuildRequires: rubygem(lemon) 
%endif
BuildArch: noarch


%description
The ANSI project is a superlative collection of ANSI escape code related
libraries enabling ANSI colorization and styling of 
console output. Byte for byte ANSI is the best ANSI code 
library available for the Ruby programming
language.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Run the test suite
%check
%if 0%{?enable_checks}
pushd .%{gem_instdir}
testrb -Ilib test
popd
%endif


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE.txt


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/NOTICE.md
%doc %{gem_instdir}/demo


%changelog
%autochangelog
