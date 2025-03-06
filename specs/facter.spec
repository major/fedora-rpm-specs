%global gem_name facter

Name:           facter
Version:        4.9.0
Release:        %autorelease
Summary:        Command and ruby library for gathering system information

License:        Apache-2.0
URL:            https://github.com/puppetlabs/facter
Source0:        https://downloads.puppetlabs.com/%{name}/%{name}-%{version}.gem
Source1:        https://downloads.puppetlabs.com/%{name}/%{name}-%{version}.gem.asc
Source2:        https://downloads.puppetlabs.com/puppet-gpg-signing-key-20250406.pub

BuildRequires:  gnupg2
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.5
Requires:       ruby(release) >= 2.5
Requires:       ruby(rubygems)

# Add runtime deps for testing
BuildRequires:  (rubygem(hocon) >= 1.3 with rubygem(hocon) < 2)
BuildRequires:  (rubygem(thor) >= 1.0.1 with rubygem(thor) < 2)
BuildRequires:  rubygem(sys-filesystem)
BuildRequires:  rubygem(base64)

# Binaries that Facter can call for complete facts
%ifarch %ix86 x86_64 ia64
Requires:       dmidecode
Requires:       pciutils
Requires:       virt-what
%endif
Requires:       net-tools

# Soft dependency for the mountpoints fact
Requires:       rubygem(sys-filesystem)
# dependency for facter/util/resolvers
Requires:       rubygem(base64)

Provides:       ruby-%{name} = %{version}
Obsoletes:      ruby-%{name} < 4
Obsoletes:      %{name}-devel < 4

BuildArch: noarch

%description
Facter is a lightweight program that gathers basic node information about the
hardware and operating system. Facter is especially useful for retrieving
things like operating system names, hardware characteristics, IP addresses, MAC
addresses, and SSH keys.

Facter is extensible and allows gathering of node information that may be
custom or site specific. It is easy to extend by including your own custom
facts. Facter can also be used to create conditional expressions in Puppet that
key off the values returned by facts.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n %{gem_name}-%{version}
%gemspec_add_dep -g sys-filesystem
# Revert https://github.com/puppetlabs/facter/commit/5e6c601f2a4ae37e3cd72f8411816a508d2f8b3c
%gemspec_remove_dep -g thor [">= 1.0.1", "< 1.3"]
%gemspec_add_dep -g thor [">= 1.0.1", "< 2"]

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm %{buildroot}%{gem_instdir}/LICENSE

mkdir -p %{buildroot}%{_bindir}
cp -a .%{gem_instdir}/bin/facter %{buildroot}%{_bindir}
rm -rf %{buildroot}/%{gem_instdir}/bin


%check
# No test suite can run since the spec files are not part of the gem
# So try to run the executable and see if that works
GEM_HOME="%{buildroot}%{gem_dir}" %{buildroot}%{_bindir}/facter


%files
%license LICENSE
%dir %{gem_instdir}
%{_bindir}/facter
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
%autochangelog
