%global gem_name snmp

Name:           rubygem-%{gem_name}
Version:        1.3.3
Release:        %autorelease
Summary:        A Ruby implementation of SNMP (the Simple Network Management Protocol)
License:        MIT
URL:            https://github.com/hallidave/ruby-snmp
VCS:            git:%{url}
# GEM           https://rubygems.org/gems/snmp/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(minitest)
BuildArch:      noarch

%if 0%{?el7}
Provides:       rubygem(%{gem_name}) = %{version}
%endif



%description
A Ruby implementation of SNMP (the Simple Network Management Protocol).


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

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



%check
# Do not run check on EPEL7, Minitest is lacking Test method there
%if !0%{?el7}
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd
%endif

%files
%dir %{gem_instdir}
%{gem_instdir}/data
%{gem_instdir}/dump_yaml.rb
%{gem_instdir}/import.rb
%{gem_libdir}
%license %{gem_instdir}/MIT-LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
#%%{gem_instdir}/test

%changelog
%autochangelog
