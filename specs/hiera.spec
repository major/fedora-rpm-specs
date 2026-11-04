Name:           hiera
Version:        3.12.0
Release:        %autorelease
Summary:        A simple hierarchical database supporting plugin data sources

License:        Apache-2.0
URL:            https://github.com/puppetlabs/hiera
Source0:        https://downloads.puppetlabs.com/hiera/%{name}-%{version}.tar.gz
Source1:        https://downloads.puppetlabs.com/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        https://downloads.puppetlabs.com/puppet-gpg-signing-key-20250406.pub
# Use /etc/puppet rather than /etc/puppetlabs/puppet
Patch0:         fix-puppetlab-paths.patch
BuildArch:      noarch
BuildRequires:  openpgpverify
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(json)
BuildRequires:  ruby-devel

%description
A simple hierarchical database supporting plugin data sources.

%prep
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_vendorlibdir}
mkdir -p %{buildroot}%{_sysconfdir}/puppet
mkdir -p %{buildroot}%{_bindir}
cp -pr lib/hiera %{buildroot}%{ruby_vendorlibdir}
cp -pr lib/hiera.rb %{buildroot}%{ruby_vendorlibdir}
install -p -m0755 bin/hiera %{buildroot}%{_bindir}
install -p -m0644 ext/hiera.yaml %{buildroot}%{_sysconfdir}/puppet
mkdir -p %{buildroot}%{_sharedstatedir}/hiera

%check
rspec -Ilib spec

%files
%{_bindir}/hiera
%{ruby_vendorlibdir}/hiera.rb
%{ruby_vendorlibdir}/hiera
%dir %{_sharedstatedir}/hiera
%dir %{_sysconfdir}/puppet
%config(noreplace) %{_sysconfdir}/puppet/hiera.yaml
%doc COPYING README.md
%license LICENSE

%changelog
%autochangelog
