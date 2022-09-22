%global cowpathdir %{_sysconfdir}/cowsay/cowpath.d
%global pkgcowsdir %{_datadir}/%{name}/cows

Name:           cowsay-beefymiracle
Version:        1.0
Release:        %autorelease
Summary:        Cowsay file for the Beefy Miracle

License:        CC-BY-SA
URL:            http://rrix.fedorapeople.org/beefsay
Source0:        http://rrix.fedorapeople.org/beefsay/beefymiracle.cow

# 3.7.0-6 first shipped /etc/cowsay/cowpath.d/
BuildRequires:  cowsay >= 3.7.0-6
Requires:       cowsay >= 3.7.0-6

BuildArch:      noarch


%description
Provides a cowsay file for His Holiness the Beefy Miracle. It can be invoked
using cowsay -f beefymiracle, or aliased appropriately.


%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}


%build
cd %{name}-%{version}
echo "%{pkgcowsdir}" > %{name}.path
sed -e 's,/bin/env perl,/usr/bin/perl,g' %{SOURCE0} > beefymiracle.cow


%install
cd %{name}-%{version}
rm -rf %{buildroot}
install -d -m 0755              %{buildroot}%{cowpathdir}
install -p -m 0644 %{name}.path %{buildroot}%{cowpathdir}
install -d -m 0755                  %{buildroot}%{pkgcowsdir}
install -p -m 0644 beefymiracle.cow %{buildroot}%{pkgcowsdir}


%check
# Note: This does *not* check that our cowsdir is the same as the
#       cowsay package's cowsdir
export COWPATH=%{buildroot}%{pkgcowsdir}
echo "Installation (probably) successful" | cowsay -f beefymiracle


%files
%doc
%{cowpathdir}/%{name}.path
%{pkgcowsdir}/beefymiracle.cow


%changelog
%autochangelog
