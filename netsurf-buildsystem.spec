%global src_name buildsystem

Name:           netsurf-buildsystem
Version:        1.10
Release:        %autorelease
Summary:        Makefiles shared by NetSurf projects
License:        MIT
URL:            http://www.netsurf-browser.org/
Source0:        http://download.netsurf-browser.org/libs/releases/%{src_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators

%description
%{name} contains makefiles shared by NetSurf projects.

%prep
%autosetup -n %{src_name}-%{version} -p1

sed -i -e 1s@/bin/@/usr/bin/@ testtools/testrunner.pl
chmod +x testtools/testrunner.pl

%install
%make_install PREFIX=%{_prefix}

%files
%doc README
%license COPYING
%{_datadir}/%{name}/

%changelog
%autochangelog
